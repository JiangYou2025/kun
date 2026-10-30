---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1982 · Computing"
permalink: /en/history/e/arch/
title: "The ARCH Model (Engle, 1982)"
lead: "Storms in financial markets come in clusters: calm follows calm, turmoil follows turmoil. Engle let the variance itself rise and fall over time, writing “volatility clustering” into the model."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 6 · Volatility and Cointegration](../../06/).

### Background

Classical time series analysis ([Yule](../yule-ar/)'s AR, Box–Jenkins's ARMA) focuses on the **conditional mean** of a series: roughly what the next value will be. These models assume the error term is **homoscedastic**, meaning the size of fluctuations stays constant. That is good enough in many settings, but financial data plainly refuse to comply: the daily volatility of stock returns swings between large and small, and it shows **clustering**: big rises and falls tend to come in runs, and calm periods arrive in runs too. Risk hides precisely in this changing variance, and the classical models are blind to it.

### The problem

A return series itself is nearly free of autocorrelation (its mean is hard to predict), yet its **square** (or absolute value) is strongly autocorrelated: if volatility is high today, it is likely to be high tomorrow as well. This shows that **the conditional variance varies over time and is predictable**. How can the variance be made a function of the past, rather than a fixed constant, while keeping the model estimable?

### Other approaches of the time (and their limits)

- **Homoscedastic ARMA**: assumes a constant error variance. It can model the mean, but systematically underestimates risk in turbulent periods and overestimates it in calm ones.
- **Rolling-window variance**: uses the sample variance of the most recent periods as current volatility. Simple, but the window length is entirely subjective, and old data at the edge of the window are forgotten abruptly, all at once.
- **Stochastic volatility (SV)**: lets the variance follow a latent process of its own. Flexible in theory, but at the time models with latent variables were hard to estimate, and no ready-made maximum-likelihood method existed.

### Method

Engle proposed the autoregressive conditional heteroscedasticity (ARCH) model. Write the residual as $$\varepsilon_t = \sigma_t z_t$$, where $$z_t$$ is i.i.d. standard noise with mean 0 and variance 1, and let the **conditional variance** $$\sigma_t^2$$ be determined by past squared residuals:

$$ \sigma_t^2 = \alpha_0 + \sum_{i=1}^{q}\alpha_i\,\varepsilon_{t-i}^2,\qquad \alpha_0>0,\;\alpha_i\ge 0 $$

The meaning is intuitive: a large shock in an earlier period (large $$\varepsilon_{t-i}^2$$) pushes up the variance in the current period, and **volatility clustering** emerges naturally. The constraints $$\alpha_0>0,\alpha_i\ge0$$ keep the variance positive. Under the model, given the past information $$\mathcal{F}_{t-1}$$,

$$ \varepsilon_t \mid \mathcal{F}_{t-1} \sim \mathcal{N}\!\big(0,\ \sigma_t^2\big) $$

so the whole model can be estimated by **maximum likelihood**, which is exactly what made it much easier to put into practice than stochastic volatility. The sum $$\sum_i \alpha_i$$ measures how persistent volatility shocks are.

### Impact

ARCH was the first to turn "the variance moves" into a statistical model that can be estimated, tested and used for forecasting, and it described the volatility of inflation and financial returns far better than homoscedastic models. It launched an entire research programme on volatility modelling and laid the groundwork for risk measures such as VaR. Engle received the 2003 Nobel Prize in Economics for ARCH.

### Significance and outlook

ARCH extended the focus of modelling from "forecasting the mean" to "**forecasting risk**", establishing the conditional variance as an object of study in its own right. One immediate limitation: capturing long-memory persistence in volatility often requires a very high order $$q$$ and too many parameters. Four years later [Bollerslev's GARCH](../garch/) solved this elegantly by adding lags of the variance itself. From ARCH grew EGARCH, GJR, stochastic volatility, realized volatility and today's neural-network volatility models; volatility modelling has remained a central battleground of financial time series ever since.
