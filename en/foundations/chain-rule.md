---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/chain-rule/
title: "The Chain Rule"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

The chain rule is the rule for differentiating **composite functions** (functions nested inside functions): the overall rate of change = the rate of change of the outer layer × the rate of change of the inner layer. It is the mathematical engine of **[backpropagation](../backpropagation/)** in [neural networks](../neural-network/).

## Intuition

Imagine a gear train: gear A drives gear B, and gear B drives gear C.

- When A turns once, B turns 3 times (B's "gear ratio" relative to A is 3);
- when B turns once, C turns 2 times (C's ratio relative to B is 2);
- so when A turns once, C turns **3 × 2 = 6** times.

Ratios (rates of change) propagate by **multiplication**. That is exactly what the chain rule says: when $x$ affects $u$ and $u$ in turn affects $y$, the total effect of $x$ on $y$ is the product of the two effects.

{% include fviz/chain-rule.html %}

## Mathematical formulation

Let $y=f(u)$ and $u=g(x)$, i.e. $y=f(g(x))$. Then

$$
\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\cdot g'(x)
$$

- $\dfrac{dy}{du}$ is the derivative of the **outer** function (evaluated at the value of the inner one);
- $\dfrac{du}{dx}$ is the derivative of the **inner** function;
- multiplying them gives the overall derivative.

With more levels of nesting, keep multiplying: if $y=f(g(h(x)))$, then

$$
\frac{dy}{dx}=f'\cdot g'\cdot h'
$$

The multivariable version (the form neural networks actually use) replaces the product with a **sum over all paths**:

$$
\frac{\partial L}{\partial x}=\sum_i \frac{\partial L}{\partial u_i}\frac{\partial u_i}{\partial x}
$$

## A concrete example

Find the derivative of $y=(3x+1)^2$.

Let the inner function be $u=3x+1$ and the outer one $y=u^2$.

$$
\frac{dy}{du}=2u,\qquad \frac{du}{dx}=3
$$

$$
\frac{dy}{dx}=2u\cdot 3=2(3x+1)\cdot 3=18x+6
$$

Check: expanding gives $y=9x^2+6x+1$, and differentiating directly gives $18x+6$ — the same result.

```python
import sympy as sp
x = sp.symbols('x')
y = (3*x + 1)**2
print(sp.diff(y, x))   # 18*x + 6
```

## Why it matters / where it is used

The chain rule is the whole secret of **backpropagation**. A neural network is just a long chain of composite functions:

$$
L\big(f_n(\cdots f_2(f_1(x))\cdots)\big)
$$

To find out how an early parameter affects the final loss $L$, you **multiply together** the local derivatives of every layer along the path from that parameter to $L$. Frameworks (PyTorch, TensorFlow) do this for you automatically with autograd, but what they do is the chain rule.

It also explains **[vanishing / exploding gradients](../vanishing-exploding-gradient/)**: multiplying many derivatives smaller than 1 tends to 0 (vanishing), and multiplying many larger than 1 blows up (exploding) — a direct side effect of the repeated product.

## Relevance to time series forecasting

- KUN (Kernel U-Net) has a multi-layer structure with an encoder, kernel operations and a decoder; during training, the [gradient](../gradient/) of the loss with respect to the lowest-level parameters is propagated back layer by layer by the chain rule.
- A sequence model ([RNN](../rnn/)) unrolled over time steps is an extremely deep composite function; "backpropagation through time (BPTT)" is essentially the chain rule's repeated product along the time axis — and that is precisely why long sequences are hard to train.

## Summary

- Differentiating a composite function = **multiplying** the local derivatives of each layer (and adding over multiple paths).
- It is the mathematical basis of backpropagation, which makes deep networks trainable.
- The repeated product brings efficiency, but also the hazard of vanishing / exploding gradients.

[← Math foundations](../math/) · [Foundations overview](../)
