---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/architectures/
title: "Common Architectures"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

A **network architecture** is the "skeleton design" describing how [neurons](../neuron/) are organized and connected. All of them are [neural networks](../neural-network/), yet structures tailored to different data and tasks differ enormously — this page gives you a quick tour of MLPs, CNNs, RNNs / LSTMs, Transformers and U-Nets, and shows where this site's featured model, **Kernel U-Net (KUN)**, fits in.

**Related:** [MLP](../mlp/) · [CNN](../cnn/) · [RNN](../rnn/) · [LSTM](../lstm/) · [Transformer](../transformer/) · [U-Net](../u-net/)

## Intuition: why we need different architectures

A "fully connected" [MLP](../mlp/) can in theory approximate any function, so why invent other architectures? Because **a good architecture builds the structure of the data into the network as a prior**, which saves parameters, makes training easier, and improves accuracy:

- The data has **local patterns** (neighboring pixels, neighboring time steps) → use convolution ([CNN](../cnn/)).
- The data has **sequential dependencies** (ordering, memory) → use recurrence ([RNN](../rnn/) / [LSTM](../lstm/)).
- The data has **long-range relationships** (any two points may be related) → use [attention](../attention/) ([Transformer](../transformer/)).
- The task needs **multiple scales + recovery of detail** (segmentation, forecasting) → use an encoder–decoder ([U-Net](../u-net/)).

Choosing an architecture essentially means choosing "which structural assumption to hand to the network".

## Architectures at a glance

**MLP (multilayer perceptron)** — a fully connected feedforward network, the most general and the simplest; in theory it can approximate any function. It does not exploit the structure of the data and its parameter count explodes on long inputs, but it is often a strong baseline and also a building block inside other architectures.
**Related:** [MLP](../mlp/) · [Forward propagation](../forward-propagation/) · [Activation functions](../activation-function/)

**CNN (convolutional neural network)** — slides shared convolution kernels to extract **local, translation-invariant** patterns, combined with downsampling to build multi-scale features from fine to coarse. Few parameters, parallelizable; 1D convolutions suit time series.
**Related:** [CNN](../cnn/)

**RNN (recurrent neural network)** — processes the input step by step in time order, using a hidden state as "memory" to carry history forward. A natural fit for sequences, but sequential and slow, and prone to [vanishing / exploding gradients](../vanishing-exploding-gradient/) on long sequences.
**Related:** [RNN](../rnn/)

**LSTM (long short-term memory)** — adds "gates" and a cell state to the RNN, so it can remember key information for longer and mitigates vanishing gradients; it was the workhorse of sequence modeling before the Transformer.
**Related:** [LSTM](../lstm/)

**Transformer** — based entirely on self-attention: it processes the whole sequence in parallel and connects any two points in a single step, giving strong long-range dependencies and good scalability; it is the backbone of modern sequence modeling and large models. The price is the $O(L^2)$ cost of attention.
**Related:** [Transformer](../transformer/) · [Attention](../attention/)

**U-Net** — an encoder–decoder with skip connections that downsamples level by level to see the big picture and upsamples to restore detail; the classic structure for multi-scale modeling.
**Related:** [U-Net](../u-net/)

## A comparison table

| Architecture | Core assumption | Strengths | Weaknesses |
|---|---|---|---|
| MLP | None (fully connected) | General mappings, strong baseline | Ignores structure, many parameters |
| CNN | Locality + translation invariance | Local patterns, multiple scales | Long-range relations need many stacked layers |
| RNN/LSTM | Sequential memory | Sequential dependencies | Slow (sequential), long range is hard |
| Transformer | Any two points may be related | Long-range dependencies, scalable | High $O(L^2)$ cost |
| U-Net | Multiple scales + reconstruction | Segmentation, multi-resolution tasks | Heavy convolution blocks |

## Relevance to time series forecasting: where KUN fits

Time series forecasting can use any of the architectures above: flatten the input and feed it to an [MLP](../mlp/), use a 1D [CNN](../cnn/) to capture local waveforms, use an [LSTM](../lstm/) to remember history, or use a [Transformer](../transformer/) to relate distant time steps. But long-horizon forecasting shares a common difficulty — **you must see long-range trends clearly, preserve short-term detail, and keep computation (especially attention's $O(L^2)$) under control.**

This site's featured model, **Kernel U-Net (KUN)**, was built precisely for this: it is a **[U-Net](../u-net/)-style multi-scale (multi-resolution) encoder–decoder model** that downsamples level by level **along the time axis** to obtain several views from fine to coarse, then upsamples to reconstruct the future forecast, with skip connections preserving fine-grained information. Unlike the original U-Net, KUN **replaces heavy convolution blocks with lightweight learnable "kernels"**, so that at a cost **far below $O(L^2)$** it models long-range trends and short-term fluctuations simultaneously across different time scales.

You can think of KUN as a time-series-forecasting architecture that "**stands in the U-Net lineage, absorbs the multi-scale intuition of CNNs, and avoids the quadratic cost of Transformers**".

## Summary

- Architecture = building the structure of the data into the network as a prior; choosing an architecture means choosing a structural assumption.
- MLP is general, CNN is local, RNN/LSTM is sequential, Transformer is long-range, U-Net is multi-scale.
- **Kernel U-Net (KUN)** is a U-Net-style multi-scale forecasting model that uses lightweight kernels to gain efficiency on long sequences — the protagonist of this site.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
