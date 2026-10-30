---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1986 · Computing"
permalink: /en/history/e/garch/
title: "The GARCH Model (Bollerslev, 1986)"
lead: "ARCH needs a long tail of lags to remember volatility. Bollerslev gave the variance its own “yesterday”, and with just three parameters it remembered the long-lasting storms."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 6 · Volatility and Cointegration](../../06/).

### Background

[Engle's ARCH](../arch/) was the first to make the conditional variance a time-varying, estimable model, elegantly capturing volatility clustering. But fitting it to real financial data exposed an engineering problem: volatility in real markets is **very persistent** — the effect of a large shock takes many periods to die away. To express such long memory, ARCH has to let the variance depend on squared residuals from many past periods, i.e. the order $$q$$ must be very large, which leads to **too many parameters**, unstable estimates and frequent violations of the non-negativity constraints. How could one keep the long memory while cutting down the number of parameters?

### The problem

In the ARCH framework, the variance can only be a weighted sum of squared residuals over a number of past periods. Approximating a slowly decaying long-range weighting with a pure moving sum requires that sum to be very long. **Could some recursive structure be introduced that lets the variance "remember" its own history, so that long-range clustering is expressed with very few parameters?**

### Other approaches of the time (and their limits)

- **High-order ARCH(q)**: simply increase $$q$$. This can approximate long memory, but the number of parameters grows linearly with $$q$$; estimation becomes hard, constraints are difficult to satisfy and the risk of overfitting is high.
- **Fixed-window moving variance**: use the sample variance over a recent window. It weights all data in the window equally and forgets abruptly outside it, lacking a smooth decay structure.
- **Stochastic volatility (SV)**: the variance is driven by an independent latent process. Flexible, but with latent variables, maximum likelihood estimation was still intractable at the time.

### Method

Bollerslev proposed generalized ARCH (GARCH). The key step is to let the conditional variance **also depend on its own lagged values**. The most widely used GARCH(1,1) is:

$$ \sigma_t^2 = \omega + \alpha\,\varepsilon_{t-1}^2 + \beta\,\sigma_{t-1}^2,\qquad \omega>0,\;\alpha\ge 0,\;\beta\ge 0 $$

Only three parameters: $$\omega$$ is the baseline variance level, $$\alpha$$ measures the impact of the latest shock, and $$\beta$$ carries the previous period's variance into the current one. The recursion can be unrolled step by step into an **exponentially decaying weighting** of all past squared residuals — so a GARCH(1,1) is equivalent to an ARCH of infinite order, packing long-range memory into three parameters. $$\alpha+\beta$$ measures volatility persistence: the closer it is to 1, the more slowly shocks decay and the more stubborn the clustering. When $$\alpha+\beta<1$$ the process is covariance-stationary, with **unconditional variance**

$$ \mathrm{Var}(\varepsilon_t)=\frac{\omega}{1-\alpha-\beta} $$

The model is likewise estimated by maximum likelihood under a conditionally normal (or Student-t) assumption.

### Impact

With a minimal parameterization, GARCH(1,1) precisely captures the volatility clustering and persistence of returns on stocks, exchange rates and interest rates. It became the most cited and most used volatility model in financial econometrics, and is practically the default starting point for risk management, option pricing and VaR computation. It is so often "good enough" in empirical fits that "GARCH(1,1)" has become an industry catchphrase.

### Significance and outlook

GARCH compressed the long lags of ARCH into three parameters with a single recursive term, embodying the modelling wisdom of "**trading an autoregressive structure for parsimony**" — exactly mirroring the relationship of AR to MA at the level of the mean. It spawned a vast family: EGARCH and GJR-GARCH for the leverage effect, FIGARCH for long memory, multivariate DCC-GARCH, and more. To this day, deep learning volatility models often use GARCH as their baseline and point of comparison, which shows how foundational this step was.
