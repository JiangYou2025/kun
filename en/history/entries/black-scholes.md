---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1973 · Mathematics"
permalink: /en/history/e/black-scholes/
title: "The Option Pricing Formula (Black · Scholes · Merton, 1973)"
lead: "Replicate an option with a continuously rebalanced hedging portfolio, and its price no longer depends on attitudes to risk. Black, Scholes and Merton pushed Itô calculus into a single PDE and opened a new era in derivative pricing."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Options, the right to buy or sell an underlying asset at an agreed price in the future, had been traded for a long time, but there was no convincing answer to the question "what exactly is one worth?". Earlier attempts usually had to assume investors' risk preferences or their expectations of future returns, and opinions diverged widely. By then [Itô calculus](../ito/) had provided rigorous tools for continuous-time stochastic processes, and geometric Brownian motion was being used to describe stock price paths. Everything was in place; only the final step was missing.

### The problem

The core difficulty was **risk preference**: an option's payoff depends on an uncertain future stock price, so it seemed one had to know how much compensation the market demands for bearing risk before the option could be priced. But different investors have different preferences; would the price then differ from person to person? **Can one give an objective option price that does not depend on anyone's subjective preferences?**

### Other approaches of the time (and their limits)

- **Utility / equilibrium pricing**: derives prices from investors' utility functions and market equilibrium. It requires preference parameters that are hard to observe, and the conclusions are not unique.
- **Discounted expected payoff**: discounts the option's expected future payoff at some rate of return. But "which discount rate to use" smuggles the risk-premium problem straight back in.
- **Purely statistical fitting of historical option prices**: strongly empirical, but lacking a no-arbitrage theoretical foundation, so it is hard to extrapolate to new contracts.

### Method

The key insight is **replication by dynamic hedging**. Let the stock price follow geometric Brownian motion $$dS=\mu S\,dt+\sigma S\,dW$$, and expand the option price $$V(S,t)$$ with **Itô's lemma**:

$$ dV=\frac{\partial V}{\partial t}\,dt+\frac{\partial V}{\partial S}\,dS+\frac12\,\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\,dt $$

Build a portfolio that holds the option and sells short $$\partial V/\partial S$$ shares of stock. The random term $$dW$$ cancels exactly, and the portfolio is instantaneously **risk-free**. No arbitrage then requires it to earn exactly the risk-free rate $$r$$, which yields the **Black–Scholes partial differential equation**:

$$ \frac{\partial V}{\partial t}+\frac12\,\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV=0 $$

Note that the equation **contains no $$\mu$$**: the real drift has disappeared, and the price does not depend on risk preferences. For a European call it can be solved in closed form ($$N(\cdot)$$ is the standard normal distribution function):

$$ C=S_0\,N(d_1)-K e^{-rT}N(d_2),\qquad d_{1,2}=\frac{\ln(S_0/K)+(r\pm\tfrac12\sigma^2)T}{\sigma\sqrt{T}} $$

### Impact

A formula that needs only five quantities, $$S_0,K,r,T,\sigma$$, and whose only unknown parameter is the volatility $$\sigma$$, turned derivative pricing from guesswork into computable engineering. It drove the explosive growth of options markets and became a founding result of financial engineering; Scholes and Merton received the 1997 Nobel Prize in Economics for it.

### Significance and outlook

For time series, Black–Scholes pushed **stochastic process modelling** into the heart of financial practice, and it also exposed the weak points of its assumptions: constant volatility $$\sigma$$ and Gaussian returns. The market voted against them with the "volatility smile". The efforts to fix this are exactly the main line that followed: [ARCH/GARCH](../arch/) to describe time-varying volatility, stochastic volatility and [rough volatility](../rough-volatility/) to describe more realistic volatility paths, while the efficient computation of sensitivities (the Greeks) gave rise to applications of [Malliavin calculus](../malliavin/). One PDE opened the whole era of quantitative finance.
