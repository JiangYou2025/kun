---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1946 · Control / Communications"
permalink: /en/history/e/gabor-stft/
title: "Putting a Timestamp on Frequency (Gabor, 1946)"
lead: "Fourier tells you which frequencies a signal contains, but not when they occur. Gabor used a sliding window to give the spectrum a time coordinate for the first time — at the price of an uncertainty trade-off."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

[Fourier analysis](../fourier/) is the cornerstone of signal processing: any signal can be decomposed into a superposition of sinusoids of different frequencies. But the Fourier transform is **global** — it compresses an entire signal into a single spectrum, telling you "which frequencies are present" while erasing "when they occur". For signals whose frequency content changes over time, such as speech, music or radar echoes, this is a fatal gap. In 1946, Dennis Gabor proposed a spectral representation with time resolution in his paper "Theory of Communication".

### The problem

A piece of music that plays low notes first and high notes later shows both low and high frequencies in its Fourier spectrum, with no sign of which came first. **How can one obtain a joint representation that carries frequency information while preserving localization in time?** And can time and frequency resolution both be made arbitrarily fine, or is there some fundamental limit?

### Other approaches of the time (and their limits)

- **The global Fourier transform**: excellent frequency resolution, zero time resolution. Well suited to stationary signals, powerless against non-stationary signals whose frequencies drift over time.
- **Looking at the raw waveform in the time domain**: watching the waveform rise and fall over time gives clear time localization, but the frequency content cannot be read off. The two extremes each hold one end.
- **Hard segmentation followed by Fourier analysis**: cut the signal into non-overlapping pieces and transform each separately. The direction is right, but the rectangular hard cut introduces severe spectral leakage at the boundaries (Gibbs ringing), and there was no theory to guide the choice of segment length.

### Method

Gabor's approach was to multiply the signal by a sliding **window function** $$g$$ and then take the Fourier transform of the windowed piece. This is the **short-time Fourier transform (STFT)**:

$$ X(\tau,\omega)=\int_{-\infty}^{\infty} x(t)\,g(t-\tau)\,e^{-i\omega t}\,dt $$

The window centre $$\tau$$ gives the **time** coordinate and $$\omega$$ gives the **frequency** coordinate, so the spectrum acquires a timestamp; $$\lvert X(\tau,\omega)\rvert^2$$ is the spectrogram. Gabor particularly advocated the **Gaussian window**, because it attains the lower bound of the joint time–frequency uncertainty — which is exactly the Gabor limit, or uncertainty principle:

$$ \Delta t\,\cdot\,\Delta \omega \ \ge\ \tfrac12 $$

where $$\Delta t,\Delta\omega$$ are the spreads (standard deviations) of the signal in time and in frequency. It shows that **time resolution and frequency resolution cannot both be had**: a narrow window gives precise timing and blurred frequency; a wide window does the opposite. Once the window is chosen, the resolution of the whole time–frequency map is locked in by this trade-off.

### Impact

The STFT made the analysis of non-stationary signals possible: formants of speech moving over time, Doppler shifts of radar targets, fault frequencies in machine vibrations could all be "seen" in a spectrogram. The optimal time–frequency concentration of the Gaussian window made the Gabor representation the standard starting point of joint time–frequency analysis.

### Significance and outlook

Gabor turned "frequency" from a global notion into a local one, opening up the entire field of **time–frequency analysis**. The resolution compromise imposed by a fixed window is precisely what the **wavelet transform** would later overcome — wavelets use windows that scale adaptively with frequency (short windows for high frequencies, long windows for low ones) to achieve multiresolution analysis. From spectrograms and Mel spectra to the front-end features of deep speech and audio models, when we handle "signals whose frequency changes" today, the first step is still very often Gabor's sliding window.
