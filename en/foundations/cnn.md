---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/cnn/
title: "CNN (Convolutional Neural Networks)"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

A **CNN (Convolutional Neural Network)** slides small, compact **convolution kernels** over the data to extract **translation-invariant local patterns**. It first shone on images, but it works just as well on time series — you simply replace the 2D convolution with a **1D convolution** along the time axis.

## Intuition

Imagine sweeping a small magnifying glass (the convolution kernel, say of width 3) over a time series from left to right. At each position, the magnifying glass answers one question: "Does this short stretch contain the shape I care about?" — such as a rising edge, a spike or a step.

The key is that **the same magnifying glass uses the same parameters at every position**. This brings two benefits:

- **Translation invariance**: whether a spike appears at the beginning or the end of the series, the same kernel can recognize it;
- **Parameter sharing**: unlike an [MLP](../mlp/), which gives each position its own set of weights, a CNN uses a single set of kernel parameters for the whole series, so it has far fewer parameters and is less prone to [overfitting](../overfitting/).

## How it works

1D convolution: a kernel $\mathbf{w}$ of length $k$ slides over the input $\mathbf{x}$, and the $t$-th output value is:

$$
y_t = \sum_{i=0}^{k-1} w_i \, x_{t+i} + b
$$

- $x_{t+i}$: the input value at time $t+i$;
- $w_i$: the $i$-th weight of the kernel, a parameter to be learned;
- $k$: the kernel size, i.e. how wide a local window is seen each time;
- $b$: the bias;
- $y_t$: the output at that position, a point on the "feature map".

A convolutional layer is usually followed by a nonlinear [activation function](../activation-function/) and then by **pooling** for downsampling — for example, max pooling takes the maximum in each small window:

$$
p_t = \max\left(y_{2t},\, y_{2t+1}\right)
$$

After downsampling the sequence gets shorter (here its length is halved), but the range each point "sees" (its **receptive field**) gets larger. **Stacking multiple convolutional layers with downsampling lets the network go from local details to patterns at progressively larger scales** — this is the origin of the multi-scale idea behind U-Net and KUN later on.

A few common knobs:

- **stride**: how many steps the kernel jumps each time; a stride > 1 also downsamples;
- **padding**: pad both ends with zeros so the output has the same length as the input;
- **dilation**: leave gaps between the kernel's sampling points to enlarge the receptive field without adding parameters (causal dilated convolutions, as in WaveNet/TCN, are common for time series).

## A concrete example

Convolve the input $\mathbf{x} = [3, 3, 5, 5, 5]$ with a length-3 kernel $\mathbf{w} = [1, 0, -1]$ (a simple "edge detector"), with no padding, stride 1 and $b=0$:

- $y_0 = 1\cdot3 + 0\cdot3 + (-1)\cdot5 = -2$
- $y_1 = 1\cdot3 + 0\cdot5 + (-1)\cdot5 = -2$
- $y_2 = 1\cdot5 + 0\cdot5 + (-1)\cdot5 = 0$

The output $[-2, -2, 0]$ gives a nonzero response at the 3→5 "jump" and 0 on the flat part. This is the kernel "detecting local change".

The PyTorch version:

```python
import torch.nn as nn

conv = nn.Conv1d(in_channels=1, out_channels=16,
                 kernel_size=3, padding=1)   # 16 kernels, output of equal length
# Input shape: (batch, channels=1, time length)
```

## Why it matters / where it is used

- **Efficient**: few parameters, parallelizable computation, fast training.
- **A specialist in local features**: good at catching "shape-like" patterns — periodic waveforms, abrupt changes, seasonal segments.
- **The cornerstone of multi-scale modeling**: downsampling layer after layer forms a fine-to-coarse feature pyramid, the structural basis of the image segmentation network [U-Net](../u-net/) and of many time series models.

## Relevance to time series forecasting

**1D convolution + downsampling** along the time axis is the conceptual ancestor of **Kernel U-Net (KUN)**, the model this site focuses on. CNNs teach us one core intuition:

> **Looking at a series at different time resolutions captures both short-term details and long-term trends at once.**

The lowest convolutional layers see "minute-level" jitter; after a few rounds of downsampling, the network sees "hour-level and day-level" trends. KUN inherits this **multi-scale (multi-resolution)** idea: it downsamples step by step along the time axis to obtain several views from fine to coarse, but **replaces the heavy convolution blocks with lighter learnable "kernels"**, so it covers both long- and short-range information at a lower computational cost. Understanding 1D convolution and downsampling is therefore the first step toward understanding KUN.

## Summary

- A CNN slides **shared convolution kernels** to extract **local, translation-invariant** patterns.
- **Downsampling + multiple layers** enlarge the receptive field step by step, forming fine-to-coarse multi-scale features.
- 1D convolution is a natural fit for time series and is the conceptual source of the multi-scale structure of [U-Net](../u-net/) and Kernel U-Net.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
