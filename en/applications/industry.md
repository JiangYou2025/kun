---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 7 · Industrial IoT"
permalink: /en/applications/industry/
title: "Industry & IoT"
lead: "Before a machine breaks, it usually leaves telltale traces in its sensors. The goal of industrial time series is to hear the footsteps of a failure in advance, amid piles of vibration, temperature and current signals."
math: false
prev: /applications/weather/
next: /applications/signal/
---

> This is scenario 7 of the [time series applications](../) section.

## Data and tasks

- **Data**: multi-sensor streams from equipment (vibration / temperature / current / pressure), SCADA logs, quality inspection data.
- **Tasks**: predictive maintenance and remaining useful life (RUL), anomaly / fault detection, statistical process monitoring (SPC), soft sensing.

## What makes it special

- **Multivariate and high-frequency**: dozens or hundreds of sensors are sampled simultaneously, along with sensor drift and noise.
- **Scarce fault labels**: equipment rarely breaks, positive samples are very few, and most tasks can only take the route of **unsupervised anomaly detection**.
- **Real time at the edge**: models often have to run on the device itself with low latency.

## Common methods

- **Statistical process control (SPC)** control charts as the simplest baseline.
- State space models / the Kalman filter for smoothing and online monitoring (history [4](../../history/04/)).
- Unsupervised anomaly detection: raise an alarm when an autoencoder's **reconstruction error** or a forecasting model's **residual** exceeds a threshold.
- RUL prediction regresses multi-sensor series onto remaining life, typically with LSTM / TCN (course [9](../../course/09/)).

## A representative case: remaining useful life (RUL)

NASA's C-MAPSS turbofan engine dataset is the standard benchmark for predictive maintenance: the input is multi-sensor degradation series, the output is "how many more cycles it can run". It brings the two big pain points of industrial settings together — modelling multivariate degradation, and still giving trustworthy predictions when fault samples are scarce.

---

**Key terms:** predictive maintenance, remaining useful life (RUL), anomaly detection, SPC control charts, soft sensing, sensor drift.
