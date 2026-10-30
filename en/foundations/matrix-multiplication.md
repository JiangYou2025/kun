---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/matrix-multiplication/
title: "Matrix Multiplication"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Matrix multiplication is the central operation of [linear algebra](../linear-algebra/): it applies a **linear transformation** to a set of vectors, and it is also the way to **chain** several linear transformations into one. Every layer of a [neural network](../neural-network/) and the [attention mechanism](../attention/) are, underneath, matrix multiplications.

## Intuition

There are two ways to understand $C=AB$:

- **Composition of transformations**: if $B$ is "do one transformation first" and $A$ is "then do another", then $AB$ is the single matrix that "performs both transformations in one go". First $B$, then $A$ — the order cannot be reversed, and this is the root of its **non-commutativity**.
- **Rows dotted with columns**: the entry in row $i$, column $j$ of the result is the dot product of **row** $i$ of $A$ with **column** $j$ of $B$. "Row meets column" is the mnemonic for computing by hand.

{% include fviz/matmul-compose.html %}

## The math

Let $A\in\mathbb{R}^{m\times k}$ and $B\in\mathbb{R}^{k\times n}$. Then the product $C=AB\in\mathbb{R}^{m\times n}$ is:

$$
C_{ij}=\sum_{l=1}^{k} A_{il}\,B_{lj}
$$

**Shape rule** (the most common pitfall): the **number of columns** of $A$ must equal the **number of rows** of $B$ (both are $k$), and the result has shape "rows of $A$ × columns of $B$":

$$
(m\times k)\cdot(k\times n)=(m\times n)
$$

Important properties:

- **Not commutative**: in general $AB\ne BA$;
- Associative, $A(BC)=(AB)C$, and distributive;
- $(AB)^\top=B^\top A^\top$ (the order flips after transposition).

## A concrete example

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
print(B @ A)        # [[23 34] [31 46]]  ≠ A@B, confirming non-commutativity
```

## Why it matters / where it is used

- **Forward pass of neural networks**: every fully connected layer is $\mathbf{y}=W\mathbf{x}+\mathbf{b}$, a single matrix–vector multiplication.
- **Attention mechanism**: $\text{softmax}(QK^\top/\sqrt{d})\,V$, several matrix multiplications in a row.
- **Batching**: stacking a batch of samples into a matrix lets one multiplication process all of them at once — the key to [GPU](../gpu/) efficiency. The cost is about $O(mkn)$, so model size directly determines compute requirements.

## Relevance to time series forecasting

- The convolutions, kernel projections and linear layers of KUN (Kernel U-Net) all become matrix multiplications on the hardware; forecasting latency and memory use are largely determined by the size of these multiplications.
- Transforming multivariate series (time × variables) and forecasting many series in a batch are both done by arranging the data into matrices and multiplying them in one shot.

## Common pitfalls

- **Mismatched dimensions** is the most common error: always check that the "inner dimensions agree" (columns of $A$ = rows of $B$).
- Do not confuse matrix multiplication with **element-wise multiplication** (Hadamard, `*` or `np.multiply`); the two are completely different.
- Order matters: $AB\ne BA$, and when transposing remember $(AB)^\top=B^\top A^\top$.

[← Math foundations](../math/) · [Foundations overview](../)
