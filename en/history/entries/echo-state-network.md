---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2001–04 · Control / Communications"
permalink: /en/history/e/echo-state-network/
title: "Echo State Networks (Jaeger, 2001–04)"
lead: "Recurrent networks too hard to train? Then don't train them. Jaeger froze a pool of randomly connected neurons into a “reservoir”, learned only a linear readout layer, and still predicted chaos."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

Around 2000, recurrent neural networks (RNNs) could in theory approximate any dynamical system, but they were **extremely hard to train**: backpropagation through time ran into vanishing and exploding gradients, and convergence was slow and unstable. Meanwhile, the control and signal-processing communities had long relied on the dependable tools of **linear system identification**. Jaeger (who proposed the idea in 2001 and, with Haas, demonstrated chaotic prediction in *Science* in 2004) took a different route and introduced the **Echo State Network (ESN)**; at almost the same time Maass proposed the "liquid state machine", and the two are together known as **reservoir computing**.

### The problem

If the recurrent weights are hard to train, can we **sidestep them**? The key insight is that a sufficiently rich nonlinear dynamical system, once driven by an input signal, has an internal state that is itself a **high-dimensional nonlinear expansion** of the input history. We then only need to perform a **linear regression** on that expansion to read out the target, without adjusting the recurrent internals at all. The question becomes: what kind of recurrent system guarantees that "the readout is feasible" and that it is **stable**?

### Other currents of the time (and their limits)

- **RNNs trained with BPTT**: highly expressive and trainable end to end, but gradient problems made training slow and prone to divergence; at the time they struggled to forecast long-range chaos stably.
- **Linear system identification (ARMA / state space)**: robust estimation with theoretical guarantees, but fundamentally linear, unable to capture strongly nonlinear dynamics such as chaos.
- **Delay embedding + local models (Takens)**: can reconstruct the attractor, but requires careful choice of embedding dimension and neighbourhood, and is sensitive to noise and dimensionality.

### The method

An ESN consists of a fixed, randomly generated recurrent "**reservoir**" and a trainable **linear readout**. The reservoir state is updated as

$$ x_t = (1-a)\,x_{t-1} + a\,\tanh\!\big(W^{\text{in}} u_t + W\, x_{t-1}\big) $$

where $$ u_t $$ is the input, $$ x_t $$ is the high-dimensional reservoir state, $$ a\in(0,1] $$ is the leak rate, and $$ W^{\text{in}},W $$ are **generated at random and then frozen, never trained**. The output is simply a linear combination of the state:

$$ y_t = W^{\text{out}}\,[\,x_t;\,u_t\,] $$

Only $$ W^{\text{out}} $$ needs to be learned, and since the target is **linear** in it, it can be solved in closed form with a single **ridge regression** — fast to train, with no local minima. What makes this work is the **echo state property**: the reservoir's **dependence on its initial state fades over time**, so the state is uniquely determined by the recent input history. In practice this is ensured by scaling the **spectral radius** $$ \rho(W) $$ of the recurrent matrix to around 1:

$$ \rho(W) \lesssim 1 $$

A spectral radius close to 1 gives the longest "memory" without losing stability (for chaotic tasks it is sometimes set slightly above 1).

### Results

The landmark result of 2004: an ESN predicted the Mackey–Glass chaotic series with an accuracy **several orders of magnitude** better than the methods of the time, and it could learn a wide range of nonlinear dynamical systems. Because only the linear readout is trained, it is **extremely fast to train and simple to implement**, and the reservoir can even be realized physically in hardware (photonics, memristors), giving rise to very low-power "physical reservoir computing". Its limits: performance is sensitive to hyperparameters such as the random seed, the spectral radius and the reservoir size, and its memory length is bounded.

### Significance and outlook

The ESN offers a deep and economical paradigm: **complexity can come from fixed random dynamics, and learning need only happen in the last layer**. It turned chaotic prediction (see [Lorenz](../lorenz-chaos/) on deterministic chaos) from a "hard to train" problem into a "random expansion + linear regression" problem, in the same spirit as kernel methods and random features. Today reservoir computing remains an active direction for low-power time-series processing on edge devices and for neuromorphic computing, and it keeps prompting the question: how many of the parameters in a deep network really "have to be trained"?
