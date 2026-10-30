---
updated: "2026-06-11"
lang: fr
ref: kernel-u-net
permalink: /fr/kernel-u-net/
title: "Comprendre en profondeur le Kernel U-Net (KUN)"
lead: "KUN parcourt une série temporelle avec une structure symétrique en U, « du fin vers le grossier, puis du grossier vers le fin », en plaçant à chaque nœud un noyau interchangeable. Cette page démonte cette structure couche par couche : quel problème elle résout, ce que fait chaque couche, pourquoi elle est efficace, comment la prendre en main, et ce qui la distingue fondamentalement de DLinear et du Transformer."
prev: kun
math: true
---

> Cette page est le **développement** de la page [Les questions de pointe des séries temporelles en 2026](../kun/) : celle-ci expose clairement les défis auxquels KUN veut répondre ; la présente page détaille d'un seul tenant **l'idée, l'architecture couche par couche, la complexité et un tutoriel de prise en main** de KUN.

## En une phrase

**KUN (Kernel U-Net) = la forme hiérarchique du U-Net + des noyaux interchangeables.** Il transpose aux séries temporelles le schéma du [U-Net](../foundations/u-net/) issu de la segmentation d'images — « sous-échantillonnage dans l'encodeur, sur-échantillonnage dans le décodeur, connexions résiduelles (*skip connections*) » — et remplace la convolution fixe de chaque nœud par une petite fonction librement choisie : linéaire, [MLP](../foundations/mlp/) ou [attention](../foundations/attention/).

## Quel problème KUN veut-il résoudre ?

Comme on l'a vu dans [Les questions de pointe des séries temporelles en 2026](../kun/), la prévision à long horizon se heurte à deux contradictions incontournables :

1. **Le multi-échelle** — une série réelle superpose à la fois une tendance de long terme, des cycles de moyen terme et des détails haute fréquence de court terme, comme un mélange de plusieurs formes d'onde. Tout modèle qui ne regarde qu'une seule échelle est incomplet.
2. **Efficacité contre expressivité** — le [Transformer](../foundations/transformer/) capture les dépendances à longue portée grâce à l'auto-attention, mais sa complexité est en $O(L^2)$ et devient intenable dès que la séquence s'allonge ; à l'inverse, le modèle linéaire minimaliste (DLinear) est rapide et performant, mais peine à exprimer des structures complexes.

La réponse de KUN : **séparer naturellement les échelles grâce à une structure hiérarchique, et glisser librement entre « rapide » et « puissant » grâce à des noyaux interchangeables.**

## D'abord, bien voir qu'une série est « multi-échelle »

Pour comprendre pourquoi KUN a la forme d'un U, il faut d'abord voir une chose : **une série temporelle réelle cache souvent plusieurs « échelles » à la fois.**

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 380" role="img" aria-label="Une série décomposée en plusieurs échelles">
  <text x="12" y="40" fill="var(--muted)" font-size="13">Série brute</text>
  <text x="12" y="56" fill="var(--muted)" font-size="11">(ce que vous voyez)</text>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="175,72 222,58 269,66 316,44 363,58 410,36 457,50 504,28 551,44 598,22 645,36 690,16"/>
  <text x="430" y="116" fill="var(--muted)" font-size="13" text-anchor="middle">Décomposée = plusieurs échelles superposées ↓</text>
  <line x1="160" y1="128" x2="700" y2="128" stroke="var(--border)"/>

  <text x="12" y="178" fill="var(--accent)" font-size="13">Échelle grossière</text>
  <text x="12" y="194" fill="var(--muted)" font-size="11">tendance longue</text>
  <line x1="175" y1="200" x2="690" y2="200" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,190 269,180 363,164 457,146 551,130 645,114 690,106"/>

  <text x="12" y="262" fill="var(--accent-2)" font-size="13">Échelle moyenne</text>
  <text x="12" y="278" fill="var(--muted)" font-size="11">cycle</text>
  <line x1="175" y1="262" x2="690" y2="262" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,262 222,238 269,262 316,286 363,262 410,238 457,262 504,286 551,262 598,238 645,262 690,286"/>

  <text x="12" y="340" fill="#fbbf24" font-size="13">Échelle fine</text>
  <text x="12" y="356" fill="var(--muted)" font-size="11">détails HF</text>
  <line x1="175" y1="338" x2="690" y2="338" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="175,338 215,324 255,350 295,328 335,352 375,322 415,346 455,330 495,352 535,326 575,348 615,330 655,346 690,332"/>
