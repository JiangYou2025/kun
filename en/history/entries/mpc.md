---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1980 · Control / Communications"
permalink: /en/history/e/mpc/
title: "Model Predictive Control (Cutler · Ramaker, 1980)"
lead: "Rather than chasing errors and correcting them after the fact, look a few steps ahead: use a model to predict the future, solve a constrained optimization, take only the first step, and then roll forward and start again."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the 1970s, the workhorse of industrial control was PID: adjusting according to the current error and its integral and derivative. It is simple and reliable, but essentially **reactive**: it only looks at the present, does not actively plan for the future, and has difficulty handling hard constraints gracefully, such as "the valve opening has an upper limit" or "the temperature must not exceed its limit". Yet processes in oil refining and petrochemicals are often multi-input multi-output, strongly coupled and subject to many operating constraints, and loop-by-loop PID tuning struggles to cope. [Bellman](../bellman-dp/)'s dynamic programming and optimal control theory already existed, but solving an infinite-horizon optimal control problem directly was out of reach for online computation.

### The problem

How can a controller **actively use predictions of the future**, **handle constraints explicitly**, and still be computable within each sampling period? Theoretical optimal control either lacked constraint handling or was computationally infeasible. Industry needed a compromise that was both optimal and deployable.

### Other approaches of the time (and their limits)

- **PID / classical feedback**: simple to tune and robust, but with no look-ahead, no constraint handling and difficulty coordinating coupled multivariable loops.
- **LQR / optimal control ([Kalman](../kalman/) and others)**: gives elegant state feedback, but its standard form has no inequality constraints, and it breaks down as soon as a constraint becomes active.
- **Pure dynamic programming**: theoretically optimal, but the curse of dimensionality makes solving over the full horizon online unrealistic.

### Method

Cutler and Ramaker introduced Dynamic Matrix Control (DMC), laying the foundation of model predictive control (MPC). The idea is the **receding horizon**: at each time $$t$$, use a process model to predict the outputs $$\hat{y}_{t+k}$$ over the next $$N$$ steps, and solve a finite-horizon constrained optimization:

$$ \min_{u_t,\dots,u_{t+M-1}} \sum_{k=1}^{N}\big\| \hat{y}_{t+k}-r_{t+k}\big\|_Q^2 + \sum_{k=0}^{M-1}\big\|\Delta u_{t+k}\big\|_R^2 $$

$$ \text{s.t.}\quad u_{\min}\le u_{t+k}\le u_{\max},\quad \Delta u_{\min}\le \Delta u_{t+k}\le \Delta u_{\max},\quad y_{\min}\le \hat{y}_{t+k}\le y_{\max} $$

Here $$r$$ is the reference trajectory, $$Q,R$$ are weights, and $$\Delta u$$ is the control increment. DMC builds its prediction model from step-response coefficients, and the whole problem is a quadratic program (QP). The key is that after solving for the entire optimal input sequence, **only the first step** $$u_t$$ is applied; at the next time step, a new measurement arrives, and the prediction and optimization are redone. This rolling structure of "predict, optimize, apply the first step, take feedback, predict again" combines the foresight of optimal planning with feedback that counters model errors and disturbances.

### Impact

DMC was a great success on refinery units at Shell and other companies: it could operate stably close to the constraint boundaries (which is often exactly where the economic optimum lies), markedly improving throughput and energy efficiency. MPC then became the de facto standard of advanced process control in the process industries, and spread to chemicals, power, automotive and even robotics.

### Significance and outlook

MPC engineered the idea of **prediction-driven decision-making**: control is no longer passive error correction, but constrained optimal planning based on rolling predictions of the future. The process models it relies on often come from [system identification](../system-identification/); its receding-horizon idea echoes the way [temporal-difference learning / Q-learning](../td-qlearning/) in reinforcement learning "uses predictions to guide the current action". Today, from autonomous driving to data-centre scheduling, wherever one "looks a few steps ahead, solves an optimization, takes a step, and looks again", the spirit of MPC lives on.
