---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1950s · Computing"
permalink: /en/history/e/brown-ses/
title: "Simple Exponential Smoothing (Brown, 1950s)"
lead: "Radar tracking and warehouse restocking both need to “compute on the move”. With a recursion that stores just one number, Brown compressed the entire history, with exponentially decaying weights, into the best current guess."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 3 · Exponential Smoothing](../../03/).

### Background

During and after the Second World War, Robert G. Brown worked on fire control and air defence for the US Navy; after the war he moved into operations research, forecasting demand for large numbers of inventory items. The two settings share an engineering constraint: data arrive **one at a time**, and computing and storage resources are very limited. Radar must track in real time, and an inventory system must manage thousands of parts at once. Retrieving the whole history to refit a curve was neither computable nor storable.

### The problem

Classical methods (moving averages, least-squares fitting) need to keep a window or even the whole history, and **they treat all historical samples equally**. In reality, the more recent an observation, the better it represents the current true level. **Could there be a forecast that stores just "one number", updates at O(1) cost with each new observation, and automatically lets the influence of older data fade away?**

### Other approaches of the time (and their limits)

- **Simple moving average**: averages the latest $$k$$ periods with equal weights. It must buffer $$k$$ values, and the weights are cut off like a cliff: data that have just slid out of the window suddenly drop to zero, making it both sluggish and unsmooth.
- **Global least squares / regression fitting**: accurate, but it must keep the whole history and recompute in batch, so it cannot run online and does not scale to huge numbers of items.
- **The naive method (use the last value as the forecast)**: the ultimate in convenience, but with no resistance to noise at all; a single fluctuation passes straight into the forecast.

### Method

Brown proposed **simple exponential smoothing (SES)**: maintain a "level" $$\ell_t$$ that moves towards each new observation by a fixed proportion every period:

$$ \ell_t = \alpha\, x_t + (1-\alpha)\,\ell_{t-1},\qquad 0<\alpha<1 $$

where $$x_t$$ is the current observation and $$\alpha$$ the smoothing coefficient. The forecast $$h$$ steps ahead is simply $$\hat{x}_{t+h}=\ell_t$$ (flat extrapolation). Unrolling the recursion reveals that it is in essence an **exponentially weighted average**:

$$ \ell_t = \alpha\sum_{j=0}^{t-1}(1-\alpha)^{j}\,x_{t-j} + (1-\alpha)^{t}\ell_0 $$

The weight of older observations decays geometrically as $$(1-\alpha)^{j}$$: it never reaches zero but shrinks quickly. A larger $$\alpha$$ makes the forecast more responsive and closer to new data; a smaller one makes it smoother and more robust to noise. The whole computation only needs to store the single number $$\ell_{t-1}$$, and each update costs a constant O(1).

### Impact

SES spread rapidly in inventory and demand forecasting: it is extremely simple to implement, uses almost no memory and is robust on stationary series without trend. It turned "weighting the history" from a batch-fitting exercise into an online recursion that can run on indefinitely. It was later shown that SES is exactly the optimal forecast of an **ARIMA(0,1,1)** process, giving this humble formula a solid statistical foundation.

### Significance and outlook

SES established the core idea of the exponential smoothing family: **carry the history in a recursive state, and forget the past with exponential weights**. It grew upward into [Holt's linear trend method](../holt/), which handles trends, and then into [Holt–Winters](../holt-winters/) with seasonality. Its online stance of "maintain a state, then predict and update in two steps" also echoes the [Kalman filter](../kalman/), born in the same period. Today's EWMA monitoring in streaming systems, and momentum and Adam in gradient optimization, are at heart still Brown's one-line recursion.
