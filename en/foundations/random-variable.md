---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/random-variable/
title: "Random Variables"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

A random variable is a variable that maps "random outcomes" to **numbers**; the pattern of its values is described by a **probability distribution**. A time series can be seen as a sequence of random variables changing over time.

## Intuition

The "outcome" of rolling a die is an abstract event, but we want to compute with numbers. A random variable is the bridge: it **attaches a numeric label** to each possible outcome, so that we can talk about averages, fluctuations and probability distributions.

- Rolling a die → the random variable $X$ takes values 1\~6;
- Tossing a coin → let heads = 1, tails = 0;
- Tomorrow's temperature → a continuous random variable.

Note: a random variable is not itself a fixed number but "a probability machine that has not yet produced its result"; it describes **all possible values and their probabilities**.

## Mathematical formulation

A **discrete random variable** is described by a **probability mass function (PMF)**:

$$
p(x)=P(X=x),\qquad \sum_x p(x)=1
$$

A **continuous random variable** is described by a **probability density function (PDF)**, and probabilities are given by integrals:

$$
P(a\le X\le b)=\int_a^b f(x)\,dx,\qquad \int_{-\infty}^{\infty} f(x)\,dx=1
$$

Two key numbers characterize a random variable:

$$
\text{Expectation (centre)}\quad \mu=\mathbb{E}[X]=\sum_x x\,p(x)\ \text{or}\ \int x f(x)\,dx
$$
$$
\text{Variance (spread)}\quad \sigma^2=\operatorname{Var}(X)=\mathbb{E}[(X-\mu)^2]
$$

Relationships between several random variables are described by their **joint distribution** and their **covariance** $\operatorname{Cov}(X,Y)$.

## A concrete example

A Bernoulli random variable: a single toss with probability of heads $p=0.3$; let $X=1$ for heads and $X=0$ for tails.

$$
\mathbb{E}[X]=1\cdot 0.3+0\cdot 0.7=0.3
$$
$$
\operatorname{Var}(X)=p(1-p)=0.3\times 0.7=0.21
$$

```python
import numpy as np
X = (np.random.rand(100000) < 0.3).astype(int)  # Bernoulli(0.3)
print(round(X.mean(), 3))  # ≈ 0.300  ← expectation
print(round(X.var(),  3))  # ≈ 0.210  ← variance
```

## Why it matters / where it is used

- **The atom of all modelling**: data, parameters, noise and forecasts are all modelled as random variables.
- **[Loss](../loss-function/) and inference**: [maximum likelihood](../maximum-likelihood/) and [Bayesian methods](../bayes-theorem/) both operate on the distributions of random variables.
- **Generative models**: treat the data as samples drawn from some random variable and learn its distribution (VAEs, diffusion models, etc.).

## Relevance to time series forecasting

- A time series $\{X_1,X_2,\dots,X_t\}$ is a sequence of random variables; forecasting means estimating the distribution of $X_{t+1}$ (or its expectation).
- **Stationarity** means that the statistical properties of these random variables (mean, variance, autocorrelation) do not change over time — a prerequisite for many classical methods.
- When KUN (Kernel U-Net) makes a point forecast, it outputs the conditional expectation $\mathbb{E}[X_{t+1}\mid \text{history}]$; for a probabilistic forecast, it directly outputs the parameters of the distribution of $X_{t+1}$ (such as its mean and variance).

## Summary

- Random variable = a mapping from random outcomes to numbers, whose pattern of values is described by a distribution (PMF/PDF).
- The expectation describes the centre, the variance the fluctuation.
- A time series is a sequence of random variables, and forecasting is inferring the distribution or expectation of future random variables.

[← Math foundations](../math/) · [Foundations overview](../)
