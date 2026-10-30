---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1963 · Mathematics"
permalink: /en/history/e/mandelbrot/
title: "Heavy Tails, Fractals and Long Memory (Mandelbrot, 1963)"
lead: "The booms and crashes of cotton prices were far more violent and more frequent than the bell curve allows. From this, Mandelbrot tore open the Gaussian assumption and brought heavy tails, fractals and long memory into financial time series."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the first half of the 20th century, the default assumption in financial and economic modelling was **Gaussian**: price changes are normally distributed, independent and of finite variance. This was the cornerstone of the random-walk tradition since Bachelier, and later one of the premises of [Black–Scholes](../black-scholes/). Normality implies that extreme events almost never happen, and that the standard deviation suffices to describe risk. Mandelbrot obtained a long series of **cotton prices** spanning a century and set out to test this assumption.

### The problem

The data did not cooperate with the Gaussian. The distribution of price returns had **a tall, sharp peak** and **long, heavy tails**: violent swings that should occur once in ten thousand years came every few years. Moreover, volatility came in **clusters**: large moves were often followed by large moves. **If extreme events are far more frequent than the normal distribution predicts, then every risk measure based on normality and finite variance systematically underestimates risk.** This was a question about the very foundations of modelling.

### Other approaches of the time (and their limits)

- **Gaussian random walk**: mathematically elegant and convenient for derivations, but it underestimates the tails and cannot explain how often booms and crashes occur.
- **The independent-increments assumption**: returns at different times are taken to be uncorrelated. Yet the data show long-range dependence (long memory) in volatility, so independence is too strong an assumption.
- **A purely deterministic view of cycles and trends**: tries to fit the market with regular curves, but ignores the roughness and self-similarity of the price path itself.

### Method

Mandelbrot proposed describing returns with **Lévy stable distributions**. A stable distribution is parameterized by an index $$\alpha\in(0,2]$$, and its tails decay as a power law:

$$ \mathbb{P}(|X|>x)\sim C\,x^{-\alpha},\qquad 0<\alpha<2 $$

When $$\alpha<2$$ the variance diverges, which is the source of the heavy tails ($$\alpha=2$$ reduces to the Gaussian). He went on to develop **fractals** and **fractional Brownian motion** $$B_H(t)$$ to describe long memory, whose covariance is governed by the Hurst exponent $$H$$:

$$ \mathbb{E}\!\left[B_H(t)\,B_H(s)\right]=\tfrac{1}{2}\left(|t|^{2H}+|s|^{2H}-|t-s|^{2H}\right) $$

When $$H>1/2$$ the increments are positively correlated and show persistent long memory; when $$H<1/2$$ they are anti-persistent. The price path is thus a **self-similar fractal**: zoom in on any segment and its statistical shape resembles the whole, with no scale at which it becomes "smooth enough".

### Impact

Heavy tails and long memory became core topics in financial modelling from then on. Mandelbrot's work explained why crises occur far more often than normality would suggest, and brought a respect for the tails into risk management. Although pure stable distributions are hard to apply directly because of their infinite variance, they gave rise to a series of more workable successor models.

### Significance and outlook

This thread leads to two major branches: one is the finite-variance path of describing volatility clustering with [ARCH/GARCH](../arch/); the other brings long memory into the mean and the volatility via **ARFIMA** (fractional differencing) and, more recently, [rough volatility](../rough-volatility/) (modelling the rough paths of volatility with fractional Brownian motion with $$H<1/2$$). Mandelbrot's fundamental contribution was to make people accept that the **roughness, heavy tails and self-similarity** of markets are the norm rather than anomalies: a worldview of modern financial time series that endures to this day.
