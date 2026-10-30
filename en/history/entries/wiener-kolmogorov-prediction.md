---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1940s · Control / Communications"
permalink: /en/history/e/wiener-kolmogorov-prediction/
title: "Optimal Prediction as Orthogonal Projection (Wiener · Kolmogorov, 1940s)"
lead: "The best linear way to predict the future is to project it perpendicularly onto \"the space spanned by the past\" — a geometric statement that unified filtering, smoothing and forecasting."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 2 · Theoretical Foundations](../../02/).

### Background

The 1938 [Wold decomposition](../wold/) told us the structure of stationary processes, but gave no operational answer to "how best to predict the future from the past". In the 1940s, Andrey Kolmogorov (discrete time) and Norbert Wiener (continuous time, studying filtering for wartime anti-aircraft fire control) solved the problem of **optimal linear prediction** of stationary processes almost simultaneously and independently. It was the first seamless joining of the geometry of probability theory (Hilbert space) with the filtering needs of engineering.

### The problem

Given all (or part) of the past of a stationary process $$\{X_t\}$$, we want to predict $$X_{t+h}$$ (forecasting), or recover the true signal from noisy observations (filtering). **Among all "linear combinations of the past", which one minimizes the mean squared error?** Does this optimal predictor have a computable closed-form structure?

### Other approaches of the time (and their limits)

- **Least-squares curve extrapolation**: fit polynomials or sinusoids to history and extrapolate. It assumes a deterministic functional form and ignores the random correlation structure of the process; for stationary random series it is neither optimal nor robust.
- **Ad hoc point-by-point recursive formulas**: smoothers designed empirically in engineering (such as simple exponential smoothing). Effective but lacking any proof of optimality — they cannot say under what criterion they are best, or how large the error is.
- **Pure frequency-domain intuition**: pick frequency bands by looking only at the power spectrum. It captures part of the information but does not build in the key constraint of "causality (only the past may be used)" — and the causality constraint is precisely the core difficulty of the Wiener–Hopf method.

### Method

The central insight is geometric. Regard all zero-mean, finite-variance random variables as a **Hilbert space** with inner product $$\langle X,Y\rangle=\mathbb{E}[XY]$$. Let $$\mathcal{H}_t=\overline{\mathrm{span}}\{X_s:s\le t\}$$ be the closed subspace spanned by "the past up to $$t$$". Then the optimal linear predictor $$\hat X_{t+h}$$, which minimizes the mean squared error $$\mathbb{E}[(X_{t+h}-\hat X)^2]$$, is the **orthogonal projection** of $$X_{t+h}$$ onto $$\mathcal{H}_t$$:

$$ \hat X_{t+h}=P_{\mathcal{H}_t}X_{t+h},\qquad \mathbb{E}\big[(X_{t+h}-\hat X_{t+h})\,X_s\big]=0\ \ \forall\,s\le t $$

The second equation is the **orthogonality principle**: the prediction error is uncorrelated with all the past information used. For (jointly) Gaussian processes, orthogonality means independence, and the orthogonal projection equals the conditional expectation $$\mathbb{E}[X_{t+h}\mid \mathcal{H}_t]$$, so this linear optimum is also the global optimum. Using the MA(∞) representation of the [Wold decomposition](../wold/), the prediction can be written as a truncation over innovations; in the frequency domain, finding the **causal** optimal filter from a noisy spectrum comes down to the spectral factorization of the **Wiener–Hopf equation** (see [Wiener's cybernetics](../wiener-cybernetics/)).

### Impact

Prediction went from "a formula found by trial" to "a unique solution obtained by projection", complete with a computable error variance. The same framework unified three tasks: forecasting ($$h>0$$), filtering (denoising, $$h=0$$) and smoothing (using the future as well as the past). The innovation sequence $$\varepsilon_t=X_t-P_{\mathcal{H}_{t-1}}X_t$$ became the natural basis for recursive computation, and orthogonality meant that step-by-step updates need not recompute the whole history.

### Significance and outlook

"Optimal estimation = orthogonal projection = conditional expectation" became the backbone of all estimation theory. But Wiener–Kolmogorov theory requires the process to be stationary and often needs an infinite past and frequency-domain factorization, making engineering implementations cumbersome. Precisely to handle "non-stationarity, finite data and real-time recursion", in 1960 [Kalman](../kalman/) carried the very same projection idea into **state space**, obtaining the Kalman filter, which recurses step by step in time. From wartime fire control to today's GPS, SLAM and sequence forecasting, the skeleton is this one step: project the future perpendicularly onto the past.
