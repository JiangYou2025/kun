---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2022–23 · Physics"
permalink: /en/history/e/neural-weather/
title: "Neural Weather Forecasting: FourCastNet and GraphCast (2022–23)"
lead: "For decades, weather forecasting relied on supercomputers grinding through the equations of the atmosphere. Train a spatiotemporal forecasting network on reanalysis data instead, and it can be tens of thousands of times faster, and more accurate too."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

The workhorse of modern weather forecasting is **numerical weather prediction (NWP)**: integrating the fluid-dynamical and thermodynamic equations of the atmosphere forward in time on a grid, with each run consuming considerable computing power on a large supercomputer. Meanwhile, decades of observations have been assimilated into high-quality **reanalysis datasets** (such as ERA5), which provide long-term, dense and regular global atmospheric states: exactly the kind of training material data-driven models dream of.

### The problem

NWP is accurate but **expensive and slow**: generating large ensemble forecasts and updating frequently are both constrained by computing power. A sharp question follows: **can deep learning learn the mapping "current state to future state" directly from reanalysis data**, maintaining or even exceeding NWP accuracy while cutting the cost of a single forecast from supercomputer hours to seconds on an ordinary GPU?

### Other approaches of the time (and their limits)

- **Traditional numerical models (NWP)**: physically rigorous and interpretable, but extremely expensive to compute, which limits ensembles and high resolution.
- **Early machine-learning corrections**: only post-process NWP output to correct biases, without replacing the core forecast, so the gains are limited.
- **Small-scale purely data-driven models**: lack globally consistent physical structure and long-term stability, and their errors blow up after several autoregressive rollout steps.

### Method

These models treat forecasting as **autoregressive spatiotemporal prediction**: learn an operator $$G_\theta$$ that advances the global atmospheric state field $$X_t$$ at a given time (a high-dimensional tensor stacking variables such as wind, temperature and humidity over multiple pressure levels) by one time step, then feed the output back into itself to roll out a long-range forecast:

$$ \widehat{X}_{t+\Delta t}=G_\theta(X_t),\qquad \widehat{X}_{t+k\Delta t}=G_\theta^{\,k}(X_t) $$

**FourCastNet** uses an adaptive Fourier neural operator (inheriting the frequency-domain global convolution of [FNO](../fno/)) to model high-resolution spherical fields; **GraphCast** instead discretizes the Earth into a multi-scale graph, passes information between nodes with a graph neural network, and is trained with a multi-step rollout loss to suppress error accumulation:

$$ \mathcal{L}=\sum_{k=1}^{K} w_k\,\big\|\,G_\theta^{\,k}(X_t)-X_{t+k\Delta t}\,\big\|^2 $$

Both are trained end to end on ERA5; what they learn are the laws of atmospheric evolution contained in the data, rather than explicit solutions of the equations.

### Impact

On a large number of key meteorological variables and lead times of several days, GraphCast's forecasts **outperformed the operational numerical models of the time**, while a single 10-day forecast takes only about a minute on one machine, several orders of magnitude faster than traditional models. FourCastNet likewise produces high-resolution global forecasts at very low cost, making large ensemble forecasts cheap and feasible.

### Significance and outlook

Neural weather models show that **data-driven spatiotemporal prediction can match or even surpass first-principles solvers on hard-core physical problems such as the Earth system**, while being much faster and much cheaper. They have pushed time series forecasting to the planetary scale; together with [FNO](../fno/) and [PINN/DeepONet](../pinn-deeponet/), they sketch the outline of "AI for Science", and they are moving toward the prediction of broader spatiotemporal dynamics such as climate, oceans and earthquakes, and even toward foundation models for the Earth system ([../foundation-models/](../foundation-models/)).
