---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1938 · Mathematics"
permalink: /en/history/e/wold/
title: "The Anatomy of Stationary Processes (Wold, 1938)"
lead: "Any stationary series can be cleanly split into \"a part fully determined by its history\" and \"a part driven by a stream of white noise\" — the step that turned ARMA from an empirical trick into a theorem."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 2 · Theoretical Foundations](../../02/).

### Background

After [Yule](../yule-ar/) used autoregression in 1927 to make sense of "quasi-periodicity", statisticians had AR in hand, and some were also fitting data with moving averages (MA). But all of this rested on **empirical intuition about model choice**: should one use AR or MA? How many lags? Was there a unified theory that could say clearly "what a stationary series actually looks like"? In his 1938 doctoral thesis, *A Study in the Analysis of Stationary Time Series*, the Swedish economist Herman Wold answered this fundamental question.

### The problem

Given a (weakly / covariance-) stationary process $$\{X_t\}$$ — constant mean, autocovariance depending only on the time lag — what can we assert about its internal structure? **Is there a universal decomposition that completely separates "the predictable component" from "the unpredictable random excitation"**, without relying on any specific parametric model assumption? If so, it could serve as the common foundation of all linear time series models.

### Other approaches of the time (and their limits)

- **The harmonic/periodogram school**: still viewed a stationary series as deterministic sine waves plus noise. It could describe deterministic components but could not capture the kind of random dynamics "continually driven by white noise", and was helpless before AR-style quasi-periodicity.
- **Purely empirical model fitting**: plug in AR(p) or MA(q) directly, tune the parameters, and pick whichever leaves smaller residuals. No theoretical guarantee — one did not know whether such model classes were "large enough" to approximate every stationary process.
- **Deterministic extrapolation**: assumes the series is fully determined by a few deterministic trends or cycles. This is precisely a special case of the "deterministic component" in the Wold decomposition, and it misses all the random dynamics represented by the infinite-order moving average.

### Method

Wold proved that any zero-mean covariance-stationary process can be uniquely decomposed into two uncorrelated parts — a **deterministic component** $$V_t$$ (linearly and perfectly predictable from its infinitely distant past) and a **purely nondeterministic component** (an infinite-order moving average):

$$ X_t = \sum_{j=0}^{\infty}\psi_j\,\varepsilon_{t-j} + V_t,\qquad \psi_0=1,\ \sum_{j=0}^{\infty}\psi_j^2<\infty $$

where $$\varepsilon_t \sim \mathrm{WN}(0,\sigma^2)$$ is the **innovation**: $$\varepsilon_t$$ equals $$X_t$$ minus its optimal prediction obtained by linear projection on the past $$\{X_s:s<t\}$$, that is, the one-step prediction error. The coefficients $$\psi_j$$ are the impulse response of the linear filter that "filters" this stream of white noise into $$X_t$$, and square-summability guarantees convergence and stationarity. The deterministic component $$V_t$$ is orthogonal to all $$\varepsilon_s$$. Intuitively: **a stationary process = a perfectly predictable shell + dynamics excited by white noise through a linear filter, which can never be predicted exactly**.

### Impact

This result raised ARMA from a technique to a theorem. The MA(∞) form shows that, as long as the spectral density of the random part is rational, the infinite sum can be approximated by a ratio of finite-order AR and MA — which is exactly the justification for the existence of ARMA($$p,q$$). So "AR or MA?" was no longer a mystery: both are **finite-parameter approximations** of the same Wold representation and can be converted into each other (AR(∞) ↔ MA(∞)). The innovation $$\varepsilon_t$$ also became the standard object of "optimal one-step prediction error" in later Kalman filtering and prediction theory.

### Significance and outlook

The Wold decomposition is the constitution of modern linear time series. It established a worldview: studying a stationary process essentially means studying "the linear filter that turns white noise into the observed series". This line leads directly to [Wiener–Kolmogorov prediction theory](../wiener-kolmogorov-prediction/) (optimal prediction is orthogonal projection onto the space spanned by the past), to the 1970 [Box–Jenkins ARMA/ARIMA](../box-jenkins/) modelling framework, and to spectral factorization in the frequency domain. Today, when we say "any stationary signal can be seen as white noise shaped by a filter", we are quoting this step Wold took in 1938.
