---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1944 · Mathematics"
permalink: /en/history/e/ito/
title: "Calculus for a Random World (Itô, 1944)"
lead: "The paths of Brownian motion are nowhere differentiable, and ordinary calculus breaks down there. Itô built a new chain rule that sprouts an extra half second-order term, and continuous-time stochastic modelling finally had an engine."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Bachelier in 1900, Einstein in 1905 and Wiener in 1923 each described **Brownian motion** from a different angle: a random path that is continuous yet extremely irregular. People wanted to use it to write "random versions of differential equations", $$dX_t=\mu\,dt+\sigma\,dW_t$$, to describe continuous systems constantly perturbed by noise. But Brownian paths are **continuous everywhere yet differentiable nowhere**, and $$dW_t$$ is not a differential in the ordinary sense. In 1944 the Japanese mathematician Kiyosi Itô provided the stochastic integral and calculus that made this notation rigorous.

### The problem

The cornerstone of ordinary calculus is the chain rule $$df=f'(x)\,dx$$, which implicitly treats $$(dx)^2$$ as a negligible higher-order term. But for Brownian motion, **$$(dW_t)^2$$ cannot be neglected** — in the mean-square sense it equals $$dt$$. So: how should $$\int H_t\,dW_t$$ be defined to be well behaved? What should the differential of a composite function $$f(W_t)$$ look like? **When the second-order term no longer vanishes, how must calculus be rewritten?**

### Other approaches of the time (and their limits)

- **Classical pathwise integration (Riemann–Stieltjes)**: try to integrate directly along each sample path. It fails — Brownian paths have infinite total variation almost surely, so the classical integral simply does not converge.
- **Stratonovich's symmetric integral (somewhat later)**: evaluates at the midpoint, preserving the ordinary chain rule and being more natural geometrically, but it **breaks the martingale property** and the causal adaptedness of "the integrand depends only on the past", making it less clean than Itô's for the concepts of probability and finance.
- **Formally ignoring the second-order term**: physicists often simply applied the classical rules. This produces a systematic bias — what is missed is precisely the $$\tfrac12\sigma^2$$ correction term.

### Method

Itô defined the integral as the mean-square limit of left-endpoint sums for **adapted integrands that do not look into the future**, so that $$\int_0^t H_s\,dW_s$$ is a martingale. His central result is **Itô's lemma**: if $$dX_t=\mu_t\,dt+\sigma_t\,dW_t$$, then for a sufficiently smooth $$f$$,

$$ df(t,X_t)=\Big(f_t+\mu_t f_x+\tfrac12\sigma_t^2 f_{xx}\Big)dt+\sigma_t f_x\,dW_t $$

Compared with the classical chain rule, **the extra term $$\tfrac12\sigma_t^2 f_{xx}\,dt$$ that appears out of nowhere** is exactly the second-order contribution of $$(dW_t)^2=dt$$. Applying it to geometric Brownian motion $$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$$ with $$f=\ln S$$ gives the explicit solution

$$ S_t=S_0\exp\!\Big(\big(\mu-\tfrac12\sigma^2\big)t+\sigma W_t\Big) $$

The drift correction $$-\tfrac12\sigma^2$$ is a direct consequence of the extra term in Itô's lemma.

### Impact

Itô calculus turned "stochastic differential equations" into a tool that can be rigorously solved and whose expectations can be computed. With the martingale property, adaptedness and the second-order correction forming a single whole, the analysis of stochastic processes gained a calculus on a par with classical analysis. Geometric Brownian motion became the standard continuous-time stochastic model; the Itô integral became the common language of the later [Feynman–Kac formula](../feynman-kac/), stochastic control and filtering theory.

### Significance and outlook

This calculus is the engine of continuous-time stochastic modelling. The [Black–Scholes option pricing](../black-scholes/) of 1973 was derived precisely by applying Itô's lemma to geometric Brownian motion — the famous diffusion term $$\tfrac12\sigma^2 S^2\,\partial_{SS}$$ is a direct descendant of that half second-order term from 1944. From financial engineering to filtering, from population genetics to the stochastic-differential-equation generative models of machine learning (diffusion models), wherever there is "continuous time + noise-driven dynamics", the underlying language is Itô's.
