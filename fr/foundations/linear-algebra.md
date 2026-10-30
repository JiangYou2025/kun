---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/linear-algebra/
title: "L'algèbre linéaire"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

L'algèbre linéaire étudie les **vecteurs, les matrices et les transformations linéaires**. Chaque couche d'un réseau de neurones, et presque toutes les méthodes de réduction de dimension et de représentation, reposent sur elle — on peut dire que c'est la « langue maternelle » de l'[apprentissage automatique](../ml/).

## Intuition

Imaginez les données comme des **points dans un espace (des vecteurs)** : une image est un point dans un espace de plusieurs dizaines de milliers de dimensions, une série temporelle est un vecteur formé d'une suite de nombres. Une **matrice**, elle, est « une opération appliquée à ces points » — elle peut faire tourner, étirer, comprimer ou projeter tout l'espace.

Géométriquement, « entraîner un modèle » revient donc souvent à **chercher un ensemble de transformations linéaires (de matrices) adaptées** qui déplacent des données désordonnées vers un nouvel espace où elles sont plus faciles à distinguer et à prédire. L'algèbre linéaire est le langage qui décrit ces points et ces opérations.

{% include fviz/matrix-transform.html %}

## Formulation mathématique

Un **vecteur** $\mathbf{x}\in\mathbb{R}^n$ est une liste ordonnée de $n$ nombres, que l'on peut voir comme une flèche dans l'espace.

Une **matrice** $A\in\mathbb{R}^{m\times n}$ est un tableau de nombres à $m$ lignes et $n$ colonnes, qui représente une **transformation linéaire** de $\mathbb{R}^n$ vers $\mathbb{R}^m$.

L'opération centrale — le **produit matrice–vecteur** :

$$
\mathbf{y}=A\mathbf{x},\qquad y_i=\sum_{j} A_{ij}\,x_j
$$

transforme le vecteur d'entrée $\mathbf{x}$ en vecteur de sortie $\mathbf{y}$ (voir le [produit matriciel](../matrix-multiplication/)).

Quelques notions qui reviennent sans cesse :

- **Produit scalaire** $\mathbf{a}\cdot\mathbf{b}=\sum_i a_i b_i$, qui mesure la similarité / la projection entre deux vecteurs ;
- **[Norme](../norm/)** $\lVert\mathbf{x}\rVert$, la longueur d'un vecteur ;
- **Indépendance linéaire / rang** : le nombre de dimensions qu'un ensemble de vecteurs peut « engendrer » ;
- **Valeurs propres et vecteurs propres** $A\mathbf{v}=\lambda\mathbf{v}$ : les directions particulières que la transformation ne modifie pas, se contentant de les multiplier par $\lambda$ ;
- **[SVD](../svd/)** : toute matrice se décompose en « rotation — mise à l'échelle — rotation ».

## Un exemple concret

Une couche entièrement connectée $\mathbf{y}=W\mathbf{x}+\mathbf{b}$, avec une entrée et une sortie de dimension 2 :

$$
W=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad \mathbf{x}=\begin{pmatrix}3\\4\end{pmatrix}
\ \Rightarrow\
W\mathbf{x}=\begin{pmatrix}1\cdot3+0\cdot4\\0\cdot3+2\cdot4\end{pmatrix}=\begin{pmatrix}3\\8\end{pmatrix}
$$

Cette matrice $W$ étire l'espace d'un facteur 2 selon la direction $y$ et laisse la direction $x$ inchangée.

```python
import numpy as np
W = np.array([[1, 0], [0, 2]])
x = np.array([3, 4])
print(W @ x)   # [3 8]
```

## Pourquoi c'est important / où l'utilise-t-on

- **Chaque couche d'un [réseau de neurones](../neural-network/)** se résume à un produit matriciel suivi d'une non-linéarité, et le [mécanisme d'attention](../attention/) est un calcul matriciel en $QK^\top V$.
- **Réduction de dimension et compression** : l'[ACP](../pca/), la [SVD](../svd/) et les plongements (embeddings) reposent tous sur l'algèbre linéaire.
- **Accélération par [GPU](../gpu/)** : le matériel est optimisé pour les produits matriciels à grande échelle, ce qui est la condition physique pour que l'apprentissage profond puisse tourner.

## Signification pour la prévision de séries temporelles

- Une fois la fenêtre historique mise sous forme de vecteur / matrice, les convolutions, les projections par noyau et les sous-/sur-échantillonnages de KUN (Kernel U-Net) ne sont, au fond, que des opérations matricielles.
- Une série temporelle multivariée est naturellement une matrice (temps × variables) ; la structure de corrélation entre variables s'analyse à l'aide de la matrice de covariance ou de décompositions de rang faible.
- Une prévision par lots efficace consiste à empiler de nombreuses séries dans une grande matrice pour les calculer en une seule fois.

## En résumé

- Vecteur = point dans l'espace ; matrice = transformation linéaire qui agit sur ces points.
- Produit matriciel, norme, rang, valeurs propres / SVD sont les outils centraux.
- C'est la base commune du calcul direct des réseaux de neurones, de la réduction de dimension et de l'accélération par GPU.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
