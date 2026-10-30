---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/norm/
title: "Norms"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

A norm is a function that measures the "**length / size**" of a vector. The same vector has different "lengths" under different norms; in machine learning the most common are $\ell_1$ and $\ell_2$, which are also the core tools of [regularization](../regularization/) and distance measurement.

## Intuition

"How far is it from home to the office?" depends on how you travel:

- Flying in a straight line ($\ell_2$, Euclidean distance);
- Walking along a grid of streets ($\ell_1$, Manhattan / taxicab distance);
- Caring only about the single direction in which you travel farthest ($\ell_\infty$).

A norm formalizes the plain notion of "size / distance", and allows for several reasonable ways of measuring it. It also measures "how sparse or how extreme a vector is", which is exactly what regularization exploits.

{% include fviz/norm-ball.html %}

## The math

For a vector $\mathbf{x}=(x_1,\dots,x_n)$:

**The $\ell_2$ norm (Euclidean length)**

$$
\lVert\mathbf{x}\rVert_2=\sqrt{\sum_i x_i^2}
$$

**The $\ell_1$ norm (sum of absolute values)**

$$
\lVert\mathbf{x}\rVert_1=\sum_i |x_i|
$$

**The $\ell_\infty$ norm (largest absolute value)**

$$
\lVert\mathbf{x}\rVert_\infty=\max_i |x_i|
$$

They are all special cases of the more general **$\ell_p$ norm**:

$$
\lVert\mathbf{x}\rVert_p=\Big(\sum_i |x_i|^p\Big)^{1/p}
$$

Every norm satisfies three axioms: non-negativity (zero only for the zero vector), absolute homogeneity $\lVert c\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$, and the triangle inequality $\lVert\mathbf{x}+\mathbf{y}\rVert\le\lVert\mathbf{x}\rVert+\lVert\mathbf{y}\rVert$.

## A concrete example

Take $\mathbf{x}=(3,-4)$:

$$
\lVert\mathbf{x}\rVert_2=\sqrt{3^2+(-4)^2}=\sqrt{25}=5
$$
$$
\lVert\mathbf{x}\rVert_1=|3|+|-4|=7,\qquad \lVert\mathbf{x}\rVert_\infty=\max(3,4)=4
$$

The same vector, three different "lengths".

```python
import numpy as np
x = np.array([3, -4])
print(np.linalg.norm(x, 2))     # 5.0
print(np.linalg.norm(x, 1))     # 7.0
print(np.linalg.norm(x, np.inf))# 4.0
```

## Why it matters / where it is used

- **Regularization**: add a norm penalty to the loss to limit model complexity and curb [overfitting](../overfitting/).
  - **L2 regularization (ridge regression / weight decay)**: add $\lambda\lVert\mathbf{w}\rVert_2^2$, making the weights smaller overall and smoother.
  - **L1 regularization (Lasso)**: add $\lambda\lVert\mathbf{w}\rVert_1$, which pushes some weights exactly to 0, giving a **sparse** model that can perform feature selection.
- **Distance and similarity**: KNN and [clustering](../clustering/) use $\ell_2$ distance; among error measures, MSE is $\ell_2$ and MAE is $\ell_1$.
- **Gradient clipping**: rescale by the $\ell_2$ norm of the gradient to prevent exploding [gradients](../gradient/).

## Relevance to time series forecasting

- Forecast error measures are themselves norms: **MSE/RMSE = $\ell_2$** (sensitive to large errors), **MAE = $\ell_1$** (more robust to outliers). Which to choose depends on whether you fear big mistakes more, or being dragged off course by outliers.
- When training KUN (Kernel U-Net), adding weight decay (L2) helps keep [generalization](../generalization/) stable on long series; when sparse, interpretable features are needed, consider L1.

## Common pitfalls

- **Geometric intuition for L1 vs L2**: the "diamond" constraint boundary of L1 has sharp corners, so the optimum tends to land on a coordinate axis → sparse solutions; the "circular" boundary of L2 shrinks the weights smoothly but generally not to 0.
- The $\ell_2$ norm and its square are often used interchangeably: losses mostly use the **square** $\lVert\cdot\rVert_2^2$ (differentiable, with no square root, easier to differentiate).
- A norm is always non-negative, and only the zero vector has norm 0.

[← Math foundations](../math/) · [Foundations overview](../)
