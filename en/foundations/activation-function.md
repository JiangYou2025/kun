---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/activation-function/
title: "Activation Functions"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

An **activation function** is the **nonlinear function** applied after each [neuron](../neuron/)'s weighted sum. It is the key to a [neural network](../neural-network/)'s ability to "express complex relationships" — **without it, even the deepest network is equivalent to a single linear transformation**.

## Why it must be nonlinear

Recall [forward propagation](../forward-propagation/): each layer computes $z = Wa + b$. Without an activation function, stacking several layers gives:

$$
W_2(W_1 x + b_1) + b_2 = (W_2 W_1)\,x + (W_2 b_1 + b_2)
$$

No matter how many layers you stack, the result **is still a linear function of $x$**! The depth is completely wasted. The activation function $\sigma$ introduces a "bend" at every layer, which lets the network approximate **arbitrarily complex nonlinear relationships** (this is the intuition behind the universal approximation theorem).

## Three classic activation functions

**Sigmoid**: squashes the input into $(0,1)$.

$$
\sigma(x) = \frac{1}{1+e^{-x}},\qquad
\sigma'(x) = \sigma(x)\big(1-\sigma(x)\big)
$$

Its derivative peaks at only $0.25$ at $x=0$ and tends to 0 at both ends. This means that every time the error signal passes through a Sigmoid layer, it is multiplied by a factor of at most $0.25$ — in a deep network the product quickly goes to 0, causing [vanishing gradients](../vanishing-exploding-gradient/). Today it is mostly used in the output layer for binary classification, and rarely in hidden layers.

**Tanh**: squashes the input into $(-1,1)$; it is the "zero-centered" version of Sigmoid.

$$
\tanh(x) = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}},\qquad
\tanh'(x) = 1 - \tanh^2(x)
$$

Being zero-centered (outputs can be positive or negative) makes training slightly better than with Sigmoid, and the derivative peaks at 1 (at $x=0$). But both ends still saturate, so deep networks still suffer from vanishing gradients. It is common in [RNNs](../rnn/)/[LSTMs](../lstm/).

**ReLU**: the most widely used hidden-layer activation — simple and blunt.

$$
\mathrm{ReLU}(x) = \max(0, x),\qquad
\mathrm{ReLU}'(x) = \begin{cases}1 & x>0\\ 0 & x<0\end{cases}
$$

**Why ReLU mitigates vanishing gradients**: on the positive side its derivative is **always 1**, so the error signal is not shrunk again and again during backpropagation — multiplying by 1 still gives 1. This makes even very deep networks trainable. The price is a zero derivative on the negative side, so a neuron can "die" (output 0 forever). The improved **Leaky ReLU** (a small slope $0.01x$ when $x<0$) alleviates this problem.

## A concrete example

Suppose a neuron's weighted sum is $z = -0.5$. Compare the outputs of the three activations and "how much gradient can flow back" (i.e., the derivative):

| Activation | Output | Derivative (gradient factor at that point) |
|---|---|---|
| Sigmoid | $\sigma(-0.5)\approx0.378$ | $0.378(1-0.378)\approx0.235$ |
| Tanh | $\tanh(-0.5)\approx-0.462$ | $1-0.462^2\approx0.787$ |
| ReLU | $\max(0,-0.5)=0$ | $0$ (negative region) |

Imagine 10 layers all using Sigmoid: the gradient factor is about $0.235^{10}\approx 5\times10^{-7}$ — **it practically vanishes**. This is exactly why deep networks abandoned Sigmoid in favor of ReLU.

```python
import numpy as np
sigmoid = lambda x: 1/(1+np.exp(-x))
tanh    = np.tanh
relu    = lambda x: np.maximum(0, x)
z = -0.5
print(sigmoid(z), tanh(z), relu(z))   # 0.378  -0.462  0.0
```

## How to choose

- **Use ReLU by default in hidden layers** (or GELU, Leaky ReLU) — fast, stable, resistant to vanishing gradients.
- **Use Sigmoid in the output layer for binary classification** (it outputs a probability), and Softmax for multi-class classification.
- **Regression output layers usually have no activation** (they output a real number directly) — this is typically the case for the output layer in time series forecasting.
- Inside [RNNs](../rnn/)/[LSTMs](../lstm/), Tanh and Sigmoid are often combined for gating.

## Common misconceptions

- **"The output layer needs ReLU too"** — not when predicting real numbers; otherwise it can never output a negative value.
- **"The more complex the activation function, the better"** — ReLU is so simple yet the most widely used; complexity does not equal effectiveness.
- **"Sigmoid is good for deep hidden layers"** — quite the opposite: it causes [vanishing gradients](../vanishing-exploding-gradient/).

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
