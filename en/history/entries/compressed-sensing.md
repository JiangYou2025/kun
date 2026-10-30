---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2006 · Control / Communications"
permalink: /en/history/e/compressed-sensing/
title: "Compressed Sensing (Donoho · Candès · Tao, 2006)"
lead: "Nyquist says you must sample densely enough. But what if the signal is sparse to begin with? With far fewer random measurements than Nyquist requires, followed by ℓ1 minimization, exact reconstruction turns out to be possible."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

For more than half a century the golden rule of signal processing was the **Shannon–Nyquist sampling theorem**: to reconstruct a signal of bandwidth $$ B $$ without distortion, the sampling rate must be at least $$ 2B $$. The paradigm of "sample densely first, then compress by discarding most coefficients" (JPEG, for example) looked wasteful: if only a few large coefficients are kept in the end, why acquire so many samples in the first place? In 2006, Donoho and Candès–Romberg–Tao published foundational papers almost simultaneously, proving that if a signal is **sparse** in some basis, it can be reconstructed exactly from **far fewer measurements than Nyquist requires**. **Compressed sensing** was born.

### The problem

Many natural and man-made signals (images, audio, radar echoes, time-series spectra) have only a few nonzero coefficients in a suitable transform domain (Fourier, wavelets); they are **sparse**. Could "sampling" and "compression" be merged into one, so that **compressed information is acquired directly**? Mathematically: given $$ m \ll n $$ linear observations $$ y = \Phi x $$, the underdetermined system has infinitely many solutions. How can the sparse $$ x $$ be recovered uniquely?

### Other approaches of the time (and their limits)

- **Classical Nyquist sampling**: foolproof, but it **does not exploit sparsity**, causing large amounts of redundant sampling and later discarding for sparse signals.
- **Direct $$ \ell_0 $$ minimization (find the sparsest solution)**: correct in theory, but an **NP-hard** combinatorial optimization, and thus not computable.
- **Greedy methods such as matching pursuit**: fast, but lacking theoretical guarantees of global optimality and exact reconstruction, and prone to suboptimal solutions.

### Method

Let the original signal $$ x\in\mathbb{R}^n $$ be $$ k $$-sparse in some basis (only $$ k $$ nonzero entries, $$ k\ll n $$). Sample it with an $$ m\times n $$ **random measurement matrix** $$ \Phi $$:

$$ y = \Phi x,\qquad m \ll n $$

Directly seeking the sparsest solution $$ \min \|x\|_0 $$ is infeasible. The key breakthrough is to relax it with the **convex $$ \ell_1 $$ norm**, which recovers the sparse solution exactly and is a convex optimization (linear or second-order cone programming) that can be solved efficiently:

$$ \min_{x}\ \|x\|_1 \quad \text{s.t.}\quad \Phi x = y $$

A sufficient condition for success is that $$ \Phi $$ satisfies the **Restricted Isometry Property (RIP)**: there is a small $$ \delta_k\in(0,1) $$ such that for every $$ k $$-sparse vector

$$ (1-\delta_k)\|x\|_2^2 \le \|\Phi x\|_2^2 \le (1+\delta_k)\|x\|_2^2 $$

that is, $$ \Phi $$ approximately preserves the length of sparse vectors and does not "alias" different sparse signals onto each other. Random Gaussian or Bernoulli matrices satisfy the RIP with overwhelming probability, and the number of measurements needed is only $$ m = O\big(k\log(n/k)\big) $$, far smaller than $$ n $$.

### Impact

Compressed sensing brought a paradigm shift of "trading computation for sampling": much shorter MRI scan times, the single-pixel camera, sparse radar and arrays, sub-Nyquist spectrum sensing and wideband cognitive radio all became reality. In time series and system identification it underpins **sparse spectral estimation**, signal completion with missing data, and "sparsity + physics" identification of dynamical systems (SINDy, for instance, which uses sparse regression to discover governing equations from data, belongs to the same line of thought).

### Significance and outlook

The deep significance of compressed sensing is that it elevated "**sparsity is a prior that sampling can exploit**" to a general principle, and proved that the convex $$ \ell_1 $$ relaxation achieves the $$ \ell_0 $$ goal under the RIP, closing the loop perfectly between theory and algorithm. It shares the same mathematical core as sparse regression in statistics ([LASSO](../../../foundations/regularization/)) and profoundly influenced ideas of regularization in high-dimensional statistics and machine learning. In time series, from spectral compression and missing-data completion to the discovery of sparse dynamical systems, wherever a problem involves "few measurements and sparse structure", the echo of the 2006 breakthrough can be heard.
