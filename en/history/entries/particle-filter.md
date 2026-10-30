---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1993 · Control / Communications"
permalink: /en/history/e/particle-filter/
title: "The Particle Filter (Gordon et al., 1993)"
lead: "When a system is both nonlinear and non-Gaussian, the Kalman filter's formulas break down. So stop looking for a closed-form solution — scatter a swarm of weighted “particles” to approximate the posterior."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

The [Kalman filter (1960)](../kalman/) was a milestone in state estimation, but its elegance rests on two strong assumptions: a linear system and Gaussian noise. Under them the posterior distribution stays Gaussian at all times and can be propagated exactly with just two quantities, the mean and the covariance. Yet real radar tracking, manoeuvring targets and financial volatility are often **both nonlinear and non-Gaussian**, and the posterior may take on complicated multimodal, skewed shapes. The extended Kalman filter (EKF) copes, barely, through local linearization, but it diverges in the face of strong nonlinearity or multimodality.

### The problem

The ideal of Bayesian filtering is to maintain the full posterior distribution $$p(\mathbf{x}_t\mid \mathbf{y}_{1:t})$$ recursively, but the integrals involved have no closed-form solution for general nonlinear, non-Gaussian models. **How can an arbitrary posterior be represented and updated approximately and recursively, without assuming its shape?** The answer requires a numerical representation that can express any distribution and also be updated online as observations arrive.

### Other approaches of the time (and their limits)

- **The extended Kalman filter (EKF)**: takes a first-order Taylor expansion of the nonlinearity around the current estimate. Cheap to compute, but the linearization error is large under strong nonlinearity, and it can fundamentally describe only a unimodal Gaussian posterior, so it is bound to fail when the posterior is multimodal.
- **Grid / point-mass filters**: lay a fixed grid over the state space and integrate numerically. Feasible in low dimensions, but the number of grid points explodes exponentially as the dimension grows (the curse of dimensionality).
- **Gaussian-sum filters**: approximate the posterior with a mixture of Gaussians. More flexible than the EKF, but managing the number of components and their parameters is complicated, and it is still limited by its Gaussian building blocks.

### Method

The particle filter (**sequential Monte Carlo / the bootstrap filter**) approximates the posterior with a set of weighted samples, or particles:

$$ p(\mathbf{x}_t\mid \mathbf{y}_{1:t})\;\approx\;\sum_{i=1}^{N} w_t^{(i)}\,\delta\big(\mathbf{x}_t-\mathbf{x}_t^{(i)}\big) $$

Each step has two stages. **Prediction**: each particle is propagated forward by sampling from the state-transition model, $$\mathbf{x}_t^{(i)}\sim p(\mathbf{x}_t\mid \mathbf{x}_{t-1}^{(i)})$$. **Update**: the particles are reweighted using the new observation — the better a particle agrees with the observation, the larger its weight:

$$ w_t^{(i)}\;\propto\;w_{t-1}^{(i)}\;p\big(\mathbf{y}_t\mid \mathbf{x}_t^{(i)}\big) $$

This is **importance sampling**. But over time "weight degeneracy" sets in: a handful of particles take nearly all the weight while the rest become dead weight. The key move of Gordon and his colleagues was **resampling**: particles are copied with replacement according to their weights, so that low-weight samples die out and high-weight samples multiply, restoring an equally weighted set. The cycle of "importance sampling + resampling" makes the particle swarm gather automatically in regions of high posterior probability.

### Impact

On nonlinear, non-Gaussian target tracking, the bootstrap filter clearly outperformed the EKF and handled multimodal posteriors and violent manoeuvres robustly. Because all it requires is the ability to "sample from the transition model and evaluate the likelihood of an observation", it places almost no constraints on the form of the model, and it was quickly adopted in radar, navigation, robot localization (SLAM), econometrics and other fields.

### Significance and outlook

The particle filter brought the flexibility of Monte Carlo into online state estimation. Together with the [Kalman filter](../kalman/) and the [ensemble Kalman filter](../enkf/), it forms the lineage of modern Bayesian filtering: from "closed-form linear-Gaussian solutions" to "high-dimensional ensemble approximations" to "sample approximations of arbitrary distributions". Its sample–weight–resample paradigm remains to this day the core engine of sequential Bayesian inference, probabilistic programming and even differentiable filters.
