---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1960 · Control / Communications"
permalink: /en/history/e/holt-winters/
title: "Holt–Winters Seasonal Smoothing (Winters, 1960)"
lead: "Sales jump every Christmas. Winters added a set of seasonal recursions to “level + trend”, and exponential smoothing learned to celebrate the holidays."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 4 · Kalman Filtering](../../04/).

### Background

In 1960 Peter R. Winters published "Forecasting Sales by Exponentially Weighted Moving Averages", taking his colleague [Holt](../holt/)'s linear trend method one step further. One of the most persistent structures in business demand is **seasonality**: retail spikes at year end, energy consumption follows hot and cold spells, foot traffic cycles weekly. Earlier generations of exponential smoothing could track the level and the trend, but were helpless against such periodic ups and downs.

### The problem

[SES](../brown-ses/) tracks the level and [Holt](../holt/) adds the trend, but both assume the series has no recurring rises and falls with a fixed period. Faced with seasonal sales, they treat the regular yearly swings as noise and keep correcting back and forth, so the forecast can neither rise in the peak season nor drop in the off season. **Could a seasonal pattern of length $$m$$ be learned explicitly and extrapolated while keeping the online recursion of exponential smoothing?**

### Other approaches of the time (and their limits)

- **[Holt's linear trend method](../holt/)**: tracks level and trend, but has no seasonal term and is systematically biased on periodic series.
- **Seasonal dummy regression / harmonic regression**: can express seasonality, but usually assumes a fixed seasonal shape and requires batch fitting, making it hard for the seasonal pattern to evolve slowly over time.
- **Seasonal adjustment first, then forecasting (e.g. X-11)**: a two-stage process that is cumbersome, and the adjustment is not aligned with the forecasting objective.

### Method

On top of Holt's level $$\ell_t$$ and trend $$b_t$$, Winters added a set of **seasonal factors** $$s_t$$ (period length $$m$$): three sets of recursions with three smoothing coefficients $$\alpha,\beta,\gamma$$. Taking the **additive** form (roughly constant seasonal amplitude) as an example:

$$ \ell_t = \alpha\,(x_t-s_{t-m}) + (1-\alpha)(\ell_{t-1}+b_{t-1}) $$

$$ b_t = \beta\,(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1},\qquad s_t = \gamma\,(x_t-\ell_t) + (1-\gamma)\,s_{t-m} $$

The forecast adds the three together and extrapolates: $$\hat{x}_{t+h}=\ell_t+h\,b_t+s_{t-m+((h-1)\bmod m)+1}$$. When the seasonal amplitude scales in proportion to the level, the **multiplicative** form is used instead — the level update uses $$x_t/s_{t-m}$$, the seasonal update uses $$x_t/\ell_t$$, and the forecast combines them multiplicatively, $$\hat{x}_{t+h}=(\ell_t+h\,b_t)\,s_{t-m+\dots}$$. Each seasonal factor is updated once every $$m$$ periods, so the seasonal pattern adapts slowly to the data.

### Impact

Holt–Winters became the classic baseline for series with trend and seasonality: simple to implement, efficient online and interpretable (level, trend and seasonal components are plain to see). It is still used today in retail, energy and operations forecasting. It completed the exponential smoothing family as the full "level–trend–season" trio.

### Significance and outlook

Holt–Winters marked the maturity of exponential smoothing, and was later absorbed into the unified **ETS (Error–Trend–Seasonal) state space framework** — each variant corresponds to a state space model whose likelihood and prediction intervals can be computed with the [Kalman filter](../kalman/), which fits neatly with the theme of this chapter. From ETS to TBATS with multiple seasonalities, and on to the default baselines of modern forecasting tools, the idea of "smoothing component by component, each with its own recursion" remains the yardstick for whether a complex model is truly useful.
