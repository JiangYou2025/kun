---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/vanishing-exploding-gradient/
title: "Vanishing / Exploding Gradients"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**Vanishing / exploding gradients** describe what happens when, during [backpropagation](../backpropagation/) in a deep network, gradients **shrink toward 0** (vanish) or **blow up** (explode) exponentially because of **repeated multiplication**, so that the early layers cannot learn or training simply collapses. It is the number-one obstacle to training very deep / very long networks.

## Intuition

Backpropagation sends the error signal back **layer by layer, multiplying as it goes**. Imagine a number being multiplied by the same factor $r$ over and over:

- If $r=0.5$, after 10 layers it becomes $0.5^{10}\approx0.001$ — the signal has all but **vanished**; the layers near the input receive gradients of almost 0 and **cannot learn**.
- If $r=1.5$, after 10 layers it becomes $1.5^{10}\approx58$, and after 30 layers it is astronomical — the gradient **explodes**, the parameter updates are huge, the loss turns into NaN, and training **collapses**.

Only when this factor stays close to 1 can the signal pass through many layers intact. **Depth itself amplifies the problem** — the more layers, the more multiplications.

## How it works: where the repeated multiplication comes from

Recall the backpropagation recurrence:

$$
\delta^{(l)} = \big(W^{(l+1)\top}\,\delta^{(l+1)}\big)\odot \sigma'\big(z^{(l)}\big)
$$

Going from the output layer back to layer $l$, the gradient accumulates a long chain of products of $W$ and $\sigma'$. Roughly, the magnitude of the gradient at layer $l$ is proportional to

$$
\prod_{k=l}^{L} \big\| W^{(k)} \big\| \cdot \big| \sigma'(z^{(k)}) \big|
$$

Term by term:

- $\sigma'(z)$: the derivative of the [activation function](../activation-function/). **The derivative of the sigmoid is $\le0.25$**, so the repeated product must decay exponentially → vanishing gradients.
- $\big\|W^{(k)}\big\|$: the size of the weights. If the weights are generally $>1$, the product grows exponentially → exploding gradients.
- **Product greater than 1 → explosion; less than 1 → vanishing.** The critical point is to keep each layer's effective factor as close to 1 as possible.

## A concrete example

A 10-layer network with a sigmoid in every layer, assuming a per-layer gradient factor of about $0.2$:

$$
0.2^{10} = 1.024\times10^{-7}
$$

The first layer receives a gradient only one ten-millionth of the output layer's — **it is effectively not learning**. Conversely, if the weights make the factor $1.3$:

$$
1.3^{10} \approx 13.8,\qquad 1.3^{30}\approx 2620
$$

After 30 layers the gradient is amplified more than a thousandfold, and a single update can push the parameters to NaN.

## How to mitigate it

This is the common motivation behind several key innovations in [deep learning](../dl/):

- **Change the activation function**: use [ReLU](../activation-function/) (whose derivative is constantly 1 on the positive side) instead of sigmoid/tanh, fundamentally avoiding the decay from multiplying derivatives $<1$.
- **Good weight initialization**: Xavier / He initialization keeps each layer's variance stable, with an initial factor close to 1.
- **Normalization**: [BatchNorm](../batchnorm/) / LayerNorm bring each layer's inputs back to a stable distribution, preventing numerical drift.
- **Residual connections (ResNet)**: add an "identity shortcut" $y = x + F(x)$, giving the gradient a **non-decaying direct path** back to the shallow layers.
- **Gradient clipping**: when the gradient norm exceeds a threshold, scale it back down — the most direct emergency measure **against explosion**.
- **Gating**: the [LSTM](../lstm/) uses gates + a cell state specifically to keep [RNN](../rnn/) gradients from vanishing over long sequences.

```python
# Gradient clipping: the usual one-liner that prevents explosion during training
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

## Relevance to time series forecasting

A sequence model unrolls the network along **time steps**: **the longer the lookback window, the more equivalent layers, and the more gradient multiplications** — so vanishing / exploding gradients are especially severe in long-sequence forecasting. This is precisely why plain [RNNs](../rnn/) cannot learn long-term dependencies, and why the [LSTM](../lstm/) came into being.

This site's flagship model, [Kernel U-Net (KUN)](../../kun/), uses **multi-scale downsampling** to compress a long sequence into a shorter representation before processing it, effectively shortening the path the gradient has to travel and naturally alleviating the problem. When training KUN on long lookback windows, it is still advisable to combine it with [Adam](../adam/), a moderate [learning rate](../learning-rate/), and gradient clipping to keep training stable.

## Summary

- Root cause: in backpropagation, gradients are **products**; factors $<1$ make them **vanish**, factors $>1$ make them **explode**, and depth/sequence length amplifies the effect.
- Vanishing → the shallow layers cannot learn; exploding → the loss becomes NaN.
- The combined remedy: **ReLU + good initialization + normalization + residuals + gradient clipping + gating (LSTM)**.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
