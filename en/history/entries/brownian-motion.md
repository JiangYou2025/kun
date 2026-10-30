---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1905 · Physics"
permalink: /en/history/e/brownian-motion/
title: "The Physical Theory of Brownian Motion (Einstein · Smoluchowski, 1905)"
lead: "Why do pollen grains jitter in water without ever stopping? Einstein's answer: you are watching invisible molecules hit them. A microscopic random process left hard evidence in a mean squared displacement proportional to time."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In 1827 the botanist Brown observed that tiny particles from pollen suspended in water jittered ceaselessly and irregularly, and for almost eighty years nobody could explain it. At the start of the twentieth century the atomic-molecular theory was still contested; some physicists (such as Mach and Ostwald) even doubted that atoms really existed. In 1905 (Einstein) and 1906 (Smoluchowski) each gave a quantitative theory of Brownian motion, turning this microscopic jitter into testable evidence for the existence of atoms.

### The problem

If a particle is struck by water molecules from all sides, each impact in a random direction, with a resultant force that averages to zero, **why does the particle keep wandering further away instead of staying put?** And its motion seems to show no inertia whatsoever. What exactly is the relation between displacement and time? Can this relation be measured experimentally and, in turn, be used to weigh the size of molecules?

### Other approaches of the time (and their limits)

- **The mechanical / inertial-trajectory view**: tries to follow the particle's instantaneous velocity and trajectory as one would a billiard ball. The limitation is that collisions occur trillions of times per second, so the instantaneous velocity simply cannot be measured; in practice this road is a dead end.
- **A purely qualitative thermal-agitation account**: accepts that molecular impacts are the cause but stays at the level of qualitative description, offering no verifiable quantitative prediction, and so cannot be used to decide whether atomic theory is true.
- The breakthrough was to give up following trajectories and instead study **statistics of the displacement** (the mean squared displacement), linking it to the macroscopically measurable diffusion coefficient.

### Method

Einstein's key move was to jump from random trajectories to the **evolution of a probability density**: the distribution of particle positions $$\rho(x,t)$$ satisfies the **diffusion equation**

$$ \frac{\partial \rho}{\partial t}=D\,\frac{\partial^2 \rho}{\partial x^2} $$

Its solution is a Gaussian distribution whose variance grows linearly with time, so **the mean squared displacement is proportional to time**:

$$ \langle x^2\rangle = 2Dt $$

and the diffusion coefficient is tied to temperature, viscosity and particle size by the **Einstein relation**:

$$ D=\frac{k_B T}{6\pi\eta a} $$

where $$k_B$$ is the Boltzmann constant, $$T$$ the temperature, $$\eta$$ the viscosity and $$a$$ the particle radius. That $$\langle x^2\rangle\propto t$$ rather than $$\propto t^2$$ is precisely the statistical fingerprint that distinguishes "inertia-free random accumulation" from "uniform motion".

### Impact

In 1908 Perrin verified $$\langle x^2\rangle = 2Dt$$ precisely by experiment and used it to measure Avogadro's number, **settling the question of whether atoms really exist** (Perrin later received the Nobel Prize). A seemingly pure random process turned out to be a balance for weighing molecules.

### Significance and outlook

The mathematical skeleton of Brownian motion, "independent increments, Gaussian increments, variance proportional to time", was rigorously constructed by Norbert Wiener in 1923 and became the **Wiener process** of probability theory, the cornerstone of almost every continuous-time stochastic process. It gave [Bachelier](../bachelier/)'s financial random walk of five years earlier both a physical and a mathematical foundation. It leads on to the [Langevin equation](../langevin/), another description of the same phenomenon, and to stochastic differential equations, to the [Ornstein–Uhlenbeck process](../ornstein-uhlenbeck/), and through the Itô integral to modern stochastic analysis. Whenever we speak today of "diffusion models" or "stochastic processes", the source lies on that jittering surface of water.
