---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1906 · Mathematics"
permalink: /en/history/e/markov/
title: "The Memoryless Chain (Markov, 1906)"
lead: 'Must the law of large numbers rely on "independence" to hold? With a chain that remembers only the present and forgets the past, Markov proved it need not: it is enough for the future to depend only on the present. From then on, stochastic processes had a skeleton.'
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In late 19th-century probability theory, the heavyweight results (the law of large numbers, the central limit theorem) were almost all built on the assumption of **independence**. The dispute between Andrey Markov and Nekrasov, among others, centred on exactly this point: Nekrasov suggested that the law of large numbers required independence. Markov disagreed and set out to construct a class of random variables that were **dependent yet still obeyed the limit laws**. From 1906 on, he introduced and studied the "chains" later named after him, and gave a famous empirical illustration using the alternation of vowels and consonants in Pushkin's verse novel *Eugene Onegin*.

### The problem

Real sequences are dependent almost everywhere: today's weather affects tomorrow's, and one letter affects the next. **If the variables are not independent, do the limit theorems of probability still hold? How much dependence is "manageable"?** Completely arbitrary dependence cannot be analysed, while complete independence is divorced from reality: what was needed was a middle ground that is both realistic and tractable.

### Other approaches of the time (and their limits)

- **The i.i.d. paradigm**: the mainstream premise of limit theorems at the time. Mathematically beautiful, but it excludes the ubiquitous phenomenon of "the past influencing the present", and cannot describe real sequences such as weather, language or population.
- **Complete dependence / determinism**: the other extreme, holding that a system is entirely determined by its initial conditions. There is no randomness to speak of, so it can neither explain the fluctuations seen in observations nor give probabilistic tools anything to do.
- What was missing was a **structured dependence**: one that keeps randomness while restricting dependence to a form that can be computed recursively.

### Method

Markov's core idea is the **Markov property (memorylessness)**: given the present, the future is conditionally independent of the past. For a sequence of states $$\{X_t\}$$,

$$ \mathbb P(X_{t+1}=j \mid X_t=i,\,X_{t-1},\dots,X_0)=\mathbb P(X_{t+1}=j\mid X_t=i)=p_{ij} $$

The whole chain is determined by the **transition matrix** $$P=(p_{ij})$$. Multi-step transitions satisfy the **Chapman–Kolmogorov equation**:

$$ p_{ij}^{(m+n)}=\sum_{k} p_{ik}^{(m)}\,p_{kj}^{(n)} $$

That is, going from $$i$$ to $$j$$ in $$m+n$$ steps equals the sum, over all intermediate states $$k$$, of the probabilities of "first $$m$$ steps, then $$n$$ steps", breaking long-range evolution into short steps that can be multiplied together. Under suitable conditions (irreducible, aperiodic), the chain converges to a unique **stationary distribution** $$\pi$$ satisfying $$\pi P=\pi$$.

### Impact

Markov proved that even when the variables are dependent, the law of large numbers still holds as long as they have this chain structure, directly answering the dispute with Nekrasov. More importantly, he provided the first class of stochastic processes that were **both analytically tractable and close to reality**: dependence is compressed into a one-step transition, long-term behaviour is described by the stationary distribution, and analysis becomes feasible.

### Significance and outlook

The Markov property became the common skeleton of the entire theory of stochastic processes. [AR autoregression](../yule-ar/) is its special case for linear Gaussian continuous states; the hidden Markov model (HMM) adds an observation layer on top; the Markov decision process (MDP) is the foundation of reinforcement learning; and MCMC turns the idea around, "designing" a chain whose stationary distribution is the target distribution in order to sample from it. The continuous-time version was systematized through [Kolmogorov](../kolmogorov/)'s forward and backward equations, with [Brownian motion](../brownian-motion/) and the [OU process](../ornstein-uhlenbeck/) among its members. Today, when large language models "predict the next token from the current context", they are at heart a Markov chain with an extended memory.
