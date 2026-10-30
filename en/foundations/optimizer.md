---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/optimizer/
title: "Optimizers"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

An **optimizer** is the [algorithm](../algorithms/) that takes the gradients computed by [backpropagation](../backpropagation/) and **actually updates the network's parameters**. Once you "know which way to go", it decides **how exactly to take the step** — how big the step is, whether to take past directions into account, and whether each parameter gets its own step size. The most common ones are SGD, Momentum and [Adam](../adam/).

## Intuition

Picture training as **walking down into a valley blindfolded** to find the lowest point (the minimum of the [loss](../loss-function/)). Backpropagation tells you the **steepest downhill direction** under your feet (the negative gradient). But knowing the direction is not enough; you still have to decide:

- How big a step to take? (That is the [learning rate](../learning-rate/).)
- Should you **carry some inertia**, like a ball rolling downhill, so you roll over small dips? (Momentum.)
- Should you move more along gentle directions and less along steep ones? (Adaptive step sizes.)

Different optimizers are just different combinations of these strategies. **Optimizer = the rule that turns gradients into parameter updates.**

## How it works: from the plainest to adaptive

**Plain [gradient descent](../gradient-descent/) (SGD)**:

$$
\theta_{t+1} = \theta_t - \eta\, g_t
$$

- $\theta_t$: the parameters at step $t$; $g_t = \nabla_\theta \mathcal{L}$ is the current gradient; $\eta$ is the [learning rate](../learning-rate/) (step size).
- Meaning: move a distance $\eta$ along the negative gradient. Simple, but it tends to zigzag back and forth in long narrow valleys and converge slowly.

**Adding momentum**: accumulate a "velocity" so that updates carry inertia:

$$
v_t = \beta v_{t-1} + g_t,\qquad
\theta_{t+1} = \theta_t - \eta\, v_t
$$

- $v_t$: the velocity (an exponential moving average of the gradients); $\beta$ (e.g. 0.9) controls how much history is kept.
- Effect: it **speeds up** along consistent directions and **cancels out** along oscillating ones, making progress smoother and faster.

**Adaptive step sizes (e.g. Adam)**: additionally scale the step separately for each parameter — parameters whose gradients are consistently large get small steps, sparsely updated parameters get large steps. That is what [Adam](../adam/) does: it combines momentum with per-parameter adaptation.

{% include fviz/optimizer.html %}

## A concrete example

Minimize $\mathcal{L}(\theta) = \theta^2$ (optimum $\theta=0$, gradient $g=2\theta$). Start from $\theta_0 = 1$ with $\eta=0.1$ and use SGD:

$$
\theta_1 = 1 - 0.1\times(2\times1) = 0.8
$$
$$
\theta_2 = 0.8 - 0.1\times(2\times0.8) = 0.64
$$
$$
\theta_3 = 0.64 - 0.1\times(2\times0.64) = 0.512
$$

Each step multiplies by 0.8, converging steadily towards 0.

```python
import torch
theta = torch.tensor([1.0], requires_grad=True)
opt = torch.optim.SGD([theta], lr=0.1)        # swap in torch.optim.Adam to use Adam
for step in range(3):
    opt.zero_grad()
    loss = theta**2
    loss.backward()                            # backpropagation computes the gradient
    opt.step()                                 # the optimizer updates the parameters
    print(round(theta.item(), 3))             # 0.8, 0.64, 0.512
```

Note the division of labour: `loss.backward()` ([backpropagation](../backpropagation/) / [automatic differentiation](../autodiff/)) **only computes gradients**; `opt.step()` (the optimizer) is **what updates the parameters**.

## Why it matters / where it is used

- The optimizer **directly determines whether training converges, how fast, and how accurate the final model is**. The same network with a different optimizer can give wildly different results.
- After the [learning rate](../learning-rate/), it is the most important training knob. In practice **[Adam](../adam/) is the default first choice**, hassle-free and robust; those chasing the very best generalization sometimes switch to SGD+Momentum and tune it patiently.

## Relevance to time series forecasting

When training a forecasting model such as [Kernel U-Net (KUN)](../../kun/), long look-back windows and multi-scale structure make the loss landscape more complex and the gradient scales more uneven. This is where **the per-parameter step sizes of an adaptive optimizer (Adam)** are especially useful — they automatically balance parameters of different scales and, combined with a sensible [learning rate](../learning-rate/), let KUN converge quickly and stably.

## Summary

- Optimizer = **the rule that turns gradients into parameter updates**; the gradients are supplied by backpropagation.
- The line of evolution: SGD → + momentum (inertia) → + adaptive step sizes (Adam).
- It works hand in hand with the [learning rate](../learning-rate/): the optimizer decides "how to move", the learning rate decides "how far".

[← Deep learning foundations](../dl/) · [Foundations overview](../)
