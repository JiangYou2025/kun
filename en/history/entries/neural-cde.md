---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2020s · Mathematics"
permalink: /en/history/e/neural-cde/
title: "Hidden States Driven by Paths (Neural CDE · Signature Kernels, 2020s)"
lead: "Let the hidden state be driven by the observation path itself, dz=f(z)dX: neural controlled differential equations and signature kernels turn irregular sampling and missing values into a natural stroke along a continuous path."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Real-world sequences often "don't play by the rules": in medical monitoring, high-frequency finance and sensor networks, data are sampled unevenly, values go missing, and channels run at different paces. Yet mainstream deep models (RNNs, Transformers) assume by default that the input is an **evenly spaced, aligned** discrete sequence, and when faced with irregular sampling they can only patch things up with interpolation, zero-filling or extra masks. Meanwhile, mathematics had long had a mature language for handling continuous paths: controlled differential equations (CDEs) and the **path signature** from [rough path](../rough-paths/) theory. Neural CDEs and signature kernels plug exactly this language into neural networks.

### The problem

A Neural ODE lets the hidden state evolve autonomously through time, $$dz=f(z)\,dt$$, but **once the initial value is given, it no longer depends on subsequent observations**: it cannot absorb newly arriving data along the way. For time series, what we need is precisely for **the observations themselves to keep driving** the hidden state, and this driving must naturally accommodate irregular data at any time and on any channel. **How can the hidden state be driven by the "data path" rather than by the "clock"?**

### Other approaches of the time (and their limits)

- **Interpolation + a standard RNN/Transformer**: first fill the irregular data onto a regular grid, then feed the model. Limits: interpolation fabricates data and distorts statistical properties, and the missingness pattern ("why a value is missing" often carries information) is erased.
- **Neural ODE**: continuous-time and elegant, but the hidden state evolves only with time and cannot be "corrected" when observations arrive, so it is ill-suited to absorbing new data online.
- **RNNs with time-gap features (GRU-D and others)**: approximate the handling of gaps with decay gates; an engineering patch rather than a native continuous-time formulation, with unclear theoretical properties.

### Method

A Neural CDE first interpolates the discrete observations $$(t_i,x_i)$$ into a continuous, differentiable path $$X(t)$$, then makes the hidden state follow a **controlled** differential equation, driven by the control path $$X$$:

$$ z(T) = z(t_0) + \int_{t_0}^{T} f_\theta\big(z(t)\big)\,dX(t) $$

Intuitively, $$dX$$ is a small increment of the data path, and $$f_\theta(z)$$ determines how that increment changes the hidden state; the integral is computed numerically with an ODE solver. Because the driving quantity is $$dX$$ rather than $$dt$$, during periods with no observations the path is flat and the hidden state glides smoothly through, while a new observation takes effect as soon as it arrives. **Irregular sampling and missing values are unified as "the path does not change over certain intervals"**, with no special handling required. Complementary to this are **signature kernels**: [rough path](../rough-paths/) theory gives the "signature" of a path, a collection of iterated integrals

$$ S(X)^{i_1\cdots i_k} = \idotsint_{t_0<u_1<\cdots<u_k<T} dX^{i_1}_{u_1}\cdots dX^{i_k}_{u_k} $$

which is a universal, parameterization-independent feature of the path. Signature kernels use it to measure the similarity between two paths, turning sequence learning into a kernel method on path space that is likewise robust to how the data were sampled.

### Impact

On sequence tasks with irregular sampling, long gaps of missing data and online arrival (such as clinical time series classification), Neural CDEs and signature methods are more accurate and more stable than "interpolation + RNN", and come with solid continuous-time theoretical guarantees; the hidden state can be queried at any time, which naturally supports asynchronous multichannel data.

### Significance and outlook

Neural CDEs and signature kernels connect [Itô](../ito/)'s stochastic analysis and rough path theory with deep learning, providing a principled paradigm for "continuous-time sequence modelling". They share a common origin with state-space models such as [Mamba](../mamba/): both view a sequence as samples of a continuous dynamical system, one driven by $$dX$$, the other modulated by selective parameters. On the road toward time series [foundation models](../foundation-models/), how to make a single large model robustly ingest heterogeneous series with wildly different sampling schemes is one of the core challenges; the "sampling-agnostic" view offered by paths and signatures may be a class of operators worth including in future pluggable architectures such as [Kernel U-Net](../kun/). From deterministic cycles to stochastic processes, and on to continuous hidden states driven by paths, the worldview of time series has deepened by one more layer.
