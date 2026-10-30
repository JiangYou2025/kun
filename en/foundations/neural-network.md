---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/neural-network/
title: "Neural Networks"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

A **neural network** is a mathematical model made of a large number of simple computing units — [neurons](../neuron/) — connected in layers. It computes its output through [forward propagation](../forward-propagation/) and learns its parameters from its mistakes through [backpropagation](../backpropagation/), thereby mapping "inputs" to the "outputs" we want.

## Intuition

Imagine an assembly line. Raw material (the input data, say the temperature at the past 96 time steps) enters at one end, passes through one "workshop" after another, and a finished product comes out at the other end (say a forecast of the temperature at the next 24 time steps).

Each workshop has many workers (neurons). What each worker does is extremely simple:

1. Multiply each of the numbers coming from the previous layer by a "degree of importance" (a weight $w$);
2. Add them all up, then add a bias $b$;
3. Pass the result through a non-linear "switch" (an [activation function](../activation-function/)).

A single worker is dumb, but thousands of workers cooperating in layers can, as a whole, fit extremely complex patterns. **The power of a neural network comes not from any single neuron, but from layered composition and a vast number of parameters.**

## The math

The computation of one neuron is a "weighted sum + activation":

$$
a = \sigma\!\left( \sum_{i=1}^{n} w_i x_i + b \right)
$$

- $x_i$: the $i$-th component of the input (the output of the previous layer);
- $w_i$: the corresponding weight, expressing how important this input is; a parameter to be learned;
- $b$: the bias, giving the neuron an adjustable baseline;
- $\sum_{i=1}^{n} w_i x_i + b$: the weighted sum, a linear operation;
- $\sigma(\cdot)$: the activation function (e.g. ReLU, Sigmoid), which introduces non-linearity;
- $a$: the output (activation) of the neuron.

Writing a whole layer of neurons together in matrix form is more compact:

$$
\mathbf{h}^{(l)} = \sigma\!\left( \mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)} \right)
$$

- $\mathbf{h}^{(l-1)}$: the output vector of layer $l-1$ (for the first layer, the input $\mathbf{x}$);
- $\mathbf{W}^{(l)}$: the weight matrix of layer $l$; each row corresponds to one neuron of the layer;
- $\mathbf{b}^{(l)}$: the bias vector of layer $l$;
- $\mathbf{h}^{(l)}$: the output of layer $l$.

The whole network applies this formula from layer 1 all the way to layer $L$: input in, output out. This journey is **forward propagation**.

### Why activation functions are essential

Remove $\sigma$, and stacking layers, $\mathbf{W}^{(3)}(\mathbf{W}^{(2)}(\mathbf{W}^{(1)}\mathbf{x}))$, is still just a single linear transformation $\mathbf{W}'\mathbf{x}$ — any number of layers is equivalent to one, unable to express curves, kinks or thresholds, or any other non-linear relationship. **Activation functions are the key to making neural networks "deep" and "powerful".**

## How it learns

When the network is first initialized, its weights are random and its output is basically a wild guess. Learning loops through three steps:

1. **Forward propagation**: compute the prediction $\hat{y}$ with the current parameters;
2. **Compute the loss**: measure the gap between the prediction and the true value $y$ with a [loss function](../loss-function/), for example the mean squared error
   $$ \mathcal{L} = \frac{1}{N}\sum_{j=1}^{N}\left(\hat{y}_j - y_j\right)^2 $$
   where $N$ is the number of samples, $\hat{y}_j$ the prediction and $y_j$ the true value;
3. **[Backpropagation](../backpropagation/) + [optimizer](../optimizer/)**: use the [chain rule](../chain-rule/) to compute the [gradient](../gradient/) of the loss with respect to every parameter, $\frac{\partial \mathcal{L}}{\partial w}$, then nudge each parameter in the opposite direction of the gradient:
   $$ w \leftarrow w - \eta \,\frac{\partial \mathcal{L}}{\partial w} $$
   $\eta$ is the [learning rate](../learning-rate/), which controls the size of each step.

Repeat these three steps thousands of times over large amounts of data, and the parameters gradually converge to values that give good predictions.

## A concrete example

Build a 3-layer network in PyTorch style that maps 96 steps of history to a 24-step forecast:

```python
import torch.nn as nn

net = nn.Sequential(
    nn.Linear(96, 128),   # layer 1: 96 dims -> 128 dims
    nn.ReLU(),            # activation
    nn.Linear(128, 64),   # layer 2: 128 -> 64
    nn.ReLU(),
    nn.Linear(64, 24),    # output layer: 64 -> 24-step forecast
)

x = torch.randn(32, 96)  # a batch of 32 samples, each with 96 steps of history
y_hat = net(x)           # shape (32, 24)
```

These few lines are a complete, trainable neural network: the three `Linear` layers are the weight matrices, `ReLU` is the activation function, and what `net(x)` does internally is exactly the chain of matrix multiplications above.

## Relevance to time series forecasting

Time series forecasting is, in essence, learning a function $f$ that maps the history window $[x_{t-95}, \dots, x_t]$ to the future $[x_{t+1}, \dots, x_{t+24}]$. Neural networks are precisely good at **learning such complex mappings automatically from data**, with no need to specify the form of the model by hand.

Different tasks have given rise to different structures (all of them neural networks): [CNNs](../cnn/) for local patterns, [RNNs](../rnn/) / [LSTMs](../lstm/) for sequential dependencies, [attention](../attention/) and the [Transformer](../transformer/) for long-range relationships, while the multi-scale forecasting model promoted on this site, **Kernel U-Net (KUN)**, is built on the [U-Net](../u-net/) structure. Understanding the general neural network framework is a prerequisite for understanding these specialized [architectures](../architectures/).

## Summary

- Neural network = many neurons connected in layers, parameterized by **weights** and **biases**.
- **Forward propagation** computes the output; **backpropagation + an optimizer** updates the parameters.
- **Activation functions** bring non-linearity and are the fundamental reason "depth" is meaningful.
- The same framework can be tailored into different architectures such as the [MLP](../mlp/), CNN, Transformer and U-Net.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
