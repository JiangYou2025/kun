---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/transformer/
title: "Transformer"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**The Transformer** is a [neural network](../neural-network/) architecture built entirely on [attention](../attention/) (self-attention). It abandons recurrence, **processing the whole sequence in parallel and connecting any two positions directly in a single step**, which lets it capture long-range dependencies efficiently. It is the dominant backbone of modern sequence modeling (including every large language model).

## Intuition

Before the Transformer, sequence modeling relied mainly on [RNNs](../rnn/) / [LSTMs](../lstm/): like reading a book word by word, information was passed along step by step through "memory". The problem is that the further you read, the more the earlier information gets diluted, and the processing must be **sequential**, with no way to parallelize.

The Transformer takes a completely different approach: **lay out the whole sequence at once and let every position "look at" every other position simultaneously**, deciding for itself whom to attend to based on relevance. No loss from "passing messages along", no sequential bottleneck. The price is that it has no built-in sense of order, so you have to **tell it explicitly where each position is** (positional encoding).

## How it works

A Transformer is a stack of identical **blocks**. Each block contains two sub-layers, each wrapped with a residual connection and layer normalization:

**Sub-layer 1: multi-head self-attention**

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left( \frac{QK^{\top}}{\sqrt{d_k}} \right) V
$$

where $Q, K, V$ are all linear projections of the input, $d_k$ is the dimension of each head, and $\sqrt{d_k}$ provides scaling (see [attention](../attention/) for details). Multi-head = several sets in parallel, each attending to different aspects, then concatenated.

**Sub-layer 2: position-wise feed-forward network** (really just a small [MLP](../mlp/) applied independently to each position)

$$
\mathrm{FFN}(x) = W_2\,\sigma\!\left(W_1 x + b_1\right) + b_2
$$

- $W_1, W_2$: the two layers of weights (the hidden dimension is usually expanded 4×);
- $\sigma$: the [activation function](../activation-function/) (e.g. ReLU/GELU).

**Residual + layer normalization** wraps each sub-layer, alleviating [vanishing / exploding gradients](../vanishing-exploding-gradient/) and making deep stacks trainable:

$$
x \leftarrow \mathrm{LayerNorm}\big(x + \mathrm{Sublayer}(x)\big)
$$

**Positional encoding**: because self-attention is "blind" to order, vectors carrying position information are added to the input, for example the sinusoidal form

$$
PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right),\qquad
PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)
$$

- $pos$: position index; $i$: dimension index; $d$: model dimension. Sines and cosines at different frequencies give each position a unique "fingerprint".

{% include fviz/attention-heat.html %}

## A concrete example

A minimal encoder block (built into PyTorch):

```python
import torch, torch.nn as nn

layer = nn.TransformerEncoderLayer(
    d_model=64, nhead=4,           # model dimension 64, 4 attention heads
    dim_feedforward=256,           # FFN hidden layer 64*4
    batch_first=True,
)
encoder = nn.TransformerEncoder(layer, num_layers=2)

x = torch.randn(8, 96, 64)         # (batch, sequence length=96, features=64)
out = encoder(x)                   # (8, 96, 64); every position has now fused global information
```

Each time step of `x` goes in carrying only its own information, and comes out having "seen" all 96 steps and fused them according to relevance.

## Why it matters / where it is used

- **Parallel training**: the whole sequence is computed at once, far faster than RNNs, which must run sequentially.
- **Strong long-range dependencies**: any two positions are connected directly in one step, so relationships do not decay with distance.
- **Scalable**: the deeper the stack and the more data, the better the results — the very foundation of the large-model era.
- There are also many Transformer variants for time series (Informer, Autoformer, PatchTST, and others).

## Relevance to time series forecasting

The Transformer brings attention's "long-range direct connection" advantage to forecasting, directly relating distant time steps across cycles. But it inherits attention's fundamental weakness: self-attention costs **$O(L^2)$** time and memory on a sequence of length $L$. Time series history windows easily run to thousands or even tens of thousands of steps, and the quadratic cost makes a standard Transformer slow and memory-hungry.

This site's flagship model, **Kernel U-Net (KUN)**, offers a different path: borrowing the **multi-scale encoder–decoder** structure of [U-Net](../u-net/), it downsamples step by step along the time axis and models long-range dependencies on **shorter, coarse-grained sequences** at a lower cost, instead of brute-forcing $O(L^2)$ over the full-length sequence. It should be stressed that **this is not "attention vs. Transformer"** — attention can still be embedded in KUN as a local component at some scale; what KUN changes is the overall complexity structure, trading in multi-resolution for efficiency on long sequences.

## Common misconceptions

- **"The Transformer naturally understands order"**: it does not. Order information is injected entirely through **positional encoding**; remove it and shuffling the input leaves the result unchanged.
- **"Attention is $O(L)$"**: standard self-attention is $O(L^2)$, which is exactly why long-sequence forecasting needs efficient variants (or a multi-scale structure like KUN).
- **"The Transformer always beats RNNs/[CNNs](../cnn/)/MLPs"**: not necessarily. For short-to-medium time series with limited data, a simple [MLP](../mlp/) or a multi-scale model is often cheaper and more accurate.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
