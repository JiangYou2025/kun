---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1983 · Physics"
permalink: /en/history/e/correlation-dimension/
title: "The Correlation Dimension (Grassberger · Procaccia, 1983)"
lead: "Is a signal low-dimensional chaos or high-dimensional noise? Count “how many pairs of points lie close to each other” in phase space, and the fractal dimension emerges from a scaling law."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

[Takens's delay embedding](../takens/) let people reconstruct phase space from a single scalar series and "draw" the attractor of a [chaotic](../lorenz-chaos/) system. But reconstruction immediately raises a sharper question of discrimination: is the tangled trajectory in front of us **low-dimensional deterministic chaos** governed by a handful of degrees of freedom, or essentially **high-dimensional random noise**? Both can look "messy" when plotted, and the eye cannot tell them apart. A quantitative indicator was needed, the **dimension** of the attractor, to say how many effective degrees of freedom it "occupies". [Mandelbrot](../mandelbrot/)'s fractal geometry supplied the language of "non-integer dimension", but how to compute that dimension reliably from finite, noisy experimental data remained an open problem.

### The problem

The theoretical box-counting dimension requires dividing space into small boxes and counting them; in a high-dimensional phase space the amount of data needed grows exponentially with dimension, making it almost infeasible for experimental data. **Could an algorithm be designed to estimate the fractal dimension directly and robustly from a finite set of sampled points?**

### Other approaches of the time (and their limits)

- **Box-counting dimension**: clearly defined, but in high dimensions it needs astronomical numbers of data points and is sensitive to noise, so it rarely converges in experiments.
- **Eyeballing the attractor / spectral analysis**: judging by eye or from the Fourier spectrum. The spectrum of chaos is broadband and looks like that of noise, so the dimension cannot be distinguished quantitatively.
- **Lyapunov exponent estimation**: can determine whether there is sensitivity to initial conditions, but the algorithms of the time were fragile under noise and did not directly give a geometric dimension.

### Method

Grassberger and Procaccia proposed estimating the dimension with the **correlation integral**. Take $$N$$ points $$\{\mathbf{y}_i\}$$ in an $$m$$-dimensional reconstructed phase space and define the fraction of pairs of points closer than $$r$$:

$$ C(r) = \lim_{N\to\infty}\frac{2}{N(N-1)}\sum_{i<j}\Theta\big(r-\|\mathbf{y}_i-\mathbf{y}_j\|\big) $$

where $$\Theta$$ is the Heaviside step function (1 if the distance is less than $$r$$, 0 otherwise). For a fractal attractor, the correlation integral follows a power law for small $$r$$:

$$ C(r)\sim r^{D_2}\quad\Longrightarrow\quad D_2 = \lim_{r\to 0}\frac{\log C(r)}{\log r} $$

$$D_2$$ is the **correlation dimension**. In practice one plots $$\log C(r)$$ against $$\log r$$ and takes the slope of the straight line in the intermediate scaling range to obtain $$D_2$$. The key to discrimination: as the embedding dimension $$m$$ increases, the $$D_2$$ of **low-dimensional chaos** converges to a finite value (the degrees of freedom saturate), whereas the $$D_2$$ of **random noise** keeps growing with $$m$$ without saturating. This is the fingerprint that tells the two apart.

### Impact

The correlation-dimension algorithm is computationally cheap and needs far less data than box counting. It quickly became a standard tool of nonlinear time-series analysis, widely applied to fluid turbulence, lasers, ECG and EEG signals to determine whether a low-dimensional deterministic structure lies behind them. Together with Lyapunov exponents and the choice of embedding parameters, it formed the toolbox of experimental chaos.

### Significance and outlook

The Grassberger–Procaccia algorithm turned the fractal dimension from a purely mathematical concept into **a physical quantity that can be measured from data**, making "how many effective degrees of freedom does this signal have?" an empirically answerable question. Its limits were recognized later: finite data, noise and long-range correlations can produce spurious low-dimensional illusions, so results must be interpreted with care. But the idea it established, **inferring geometry from data through scaling laws**, has had a lasting influence, and it runs straight through to modern work that uses phase-space methods for nonlinear prediction, complexity measures and the discrimination between determinism and randomness.
