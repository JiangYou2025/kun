---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2020 · Physics"
permalink: /en/history/e/fno/
title: "The Fourier Neural Operator (Li et al., 2020)"
lead: "A convolution only sees a local neighbourhood. Move the convolution into the frequency domain as a global operation, and you can learn PDE solution operators that are independent of the grid resolution."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

Right after [PINNs and DeepONet](../pinn-deeponet/), "learning PDE solution operators with neural networks" became a hot goal: train a model that maps an input function (such as an initial condition or a parameter field) to the output solution function, giving the solution instantly for new inputs and sparing the cost of rerunning traditional numerical methods each time. The difficulty is that the receptive field of an ordinary convolutional network is local, whereas PDE solutions are often determined by **global interactions**.

### The problem

An ideal operator learner should satisfy two requirements: **globality** — a single operation should let distant information interact; and **discretization invariance** — it should still work when trained on a coarse grid and evaluated on a fine one, because what it learns is a continuous operator rather than a discrete mapping on a fixed grid. An ordinary CNN satisfies neither: its receptive field is local, and changing the resolution requires retraining. **How can one build a learnable operator that is both global and grid-independent?**

### Other currents of the time (and their limits)

- **CNN surrogate models**: treat the PDE solution as image regression; the receptive field is local and **tied to a fixed resolution**, so they fail when the grid changes.
- **Graph neural network operators**: can handle irregular meshes, but global information has to accumulate over many steps of message passing, making long-range interactions costly.
- **DeepONet**: pioneered operator learning, but its branch–trunk architecture is less direct than frequency-domain methods at generalizing across resolutions and expressing global kernels.

### The method

The heart of the FNO is the **Fourier layer**, which takes the convolution theorem all the way: convolution in the spatial domain equals pointwise multiplication in the frequency domain. Each layer Fourier-transforms the features $$v$$, multiplies the low-frequency modes by learnable weights $$R$$, and transforms back, yielding a **global** kernel integral operation:

$$ (\mathcal{K}v)(x)=\mathcal{F}^{-1}\big(R\cdot \mathcal{F}(v)\big)(x) $$

In practice only the first few low-frequency modes are kept, $$R\in\mathbb{C}^{k_{\max}\times d\times d}$$, and combined with a pointwise linear branch $$Wv$$ and a nonlinearity $$\sigma$$ to form a layer:

$$ v_{t+1}(x)=\sigma\Big(Wv_t(x)+\mathcal{F}^{-1}\big(R\cdot\mathcal{F}(v_t)\big)(x)\Big) $$

Because the weights act on **frequency modes** rather than on grid points, the same set of parameters can be applied at any resolution — this is where the resolution independence comes from; computing it with the FFT makes the whole layer efficient.

### Results

On parametric PDEs such as Burgers, Darcy flow and Navier–Stokes, the FNO was more accurate than earlier neural operators, and its inference was **several orders of magnitude faster** than traditional numerical solvers. It can be trained on low-resolution data and transferred zero-shot to high-resolution inference (zero-shot super-resolution), significantly reducing data and compute costs.

### Significance and outlook

The FNO injected classical [Fourier analysis](../fourier/) and frequency-domain thinking into deep operator learning, offering a global, efficient, resolution-independent paradigm. It directly advanced data-driven scientific computing, especially large-scale spatio-temporal forecasting — applying resolution-independent frequency-domain operators to the Earth system gave rise to [FourCastNet and other neural weather models](../neural-weather/). On the central theme of time series — "learning how dynamics evolve in space and time" — the FNO provides a powerful tool from the physics side.
