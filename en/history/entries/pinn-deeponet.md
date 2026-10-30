---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2019 · Physics"
permalink: /en/history/e/pinn-deeponet/
title: "Physics-Informed Networks and Neural Operators (Raissi · Lu, 2019)"
lead: "If the governing equations themselves are written into the loss function, can a neural network both fit the data and obey the physics? And going a step further, can it learn the solutions of a whole family of equations at once?"
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

A great many dynamical systems — fluids, heat conduction, waves — are described by **partial differential equations (PDEs)**. Traditionally they are discretized and solved with numerical methods such as finite differences and finite elements, which are accurate but expensive in their meshes; **inverse problems** (recovering unknown parameters or fields from sparse observations) are especially hard. Meanwhile, neural networks are good at fitting data but often ignore physical constraints, and become unreliable when extrapolating into regions without data.

### The problem

Two long-standing wishes. First, **can a data-driven model be made to respect known physical laws**, giving physically plausible solutions even from sparse or noisy observations, and solving for the unknown parameters of an inverse problem along the way? Second, traditional numerical solvers **must recompute from scratch for every set of parameters or initial/boundary conditions** — could one train a model that learns the "input function to output function" mapping once and for all, and gives the solution for a new input instantly?

### Other approaches of the time (and their limits)

- **Pure numerical solvers (FEM/FDM)**: accurate and reliable, but meshes are expensive, every new configuration needs a fresh solve, and inverse problems require repeated forward simulations.
- **Pure data-driven regression**: flexible, but it contains no physical constraints, extrapolates poorly, needs a lot of data, and has little physical credibility.
- **Classical neural networks approximating a single solution function**: they can fit one solution curve, but this turns the solver into a single-use tool that cannot generalize to different input functions.

### Method

The **PINN (physics-informed neural network)** represents the solution directly with a network $$u_\theta(x,t)$$ and uses automatic differentiation to write the PDE residual into the loss. For an equation of the form $$u_t+\mathcal{N}[u]=0$$, the residual is defined as $$r_\theta=\partial_t u_\theta+\mathcal{N}[u_\theta]$$, and the following is minimized jointly:

$$ \mathcal{L}=\underbrace{\frac{1}{N_d}\sum\big(u_\theta-u_{\text{obs}}\big)^2}_{\text{data/boundary}}+\lambda\,\underbrace{\frac{1}{N_r}\sum r_\theta^2}_{\text{physics residual}} $$

The physics residual term makes the network obey the equation even where there is no data; if the equation contains unknown parameters, they are simply treated as trainable variables and optimized alongside, which solves the inverse problem. **DeepONet (deep operator network)** goes a step further and learns an **operator** $$G:u\mapsto G(u)$$. A "branch net" encodes the values of the input function $$u$$ at a set of sample points, a "trunk net" encodes the query coordinate $$y$$, and their inner product gives the output:

$$ G_\theta(u)(y)=\sum_{k=1}^{p} b_k(u)\,t_k(y) $$

This architecture is backed by a theoretical guarantee that it can approximate any continuous nonlinear operator (the universal operator approximation theorem).

### Impact

PINNs can solve forward problems under sparse, noisy data while simultaneously identifying unknown coefficients in the PDE, unifying "solving" and "inverting" in a single optimization. Once trained, DeepONet produces the entire solution for a **new input function** almost instantly, far faster than repeated numerical solves, and it shows strong generalization across many classes of parameterized PDEs.

### Significance and outlook

These two works welded "scientific computing" to "deep learning": PINNs make networks obey physics, and DeepONet makes networks learn the "solution operator" itself. At their core they share something with time series — both are about learning how dynamics evolve in space and time. Along the "learning operators" line there soon appeared the Fourier neural operator, which performs global convolutions in the frequency domain ([../fno/](../fno/)), leading further to data-driven weather and climate forecasting ([../neural-weather/](../neural-weather/)).
