---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2017–19 · Computing"
permalink: /en/history/e/deepar/
title: "DeepAR: Global Probabilistic Forecasting (Amazon, 2017–19)"
lead: "Fitting a separate model to each of thousands of related series is extravagant, and new products have no history. Can a single global network learn them all at once?"
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 9 · Deep Learning](../../09/).

### Background

In industry, the objects of forecasting are often **huge numbers of related series**: demand for every product in every warehouse of an e-commerce business, the load of every household in an energy network. Classical statistical methods such as [ARIMA](../box-jenkins/) or exponential smoothing are **local**: they estimate parameters separately for each series, independently of the others. This struggles when series are numerous and short and new products (cold starts) appear frequently.

### The problem

Local models face a threefold dilemma: parameter estimates are unreliable when series are too short; fitting thousands of series one by one is expensive; and **a new series has no history**, so there is nothing to estimate from. Yet these series are in fact highly related: products in the same category or the same region often share seasonality and shape. **Could a single model share statistical strength across all series and directly provide the uncertainty of its forecasts?**

### Other approaches of the time (and their limits)

- **Local statistical models (ARIMA / ETS)**: interpretable and effective on a single series, but they share no information across series and have no answer to cold starts.
- **Machine-learning regression for point forecasts**: can use covariates, but usually outputs a single value and does not describe the forecast distribution, leaving decisions (such as safety stock) without a basis in uncertainty.
- **Hierarchical / grouped aggregation**: eases the short-series problem but struggles to express the nonlinear dynamics of individual series.

### Method

DeepAR trains a **global autoregressive RNN**: all series share the same set of parameters, and at each step the network outputs **the parameters of a probability distribution** rather than a single value. Given the history and covariates, an [LSTM](../lstm/) produces a hidden state $$h_t$$, which is mapped to likelihood parameters (for example the mean and variance of a Gaussian, or a negative binomial distribution for count data):

$$ \ell(z_t\mid \theta_t),\qquad \theta_t=\theta\big(h_t\big),\quad h_t=\mathrm{RNN}\big(h_{t-1},\,z_{t-1},\,x_t\big) $$

Training maximizes the log-likelihood of the whole series (with teacher forcing, feeding in the true $$z_{t-1}$$):

$$ \mathcal{L}=\sum_{t}\log \ell\big(z_t\mid \theta_t\big) $$

At prediction time it switches to **autoregressive sampling**: draw $$\hat z_t$$ from $$\ell(\cdot\mid\theta_t)$$, feed it back into the network, and repeat over many paths to obtain **Monte Carlo quantiles** of the future. To handle series whose magnitudes differ enormously, each series is also rescaled by its own mean.

### Impact

On benchmarks such as retail demand, DeepAR's forecasts were markedly more accurate than traditional local baselines, especially when series are numerous and of uneven length. It naturally supports **cold starts**: a new series can receive a sensible probabilistic forecast from covariates and the globally learned prior over shapes alone, and the model directly produces calibrated prediction intervals for downstream decisions.

### Significance and outlook

DeepAR established the "**global model + probabilistic output + autoregressive sampling**" paradigm of deep learning for time series, shifting the focus from "tuning parameters for each series" to "learning shared representations across series". This idea deeply influenced later work: whether the purely feed-forward [N-BEATS](../nbeats/), attention-based forecasters ([../transformer/](../transformer/)), or time-series foundation models ([../foundation-models/](../foundation-models/)), they all inherit the worldview of "one large model serving millions of series".
