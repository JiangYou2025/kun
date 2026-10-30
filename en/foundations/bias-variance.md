---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/bias-variance/
title: "The Bias–Variance Tradeoff"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

The **bias–variance tradeoff** says that a model's prediction error can be split into two parts: **bias** (the model's assumptions are too rigid, so it deviates systematically from the truth) and **variance** (the model is too sensitive to the training data, so its conclusions change drastically with a different batch of data). The simpler the model, the larger the bias; the more complex, the larger the variance. We want to find a sweet spot between the two.

## Intuition

Imagine you are shooting at a target.

- **High bias, low variance**: every shot lands in a tight group, but the whole group is off-center. It is like using a gun with a crooked sight — no matter how steady you are, you will not hit the bullseye. This corresponds to **underfitting**: the model is too simple to capture even the patterns in the training data.
- **Low bias, high variance**: the average point of impact is right around the bullseye, but the hits are scattered everywhere. It is like having very shaky hands — the occasional bullseye is pure luck. This corresponds to **[overfitting](../overfitting/)**: the model is too complex and memorizes the noise in the training data as if it were a pattern.
- **Low bias, low variance**: both accurate and steady. This is what we want, but in practice we can usually only approach it.

The key intuition: **bias and variance usually trade off against each other**. Making the model more complex lowers the bias but raises the variance, and vice versa.

## Mathematical formulation

Suppose the true relationship is $y = f(x) + \varepsilon$, where $\varepsilon$ is noise with mean 0 and variance $\sigma^2$. We learn a model $\hat{f}(x)$ from a training set. At a fixed test point $x_0$, taking the expectation over "all possible training sets", the mean squared prediction error decomposes exactly as:

$$
\mathbb{E}\big[(y - \hat{f}(x_0))^2\big]
= \underbrace{\big(\mathbb{E}[\hat{f}(x_0)] - f(x_0)\big)^2}_{\text{bias}^2}
+ \underbrace{\mathbb{E}\big[(\hat{f}(x_0) - \mathbb{E}[\hat{f}(x_0)])^2\big]}_{\text{variance}}
+ \underbrace{\sigma^2}_{\text{irreducible error}}
$$

Term by term:

- **Bias$^2$**: $\mathbb{E}[\hat{f}(x_0)]$ is the "average" prediction of the model (across different training sets); this term is its gap from the true value $f(x_0)$. A large bias means the model's structure itself is wrong.
- **Variance**: how much the model's predictions fluctuate around their own average. A large variance means the predictions change dramatically with a different batch of training data.
- **Irreducible error $\sigma^2$**: the random noise inherent in the data, which **no model can remove**; it is the lower bound on the error.

Only the first two terms are under our control. The goal is to minimize the sum **bias$^2$ + variance** — not to push either one to its extreme on its own.

## A concrete example

Fit a noisy curve with polynomials to see how complexity affects both terms:

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
x = np.linspace(0, 1, 60).reshape(-1, 1)
y = np.sin(2 * np.pi * x).ravel() + rng.normal(0, 0.2, 60)
Xtr, Xte, ytr, yte = train_test_split(x, y, test_size=0.4, random_state=0)

for deg in [1, 4, 15]:
    model = make_pipeline(PolynomialFeatures(deg), LinearRegression())
    model.fit(Xtr, ytr)
    tr = np.mean((model.predict(Xtr) - ytr) ** 2)
    te = np.mean((model.predict(Xte) - yte) ** 2)
    print(f"degree={deg:2d}  train MSE={tr:.3f}  test MSE={te:.3f}")
```

A typical output shows this trend:

- **degree=1** (a straight line): both training and test errors are high → **high bias** (underfitting).
- **degree=4**: training and test errors are both small and close to each other → **the balance point**, the best.
- **degree=15**: the training error is almost 0, but the test error shoots up → **high variance** (overfitting).

## Why it matters / where it is used

This framework is a unified lens for understanding **almost every tuning choice**:

- **Tuning model complexity**: tree depth, the number of layers in a [neural network](../neural-network/), the polynomial degree — all of these essentially slide along the bias–variance axis.
- **[Regularization](../regularization/)**: $\ell_2$ / $\ell_1$ penalties, [early stopping](../early-stopping/) and [Dropout](../dropout/) all **deliberately add a little bias in exchange for a large drop in variance**.
- **Ensemble methods**: [bagging / random forests](../ensemble-gbdt/) mainly reduce variance (by averaging several high-variance models); boosting mainly reduces bias (by correcting the residuals step by step).
- **Adding data**: more training data mainly reduces variance — it makes the model less sensitive to individual noisy points.

## Relevance to time series forecasting

In forecasting tasks, this tradeoff is just as pervasive, with a few particularities:

- **Window length = complexity knob**: forecasting from a very short history window gives a simple model with large bias that easily misses trends and seasonality; a very long window with many features gives large variance and easily mistakes occasional fluctuations for patterns.
- **Modeling seasonality**: using only the same day last week (a single lag) gives large bias; stuffing in dozens of lag features gives high variance. A common compromise is **a few meaningful lags + regularization**.
- **Evaluation must respect time order**: to tell whether you are in the bias regime or the variance regime, rely on [time series cross-validation](../cross-validation/) (rolling/expanding windows) and **never shuffle randomly**, or "future leakage" will fool you into underestimating the variance.

## Summary

- Error = bias$^2$ + variance + irreducible noise; the last term cannot be removed.
- **Underfitting ↔ high bias**, **overfitting ↔ high variance**; the two usually trade off.
- The goal is not to push one term to 0 but to minimize their sum — which usually happens at moderate complexity.
- Regularization, ensembles and more data are all tools for adjusting this tradeoff.

[← Machine learning foundations](../ml/) · [Foundations overview](../)
