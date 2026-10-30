---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/linear-algebra/
title: "Linear Algebra"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Linear algebra studies **vectors, matrices and linear transformations**. Every layer of a neural network and almost every dimensionality-reduction and representation method is built on it — it is fair to call it the "native language" of [machine learning](../ml/).

## Intuition

Think of data as **points in space (vectors)**: an image is a point in a space of tens of thousands of dimensions, and a time series segment is a vector made of a string of numbers. A **matrix** is then "an operation acting on those points" — it can rotate, stretch, compress or project the whole space.

So, geometrically, "training a model" often means **finding a suitable set of linear transformations (matrices)** that move messy data points into a new space where they are easier to separate and easier to predict. Linear algebra is the language that describes these points and operations.

{% include fviz/matrix-transform.html %}

## Mathematical formulation

A **vector** $\mathbf{x}\in\mathbb{R}^n$ is an ordered list of $n$ numbers, which can be seen as an arrow in space.

A **matrix** $A\in\mathbb{R}^{m\times n}$ is a table of numbers with $m$ rows and $n$ columns, representing a **linear transformation** from $\mathbb{R}^n$ to $\mathbb{R}^m$.

The core operation — **matrix–vector multiplication**:

$$
\mathbf{y}=A\mathbf{x},\qquad y_i=\sum_{j} A_{ij}\,x_j
$$

transforms the input vector $\mathbf{x}$ into the output vector $\mathbf{y}$ (see [matrix multiplication](../matrix-multiplication/)).

A few concepts that keep coming back:

- the **dot product** $\mathbf{a}\cdot\mathbf{b}=\sum_i a_i b_i$, which measures similarity / projection between two vectors;
- the **[norm](../norm/)** $\lVert\mathbf{x}\rVert$, the length of a vector;
- **linear independence / rank**: how many dimensions a set of vectors can "span";
- **eigenvalues and eigenvectors** $A\mathbf{v}=\lambda\mathbf{v}$: special directions whose orientation is unchanged by the transformation, which are only scaled by a factor $\lambda$;
- **[SVD](../svd/)**: any matrix can be decomposed into "rotation — scaling — rotation".

## A concrete example

Take a fully connected layer $\mathbf{y}=W\mathbf{x}+\mathbf{b}$ with a 2-dimensional input and a 2-dimensional output:

$$
W=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad \mathbf{x}=\begin{pmatrix}3\\4\end{pmatrix}
\ \Rightarrow\
W\mathbf{x}=\begin{pmatrix}1\cdot3+0\cdot4\\0\cdot3+2\cdot4\end{pmatrix}=\begin{pmatrix}3\\8\end{pmatrix}
$$

This $W$ stretches space by a factor of 2 in the $y$ direction and leaves the $x$ direction unchanged.

```python
import numpy as np
W = np.array([[1, 0], [0, 2]])
x = np.array([3, 4])
print(W @ x)   # [3 8]
```

## Why it matters / where it is used

- **Every layer of a [neural network](../neural-network/)** is essentially matrix multiplication + a nonlinearity, and the [attention mechanism](../attention/) is the matrix computation $QK^\top V$.
- **Dimensionality reduction and compression**: [PCA](../pca/), [SVD](../svd/) and embeddings all rely on linear algebra.
- **[GPU](../gpu/) acceleration**: the hardware is optimized for large-scale matrix multiplication, which is the physical precondition that makes deep learning feasible.

## What it means for time series forecasting

- Once the history window is arranged as a vector / matrix, the convolutions, kernel mappings and up/down-sampling in KUN (Kernel U-Net) are all matrix operations under the hood.
- A multivariate time series is naturally a matrix (time × variables), and the correlation structure between variables can be analyzed with covariance matrices and low-rank decompositions.
- Efficient batch forecasting relies on stacking many series into a large matrix and computing them all at once.

## Summary

- Vector = a point in space; matrix = a linear transformation acting on it.
- Matrix multiplication, norms, rank, eigenvalues/SVD are the core tools.
- It is the common foundation of neural network forward computation, dimensionality reduction and GPU acceleration.

[← Math foundations](../math/) · [Foundations overview](../)
