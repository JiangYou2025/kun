---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/matrix-multiplication/
title: "Multiplication matricielle"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)

La multiplication matricielle est l'opération centrale de l'[algèbre linéaire](../linear-algebra/) : elle applique une **transformation linéaire** à un ensemble de vecteurs, et c'est aussi la façon d'**enchaîner** plusieurs transformations linéaires en une seule. Chaque couche d'un [réseau de neurones](../neural-network/) comme le [mécanisme d'attention](../attention/) reposent, au fond, sur des multiplications matricielles.

## Intuition

On peut comprendre $C=AB$ de deux manières :

- **Composition de transformations** : si $B$ signifie « appliquer d'abord une transformation » et $A$ « en appliquer ensuite une autre », alors $AB$ est la matrice unique qui « réalise les deux d'un seul coup ». D'abord $B$, puis $A$ — l'ordre ne peut pas être inversé : c'est là l'origine de sa **non-commutativité**.
- **Ligne fois colonne** : l'élément en ligne $i$, colonne $j$ du résultat est le produit scalaire de la **ligne** $i$ de $A$ et de la **colonne** $j$ de $B$. « Ligne contre colonne » : c'est le moyen mnémotechnique du calcul à la main.

## Formulation mathématique

Soit $A\in\mathbb{R}^{m\times k}$ et $B\in\mathbb{R}^{k\times n}$ ; le produit $C=AB\in\mathbb{R}^{m\times n}$ vaut :

$$
C_{ij}=\sum_{l=1}^{k} A_{il}\,B_{lj}
$$

**Règle des dimensions** (le piège le plus fréquent) : le **nombre de colonnes** de $A$ doit être égal au **nombre de lignes** de $B$ (tous deux valent $k$), et le résultat a pour forme « lignes de $A$ × colonnes de $B$ » :

$$
(m\times k)\cdot(k\times n)=(m\times n)
$$

Propriétés importantes :

- **Pas de commutativité** : en général, $AB\ne BA$ ;
- associativité $A(BC)=(AB)C$ et distributivité ;
- $(AB)^\top=B^\top A^\top$ (l'ordre s'inverse après transposition).

## Un exemple concret

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad
B=\begin{pmatrix}5&6\\7&8\end{pmatrix}
$$

$$
C_{11}=1\cdot5+2\cdot7=19,\quad C_{12}=1\cdot6+2\cdot8=22
$$
$$
C_{21}=3\cdot5+4\cdot7=43,\quad C_{22}=3\cdot6+4\cdot8=50
$$

$$
AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}
$$

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)        # [[19 22] [43 50]]
print(B @ A)        # [[23 34] [31 46]]  ≠ A@B, la non-commutativité est vérifiée
```

## Pourquoi c'est important / où on l'utilise

- **Propagation avant d'un réseau de neurones** : chaque couche entièrement connectée calcule $\mathbf{y}=W\mathbf{x}+\mathbf{b}$, soit un produit matrice–vecteur.
- **Mécanisme d'attention** : $\text{softmax}(QK^\top/\sqrt{d})\,V$, plusieurs multiplications matricielles successives.
- **Traitement par lots** : en empilant un lot d'exemples dans une matrice, une seule multiplication les traite tous à la fois — c'est la clé de l'efficacité des [GPU](../gpu/). Le coût de calcul est d'environ $O(mkn)$ ; la taille du modèle détermine donc directement la puissance de calcul nécessaire.

## Intérêt pour la prévision de séries temporelles

- Les convolutions, les projections par noyaux et les couches linéaires de KUN (Kernel U-Net) se ramènent toutes, au niveau matériel, à des multiplications matricielles ; la latence de prévision et la mémoire GPU occupée dépendent largement de la taille de ces multiplications.
- La transformation de séries multivariées (temps × variables) et la prévision par lots de plusieurs séries se font en disposant les données en matrice puis en les multipliant d'un seul coup.

## Erreurs fréquentes

- **Des dimensions incompatibles**, l'erreur la plus courante : vérifiez toujours que les « dimensions intérieures sont égales » (colonnes de $A$ = lignes de $B$).
- Ne confondez pas la multiplication matricielle avec le **produit terme à terme** (produit de Hadamard, `*` ou `np.multiply`) : ce sont deux opérations totalement différentes.
- L'ordre compte : $AB\ne BA$, et lors d'une transposition, souvenez-vous que $(AB)^\top=B^\top A^\top$.

[← Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)
