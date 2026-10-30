---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/forward-propagation/
title: "Forward Propagation"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Forward propagation** is the process of "feeding" input data through a network from the first layer to the last, applying "weighted sum + activation" layer by layer, until the prediction comes out. It is the half of a [neural network](../neural-network/) that "makes predictions" (the other half, [backpropagation](../backpropagation/), is responsible for "learning").

## Intuition

Picture a neural network as an **assembly line**. Raw material (the input features) enters at one end, and at each workstation (each layer) it is processed once: first mixed according to a recipe (a linear weighted sum), then passed through a "quality-control valve" (the [activation function](../activation-function/)) that decides how much of the signal gets through. The material flows forward all the way and never turns back; the finished product coming out of the exit is the network's **prediction**.

The word "forward" emphasizes exactly this **one-way flow**: data only travels toward the output. Only when we want to adjust the network based on its error does information travel back the other way — that is backpropagation.

## Mathematical formulation

Suppose the network has $L$ layers. Write the input vector of layer $l$ as $a^{(l-1)}$ (that is, the previous layer's output); the layer has a weight matrix $W^{(l)}$ and a bias vector $b^{(l)}$. The layer then does two things:

$$
z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}
$$

$$
a^{(l)} = \sigma\big(z^{(l)}\big)
$$

Symbol by symbol:

- $a^{(l-1)}$: the **activation output** of layer $l-1$ (layer 0 is the raw input $x$, i.e. $a^{(0)} = x$).
- $W^{(l)}$: the **weight matrix** of layer $l$, of shape $(\text{neurons in this layer} \times \text{neurons in the previous layer})$.
- $b^{(l)}$: the **bias** of layer $l$, giving each [neuron](../neuron/) an adjustable baseline.
- $z^{(l)}$: the **weighted sum** (also called the pre-activation, the value before activation).
- $\sigma(\cdot)$: the **activation function**, e.g. ReLU or Sigmoid (applied element-wise).
- $a^{(l)}$: this layer's output, which becomes the next layer's input.

Computing these two steps from $l=1$ all the way to $l=L$, the final $a^{(L)} = \hat{y}$ is the network's prediction. The whole chain can be written as a nested function:

$$
\hat{y} = \sigma^{(L)}\Big(W^{(L)} \, \sigma^{(L-1)}\big(\cdots \sigma^{(1)}(W^{(1)} x + b^{(1)}) \cdots\big) + b^{(L)}\Big)
$$

{% include fviz/backprop-graph.html %}

## A concrete example

Take a minimal network: 2-dimensional input, a hidden layer of 2 neurons with ReLU, and an output layer of 1 neuron (linear). Given

$$
x = \begin{bmatrix} 1 \\ 2 \end{bmatrix},\quad
W^{(1)} = \begin{bmatrix} 0.5 & -0.5 \\ 1.0 & 0.0 \end{bmatrix},\quad
b^{(1)} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}
$$

Step one, the weighted sum:

$$
z^{(1)} = \begin{bmatrix} 0.5\cdot1 + (-0.5)\cdot2 \\ 1.0\cdot1 + 0\cdot2 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \end{bmatrix}
= \begin{bmatrix} -0.5 \\ 1.0 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \end{bmatrix}
= \begin{bmatrix} -0.5 \\ 0 \end{bmatrix}
$$

Through ReLU (negatives set to zero):

$$
a^{(1)} = \mathrm{ReLU}(z^{(1)}) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Oops — both hidden neurons have been "switched off". This is a reminder that ReLU makes some neurons output 0 for certain inputs. Finally, the output layer (with $W^{(2)} = [1, 1],\, b^{(2)} = 0.3$):

$$
\hat{y} = 1\cdot0 + 1\cdot0 + 0.3 = 0.3
$$

Checking with code:

```python
import numpy as np

x  = np.array([1.0, 2.0])
W1 = np.array([[0.5, -0.5], [1.0, 0.0]])
b1 = np.array([0.0, -1.0])
W2 = np.array([1.0, 1.0])
b2 = 0.3

z1 = W1 @ x + b1          # [-0.5, 1.0] -> +b1 -> [-0.5, 0.0]
a1 = np.maximum(0, z1)    # ReLU -> [0, 0]
y  = W2 @ a1 + b2         # 0.3
print(z1, a1, y)          # [-0.5  0. ] [0. 0.] 0.3
```

## Why it matters / where it is used

- **It is all of inference.** When a deployed model makes predictions, what runs is forward propagation — fast and simple.
- **It is the first half of training.** Every training step first runs a forward pass to get $\hat{y}$, then computes the [loss](../loss-function/) $\mathcal{L}(\hat{y}, y)$, and only then can backpropagation compute the gradients.
- The intermediate values $z^{(l)}, a^{(l)}$ saved during the forward pass are reused by [backpropagation](../backpropagation/), which is exactly why [automatic differentiation](../autodiff/) frameworks (PyTorch/TensorFlow) manage the "computation graph" for you automatically.

## Why it matters for time series forecasting

For sequence models such as [RNNs](../rnn/) and [LSTMs](../lstm/), forward propagation unrolls along the **time steps**: the hidden state at step $t$ depends on step $t-1$, and information flows forward step by step. This site's flagship model, [Kernel U-Net (KUN)](../../kun/), is a multi-scale architecture: its forward pass progressively downsamples a long look-back window and then progressively upsamples it back — but at heart it is still the same "transform the input layer by layer to get a prediction". Understanding forward propagation is the first step to understanding how any forecasting model works.

## Summary

- Forward propagation = **data flowing one way from input to output**, applying "linear transform + activation" layer by layer.
- Core formulas: $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$.
- It is both **prediction** itself and **the first step of the training loop**; its intermediate values are kept for backpropagation.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
