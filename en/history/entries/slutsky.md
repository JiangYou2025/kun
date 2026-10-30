---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1927 · Mathematics"
permalink: /en/history/e/slutsky/
title: "Spurious Cycles from Summed Randomness (Slutsky, 1927)"
lead: "Keep taking moving sums of pure noise and fluctuations strikingly like business cycles emerge — with this counterexample Slutsky warned that the cycles you see may be nothing but ghosts left behind by filtering."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 1 · Autoregression](../../01/).

### Background

In the 1920s, economists were fascinated by the "business cycle": crises, booms and depressions seemed to recur with some rhythm, and many scholars believed that a definite cycle length lay hidden behind them, waiting to be discovered. In statistical practice, it was customary to apply a **moving average** to the raw data to "smooth out" short-term disturbances and bring out trends and cycles. At the same time, [Yule](../yule-ar/) was using autoregression to explain the quasi-periodicity of sunspots. The Ukrainian statistician Slutsky approached the same puzzle from another direction.

### The problem

A pointed suspicion: are those "cycles" that are observed and named over and over really a property of the economic system itself, or are they **manufactured by our own processing**? Could routine operations such as smoothing, differencing and moving averages generate fluctuations out of nothing? If so, a great deal of "cycle-discovering" research was built on sand.

### Other approaches of the time (and their limits)

- **The deterministic-cycle school**: believed in business cycles of fixed length and tried to capture them with harmonics or periodograms. Its limit was treating data processing as a neutral lens, overlooking the fact that filtering itself shapes the data.
- **[Yule](../yule-ar/)'s autoregressive view (the same year)**: cycles arise from an internal restoring structure excited by noise. Profound, but it emphasizes that "the system has a genuine quasi-period", which complements rather than replaces Slutsky's emphasis that "the cycle may be a pure artifact".
- Only together are the two complete: a cycle can stem from real dynamics or from filtering — and one must be able to tell them apart.

### Method

Slutsky took a series of **independent, identically distributed random numbers** (pure noise) and did nothing but form linear weighted sums of them, obtaining a new series:

$$ X_t = \sum_{j=0}^{q} b_j\,\varepsilon_{t-j},\qquad \varepsilon_t \sim \mathrm{WN}(0,\sigma^2) $$

This is exactly the structure later called **MA(q)** (moving average). The key finding: even though the input has no periodicity at all, the output $$X_t$$ shows smooth, regular fluctuations. The reason lies in the frequency domain: summation is equivalent to a **low-pass filter**, whose frequency response

$$ H(\omega) = \sum_{j=0}^{q} b_j\, e^{-i\omega j} $$

suppresses high frequencies and amplifies a band of low-to-middle frequencies, so the flat power spectrum of white noise is "shaped" into a spectrum with a peak — which looks just as if there were some dominant period. Slutsky thereby proved that **linear filtering can make quasi-periodicity "emerge" from no periodicity at all**, a phenomenon later known as the **Slutsky–Yule effect**.

### Impact

The conclusion was unsettling and highly illuminating: routine preprocessing such as moving averages and differencing introduces spurious cycles, and many solemnly reported "business cycles" may well be mere filtering artifacts. It sounded an alarm for the entire empirical study of cycles — before claiming to have found a cycle, one must rule out the contribution of the processing itself.

### Significance and outlook

Slutsky and [Yule](../yule-ar/), from opposite ends, jointly laid the foundation of the modern view of linear stochastic processes: a series is the product of white noise shaped by a linear system. The MA and AR structures were unified in 1938 by the [Wold decomposition](../wold/), and then flowed into the ARMA/ARIMA framework of [Box–Jenkins](../box-jenkins/). The longer-lasting legacy is a methodological vigilance: faced with any "cycle" or "signal", first ask — does this belong to the data, or did my processing put it there? This caution has run through a century of spectral analysis and filtering practice since.
