---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 8 · Communications & signals"
permalink: /en/applications/signal/
title: "Communications & Signal Processing"
lead: "Signal processing is the engineering home of time series: long before machine learning became popular, engineers were using filters and linear prediction to track signals, compress data and decode codewords through noise, in real time."
math: false
prev: /applications/industry/
next: /applications/geophysics/
---

> This is scenario 8 of the [time series applications](../) section.

## Data and tasks

- **Data**: speech / audio, wireless channel responses, radar / sonar echoes, bioelectric signals.
- **Tasks**: speech coding and recognition, channel equalisation and prediction, echo and noise cancellation, radar target tracking, modulation recognition.

## What makes it special

- **High sampling rates, hard real time**: tens of thousands to millions of samples per second, so processing must be online and low-latency.
- **Deep physical / linear foundations**: decades of accumulated filter theory are very mature and reliable.
- **Noise and multipath**: signals are often heavily corrupted by noise and reflections.

## Common methods

- Classical adaptive filtering: Wiener filtering, LMS, RLS; **linear predictive coding (LPC)** for speech.
- The **Kalman filter** for target tracking and state estimation (history [4](../../history/04/), [prologue](../../history/foundations/)).
- The **Viterbi algorithm** for optimal decoding of HMMs / convolutional codes ([prologue](../../history/foundations/)).
- In recent years, end-to-end deep learning for speech and signals (course [9](../../course/09/), [10](../../course/10/)).

## A representative case: linear predictive coding (LPC)

Model a short segment of speech as an **AR process** — predict the current sample linearly from the previous few, and transmit only the residual and the coefficients. This is the classic engineering application of the AR model (course [8](../../course/08/)), and it underpinned decades of speech compression, synthesis and mobile communication. Under another name, it is what statisticians call autoregression.

---

**Key terms:** adaptive filtering, LPC, Kalman tracking, Viterbi, channel equalisation, AR process.
