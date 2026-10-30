---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/svm/
title: "SVM (machines à vecteurs de support)"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

Le **SVM (machine à vecteurs de support, Support Vector Machine)** est une méthode de classification (qui peut aussi faire de la régression) dont l'idée centrale est de trouver, entre deux classes de données, la frontière dont la **marge est maximale** ; grâce à l'**astuce du noyau**, il traite en outre sans peine les problèmes non linéaires.

## Intuition

Supposons qu'il y ait dans le plan deux tas de points, l'un rouge, l'autre bleu, et que vous deviez tracer une droite pour les séparer. Il existe une infinité de droites qui conviennent — mais laquelle est « la meilleure » ?

La réponse du SVM : **celle dont les deux classes sont aussi éloignées que possible**. Concrètement, imaginez qu'on construise entre les deux classes la **rue (street) la plus large possible** : la ligne médiane de la rue est la frontière de décision, et la largeur de la rue est la **marge (margin)**. Plus la rue est large, plus le modèle a de « réserve » pour juger de nouvelles données, et meilleure est sa capacité de **[généralisation](../generalization/)**.

Or ce qui détermine réellement la largeur et la position de cette rue, ce sont seulement les quelques **points collés au bord de la rue** — on les appelle les **vecteurs de support (support vectors)**. Les autres points, plus éloignés, peuvent bouger sans changer le résultat. C'est l'origine du nom SVM, et l'une de ses grandes caractéristiques : **le modèle n'est déterminé que par un petit nombre d'échantillons clés**.

## Principe : la marge maximale

Soit la frontière de décision (un hyperplan)

$$w^\top x + b = 0$$

Pour un point $x$, le signe de $w^\top x + b$ indique de quel côté de la frontière il se trouve. On peut montrer que la **marge** entre les deux bords vaut

$$\text{margin} = \frac{2}{\|w\|}$$

Rendre la marge **maximale** revient à rendre $\|w\|$ **minimale**. L'objectif d'optimisation du SVM s'écrit alors sous une forme élégante :

$$\min_{w,b}\ \frac{1}{2}\|w\|^2 \quad \text{s.t.}\quad y_i\,(w^\top x_i + b) \ge 1,\ \forall i$$

Ici $y_i \in \{-1, +1\}$ est l'étiquette de classe. La contrainte $y_i(w^\top x_i + b)\ge 1$ signifie que « chaque point doit rester du bon côté de la rue, et au-delà de son bord ». Les points qui **tombent exactement sur le bord** (où l'égalité est atteinte) sont les **vecteurs de support**.

## Marge souple et paramètre C

Les données réelles sont souvent bruitées et se chevauchent ; exiger à tout prix que « tous les points soient bien classés » rend la marge très étroite, voire le problème insoluble. On introduit donc une **marge souple (soft margin)** : on autorise quelques points à franchir la limite, mais en leur faisant payer un coût. L'objectif devient

$$\min_{w,b}\ \frac{1}{2}\|w\|^2 + C\sum_i \xi_i$$

où $\xi_i \ge 0$ est la « **variable d'écart** » de chaque point, qui mesure de combien il dépasse ; $C$ est le **coefficient de pénalité (paramètre de [régularisation](../regularization/))**, qui règle le compromis :

- **C grand** → les dépassements sont fortement pénalisés → on cherche à bien classer chaque point → marge étroite, risque de **[surapprentissage](../overfitting/)** ;
- **C petit** → on tolère davantage de dépassements → marge large, plus robuste, mais risque de **sous-apprentissage**.

$C$ arbitre donc essentiellement entre « largeur de la marge » et « erreurs de classification » ; c'est un hyperparamètre clé qu'il faut absolument régler.

## L'astuce du noyau (kernel trick)

Et si les données ne peuvent tout simplement pas être séparées par une droite ? L'arme secrète du SVM est l'**astuce du noyau** : projeter les données **implicitement** dans un espace de dimension plus élevée, où elles deviennent peut-être linéairement séparables — **sans jamais calculer réellement les coordonnées en grande dimension** : il suffit d'une **fonction noyau (kernel)** $K(x_i, x_j)$ qui remplace le produit scalaire dans cet espace. Noyaux courants :

