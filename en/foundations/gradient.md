---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/gradient/
title: "Gradient"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

The gradient of a multivariable function is the **vector of its partial derivatives** with respect to each variable. It points in the direction in which the function **increases fastest**, and its length tells you how steep that ascent is. In [optimization](../optimization/), stepping in the opposite direction makes the function decrease.

## Intuition

For a function of one variable, the "derivative" is a single number (the slope). But a model has thousands upon thousands of parameters, so the function is **multivariable** — and then the "slope" is no longer a number but a **vector** that tells you "which way to go to climb fastest".

Imagine standing on a mountain. The gradient is like an arrow: it **points up the steepest slope**, and **the longer the arrow, the steeper the slope**. To go downhill, walk in the opposite direction of the arrow. Once you stand at the bottom of a valley (a minimum), nothing rises in any direction and the arrow shrinks to length 0 — this is what "the gradient is zero" means.

## Mathematical formulation

For $f(x_1,x_2,\dots,x_n)$, the gradient is the vector formed by its **partial derivatives**:

$$
\nabla f=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\dots,\frac{\partial f}{\partial x_n}\right)
$$

- $\dfrac{\partial f}{\partial x_i}$ — **partial derivative**: the rate of change of the function when only $x_i$ varies and all other variables are held fixed;
- $\nabla$ (nabla) — the gradient operator;
- the **direction** of the gradient is the direction of fastest increase, and its **magnitude** $\lVert\nabla f\rVert$ is the maximum rate of change along that direction.

A key property: the gradient is **perpendicular to the level curves** (level surfaces). Walking along a level curve leaves the function value unchanged, while the gradient points in the direction of fastest change, so the two are naturally orthogonal.

## A concrete example

Let $f(x,y)=x^2+3y^2$. Taking the partial derivatives with respect to $x$ and $y$:

$$
\frac{\partial f}{\partial x}=2x,\qquad \frac{\partial f}{\partial y}=6y
$$

$$
\nabla f=(2x,\ 6y)
$$

At the point $(1,1)$, $\nabla f=(2,6)$: at this point the $y$ direction is much steeper than the $x$ direction (because $y$ has the larger coefficient). To descend, move in the direction $(-2,-6)$. At the optimum $(0,0)$, the gradient is $(0,0)$.

```python
import numpy as np
def grad(x, y):
    return np.array([2*x, 6*y])
print(grad(1, 1))   # [2 6]  direction of fastest ascent
print(grad(0, 0))   # [0 0]  optimum, gradient is zero
```

## Why it matters / where it is used

- **The steering wheel of optimization**: [gradient descent](../gradient-descent/) uses $-\nabla L$ to decide where each step goes.
- **[Backpropagation](../backpropagation/)**: uses the [chain rule](../chain-rule/) to efficiently compute the gradient of the [loss](../loss-function/) with respect to every parameter.
- **Geometric insight**: the gradient is perpendicular to the level curves, which explains why gradient descent "zigzags" in a long, narrow valley.

## What it means for time series forecasting

- When training KUN (Kernel U-Net), the framework automatically computes the gradient of the loss with respect to each weight and hands it to the [optimizer](../optimizer/) for the update — the gradient is the precise instruction for "how the model should improve".
- In deep networks on long sequences, gradients can **vanish or explode** during backpropagation (the result of multiplying many derivatives together); residual connections, normalization and gradient clipping all exist to keep the gradient flowing healthily.

## Common pitfalls

- The gradient is a **vector**, with both direction and magnitude; do not confuse it with the derivative of a one-variable function (a scalar).
- The gradient points in the direction of fastest **ascent**; to descend, take the **negative** gradient.
- A zero gradient only indicates a "stationary point", which may be a minimum, a maximum or a saddle point; second-order information is needed to tell which.

[← Math foundations](../math/) · [Foundations overview](../)
