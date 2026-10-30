---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1960 · Control / Communications"
permalink: /en/history/e/kalman/
title: "The Kalman Filter and State Space (Kálmán, 1960)"
lead: "Given noisy observations, how can the true state of a system be squeezed out in real time? Kálmán gave a two-step predict–update recursion, and it helped Apollo find its way home."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 4 · Kalman Filtering](../../04/).

### Background

In 1960 Rudolf E. Kálmán published "A New Approach to Linear Filtering and Prediction Problems". At the time, spaceflight and guidance urgently needed to estimate a vehicle's position and velocity **in real time** from noisy sensors. The previous generation, Wiener–Kolmogorov filtering, gave an optimal solution in the frequency domain, but it required stationarity, needed the entire history and was hard to run recursively on an onboard computer. The era called for an estimation method that could compute on the go with minimal resources.

### The problem

The true state (position, velocity) is invisible; all that is available are indirect observations corrupted by noise (radar, gyroscopes). **At each instant, how can "the prior prediction from the system dynamics" and "the noisy observation that has just arrived" be fused optimally, so as to estimate the hidden state recursively and in real time, while quantifying the uncertainty of the estimate?**

### Other approaches of the time (and their limits)

- **Wiener–Kolmogorov filtering**: theoretically optimal, but limited to stationary processes, based on spectra and the whole history, non-recursive, and unsuitable for online and time-varying systems.
- **Recursive least squares (RLS)**: can update parameters online, but does not explicitly model the dynamics of "a state evolving over time + process noise".
- **[Exponential smoothing](../holt/) methods**: efficient recursions, but the smoothing coefficients are set by experience, there is no optimal gain derived from the noise statistics, and no covariance is output.

### Method

Kálmán described the system in **state space**: the hidden state $$x_t$$ evolves linearly, and the observation $$z_t$$ is a linear map of the state, each with Gaussian noise:

$$ x_t = F x_{t-1} + w_t,\qquad z_t = H x_t + v_t,\quad w_t\sim\mathcal{N}(0,Q),\ v_t\sim\mathcal{N}(0,R) $$

Estimation proceeds in a two-step recursion. **Predict** (extrapolate the state and covariance with the dynamics):

$$ \hat{x}_{t}^{-}=F\hat{x}_{t-1},\qquad P_t^{-}=F P_{t-1}F^{\top}+Q $$

**Update** (correct with the new observation $$z_t$$), the core of which is the **Kalman gain** $$K_t$$:

$$ K_t = P_t^{-}H^{\top}\big(H P_t^{-}H^{\top}+R\big)^{-1},\qquad \hat{x}_t=\hat{x}_t^{-}+K_t\big(z_t-H\hat{x}_t^{-}\big) $$

and update the covariance $$P_t=(I-K_tH)P_t^{-}$$. The gain $$K_t$$ is the key: when the observation noise $$R$$ is small (the observation is trustworthy), $$K_t$$ is large and the new data is trusted more; when the prediction uncertainty $$P_t^{-}$$ is small, $$K_t$$ is small and the model's prediction is trusted more. The term in parentheses, $$z_t-H\hat{x}_t^{-}$$, is the **innovation** — the difference between observation and prediction. Under linear-Gaussian assumptions, this is the optimal estimate in the **minimum mean-square error** sense.

### Impact

The Kalman filter was soon used in Apollo navigation, inertial guidance and radar tracking, and quickly spread through signal processing and control engineering. It only needs to store the current state and covariance, with constant cost per step, yet it delivers both a **point estimate and its uncertainty**, which makes it extremely practical in engineering. For nonlinear systems, the extended Kalman filter (EKF) and the unscented Kalman filter (UKF) followed.

### Significance and outlook

The Kalman filter established the "predict–update" recursion as the general paradigm of sequential estimation, and the state space model became a unifying framework for time series — [exponential smoothing](../holt-winters/), structural time series and ARIMA can all be written in state space form and estimated, with likelihoods computed, by the Kalman filter. It mirrors [Bellman's dynamic programming](../bellman-dp/) (one is optimal estimation, the other optimal control; together they form LQG), and shares a lineage with the "innovation" idea of [Doob's martingales](../doob-martingale/). From spacecraft to today's SLAM, sensor fusion and probabilistic filtering, the way home is still paved with these two steps.
