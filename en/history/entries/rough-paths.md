---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1998 · Mathematics"
permalink: /en/history/e/rough-paths/
title: "Rough Paths and Path Signatures (Lyons, 1998)"
lead: "Can all the information in a path be compressed into a set of numbers? With the “signature” spanned by iterated integrals, Lyons forged a universal key for sequences."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Classical stochastic analysis (the Itô integral) can integrate along paths such as Brownian motion, but it is essentially probabilistic and makes stringent demands on the regularity of paths. Faced with driving signals that are "rougher" than Brownian motion and have more complex correlation structure, the traditional theory struggles to provide a **pathwise**, deterministic framework for solving differential equations. In 1998 Lyons proposed **rough path theory**, establishing a rigorous and robust solution theory for differential equations driven by highly irregular signals. Its by-product — the **path signature** — later became a powerful feature for analysing sequential data.

### The problem

Problems on two levels are intertwined. On the analytical level: when the driving path is very rough, the classical definition of the "integral" $$\int Y\,dX$$ breaks down — **how can $$dY=f(Y)\,dX$$ be defined and solved stably?** On the data level: **how can a multidimensional, ordered, variable-length path, which may be reparameterized arbitrarily, be encoded as a finite, structured set of features that fully characterizes its shape?**

### Other approaches of the time (and their limits)

- **Itô / stochastic calculus**: enormously successful for semimartingales, but it depends on probabilistic structure, is not pathwise, and limits how rough the signal may be, making it hard to treat more general driving signals in a unified way.
- **Hand-crafted time-series features (mean, variance, Fourier coefficients, etc.)**: interpretable but piecemeal, sensitive to sampling rate, start and end points and parameterization, and lacking completeness or any unified theoretical guarantee.
- **Alignment methods such as dynamic time warping (DTW)**: they can compare the shapes of sequences, but do not provide a representation that can be linearly combined or fed as a general-purpose feature into downstream models.

### Method

Given a path $$X:[0,T]\to\mathbb{R}^d$$, its **signature** is the infinite sequence of tensors made up of the **iterated integrals** of every order:

$$ S(X)_{0,T}=\Big(1,\;\big\{\textstyle\int_0^T dX^{i}\big\}_i,\;\big\{\textstyle\iint_{0<s<t<T} dX^{i}_s\,dX^{j}_t\big\}_{i,j},\;\dots\Big) $$

where the order-$$k$$ term is a tensor with components

$$ S(X)^{\,i_1 i_2\cdots i_k}_{0,T}=\idotsint_{0<t_1<\cdots<t_k<T} dX^{i_1}_{t_1}\,dX^{i_2}_{t_2}\cdots dX^{i_k}_{t_k} $$

The signature has several decisive properties: it is **invariant to reparameterization** (independent of the speed at which the path is traversed, caring only about its geometric shape); it satisfies Chen's identity (the signature of concatenated paths is the tensor product of the signatures of the pieces), which makes incremental computation easy; and, once trivial time augmentation is removed, the signature **determines the path almost uniquely**. Most important is its **universal nonlinearity**: any continuous functional on paths can be approximated arbitrarily well by a **linear combination** of the signature's terms — which means that taking the signature and then attaching a linear model can, in principle, express any (smooth) function of the path. In practice, only a finite-dimensional signature truncated at some order is used as the feature set.

### Impact

Mapping sequences to (truncated) signatures and then attaching a simple model has delivered strong and robust performance on tasks such as Chinese handwriting recognition, financial time series, medical signals and machine-learning competitions. Signature features are naturally suited to irregular sampling, missing values and unequal lengths, and come with solid mathematical guarantees, making them a distinctive and competitive kind of sequence representation.

### Significance and outlook

Rough path theory is rooted at one end deep in stochastic analysis (providing a pathwise framework for solving stochastic differential equations; Hairer's regularity structures were also inspired by it), and reaches at the other end into machine learning, placing "universal features of sequences" on rigorous mathematical ground. Combined with neural networks, it has given rise to **signature kernels**, **deep signature networks** and even [neural controlled differential equations (Neural CDEs)](../neural-cde/) — the latter make "continuous dynamics driven by a path" the very core of a sequence model. From pure mathematics to sequence learning, the signature provides a rare key that combines theoretical completeness with engineering practicality.
