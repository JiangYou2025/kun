---
lang: en
ref: time-series
permalink: /en/time-series/
title: "What is a time series?"
lead: "Before you can forecast, you need to understand what you are looking at. This page covers the core vocabulary and the structure hiding inside almost every time series."
next: forecasting
math: true
---

## The one-sentence definition

A **time series** is a sequence of observations recorded in time order, usually at regular intervals:

$$ x_1, x_2, x_3, \dots, x_T $$

Each $x_t$ is the value measured at time step $t$. What makes a time series special — and harder than ordinary tabular data — is that **the order matters**. Yesterday influences today; you cannot shuffle the rows.

Examples are everywhere: daily temperature, hourly electricity demand, a stock's closing price, the number of patients arriving at a hospital, the CPU usage of a server.

## Univariate vs. multivariate

- **Univariate** — a single variable over time (one sensor, one product's sales).
- **Multivariate** — many variables recorded together, often correlated (temperature *and* humidity *and* electricity load). KUN is designed for the multivariate case.

## The four components

Most series can be decomposed into a few recurring pieces. Understanding them tells you what a model has to capture.

| Component | What it is | Example |
|---|---|---|
| **Trend** | Long-term direction (up/down) | A city's population growing each year |
| **Seasonality** | A pattern that repeats on a fixed period | Higher ice-cream sales every summer |
| **Cyclic** | Repeats, but with no fixed period | Economic boom–bust cycles |
| **Noise / residual** | The irregular, unpredictable part | A random measurement error |

A classic way to write this is the **additive decomposition**:

$$ x_t = \text{Trend}_t + \text{Seasonality}_t + \text{Residual}_t $$

> **Intuition:** forecasting is the art of modelling trend and seasonality well, and *not* trying to predict the noise.

## Stationarity — the property models love

A series is **stationary** if its statistical properties (mean, variance, autocorrelation) do not change over time. Many classical methods assume stationarity, because a process whose rules keep shifting is nearly impossible to extrapolate.

Real data is usually **non-stationary** (it has trends and changing variance). Two common fixes:

- **Differencing** — model the change $x_t - x_{t-1}$ instead of the raw value, which removes a trend.
- **Transformations** — e.g. taking the logarithm to stabilise a growing variance.

Modern deep-learning models like KUN are more tolerant of non-stationarity, but normalising your data still helps a lot.

## Autocorrelation — the past predicts the future

The reason forecasting is possible at all is **autocorrelation**: a value is correlated with its own past values. The **lag-$k$ autocorrelation** measures how similar the series is to a copy of itself shifted by $k$ steps. Strong autocorrelation at lag 24 in hourly data, for example, screams "daily seasonality".

## How we frame the problem for a model

Given a **lookback window** (also called *context* or *input length*) of the last $L$ observations, we want to predict the next $H$ values (the **horizon**):

$$ \underbrace{(x_{t-L+1}, \dots, x_t)}_{\text{input}} \;\longrightarrow\; \underbrace{(x_{t+1}, \dots, x_{t+H})}_{\text{forecast}} $$

This sliding-window framing turns a raw series into many (input → target) training examples — exactly the format KUN expects.

## A few practical gotchas

- **Missing values & irregular timestamps** — fill, interpolate, or resample before training.
- **Data leakage** — never let information from the future leak into the input (a very common bug). Always split by time, not randomly.
- **Outliers & regime changes** — a holiday, a sensor failure, or a pandemic can break patterns the model learned.

With this vocabulary in hand, you are ready for the next question: *how do we actually produce a forecast?*
