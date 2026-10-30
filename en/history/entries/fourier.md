---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1807 · Mathematics"
permalink: /en/history/e/fourier/
title: "The Birth of the Frequency Domain (Fourier, 1807)"
lead: "How does the temperature of a heated metal bar dissipate over time? To solve the heat equation, Fourier claimed that any function can be broken down into a sum of sine waves — a statement his peers dismissed as “impossible”, and one that opened up the entire world of the frequency domain."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

In the early 19th century, one of the central problems of analysis was **heat conduction**. In 1807 Joseph Fourier submitted a paper to the French Academy of Sciences on the diffusion of heat in solid bodies; the equation he had to solve is the one later named after him, the **heat equation**. The difficulty was that the initial temperature distribution could be a function of any shape, while the tools mathematicians of the time could use to solve such problems exactly worked only for "simple" functions such as sines and cosines. Fourier boldly asserted that any such initial distribution could be written as a superposition of a series of sine and cosine waves, so that the whole problem could be solved "wave by wave, then added back together".

### The problem

Sine waves are periodic, smooth and forever oscillating; an arbitrary temperature curve, by contrast, can have sharp corners, be defined piecewise, and be entirely non-periodic. **Why should adding up infinitely many smooth sine waves be able to approximate an arbitrary function with corners and no periodicity?** This was so counter-intuitive at the time that Lagrange and other referees refused to believe it, and the paper was at first not accepted.

### Other currents of the time (and their limits)

- **Power series / Taylor expansion**: writes a function as a superposition of $$1,x,x^2,\dots$$. It works beautifully for analytic functions, but it requires the function to be sufficiently smooth and is essentially a "local" approximation, ill-suited to periodic phenomena and global oscillation.
- **The d'Alembert–Euler vibrating-string controversy**: in the 18th century, whether "an arbitrary initial shape can be represented by a trigonometric series" had been debated for decades, and the prevailing view leaned towards **no**, holding that trigonometric series could only represent "well-behaved" functions. This conservative judgement underestimated the expressive power of the trigonometric system.
- The common root of these limits: there was not yet a rigorous language of convergence and function spaces. People substituted "can a formula be written down" for "in what sense are they equal", and so could neither affirm the claim nor refute it.

### The method

Fourier's core idea: expand a function on a **basis of sine waves**. For a function with period $$2\pi$$, the Fourier series is

$$ f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\big(a_n\cos nt + b_n\sin nt\big),\qquad a_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\cos nt\,dt,\;\; b_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\sin nt\,dt $$

Each coefficient $$a_n,b_n$$ measures how strong the component at frequency $$n$$ is. For a non-periodic function, the sum becomes an integral, giving the **Fourier transform**:

$$ \hat f(\omega)=\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt $$

$$\hat f(\omega)$$ gives the complex amplitude of the signal at frequency $$\omega$$: $$|\hat f(\omega)|$$ is the strength of that frequency, while the phase encodes its time shift. The key property of the sine basis is **orthogonality**: different frequencies are independent of one another, so "finding the content at a given frequency" becomes a single inner-product integral — clean and simple.

### Results

The heat equation was solved completely: each frequency component decays independently as $$e^{-k\omega^2 t}$$, high frequencies dissipating quickly and low frequencies lingering, so the physical picture of "sharp edges being smoothed away first" can be read straight from the mathematics. More profoundly, Fourier analysis gave people a pair of "frequency glasses": from then on one could ask of any signal, "which frequencies is it made of?"

### Significance and outlook

The Fourier transform links the "time domain" and the "frequency domain" as a pair of mirror images, and became the mother tongue of all signal processing, spectral analysis and frequency-domain methods for time series. It leads directly to the [power spectrum and the Wiener–Khinchin theorem](../wiener-khinchin/) for stationary processes — the autocovariance and the power spectrum are precisely a Fourier transform pair — and it underpins the periodogram, filtering, the sampling theorem and the fast Fourier transform (FFT). Two centuries later, from audio coding to spectral representations of [diffusion processes](../brownian-motion/) and even frequency-domain attention in deep models, the same step of Fourier's is still at work: measuring the world with sine waves.
