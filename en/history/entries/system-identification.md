---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1970s–80s · Control / Communications"
permalink: /en/history/e/system-identification/
title: "System Identification (Åström · Ljung, 1970s–80s)"
lead: "Engineers had no ready-made differential equations, only piles of input–output data — so let the data \"grow\" the model itself: identifying dynamic systems from signals."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Mid-20th-century control theory was built on "the model comes first": [Kalman](../kalman/)'s state space, optimal control and stability analysis all assumed that the system's differential or difference equations were known. But real chemical reactors, aircraft and paper machines often cannot be described by exact equations derived from first principles — the parameters are unknown and the mechanisms too complex. What engineers actually had were the **input $$u_t$$ and output $$y_t$$ sequences** recorded after exciting the system. Inferring a dynamic model from these two signals became the key to bringing control into engineering practice.

### The problem

The time series models of statistics (such as [Yule](../yule-ar/)'s AR and Box–Jenkins's ARMA) describe a single series with no external input, whereas control systems have **manipulable inputs**. What was needed was a class of models that could absorb exogenous inputs and reliably estimate parameters from noisy data, while answering three engineering questions: **Which model structure? What order? Can the estimated model be trusted?**

### Other approaches of the time (and their limits)

- **Pure physical modelling (white box)**: derive equations from conservation laws. The physical meaning is clear, but for complex industrial processes the equations often cannot be written down or the parameters cannot be measured.
- **Classical frequency-domain identification (frequency sweeps)**: inject sinusoidal signals into the system and measure the frequency response. Intuitive, but time-consuming, sensitive to noise, and hard to carry out online while the loop is closed.
- **Purely statistical ARMA fitting**: ignores the controllable input and treats everything as spontaneous fluctuation, discarding the causal layer that control cares about most — how the input affects the output.

### Method

Åström and Ljung combined statistical estimation with control and developed system identification. The core model is a difference equation with exogenous input, **ARX**:

$$ y_t + a_1 y_{t-1} + \cdots + a_{n_a} y_{t-n_a} = b_1 u_{t-1} + \cdots + b_{n_b} u_{t-n_b} + \varepsilon_t $$

The more general **ARMAX** also equips the noise with a moving-average term $$C(q)\varepsilon_t$$. The unified formulation is the prediction error method (PEM): with model parameters $$\theta$$, the model yields a one-step prediction $$\hat{y}_t(\theta)$$ and a prediction error $$\varepsilon_t(\theta)=y_t-\hat{y}_t(\theta)$$, and one minimizes

$$ \hat{\theta} = \arg\min_{\theta}\; \frac{1}{N}\sum_{t=1}^{N}\varepsilon_t(\theta)^2 $$

In the ARX case this is linear least squares with a closed-form solution; ARMAX requires iteration. **Order selection** relies on information criteria such as AIC/BIC to trade goodness of fit against the number of parameters; **model validation** relies on residual tests — if $$\varepsilon_t$$ is close to white noise and uncorrelated with past inputs, the model has squeezed out all the predictable structure.

### Impact

Identification methods allowed fields such as papermaking, oil refining and aviation to obtain usable prediction and control models without precise knowledge of the mechanisms, and supported online recursive updating (to adapt to slowly changing processes). Ljung's *System Identification: Theory for the User* became the standard textbook, and the accompanying MATLAB System Identification Toolbox turned the whole workflow into widely used engineering practice.

### Significance and outlook

System identification built a bridge between statistical time series and control engineering: it distilled "estimating dynamic models from data" into a structured engineering methodology with order selection and validation. Its ideas — prediction error, model validation, the overfitting trade-off — share the same roots as today's train–validate paradigm in machine learning. It directly supplied the models that 1980s [model predictive control](../mpc/) relies on for its rolling forecasts, and it runs in a straight line to modern "data-driven control" and "grey-box modelling".
