---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1949 · Mathematics"
permalink: /en/history/e/feynman-kac/
title: "Solving PDEs with Random Paths (Kac · Feynman, 1949)"
lead: "The solution of a parabolic partial differential equation turns out to equal an average taken over countless random paths — the Feynman–Kac formula welds deterministic PDEs to expectations of stochastic processes."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

In 1948 Feynman put forward the **path integral** formulation of quantum mechanics: the evolution of a particle is a sum over all possible paths. After hearing the talk, Mark Kac realized that applying this "sum over paths" idea to the **real** diffusion equation (rather than the Schrödinger equation in imaginary time) could be made rigorous — because what appears there is precisely the [Wiener measure](../ito/). In 1949 Kac gave the rigorous result now known as the **Feynman–Kac formula**, expressing for the first time the solution of a parabolic PDE as the expectation of a stochastic process.

### The problem

**Parabolic PDEs** such as the heat and diffusion equations are usually solved by analytical means (separation of variables, Green's functions), which become extremely difficult as the dimension grows. **Could one take a different viewpoint: rather than solving the equation directly, use a crowd of randomly walking particles to "sample" the solution?** And conversely, what exactly is the relationship between PDEs and stochastic processes?

### Other currents of the time (and their limits)

- **Purely analytical methods (Green's functions, eigenfunction expansions)**: elegant in low dimensions with regular boundaries, but faced with high dimensions, variable coefficients or complex boundaries they hit the curse of dimensionality, and closed-form solutions are hard to find.
- **Deterministic finite differences**: discretize the PDE on a grid. The number of grid points grows exponentially with the dimension, making high-dimensional computation infeasible.
- **Formal path integrals**: Feynman's sum is enormously powerful in physics, but its measure is not rigorous in imaginary time (it is not a true measure). **Kac's key correction** was to move to real diffusion, so that the "sum" over paths becomes a genuine expectation with respect to Wiener measure, and thus rigorous.

### The method

Consider a parabolic PDE with a potential term $$V$$ and a source term
$$ \frac{\partial u}{\partial t}=\tfrac12\sigma^2\,\frac{\partial^2 u}{\partial x^2}+\mu\,\frac{\partial u}{\partial x}-V(x)\,u,\qquad u(0,x)=f(x) $$
The Feynman–Kac formula asserts that its solution can be written as an **expectation** over a diffusion process $$X_s$$ (satisfying $$dX_s=\mu\,ds+\sigma\,dW_s$$, $$X_0=x$$):

$$ u(t,x)=\mathbb{E}\Big[\,f(X_t)\,\exp\!\Big(-\!\int_0^t V(X_s)\,ds\Big)\,\Big|\,X_0=x\Big] $$

The intuition: release countless random trajectories from $$x$$, let each carry the weight $$\exp(-\!\int V)$$ to its end point and take the value of $$f$$ there, then average over all paths — this gives the solution at that point. The engine of the proof is precisely [Itô's lemma](../ito/): differentiating $$u(t-s,X_s)\exp(-\!\int_0^s V)$$, the PDE makes the drift terms cancel exactly, leaving a **martingale**; taking the expectation of the martingale yields the formula.

### Results

Solving PDEs thus gained a "Monte Carlo" route: estimate the expectation by random simulation, with a computational cost that no longer explodes exponentially with the dimension — high-dimensional problems suddenly opened up. More profoundly, it revealed that the generator of a diffusion process and the parabolic operator are one and the same, permanently linking the two great fields of probability theory and partial differential equations.

### Significance and outlook

Feynman–Kac is the theoretical engine of continuous-time finance. The solution of the 1973 [Black–Scholes](../black-scholes/) pricing PDE can be written directly as "the expectation of the discounted payoff under the risk-neutral measure" — this is the financial incarnation of Feynman–Kac, and the basis of Monte Carlo pricing. It made "solving an equation" and "averaging over random paths" one and the same thing, and it still runs through derivatives pricing, stochastic control, rare-event simulation, and sampling-based solvers in physics and machine learning.
