---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/autodiff/
title: "Automatic Differentiation"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Automatic differentiation (autodiff)** is the technique that frameworks (PyTorch, TensorFlow, JAX) use to compute the derivatives of any computational graph automatically and **exactly**. You only write the forward computation, and the framework computes the [gradient](../gradient/) — you never have to derive derivatives by hand again. [Backpropagation](../backpropagation/) is simply a special case of it applied to [neural networks](../neural-network/).

## Intuition

Any complex computation is, in the end, assembled from a pile of **elementary operations** (addition, multiplication, exponentials, matrix multiplication…). And we have long known the derivative of each elementary operation ($\frac{d}{dx}e^x = e^x$, the product rule for multiplication…).

The core idea of automatic differentiation is simple: **since the derivative of every small building block is known, just assemble them mechanically with the [chain rule](../chain-rule/)**, and the derivative of the whole graph follows naturally. While you run the forward computation, the framework quietly records every operation into a **computational graph**; to get the gradient, it simply walks back through this graph once.

It differs from the two other ways of computing derivatives:

- **Numerical differentiation**: approximate with $\frac{f(x+h)-f(x)}{h}$ — it has **rounding errors**, and it must be recomputed once per parameter, far too slow for millions of parameters.
- **Symbolic differentiation**: derive a formula for the derivative as in a math class — the expressions **blow up explosively**.
- **Automatic differentiation**: exact to machine precision, with controlled complexity. That is why it wins.

## How it works: two modes

Automatic differentiation can proceed in two directions:

**Forward mode**: moves forward along the computational graph, carrying derivative information along. Suited to "few inputs, many outputs".

**Reverse mode**: first computes a forward pass and records the graph, then propagates derivatives **backward from the output**. Suited to "many inputs, few outputs" — and [deep learning](../dl/) is exactly "millions of parameter inputs, one scalar loss output", so frameworks all use reverse mode. **Backpropagation is reverse-mode automatic differentiation.**

The core of reverse mode is still the chain rule. For every intermediate variable $v$ in the computational graph, the framework maintains an adjoint

$$
\bar{v} = \frac{\partial \mathcal{L}}{\partial v}
$$

and propagates it in reverse topological order: if $v$ influences $u_1, u_2, \dots$, then

$$
\bar{v} = \sum_{i} \bar{u}_i \, \frac{\partial u_i}{\partial v}
$$

Notation: $\mathcal{L}$ is the final scalar output (the loss); $\bar v$ means "if $v$ changes a little, how much does $\mathcal{L}$ change"; $\frac{\partial u_i}{\partial v}$ is the **local derivative** of a single elementary operation (known). A single backward sweep fills in every $\bar v$.

{% include fviz/backprop-graph.html %}

## A concrete example

Find the derivative of $f(x) = x^2 \cdot \sin(x)$ at $x=2$. By hand, $f'(x) = 2x\sin x + x^2\cos x$; substituting $x=2$: $4\sin2 + 4\cos2 \approx 4(0.909) + 4(-0.416) \approx 1.97$.

With PyTorch's automatic differentiation:

```python
import torch
x = torch.tensor(2.0, requires_grad=True)   # mark x for gradient tracking
y = x**2 * torch.sin(x)                       # forward: the framework builds the graph at the same time
y.backward()                                  # backward: automatic differentiation
print(x.grad)                                 # tensor(1.9726) — matches the hand calculation
```

We **wrote no derivative formula at all**; the framework assembled the result automatically from the local derivatives of the three elementary operations `pow`, `sin` and `mul`. That is the power of autodiff.

## Why it matters / where it is used

- **It is the engine of deep learning frameworks.** Define any network, however complex (loops, branches, attention…), and you get gradients automatically, with no hand derivation.
- **It supports dynamic structures.** Graphs that change with the input length, as in an [RNN](../rnn/), are handled just as well.
- It frees researchers: when inventing new layers or new [loss functions](../loss-function/), **you need not worry about how to differentiate them** — which has greatly accelerated model innovation.
- The computed gradients are then handed to an [optimizer](../optimizer/) (such as [Adam](../adam/)) to update the parameters.

## Common misconceptions

- **"Autodiff = numerical differentiation"** — no. Autodiff is **exact** (to machine precision); numerical differentiation is an approximation.
- **"Autodiff = symbolic differentiation"** — no. It does not generate huge derivative formulas; it propagates derivatives numerically along the graph.
- **"Backpropagation and autodiff are two different things"** — backpropagation is the concrete application of autodiff (reverse mode) to neural networks; the two share the same lineage.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
