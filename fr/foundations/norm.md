---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/norm/
title: "Normes"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)

Une norme est une fonction qui mesure la « **longueur / taille** » d'un vecteur. Un même vecteur a des « longueurs » différentes selon la norme utilisée ; en apprentissage automatique, les plus courantes sont $\ell_1$ et $\ell_2$, qui sont aussi des outils centraux de la [régularisation](../regularization/) et de la mesure des distances.

## Intuition

« À quelle distance est le bureau de chez moi ? » La réponse dépend de la façon dont vous vous déplacez :

- à vol d'oiseau ($\ell_2$, distance euclidienne) ;
- en suivant des rues qui se croisent à angle droit ($\ell_1$, distance de Manhattan / du taxi) ;
- en ne considérant que la direction dans laquelle vous allez le plus loin ($\ell_\infty$).

La norme formalise la notion intuitive de « taille / distance » en admettant plusieurs façons raisonnables de la mesurer. Elle indique aussi « à quel point un vecteur est parcimonieux, à quel point il est extrême » — exactement ce qu'exploite la régularisation.

{% include fviz/norm-ball.html %}

## Formulation mathématique

Pour un vecteur $\mathbf{x}=(x_1,\dots,x_n)$ :

**Norme $\ell_2$ (longueur euclidienne)**

$$
\lVert\mathbf{x}\rVert_2=\sqrt{\sum_i x_i^2}
$$

**Norme $\ell_1$ (somme des valeurs absolues)**

$$
\lVert\mathbf{x}\rVert_1=\sum_i |x_i|
$$

**Norme $\ell_\infty$ (plus grande valeur absolue)**

$$
\lVert\mathbf{x}\rVert_\infty=\max_i |x_i|
$$

Ce sont toutes des cas particuliers de la **norme $\ell_p$**, plus générale :

$$
\lVert\mathbf{x}\rVert_p=\Big(\sum_i |x_i|^p\Big)^{1/p}
$$

Toute norme satisfait trois axiomes : positivité (nulle uniquement pour le vecteur nul), homogénéité absolue $\lVert c\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$, et inégalité triangulaire $\lVert\mathbf{x}+\mathbf{y}\rVert\le\lVert\mathbf{x}\rVert+\lVert\mathbf{y}\rVert$.

## Un exemple concret

Prenons $\mathbf{x}=(3,-4)$ :

$$
\lVert\mathbf{x}\rVert_2=\sqrt{3^2+(-4)^2}=\sqrt{25}=5
$$
$$
\lVert\mathbf{x}\rVert_1=|3|+|-4|=7,\qquad \lVert\mathbf{x}\rVert_\infty=\max(3,4)=4
$$

Un même vecteur, trois « longueurs » toutes différentes.

```python
import numpy as np
x = np.array([3, -4])
print(np.linalg.norm(x, 2))     # 5.0
print(np.linalg.norm(x, 1))     # 7.0
print(np.linalg.norm(x, np.inf))# 4.0
```

## Pourquoi c'est important / où on l'utilise

- **Régularisation** : ajouter une pénalité de norme à la perte pour limiter la complexité du modèle et réduire le [surapprentissage](../overfitting/).
  - **Régularisation L2 (régression ridge / weight decay)** : on ajoute $\lambda\lVert\mathbf{w}\rVert_2^2$, ce qui rend les poids globalement plus petits et plus lisses.
  - **Régularisation L1 (Lasso)** : on ajoute $\lambda\lVert\mathbf{w}\rVert_1$, ce qui ramène certains poids exactement à 0 et produit un modèle **parcimonieux**, utilisable pour la sélection de variables.
- **Distance et similarité** : le KNN et le [partitionnement](../clustering/) utilisent la distance $\ell_2$ ; parmi les mesures d'erreur, la MSE correspond à $\ell_2$ et la MAE à $\ell_1$.
- **Écrêtage du gradient** : on redimensionne le gradient selon sa norme $\ell_2$ pour éviter l'explosion du [gradient](../gradient/).

## Intérêt pour la prévision de séries temporelles

- Les mesures de l'erreur de prévision sont elles-mêmes des normes : **MSE/RMSE = $\ell_2$** (sensible aux grandes erreurs), **MAE = $\ell_1$** (plus robuste aux valeurs aberrantes). Le choix dépend de ce que vous craignez le plus : les grosses erreurs, ou être entraîné par des points aberrants.
- Lors de l'entraînement de KUN (Kernel U-Net), ajouter un weight decay (L2) aide à stabiliser la [généralisation](../generalization/) sur les longues séries ; lorsqu'on a besoin de variables parcimonieuses et interprétables, on peut envisager L1.

## Erreurs fréquentes

- **Intuition géométrique L1 vs L2** : la frontière de contrainte en « losange » de L1 a des pointes, si bien que l'optimum tombe facilement sur un axe de coordonnées → solution parcimonieuse ; la frontière « circulaire » de L2 fait rétrécir les poids en douceur, sans qu'ils deviennent nuls en général.
- On confond souvent la norme $\ell_2$ et son carré : dans les pertes, on utilise surtout le **carré** $\lVert\cdot\rVert_2^2$ (dérivable et sans racine, donc plus facile à dériver).
- Une norme est toujours positive ou nulle, et seul le vecteur nul a une norme égale à 0.

[← Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)
