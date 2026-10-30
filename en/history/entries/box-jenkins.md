---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1970 · Computing"
permalink: /en/history/e/box-jenkins/
title: "ARIMA and a Modelling Methodology (Box · Jenkins, 1970)"
lead: "Differencing tames non-stationarity; a three-stage procedure tames the modelling process. Box and Jenkins combined scattered time-series techniques into an operational, reproducible engineering methodology."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 5 · ARIMA](../../05/).

### Background

By the end of the 1960s, time series analysis had plenty of parts: [Yule](../yule-ar/)'s autoregression (AR), the moving average (MA) inspired by [Slutsky](../slutsky/), the theoretical ARMA framework provided by the [Wold decomposition](../wold/), and spectral methods. But these were mostly tools for stationary processes, whereas real data (sales, output, prices) usually carry trends and seasonality and are **not stationary**. Faced with a real series, practitioners lacked not only models but also a set of rules for "which model to use, how to choose the order and how to check it".

### The problem

Two levels of difficulty were intertwined. First, **how to handle non-stationarity**: series with trends or random-walk behaviour cannot be fitted directly with stationary models. Second, **how to make modelling systematic**: given concrete data, how does one choose among the many orders of AR, MA and ARMA on a principled basis, instead of by feel and trial and error? What was needed was a procedure that could be taught and reproduced.

### Other approaches of the time (and their limits)

- **Pure spectral / periodogram methods**: good at revealing frequency structure, but they do not directly provide a parametric generative model suited to forecasting and extrapolation.
- **Deterministic trend + seasonal decomposition**: splits the series into trend, seasonal and residual parts. Intuitive, but it makes strong assumptions about the shape of the trend, and the residuals often still contain modellable correlation structure.
- **Using AR or MA in isolation**: each works, but without unified criteria for selection and diagnosis it is easy to overfit or pick the wrong order.

### Method

Box–Jenkins introduced the **differencing operator** $$\nabla=1-B$$ (where $$B$$ is the lag operator, $$B X_t=X_{t-1}$$) to remove trends: difference a non-stationary series $$d$$ times to make it stationary, then model the stationary part with ARMA, giving **ARIMA(p,d,q)**:

$$ \phi(B)\,(1-B)^{d}\,X_t=\theta(B)\,\varepsilon_t $$

Here $$\phi(B)=1-\phi_1 B-\dots-\phi_p B^p$$ is the AR operator and $$\theta(B)=1+\theta_1 B+\dots+\theta_q B^q$$ the MA operator. With a seasonal period $$s$$ this extends to **SARIMA**, adding seasonal differencing $$(1-B^s)^D$$ and seasonal operators. More importantly, they proposed a **three-stage methodology**:

- **Identification**: use the shapes of the autocorrelation (ACF) and partial autocorrelation (PACF) functions to make a first determination of $$p,d,q$$;
- **Estimation**: fit the parameters by maximum likelihood or least squares;
- **Diagnostic checking**: test whether the residuals are approximately white noise (for example with the Ljung–Box test); if not, return to identification and iterate.

### Impact

This procedure turned time-series modelling from an empirical craft into teachable, reproducible engineering. ARIMA/SARIMA became the workhorse of forecasting for decades, widely used for economic, inventory, sales and demand forecasting, and it remains a strong baseline in statistical forecasting today. The iterative "identification, estimation, diagnosis" paradigm also became a general template for applied statistical modelling.

### Significance and outlook

Box–Jenkins made the crucial leap from the theoretical groundwork of [Yule](../yule-ar/), [Slutsky](../slutsky/) and [Wold](../wold/) to a practical methodology. Later developments extended along the same line: automatic order selection with information criteria (AIC, BIC), unit-root tests to decide how many times to difference, and [ARCH/GARCH](../arch/) to capture variance dynamics. Even today, with machine learning and deep forecasting in vogue, ARIMA remains an honest yardstick for whether a complex model really brings an improvement, and its engineering discipline of "model, check, revise" has lost none of its value.
