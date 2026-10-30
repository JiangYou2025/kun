---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/overfitting/
title: "Overfitting"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**Overfitting** is when a model performs extremely well on its training data but has also taken the **noise and chance coincidences** in that data for real patterns, so that it does poorly on new data it has never seen. It is the most common failure mode in [machine learning](../ml/); its opposite is **underfitting** (the model is too simple to learn even the training data well).

## Intuition

Imagine students preparing for an exam:

- **The underfitting student** barely studied and can solve neither the basic exercises nor the exam questions.
- **The overfitting student** memorized the **answers** to past papers word for word — change a single number in a question and they are lost. They memorized specific answers, not the method.
- **The student who [generalizes](../generalization/) well** understood the underlying method and can also solve new questions.

The essence of overfitting is "rote memorization": the model has enough capacity, so it takes the shortcut of **memorizing every training example** instead of **extracting patterns that carry over**.

## How to recognize it

The most reliable signal is the **gap between training error and validation error**:

$$
\text{generalization gap} = \text{validation error} - \text{training error}
$$

- Low training error, validation error also low and close to it → a good fit.
- **Very low** training error, **clearly higher** validation error → **overfitting**, a large gap.
- **Both** training and validation errors high → underfitting.

When training a [neural network](../neural-network/), plot a **learning curve** (epochs on the horizontal axis, loss on the vertical axis): if the training [loss](../loss-function/) keeps falling while the validation loss starts to **rise again**, that turning point is where overfitting begins — and where [early stopping](../regularization/) should step in.

## Why it happens

From the [bias–variance](../bias-variance/) point of view, overfitting = **high variance**. Common causes:

- **Model capacity too large relative to the data**: more parameters than samples (high-degree polynomials, very deep trees, huge networks).
- **Too little or too noisy training data**: with too few samples, the model can only fit individual points.
- **Leakage or redundancy in the features**: the model latches onto a feature that is correlated by chance but has no causal link.
- **Training too long**: with too many iterations, the model slides from learning patterns to memorizing samples.

## A concrete example

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(1)
X = rng.uniform(0, 1, (120, 1))
y = (np.sin(6 * X).ravel() + rng.normal(0, 0.15, 120))
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=0)

for depth in [2, 5, None]:   # None = unlimited depth, can split arbitrarily
    m = DecisionTreeRegressor(max_depth=depth, random_state=0).fit(Xtr, ytr)
    tr = np.mean((m.predict(Xtr) - ytr) ** 2)
    te = np.mean((m.predict(Xte) - yte) ** 2)
    print(f"max_depth={str(depth):>4}  train MSE={tr:.3f}  test MSE={te:.3f}")
```

The tree with unlimited depth reaches a training MSE close to 0 (it can give every sample its own leaf), yet its test MSE is the largest — the textbook symptom of overfitting.

## How to fight it

- **More data / data augmentation**: the most fundamental remedy.
- **[Regularization](../regularization/)**: $\ell_1$ / $\ell_2$ penalties, [Dropout](../dropout/), pruning trees, limiting `max_depth`.
- **Early stopping**: stop training when the validation loss starts to rise again.
- **Reducing model complexity**: fewer features, shallower models.
- **Choosing hyperparameters by [cross-validation](../cross-validation/)**: select models on a validation set, not on the training set.
- **[Ensembles](../ensemble-gbdt/)**: bagging / random forests reduce variance by averaging.

## Relevance to time series forecasting

Overfitting is especially insidious in time series because the data points are **not independent**:

- **Look-ahead bias**: using information that would not yet be available at forecast time (for example future statistics, or a validation set built after random shuffling) inflates validation scores — a kind of "cheating overfitting". Always split by time with [time series cross-validation](../cross-validation/).
- **Too many lag features**: stuffing in dozens or hundreds of lag / rolling-statistic features makes it easy for the model to memorize chance fluctuations of the past. Prefer a small number of features with business meaning, plus regularization.
- **Overfitting a single historical period**: special events in one stretch of history (a pandemic, a promotion) get treated as the norm. Validating with rolling windows over **several time periods** is more robust.

## Summary

- Overfitting = good on training, poor on test; it corresponds to **high variance** and rote memorization.
- Diagnose it with the **gap between training and validation error** and with **learning curves**.
- The toolkit: more data, regularization, early stopping, lower complexity, cross-validation, ensembles.
- In forecasting, the greatest danger is **look-ahead leakage** — splitting by time is the bare minimum.

[← Machine learning foundations](../ml/) · [Foundations overview](../)
