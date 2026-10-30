---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1930 · Physics"
permalink: /en/history/e/ornstein-uhlenbeck/
title: "The Random Process That Comes Home (Ornstein · Uhlenbeck, 1930)"
lead: "Brownian motion wanders ever further and its variance grows without bound, yet in reality velocities, interest rates and temperatures are always pulled back toward equilibrium. The OU process supplied the missing “restoring spring” — and once discretized, it turns out to be nothing other than AR(1)."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Pure [Brownian motion / the Wiener process](../brownian-motion/) has something "unphysical" about it: its variance grows without limit, $$\propto t$$, and if it is used to describe a velocity, that velocity drifts without bound over time. But the **velocity** of a real Brownian particle obviously does not keep growing — viscous drag pulls it back. In 1930, building on the [Langevin equation](../langevin/), Leonard Ornstein and George Uhlenbeck gave a rigorous statistical description of a random process with mean reversion, designed precisely to capture this kind of fluctuation that is "pulled back toward equilibrium".

### The problem

The [Langevin equation](../langevin/) tells us that the velocity is held in check by the friction term $$-\gamma v$$. **So what distribution does a quantity settle into in the long run when friction keeps pulling it back and a random force keeps pushing it away? And how does its autocorrelation decay with the time lag?** In other words, what exactly is the statistical difference between "a random process with a restoring force" and "a random walk without one"?

### Other approaches of the time (and their limits)

- **Modelling every fluctuation directly with Brownian motion $$W_t$$**: simple, but the variance diverges and there is no stationary distribution, so it cannot describe quantities that fluctuate around an equilibrium (velocities, interest rates, inventories).
- **Deterministic reversion plus noise added afterwards**: first solve $$\dot x=-\gamma x$$ so that it decays to 0, then superimpose a little observation noise after the fact. This separates "reversion" from "randomness" and fails to produce the correct autocorrelation structure and stationary variance.
- The right approach is to let the restoring force and the noise **act continuously within the same equation**, so that their dynamic balance yields a stationary distribution.

### Method

The OU process is defined by the following stochastic differential equation (the drift points toward the mean, the diffusion supplies the fluctuations):

$$ dX_t=-\theta\,(X_t-\mu)\,dt+\sigma\,dW_t $$

where $$\theta>0$$ is the rate of reversion, $$\mu$$ the long-run mean, $$\sigma$$ the noise intensity, and $$W_t$$ a Wiener process. Its autocovariance **decays exponentially** with the lag, and it has a stationary variance:

$$ \mathrm{Cov}(X_t,X_{t+s})=\frac{\sigma^2}{2\theta}\,e^{-\theta |s|},\qquad \mathrm{Var}_\infty=\frac{\sigma^2}{2\theta} $$

The crucial point is its **discretization**: sampling with step $$\Delta$$ and setting $$\phi=e^{-\theta\Delta}$$, we get

$$ X_{t+\Delta}=\mu(1-\phi)+\phi\,X_t+\varepsilon_t,\qquad \varepsilon_t\sim \mathcal N\!\Big(0,\tfrac{\sigma^2}{2\theta}(1-\phi^2)\Big) $$

This is exactly **AR(1)**. The physicist's "friction + thermal noise" and the statistician's "autoregressive coefficient $$\phi$$ + innovation" are two languages for the same thing.

### Impact

The OU process was the **first** continuous-time process to be at once stationary, Gaussian and Markov (Doob later proved that these three properties together essentially force a process to be OU). It delivered a whole clean set of statistical properties — mean reversion, exponentially decaying autocorrelation, finite stationary variance — and became the standard model of an analytically tractable random process.

### Significance and outlook

The bridge "discretized OU = AR(1)" welds physical random processes directly to [Yule's autoregressive](../yule-ar/) time series, and it is the best illustration of the "shared interdisciplinary roots" running through this timeline. In finance, the OU process underlies the Vasicek interest-rate model and the "mean-reverting spread" of pairs trading; in engineering, it is the standard model of coloured noise. Its exponential autocorrelation structure is also the origin of a kernel commonly used in Gaussian process regression (Matérn-1/2). Today, whenever anyone speaks of "mean reversion", "persistence $$\phi$$" or "damping", they are almost always speaking the language of OU.
