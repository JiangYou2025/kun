---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/convex-optimization/
title: "Convex Optimization"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Convex optimization studies optimization problems whose objective function is "bowl-shaped" (a convex function). Its most beautiful property is that **every local optimum is necessarily a global optimum**, so solving is stable, reliable and backed by theoretical guarantees.

## Intuition

Think of the objective function as a landscape:

- A **convex function** is like a large smooth bowl: wherever you drop a small ball, it rolls down to **the same lowest point**.
- A **non-convex function** is like a rugged valley full of small pits (local optima): the ball may get stuck in one of them, unable to get out and unable to find the true bottom of the valley.

Convex optimization is loved precisely because "there are no traps" — you never have to worry about getting stuck in a suboptimal solution.

{% include fviz/convex-landscape.html %}

## Mathematical formulation

**Convex set**: the segment between any two points of the set stays inside the set.

**Convex function**: its domain is a convex set, and for any two points $x_1,x_2$ and any $\lambda\in[0,1]$,

$$
f(\lambda x_1+(1-\lambda)x_2)\le \lambda f(x_1)+(1-\lambda)f(x_2)
$$

Intuitively: **the graph of the function always lies below any of its secant lines**.

If $f$ is twice differentiable, the criterion is simpler:

- in one dimension: $f''(x)\ge 0$ everywhere;
- in several dimensions: the **Hessian matrix** $\nabla^2 f$ is **positive semidefinite** everywhere.

The standard form of a convex optimization problem:

$$
\min_{x}\ f(x)\quad \text{s.t.}\quad g_i(x)\le 0,\ h_j(x)=0
$$

where the objective $f$ and the inequality constraints $g_i$ are all convex functions, and the equality constraints $h_j$ are affine (linear) functions.

## A concrete example

Least squares: $f(x)=(x-2)^2+1$. Its second derivative $f''(x)=2>0$ is positive everywhere, so it is convex. Setting the first derivative to zero:

$$
f'(x)=2(x-2)=0\ \Rightarrow\ x=2
$$

$x=2$ is a local optimum and is also guaranteed to be the **global optimum**, with $f(2)=1$.

```python
import numpy as np
xs = np.linspace(-1, 5, 7)
f  = (xs - 2)**2 + 1
print(list(zip(xs, f)))   # bowl-shaped everywhere, lowest point at x=2
```

By contrast, a function with two valleys such as $f(x)=x^4-3x^2$ is non-convex, and [gradient descent](../gradient-descent/) started from different points may end up in different valleys.

## Why it matters / where it is used

- The objective functions of **linear regression, ridge regression, logistic regression and [SVMs](../svm/)** are all convex, so they have a unique optimum and are reproducible.
- Adding an $\ell_1/\ell_2$ [regularization term](../norm/) (a convex function) keeps the whole problem convex, which is one reason [regularization](../regularization/) works so well.
- Convexity gives **convergence guarantees**: convex + a suitable step size, and gradient descent is guaranteed to converge to the global optimum.

## Relevance to time series forecasting

- Classical models (parts of ARIMA estimation, linear autoregression) fall within convex optimization, so their solutions are stable and interpretable.
- The [loss](../loss-function/) of deep models such as KUN (Kernel U-Net) is **non-convex**, with no guarantee of a global optimum, so in practice we rely on tricks such as good initialization, [Adam](../adam/), [learning rate](../learning-rate/) schedules and [batch normalization](../batchnorm/) to "steer around bad local solutions". Understanding convex vs. non-convex helps you see why training deep models takes so many tricks.

## Summary

- Convex function = bowl-shaped; every local optimum is the global optimum.
- Criterion: $f''\ge 0$ / positive semidefinite Hessian.
- Classical ML is mostly convex (worry-free); deep learning is mostly non-convex (needs tricks).

[← Math foundations](../math/) · [Foundations overview](../)
