---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1963 · Physics"
permalink: /en/history/e/lorenz-chaos/
title: "Deterministic Chaos and the Butterfly Effect (Lorenz, 1963)"
lead: "Three simple equations, and yet long-range weather can never be predicted exactly. Lorenz discovered that deterministic systems can be extremely sensitive to initial conditions: the butterfly effect sets a fundamental time limit on predictability."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the early 1960s, meteorologists widely believed that if the equations were precise enough, the initial observations dense enough and the computing power large enough, the weather could be forecast indefinitely far ahead. This was an extension of Laplacian determinism: deterministic equations yield a determined future. Lorenz used an early computer to solve numerically a highly simplified model of atmospheric convection, to see how far a long-range forecast could actually go.

### The problem

Then came an accident: he truncated an intermediate value to three decimal places and restarted the computation, expecting the result to be almost unchanged, yet before long the trajectory had **parted ways completely** with the original. The system was purely deterministic, with no random term at all, yet it amplified tiny differences in the initial values dramatically. **Why would a deterministic system become, in practice, unpredictable in the long run?** This struck at the heart of deterministic predictability.

### Other approaches of the time (and their limits)

- **Laplacian determinism**: deterministic equations + exact initial values = a fully computable future. Its limit is that it ignores exponential sensitivity to initial conditions, while in reality initial values can only ever be approximate.
- **Linear-stability intuition**: the belief that small perturbations have only small consequences. This fails for nonlinear systems, where errors grow exponentially.
- **Attributing unpredictability to random noise**: the mistaken view that only randomness causes uncertainty. Lorenz showed that determinism by itself is enough to produce unpredictability.

### Method

Lorenz's system has only three variables and three nonlinear ordinary differential equations:

$$ \dot{x}=\sigma(y-x),\qquad \dot{y}=x(\rho-z)-y,\qquad \dot{z}=xy-\beta z $$

With the classical parameters $$\sigma=10,\ \rho=28,\ \beta=8/3$$, the trajectory neither converges to a fixed point nor settles into a cycle; instead it winds around a **strange attractor** (the Lorenz attractor) that never intersects itself. The core mechanism is sensitive dependence on initial conditions: two trajectories initially a distance $$|\delta_0|$$ apart diverge approximately exponentially,

$$ |\delta(t)|\approx |\delta_0|\,e^{\lambda t} $$

where $$\lambda>0$$ is the largest **Lyapunov exponent**. It directly gives the time scale of predictability: the time needed for an error to grow to the size of the system itself is about $$1/\lambda$$, and beyond that limit, no amount of precision in the initial values helps. This is the **butterfly effect**.

### Impact

Lorenz showed that "deterministic yet unpredictable in the long run" is not a contradiction but the normal state of nonlinear systems. His three equations became the emblematic example of chaos theory; strange attractors and positive Lyapunov exponents became the tools for diagnosing chaos, and they gave a quantitative explanation of why weather forecasting has an inherent time limit.

### Significance and outlook

For time series, chaos poses a fundamental dichotomy: does a seemingly random series come from a high-dimensional stochastic process, or from low-dimensional deterministic chaos? Answering that requires phase-space reconstruction, which is exactly the starting point of [Takens's embedding theorem](../takens/) in 1981, showing that the geometry of the attractor can be rebuilt from a single observed series. The Lyapunov exponent, meanwhile, provides a principled upper bound on "how much longer can this series be predicted". Lorenz made people realize that the limits of prediction sometimes lie not in the data or the computing power, but are written into the dynamics itself.