- **Noyau linéaire** : $K(x, x') = x^\top x'$, c'est le SVM linéaire ordinaire.
- **Noyau polynomial** : $K(x, x') = (x^\top x' + c)^d$, qui permet d'ajuster des frontières de forme polynomiale.
- **Noyau RBF (gaussien)** : $K(x, x') = \exp(-\gamma\|x - x'\|^2)$, le plus utilisé et le plus souple. $\gamma$ règle le « rayon d'influence » de chaque point : $\gamma$ grand → influence restreinte, frontière sinueuse, surapprentissage facile ; $\gamma$ petit → frontière lisse.

Pour la régression, on utilise la **SVR (régression à vecteurs de support)** : l'idée est symétrique — au lieu de chercher « aucun point dans la marge », on autorise les prédictions à tomber dans un « tube » de largeur $\varepsilon$ autour de la vraie valeur, et on ne pénalise que les points qui en sortent.

## Un exemple concret (sklearn)

```python
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=200, noise=0.2, random_state=0)  # données non linéaires

# Standardiser d'abord, puis SVM à noyau RBF — la standardisation est cruciale pour le SVM
clf = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1.0, gamma="scale")   # C et gamma sont les hyperparamètres clés
)
clf.fit(X, y)

print("Exactitude :", clf.score(X, y))
print("Nombre de vecteurs de support :", clf.named_steps["svc"].n_support_)
```

Il faut impérativement commencer par une **mise à l'échelle des variables (StandardScaler)** : les fonctions noyaux (surtout RBF) reposent sur les distances entre échantillons, et des unités hétérogènes font que les variables de grande valeur « noient » les autres.

## Pourquoi c'est important (où l'utiliser)

- Très performant sur des données **de taille petite ou moyenne et de grande dimension** — classification de textes, bio-informatique : ces situations où « les variables sont nombreuses et les échantillons pas si nombreux » ont longtemps été le terrain de prédilection du SVM.
- La **marge maximale** assure une bonne généralisation et une certaine robustesse au bruit.
- L'astuce du noyau lui permet de capturer des relations **non linéaires** complexes sans augmenter explicitement la dimension.
- Il appartient à une autre [famille de modèles](../model-families/) que les [arbres de décision](../decision-tree/) ou l'[apprentissage ensembliste / GBDT](../ensemble-gbdt/) ; chacun excelle sur certains types de données, et il vaut la peine de les comparer.

## Intérêt pour la prévision de séries temporelles

En séries temporelles, on peut prévoir avec une **SVR sur des variables retardées** : on prend les valeurs passées $y_{t-1}, \dots, y_{t-p}$ comme entrées pour prédire $y_t$. Par rapport à une autorégression linéaire, une SVR à noyau RBF capture les **relations non linéaires** entre variables retardées. Points pratiques :

- **Mettez impérativement les variables à l'échelle** — pour le SVM/la SVR, ce n'est pas une option, c'est une nécessité.
- **Le choix du noyau** détermine la complexité des motifs que l'on peut exprimer ; RBF est le premier choix par défaut.
- **Régler C et gamma est absolument crucial**, généralement par recherche en grille avec [validation croisée](../cross-validation/) ; mal réglé, le modèle sur-apprend ou sous-apprend très facilement.
- Attention : le SVM est **lent sur de gros volumes de données** (la complexité d'entraînement croît à peu près comme le carré du nombre d'échantillons, voire plus) ; quand les données sont très nombreuses, l'[apprentissage ensembliste / GBDT](../ensemble-gbdt/) est souvent à la fois rapide et précis, et constitue un choix plus pratique.

## Résumé

- **SVM = trouver l'hyperplan séparateur à marge maximale** : $w^\top x + b = 0$, marge $=\frac{2}{\|w\|}$, maximiser la marge ⇔ minimiser $\frac12\|w\|^2$.
- Les **vecteurs de support** sont les échantillons clés collés au bord de la marge ; ils déterminent à eux seuls le modèle.
- **Marge souple + paramètre C** : compromis entre « largeur de la marge » et « erreurs de classification ».
- **Astuce du noyau** (linéaire / polynomial / RBF) : montée en dimension implicite pour traiter le non-linéaire ; la version régression est la **SVR**.
- Adapté aux données de taille petite ou moyenne et de grande dimension ; en séries temporelles, on peut utiliser une **SVR sur des variables retardées**, à condition de **mettre les variables à l'échelle et de bien régler C et gamma** ; sur de gros volumes, il est moins efficace que le [GBDT](../ensemble-gbdt/).

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
