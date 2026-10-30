---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2010 · Control / Communications"
permalink: /en/history/e/particle-mcmc/
title: "Particle MCMC (Andrieu et al., 2010)"
lead: "In a nonlinear state-space model, how can the parameters and the hidden states be estimated together? Plug the likelihood estimate produced by a particle filter into MCMC — even though it is only an estimate, the chain still converges to the correct distribution."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

The state-space model is the universal skeleton of time series: a hidden state $$ x_t $$ evolves according to some dynamics, and the observation $$ y_t $$ is a noisy reflection of it. In the linear-Gaussian case the [Kalman filter](../kalman/) gives a closed-form solution; in the nonlinear or non-Gaussian case there is the **particle filter (sequential Monte Carlo)**, developed in the 1990s, which approximates the filtering distribution and, as a by-product, yields an **unbiased estimate of the marginal likelihood**. But the particle filter assumes the parameters are known. The real difficulty is this: **when the parameters are unknown, how can Bayesian inference be carried out on the parameters and the hidden states simultaneously?** In 2010 Andrieu, Doucet and Holenstein gave an elegant answer in JRSS-B — **particle MCMC (PMCMC)**.

### The problem

Bayesian inference on a parameter $$ \theta $$ requires the marginal likelihood $$ p(y_{1:T}\mid\theta) $$, which means integrating over all hidden state trajectories; for nonlinear models this integral has **no analytical solution**. Running Gibbs sampling or MCMC directly on the joint $$ (\theta, x_{1:T}) $$, on the other hand, mixes extremely poorly because the states are so strongly correlated. Is it possible to build an MCMC whose target stationary distribution over $$ \theta $$ is exactly the true posterior $$ p(\theta\mid y_{1:T}) $$, while the particle filter takes care of integrating out the states?

### Other approaches of the time (and their limits)

- **Extended / unscented Kalman filters (EKF/UKF)**: fast, but they rely on linearization or moment matching, are badly biased under strong nonlinearity or multimodality, and do not provide the full posterior.
- **Gibbs sampling of the state trajectory directly**: workable in principle, but the strong correlation between neighbouring states makes **mixing extremely slow**; on long series the chain barely moves.
- **The plain particle filter**: handles nonlinear states, but **does not estimate parameters**; even with fixed parameters it suffers from path degeneracy.

### Method

The heart of PMCMC is the **pseudo-marginal principle**: if, in the Metropolis–Hastings acceptance ratio, the true but unavailable likelihood is replaced by an **unbiased estimate of the likelihood** $$ \hat{p}(y_{1:T}\mid\theta) $$, the stationary distribution of the resulting Markov chain is **still exactly** the target posterior. The particle filter provides precisely such an unbiased estimate:

$$ \hat{p}(y_{1:T}\mid\theta) = \prod_{t=1}^{T}\Big(\frac{1}{N}\sum_{i=1}^{N} w_t^{(i)}\Big),\qquad \mathbb{E}\big[\hat{p}\big] = p(y_{1:T}\mid\theta) $$

where $$ N $$ is the number of particles and $$ w_t^{(i)} $$ are the importance weights. **Particle marginal Metropolis–Hastings (PMMH)** proposes a new parameter from $$ q(\theta'\mid\theta) $$ at each step, runs a particle filter to obtain $$ \hat{p}(y_{1:T}\mid\theta') $$, and accepts it with probability

$$ \alpha = \min\!\left\{1,\ \frac{\hat{p}(y_{1:T}\mid\theta')\,p(\theta')\,q(\theta\mid\theta')}{\hat{p}(y_{1:T}\mid\theta)\,p(\theta)\,q(\theta'\mid\theta)}\right\} $$

Unbiasedness guarantees that even though $$ \hat p $$ contains random noise, the chain still converges to the exact joint posterior $$ p(\theta, x_{1:T}\mid y_{1:T}) $$. Another variant, **particle Gibbs**, uses a "conditional particle filter" that resamples the states while keeping one reference trajectory fixed, which improves mixing.

### Impact

PMCMC made full Bayesian inference feasible for a large class of previously intractable **nonlinear, non-Gaussian state-space models**: stochastic volatility, ecological population dynamics, epidemic spread, biochemical reaction networks and more. It turned "the likelihood can only be estimated, never computed exactly" from an obstacle into an acceptable cost, and it requires only **forward simulation** of the model, without ever writing down the likelihood — a perfect fit for complex mechanistic models. The price is computational expense (each MCMC step embeds a full run of the particle filter), and if $$ N $$ is too small the variance of the likelihood estimate becomes too large and the chain gets stuck.

### Significance and outlook

The intellectual legacy of PMCMC is **pseudo-marginal MCMC**: as long as an unbiased likelihood estimate is available, it can be traded for exact Bayesian inference — which **rigorously stitches together** the two pillars of Monte Carlo and MCMC. Together with later work on variational inference, probabilistic programming and differentiable particle filters, it forms the foundation of modern Bayesian inference for nonlinear time series. Today's probabilistic programming frameworks still treat particle MCMC as a general-purpose tool for arbitrary state-space models, carrying on the powerful paradigm of "simulation as inference".
