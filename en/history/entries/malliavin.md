---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1976 · Mathematics"
permalink: /en/history/e/malliavin/
title: "Differentiating Randomness (Malliavin, 1976)"
lead: "Can one differentiate with respect to a Brownian path itself? Malliavin brought the calculus of variations into infinite-dimensional random spaces, making it possible to decide whether solutions of stochastic equations have smooth densities, and giving an elegant algorithm for hedging sensitivities."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

[Itô calculus](../ito/) solved "how to integrate with respect to a stochastic process", making the stochastic differential equation (SDE) $$dX_t=b(X_t)dt+\sigma(X_t)dW_t$$ the standard language for modelling continuous-time random phenomena; [Black–Scholes](../black-scholes/) is built on it. But a complementary question remained open: can one differentiate a random quantity with respect to **the random source that drives it (the Brownian path itself)**? That requires a differential calculus on the infinite-dimensional space of paths.

### The problem

Two concrete needs drove it. The first was purely theoretical: when does the solution $$X_t$$ of an SDE have a **smooth probability density**? This bears on the regularity of solutions of partial differential equations (Malliavin originally created the theory to give a probabilistic proof of Hörmander's hypoellipticity theorem). The second was applied: in finance, how can the **sensitivities (Greeks)** of an option price with respect to its parameters be computed efficiently and stably, especially when the payoff function is not smooth and finite differences are very noisy? **What was needed was a calculus able to "differentiate randomness".**

### Other approaches of the time (and their limits)

- **Itô calculus**: excellent for stochastic integrals, but it does not itself provide "directional derivatives" with respect to the Brownian path, so it cannot directly answer whether a density exists.
- **Finite differences for the Greeks**: simple to implement, but numerically very unstable for discontinuous payoffs, with high variance and slow convergence.
- **PDE methods for sensitivities**: effective in low dimensions, but they break down quickly as dimension grows (the curse of dimensionality).

### Method

Malliavin defined a **derivative operator** $$D$$ on Wiener space: for a functional $$F$$ (for example $$F=\int_0^T h_s\,dW_s$$), $$D_t F$$ measures the sensitivity of $$F$$ to the Brownian increment at time $$t$$. Its adjoint operator $$\delta$$ (the Skorokhod integral) satisfies an integration-by-parts formula:

$$ \mathbb{E}\!\left[\,F\,\delta(u)\,\right]=\mathbb{E}\!\left[\,\langle DF,\,u\rangle_{L^2[0,T]}\,\right] $$

This **stochastic integration by parts** is the source of all its power. On the one hand, define the Malliavin covariance matrix $$\gamma_X=\langle DX,DX\rangle$$; if it is invertible and regular enough, one can prove that $$X$$ has a smooth density. That is the density criterion. On the other hand, it can turn "differentiating a non-smooth payoff" into "taking the expectation against a smooth weight":

$$ \frac{\partial}{\partial\theta}\,\mathbb{E}[\Phi(X_T)]=\mathbb{E}\!\left[\Phi(X_T)\,\pi\right] $$

where the weight $$\pi$$ is given explicitly by $$\delta$$. **The derivative lands on the weight rather than on the payoff**, so even when $$\Phi$$ has jumps, the Greeks can be estimated stably by Monte Carlo.

### Impact

On the theoretical side, Malliavin calculus gave a neat criterion for the existence and smoothness of densities of SDE solutions, and provided a probabilistic proof for Hörmander-type hypoelliptic equations. On the applied side, it brought the "Malliavin weights" method for computing sensitivities such as Delta, Gamma and Vega, which is especially effective for discontinuous or path-dependent derivatives and markedly reduces Monte Carlo variance.

### Significance and outlook

It extended the calculus of variations to infinite-dimensional stochastic analysis and became one of the pillars of modern stochastic analysis; it also serves quantitative finance deeply, in refined hedging and risk computations within the [Black–Scholes](../black-scholes/) framework. This toolkit for "differentiating randomness" echoes recent frontiers such as [rough volatility](../rough-volatility/), modelled with fractional Brownian motion: as volatility paths become rougher and payoffs more irregular, the ability to differentiate and integrate by parts on path space is precisely what is needed to analyse these models.
