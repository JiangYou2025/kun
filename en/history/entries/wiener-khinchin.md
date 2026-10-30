---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1934 · Mathematics"
permalink: /en/history/e/wiener-khinchin/
title: "The Duality of Autocorrelation and Power Spectrum (Khinchin, 1934)"
lead: "A random signal has no Fourier transform — its energy is infinite. Khinchin got around the obstacle: transform not the signal itself but its autocovariance, and \"correlation\" and \"spectrum\" become two sides of the same coin."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

The [Fourier transform](../fourier/) can break a deterministic signal into frequencies, but it requires the signal to be integrable (finite energy). A **stationary random process** (thermal noise, ocean waves, sunspots) keeps fluctuating forever; its sample paths neither decay nor repeat, so the ordinary Fourier transform diverges and cannot be defined. Yet engineers could clearly measure the "power spectrum" of noise — energy concentrated more in some frequency bands than others. In 1934 Aleksandr Khinchin (building on Norbert Wiener's 1930 work on generalized harmonic analysis) provided the rigorous bridge, known as the **Wiener–Khinchin theorem**.

### The problem

A stationary process has no convergent Fourier transform, **so what exactly is the "power spectrum" the Fourier transform of? How should the frequency content of a stationary signal be rigorously defined?** Transforming the random sample path directly does not work; one must find an object that both represents the process and is "tame" enough to be transformed.

### Other approaches of the time (and their limits)

- **Direct spectral estimation with the periodogram**: Fourier-transform a stretch of the sample and take the squared modulus as the spectrum. It is an empirical quantity defined on a finite sample, but it is **inconsistent** — its variance does not shrink as the sample grows, so the estimate keeps jittering wildly; in theory, it also sidesteps the fundamental difficulty that "a random signal has no Fourier transform".
- **Deterministic harmonic decomposition (the [Fourier](../fourier/) school)**: assumes the signal is a sum of a few fixed sine waves. For purely random signals with continuous spectra, this "find a few spectral lines" approach is systematically distorted.
- The crux: people wanted to transform the **signal** directly, but a stationary random signal is itself not transformable.

### Method

Khinchin's central idea: **do not transform the signal; transform its autocovariance function**. The autocovariance of a stationary process

$$ \gamma(\tau)=\mathbb E\big[(X_t-\mu)(X_{t+\tau}-\mu)\big] $$

is a well-behaved, integrable deterministic function. The theorem asserts that the autocovariance $$\gamma(\tau)$$ and the **power spectral density** $$S(\omega)$$ form a Fourier transform pair:

$$ S(\omega)=\int_{-\infty}^{\infty}\gamma(\tau)\,e^{-i\omega\tau}\,d\tau,\qquad \gamma(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S(\omega)\,e^{i\omega\tau}\,d\omega $$

So $$S(\omega)\ge 0$$ describes how power is distributed across frequencies, and $$\gamma(0)=\frac1{2\pi}\int S(\omega)\,d\omega$$ is exactly the total variance (total power) of the process. "Correlation structure in the time domain" and "energy distribution in the frequency domain" were proven fully equivalent and invertibly translatable into each other.

### Impact

The power spectrum thereby gained an unambiguous mathematical definition, and spectral analysis a solid foundation. The theorem also showed why the naive periodogram is unreliable and inspired **consistent** spectral estimators such as windowed smoothing and Blackman–Tukey. Any stationary process can be studied equivalently in the time domain (autocorrelation) or the frequency domain (power spectrum), switching between them as convenient.

### Significance and outlook

The Wiener–Khinchin theorem is the key link between the [Fourier frequency domain](../fourier/) and [Kolmogorov's stochastic processes](../kolmogorov/), and the cornerstone of all spectral methods. It is precisely why [AR/ARMA](../yule-ar/) models can read spectral peaks (resonances) in the frequency domain; it also underpins Wiener filtering, optimal prediction, and noise analysis in oceanography and communications. Today, the duality "autocorrelation $$\leftrightarrow$$ power spectrum" taught in signal processing courses, and even the use of spectral features of sequences in deep models, are direct continuations of this 1934 theorem.
