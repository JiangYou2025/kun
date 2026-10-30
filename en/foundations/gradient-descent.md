---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/gradient-descent/
title: "Gradient Descent"
no_comments: true
math: true
---

> Part of [Math Fundamentals](../math/) · [Foundations overview](../)

Gradient descent is an iterative [optimization](../optimization/) [algorithm](../algorithms/): at each step it takes a small step in the **opposite direction** of the [gradient](../gradient/) of the [loss function](../loss-function/), gradually approaching the minimum. Almost every modern model is trained with it.

## Intuition

Imagine standing on a hillside in thick fog. You can't see the whole mountain; you just want to reach the valley floor as quickly as possible. All you can sense is **which direction is steepest under your feet**. The strategy is simple:

1. Feel out the steepest downhill direction under your feet (the negative gradient direction);
2. Take a step that way;
3. Repeat until everything around you is flat (the gradient is close to 0).

The size of each step is the **[learning rate](../learning-rate/)**. Steps too small, and the descent is maddeningly slow; steps too large, and you may overshoot the valley floor in one stride, bouncing back and forth between the two sides or even climbing higher and higher.

## Mathematical formulation

The update rule:

$$
\theta \leftarrow \theta - \eta\,\nabla L(\theta)
$$

- $\theta$ — the model parameters (possibly a vector with millions of dimensions);
- $L(\theta)$ — the loss function, measuring how bad the current parameters are;
- $\nabla L(\theta)$ — the [gradient](../gradient/) of the loss with respect to the parameters, pointing in the direction of **steepest ascent**, hence the minus sign in front;
- $\eta$ — the **learning rate**, controlling how far each step goes.

Three common variants, differing in "how much data is used to estimate the gradient at each step":

- **[Batch](../batch/) GD**: uses all the data; the gradient is accurate but slow.
- **Stochastic (SGD)**: uses a single sample each time; fast but very noisy.
- **Mini-batch**: uses a small batch each time (e.g. 32 or 64); this is the standard practice in deep learning, balancing speed and stability.

In practice, improved versions with momentum (Momentum, [Adam](../adam/), etc.) are widely used to speed up convergence and dampen oscillation.

## A concrete example

Minimize $L(\theta)=\theta^2$, whose gradient is $\nabla L=2\theta$. Take learning rate $\eta=0.1$ and start from $\theta_0=5$:

$$
\theta_1=5-0.1\cdot 10=4.0,\quad \theta_2=4-0.1\cdot 8=3.2,\quad \theta_3=3.2-0.1\cdot 6.4=2.56,\ \dots
$$

Step by step, the parameter approaches the optimum 0.

```python
theta, lr = 5.0, 0.1
for step in range(20):
    grad = 2 * theta          # gradient of L = theta^2
    theta -= lr * grad
    print(step, round(theta, 4))
# theta gradually approaches 0
```

Try changing $\eta$ to $1.1$: you will see $\theta$ not converge but **diverge** — that is what a learning rate that is too large does.

## Why it matters / where it is used

- **The universal engine of training**: from linear regression to large neural networks, parameter learning is almost always gradient descent (or one of its variants).
- Combined with **[backpropagation](../backpropagation/)** (the [chain rule](../chain-rule/)), the gradients are computed efficiently and then applied with this rule.
- On [convex optimization](../convex-optimization/) problems it converges to the global optimum; on non-convex problems (deep learning) it converges to a "good enough" local solution.

## Why it matters for time series forecasting

- All the learnable parameters of KUN (Kernel U-Net) are trained by running mini-batch gradient descent + Adam on a forecasting loss (such as MSE).
- Techniques such as learning-rate schedules (warmup, cosine decay) and gradient clipping exist precisely to make gradient descent converge stably on long sequences and deep networks.
- Understanding the "step size vs convergence" trade-off helps you diagnose common problems such as training that won't converge, or a loss that oscillates or explodes.

## Common pitfalls

- **The learning rate is the number-one hyperparameter**: too large and training diverges, too small and it stalls — it needs tuning.
- A zero gradient is not necessarily the lowest point (it may be a saddle point or a local minimum); watch out for this especially in non-convex problems.
- Always **normalize your features**: features on wildly different scales turn the loss surface into a long, narrow valley, making descent extremely inefficient.

[← Math Fundamentals](../math/) · [Foundations overview](../)
