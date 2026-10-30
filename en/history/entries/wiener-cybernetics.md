---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1948 · Control / Communications"
permalink: /en/history/e/wiener-cybernetics/
title: "Feedback, Prediction and Optimal Filtering (Wiener, 1948)"
lead: "From anti-aircraft fire control to Cybernetics, Wiener turned \"predicting the future from a noisy past\" into a solvable optimal-filtering equation in the frequency domain, and established feedback as a language shared by machines and living things."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

During the Second World War, Norbert Wiener studied how anti-aircraft guns could aim at manoeuvring aircraft: the aircraft position measured by radar was noisy, and shells had a flight time, so one had to **predict the aircraft's future position**. This forced "noisy observation + prediction" into a mathematical problem. After the war, in his 1948 *Cybernetics: or Control and Communication in the Animal and the Machine*, he elevated these ideas into an interdisciplinary programme — the origin of the word "cybernetics"; its technical core is the **Wiener optimal filter**.

### The problem

The observation $$y(t)=s(t)+n(t)$$ is the sum of the true signal and noise. We want to design a filter $$h$$ that is **linear and may use only the past and present (causal)** to estimate a target $$d(t)$$ from $$y$$ ($$d=s$$ for denoising, $$d(t)=s(t+\lambda)$$ for prediction), minimizing the mean squared error. **Under the causality constraint, what is the frequency response of the optimal filter?**

### Other approaches of the time (and their limits)

- **Empirical low-pass/smoothing filters**: set the cutoff frequency by intuition to suppress noise. Usable, but neither tailored to the actual spectra of signal and noise nor optimal, and weak at prediction.
- **Unconstrained frequency-domain deconvolution**: if all future data may be used, the optimal filter is the simple spectral ratio $$S_{sy}/S_{yy}$$. But it is **non-causal** and cannot be implemented in real time — the real difficulty lies precisely in making it causal.
- **Deterministic trajectory extrapolation**: treat the aircraft's track as a deterministic function and extrapolate. Neither robust nor optimal in the face of manoeuvres and measurement noise, it ignores the random spectral structure of the signal.

### Method

Assume signal and noise are stationary with known spectra. The optimal **causal** filter is determined by the **Wiener–Hopf equation**, whose solution hinges on **spectral factorization**: write the observation spectrum as $$S_{yy}(\omega)=\lvert\Phi^{+}(\omega)\rvert^2$$, where $$\Phi^{+}$$ and its inverse are both causal (minimum phase). For pure denoising, the frequency response of the optimal filter is

$$ H(\omega)=\frac{1}{\Phi^{+}(\omega)}\left[\frac{S_{sy}(\omega)}{\overline{\Phi^{+}(\omega)}}\right]_{+} $$

where $$[\,\cdot\,]_{+}$$ means **taking the causal part** (discarding the impulse response at negative times). Intuitively: first use $$1/\Phi^{+}$$ to "whiten" the observation into a white-noise innovation, then perform the optimal projection on the innovation, and finally keep only the physically realizable causal part. Without the causality constraint, the formula reduces to $$H=S_{sy}/S_{yy}$$, which shows that $$[\cdot]_+$$ is exactly the price of causality. This is the frequency-domain incarnation of the same idea as the orthogonal projection of [Wiener–Kolmogorov prediction](../wiener-kolmogorov-prediction/).

### Impact

The Wiener filter gave the optimal, realizable solution in the mean-square sense to the "signal + noise" problem, with its error spectrum included. It brought fire-control prediction, communication denoising and radar tracking into a single framework, and made "feedback–prediction–correction" an object that could be designed and analysed. *Cybernetics* went further, elevating feedback into a universal principle spanning machines and living organisms, with influence reaching as far as neuroscience and economics.

### Significance and outlook

Wiener filtering is a milestone of optimal estimation theory in the frequency domain, but it depends on **stationarity, known spectra and spectral factorization**, making it rather cumbersome for non-stationary systems and real-time recursion. In 1960, [Kalman](../kalman/) carried the same optimal-projection idea into the **time-domain state space**, obtaining the Kalman filter, which can be computed recursively step by step and adapts to non-stationarity — often regarded as the recursive generalization of the Wiener filter. From GPS and guidance to signal denoising, today's lineage of optimal filtering has its roots here, with Wiener in 1948.
