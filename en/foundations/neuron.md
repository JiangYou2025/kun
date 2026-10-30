---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/neuron/
title: "The Neuron"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**A neuron is the smallest computing unit in a [neural network](../neural-network/)**: it takes a weighted sum of several inputs, adds a bias, passes the result through an [activation function](../activation-function/), and outputs a single number. Every deep model, in the end, is built from thousands upon thousands of these small units.

## Intuition

Think of a neuron as **a little judge who gives scores**. In front of it are a few features (say a stock's opening price today, its trading volume, and yesterday's closing price). For each feature it has a weight saying "how much I care about this", and it adds them up according to those weights to get a total score. If the total is high enough (above some threshold), it gets "excited" and outputs a large value; otherwise it stays quiet.

- **Weight $w_i$**: expresses "how important this input is to me". A positive weight means the larger the input, the more it pushes toward activation; a negative weight means the opposite.
- **Bias $b$**: like the judge's "baseline" or "temperament". A large bias means it gets excited easily; a very negative bias means it is hard to activate.
- **Activation function**: decides "how the total score becomes the output", and introduces the crucial **non-linearity**.

A single neuron is dumb and can only do one simple thing; but connect many neurons into a network, and together they can approximate extremely complex functions.

## The math

A single neuron computes in two steps. First, a **linear weighted sum** (also called the pre-activation, written $z$):

$$ z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^\top \mathbf{x} + b $$

where:

- $\mathbf{x} = (x_1, \dots, x_n)$ is the input vector and $n$ is the number of input features;
- $\mathbf{w} = (w_1, \dots, w_n)$ is the weight vector, the parameters the neuron must **learn**;
- $b$ is the bias, also a parameter to be learned;
- $\mathbf{w}^\top \mathbf{x}$ is the dot product, i.e. $w_1x_1 + w_2x_2 + \dots + w_nx_n$.

Then it passes through an activation function $\sigma$ to give the **output $a$** (the activation):

$$ a = \sigma(z) = \sigma(\mathbf{w}^\top \mathbf{x} + b) $$

Without $\sigma$ (i.e. if $\sigma$ is the identity function), no matter how many layers you stack, the whole network is only a composition of linear transformations, and therefore still just a linear function — this is why [activation functions](../activation-function/) are indispensable.

{% include fviz/neuron-2d.html %}

## A concrete example

Suppose a neuron has two inputs $x_1, x_2$, weights $\mathbf{w} = (0.5,\ -1.2)$, bias $b = 0.3$, and uses ReLU as its activation function ($\mathrm{ReLU}(z)=\max(0,z)$).

Given the input $\mathbf{x} = (4,\ 1)$:

$$ z = 0.5 \times 4 + (-1.2)\times 1 + 0.3 = 2.0 - 1.2 + 0.3 = 1.1 $$
$$ a = \mathrm{ReLU}(1.1) = 1.1 $$

Now try another input, $\mathbf{x} = (1,\ 3)$:

$$ z = 0.5\times 1 + (-1.2)\times 3 + 0.3 = 0.5 - 3.6 + 0.3 = -2.8 $$
$$ a = \mathrm{ReLU}(-2.8) = 0 $$

As you can see, the second input "silences" the neuron. In code:

```python
import numpy as np

w = np.array([0.5, -1.2])
b = 0.3

def neuron(x):
    z = w @ x + b          # weighted sum
    return max(0.0, z)     # ReLU activation

print(neuron(np.array([4, 1])))  # 1.1
print(neuron(np.array([1, 3])))  # 0.0
```

## Why it matters / where it is used

The neuron is the **atom** for understanding every [deep learning](../dl/) structure:

- Place several neurons side by side in one layer and you get a **fully connected layer**; stack several fully connected layers and you have an [MLP](../mlp/).
- In a [CNN](../cnn/), neurons share weights and look only at local inputs, becoming convolution kernels.
- In an [RNN](../rnn/), a neuron additionally receives the hidden state from the previous time step.

Once you understand the "weighted sum + activation" step, you can follow [forward propagation](../forward-propagation/) (repeating this step along the network) and [backpropagation](../backpropagation/) (working backwards to get the gradient of each $w_i, b$).

## Relevance to time series forecasting

In forecasting, the "inputs" a neuron receives are usually **several values from the history window** or features derived from them. For example, to forecast the future from the past 96 time points, each neuron forms a weighted combination of these 96 numbers (or of features extracted by higher layers). The site's flagship model, [Kernel U-Net (KUN)](../u-net/), is no exception — it uses this basic "weighted sum + non-linearity" unit at multiple scales to distill temporal patterns, only organizing the units into a U-shaped, multi-scale structure.

## Summary

- Neuron = **weighted sum $\mathbf{w}^\top\mathbf{x}+b$, then an activation function $\sigma$**.
- $\mathbf{w}$ and $b$ are the parameters to learn, tuned automatically by training ([backpropagation](../backpropagation/) + an [optimizer](../optimizer/)).
- **The non-linearity brought by the activation function** is the key to a network's ability to fit complex functions; without it, however deep, it is just a [linear model](../linear-model/).
- Every complex architecture is a different "arrangement" of neurons.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
