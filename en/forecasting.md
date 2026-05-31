---
lang: en
ref: forecasting
permalink: /en/forecasting/
title: "How to forecast"
lead: "Forecasting is a workflow, not a single model. This page walks through that workflow — from a trivial baseline up to deep learning — and shows how to know whether your forecast is any good."
prev: time-series
next: kun
math: true
---

## The forecasting workflow

A reliable forecasting project almost always follows the same loop:

1. **Define the task.** What are you predicting, how far ahead (the horizon $H$), and how often?
2. **Prepare the data.** Clean missing values, resample to a regular frequency, handle outliers.
3. **Split by time.** Train on the past, validate on a more recent slice, test on the most recent slice. *Never shuffle.*
4. **Start with a baseline.** If your fancy model can't beat it, the model is the problem.
5. **Train and tune** progressively more capable models.
6. **Evaluate** on held-out data with the right metric.
7. **Monitor** in production and retrain as the world drifts.

> The single biggest mistake beginners make is skipping step 3 or step 4. A leaderboard number means nothing without an honest time-based split and a baseline to beat.

## Baselines you must beat

Always compute these first — they are free and surprisingly strong:

- **Naïve / persistence:** tomorrow = today, i.e. $\hat{x}_{t+1} = x_t$.
- **Seasonal naïve:** this Monday = last Monday, i.e. $\hat{x}_{t+1} = x_{t+1-s}$ for season length $s$.
- **Moving average / drift:** extend the recent average or recent slope.

## The model landscape

### 1. Classical statistical models
- **ARIMA** — models autocorrelation and differencing; great for a single, well-behaved series.
- **Exponential smoothing (ETS / Holt-Winters)** — weights recent observations more; excellent with clear trend + seasonality.

*Strengths:* interpretable, strong on small data. *Limits:* one series at a time, struggle with many interacting variables and long horizons.

### 2. Machine-learning models
- **Gradient boosting (XGBoost, LightGBM)** on engineered features (lags, rolling means, calendar features like day-of-week).

*Strengths:* handles many covariates, robust. *Limits:* you do the feature engineering by hand.

### 3. Deep-learning models
- **RNN / LSTM / GRU, TCN, and Transformers** learn temporal patterns directly from raw windows.
- **Modern forecasters** — PatchTST, DLinear, N-BEATS, and **Kernel U-Net (KUN)** — are built specifically for long-horizon, multivariate forecasting.

*Strengths:* learn complex, shared patterns across many series; scale to long horizons. *Limits:* need more data and compute.

## Choosing a metric

The metric encodes what "good" means for *your* problem.

| Metric | Formula | Use when |
|---|---|---|
| **MAE** | $\frac{1}{H}\sum\lvert x_t-\hat{x}_t\rvert$ | You want errors in the original units, robust to outliers |
| **RMSE** | $\sqrt{\frac{1}{H}\sum (x_t-\hat{x}_t)^2}$ | Large errors should be penalised more |
| **MAPE** | $\frac{100}{H}\sum\frac{\lvert x_t-\hat{x}_t\rvert}{\lvert x_t\rvert}$ | You need a scale-free percentage (avoid near-zero values) |

Report your metric **against the baseline**, not in isolation.

## Validating over time

Because you cannot shuffle, use **rolling / expanding-window cross-validation**: train up to a point, forecast the next block, slide forward, repeat. This simulates how the model will actually be used and gives you a distribution of errors rather than one lucky number.

```
|--- train ---|--- test ---|
|------ train ------|--- test ---|
|--------- train ---------|--- test ---|
```

## Single-step vs. multi-step

To forecast a horizon $H > 1$ you can either:

- **Iterative (recursive):** predict one step, feed it back as input, repeat. Simple, but errors compound.
- **Direct / multi-output:** predict all $H$ steps at once. More stable for long horizons — and this is exactly how **KUN** produces its forecast.

With the workflow and the vocabulary in place, you're ready to meet the model itself.