</svg>
<figcaption class="figcap">Une même série superpose à la fois une tendance de long terme <strong>grossière</strong>, un cycle d'échelle <strong>moyenne</strong> et des fluctuations haute fréquence <strong>fines</strong>. Ne regarder qu'une seule de ces échelles donne une image incomplète — c'est ce que l'on veut dire en qualifiant une série de <strong>multi-échelle (<em>multi-scale</em>)</strong>.</figcaption>
</figure>

Le détail proche (demain sera un tout petit peu plus haut qu'aujourd'hui) et le contour lointain (sur l'année, la série monte globalement) sont deux informations de **granularité différente** : il faut les voir clairement chacune de son côté, puis les recombiner. C'est exactement ce que fait la forme en U de KUN : l'encodeur rend la série **plus grossière** couche après couche (d'abord les détails, puis le contour d'ensemble), et le décodeur reconstruit la prévision en la rendant **plus fine** couche après couche — toutes les échelles sont prises en compte en une seule passe.

## Idée centrale : pourquoi un U ?

En imagerie, le U-Net réduit d'abord l'image couche après couche pour en saisir le « contour global », puis l'agrandit couche après couche pour restituer les « détails locaux », en recousant les deux extrémités par des connexions résiduelles. Il en va de même pour les séries temporelles :

```
Fenêtre d'entrée (L pas)
   │  découpage en patchs (segments)
   ▼
[ Encodeur ]  patch → patch → patch → ⋯ → représentation latente   (sous-échantillonnage : moins d'unités, plus grossières, échelle plus large)
   │            │       │       │
   │          skip    skip    skip                  (connexions résiduelles : envoient les détails directement à la couche correspondante)
   ▼            ▼       ▼       ▼
[ Décodeur ]  patch ← patch ← patch ← ⋯ ← représentation latente   (sur-échantillonnage : reconstruction du grossier vers le fin)
   │
   ▼
Horizon de prévision (H pas)
```

**À chaque couche que l'on descend, l'échelle observée devient d'un cran plus grossière** : les couches peu profondes, proches de l'entrée, capturent les détails locaux et haute fréquence ; plus on descend, plus le contexte vu est long et grossier. Une série vit rarement à une seule échelle, et la forme en U les prend toutes en compte d'un coup.

## L'architecture, couche par couche

### 1. Découpage en patchs

L'entrée est une fenêtre de longueur $L$ à $C$ canaux (le nombre de variables), de forme $(L, C)$. KUN commence par la découper le long du temps en plusieurs **patchs (segments)**, qui forment les unités de la couche la plus fine.

### 2. Encodeur : sous-échantillonnage couche par couche

Chaque couche **agrège (*chunk*)** plusieurs patchs adjacents en une unité plus grossière ; la résolution temporelle diminue et les unités deviennent moins nombreuses :

$$\text{Encodeur :}\quad (L, C) \xrightarrow{\;k_1\;} (L/k_1,\, C') \xrightarrow{\;k_2\;} \cdots \xrightarrow{\;\;} (1,\, C_{\text{latent}})$$

où $k_l$ est le facteur de sous-échantillonnage de la couche $l$ (fixé par `patch_sizes`). Au plus profond, toute la séquence est comprimée en une **représentation latente** — qui encode l'information globale la plus grossière (par exemple « sur l'année, la série monte globalement »).

### 3. Décodeur : sur-échantillonnage couche par couche

Le décodeur est le miroir de l'encodeur : chaque couche **déploie (*expand*)** les unités grossières vers une résolution plus fine, jusqu'à reconstruire la longueur de prévision $H$ :

$$\text{Décodeur :}\quad (1,\, C_{\text{latent}}) \xrightarrow{\;\;} \cdots \xrightarrow{\;\;} (H,\, C)$$

### 4. Connexions résiduelles

La sortie de chaque couche de l'encodeur est reliée directement à la couche de même niveau du décodeur. Ainsi, lors de la reconstruction du grossier vers le fin, **les détails ne se perdent pas dans la compression** — c'est la connexion qui, dans le nom U-Net, « saute le milieu et relie les deux extrémités ».

### 5. Sortie multiple directe

KUN **produit tout l'horizon de prévision en une seule fois** (*direct multi-output*), au lieu de prédire un pas puis de le réinjecter pour prédire le suivant. On évite ainsi **l'accumulation d'erreurs** de la prévision récursive — plus on avance dans l'horizon, plus l'erreur d'une approche récursive fait boule de neige.

## La clé qui lui donne son nom : des noyaux interchangeables

La forme en U est le squelette ; **le noyau (*kernel*) est l'âme de KUN**. À chaque nœud du U, l'opération qui « transforme un groupe de segments en un autre » n'est pas une convolution figée, mais un **module que l'on peut remplacer d'un bloc**, $\mathcal{K}_l$ :

$$\text{Couche } l \text{ :}\quad \mathbf{z}_{l+1} = \mathcal{K}_l(\mathbf{z}_l)$$

### Un squelette fixe, des noyaux interchangeables

KUN découpe un modèle en deux parties :

- **Le squelette** décide comment découper, réduire et reconstruire : découpage en patchs, sous-échantillonnage couche par couche, suréchantillonnage symétrique, connexions résiduelles (*skip connections*) et sortie multi-horizon directe. Cette partie est la même pour tous les modèles et ne s'écrit qu'une fois.
- **Le noyau** ne fait qu'une chose : à son niveau, transformer un groupe de segments en un autre.

Entre les deux, un seul contrat : le noyau reçoit une entrée de forme (segments, canaux) et renvoie une sortie de la forme convenue. Tout réseau qui respecte cette interface peut être placé à n'importe quel niveau du U. Ainsi :

> **Construire un nouveau modèle = écrire un nouveau noyau**, sans concevoir une nouvelle architecture de zéro. Le nouveau noyau hérite automatiquement de la structure multi-échelle, des connexions résiduelles et de la sortie multi-horizon directe qu'apporte le squelette.

### Changer de noyau, c'est obtenir un nouveau modèle

| Noyaux par niveau | Modèle obtenu | Caractéristiques |
|-------------------|---------------|------------------|
| **Linéaire** partout | Modèle linéaire hiérarchique | Coût minime, $O(L)$ ; même esprit que DLinear, une base de référence rapide et solide |
| **[MLP](../foundations/mlp/)** partout | MLP hiérarchique | Ajoute une dose modérée de non-linéarité |
| Linéaire en surface, **[attention](../foundations/attention/)** en profondeur | Modèle hybride | L'attention ne voit que la séquence courte issue du sous-échantillonnage : le coût reste maîtrisé |
| **LSTM / convolution** | RNN / CNN hiérarchique | Réutilise tels quels les opérateurs classiques |
| **Un noyau que vous écrivez vous-même** (modèle d'espace d'états, MoE, opérateur de Fourier…) | Votre nouveau modèle | Vous n'écrivez que le noyau ; le squelette est déjà prêt |

Le fichier [`kun_lib_v2.py`](https://github.com/JiangYou2025/kun/blob/main/notebooks/kun_lib_v2.py) du dépôt fournit déjà quatre noyaux : linear, conv, lstm et transformer. Chaque niveau peut utiliser un noyau différent, et vous pouvez y mêler vos propres noyaux.

### Écrire son propre noyau

Un noyau n'est qu'un petit module qui hérite de `Kernel` : le constructeur reçoit les formes et nombres de canaux d'entrée et de sortie, et `forward` réalise la transformation. Voici un GRU transformé en noyau, en une douzaine de lignes :

```python
import torch.nn as nn
from math import prod
from kun_lib_v2 import Kernel

class GRUKernel(Kernel):
    """Exemple : un GRU comme noyau"""
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.rnn = nn.GRU(input_dim, output_dim, batch_first=True)
        self.resize = nn.Linear(prod(input_shape), prod(output_shape))

    def forward(self, x):                       # (..., *input_shape, input_dim)
        x = x.reshape(-1, prod(self.input_shape), self.input_dim)
        h, _ = self.rnn(x)                      # (batch, nb_segments, output_dim)
        h = self.resize(h.transpose(1, 2)).transpose(1, 2)   # nb_segments -> nb_segments cible
        return h.reshape(-1, *self.output_shape, self.output_dim)

# noyaux linéaires intégrés pour les deux premiers niveaux, votre propre noyau GRU au plus profond (longueur de la liste = nombre de niveaux)
kernel = ["linear", "linear", GRUKernel]
```

**L'essentiel** : on teste de nouvelles idées et on arbitre entre calcul et précision en **changeant de noyau**, et non en réécrivant le modèle. « Concevoir un nouveau modèle » devient « remplacer le $\mathcal{K}_l$ d'une couche ». De plus, les noyaux profonds opèrent sur une **séquence déjà sous-échantillonnée, donc raccourcie** : même avec de l'attention, le coût reste bien inférieur à celui d'une auto-attention en $O(L^2)$ appliquée directement à la longue séquence brute.

## Complexité : pourquoi O(L) ?

| Caractéristique | DLinear | Transformer | **KUN** |
|------|---------|-------------|---------|
| Multi-échelle | ✗ | Partiel (patchs) | ✓ Hiérarchie native |
| Interprétabilité | Tendance + saisonnalité | Cartes d'attention | Chaque couche correspond à une échelle |
| Noyau / opérateur | Linéaire uniquement | Attention uniquement | Linéaire / MLP / attention **au choix** |
| Complexité | $O(L)$ | $O(L^2)$ | $O(L)$ (noyau linéaire) |
| Connexions résiduelles | ✗ | ✗ | ✓ Préservent les détails |
| Sortie multi-pas | Directe | Directe / récursive | Sortie multiple directe |

Le sous-échantillonnage hiérarchique **raccourcit géométriquement** la séquence à chaque couche ; ainsi, même si les couches profondes utilisent des noyaux plus lourds, le coût total reste maîtrisé. Sur les tâches multivariées à long horizon, KUN obtient ainsi à la fois « l'efficacité d'un modèle linéaire » et « une expressivité proche de celle des modèles à attention ».

## Philosophie de conception : c'est aux données de décider de la complexité

Le jugement qui sous-tend KUN rejoint la tendance de la dernière décennie (voir le [chapitre 10 de l'histoire](../history/10/)) : **la complexité d'un modèle doit être dictée par les données, et non par un pari d'emblée sur l'architecture la plus lourde.**

- Données simples → noyaux linéaires partout : KUN se réduit à un modèle linéaire hiérarchique efficace ;
- Données complexes → on place des noyaux d'attention aux niveaux qui en ont besoin, pour ajouter de la capacité à la demande.

Unifier « modélisation hiérarchique » et « choix flexible du noyau » dans un même cadre symétrique — voilà l'exploration que propose KUN, à l'ère des grands modèles, en faveur d'une **conception structurée et efficace**.

## Tutoriel pas à pas : prévoir avec KUN
{: #tutoriel-pas-a-pas}

> **À propos de l'API.** Les extraits de code ci-dessous montrent la *forme* d'un flux d'entraînement typique, pour que vous puissiez l'adapter à la véritable interface de KUN dans ce dépôt. Une fois le code officiellement publié, remplacez les chemins d'import, les noms de classes et les noms de paramètres par ceux du code réel. Considérez-le comme un modèle, et non comme du code à copier-coller et exécuter tel quel.

### 1. Récupérer le code et l'installer

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # ou : pip install -e .
```

### 2. Préparer les données

KUN attend le format à fenêtre glissante présenté dans la page [Séries temporelles](../time-series/) : une entrée de longueur `L` (la fenêtre passée), associée à une sortie de longueur `H` (l'horizon), sur `C` canaux (variables).

```python
# x : tableau de forme (n_échantillons, L, C)  -> fenêtre passée
# y : tableau de forme (n_échantillons, H, C)  -> cible à prédire
```

Veillez à **normaliser canal par canal** (soustraire la moyenne et diviser par l'écart-type calculés sur l'ensemble d'entraînement) et à **découper selon le temps**.

### 3. Configurer le modèle

```python
from kun import KernelUNet            # à remplacer par le vrai chemin d'import

model = KernelUNet(
    input_len=336,     # L — fenêtre passée
    pred_len=96,       # H — horizon de prévision
    n_channels=7,      # C — nombre de variables
    patch_sizes=[16, 8, 4],   # façon de découper la séquence à chaque niveau
    kernel="linear",          # "linear" | "mlp" | "attention" — noyau de chaque couche
)
```

Commencez avec `kernel="linear"` et un horizon court. L'entraînement prend quelques secondes et vous donne une base de référence à battre — c'est précisément la discipline sur laquelle insiste la page [Comment prévoir](../forecasting/).

### 4. Entraîner

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.L1Loss()          # MAE — robuste et interprétable

for epoch in range(50):
    for xb, yb in train_loader:
        opt.zero_grad()
        pred = model(xb)             # (batch, H, C)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.step()
```

### 5. Évaluer et prévoir

```python
model.eval()
with torch.no_grad():
    pred = model(x_test)             # prévoir l'horizon mis de côté
mae = (pred - y_test).abs().mean()
print("MAE sur l'ensemble de test :", mae.item())
```

Comparez ce chiffre à la **base de référence naïve saisonnière**. Si KUN l'emporte, vous tenez un modèle réellement utile ; sinon, revérifiez vos fenêtres, votre normalisation et votre découpage.

## Un ordre de réglage raisonnable

1. **Longueur de la fenêtre passée `L`** — un contexte plus long aide généralement pour les longs horizons, mais jusqu'à un certain point.
2. **Taille des patchs** — plus il y a de niveaux, plus la hiérarchie est marquée ; faites en sorte, autant que possible, que chaque taille de patch divise la longueur de son niveau.
3. **Choix du noyau** — ne passez de `linear` → `mlp` → `attention` que si l'erreur de validation prouve que le surcoût en vaut la peine.
4. **Taux d'apprentissage et nombre d'époques** — arrêt précoce fondé sur la MAE de validation.

## Pour aller plus loin

- **Pour passer à la pratique** : voir le [tutoriel pas à pas](#tutoriel-pas-a-pas) ci-dessus, en commençant par une base de référence à noyau linéaire et horizon court.
- **Pour consolider d'abord les bases de référence** : relisez [Comment prévoir](../forecasting/) — KUN n'a de sens que par rapport à une base de référence.
- **Pour situer KUN dans l'histoire des méthodes** : lisez le [chapitre 10 de l'histoire · Grands modèles, régression linéaire et Kernel U-Net](../history/10/).
- **Pour une perspective de cours** : voir la [leçon 11 · Kernel U-Net](../course/11/), qui compare N-BEATS, DLinear et KUN.
- **Pour lire le code source ou poser une question** : le [dépôt GitHub](https://github.com/JiangYou2025/kun).

<div class="note">
  <strong>Citer KUN.</strong> Si KUN vous a été utile pour vos recherches ou votre produit, merci de citer les travaux de Jiang You sur le Kernel U-Net et d'ajouter un lien vers ce dépôt.
</div>
