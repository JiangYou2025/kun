---
updated: "2026-05-31"
lang: fr
ref: kun
permalink: /fr/kun/
title: "Utiliser KUN — Kernel U-Net"
lead: "KUN (Kernel U-Net) est une architecture hiérarchique et symétrique pour la prévision multivariée de séries temporelles à long horizon. Cette page explique l'idée qui la sous-tend et donne une recette pas à pas pour l'exécuter sur vos données."
prev: forecasting
math: true
---

## L'idée en une image

KUN emprunte sa forme au **U-Net** utilisé en segmentation d'images : un **encodeur** qui compresse progressivement l'entrée, et un **décodeur symétrique** qui la dilate progressivement vers une prédiction, l'information circulant entre les niveaux correspondants.

```
fenêtre d'entrée
   │  découpée en patches
   ▼
[ Encodeur ]  patch → patch → patch       (sous-échantillonnage : moins d'unités, plus grossières)
   │             │      │       │
   │          skip   skip    skip          (les niveaux correspondants sont reliés)
   ▼             ▼      ▼       ▼
[ Décodeur ]  patch ← patch ← patch       (sur-échantillonnage : on reconstruit la résolution)
   │
   ▼
horizon de prévision
```

La particularité qui donne son nom à KUN : à chaque nœud du U, l'opération est un **noyau (kernel) interchangeable**, et non une convolution fixe. Un noyau n'est qu'une petite fonction qui transforme un segment en un autre — ce peut être une **couche linéaire, un MLP, un RNN ou un bloc d'attention**. Vous choisissez le noyau par niveau, si bien que le même squelette peut être rendu léger ou expressif selon vos données.

## Pourquoi cette conception fonctionne

- **La hiérarchie épouse le temps.** Les courts patches près de l'entrée capturent le détail local à haute fréquence ; les niveaux plus profonds voient un contexte plus long et plus grossier. Une série vit rarement à une seule échelle, et le U en capture plusieurs à la fois.
- **La symétrie garde l'efficacité.** Comme le décodeur reflète l'encodeur, le modèle reconstruit un horizon complet sans explosion quadratique en longueur — un avantage sur les Transformers classiques pour les longues séquences.
- **Les noyaux apportent la souplesse.** Les noyaux linéaires offrent une référence rapide et solide (dans l'esprit de DLinear) ; les noyaux d'attention ajoutent de la capacité là où les données l'exigent. On arbitre calcul/précision en échangeant des noyaux, sans réécrire le modèle.
- **Multi-sortie directe.** KUN prédit tout l'horizon d'un coup, évitant l'accumulation d'erreurs de la prévision récursive.

## Pas à pas : prévoir avec KUN

> **Note sur l'API.** Les extraits ci-dessous montrent la *forme* d'un pipeline d'entraînement typique afin que vous l'adaptiez à l'interface réelle de KUN dans ce dépôt. Remplacez le chemin d'import, le nom de la classe et les noms d'arguments par ceux du code une fois publiés. Considérez-le comme un gabarit, pas comme du code prêt à copier-coller.

### 1. Récupérer le code et l'installer

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # ou : pip install -e .
```

### 2. Mettre en forme les données

KUN attend le format à fenêtre glissante de la page [Séries temporelles](./../time-series/) : une entrée de longueur `L` (rétrospection) vers une sortie de longueur `H` (horizon), avec `C` canaux (variables).

```python
# x : tableau de forme (n_échantillons, L, C)  -> les fenêtres de rétrospection
# y : tableau de forme (n_échantillons, H, C)  -> les cibles à prédire
```

Normalisez toujours **par canal** (soustraire la moyenne d'entraînement, diviser par l'écart-type d'entraînement) et **découpez selon le temps**.

### 3. Configurer le modèle

```python
from kun import KernelUNet            # à adapter à l'import réel

model = KernelUNet(
    input_len=336,     # L — fenêtre de rétrospection
    pred_len=96,       # H — horizon de prévision
    n_channels=7,      # C — nombre de variables
    patch_sizes=[16, 8, 4],   # comment chaque niveau découpe la séquence
    kernel="linear",          # "linear" | "mlp" | "attention" — noyaux par niveau
)
```

Commencez par `kernel="linear"` et un horizon court. Il s'entraîne en quelques secondes et vous donne la référence à dépasser — exactement la discipline de la page [Comment prévoir](./../forecasting/).

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
    pred = model(x_test)             # prévoir l'horizon réservé
mae = (pred - y_test).abs().mean()
print("MAE de test :", mae.item())
```

Comparez ce nombre à la **référence naïve saisonnière**. Si KUN gagne, vous tenez un vrai modèle ; sinon, revoyez vos fenêtres, votre normalisation et votre découpage.

## Un ordre de réglage raisonnable

1. **Rétrospection `L`** — un contexte plus long aide généralement les longs horizons, jusqu'à un certain point.
2. **Tailles de patch** — plus de niveaux = plus de hiérarchie ; gardez chaque taille de patch diviseur de la longueur du niveau.
3. **Choix du noyau** — passez de `linear` → `mlp` → `attention` seulement si l'erreur de validation justifie le surcoût.
4. **Taux d'apprentissage et époques** — utilisez l'arrêt précoce sur le MAE de validation.

## Pour aller plus loin

- Relisez [Comment prévoir](./../forecasting/) et lancez d'abord les références — KUN n'a de sens que par rapport à elles.
- Ouvrez une issue ou lisez le code source sur [GitHub](https://github.com/JiangYou2025/kun) pour connaître l'API exacte et actuelle.

<div class="note">
  <strong>Citer KUN.</strong> Si KUN aide votre recherche ou votre produit, merci de citer les travaux Kernel U-Net de Jiang You et de renvoyer vers ce dépôt.
</div>
