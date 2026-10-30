---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1953 · Mathematics"
permalink: /en/history/e/doob-martingale/
title: "Martingale Theory (Doob, 1953)"
lead: "“In a fair game, your expected wealth at the next moment equals your wealth now.” Doob forged this plain intuition into the backbone of modern stochastic processes — and it became the mathematical heart of no-arbitrage finance."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

The word "martingale" comes from an old gambling strategy: "double your bet whenever you lose". Lévy and Ville gave it a probabilistic definition in the 1930s, but the person who truly built it into a complete theoretical edifice was Joseph L. Doob, in his 1953 magnum opus *Stochastic Processes*. By then measure-theoretic probability (Kolmogorov's axiomatization) had matured, and a language was needed to describe precisely the dynamics of "information accumulating over time" — martingales filled exactly that gap.

### The problem

How can "a fair game" and "a flow of information" be expressed with mathematical rigour? Intuitively, in a fair game your best forecast of your future wealth is your current wealth; but to make this statement provable and usable — to prove that no betting system can win for sure, to obtain convergence results and inequalities — one must first define precisely "taking the conditional expectation given the known information", and constrain how it evolves over time. **How do you turn "unpredictable fair fluctuation" into an object you can compute with and prove theorems about?**

### Other currents of the time (and their limits)

- **Processes with independent increments (random walks, Brownian motion)**: clearly structured, but they require increments to be mutually independent, which is too strong; many fair processes are not independent and yet still "cannot predict the direction of the next step".
- **Spectral theory of stationary processes ([Wold](../wold/), Wiener)**: excellent for second moments and frequency-domain analysis, focused on correlation structure, but it does not directly describe the dynamics of "conditional expectations updated as information arrives", nor stopping times.
- **Classical limit theorems (law of large numbers, central limit theorem)**: designed for sums of independent variables, and hard to apply directly to sequential situations with dependence where one must stop at a random time.

### The method

Given an increasing sequence of information sets (a **filtration**) $$\mathcal{F}_0\subseteq\mathcal{F}_1\subseteq\cdots$$, a process $$\{X_t\}$$ is called a **martingale** if it is adapted to the filtration and

$$ \mathbb{E}\!\left[X_{t+1}\mid \mathcal{F}_t\right] = X_t $$

That is: when you forecast the next moment using all the information up to $$t$$, the best guess is the current value — this is the precise statement of "fairness" ($$\ge$$ gives a submartingale, $$\le$$ a supermartingale). On this basis Doob built three pillars. The **Doob decomposition**: every submartingale can be uniquely split into a martingale and a predictable increasing process,

$$ X_t = M_t + A_t,\qquad M\ \text{is a martingale},\ A\ \text{is predictable and non-decreasing} $$

cleanly separating the "predictable trend" $$A_t$$ from the "unpredictable fair fluctuation" $$M_t$$. The **optional stopping theorem**: under suitable conditions $$\mathbb{E}[X_\tau]=\mathbb{E}[X_0]$$, which asserts that no stopping strategy based on available information can change the expectation of a fair game (betting systems cannot win for sure). And **Doob's maximal inequality** together with the **martingale convergence theorem**, which guarantee that bounded martingales converge almost surely.

### Results

Martingales quickly became a universal tool for stochastic processes: they unified proofs of the law of large numbers, underpin Itô stochastic integration and stochastic differential equations, and made the analysis of "stopping at a random time" tractable. In statistics, they placed sequential testing, likelihood ratios and stopping-time analysis within a single framework.

### Significance and outlook

Martingales are the mathematical heart of modern finance. The **efficient market hypothesis** says that prices already reflect all information and that future changes are unpredictable — which is precisely $$\mathbb{E}[X_{t+1}\mid\mathcal{F}_t]=X_t$$; **no arbitrage** is equivalent to the existence of an "equivalent martingale measure" under which discounted prices are martingales, from which Black–Scholes option pricing follows. Seen from this angle, [Bachelier](../bachelier/)'s random walk of 1900 was its embryo, and the "regret" and stopping-time analysis of the [Robbins bandit](../robbins-bandit/) are close neighbours. A single sentence — "the expectation of the next moment equals the present" — has held up half a century of work, from the limit theorems of probability to derivatives pricing.
