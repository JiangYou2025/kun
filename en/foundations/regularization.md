---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/regularization/
title: "Regularization"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Regularization** means **adding extra constraints or penalties** while training a model in order to limit its complexity, which curbs **overfitting** and improves its ability to **[generalize](../generalization/)**. In one sentence: keep the model from being too "willful" — make it learn something simpler and steadier.

## Intuition

Recall what overfitting really is: to fit the training data perfectly, the model pushes its weights to large, strange values and ends up memorizing a pile of noise. The core idea of regularization is to **put a tight rein on the model**:

> **While fitting the data, keep the weights small and the model simple.**

Behind this lies **Occam's razor**: when two explanations are about equally good, the simpler model is more likely to be right, and more likely to generalize well.

An analogy: you are asked to draw a curve through a cloud of scattered points.

- Without constraints: you can draw a wildly wiggling curve that passes through every single point (huge weights, overfitting).
- With regularization: it is as if someone beside you keeps saying "don't bend the curve so sharply", so you draw a smooth curve that captures the overall trend — and it actually predicts new points better.

See [overfitting](../overfitting/) for details.

## Mathematical formulation

Ordinary training only minimizes the [loss](../loss-function/) on the data. Regularization **adds a penalty term** to the objective:

$$\min_{w}\;\; \underbrace{\frac{1}{n}\sum_{i=1}^{n} L\big(y_i, f(x_i)\big)}_{\text{fit the data}} \;+\; \underbrace{\lambda\, \Omega(w)}_{\text{penalize complexity}}$$

- $\Omega(w)$ is the **complexity penalty**, usually some measure of the "size" of the weights. The larger the weights, the heavier the penalty.
- $\lambda \ge 0$ is the **regularization strength**; it controls a tug-of-war between two forces:
  - $\lambda \to 0$: almost no penalty, back to plain fitting, prone to **overfitting**.
  - Very large $\lambda$: the weights are crushed, the model becomes too simple, prone to **underfitting**.
  - A suitable $\lambda$: a balance between fitting and simplicity. $\lambda$ is a hyperparameter that has to be tuned on a **validation set / with [cross-validation](../cross-validation/)**.

## Common kinds of regularization

Different choices of $\Omega(w)$ give different kinds of regularization.

**L2 / Ridge**: penalize the sum of squared weights

$$\Omega(w) = \|w\|_2^2 = \sum_j w_j^2$$

L2 makes all the weights **smaller and smoother overall**, but generally does not push them exactly to 0. It is especially effective against collinearity and for stabilizing a model, and is also often called **weight decay**.

**L1 / Lasso**: penalize the sum of absolute values of the weights

$$\Omega(w) = \|w\|_1 = \sum_j |w_j|$$

The remarkable thing about L1 is that it **drives some weights exactly to 0**, which performs automatic **feature selection** — unimportant features are simply kicked out of the model, giving a **sparse** solution.

Why can L1 "zero things out" while L2 cannot? Look at the geometric intuition. Optimization amounts to finding the point of lowest loss inside a constraint region defined by a "penalty budget":

- The L2 constraint region is a **circle** (a ball in higher dimensions). Its surface is smooth, so the loss contours usually touch it at some slanted position where every component is non-zero.
- The L1 constraint region is a **rhombus / diamond** (in higher dimensions, a polytope with sharp corners), and its **corners sit exactly on the coordinate axes**. As the loss contours expand outward, they are most likely to hit these corners first, and at a corner some coordinates are exactly 0 — so the corresponding weights are driven to 0.

**Elastic Net**: add L1 and L2 together

$$\Omega(w) = \alpha\|w\|_1 + (1-\alpha)\|w\|_2^2$$

It combines the sparsity of L1 with the stability of L2, and often performs better when there are many features that are correlated with each other.

## Beyond penalty terms: other regularization techniques

In the broad sense, regularization covers every technique that "constrains the model and keeps it from memorizing noise":

