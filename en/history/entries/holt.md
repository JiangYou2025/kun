---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1957 · Control / Communications"
permalink: /en/history/e/holt/
title: "Holt's Linear Trend Method (Holt, 1957)"
lead: "Simple exponential smoothing can only “extrapolate flat”, so it always lags half a step behind steadily growing sales. Holt fitted it with a second recursion, tracking the “level” and the “trend” separately."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 3 · Exponential Smoothing](../../03/).

### Background

In 1957, in a naval research memorandum at the Carnegie Institute of Technology, Charles C. Holt extended [simple exponential smoothing (SES)](../brown-ses/) to series with a trend. The setting was still production and inventory planning: real demand often does not fluctuate around a fixed level but **keeps growing or declining** — populations rise, markets expand, prices change. A forecasting system has to keep up with this directional drift.

### The problem

SES maintains only a "level" $$\ell_t$$, and its forecast of the future is flat: $$\hat{x}_{t+h}=\ell_t$$. When the series has a stable trend, flat extrapolation **lags systematically**: rising series are always underestimated, falling ones always overestimated, and the error accumulates and grows with the forecast horizon $$h$$. **Could the model also learn and extrapolate the trend while keeping the "online, memory-light" advantages of exponential smoothing?**

### Other approaches of the time (and their limits)

- **[SES](../brown-ses/)**: efficient online, but has only a level and extrapolates flat, so it is structurally biased on trending series.
- **Global linear regression (fitting a straight line against time)**: can express a trend, but assumes it is constant and requires batch recomputation, so it cannot adapt online to slow changes in the slope.
- **SES on the differenced series**: removes the trend, but mixes "level" and "trend" together, making them hard to interpret and extrapolate separately, and tuning is not intuitive.

### Method

Holt introduced **two states and two smoothing coefficients**: the level $$\ell_t$$ and the trend (slope) $$b_t$$, each updated recursively:

$$ \ell_t = \alpha\, x_t + (1-\alpha)\,(\ell_{t-1}+b_{t-1}) $$

$$ b_t = \beta\,(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1} $$

In the level update, "last level plus last trend", $$\ell_{t-1}+b_{t-1}$$, is the internal forecast for the current period, which is then balanced against the new observation $$x_t$$ by $$\alpha$$; the trend update balances "the actual increase in the level this period", $$\ell_t-\ell_{t-1}$$, against the old trend by $$\beta$$. The $$h$$-step forecast is a **linear extrapolation**:

$$ \hat{x}_{t+h} = \ell_t + h\,b_t $$

$$\alpha,\beta\in(0,1)$$ control the update speed of the level and of the trend respectively. The whole scheme is still an O(1) online recursion, needing only one extra stored value, $$b_{t-1}$$.

### Impact

For trending demand and sales series, Holt's method forecasts far more accurately than SES, and the forecast line tilts naturally with $$h$$ instead of lagging. It upgraded exponential smoothing from "tracking a stationary level" to "tracking level + trend", while keeping all the benefits of simple implementation, adaptivity and minimal computation. In practice it is often combined with a **damped trend** (giving the trend a damping factor $$\phi<1$$) to keep the slope from diverging in long-range extrapolation.

### Significance and outlook

Holt generalized exponential smoothing from a single-state recursion to a multi-state one, establishing the paradigm of "decompose into components, smooth each one". Add one more set of seasonal terms along this path and you get the contemporaneous [Holt–Winters seasonal method](../holt-winters/); and the two-state "level + trend" linear extrapolation structure is exactly a special case of the local linear trend state space model of the [Kalman filter](../kalman/). From the ETS framework to the default baselines in today's forecasting libraries, Holt's two recursions remain an unavoidable starting point.
