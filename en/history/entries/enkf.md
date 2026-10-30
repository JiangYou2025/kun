---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1994 · Control / Communications"
permalink: /en/history/e/enkf/
title: "The Ensemble Kalman Filter (Evensen, 1994)"
lead: "A weather forecast's state has hundreds of millions of dimensions; Kalman's covariance matrix can be neither stored nor computed. Evensen's answer: don't store the matrix — store a crowd of samples."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

Numerical weather prediction is, at heart, a gigantic state estimation problem: push the atmospheric state forward with a physical model, then keep correcting it with observations (radiosondes, satellites, ground stations). This is exactly the stage for the [Kalman filter](../kalman/) — but there is a fatal obstacle. The Kalman filter must explicitly store and propagate the **error covariance matrix** $$\mathbf{P}$$. The dimension $$n$$ of the atmospheric state easily exceeds $$10^7$$; an $$n\times n$$ matrix cannot even be stored, and updating it through the model's evolution would take an astronomical amount of computation.

### The problem

The bottleneck of the classical Kalman filter is the **storage and propagation** of the covariance matrix: once the dimension is high, $$\mathbf{P}$$ cannot be maintained explicitly, and schemes like the extended Kalman filter, which propagate the covariance through linearization, are both expensive and unstable in high-dimensional, strongly nonlinear settings. **How can one approximately represent and evolve the state's uncertainty in systems with millions or even hundreds of millions of dimensions, and carry out data assimilation?**

### Other currents of the time (and their limits)

- **Extended Kalman filter (EKF)**: propagates the covariance explicitly and linearizes the model. In high-dimensional systems the cost of propagating the covariance is prohibitive, and the strong nonlinearity of atmospheric models makes the linearization error severe.
- **Variational assimilation (3D/4D-Var)**: writes assimilation as an optimization problem and avoids the explicit covariance, with great engineering success; but it requires deriving and maintaining an **adjoint model**, which is costly to develop, and it assumes a static background error covariance that cannot easily change with the flow of the weather.
- **Optimal interpolation (OI)**: uses a preset, fixed background covariance; simple, but unable to reflect the dependence structure created by "today's circulation pattern".

### The method

The core idea of the EnKF: instead of storing the covariance matrix, represent it implicitly by a set of $$N$$ state samples (an **ensemble**). The ensemble mean is the state estimate, and the spread of the ensemble encodes the error covariance:

$$ \mathbf{P}^f\;\approx\;\frac{1}{N-1}\sum_{i=1}^{N}\big(\mathbf{x}_i^f-\bar{\mathbf{x}}^f\big)\big(\mathbf{x}_i^f-\bar{\mathbf{x}}^f\big)^{\!\top} $$

Each member is integrated forward on its own with the full nonlinear model (the forecast step), with no linearization or adjoint needed at all. When an observation $$\mathbf{y}$$ arrives, a Kalman-style update is applied to each member (the analysis step):

$$ \mathbf{x}_i^a=\mathbf{x}_i^f+\mathbf{K}\big(\mathbf{y}_i-\mathbf{H}\mathbf{x}_i^f\big),\qquad \mathbf{K}=\mathbf{P}^f\mathbf{H}^{\top}\big(\mathbf{H}\mathbf{P}^f\mathbf{H}^{\top}+\mathbf{R}\big)^{-1} $$

where the gain $$\mathbf{K}$$ is computed entirely from ensemble statistics, without ever forming the full $$\mathbf{P}$$. Giving each member a perturbed observation $$\mathbf{y}_i=\mathbf{y}+\boldsymbol{\varepsilon}_i$$ ensures that the variance of the updated ensemble is statistically correct. The whole procedure only requires running the model itself, and its cost grows linearly with the ensemble size $$N$$ (typically a few dozen to a few hundred) rather than exploding with the dimension $$n$$.

### Results

The EnKF made it possible, for the first time, to apply Kalman's ideas to ultra-high-dimensional systems such as the ocean and the atmosphere: the covariance adapts to the "flow" of the circulation, no adjoint model is needed, and implementation is relatively simple. It was soon adopted by meteorological and oceanographic centres around the world, becoming one of the workhorses of operational data assimilation, and it spawned many variants such as the ETKF and LETKF (combined with **localization** and **inflation** techniques to suppress the spurious correlations caused by finite ensembles).

### Significance and outlook

The EnKF brought the Monte Carlo idea of "approximating uncertainty with a sample ensemble" into high-dimensional filtering. Together with the [particle filter](../particle-filter/), it belongs to the 1990s wave of ensemble / sampling-based filters, but it is better suited to ultra-high-dimensional, near-Gaussian geophysical systems. It remains a cornerstone of numerical weather prediction, ocean and groundwater modelling, and the production of reanalysis datasets, and it stands as a representative of the modern forecasting philosophy of continuously fusing "model + observations".
