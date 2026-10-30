---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/learning-rate/
title: "Learning Rate"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

The **learning rate ($\eta$)** is the **step size** of each step of [gradient descent](../gradient-descent/). It decides "how far to go in one step along the gradient direction". Too large, and training oscillates or even diverges; too small, and training crawls along at a snail's pace — it is the **most critical hyperparameter in deep learning, and the one to tune first**.

## Intuition

Back to "walking down a mountain blindfolded". [Backpropagation](../backpropagation/) tells you the steepest downhill direction under your feet; the learning rate decides **how big each stride is**:

- **Strides too large**: you might step right over the bottom of the valley onto the opposite slope, then step back again… **oscillating** back and forth, or even climbing higher and higher (**divergence**).
- **Strides too small**: the direction is right, but progress is extremely slow; training takes a long time and may get stuck in a small dip.
- **Strides just right**: you reach the bottom of the valley steadily and fairly quickly.

So the learning rate is neither "the bigger the faster" nor "the smaller the better"; you need to find an **appropriate sweet spot**.

## How it enters the update formula

The general form of a parameter update:

$$
\theta_{t+1} = \theta_t - \eta\, g_t
$$

- $\theta_t$: the current parameters; $g_t$: the gradient computed by [backpropagation](../backpropagation/); $\eta$: the learning rate.
- $\eta$ directly **scales** the size of each move. Double $\eta$, and the step doubles.

A simple example shows its effect on convergence. To minimize $\mathcal{L}=\theta^2$ (gradient $g=2\theta$), the update becomes $\theta_{t+1} = \theta_t(1 - 2\eta)$:

- $\eta=0.1$: factor $0.8$, **smooth convergence** to 0.
- $\eta=0.5$: factor $0$, **straight there in one step** (ideal, but real loss surfaces are never this convenient).
- $\eta=1.0$: factor $-1$, **oscillates forever** between $+1$ and $-1$.
- $\eta=1.5$: factor $-2$, $|\theta|$ keeps growing — **divergence**!

{% include fviz/optimizer.html %}

## Learning rate schedules

A fixed learning rate is often not optimal. The common approach is **large first, then small**:

- **Warmup**: at the start of training, increase $\eta$ linearly from a very small value up to the target, so the model is not thrown off course by huge gradients right away.
- **Decay**: late in training, gradually reduce $\eta$ so the parameters can be **finely tuned** near the bottom of the valley. Common choices are step decay and cosine annealing.

A typical curve: warm up first, then descend gently along a cosine curve.

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
# Cosine annealing: lr goes from 1e-3 down to nearly 0 along a cosine curve
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=100)
for epoch in range(100):
    train_one_epoch(...)
    opt.step()
    sched.step()                 # update the learning rate once per epoch
    print(sched.get_last_lr())
```

{% include fviz/lr-schedule.html %}

## How to choose a learning rate

- Common starting points: **$10^{-3}$ for Adam**, $10^{-1}\sim10^{-2}$ for SGD.
- **Sweep by factors of 10**: try $10^{-2}, 10^{-3}, 10^{-4}$ and see which makes the loss drop fastest without oscillating.
- Diagnose from the loss curve: **wild up-and-down oscillation / NaN → decrease it**; **very slow, flat descent → increase it**.

## What it means for time series forecasting

When training models like [Kernel U-Net (KUN)](../../kun/) on **long lookback windows**, the learning rate is especially sensitive: the longer the sequence, the more the scale of the gradients fluctuates, and a learning rate that is too large more easily triggers [exploding gradients](../vanishing-exploding-gradient/) that turn the loss into NaN. In practice it is usually combined with [Adam](../adam/) + a moderate learning rate + warmup + cosine decay, and when gradients explode, **the first thing to do is lower the learning rate**. This is the first trick for training KUN stably.

## Summary

- Learning rate $\eta$ = the **step size** of gradient descent, appearing in $\theta_{t+1}=\theta_t-\eta g_t$.
- **Too large oscillates/diverges, too small is too slow**; find the sweet spot.
- In practice: start by trying orders of magnitude, combined with a **warmup + decay** schedule; it is the hyperparameter to tune first.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