- **[Early stopping](../early-stopping/)**: watch the validation error and stop training as soon as it starts to rise again, so the model does not overfit more and more.
- **[Dropout](../dropout/)**: when training a [neural network](../neural-network/), randomly "drop" a fraction of the [neurons](../neuron/), forcing the network not to depend on individual units and to learn more robust representations.
- **Tree pruning / limiting depth (`max_depth`)**: cap the maximum depth of a [decision tree](../decision-tree/) or prune useless branches, so the tree does not grow until it has memorized every sample.
- **Data augmentation**: apply sensible transformations to the data (rotation, added noise, etc.) to enlarge the training set artificially, which amounts to telling the model "these variations do not matter".
- **Weight decay**: keep shrinking the weights during training; this is essentially equivalent to L2 regularization.

## A concrete example (sklearn)

Let's use Ridge and Lasso to see it directly: **increasing $\alpha$ (i.e. $\lambda$) pushes the coefficients toward smaller values**.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso

rng = np.random.RandomState(0)
X = rng.randn(100, 5)
# The true relationship depends only on the first two features; the last three are noise
y = 3 * X[:, 0] - 2 * X[:, 1] + 0.1 * rng.randn(100)

for alpha in [0.0, 0.1, 1.0, 10.0]:
    ridge = Ridge(alpha=alpha).fit(X, y)
    print(f"Ridge alpha={alpha:>4}: {np.round(ridge.coef_, 2)}")

for alpha in [0.001, 0.05, 0.2, 1.0]:
    lasso = Lasso(alpha=alpha).fit(X, y)
    print(f"Lasso alpha={alpha:>5}: {np.round(lasso.coef_, 2)}")
```

You will observe:

- **Ridge**: as `alpha` grows, all the coefficients **shrink together**, but they rarely become exactly 0.
- **Lasso**: as `alpha` grows, the **coefficients of the useless features turn to 0 one after another**, until only the two truly important features remain — this is automatic feature selection.

{% include fviz/reg-path.html %}

## Why it matters: linking overfitting and bias–variance

Regularization is the most direct and most widely used weapon against [overfitting](../overfitting/). In the language of the [bias–variance tradeoff](../bias-variance/):

> **Regularization deliberately introduces a little bias in exchange for a large drop in variance.**

- Without regularization: the model has high variance and is overly sensitive to the noise in the training data (overfitting).
- With regularization: the model becomes simpler and steadier and its variance drops; the bias rises slightly, but **the overall generalization error is smaller**.

So tuning $\lambda$ is, at heart, a search for the sweet spot between bias and variance where the generalization error is lowest. See [generalization](../generalization/) for details.

## Relevance to time series forecasting

In time series forecasting we often build a large number of **lag features**: using the values at times $t-1, t-2, \dots, t-k$ to predict $t$. This causes two problems:

- **Many, correlated features**: neighbouring lags are highly collinear, so a [linear model](../linear-model/) easily overfits, mistaking chance fluctuations in the history for patterns.
- **Lots of noise**: real time series are noisy, and an unconstrained model easily fits the noise rather than the trend.

Regularization is especially useful here:

- **L2 / Ridge** stabilizes the coefficients, eases the collinearity among lag features, and makes forecasts smoother.
- **L1 / Lasso** automatically **picks out which lags really matter** — for example, it might tell you that only $t-1$ and $t-7$ (yesterday and the same day last week) are useful and set the other lag coefficients to zero, giving a model that is leaner, more interpretable and less prone to overfitting.

In one sentence: in time series with many lag features and a lot of noise, regularization helps you **learn the patterns, not memorize the noise**.

## Summary

- **Regularization** limits model complexity by adding constraints/penalties, in order to curb **overfitting** and improve **generalization**.
- Core objective: $\min_w \frac1n\sum L + \lambda\,\Omega(w)$; **the larger $\lambda$, the simpler the model**, and it must be tuned on a validation set.
- **L2/Ridge** shrinks weights smoothly; **L1/Lasso** produces sparsity and performs feature selection (the corners of the diamond constraint lie on the axes); **Elastic Net** combines both.
- Regularization in the broad sense also includes **early stopping, Dropout, pruning/depth limits, data augmentation, and weight decay**.
- From the bias–variance viewpoint: regularization **trades a little bias for a large drop in variance**.
- In time series, regularization tames the many **lag features** and prevents fitting noise; **L1** can also help you pick out the key lags.

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
