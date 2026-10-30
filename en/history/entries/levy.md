---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1934 · Mathematics"
permalink: /en/history/e/levy/
title: "Jumps, Heavy Tails and Independent Increments (Lévy, 1934)"
lead: 'Brownian motion is too "gentle": Gaussian increments, continuous paths, finite variance. Yet real crashes are instantaneous jumps and fat tails. Lévy extended the family of stochastic processes to jumps and heavy tails, foreshadowing the true face of finance.'
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

By the 1930s, the [Wiener process (Brownian motion)](../brownian-motion/) had become the model continuous-time stochastic process, but it rests on three strong, special assumptions: Gaussian increments, continuous paths and finite variance. Around 1934, Paul Lévy undertook a systematic study of general stochastic processes **with independent, stationary increments** (now called **Lévy processes**), asking: what processes can satisfy the minimal structure of "independent increments + stationary increments"? The answer turned out to be far richer than Brownian motion.

### The problem

The Gaussian assumption of Brownian motion comes from the central limit theorem, but that theorem requires the small shocks being added up to have finite variance. **What happens if a single shock can itself be very large (heavy tails), or if the process can jump instantaneously? What distribution do the increments follow then, and can the process still have a sound mathematical structure?** Stock-market crashes, huge insurance claims and the arrival of telephone calls in real life all carry jumps and fat tails that Brownian motion cannot produce.

### Other approaches of the time (and their limits)

- **The central place of the Gaussian**: the default view that all random fluctuations eventually become Gaussian. It holds when variance is finite, but it systematically **underestimates extreme events**: describing financial returns with a Gaussian makes a "once-in-a-century" crash look almost impossible.
- **The continuous-path assumption**: prices and signals are taken to change continuously. But many real processes (defaults, earthquakes, orders) move in **discrete jumps**, and continuous models miss the jumps by construction.
- These two convenient assumptions masked the **heavy tails and jumps** of the real world; a more general class of processes was needed to accommodate them.

### Method

A Lévy process $$\{X_t\}$$ is defined by three axioms: $$X_0=0$$; its increments are **independent** and **stationary**; and it is stochastically continuous. All of its information is condensed in the **Lévy–Khinchin formula** for the characteristic function:

$$ \mathbb E\big[e^{i u X_t}\big]=\exp\!\Big\{ t\Big( i b u-\tfrac12 \sigma^2 u^2+\!\int_{\mathbb R}\big(e^{iux}-1-iux\mathbf 1_{|x|<1}\big)\,\nu(dx)\Big)\Big\} $$

The three terms correspond to a **drift** $$b$$, a **Brownian diffusion** $$\sigma^2$$, and **jumps** characterized by the **Lévy measure** $$\nu$$: $$\nu(dx)$$ describes the intensity with which jumps of size $$x$$ occur. Brownian motion is just the special case $$\nu\equiv 0$$. Closely related are **stable distributions**: when the increments are self-similar and may be heavy-tailed, one obtains stable laws, whose tails decay as a power law $$\sim |x|^{-\alpha-1}$$ (with infinite variance when $$\alpha<2$$):

$$ \mathbb P(|X|>x)\sim C\,x^{-\alpha},\qquad 0<\alpha<2 $$

### Impact

Lévy freed stochastic processes from "Gaussian + continuous" and opened up the complete family "drift + diffusion + jumps", giving a precise language for describing **heavy tails and jumps**. Stable distributions provided a generalization of the central limit theorem to the case of infinite variance. In the same period, his foundational work with Doob on **martingale** theory raised [Bachelier](../bachelier/)'s intuition that "the best forecast is the current value" into a rigorous and general framework.

### Significance and outlook

Lévy's work is a watershed for modern stochastic analysis and mathematical finance. Looking forward, it connects to Itô's stochastic integral and to jump-diffusion models (Merton's jump diffusion, the variance gamma model); it also inspired the modelling of **heavy tails and volatility clustering** in financial returns, precisely the phenomena that Mandelbrot observed and that ultimately gave rise to ARCH/GARCH. Today, whenever we speak of "fat-tail risk", "jumps", "stable distributions" or "martingales", or replace Gaussian noise with Lévy noise in deep generative models, we are still using the more realistic map of the random world that Lévy drew in 1934.
