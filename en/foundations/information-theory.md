---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/information-theory/
title: "Information Theory"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Information theory uses concepts such as **entropy** to quantify "amount of information" and "uncertainty", and from them it derives theoretical limits on "the minimum number of bits needed to describe something" and "how well we can possibly predict". It was founded by Claude Shannon in 1948.

## Intuition

The core insight of information theory is: **information = the removal of uncertainty**.

- A message you already knew ("the sun will rise tomorrow") carries almost no information;
- a surprising message ("it will snow somewhere tomorrow, an event that had only a 1% chance") carries a great deal.

This suggests a way to quantify it: **the less likely an event, the more information it carries when it does occur**. Information theory turns this simple intuition into precise mathematics, so that we can "weigh" information, design compression and communication schemes, and define the [losses](../loss-function/) of [machine learning](../ml/).

## Mathematical formulation

**Self-information** (the information content of a single event):

$$
I(x)=-\log p(x)
$$

The smaller the probability, the larger $-\log p$, and the more information.

**[Entropy](../entropy/)** (the average uncertainty of a distribution, i.e. the expected self-information):

$$
H(X)=-\sum_i p_i\log p_i
$$

**[Cross-entropy](../cross-entropy/)** (the average cost of describing the true distribution $p$ with a distribution $q$):

$$
H(p,q)=-\sum_i p_i\log q_i
$$

**[KL divergence](../kl-divergence/)** (the difference between two distributions / the extra cost):

$$
D_{\mathrm{KL}}(p\parallel q)=\sum_i p_i\log\frac{p_i}{q_i}=H(p,q)-H(p)
$$

**Mutual information** (how much information two variables share):

$$
I(X;Y)=H(X)-H(X\mid Y)
$$

These quantities are tightly linked: entropy is the foundation, cross-entropy = entropy + KL divergence, and mutual information measures "how much knowing $Y$ reduces the uncertainty about $X$".

## A concrete example

A 4-letter source $\{A,B,C,D\}$ has probabilities $[0.5,0.25,0.125,0.125]$. Its entropy is:

$$
H=-(0.5\log_2 0.5+0.25\log_2 0.25+2\times 0.125\log_2 0.125)=1.75\ \text{bits}
$$

This means **each letter needs at least 1.75 bits on average** for lossless encoding. Huffman coding achieves exactly this (A→0, B→10, C→110, D→111, with an average length of exactly 1.75), reaching the theoretical lower bound given by the entropy.

```python
import numpy as np
p = np.array([0.5, 0.25, 0.125, 0.125])
H = -np.sum(p * np.log2(p))
print(H)   # 1.75
```

## Why it matters / where it is used

- **Loss functions**: classification uses [cross-entropy](../cross-entropy/), generative models and variational inference use the [KL divergence](../kl-divergence/) — both come from information theory.
- **Feature selection**: mutual information measures how relevant a feature is to the label, more generally than linear correlation.
- **Compression and communication**: entropy gives the limit of lossless compression, and the channel capacity theorem gives the upper bound on reliable transmission.

## What it means for time series forecasting

- Information theory gives a **theoretical ceiling on predictability**: the higher the entropy of a series (the closer to random), the higher the unbreakable lower bound on any model's prediction error.
- Mutual information can be used to judge "how much predictive value the history window really has for the future", guiding the choice of window length and feature design.
- If KUN (Kernel U-Net) produces probabilistic or categorical outputs, its training losses (cross-entropy, KL) are information-theoretic quantities at heart; understanding them helps you tell whether "the loss won't go down" means the model is not good enough or the data itself is simply too random.

## Summary

- Information = removal of uncertainty; rare events carry a lot of information.
- Entropy → cross-entropy → KL divergence → mutual information form one continuous line.
- It is both the theoretical limit of compression and communication and the foundation of machine learning losses and predictability analysis.

[← Math foundations](../math/) · [Foundations overview](../)
