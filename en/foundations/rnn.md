---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/rnn/
title: "RNN (Recurrent Neural Network)"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

A **Recurrent Neural Network (RNN)** is a network that reads a sequence one time step at a time and uses a "hidden state" to carry information from the past all the way to the present. It is naturally suited to data with an order, such as text, speech and time series.

## Intuition

Imagine you are reading a sentence: "The weather today is very …". By this point you have already built up a bit of "context" in your head, so you can guess that the next word is probably "nice" or "hot". You don't look at each word in isolation; you **update your memory as you read**, and that memory in turn shapes how you understand the next word.

This is exactly what an RNN does. It has a "memory vector" called the **hidden state** $h_t$:

- Each time a new input $x_t$ arrives, it blends $x_t$ with the previous memory $h_{t-1}$ to compute a new memory $h_t$;
- This $h_t$ is used both to produce the current output and to be passed on to the next time step.

An ordinary [neural network](../neural-network/) is a "one-shot deal" — input goes in, output comes out, and each case is independent. The key difference in an RNN is that **the same set of weights is reused at every time step**, and memory flows along the time axis through $h_t$.

## Mathematical formulation

The core of an RNN is a **recurrence**. Let $x_t$ be the input at time $t$ and $h_t$ the memory:

$$
h_t = \tanh\!\left(W_x\, x_t + W_h\, h_{t-1} + b\right)
$$

Symbol by symbol:

- $x_t$: the input vector at time step $t$ (for instance one day's sales, or the vector of a word).
- $h_{t-1}$: the hidden state of the previous time step, i.e. "the memory so far". The initial $h_0$ is usually set to all zeros.
- $h_t$: the updated memory at this time step.
- $W_x$: the weight matrix that maps the input $x_t$ into the memory space.
- $W_h$: the weight matrix that transforms the old memory $h_{t-1}$ before mixing it into the new memory.
- $b$: the bias vector.
- $\tanh$: the [activation function](../activation-function/), which squashes the result into $(-1, 1)$ and adds nonlinearity to the network.

The output (if a prediction is needed) is usually produced by one more layer:

$$
\hat{y}_t = W_y\, h_t + b_y
$$

Note: $W_x, W_h, W_y, b, b_y$ are **shared across all time steps** — this is where the word "recurrent" comes from. A sequence of length 100 does not use 100 sets of parameters; it uses the same set 100 times.

## Backpropagation through time (BPTT) and vanishing gradients

How does an RNN learn? Still through [backpropagation](../backpropagation/), except that it has to travel backward along the chain of "time", hence the name **Backpropagation Through Time** (BPTT).

"Unroll" the RNN along time and it looks like a very deep network: the output at step $T$ depends on $h_T$, $h_T$ depends on $h_{T-1}$, and so on down to $h_1$. When computing gradients, the [chain rule](../chain-rule/) multiplies a long string of derivatives together, in which this term appears again and again:

$$
\frac{\partial h_t}{\partial h_{t-1}} = W_h^{\top}\,\operatorname{diag}\!\big(\tanh'(\cdot)\big)
$$

To carry an error from $T$ steps back, this factor has to be multiplied $T$ times, giving a magnitude roughly like $\lambda^{T}$ (where $\lambda$ is the "effective size" of these factors):

- If $\lambda < 1$, the product quickly tends to 0 → **vanishing gradients**: the network cannot learn long-range dependencies ("it forgets what was said at the beginning");
- If $\lambda > 1$, the product blows up → **exploding gradients**: training becomes numerically unstable.

This is the typical form the [vanishing / exploding gradient](../vanishing-exploding-gradient/) problem takes in sequence models. Since $\tanh'$ is at most 1 and close to 0 far from the origin, a plain RNN is especially prone to vanishing gradients and **finds it hard to remember information from dozens of steps earlier**. Exploding gradients are usually mitigated with "gradient clipping", while vanishing gradients gave rise to the [LSTM](../lstm/).

## A concrete example

Let's walk through the numbers of a tiny one-dimensional RNN to see how memory accumulates. Let $W_x = 0.5,\ W_h = 0.9,\ b = 0$, the input sequence $x = [1, 1, 1]$, and $h_0 = 0$:

$$
\begin{aligned}
h_1 &= \tanh(0.5\times 1 + 0.9\times 0) = \tanh(0.5) \approx 0.462\\
h_2 &= \tanh(0.5\times 1 + 0.9\times 0.462) = \tanh(0.916) \approx 0.724\\
h_3 &= \tanh(0.5\times 1 + 0.9\times 0.724) = \tanh(1.152) \approx 0.818
\end{aligned}
$$

You can see the memory $h_t$ steadily accumulating. Here is the equivalent PyTorch code:

```python
import torch, torch.nn as nn

rnn = nn.RNN(input_size=1, hidden_size=8, batch_first=True)
x = torch.randn(4, 20, 1)        # (batch size=4, time steps=20, features=1)
out, h_n = rnn(x)
print(out.shape)   # (4, 20, 8): hidden state at every time step
print(h_n.shape)   # (1, 4, 8): hidden state at the last step
```

`out` gives the memory at each step, and `h_n` is the "final memory" after reading the whole sequence, which is often fed into one more layer to make a prediction.

## Relevance to time series forecasting

The RNN was once **the classic workhorse of time series forecasting**: it updates the hidden state step by step with the observations of the past few days, then uses the final state to predict the future. It handles variable-length sequences naturally and can model temporal dependencies.

But it has two serious weaknesses:

- **It must compute step by step in time order**, so it cannot be parallelized like convolution/attention, making both training and inference slow on long sequences;
- **Vanishing gradients** make it hard to capture very long dependencies, which is especially painful for long-horizon forecasting.

These limitations pushed people toward architectures that can be parallelized and can model across scales, such as the [Transformer](../transformer/) and this site's flagship multi-scale model **Kernel U-Net (KUN)** — which borrows the multi-resolution idea of [U-Net](../u-net/) to extract and fuse features at different time scales, making it both fast and good at long-horizon forecasting.

## Summary

- An RNN maintains a memory that flows through time using the shared-weight recurrence $h_t = \tanh(W_x x_t + W_h h_{t-1} + b)$.
- It is trained with **BPTT**; the products of derivatives cause **vanishing/exploding gradients**, so a plain RNN struggles to remember long-range dependencies.
- It computes sequentially, is hard to parallelize and inefficient on long sequences — exactly the problems that the [LSTM](../lstm/) and the multi-scale model KUN set out to solve.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
