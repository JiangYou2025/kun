---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2005–10 · Physics"
permalink: /en/history/e/koopman-dmd/
title: "The Koopman Operator and DMD (Mezić · Schmid, 2005–10)"
lead: "Can nonlinear dynamics “become linear”? The price is lifting to infinite dimensions: let the operator act on observable functions, and DMD then digs its coherent modes and frequencies out of the data."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Nonlinear dynamical systems are hard because there is no superposition principle; spectra, modes and frequencies, the powerful tools of the linear world, seem out of reach. Yet as early as 1931, **Koopman** showed that any dynamical system (however strongly nonlinear) corresponds to a **linear** operator acting on a **space of observable functions** — at the price that this space is usually **infinite-dimensional**. The idea lay dormant for decades until 2004–2005, when Mezić and others revived it by combining it with spectral analysis and data-driven methods; in 2008–2010 Schmid proposed **dynamic mode decomposition (DMD)**, a practical algorithm for extracting coherent modes from snapshots of high-dimensional flow fields. The two quickly merged, becoming a powerful tool for analysing high-dimensional spatio-temporal series in fluids, climate, neuroscience and beyond.

### The problem

Experiments and simulations produce huge volumes of high-dimensional series (for example, flow fields with millions of degrees of freedom per frame), yet these are often dominated by a few **coherent structures**. How can the **spatial modes, growth/decay rates and oscillation frequencies** of these structures be extracted from data **without relying on the governing equations**? Classical [PCA/EOF](../../../foundations/pca/) ranks only by energy and has no temporal-dynamical meaning; Fourier analysis assumes stationarity and global periodicity. What was needed was a decomposition that **binds spatial patterns to temporal frequencies**.

### Other approaches of the time (and their limits)

- **POD/PCA (proper orthogonal decomposition)**: gives the optimal low-dimensional basis by variance/energy, but its modes mix several frequencies and carry no dynamical information (growth rates/frequencies).
- **Global Fourier spectra**: give frequencies, but the modes are full-field sinusoids, unable to describe localized coherent structures, and stationarity is required.
- **Equation-based eigenanalysis**: exact, but requires known governing equations that can be linearized, and is helpless for purely data-driven or unknown systems.

### Method

Let a state $$ x \in \mathbb{R}^n $$ evolve as $$ x_{t+1} = F(x_t) $$ (where $$ F $$ may be nonlinear). The **Koopman operator** $$ \mathcal{K} $$ acts on observable functions $$ g $$, making their evolution along trajectories **linear**:

$$ (\mathcal{K} g)(x) = g\big(F(x)\big) $$

Although $$ \mathcal{K} $$ is linear, it is infinite-dimensional; its eigenvalues, eigenfunctions and modes characterize the global dynamics of the system. **DMD** is its data-driven finite-dimensional approximation: collect the snapshot matrices $$ X=[x_1,\dots,x_{m-1}] $$ and $$ X'=[x_2,\dots,x_m] $$, and find the best linear operator $$ A $$ such that

$$ X' \approx A\,X,\qquad A = X'\,X^{+} $$

($$ X^{+} $$ is the pseudo-inverse; in practice the solution is computed after reducing dimension with an SVD). Eigendecomposing $$ A $$, $$ A\phi_j=\lambda_j\phi_j $$: each **DMD mode** $$ \phi_j $$ is a spatial structure, and its eigenvalue $$ \lambda_j $$ gives both a **growth rate** and an **oscillation frequency** — $$ |\lambda_j| $$ determines decay/growth and $$ \arg\lambda_j $$ determines the frequency. The series is then reconstructed as

$$ x_t \approx \sum_j \phi_j\, \lambda_j^{\,t}\, b_j $$

This splits high-dimensional spatio-temporal data into a superposition of "spatial mode × complex-exponential time evolution" — exactly modal analysis from the linear world, but applied to data from nonlinear systems.

### Impact

DMD makes it possible to extract the dominant **coherent modes and frequencies** automatically from high-dimensional series in turbulence, combustion, climate, EEG and more, without governing equations. It spawned a whole set of extensions: Extended DMD, Hankel-DMD (for short observations), DMD with control (DMDc), and deep versions that learn Koopman-invariant subspaces with neural networks. In engineering it serves three purposes at once: dimensionality reduction, spectral analysis and short-term forecasting.

### Significance and outlook

The revolutionary aspect of Koopman–DMD is **trading dimension for linearity**: instead of wrestling with nonlinearity head-on in the original state space, it moves to the high-dimensional (even infinite-dimensional) space of observable functions and enjoys the full spectral toolkit of linear operators. This echoes the spirit of [echo state networks](../echo-state-network/) ("high-dimensional random expansion + linear readout") and of kernel methods. Today it is one of the core paradigms of data-driven dynamical systems, interpretable time series modelling and the analysis of chaotic systems ([Lorenz](../lorenz-chaos/)), and it keeps inspiring the fundamental question of "how to find a good set of coordinates for a nonlinear system".
