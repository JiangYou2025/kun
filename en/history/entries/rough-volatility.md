---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2014–18 · Mathematics"
permalink: /en/history/e/rough-volatility/
title: "Rough Volatility (Gatheral · Jaisson · Rosenbaum, 2014–18)"
lead: "For decades people believed volatility had long memory and was quite “smooth”. When they actually measured its trajectory, they found it was abnormally rough — with a Hurst exponent far below ½."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Volatility is the lifeblood of finance, yet it cannot be observed directly. Since [GARCH](../garch/) and the stochastic volatility models, the mainstream consensus had two parts: volatility has **long memory** (its autocorrelation decays slowly), and its driving process is usually modelled as **Brownian motion** (standard stochastic volatility) or as fractional Brownian motion with long memory, $$ H>\tfrac12 $$. In 2014 the paper "Volatility is rough" by Gatheral, Jaisson and Rosenbaum carried out a scaling analysis directly on time series of **realized volatility** and reached a conclusion that shook the field: the volatility trajectory is **abnormally rough**.

### The problem

With high-frequency data, it finally became possible to build **realized volatility** from intraday returns, and thus to approximately "observe" the trajectory of volatility itself. That made it possible to answer an old question head-on: **just how smooth is the random process that drives volatility?** Standard Brownian motion corresponds to a Hurst exponent $$ H=\tfrac12 $$; long-memory models claim $$ H>\tfrac12 $$ (persistent, smooth). Which side would the measurements come down on?

### Other approaches of the time (and their limits)

- **Classical stochastic volatility (e.g. Heston)**: volatility is driven by standard Brownian motion ($$ H=\tfrac12 $$), which is mathematically convenient and allows semi-closed-form pricing, but struggles to fit the skew of the implied volatility smile at both short and long maturities simultaneously.
- **Long-memory / fractional SV ($$ H>\tfrac12 $$)**: introduces persistence to explain the slow decay of volatility autocorrelation, but points in the opposite direction from the measurements and does not address "short-term roughness".
- **Jump-diffusion models**: use jumps to create spikes, but mistake "roughness" for discrete jumps, masking the low regularity of the continuous trajectory itself.

### Method

The core is to measure the **scaling law** of the log-volatility series. For a lag $$ \Delta $$, compute the moments of order $$ q $$ of the increments:

$$ m(q,\Delta) = \mathbb{E}\big[\,|\log\sigma_{t+\Delta} - \log\sigma_t|^q\,\big] \sim \Delta^{\,q H} $$

On log–log axes, $$ \log m(q,\Delta) $$ against $$ \log\Delta $$ is a straight line whose slope gives $$ qH $$, from which the **Hurst exponent $$ H $$** is estimated. Across a wide range of assets and periods, the empirical results are strikingly consistent:

$$ H \approx 0.1 \;(\ll \tfrac12) $$

Such a small $$ H $$ means the volatility trajectory is **extremely rough** (its local regularity is low, and it is "nowhere differentiable" to a degree far beyond Brownian motion). On this basis, models such as **rough Bergomi (rBergomi)** model volatility as driven by a **fractional Brownian motion** $$ W^H $$:

$$ \log\sigma_t^2 = \xi + \eta\, W_t^{H},\qquad H<\tfrac12 $$

where the covariance structure of $$ W^H $$ is controlled by $$ H $$. It is worth stressing that roughness (small $$ H $$, low regularity at short range) and long memory (slow decay of autocorrelation) are **phenomena at two different scales**; rough volatility emphasizes the former, correcting the old view that conflated the two.

### Impact

With only three or four parameters, rBergomi reproduces both the **term structure and the smile skew** of the implied volatility surface, and in particular fits precisely the steep skew of short-dated options that classical models could never bring down — the direct financial imprint of roughness. Rough volatility promptly became one of the most active directions in quantitative finance, spawning efficient simulation and pricing algorithms for fractional processes, as well as a corresponding explanation in terms of market microstructure (the self-exciting Hawkes processes of high-frequency order flow can, in the scaling limit, give rise to rough volatility).

### Significance and outlook

Rough volatility is a model case of "**letting the data speak**": once high-frequency data finally let us look volatility's trajectory in the eye, it overturned the smooth/long-memory default assumptions used for decades and brought **fractional Brownian motion and low Hurst exponents** back to the forefront of financial modelling. It shares a lineage with the questions [econophysics](../econophysics/) asked about scaling and long memory, and echoes across generations the rescaled-range analysis of [Hurst](../hurst/). A unified explanation running from microscopic order flow to the macroscopic volatility surface is still being pursued, but "volatility is rough" has become a fact that modern derivatives pricing cannot ignore.
