---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1987 · Computing"
permalink: /en/history/e/cointegration/
title: "Cointegration and Error Correction (Engle · Granger, 1987)"
lead: "Two series, each wandering aimlessly, yet tied together by an invisible rubber band. Cointegration tells you which “spurious correlations” are in fact real relationships."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 6 · Volatility and Cointegration](../../06/).

### Background

Many economic series (GDP, prices, exchange rates, interest rates) are **non-stationary**: they have no fixed mean and drift like a random walk; they are called **unit-root** or $$I(1)$$ processes. In 1974 Granger and Newbold sounded the alarm: regressing two independent random walks on each other often yields a very high $$R^2$$ and "significant" coefficients, a **spurious regression**. The series look strongly correlated but are in fact unrelated; their drifts merely happen to point the same way. This makes classical regression dangerous on non-stationary data. Yet economic theory firmly holds that some variables share a long-run equilibrium (consumption and income, for example). How can a "false, spurious correlation" be told apart from a "genuine long-run relationship"?

### The problem

If both series are $$I(1)$$, a direct regression cannot be trusted. But if there is some stable long-run link between them, how should that link be rigorously defined and tested? In other words: **when is some linear combination of two non-stationary series actually stationary?**

### Other approaches of the time (and their limits)

- **Regression in levels**: OLS on the raw non-stationary series. This is the very breeding ground of spurious regression; the statistics are distorted and the conclusions unreliable.
- **Difference everything, then regress**: difference each series to stationarity before modelling. This removes spurious regression but **throws away the information about long-run equilibrium between variables**, leaving only short-run changes.
- **Structural economic models**: impose constraints from theory. They depend on the model being correctly specified and lack a statistical test grounded in the data.

### Method

Engle and Granger proposed **cointegration**: if $$x_t,y_t$$ are each $$I(1)$$, but there is a constant $$\beta$$ that makes a linear combination stationary,

$$ z_t = y_t - \beta\, x_t \;\sim\; I(0)\quad(\text{stationary}) $$

then the two are said to be cointegrated, and $$z_t$$ is the deviation from the long-run equilibrium. The test has two steps: first regress the series in levels to estimate $$\beta$$ and obtain the residuals $$\hat z_t$$; then use the **ADF (augmented Dickey–Fuller) unit-root test** to decide whether $$\hat z_t$$ is stationary. The ADF test runs the regression

$$ \Delta \hat z_t = \rho\,\hat z_{t-1} + \sum_{i=1}^{p}\gamma_i\,\Delta \hat z_{t-i} + u_t $$

and tests $$\rho=0$$ (a unit root, no cointegration) against $$\rho<0$$ (stationary, cointegrated). If cointegration holds, the **Granger representation theorem** guarantees that the system can be written as an **error correction model (ECM)**:

$$ \Delta y_t = \gamma\, z_{t-1} + \sum_i a_i \Delta y_{t-i} + \sum_j b_j \Delta x_{t-j} + \varepsilon_t,\qquad \gamma<0 $$

It fuses short-run dynamics (the differenced terms) and long-run equilibrium ($$z_{t-1}$$) into one model: as soon as the system leaves equilibrium, $$z_{t-1}\neq 0$$, the "rubber band" pulls it back at speed $$\gamma$$.

### Impact

Cointegration provided a rigorous definition and a practical test for long-run relationships between non-stationary series, dissolving the spurious-regression dilemma at a stroke without discarding long-run information the way blind differencing does. The ECM became a standard tool in macroeconomic and financial modelling (pairs trading, cash-and-carry arbitrage). Granger, for cointegration, and Engle, for [ARCH](../arch/), shared the 2003 Nobel Prize in Economics.

### Significance and outlook

Engle–Granger translated the economic intuition of "long-run equilibrium + short-run adjustment" into the mathematical language of stationarity, reshaping the econometrics of non-stationary time series. Their two-step method was later generalized by Johansen's multivariate maximum-likelihood approach to multiple cointegrating vectors. The idea of cointegration and error correction, **finding the stable combinations that stay tethered in a drifting world**, remains a cornerstone of statistical arbitrage, cross-market relationship modelling and even modern causal analysis of time series.
