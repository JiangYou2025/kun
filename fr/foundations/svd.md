---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/svd/
title: "SVD (décomposition en valeurs singulières)"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

La SVD (décomposition en valeurs singulières) décompose une matrice **quelconque** en trois étapes : « **rotation → mise à l'échelle → rotation** ». Elle est la base mathématique de nombreuses méthodes comme l'[ACP](../pca/), la réduction de dimension, l'approximation de rang faible ou les systèmes de recommandation.

## Intuition

Toute transformation linéaire (toute matrice), aussi compliquée soit-elle, peut au fond se décomposer en une combinaison de trois gestes simples :

1. **faire tourner** le repère (sans changer la forme, seulement l'angle sous lequel on regarde le problème) ;
2. **étirer / comprimer** le long des nouveaux axes (chaque direction est mise à l'échelle par un certain facteur) ;
3. **faire tourner** à nouveau vers le repère de sortie.

Les « facteurs d'échelle » sont les **valeurs singulières** ; elles mesurent « la force d'action » de la matrice dans chacune de ses directions principales. Les directions associées à de grandes valeurs singulières portent la structure principale des données / de la transformation, tandis que celles associées à de petites valeurs singulières correspondent souvent à du bruit ou à des détails secondaires — **éliminer les petites valeurs singulières = compresser / débruiter**, et c'est là que réside toute la puissance de la SVD.

{% include fviz/svd-lowrank.html %}

## Formulation mathématique

Toute matrice $A\in\mathbb{R}^{m\times n}$ peut se décomposer en :

$$
A=U\Sigma V^\top
$$

- $U\in\mathbb{R}^{m\times m}$ — une matrice orthogonale dont les colonnes sont les **vecteurs singuliers à gauche** (rotation dans l'espace de sortie) ;
- $V\in\mathbb{R}^{n\times n}$ — une matrice orthogonale dont les colonnes sont les **vecteurs singuliers à droite** (rotation dans l'espace d'entrée) ;
- $\Sigma\in\mathbb{R}^{m\times n}$ — une matrice diagonale dont la diagonale contient les **valeurs singulières** $\sigma_1\ge\sigma_2\ge\dots\ge 0$ (les facteurs d'échelle).

« Orthogonale » signifie $U^\top U=I$, c'est-à-dire une pure rotation / réflexion qui ne change pas les longueurs.

**Approximation de rang faible (théorème d'Eckart–Young)** : en ne gardant que les $k$ plus grandes valeurs singulières,

$$
A_k=\sum_{i=1}^{k}\sigma_i\,u_i v_i^\top
$$

est, parmi toutes les matrices de rang $k$, celle qui est **la plus proche** de $A$ (au sens de la norme de Frobenius / de la norme spectrale). C'est précisément la garantie théorique de l'usage de la SVD pour la compression et la réduction de dimension.

## Un exemple concret

```python
import numpy as np
A = np.array([[3, 0],
              [0, 1],
              [0, 0]], dtype=float)
U, s, Vt = np.linalg.svd(A, full_matrices=False)
print(np.round(s, 3))           # valeurs singulières [3. 1.]  → action plus forte dans la direction x
# Approximation de rang 1 avec la plus grande valeur singulière
A1 = s[0] * np.outer(U[:, 0], Vt[0])
print(np.round(A1, 3))          # garde la structure principale, élimine la dimension secondaire
```

Les valeurs singulières `[3, 1]` montrent que cette transformation agit trois fois plus fort dans la première direction que dans la seconde ; en ne gardant que la plus grande valeur singulière, on obtient la meilleure approximation de rang 1.

## Pourquoi c'est important / où l'utilise-t-on

- **ACP / réduction de dimension** : en appliquant la SVD à la matrice des données, les premiers vecteurs singuliers sont les composantes principales.
- **Compression d'images / de données** : quelques grandes valeurs singulières suffisent à reconstruire un résultat proche de l'original.
- **Systèmes de recommandation** : une décomposition de rang faible de la matrice des notes « utilisateurs × articles » permet de prédire les notes manquantes.
- **Stabilité numérique** : les valeurs singulières servent à calculer le rang d'une matrice, son conditionnement et sa pseudo-inverse (solution des moindres carrés).

## Intérêt pour la prévision de séries temporelles

- Une fois une série temporelle multivariée disposée en matrice, la SVD / la décomposition de rang faible permet d'en extraire un petit nombre de **facteurs communs**, de débruiter et de réduire la dimension, fournissant au modèle de prévision une entrée plus compacte.
- L'idée de « résumer des données complexes par une structure de rang faible » rejoint celle de KUN (Kernel U-Net), qui **extrait la structure principale à plusieurs échelles** par sous-échantillonnage / projection par noyau — dans les deux cas, on saisit l'essentiel et on comprime les détails.
- Le spectre des valeurs singulières des poids d'un modèle sert aussi à analyser et compresser les réseaux (adaptation de rang faible, élagage).

## En résumé

- Toute matrice s'écrit $A=U\Sigma V^\top$ : rotation — mise à l'échelle — rotation.
- La taille des valeurs singulières représente la « force d'action » dans chaque direction : les grandes portent la structure principale, les petites sont souvent du bruit.
- Garder les $k$ premières valeurs singulières donne la meilleure approximation de rang faible, socle commun de l'ACP, de la compression, de la réduction de dimension et de la recommandation.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
