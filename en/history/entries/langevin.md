---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1908 · Physics"
permalink: /en/history/e/langevin/
title: "The Random Force (Langevin, 1908)"
lead: "Einstein computed how a probability distribution spreads; Langevin insisted on writing down the force on the particle directly — a friction term plus a random term, three lines of Newton's equation that gave rise to the whole theory of stochastic differential equations."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In 1905–1906 [Einstein and Smoluchowski](../brownian-motion/) had already explained Brownian motion with the diffusion equation, but their route — "find how the probability density evolves" — was rather abstract. In 1908 Paul Langevin proposed a more intuitive route, "infinitely simpler" in his own words: still use Newton's second law and write the equation of motion for a single particle directly, but split the net force of the molecular impacts into two parts. This viewpoint put randomness inside the differential equation itself.

### The problem

A particle in a liquid is struck by countless molecules. These impacts produce both a **systematic viscous drag** (the faster the particle moves, the harder it is hit head-on, which shows up as friction) and **irregular instantaneous fluctuations** (the random imbalance of the impacts). **Can both effects be written into a single equation of motion that yields diffusion while keeping the form of Newtonian mechanics?** The difficulty is that the equation then contains a random force that is discontinuous everywhere and cannot be differentiated in the classical sense.

### Other approaches of the time (and their limits)

- **Purely deterministic mechanics**: write Newton's equation with smooth external forces. It cannot accommodate "trillions of random impacts per second": either it ignores the fluctuations and gets no diffusion, or it tries to track every molecule explicitly, which is computationally impossible.
- **Einstein's pure probability-density route**: talks only about the evolution of the distribution $$\rho(x,t)$$ and avoids individual paths. It is correct and powerful, but it does not directly say "what force the particle feels right now"; the physical picture is not concrete enough, and it is not easily extended to cases with external forces or velocity dependence.
- What was missing was a bridge: one that unifies **the dynamics of a single random trajectory** with macroscopic diffusion.

### Method

Langevin's key idea was to split the molecular impact force into a deterministic friction term and a random force term, giving the **Langevin equation**:

$$ m\,\frac{dv}{dt}=-\gamma\, v + \xi(t) $$

where $$-\gamma v$$ is viscous friction proportional to velocity (Stokes drag, $$\gamma=6\pi\eta a$$), and $$\xi(t)$$ is a zero-mean **random force (white noise)** satisfying

$$ \langle \xi(t)\rangle=0,\qquad \langle \xi(t)\xi(t')\rangle = 2\gamma k_B T\,\delta(t-t') $$

The second relation is the **fluctuation–dissipation relation**: the same molecular impacts provide both dissipation (friction $$\gamma$$) and fluctuation (the strength of the random force), and the temperature $$T$$ locks the two together. With a few lines of algebra Langevin thereby re-derived $$\langle x^2\rangle = 2Dt$$, in complete agreement with Einstein.

### Impact

For the same Brownian motion, Langevin provided a "language of forces" far more intuitive than the diffusion equation, and it extended easily to cases with external force fields and inertia. The fluctuation–dissipation relation became one of the central theorems of statistical physics, quantitatively linking observable dissipation to microscopic fluctuations.

### Significance and outlook

The Langevin equation is the physical prototype of the **stochastic differential equation (SDE)**: a deterministic drift plus a noise drive. Making its white-noise term mathematically rigorous required the theory of stochastic integration developed later by Itô and Stratonovich; in the overdamped limit it directly yields the [Ornstein–Uhlenbeck process](../ornstein-uhlenbeck/), whose discretization is exactly AR(1), translating "friction + thermal noise" into "[autoregression](../yule-ar/)". From molecular dynamics and financial volatility modelling to the "score + noise" sampling in today's diffusion generative models (Langevin dynamics sampling), all are echoes of this 1908 equation.
