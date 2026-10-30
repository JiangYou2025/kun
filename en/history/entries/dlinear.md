---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2022 · Computer science"
permalink: /en/history/e/dlinear/
title: "The Single-Linear-Layer Challenge (DLinear, 2022)"
lead: "Split the series into trend and remainder and feed each to one linear map — a model this naive somehow beat a whole crowd of Transformers at long-horizon forecasting, forcing a pointed question: do we really need attention?"
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Chapter 10 · Large models and KUN](../../10/).

### Background

Around 2020, long-sequence time-series forecasting (LSTF) became a hot race. A string of "X-formers" — Informer, Autoformer, FEDformer and others — appeared one after another, using sparse attention, series decomposition and frequency-domain operators to push the forecast horizon to hundreds or thousands of steps, while the error curves in the papers stepped down year after year. The dominant narrative was clear: the longer the sequence, the more you need attention to capture long-distance dependencies.

### The problem

Yet these models shared an awkward feature: their architectures grew ever heavier, but whether the gains really came from "attention" itself had never been rigorously controlled for. Almost all of them included an overlooked preprocessing step — **series decomposition** (separating the trend from the seasonal/remainder component). **If you keep the decomposition and remove all the attention, how much worse do the results get?** Nobody had seriously asked.

### Other currents of the time (and their limits)

- **Attention above all (all kinds of Transformer variants)**: assumes by default that long-range dependencies must be modelled with self-attention. Limits: self-attention is permutation-invariant and does not inherently "understand" temporal order, so extra positional encodings are needed to patch it up; and its $$O(L^2)$$ complexity forces all sorts of approximations, which introduce new biases of their own.
- **Pure statistical baselines ([ARIMA](../box-jenkins/), exponential smoothing)**: interpretable and robust, but hard to scale to high-dimensional multivariate, long-window settings, and often skipped as "outdated".
- Neither side answered the question: how much of the improvement brought by complex architectures actually comes from the most basic linear trend extrapolation?

### The method

DLinear gives an almost provocative answer: first apply a **moving-average decomposition**, then map the trend and remainder components **each through a single linear layer** directly onto the future window, and add the results. With a look-back window $$X\in\mathbb{R}^{L}$$ decomposed into a trend $$X_t$$ and a remainder $$X_s=X-X_t$$, the forecast is

$$ \hat{Y} = W_t X_t + W_s X_s,\qquad W_t,W_s\in\mathbb{R}^{T\times L} $$

where $$T$$ is the forecast horizon and $$W_t,W_s$$ are two learnable weight matrices — the entire model has no nonlinearity, no attention and no recurrence. In essence it learns one set of "linear weights across time" for the trend and one for the remainder, which amounts to learning, for each future time step, a weighted average of the history. It is so simple that its parameter count and compute are one or two orders of magnitude lower.

### Results

On several standard LSTF benchmarks (electricity, traffic, weather, ETT and others), DLinear's forecast error **matched or even beat** the complex Transformers of the time, while training fast, using little memory and being almost fully interpretable — the weight matrices can be visualized directly as "how the future is a weighting of the past". The result was a bucket of cold water, reminding the whole field that much of the gain actually came from decomposition and linear extrapolation, not from attention.

### Significance and outlook

DLinear's value is not that "linear models can win", but that it established an **honest, strong baseline** and a methodological challenge: before stacking complex architectures on time series, prove that you actually need them. This reflection directly gave rise to two lines of work — one helping [Transformers](../patchtst/) find the right way to work on time series (patching, channel independence), the other returning to linear-time structures such as state space models and convolutions. It also echoes the central claim of [Kernel U-Net](../kun/): separate the "multi-scale structure" from the "per-layer operator" — the structure (decomposition, a U-shaped hierarchy) is often what does the heavy lifting, while the operator can stay light. Whenever we discuss today what backbone time series [foundation models](../foundation-models/) should use, DLinear's question — "are you sure you need attention?" — is always in the room.
