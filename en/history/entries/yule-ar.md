---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1927 · Mathematics"
permalink: /en/history/e/yule-ar/
title: "The Birth of Autoregression (Yule, 1927)"
lead: "Why do cycles \"drift out of shape\"? With a linear system continually excited by random shocks, Yule explained the wandering period of sunspots — and laid down the worldview of modern time series."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 1 · Autoregression](../../01/).

### Background

In the 1920s, one of the most fascinating datasets in statisticians' hands was the **sunspot number**: an annual series stretching back to the 18th century that visibly "rises and falls roughly every 11 years". Astronomy, agriculture and business forecasting all hoped to read laws from such cycles. The prevailing analytical paradigm was the **periodogram** and **harmonic analysis** — viewing the series as a superposition of several hidden sine waves plus a little observation noise. This line of thinking was inherited directly from the triumphs of celestial mechanics: planetary motion is deterministically periodic, so once you find the frequencies and amplitudes, you can compute the future exactly.

### The problem

But sunspots refused to cooperate. Fit them with fixed-frequency sine waves and clear structure still remains in the residuals; more awkwardly, the "11-year cycle" **drifts** — sometimes 9 years, sometimes 13, with amplitudes that swing up and down. If there really were a deterministic pendulum behind it, the period should not wander like this. **Why does a seemingly regular cycle keep drifting out of shape?** Deterministic harmonic models had no answer.

### Other approaches of the time (and their limits)

- **The deterministic-cycle view (periodogram school)**: firmly believed that a series = a sum of hidden sine waves, and attributed every irregularity to "measurement error". Its implicit assumption is pure, pendulum-like oscillation, which cannot explain random drift in the period itself.
- **Slutsky's opposite extreme (the same year, 1927)**: [Slutsky](../slutsky/) showed that taking moving sums of pure random noise can also make cycle-like fluctuations "emerge". A profound warning, but pushed to the extreme it makes one suspect that every cycle is an illusion — also not a complete answer.
- The truth lies in between: neither purely deterministic nor pure noise, but **a system with an internal restoring structure, driven by noise**.

### Method

Yule offered a third perspective: the current value is a linear regression on several past values, plus an unpredictable random shock. This is the **AR(p)** model:

$$ X_t = c + \sum_{i=1}^{p}\phi_i X_{t-i} + \varepsilon_t,\qquad \varepsilon_t \sim \mathrm{WN}(0,\sigma^2) $$

Each $$\phi_i$$ measures the influence of lag $$i$$, and $$\varepsilon_t$$ is the "innovation" — the random disturbance the system receives that cannot be predicted from history. The key lies in the characteristic equation of AR(2)

$$ 1-\phi_1 z-\phi_2 z^2 = 0 $$

When its roots are **complex**, the system exhibits **damped oscillation**: each random shock sets off an oscillation that decays, and new shocks keep "reigniting" it — so the cycle exists, yet is never exact. This is precisely the mathematical origin of "quasi-periodicity". The accompanying **Yule–Walker equations** link the autocorrelations $$\rho_k$$ to the parameters, so that AR coefficients can be estimated from data:

$$ \rho_k = \sum_{i=1}^{p}\phi_i\, \rho_{k-i},\qquad k\ge 1 $$

### Impact

The AR(2) fit to the sunspot series was **far better** than deterministic harmonic models: the residuals were closer to white noise, and the drift of the period was reproduced naturally. A random model with only two or three parameters achieved what a pile of sine waves could not — and it could also **extrapolate forecasts**, giving a future complete with uncertainty.

### Significance and outlook

Yule replaced "deterministic cycles" with "stochastic processes" and laid down the worldview of modern time series: the central task with a series shifted from "finding hidden frequencies" to "**identifying the random structure of the excited system**". Autoregression, innovations, characteristic roots and stationarity, Yule–Walker estimation — this language leads directly to the 1938 [Wold decomposition](../wold/), the 1970 [Box–Jenkins ARMA/ARIMA](../box-jenkins/) framework, and even the basic paradigm of "autoregressive generation" in today's deep models. A hundred years later, when we have a neural network "predict the next value from the past", at heart it is still Yule's step.
