---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/optimization/
title: "Optimization"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Optimization means finding the set of variables that makes an **objective function** optimal (maximal or minimal), possibly subject to constraints. Training a model is, at heart, solving an optimization problem — driving the "loss" as low as possible.

## Intuition

The three ingredients of optimization can be pictured as "finding the cheapest house":

- **Objective function**: the thing you want to minimize (the price);
- **Decision variables**: the things you can adjust (location, floor area, storey);
- **Constraints**: the limits that must be respected (budget, commute time, number of rooms).

Optimization means picking, among all the options that satisfy the constraints, the one that makes the objective best. In machine learning, the objective function is the **loss**, the decision variables are the **model parameters**, and the constraints may be regularization terms or parameter ranges.

## Mathematical formulation

General form:

$$
\min_{\theta}\ f(\theta)\quad
\text{s.t.}\quad g_i(\theta)\le 0,\quad h_j(\theta)=0
$$

- $f(\theta)$ — the objective / [loss function](../loss-function/);
- $\theta$ — the decision variables (model parameters);
- $g_i\le 0$ — inequality constraints; $h_j=0$ — equality constraints;
- without constraints only $\min_\theta f(\theta)$ remains, which is exactly the situation in most of deep learning.

Necessary condition for an optimum (unconstrained, differentiable): **the [gradient](../gradient/) is zero**

$$
\nabla f(\theta^\*)=0
$$

But a point where the gradient vanishes may be a minimum, a maximum or a saddle point; second-order information (the Hessian matrix) is needed to tell them apart.

## A concrete example

Minimize $f(\theta)=\theta^2-4\theta+5$. Set the derivative to zero:

$$
f'(\theta)=2\theta-4=0\ \Rightarrow\ \theta^\*=2,\quad f(2)=1
$$

The second derivative $f''=2>0$ confirms it is a minimum. The problem is [convex](../convex-optimization/), so $\theta^\*=2$ is also the global optimum.

```python
import numpy as np
theta = 0.0          # approach it by gradient descent instead of solving analytically
for _ in range(50):
    theta -= 0.1 * (2*theta - 4)
print(round(theta, 4))   # ≈ 2.0
```

When a function is too complex to solve analytically (as neural networks are), we switch to **iterative** methods such as [gradient descent](../gradient-descent/) that approach the solution step by step.

{% include fviz/optimizer.html %}

## Why it matters / where it is used

- **Training = optimization**: almost all "learning" can be written as "minimize some loss".
- **Family of methods**: closed-form solutions (least squares), first-order methods ([gradient descent](../gradient-descent/), SGD, [Adam](../adam/)), second-order methods (Newton's method), constrained optimization (Lagrange multipliers, KKT conditions).
- **Convex vs non-convex**: [convex optimization](../convex-optimization/) guarantees a global optimum; deep learning is non-convex, so we can only find "good enough" solutions, which is why it needs so many engineering tricks.

## Relevance to time series forecasting

- Fitting ARIMA and training KUN (Kernel U-Net) both amount to solving an optimization problem: minimizing a forecasting loss (MSE, MAE, etc.).
- Ideas from constrained optimization appear in forecasting models with regularization or with monotonicity / non-negativity constraints.
- Hyperparameter search ([learning rate](../learning-rate/), window length, network depth) is itself an **outer optimization** problem, commonly solved by grid search or [Bayesian](../bayes-theorem/) optimization.

## Summary

- Optimization = optimizing an objective function under constraints; its three ingredients are the objective, the variables and the constraints.
- The necessary condition for an unconstrained optimum is a zero gradient.
- Convex problems are easy; non-convex ones (deep learning) rely on iterative methods plus tricks. "Training a model" is "solving an optimization problem".

[← Math foundations](../math/) · [Foundations overview](../)
