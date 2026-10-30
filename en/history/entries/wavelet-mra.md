---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1989 · Mathematics"
permalink: /en/history/e/wavelet-mra/
title: "Multiresolution Analysis (Mallat, 1989)"
lead: "Fourier sees frequency but not time, and windowing nails the resolution in place. Mallat built a zoomable \"microscope\": a wide field of view for low frequencies, a fine brush for high ones."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the 1980s, the two main tools of signal analysis each had a hard flaw. The [Fourier transform](../fourier/) breaks a signal entirely into global sine waves; its frequency resolution is excellent, but it completely loses "when an event happened". [Gabor's short-time Fourier transform (STFT)](../gabor-stft/) adds a sliding window and gains a joint time–frequency view, but once the window is chosen, the resolution of the whole time–frequency plane is fixed. Meanwhile, Morlet, Grossmann, Meyer, Daubechies and others, converging from seismic exploration and from pure mathematics, were constructing a family of wavelet bases that could "dilate and translate". What was missing was a unifying framework to organize these scattered constructions, together with a fast algorithm like the FFT.

### The problem

The fixed window of the STFT brings a fundamental contradiction: low-frequency signals need long time windows to be seen clearly, high-frequency transients need short windows to be localized, and no single window length can satisfy both. **Could the analysis window adapt to frequency — automatically widening for low frequencies and narrowing for high ones?** Going further, could a signal be organized like a pyramid into multiple resolution levels "from coarse to fine", with fast recursion between levels?

### Other approaches of the time (and their limits)

- **Windowed Fourier / Gabor transform**: time–frequency resolution is locked by a single window length, unable to accommodate both long-period trends and brief transients.
- **Pyramid image coding (Burt–Adelson, 1983)**: engineering already had "coarse-to-fine" multiscale representations, but they lacked an orthogonal, perfectly reconstructible mathematical foundation; they were redundant, and the choice of scales was arbitrary.
- **Early continuous wavelet transforms**: theoretically elegant but highly redundant and computationally expensive, with no discrete orthogonal basis and no fast algorithm, making them hard to put into practice.

### Method

Mallat proposed **multiresolution analysis (MRA)**: construct a sequence of nested approximation subspaces $$\cdots\subset V_1\subset V_0\subset V_{-1}\subset\cdots$$, with the difference between adjacent scales filled by wavelet detail spaces $$W_j$$, so that $$V_{j-1}=V_j\oplus W_j$$. The scaling function $$\varphi$$ and the wavelet $$\psi$$ satisfy the two-scale (refinement) relations:

$$ \varphi(t)=\sqrt{2}\sum_k h_k\,\varphi(2t-k),\qquad \psi(t)=\sqrt{2}\sum_k g_k\,\varphi(2t-k) $$

where $$h_k$$ is a low-pass filter and $$g_k$$ a high-pass filter. At each scale the signal expands as

$$ f(t)=\sum_k a_{J,k}\,\varphi_{J,k}(t)+\sum_{j\le J}\sum_k d_{j,k}\,\psi_{j,k}(t),\qquad \psi_{j,k}(t)=2^{-j/2}\psi(2^{-j}t-k) $$

The basis functions $$\psi_{j,k}$$ automatically adjust their width through the scale $$2^j$$: large scales correspond to wide time windows and low frequencies with high frequency resolution, small scales to narrow time windows that localize high-frequency transients — this is exactly "adaptive resolution". The accompanying **fast wavelet transform (Mallat's algorithm)** reduces all of this to convolution of coefficients followed by downsampling by two, recursing level by level:

$$ a_{j+1,k}=\sum_n h_{n-2k}\,a_{j,n},\qquad d_{j+1,k}=\sum_n g_{n-2k}\,a_{j,n} $$

Its complexity is only $$O(N)$$, even lower than the FFT's $$O(N\log N)$$.

### Impact

MRA unified wavelets from scattered constructions into a single "filter-bank pyramid", delivering theory and algorithm in one stroke: orthogonal bases guarantee perfect, non-redundant reconstruction, and the fast transform let it spread rapidly through image compression, denoising and edge detection. It directly gave rise to standards such as JPEG2000 and became a mainstay of time–frequency analysis for non-stationary signals.

### Significance and outlook

MRA gave time series analysis a "zoom microscope": long-period trends and brief anomalies can be extracted level by level within one framework, which suits **non-stationary** data such as finance, heart rate and earthquakes particularly well. Its contrast with the STFT is, in essence, a paradigm shift from "fixed resolution" to "scale-adaptive resolution". This multiscale, coarse-to-fine idea later echoed in the pyramid architectures of deep learning and in wavelet scattering networks — seeing the world in layers has since become a universal intuition of signal processing.
