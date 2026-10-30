---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/adam/
title: "Adam"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Adam (Adaptive Moment Estimation)** is the most widely used [optimizer](../optimizer/) today. It simultaneously tracks the gradient's **first moment** (momentum, the direction) and **second moment** (the history of gradient magnitudes), and thereby **adapts the step size for each parameter individually** — training is both fast and stable, and it has become almost the default choice in [deep learning](../dl/).

## Intuition

Recall the "descending a mountain blindfolded" picture from the [optimizer](../optimizer/) page:

- **Momentum** makes you like a ball rolling downhill, carrying inertia over small dips — this is Adam's first ingredient.
- **Adaptive step size**: automatically take smaller steps in directions that are persistently steep (so you don't overshoot), and larger steps in flat, sparsely updated directions (so you don't dawdle) — this is Adam's second ingredient.

Adam **merges the two into one**: it remembers the average direction of the gradient, and also the average "intensity" of each parameter's gradient, and then uses the latter to normalize the former. The result: it works reliably across all kinds of networks with hardly any tuning effort.

## Mathematical formulation: the full update rule

Let $g_t$ be the gradient at step $t$ (computed by [backpropagation](../backpropagation/)). Adam maintains two moving averages:

**First moment (momentum)**:
$$
m_t = \beta_1 m_{t-1} + (1-\beta_1)\, g_t
$$

**Second moment (squared gradient)**:
$$
v_t = \beta_2 v_{t-1} + (1-\beta_2)\, g_t^2
$$

Because $m_0 = v_0 = 0$, both estimates are **biased toward 0** early on, so a **bias correction** is applied:
$$
\hat{m}_t = \frac{m_t}{1-\beta_1^{\,t}},\qquad
\hat{v}_t = \frac{v_t}{1-\beta_2^{\,t}}
$$

**Final parameter update**:
$$
\theta_{t+1} = \theta_t - \eta\,\frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

Symbol by symbol:

- $g_t$: the current gradient; $g_t^2$ is the **element-wise** square.
- $m_t$: exponential moving average of the gradient (**direction/momentum**).
- $v_t$: exponential moving average of the squared gradient (**how large each parameter's gradient is**).
- $\beta_1$: momentum decay rate, **default 0.9**.
- $\beta_2$: second-moment decay rate, **default 0.999**.
- $\beta_1^{\,t}, \beta_2^{\,t}$: $\beta$ **raised to the power $t$** (used for bias correction); they tend to 0 as $t$ grows, so the correction gradually fades away.
- $\hat m_t, \hat v_t$: the bias-corrected estimates.
- $\eta$: the [learning rate](../learning-rate/), **default 0.001**.
- $\epsilon$: a small constant preventing division by zero, **default $10^{-8}$**.

Intuition: $\dfrac{\hat m_t}{\sqrt{\hat v_t}}$ **automatically normalizes** each parameter's effective step size — in directions where the gradient has been large for a long time, the denominator is large and the step is shrunk; and vice versa.

{% include fviz/optimizer.html %}

## A concrete example

For a single parameter, first step: $g_1 = 0.1$, $\beta_1=0.9,\beta_2=0.999,\eta=0.001,\epsilon=10^{-8}$.

$$
m_1 = 0.9\times0 + 0.1\times0.1 = 0.01
$$
$$
v_1 = 0.999\times0 + 0.001\times0.01 = 0.00001
$$

Bias correction ($t=1$):
$$
\hat m_1 = \frac{0.01}{1-0.9} = 0.1,\qquad
\hat v_1 = \frac{0.00001}{1-0.999} = 0.01
$$

Update:
$$
\Delta\theta = -\,0.001\times\frac{0.1}{\sqrt{0.01}+10^{-8}}
= -0.001\times\frac{0.1}{0.1} = -0.001
$$

Note: after bias correction, the effective step size of the first step is approximately equal to the learning rate $\eta=0.001$ — this is precisely the purpose of the correction; otherwise the first step would be thrown off by the too-small $m$ and $v$.

```python
import torch
theta = torch.tensor([1.0], requires_grad=True)
opt = torch.optim.Adam([theta], lr=1e-3, betas=(0.9, 0.999), eps=1e-8)
for _ in range(3):
    opt.zero_grad()
    loss = (theta - 0.0)**2          # goal: pull theta toward 0
    loss.backward()
    opt.step()
    print(round(theta.item(), 6))
```

## Why it matters / where it is used

- **The default first-choice optimizer**: not very sensitive to the learning rate, converges fast, and works almost out of the box. A beginner training any network can hardly go wrong starting with Adam + `lr=1e-3`.
- It performs robustly on almost every architecture: [Transformers](../transformer/), [RNNs](../rnn/)/[LSTMs](../lstm/), [CNNs](../cnn/), and more.
- The common variant **AdamW** decouples weight decay from the gradient update, giving better regularization; it is the mainstream choice for training today's large models.

## Relevance to time series forecasting

When training multi-scale forecasting models like [Kernel U-Net (KUN)](../../kun/), a long lookback window makes the gradient scales of different parameters vary enormously; Adam's **per-parameter adaptive step size** smooths out exactly this disparity automatically, sparing you the trouble of hand-tuning a step size for each layer. In practice, `Adam(lr=1e-3 or 1e-4)` is a common robust starting point for training KUN; if the loss oscillates, lower the [learning rate](../learning-rate/) first rather than switching optimizers.

## Summary

- Adam = **momentum (first moment) + adaptive step size (second moment) + bias correction**.
- Key formula: $\theta_{t+1} = \theta_t - \eta\,\dfrac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}$.
- Default hyperparameters $\beta_1=0.9,\ \beta_2=0.999,\ \epsilon=10^{-8}$; you still need to tune the learning rate yourself.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
