---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/svd/
title: "SVD (Singular Value Decomposition)"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

SVD (singular value decomposition) breaks **any** matrix into three steps: "**rotate → scale → rotate**". It is the mathematical foundation of many methods, including [PCA](../pca/), dimensionality reduction, low-rank approximation and recommender systems.

## Intuition

Any linear transformation (matrix), however complicated, can essentially be split into a combination of three simple moves:

1. **Rotate** the coordinate system (the shape doesn't change, only the angle from which you look at the problem);
2. **Stretch / compress** along the new coordinate axes (each direction is scaled by its own factor);
3. **Rotate** again into the output coordinate system.

The "scaling factors" are the **singular values**, which measure "how strongly" the matrix acts along each principal direction. Directions with large singular values carry the main structure of the data / transformation, while directions with small singular values are often noise or minor detail — **discarding small singular values = compression / denoising**, and this is where SVD's power comes from.

{% include fviz/svd-lowrank.html %}

## Mathematical formulation

Any matrix $A\in\mathbb{R}^{m\times n}$ can be decomposed as:

$$
A=U\Sigma V^\top
$$

- $U\in\mathbb{R}^{m\times m}$ — an orthogonal matrix whose columns are the **left singular vectors** (a rotation of the output space);
- $V\in\mathbb{R}^{n\times n}$ — an orthogonal matrix whose columns are the **right singular vectors** (a rotation of the input space);
- $\Sigma\in\mathbb{R}^{m\times n}$ — a diagonal matrix whose diagonal holds the **singular values** $\sigma_1\ge\sigma_2\ge\dots\ge 0$ (the scaling factors).

"Orthogonal" means $U^\top U=I$, i.e. a pure rotation / reflection that does not change lengths.

**Low-rank approximation (the Eckart–Young theorem)**: keeping only the $k$ largest singular values,

$$
A_k=\sum_{i=1}^{k}\sigma_i\,u_i v_i^\top
$$

gives, among all matrices of rank $k$, the one **closest** to $A$ (in the Frobenius / spectral norm). This is the theoretical guarantee behind using SVD for compression and dimensionality reduction.

## A concrete example

```python
import numpy as np
A = np.array([[3, 0],
              [0, 1],
              [0, 0]], dtype=float)
U, s, Vt = np.linalg.svd(A, full_matrices=False)
print(np.round(s, 3))           # Singular values [3. 1.]  → stronger action along x
# Rank-1 approximation using the single largest singular value
A1 = s[0] * np.outer(U[:, 0], Vt[0])
print(np.round(A1, 3))          # Keeps the main structure, drops the minor dimension
```

The singular values `[3, 1]` show that this transformation acts 3 times as strongly along the first direction as along the second; keeping only the largest singular value gives the best rank-1 approximation.

## Why it matters / where it is used

- **PCA / dimensionality reduction**: apply SVD to the data matrix; the first few singular vectors are the principal components.
- **Image / data compression**: keeping a few large singular values is enough to reconstruct something close to the original image.
- **Recommender systems**: a low-rank factorization of the "user × item" rating matrix predicts missing ratings.
- **Numerical stability**: singular values are used to compute a matrix's rank, condition number and pseudo-inverse (the least-squares solution).

## Relevance to time series forecasting

- Once a multivariate time series is arranged as a matrix, SVD / low-rank factorization can extract a few **common factors**, denoising and reducing dimensionality to give forecasting models more compact inputs.
- The idea of "summarizing complex data with low-rank structure" is in the same spirit as KUN (Kernel U-Net), which **extracts multi-scale main structure** through downsampling / kernel mappings — both grab the backbone and compress the detail.
- The singular value spectrum of a model's weights can also be used to analyze and compress networks (low-rank adaptation, pruning).

## Summary

- Any matrix can be written as $A=U\Sigma V^\top$: rotate — scale — rotate.
- The size of the singular values represents the "strength of action" in each direction; large ones are the main structure, small ones are mostly noise.
- Keeping the top $k$ singular values gives the best low-rank approximation, the common cornerstone of PCA, compression, dimensionality reduction and recommendation.

[← Math foundations](../math/) · [Foundations overview](../)
