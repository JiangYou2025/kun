---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1952 · Mathematics"
permalink: /en/history/e/robbins-bandit/
title: "Multi-Armed Bandits and Sequential Design (Robbins, 1952)"
lead: "Facing several slot machines with unknown payoffs, should you keep pulling the one that pays best so far, or risk trying the others? Robbins turned the dilemma of “exploration versus exploitation” into mathematics."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

After the Second World War, statistics was moving from "collect all the data first, then analyse" toward "decide while collecting". Wald's sequential analysis had already shown that stopping sampling as needed saves samples. In his 1952 paper "Some aspects of the sequential design of experiments", Herbert Robbins pushed the perspective further: an experiment can not only **decide when to stop**, but can also, at every step, **decide where the next observation comes from**. Clinical trials, production inspection and ad placement are all situations of this "learning by doing" kind.

### The problem

Imagine $$K$$ slot machines ("arms"), each with an unknown expected payoff. You have a limited number of pulls, and each pull reveals only the random payoff of the machine you chose. **Should you put all your pulls on the machine that currently looks best (exploitation), or spend some of them trying the others so as not to miss a better one (exploration)?** Committing too hard can leave you stuck on a suboptimal arm; trying too much wastes rounds — this is the fundamental tension of **exploration vs. exploitation**, and it is an online sequential decision problem.

### Other approaches of the time (and their limits)

- **Fixed-design experiments + classical hypothesis testing**: fix the sample size for each treatment in advance and collect everything at once. Statistically rigorous, but during collection there is no way to feed "what has already been observed to work well or badly" back into later allocation, which wastes samples and delays gains.
- **Pure greed (always choose the arm with the highest current estimate)**: optimal in the short term, but early bad luck can lead it to abandon the truly best arm too soon, locking it into a suboptimal one for the long run.
- **Pure uniform random trials**: gather plenty of information, but keep wasting rounds on obviously suboptimal arms, accumulating large losses.

### Method

Robbins formalized the core measure of **regret**: the accumulated difference between "the expected payoff of the best fixed strategy in hindsight" and "the payoff of the strategy actually used". Let the expected payoff of arm $$a$$ be $$\mu_a$$, the best arm $$\mu^{*}=\max_a \mu_a$$, and $$A_t$$ the arm chosen at step $$t$$ over $$T$$ rounds; the cumulative regret is then

$$ R_T = T\,\mu^{*} - \mathbb{E}\!\left[\sum_{t=1}^{T}\mu_{A_t}\right] = \sum_{a}\Delta_a\,\mathbb{E}[N_a(T)] $$

where $$\Delta_a=\mu^{*}-\mu_a$$ is the suboptimality gap of arm $$a$$ and $$N_a(T)$$ is the number of times it is chosen. The aim of a good strategy is to make $$R_T$$ grow as slowly as possible (**sublinearly**, i.e. $$R_T/T\to0$$). Robbins gave simple rules guaranteeing that the best arm is chosen asymptotically, and pointed out that to keep regret under control, exploration must be gradually reduced over time and the rounds concentrated on high-payoff arms.

### Impact

This paper laid down the founding problem of sequential experimental design and of **reinforcement learning**. Later, Lai and Robbins (1985) proved a logarithmic lower bound on regret, $$\Omega(\log T)$$, which is attained by algorithms such as UCB (upper confidence bound) and Thompson sampling. Today the "adaptive traffic allocation" in A/B testing, recommender systems and online advertising is, at heart, the multi-armed bandit put into engineering practice.

### Significance and outlook

The multi-armed bandit distilled the dilemma of "learning while earning under uncertainty" into a mathematical object that can be analysed and optimized, and "regret" became the universal yardstick of online decision-making. Downstream it connects to [Bellman's dynamic programming](../bellman-dp/) and Markov decision processes (a bandit with state is reinforcement learning); outward it reaches into experimental design, Bayesian optimization and automated decision-making. Whenever a modern system must weigh "using the best known option" against "exploring for an unknown better one", what it measures is still the regret Robbins left behind.
