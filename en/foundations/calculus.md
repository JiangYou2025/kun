---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/calculus/
title: "Calculus"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Calculus is the mathematics of "**change**" and "**accumulation**": the derivative describes how fast a quantity changes, and the integral adds up countless tiny changes. It is the groundwork for understanding [gradients](../gradient/), [optimization](../optimization/) and model training.

## Intuition

Draw a mountain road as a function $y=f(x)$, where $x$ is the horizontal position and $y$ is the altitude.

- The **derivative** answers: "How steep is the road at this point?" A steep uphill has a large positive derivative, a downhill a negative one, and flat ground zero.
- The **integral** answers: "Going from the start to the end, how much has the altitude changed in total?" It adds up the areas of countless thin strips under the curve.

The two pillars of calculus — derivatives and integrals — are in fact a pair of **inverse** operations; this is the fundamental theorem of calculus.

{% include fviz/derivative.html %}

## Mathematical formulation

The **limit** is where everything starts; it expresses "getting arbitrarily close":

$$
\lim_{x\to a} f(x)=L
$$

The **derivative** is defined as the limit of the slope of a secant line as the interval shrinks to 0:

$$
f'(x)=\frac{df}{dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$

- $h$ is a tiny step;
- the numerator is the change in the function value, the denominator the change in the input;
- the ratio is the "rate of change", and taking the limit gives the **instantaneous slope** at that point.

A few differentiation rules you must remember:

$$
(x^n)'=n x^{n-1},\quad (e^x)'=e^x,\quad (\ln x)'=\frac1x
$$

The **integral** is the inverse of the derivative; the definite integral equals the area under the curve:

$$
\int_a^b f(x)\,dx
$$

The **fundamental theorem of calculus** connects the two: if $F'(x)=f(x)$, then $\int_a^b f(x)\,dx=F(b)-F(a)$.

## A concrete example

Let $f(x)=x^2$ and find its derivative at $x=3$.

By the rule, $f'(x)=2x$, so $f'(3)=6$. Let's check it against the definition with $h=0.001$:

$$
\frac{f(3.001)-f(3)}{0.001}=\frac{9.006001-9}{0.001}=6.001\approx 6
$$

```python
f  = lambda x: x**2
h  = 1e-5
x  = 3
print((f(x+h) - f(x)) / h)   # ≈ 6.00001, a numerical approximation of the derivative
```

This idea of "approximating the derivative with a tiny step" is exactly the principle behind **numerical gradient checking** in deep learning.

## Why it matters / where it is used

- **Training = differentiate + take a step**: differentiating the [loss function](../loss-function/) with respect to the parameters gives the [gradient](../gradient/), which [gradient descent](../gradient-descent/) then uses to update the parameters.
- **[Backpropagation](../backpropagation/)**: a [neural network](../neural-network/) is differentiated layer by layer, relying on the [chain rule](../chain-rule/) — which is itself the rule for differentiating composite functions.
- **Probability and integrals**: expectations and probabilities of continuous [random variables](../random-variable/) are defined with integrals, which links calculus to [probability and statistics](../probability-statistics/).

## Relevance to time series forecasting

- How fast a time series' trend rises or falls is precisely the derivative of the series with respect to time (differencing is its discrete version).
- When training models such as KUN (Kernel U-Net), every step differentiates the loss function; without calculus there is no learning.
- "Accumulating" errors over a period of time (e.g. cumulative absolute error) is a discrete application of the idea of integration.

## Summary

- Derivative = instantaneous rate of change = slope; integral = accumulation = area.
- The two are inverses of each other (the fundamental theorem of calculus).
- Calculus is the mathematical foundation of gradients, the chain rule, optimization and, indeed, all of deep learning training.

[← Math foundations](../math/) · [Foundations overview](../)
