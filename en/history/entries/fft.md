---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1965 · Computer science"
permalink: /en/history/e/fft/
title: "The Fast Fourier Transform (Cooley · Tukey, 1965)"
lead: "Bringing the discrete Fourier transform down from O(N²) to O(N log N), a divide-and-conquer algorithm made large-scale spectral analysis an everyday task on computers — and quietly transformed countless disciplines."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

The idea of Fourier analysis is old: any sequence can be decomposed into a superposition of sine waves of different frequencies. The **discrete Fourier transform (DFT)** maps an $$N$$-point sequence onto $$N$$ frequency components and is the core tool of spectral analysis. In the 1960s, as digital computers were just becoming widespread, people were eager to use them to analyse the frequency structure of seismic, radar, communication and economic series.

### The problem

Computing the DFT directly from its definition means multiplying every output by every input and summing, a cost of $$O(N^2)$$. When $$N$$ reaches tens of thousands, that is hundreds of millions of multiplications — the machines of the day would take forever. **Everyone knew how to use spectral analysis in theory, but in practice it was strangled by computational cost.** Large-scale frequency analysis was almost infeasible.

### Other currents of the time (and their limits)

- **Time-domain methods (autocorrelation, AR fitting)**: avoid explicit spectral computation, but seeing the frequency structure clearly still requires a transform, and they are not very intuitive for broadband signals.
- **Analog filter banks**: split frequency bands with hardware circuits; inflexible and of limited precision, with no freedom to adjust the resolution.
- **Direct DFT computation**: mathematically correct, but its $$O(N^2)$$ cost makes it infeasible for large $$N$$ — exactly the bottleneck waiting to be broken.

### The method

The DFT is defined as (with $$W_N=e^{-i2\pi/N}$$):

$$ X_k=\sum_{n=0}^{N-1} x_n\, W_N^{\,nk},\qquad k=0,\dots,N-1 $$

The key insight of Cooley–Tukey is **divide and conquer**: when $$N$$ is even, split the sum into two halves by even and odd indices,

$$ X_k=\underbrace{\sum_{m} x_{2m} W_{N/2}^{\,mk}}_{E_k}\;+\;W_N^{\,k}\underbrace{\sum_{m} x_{2m+1} W_{N/2}^{\,mk}}_{O_k} $$

so that one $$N$$-point DFT becomes two $$N/2$$-point DFTs, which are then combined with a single "**butterfly**" operation: $$X_k=E_k+W_N^k O_k$$ and $$X_{k+N/2}=E_k-W_N^k O_k$$ (using $$W_N^{k+N/2}=-W_N^k$$). Splitting recursively, the total cost follows from the recurrence $$T(N)=2T(N/2)+O(N)$$:

$$ T(N)=O(N\log N) $$

For $$N=2^{20}$$, this is about fifty thousand times faster than $$O(N^2)$$.

### Results

From then on, spectral analysis of long series could be done instantly on an ordinary computer. The FFT quickly became one of the most widely used algorithms in signal processing, communications, imaging, geophysics and beyond, and is hailed as one of the most important algorithms of the 20th century. Fast convolution, filtering and correlation computations all gained orders-of-magnitude speedups from it.

### Significance and outlook

For time series, the FFT made the **periodogram** and power-spectrum estimation truly practical, establishing the frequency domain as an analytical paradigm on a par with the time domain, and providing an efficient tool for studying Slutsky-style shaping by filters. Numerically, it also powers fast convolution, which speeds up computation with [ARMA/ARIMA](../box-jenkins/) models and the processing of long series. A seemingly pure algorithmic trick ended up reshaping the way people "see" signals — frequency was no longer expensive.
