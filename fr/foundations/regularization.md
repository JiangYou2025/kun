---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/regularization/
title: "Régularisation"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

La **régularisation** consiste à **ajouter des contraintes ou des pénalités supplémentaires** pendant l'entraînement d'un modèle afin d'en limiter la complexité, ce qui réduit le **surapprentissage** et améliore la capacité de **[généralisation](../generalization/)**. En une phrase : empêcher le modèle de n'en faire qu'à sa tête, et lui faire apprendre quelque chose de plus simple et de plus stable.

## Intuition

Rappelons l'essence du surapprentissage : pour coller parfaitement aux données d'entraînement, le modèle pousse ses poids vers des valeurs énormes et bizarres, et finit par mémoriser une foule de bruit. L'idée centrale de la régularisation est de **passer une bride au modèle** :

> **Ajuster les données tout en gardant les poids aussi petits, et le modèle aussi simple, que possible.**

Derrière cette idée se trouve le **rasoir d'Ockham** (*Occam's razor*) : à pouvoir explicatif comparable, le modèle le plus simple a le plus de chances d'être juste, et aussi de bien généraliser.

Une analogie : on vous demande de faire passer une courbe à travers un nuage de points.

- Sans contrainte : vous pouvez tracer une courbe qui se tord violemment pour passer par chaque point (poids énormes, surapprentissage).
- Avec régularisation : c'est comme si quelqu'un vous rappelait « ne fais pas des virages aussi serrés » ; vous tracez alors une courbe lisse qui saisit la tendance générale et qui, au final, prédit mieux les nouveaux points.

Voir [Surapprentissage](../overfitting/).

## Formulation mathématique

Un entraînement ordinaire ne minimise que la [perte](../loss-function/) sur les données. La régularisation **ajoute un terme de pénalité** à la fonction objectif :

$$\min_{w}\;\; \underbrace{\frac{1}{n}\sum_{i=1}^{n} L\big(y_i, f(x_i)\big)}_{\text{ajuster les données}} \;+\; \underbrace{\lambda\, \Omega(w)}_{\text{pénaliser la complexité}}$$

- $\Omega(w)$ est le **terme de pénalité de complexité**, en général une certaine « taille » des poids. Plus les poids sont grands, plus la pénalité est lourde.
- $\lambda \ge 0$ est l'**intensité de régularisation** (*regularization strength*) ; elle arbitre le bras de fer entre deux forces :
  - $\lambda \to 0$ : presque aucune pénalité, on revient à l'ajustement ordinaire, avec un risque de **surapprentissage**.
  - $\lambda$ très grand : les poids sont écrasés à tout prix, le modèle devient trop simple et risque le **sous-apprentissage**.
  - Un $\lambda$ bien choisi : un équilibre entre ajustement et simplicité. $\lambda$ est un hyperparamètre à régler à l'aide d'un **ensemble de validation / de la [validation croisée](../cross-validation/)**.

## Quelques régularisations courantes

Des choix différents de $\Omega(w)$ donnent des régularisations différentes.

**L2 / régression ridge (Ridge)** : pénalise la somme des carrés des poids

$$\Omega(w) = \|w\|_2^2 = \sum_j w_j^2$$

La L2 rend tous les poids **globalement plus petits et plus lisses**, mais ne les ramène généralement pas exactement à 0. Elle est particulièrement efficace contre la colinéarité et pour stabiliser le modèle ; on l'appelle aussi souvent **décroissance des poids** (*weight decay*).

**L1 / Lasso** : pénalise la somme des valeurs absolues des poids

$$\Omega(w) = \|w\|_1 = \sum_j |w_j|$$

Ce qu'a de remarquable la L1, c'est qu'elle **ramène une partie des poids exactement à 0**, effectuant ainsi automatiquement une **sélection de variables** (*feature selection*) : les variables sans importance sont purement et simplement éjectées du modèle, ce qui donne une solution **parcimonieuse** (*sparse*).

Pourquoi la L1 peut-elle « mettre à zéro » et pas la L2 ? Regardons l'intuition géométrique. L'optimisation revient à chercher, à l'intérieur de la région délimitée par le « budget de pénalité », le point de perte minimale :

- La région de contrainte de la L2 est un **cercle** (une boule en grande dimension) ; sa surface est lisse, et lorsque les lignes de niveau de la perte la touchent, c'est en général en une position oblique où toutes les composantes sont non nulles.
- La région de contrainte de la L1 est un **losange** (en grande dimension, un polytope à sommets pointus), dont **les sommets se trouvent précisément sur les axes de coordonnées**. Quand les lignes de niveau de la perte s'étendent vers l'extérieur, elles touchent le plus facilement ces sommets en premier ; or, en un sommet, certaines coordonnées valent exactement 0 — les poids correspondants sont donc ramenés à 0.

**Elastic Net (réseau élastique)** : additionne L1 et L2

$$\Omega(w) = \alpha\|w\|_1 + (1-\alpha)\|w\|_2^2$$

Elle combine la parcimonie de la L1 et la stabilité de la L2, et donne souvent de meilleurs résultats lorsque les variables sont nombreuses et corrélées entre elles.

## Au-delà du terme de pénalité : d'autres techniques de régularisation

Au sens large, la régularisation désigne toute technique qui « contraint le modèle et l'empêche d'apprendre le bruit par cœur » :

