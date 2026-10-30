---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/mlp/
title: "MLP (Multi-Layer Perceptron)"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

The **MLP (Multi-Layer Perceptron)** is the most basic [neural network](../neural-network/): a stack of fully connected layers, where every [neuron](../neuron/) in one layer is connected to every neuron in the next, with [activation functions](../activation-function/) in between. It is the "building block" of almost every modern [architecture](../architectures/).

## Intuition

"Fully connected" means **not picky**. Every neuron sees all the information from the previous layer and decides for itself what matters and what to ignore (through its learned weights).

This contrasts with the "look only at a local window" approach of the [CNN](../cnn/) and the "pick out what is relevant" approach of [attention](../attention/). The MLP presupposes no structural assumptions; it is the plainest, most general form: given enough neurons, it can in theory approximate any continuous function (the **universal approximation theorem**). The price is a large number of parameters and no use of the data's own structure (such as the order of time steps or the adjacency of pixels).

{% include fviz/relu-approx.html %}

## The math

An $L$-layer MLP repeatedly nests "linear transformation + activation". With input $\mathbf{x}$ and $\mathbf{h}^{(0)} = \mathbf{x}$, layer $l$ is:

$$
\mathbf{h}^{(l)} = \sigma\!\left( \mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)} \right), \quad l = 1, \dots, L
$$

- $\mathbf{h}^{(l-1)} \in \mathbb{R}^{d_{l-1}}$: the output of layer $l-1$ (dimension $d_{l-1}$);
- $\mathbf{W}^{(l)} \in \mathbb{R}^{d_l \times d_{l-1}}$: the weight matrix, mapping $d_{l-1}$ dimensions to $d_l$ dimensions;
- $\mathbf{b}^{(l)} \in \mathbb{R}^{d_l}$: the bias vector;
- $\sigma$: the activation function, applied element-wise (hidden layers commonly use ReLU, $\sigma(z)=\max(0,z)$);
- The output layer usually has **no activation** (for regression tasks): simply $\hat{\mathbf{y}} = \mathbf{W}^{(L)}\mathbf{h}^{(L-1)} + \mathbf{b}^{(L)}$.

**Parameter count**: layer $l$ has $d_l \times d_{l-1} + d_l$ parameters. This is also the MLP's weak spot — as dimensions grow, the weight matrices explode.

## A concrete example

Let us compute a tiny MLP by hand: 2-dimensional input, a hidden layer of 2 neurons (ReLU), 1-dimensional output.

Let $\mathbf{x} = \begin{bmatrix}1\cr 2\end{bmatrix}$,

$$
\mathbf{W}^{(1)} = \begin{bmatrix}1 & 0\\-1 & 1\end{bmatrix},\quad
\mathbf{b}^{(1)} = \begin{bmatrix}0\\0\end{bmatrix}
$$

Linear part of layer 1: $\mathbf{W}^{(1)}\mathbf{x} = \begin{bmatrix}1\cdot1 + 0\cdot2\cr  -1\cdot1 + 1\cdot2\end{bmatrix} = \begin{bmatrix}1\cr 1\end{bmatrix}$.

Through ReLU: $\mathbf{h}^{(1)} = \begin{bmatrix}\max(0,1)\cr\max(0,1)\end{bmatrix} = \begin{bmatrix}1\cr 1\end{bmatrix}$.

Output layer $\mathbf{W}^{(2)} = \begin{bmatrix}2 & 3\end{bmatrix}$, $b^{(2)}=1$:

$$
\hat{y} = 2\cdot1 + 3\cdot1 + 1 = 6
$$

In code:

```python
import torch.nn as nn

mlp = nn.Sequential(
    nn.Linear(2, 2),
    nn.ReLU(),
    nn.Linear(2, 1),
)
```

## Why it matters / where it is used

- **Universal approximator**: in theory it can fit an arbitrarily complex input–output relationship.
- **All-purpose component**: the "feed-forward network" inside every [Transformer](../transformer/) block is an MLP; the final prediction head of a CNN/U-Net is often an MLP too. Learn it and you understand part of countless models.
- **Strong baseline**: in time series forecasting, flattening the whole history and feeding it to an MLP (as in models like DLinear and N-BEATS) is often surprisingly strong, and it is an essential point of comparison.

## Relevance to time series forecasting

The simplest forecasting approach: treat a history window of length $L$ as an $L$-dimensional vector and map it directly with an MLP to an $H$-dimensional future:

```python
forecaster = nn.Sequential(
    nn.Linear(96, 256), nn.ReLU(),
    nn.Linear(256, 24),     # 96 steps of history -> 24-step forecast
)
```

This "flatten + fully connected" approach is simple and efficient, but has two limitations: it **ignores the sequential structure of time** (shuffling the input order leaves the result unchanged), and the longer the window, the more parameters it needs. The **Kernel U-Net (KUN)** promoted on this site eases both points in a [multi-scale](../u-net/) way — it processes the series with lightweight "kernels" at different time resolutions, and the transformation inside each kernel is, in essence, still a small MLP. So the MLP is both a baseline and an internal component of more advanced architectures.

## Common pitfalls

- **"An MLP works without activations"**: wrong. Without activations, the layers collapse into a single linear layer; extra depth is useless.
- **"More layers are always better"**: pure MLPs that are too deep easily run into [vanishing / exploding gradients](../vanishing-exploding-gradient/) and [overfitting](../overfitting/), and often need helpers such as [Dropout](../dropout/) and [BatchNorm](../batchnorm/).
- **"An MLP understands temporal order"**: it does not. It treats its input as an unordered vector; temporal structure has to be introduced through CNNs/RNNs/attention or deliberate design.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
