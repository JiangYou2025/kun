---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/lstm/
title: "LSTM"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**Long Short-Term Memory (LSTM)** is a special kind of [RNN](../rnn/). It uses a "cell state" highway and three "gates" to actively decide what to remember and what to forget, which lets it retain very long-range dependencies and alleviates the [vanishing gradient](../vanishing-exploding-gradient/) problem of plain RNNs.

## Intuition

In a plain RNN, memory is repeatedly "kneaded" by $\tanh$ at every step, growing fainter as it is passed along until almost nothing is left after a few dozen steps. LSTM takes a different approach: it opens a separate **cell state** $c_t$ as a "main memory road", on which information can **travel straight through almost unchanged**, with little interference.

How is memory added and removed, then? LSTM sets up three **gates**, each a small switch that outputs a value in $0\sim1$:

- **forget gate**: decides which parts of the old memory to discard (0 = forget everything, 1 = keep everything);
- **input gate**: decides how much of this step's new information gets written into memory;
- **output gate**: decides how much to read out of memory as the current output.

An analogy: $c_t$ is a conveyor belt; the forget gate removes unwanted goods from the belt, the input gate puts new goods on it, and the output gate decides which goods to show to the outside at this moment.

## Gate equations

Let $x_t$ be the current input and $h_{t-1}$ the hidden state of the previous step. The three gates and the candidate memory are as follows ($\sigma$ is the sigmoid [activation function](../activation-function/), with output in $0\sim1$):

$$
\begin{aligned}
f_t &= \sigma\!\big(W_f [h_{t-1}, x_t] + b_f\big) &\text{(forget gate)}\\
i_t &= \sigma\!\big(W_i [h_{t-1}, x_t] + b_i\big) &\text{(input gate)}\\
o_t &= \sigma\!\big(W_o [h_{t-1}, x_t] + b_o\big) &\text{(output gate)}\\
\tilde{c}_t &= \tanh\!\big(W_c [h_{t-1}, x_t] + b_c\big) &\text{(candidate memory)}
\end{aligned}
$$

Then the cell state and hidden state are updated:

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
\qquad
h_t = o_t \odot \tanh(c_t)
$$

Symbol by symbol:

- $[h_{t-1}, x_t]$: **concatenates** the previous memory and the current input into one long vector.
- $f_t, i_t, o_t$: the three gate vectors; each component lies between $0\sim1$ and acts element-wise as a "switch".
- $\tilde{c}_t$: the "candidate new memory" this step wants to write, with values in $(-1,1)$.
- $\odot$: **element-wise multiplication** (the Hadamard product), i.e. using the gates as valves that scale each dimension.
- $c_t$: the cell state, $=$ (old memory kept according to $f_t$) $+$ (new memory written according to $i_t$).
- $h_t$: the hidden state exposed as output, the part of the cell state that, after $\tanh$, is read out according to $o_t$.
- $W_\ast, b_\ast$: each gate's own weights and biases, shared across all time steps.

## Why the cell state can retain long-term information

The key is the **additive** update $c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$.

Recall the trouble with RNNs: $\partial h_t / \partial h_{t-1}$ repeatedly multiplies by $W_h$ and $\tanh'$, and the long product tends to 0. For an LSTM, differentiating along the cell state gives:

$$
\frac{\partial c_t}{\partial c_{t-1}} = f_t
$$

If the forget gate $f_t \approx 1$, the gradient **flows back almost unchanged**, and even after multiplying over many steps it does not collapse to 0. This "addition + gate close to 1" path is called the **constant error carousel (CEC)**, and it is the fundamental reason an LSTM can remember information from hundreds of steps earlier without easily suffering from vanishing gradients.

Intuitively: information "goes straight" along $c_t$ instead of being "repeatedly multiplied by matrices and squashed", so it can travel far.

## A concrete example

Suppose one dimension of the cell state currently holds $c_{t-1} = 0.8$ (representing the information "the sentence began with a plural subject"). At this step:

- forget gate $f_t = 0.95$ → keeps this information almost entirely;
- input gate $i_t = 0.10$, candidate $\tilde{c}_t = 0.5$ → writes in only a little new information;
- output gate $o_t = 0.60$.

Then:

$$
c_t = 0.95\times 0.8 + 0.10\times 0.5 = 0.76 + 0.05 = 0.81
$$

$$
h_t = 0.60 \times \tanh(0.81) \approx 0.60 \times 0.670 = 0.402
$$

The memory goes from $0.8 \to 0.81$, barely changed — "plural subject" is carried safely forward, to be read out through the output gate when it is actually needed (for example, to decide whether the verb is singular or plural). In PyTorch, you simply call:

```python
import torch, torch.nn as nn

lstm = nn.LSTM(input_size=1, hidden_size=16, num_layers=1, batch_first=True)
x = torch.randn(8, 96, 1)             # (batch=8, 96 time steps, 1 feature)
out, (h_n, c_n) = lstm(x)
print(out.shape)             # (8, 96, 16): hidden state at every step
print(h_n.shape, c_n.shape)  # h and c of the last step
```

## What it means for time series forecasting

Before Transformers became popular, LSTM was **the standard answer for long-sequence forecasting**: it can remember distant trends and cycles (such as yearly seasonality) and is much more stable than a plain RNN, so it was widely used to forecast sales, electricity, weather and more.

But it still **inherits the sequential computation of RNNs** — it must compute step by step, so training and inference on long sequences are slow, and it still struggles with very long forecast horizons. This pushed people toward structures that can be parallelized and work across scales: the [Transformer](../transformer/), and the **Kernel U-Net (KUN)** featured on this site. KUN borrows the multi-resolution idea of [U-Net](../u-net/) to model several time scales simultaneously, which both sidesteps the speed bottleneck of "step-by-step recursion" and captures long-range structure better.

## Summary

- LSTM = RNN + **cell state $c_t$** + **three gates: forget/input/output**.
- The memory update is **additive**: $c_t = f_t\odot c_{t-1} + i_t\odot\tilde{c}_t$; the gates decide what to remember, what to forget and what to read.
- $\partial c_t/\partial c_{t-1} = f_t \approx 1$ forms the constant error carousel, which **alleviates vanishing gradients** and allows long dependencies to be remembered.
- It is still a sequential model that is hard to parallelize — long-horizon forecasting drove the move to the [Transformer](../transformer/) and the multi-scale KUN.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