- **[Arrêt précoce](../early-stopping/)** (*early stopping*) : on surveille l'erreur de validation et l'on arrête l'entraînement dès qu'elle remonte, pour éviter que le surapprentissage ne s'aggrave à force d'entraînement.
- **[Dropout](../dropout/)** : pendant l'entraînement d'un [réseau de neurones](../neural-network/), on « abandonne » aléatoirement une partie des [neurones](../neuron/), ce qui force le réseau à ne pas dépendre d'unités isolées et à apprendre des représentations plus robustes.
- **Élagage / limitation de la profondeur** (*tree pruning* / `max_depth`) : pour un [arbre de décision](../decision-tree/), on limite la profondeur maximale ou l'on coupe les branches inutiles, afin que l'arbre ne grandisse pas jusqu'à mémoriser chaque échantillon.
- **Augmentation de données** (*data augmentation*) : on applique aux données des transformations raisonnables (rotation, ajout de bruit, etc.) pour enrichir artificiellement l'ensemble d'entraînement, ce qui revient à dire au modèle « ces variations n'ont pas d'importance ».
- **Décroissance des poids** (*weight decay*) : pendant l'entraînement, on fait diminuer continuellement les poids ; c'est essentiellement équivalent à une régularisation L2.

## Un exemple concret (sklearn)

Voyons concrètement avec Ridge et Lasso que **augmenter $\alpha$ (c'est-à-dire $\lambda$) tire les coefficients vers de petites valeurs**.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso

rng = np.random.RandomState(0)
X = rng.randn(100, 5)
# La vraie relation ne dépend que des deux premières variables ; les trois dernières sont du bruit
y = 3 * X[:, 0] - 2 * X[:, 1] + 0.1 * rng.randn(100)

for alpha in [0.0, 0.1, 1.0, 10.0]:
    ridge = Ridge(alpha=alpha).fit(X, y)
    print(f"Ridge alpha={alpha:>4}: {np.round(ridge.coef_, 2)}")

for alpha in [0.001, 0.05, 0.2, 1.0]:
    lasso = Lasso(alpha=alpha).fit(X, y)
    print(f"Lasso alpha={alpha:>5}: {np.round(lasso.coef_, 2)}")
```

Vous observerez :

- **Ridge** : à mesure que `alpha` augmente, tous les coefficients **rétrécissent globalement**, mais deviennent rarement exactement nuls.
- **Lasso** : à mesure que `alpha` augmente, les **coefficients des variables inutiles tombent à 0 l'un après l'autre**, jusqu'à ne laisser que les deux premières, réellement importantes — c'est la sélection automatique de variables.

{% include fviz/reg-path.html %}

## Pourquoi c'est important : le lien avec le surapprentissage et le compromis biais–variance

La régularisation est l'arme la plus directe et la plus utilisée contre le [surapprentissage](../overfitting/). Dans le langage du [compromis biais–variance](../bias-variance/) :

> **La régularisation introduit délibérément un tout petit peu de biais en échange d'une forte baisse de la variance.**

- Sans régularisation : le modèle a une variance élevée et réagit de façon excessive au bruit des données d'entraînement (surapprentissage).
- Avec régularisation : le modèle devient plus simple et plus stable, la variance baisse ; le biais augmente légèrement, mais **l'erreur de généralisation totale est plus faible**.

Régler $\lambda$ revient donc, au fond, à chercher entre biais et variance le point idéal où l'erreur de généralisation est minimale. Voir [Généralisation](../generalization/).

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, on construit souvent un grand nombre de **variables retardées** (*lag features*) : on utilise les valeurs aux instants $t-1, t-2, \dots, t-k$ pour prédire $t$. Cela pose deux problèmes :

- **Des variables nombreuses et corrélées** : les retards voisins sont fortement colinéaires, si bien qu'un [modèle linéaire](../linear-model/) surapprend facilement et prend les fluctuations accidentelles du passé pour des régularités.
- **Beaucoup de bruit** : les séries temporelles réelles sont très bruitées, et un modèle non contraint se met facilement à ajuster le bruit plutôt que la tendance.

La régularisation est ici particulièrement utile :

- **L2 / Ridge** stabilise les coefficients, atténue la colinéarité entre variables retardées et rend les prévisions plus lisses.
- **L1 / Lasso** **sélectionne automatiquement les retards réellement importants** — elle peut par exemple vous indiquer que seuls $t-1$ et $t-7$ (la veille et le même jour de la semaine précédente) sont utiles, en annulant les coefficients des autres retards : le modèle est plus concis, plus interprétable et moins sujet au surapprentissage.

En une phrase : dans une série temporelle riche en variables retardées et en bruit, la régularisation vous aide à **apprendre les régularités sans mémoriser le bruit**.

## En résumé

- La **régularisation** limite la complexité du modèle en ajoutant des contraintes ou des pénalités, afin de réduire le **surapprentissage** et d'améliorer la **généralisation**.
- Fonction objectif centrale : $\min_w \frac1n\sum L + \lambda\,\Omega(w)$ ; **plus $\lambda$ est grand, plus le modèle est simple**, et il se règle sur un ensemble de validation.
- **L2/Ridge** rétrécit les poids en douceur ; **L1/Lasso** produit des solutions parcimonieuses et sélectionne les variables (les sommets du losange de contrainte sont sur les axes) ; **Elastic Net** combine les deux.
- La régularisation au sens large comprend aussi l'**arrêt précoce, le Dropout, l'élagage/la limitation de profondeur, l'augmentation de données et la décroissance des poids**.
- Sous l'angle biais–variance : la régularisation **échange un peu de biais contre une forte baisse de variance**.
- Dans les séries temporelles, elle permet de dompter les nombreuses **variables retardées** et d'éviter d'ajuster le bruit ; la **L1** aide en outre à repérer les retards clés.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
