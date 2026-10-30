---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1900 · Mathematics"
permalink: /en/history/e/bachelier/
title: "The Theory of Speculation (Bachelier, 1900)"
lead: "What should you bet tomorrow's stock price will be? In his doctoral thesis Bachelier gave a sobering answer: the best forecast is today's price. That one sentence planted the seeds of the random walk, Brownian motion and modern mathematical finance."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In 1900, in Paris, Louis Bachelier completed his doctoral thesis *Théorie de la spéculation* (*The Theory of Speculation*) under the supervision of Henri Poincaré. His subject was the price of government bonds on the Paris Bourse. Economics at the time made almost no use of probability: prices were seen as the outcome of a contest between supply and demand, and nobody modelled them as a **stochastic process**. Bachelier's starting point was practical: what is the fair price of an option or a futures contract? To answer that, one first needs a mathematical model of "how prices fluctuate over time".

### The problem

Price movements look chaotic and seem to follow no rule. But can "no rule" itself be described mathematically? More pointedly: **if the market is fair, what should the best forecast of a future price be?** Everyone instinctively wants to predict rises and falls, but in a fair, well-informed market, should the expected future price not simply equal the present one?

### Other approaches of the time (and their limits)

- **The deterministic "intrinsic value" view**: prices oscillate around some computable true value, and if you compute that value precisely you can predict the price. Its limitation is that it throws away short-term fluctuations as noise, cannot quantify risk and gives no way to price options.
- **Charting and trend extrapolation**: "reading" a trend off the historical curve and extending it. This implicitly assumes that past direction will persist, but in an efficient market predictable trends are arbitraged away, so such extrapolation has no theoretical support.
- Both sidestep the core issue: the **probabilistic structure** of price fluctuations. Before Bachelier, almost nobody modelled this uncertainty head-on.

### Method

Bachelier modelled price changes as the accumulation of many small independent shocks, which gives a continuous-time **random walk**, what would later be called Brownian motion. In his model, price increments follow a zero-mean Gaussian distribution whose variance grows linearly with time:

$$ X_{t+\Delta}-X_t \sim \mathcal N(0,\;\sigma^2\Delta),\qquad \mathrm{Var}(X_t-X_0)=\sigma^2 t $$

A profound conclusion follows at once: **the optimal forecast equals the current value**:

$$ \mathbb E[X_{t+s}\mid \mathcal F_t]=X_t $$

That is, given all the information $$\mathcal F_t$$ available up to time $$t$$, the conditional expectation of the future price is today's price. This is the embryo of the **martingale**: the predictable part has already been absorbed into the price, and what remains is purely unpredictable random fluctuation. From this he also derived a formula for option prices, connected to the solution of the diffusion equation.

### Impact

Bachelier not only brought the language of probability into financial modelling; mathematically, he wrote down the distributional properties of Brownian motion and their link to the diffusion equation **five years before Einstein**. His ideas on option pricing are a distant ancestor of the Black–Scholes formula more than half a century later. "Best forecast = current price" also became the earliest mathematical statement of market efficiency.

### Significance and outlook

The thesis was long ignored, until it was rediscovered in the 1950s by Samuelson and others and hailed as the founding work of mathematical finance. It was the first to tie together stochastic processes, martingales and the diffusion equation: the [physical theory of Brownian motion](../brownian-motion/) was soon given by Einstein, its rigorous mathematical form became the [Wiener process](../brownian-motion/), and the general theory of martingales was completed by [Lévy](../levy/) and Doob. Corrections to "prices are approximately a random walk", such as heavy-tailed increments and jumps, lead on to [Lévy processes](../levy/), ARCH/GARCH and jump diffusions. Every model today that forecasts financial series by treating them as stochastic processes stands on this step taken by Bachelier.
