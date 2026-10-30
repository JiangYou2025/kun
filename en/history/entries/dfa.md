---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1994 · Physics"
permalink: /en/history/e/dfa/
title: "Detrended Fluctuation Analysis (Peng et al., 1994)"
lead: "Heartbeats, DNA and stock prices all hide “long-range memory”, but slow trends can disguise it. Peng's recipe: first subtract the trend segment by segment, then measure how the fluctuations grow with scale."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Prologue · Interdisciplinary roots](../../foundations/).

### Background

Many natural and physiological series exhibit **long-range correlation**: today's fluctuations remain statistically linked to fluctuations from long ago, and the autocorrelation function decays slowly as a power law rather than dropping exponentially to zero. This kind of "fractal" behaviour shows up again and again in heart rate, DNA base sequences, river flows and financial returns. The classic tools statistical physics offers to characterize it are the Hurst exponent and rescaled range (R/S) analysis. But real data almost always carry slowly drifting **non-stationary trends** on top (baseline drift, external forcing), and these badly contaminate estimates of long-range correlation.

### The problem

Estimating long-range correlation directly on the raw series cannot tell "genuine intrinsic long-range correlation" apart from "spurious correlation manufactured by an external non-stationary trend" — a trend makes a series look as if it had more "memory" than it really has. **Can one design a scaling measure that is robust to non-stationary trends, and cleanly extract the intrinsic power-law long-range correlation from the trend contamination?**

### Other currents of the time (and their limits)

- **Rescaled range (R/S) analysis (the Hurst school)**: the classic way to estimate the Hurst exponent, but very sensitive both to non-stationary trends and to short-range correlation, often giving biased or even misleading results.
- **Power-spectrum scaling (spectral exponent $$\beta$$)**: estimates scaling from the power law of the low-frequency spectrum, $$S(f)\sim f^{-\beta}$$. Trends inject a great deal of spurious power at low frequencies, contaminating exactly the most important band.
- **Direct autocorrelation fitting**: under long-range correlation the autocorrelation itself decays extremely slowly and has a large estimation variance; with a trend added it becomes nearly unusable.

### The method

The trick of DFA is "integrate first, detrend piece by piece, then measure the fluctuation". Given a series $$x_k$$ with its mean removed, first build the cumulative profile (treating the series as a random walk):

$$ Y(i)=\sum_{k=1}^{i}\big(x_k-\bar{x}\big) $$

Cut $$Y$$ into non-overlapping segments of length $$n$$, fit the local trend $$Y_n(i)$$ in each segment with a polynomial (a straight line in the simplest case) and subtract it — this step **removes the local trend**. Then compute the root-mean-square fluctuation of the detrended residual:

$$ F(n)=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\big[\,Y(i)-Y_n(i)\,\big]^2} $$

Repeat for a range of window lengths $$n$$. If there is power-law scaling

$$ F(n)\sim n^{\alpha} $$

then $$\log F(n)$$ against $$\log n$$ is a straight line on a log-log plot, and its slope is the scaling exponent $$\alpha$$. Its meaning is intuitive: $$\alpha=0.5$$ means no long-range correlation (white-noise type); $$0.5<\alpha<1$$ means persistent long-range positive correlation; $$\alpha>1$$ means stronger, non-stationary correlation; and $$\alpha<0.5$$ means anti-persistence. The higher the polynomial order, the higher the order of trend that can be removed.

### Results

Because it removes the trend segment by segment, DFA is far more robust than R/S and spectral methods to superimposed non-stationary drift, and it can reliably isolate intrinsic long-range correlation from real data that contain trends. Peng and colleagues first used it to reveal long-range correlation in DNA sequences and in heart-rate variability; it was then widely applied to physiological signals (distinguishing healthy from pathological heart rhythms), climate, earthquakes, financial volatility and more, and was extended into **multifractal DFA (MF-DFA)**.

### Significance and outlook

DFA turned "fractality / long-range memory" from a theoretical concept into a diagnostic that can be computed reliably on non-stationary real-world series, and it became one of the standard tools of scaling analysis in complex systems. It embodies an important philosophy of time series: **first strip away the trend, the non-stationary component, and only then examine the scaling structure of the remaining fluctuations** — a direct descendant of detrending ideas such as differencing, filtering and decomposition. It is also a reminder that any measure of "memory" must rest on an honest treatment of the trend.
