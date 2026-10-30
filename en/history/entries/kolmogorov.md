---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1933 · Mathematics"
permalink: /en/history/e/kolmogorov/
title: "The Axioms of Probability (Kolmogorov, 1933)"
lead: "What exactly is probability? For three hundred years it had been “a gambler's intuition”. In 1933 Kolmogorov nailed it down with three measure-theoretic axioms, and only then did “time averages equal ensemble averages” become a provable theorem."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

From Pascal and Fermat to Laplace, probability theory had accumulated a wealth of results, yet it still lacked a rigorous logical foundation — Hilbert's sixth problem of 1900 even listed "the axiomatization of probability" as an open question. In the early twentieth century, Lebesgue's theory of measure and integration matured, offering probability a possible vehicle. In 1933 Andrey Kolmogorov published *Foundations of the Theory of Probability* (*Grundbegriffe der Wahrscheinlichkeitsrechnung*), completing the axiomatization at a stroke through measure theory and formally establishing probability as a branch of modern mathematics.

### The problem

Before Kolmogorov, "random variable", "conditional probability" and "the limit of infinitely many trials" had no unified definitions, and many claims about infinite and continuous random processes could not be rigorously proved. Above all there was a question crucial for time series: **we can only observe one time series (a single realization), so what entitles us to use its time average to estimate the true expectation (the ensemble average) of the whole random process?** Without axiomatic probability, the legitimacy of this inference remained unsettled.

### Other approaches of the time (and their limits)

- **The frequentist intuition (von Mises's "collectives")**: defines probability as the limiting frequency over infinitely many trials. The idea is natural, but a "random sequence" itself is hard to define without contradiction, so it is not clean enough as an axiomatic foundation.
- **The classical equally-likely definition**: probability = number of favourable outcomes / total number of outcomes. It applies only to finite, symmetric situations and fails immediately for continuous distributions and random processes.
- Neither could support a theory of **continuous-time, infinite-dimensional** random processes, which is exactly what time series and diffusion processes require.

### Method

Kolmogorov defined probability as a **measure** on a probability space $$(\Omega,\mathcal F,\mathbb P)$$ satisfying three axioms: non-negativity, normalization $$\mathbb P(\Omega)=1$$, and countable additivity

$$ \mathbb P\Big(\bigcup_{i=1}^{\infty} A_i\Big)=\sum_{i=1}^{\infty}\mathbb P(A_i)\quad(\text{for pairwise disjoint }A_i) $$

Random variables are measurable functions, expectations are integrals, and conditional expectations are rigorously defined by the Radon–Nikodym theorem. His **consistency (extension) theorem** guarantees that as long as the finite-dimensional distributions are mutually consistent, there exists a random process defined on entire paths, so continuous-time processes legitimately exist. For Markov processes he wrote down the **forward/backward equations** governing the evolution of the probability density (the Kolmogorov equations, corresponding to Fokker–Planck in physics):

$$ \frac{\partial p}{\partial t}=-\frac{\partial}{\partial x}\big[\mu(x)p\big]+\frac12\frac{\partial^2}{\partial x^2}\big[\sigma^2(x)p\big] $$

Within this framework the **ergodic theorem** could be rigorously stated and proved: for an ergodic stationary process,

$$ \frac1T\int_0^T f(X_t)\,dt \;\xrightarrow{\;T\to\infty\;}\; \mathbb E[f(X_0)] $$

that is, **the time average converges to the ensemble average**.

### Impact

From then on, probability theory enjoyed the same rigorous standing as analysis and algebra. The most direct payoff: the ergodic theorem provided a proof of legitimacy for "statistical inference from a single sample path" — without it, estimates of the mean and autocovariance of a time series would not stand up logically. The forward and backward equations, for their part, put the stochastic dynamics of [Langevin / OU](../langevin/) in exact correspondence with deterministic partial differential equations.

### Significance and outlook

Kolmogorov's axiomatization is the common foundation of all later theory of random processes: the martingale theory of [Lévy](../levy/) and Doob, Itô's stochastic integral, [Wiener–Khinchin spectral theory](../wiener-khinchin/), and even the generalization theory of modern statistical learning are all built upon it. Whenever we assume that "the data are independent samples from some distribution" or that "stationarity makes the estimate consistent", these 1933 axioms are quietly vouching for us in the background. They made "inferring an infinite random world from finite observations" a rigorous science.
