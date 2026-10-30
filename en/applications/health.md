---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 5 · Healthcare"
permalink: /en/applications/health/
title: "Healthcare & Physiology"
lead: "Heartbeats, brain waves, blood glucose, epidemic curves — every forecast on a medical time series can be a matter of life and death, so its demands for interpretability, calibration and \"lead time\" are stricter than anywhere else."
math: false
prev: /applications/transport/
next: /applications/weather/
---

> This is scenario 5 of the [time series applications](../) section.

## Data and tasks

- **Data**: ICU vital signs (heart rate / blood pressure / oxygen saturation), ECG / EEG, wearable devices, electronic health records (EHR), epidemic curves.
- **Tasks**: early warning (e.g. sepsis), arrhythmia detection and classification, blood glucose forecasting, epidemic spread forecasting.

## What makes it special

- **High stakes**: false alarms cause alarm fatigue, missed alarms can be fatal; forecasts must be **interpretable and calibrated**.
- **Irregularity and missing data**: tests are taken at irregular times and devices drop out, so sampling intervals are uneven and modalities are mixed.
- **Extreme imbalance**: truly critical events are rare, and positive and negative samples are wildly unbalanced.

## Common methods

- For detection / classification, sequence models such as LSTM / TCN (course [9](../../course/09/)) and Transformers ([10](../../course/10/)).
- Irregular time: attention with time-interval information, and continuous-time models of the Neural ODE family.
- Epidemics: **hybrids** of mechanistic models (SIR / SEIR) and data-driven models, balancing interpretability and fitting power.
- Output **probability intervals** rather than single points, to support clinical trade-offs ([14](../../course/14/)).

## A representative case: early warning of sepsis

Predicting the onset of sepsis hours in advance from continuous vital signs is a landmark task in clinical time series (for example the 2019 PhysioNet / CinC Challenge). It combines "classification + early warning" with "severe imbalance + strong interpretability requirements" — every hour gained directly affects survival rates.

---

**Key terms:** early warning, irregular sampling, class imbalance, ECG / EEG, SIR / SEIR, probability calibration.
