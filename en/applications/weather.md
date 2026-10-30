---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 6 · Weather & climate"
permalink: /en/applications/weather/
title: "Weather & Climate"
lead: "Weather forecasting is humanity's oldest and largest-scale time series engineering effort: it has to predict the future of an entire high-dimensional spatio-temporal field, while accepting the hard limit imposed by chaos."
math: false
prev: /applications/health/
next: /applications/industry/
---

> This is scenario 6 of the [time series applications](../) section.

## Data and tasks

- **Data**: three-dimensional gridded fields of temperature / pressure / humidity / wind, satellite and radar observations, reanalysis datasets.
- **Tasks**: numerical weather prediction, nowcasting, seasonal forecasting, climate projection, early warning of extreme events.

## What makes it special

- **High-dimensional spatio-temporal fields**: the object being forecast is not a single curve but the evolution of a whole global grid over time, with enormous dimensionality and constrained by the laws of physics.
- **The chaotic limit of predictability**: Lorenz showed long ago that the atmosphere is extremely sensitive to initial conditions, and deterministic forecasts beyond roughly two weeks essentially fail.
- **Data assimilation**: vast streams of real-time observations must be continually fused into the model state to keep error growth in check.

## Common methods

- The traditional workhorse is **numerical weather prediction (NWP)**: solving the partial differential equations of atmospheric motion on supercomputers, combined with the ensemble Kalman filter (EnKF) for data assimilation (see the history [prologue](../../history/foundations/)).
- The new data-driven wave: FourCastNet, GraphCast, the Fourier neural operator (FNO) and others use deep learning to learn field-to-field mappings directly, several orders of magnitude faster ([prologue](../../history/foundations/), [2026 frontier · spatio-temporal (KUN page)](../../kun/)).

## A representative case: GraphCast

In 2023 DeepMind's GraphCast used a graph neural network for global medium-range weather forecasting, outperforming traditional numerical models on most metrics while needing only minutes of inference (traditional models take hours on a supercomputer). It is a milestone of data-driven weather forecasting — yet it is still bound by the same chaotic limit: however fast it is, it cannot conjure up deterministic forecasts beyond two weeks.

---

**Key terms:** numerical weather prediction (NWP), data assimilation, EnKF, chaos / predictability limit, neural operator (FNO), GraphCast.
