---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/u-net/
title: "U-Net"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**U-Net** is an **encoder–decoder** architecture with **skip connections**: the encoder downsamples step by step, compressing the data into coarser, more abstract multi-scale representations; the decoder then upsamples step by step to restore it, and the skip connections send each level's details along a "shortcut" to the matching restoration level. It is named after its shape, which resembles the letter **U**. This site's flagship forecasting model, **Kernel U-Net (KUN)**, is derived directly from it.

## Intuition

Think of it as the way a painter works:

- **Encoder (going down, seeing the big picture)**: first squint at the whole — gradually lower the resolution, discard local noise, and see clearly "where the subject is and what the overall trend looks like". Each downsampling step widens the view and makes the information more condensed.
- **Decoder (going up, filling in detail)**: then gradually zoom back in, redrawing the abstract big picture as a fine-grained output.
- **Skip connections (sideways, taking a shortcut)**: restoring with the decoder alone loses details such as edges and textures, because they were squashed out during downsampling. So the encoder's features at each level, **while still sharp**, are passed sideways directly to the matching decoder level. **The big picture comes from the depths, the details come from the skip connections**, and only by merging the two is the result both accurate and fine.

In one sentence: **U-Net works at several scales at once — the deep layers handle "long-range, coarse-grained" structure, the shallow layers handle "local, fine-grained" detail, and the skip connections keep either from being sacrificed for the other.**

## How it works

Let the encoder have $S$ scales. Encoding at level $s$:

$$
\mathbf{e}_s = \mathrm{Down}\big( f_s(\mathbf{e}_{s-1}) \big),\qquad \mathbf{e}_0 = \mathbf{x}
$$

- $\mathbf{x}$: the input (an image, or a time series window);
- $f_s$: the feature transform at this scale (a convolutional block in the original U-Net; KUN replaces it with a lightweight "kernel");
- $\mathrm{Down}$: downsampling (pooling or strided convolution), which shrinks the size and enlarges the receptive field;
- $\mathbf{e}_s$: the encoder output at level $s$; the deeper, the coarser and more abstract.

The lowest level is called the **bottleneck**, with the lowest resolution and the most condensed view. The decoder then upsamples level by level and merges in the skip connections:

$$
\mathbf{d}_s = g_s\big(\, [\,\mathrm{Up}(\mathbf{d}_{s+1});\ \mathbf{e}_s\,]\,\big)
$$

- $\mathrm{Up}$: upsampling (interpolation or transposed convolution), which scales the resolution back up;
- $[\,\cdot\,;\,\cdot\,]$: **concatenation** — the upsampled result is joined with the same-scale encoder features $\mathbf{e}_s$; this is the skip connection;
- $g_s$: the decoder's transform at this scale;
- $\mathbf{d}_s$: the decoder output at level $s$.

Going up level by level to the top yields an output the same size as the input. **The symmetric U shape + same-scale skip connections are U-Net's two signatures.**

Skip connections bring an extra benefit: they give the [gradient](../gradient/) a short path, alleviating [vanishing / exploding gradients](../vanishing-exploding-gradient/) in deep networks (the same principle as residual connections).

## A concrete example (1-D / time series version)

Applying U-Net to a sequence of length $L$, here is how the sizes change (each downsampling step halves the length):

```
Input       L = 96   ──┐ skip connection
  ↓ Down              │
Scale 1     48   ──┐  │
  ↓ Down            │  │
Scale 2     24   ─┐ │  │
  ↓ Down          │ │  │
Bottleneck  12    │ │  │   ← coarsest, longest-range view
  ↑ Up            │ │  │
Scale 2     24 ◄──┘ │  │   ← concatenate scale 2's details back in
  ↑ Up              │  │
Scale 1     48 ◄────┘  │
  ↑ Up                 │
Output      96 ◄───────┘   ← concatenate the finest details back in
```

On the way down the resolution goes $96\to48\to24\to12$, and at level 12 the model "takes in the whole picture at a glance"; on the way up it is restored step by step, and at each step the details stored at the corresponding scale are concatenated back in. The final output can be a segmentation mask (images) or a future sequence (forecasting).

## Why it matters / where it is used

- **Multi-scale is its soul**: it models "global structure" and "local detail" at the same time, which is crucial for many tasks.
- **Skip connections**: they preserve detail and give the gradient a shortcut, making deep networks easy to train.
- **Widely used**: medical image segmentation (where it made its name), image generation (the denoising backbone of diffusion models), super-resolution, and — time series forecasting.

## Relevance to time series forecasting (the focus of this site)

This is the heart of the site. **Kernel U-Net (KUN)** carries U-Net's ideas over to time series forecasting, with one key modification:

**1. Multi-scale along the time axis.** The encoder **downsamples** the time axis level by level: the raw series is "minute-level" fine-grained jitter, and after a few downsampling steps it becomes an "hour-level, day-level" coarse-grained trend — **the deeper you go, the longer the time span seen and the more the focus on long-range structure**. The decoder then **upsamples** level by level back to the original time resolution and outputs the future forecast.

**2. Skip connections preserve detail.** Downsampling inevitably loses high-frequency detail; the skip connections send the fine-grained information from before each scale's downsampling straight to the matching decoder level, **so the long-range trend (from the deep layers) and the short-term fluctuations (from the skip connections) are merged during restoration**, giving forecasts that are both stable and fine-grained.

**3. Lightweight "kernels" replace heavy convolutional blocks.** The original U-Net stacks parameter-heavy, compute-hungry convolutional blocks at each scale; **KUN replaces them with lightweight learnable "kernels"** that perform efficient local transforms at each scale. KUN thus keeps U-Net's multi-resolution advantage while cutting the cost dramatically.

**4. This is its key advantage over the Transformer.** A standard [Transformer](../transformer/) / [attention](../attention/) costs **$O(L^2)$** on a sequence of length $L$, which is slow and memory-hungry for long windows. KUN's multi-scale approach handles long-range dependencies on **shorter, coarse-grained sequences**, at much lower complexity — its core selling point for long-sequence forecasting. (Attention can still be embedded as a component at some scale; the two are not opposed.)

KUN's lineage in one sentence: **it is a U-Net-style multi-scale (multi-resolution) encoder–decoder forecasting model that replaces convolutional blocks with lightweight kernels and, at a cost far below $O(L^2)$, models long-range trends and short-term details simultaneously across different time scales.**

## Summary

- U-Net = **encoder downsampling + decoder upsampling + same-scale skip connections**, forming a U shape.
- **Deep layers handle long-range coarse structure, shallow layers / skip connections handle local fine detail**, with the scales working together.
- Skip connections preserve detail and give the gradient a shortcut.
- **Kernel U-Net (KUN)** brings all this to the time axis, replacing convolutional blocks with **lightweight kernels** to capture both long and short range at low cost — it is this site's flagship time series forecasting model.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
