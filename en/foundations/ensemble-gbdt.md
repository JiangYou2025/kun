---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/ensemble-gbdt/
title: "Ensemble Learning / GBDT"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

The idea behind **ensemble learning** is to combine many **weak models** into one that is far stronger than any of them alone. Among ensembles, **GBDT (gradient-boosted decision trees)** and its engineering implementations XGBoost / LightGBM / CatBoost are **the strongest baseline on tabular data**, and also one of the top methods for time series forecasting.

## Intuition

One person can easily misjudge, but when a crowd votes or averages its guesses, the result is often more accurate than any single expert — this is the **wisdom of crowds**. Ensemble learning applies the same principle to models: a single [decision tree](../decision-tree/) is weak and unstable, but **combine many trees cleverly** and their errors cancel out, leaving a whole that is both accurate and stable.

The key is "how to combine". There are two major schools of ensembling, with very different ideas:

- **Bagging**: many models learn **in parallel and independently**, then their outputs are averaged or voted — the main aim is to **reduce variance**.
- **Boosting**: models learn **sequentially, as a relay**, each one specifically correcting the errors of the ones before — the main aim is to **reduce bias**.

## The two paradigms: Bagging vs Boosting

**Bagging (parallel, reduces variance)**

The flagship example is the **random forest**. Its two sources of randomness are the heart of the method:

1. **Bootstrap sampling**: each tree is trained on a subset drawn from the training set "with replacement", so every tree sees slightly different data.
2. **Random feature subsets**: at each split, only a randomly chosen subset of the features is considered, forcing different trees to look at the problem from different angles.

This yields hundreds of trees that are **only weakly correlated** with each other; at prediction time, classification takes the majority vote and regression takes the average. A single tree has high variance (it is unstable), but averaging many independent trees **drives the variance down sharply**, making the whole very robust.

**Boosting (sequential, reduces bias)**

Here the models are no longer independent; they **run as a relay, one after another**: each new model is dedicated to filling in what the ensemble so far has not yet learned well. Boosting attacks **bias** directly — it gradually sculpts a pile of "not quite there" weak models into a strong one. GBDT belongs to this school.

(For the trade-off between bias and variance, see [Bias–variance trade-off](../bias-variance/); for where these models sit in the overall landscape, see [Model families](../model-families/).)

## How it works: gradient boosting (GBDT)

**Gradient boosting** is the most successful [algorithm](../algorithms/) in the boosting family. Its core idea is remarkably elegant: **each new tree fits the part of the error that the current model has not yet explained.**

Let the current ensemble be $F_{m-1}(x)$. We train a new tree $h_m(x)$ to fit its **residuals / negative [gradient](../gradient/)**, and then add it in:

$$F_{m}(x) = F_{m-1}(x) + \eta\, h_m(x)$$

The intuitive version (with squared loss): the $m$-th tree fits the **residuals**

$$r_i = y_i - F_{m-1}(x_i)$$

that is, "how far off we still are". More generally, it fits the **negative gradient** of the loss with respect to the current prediction, hence the name "gradient" boosting — this lets it adapt to all kinds of loss functions (regression, classification, quantiles, and so on).

The key hyperparameters in the formula:

- **[Learning rate](../learning-rate/) $\eta$**: each tree takes only a small step. Smaller $\eta$ → slower learning but more stable and less prone to overfitting, usually paired with more trees.
- **Number of trees $M$ (`n_estimators`)**: how many trees run in the relay. Too many will overfit; usually combined with early stopping.
- **Tree depth (`max_depth`)**: each base tree is usually very shallow (a weak learner); strength comes from numbers.

Note that $\eta$ and $M$ form a pair that trade off against each other: **small $\eta$ + large $M$** often works best, but trains more slowly.

{% include fviz/gbdt-boost.html %}

## Implementations and regularization

Hand-written GBDT is slow; in practice almost everyone uses one of three highly optimized libraries:

- **XGBoost**: classic and robust, a perennial favourite in competitions.
- **LightGBM**: histogram-based with leaf-wise growth, **fast and memory-efficient**, the first choice for large data.
- **CatBoost**: especially good with **categorical features**, and easy to tune.

All three are **strong baselines on tabular data** — given a structured dataset, throwing a GBDT at it first often produces a score that is very hard to beat.

GBDT is extremely expressive, so **preventing overfitting** is the main concern (see [Regularization](../regularization/), [Overfitting](../overfitting/)). The usual knobs:

- `learning_rate` ($\eta$): smaller is more stable.
- `n_estimators` ($M$): combine with **early stopping** to pick the best number of trees automatically.
- `max_depth` / `num_leaves`: limit the complexity of each tree.
- `subsample` / `colsample`: each tree uses only part of the samples/features (bringing bagging-style randomness in as well), which both speeds things up and reduces variance.

## A concrete example (sklearn / lightgbm)

```python
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=2000, n_features=20, noise=10, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

gbdt = GradientBoostingRegressor(
    n_estimators=300,     # M: number of trees
    learning_rate=0.05,   # η: learning rate, small slow steps
    max_depth=3,          # each base tree is shallow
    subsample=0.8,        # each tree uses a random 80% of the samples
    random_state=0,
)
gbdt.fit(Xtr, ytr)
print("Test MSE:", mean_squared_error(yte, gbdt.predict(Xte)))
```

Switching to LightGBM looks almost identical, but is much faster on large data:

```python
import lightgbm as lgb
model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=31, subsample=0.8)
model.fit(Xtr, ytr)
```

Try lowering `learning_rate` and raising `n_estimators` to feel how "small, slow steps are more stable".

## Why it matters for time series forecasting (key point)

This is one of the stages where GBDT shines brightest in practice. Turn the time series into a table — build **lag features** ($t-1, t-7, t-28$), **rolling statistics** (mean / max / standard deviation over the past 7 days), and **calendar features** (day of week, month, holidays) — and feed it to a GBDT: this is one of the strongest forecasting recipes today. The winning solution of the famous **M5 sales forecasting competition** was built around LightGBM.

It is particularly good at **forecasting many related series at once** (for example thousands of products or stores): stack all the series into one big table and train a single GBDT on it, and the model can share patterns across series — simple and powerful.

But there is an **important warning**, exactly the same as for [decision trees](../decision-tree/):

> **GBDT cannot extrapolate trends either.**

Because its predictions ultimately land on leaf means, its output **cannot leave the range seen during training**. Faced with a series that rises over the long term, it will systematically **underestimate the future**. The standard remedy: **detrend / difference first, then use GBDT** to model the remaining stationary part (or build a separate trend term and let the GBDT learn only the nonlinearity and seasonality in the residuals).

Finally, evaluation must use **time series cross-validation** (rolling splits in time order, only predicting the future from the past) — **never shuffle randomly**, or you will be using future information to predict the past, causing data leakage and wildly inflated results. See [Cross-validation](../cross-validation/).

## Summary

- **Ensemble learning** combines many weak models into a strong one, relying on the **wisdom of crowds**.
- Two paradigms: **Bagging** (parallel, reduces variance, e.g. random forests: bootstrap + random features) vs **Boosting** (sequential, reduces bias).
- **GBDT** is gradient boosting: each new tree fits the **residuals / negative gradient**, $F_m(x)=F_{m-1}(x)+\eta\,h_m(x)$; the key knobs are **learning rate $\eta$, number of trees $M$, depth**, and small $\eta$ + large $M$ is often best.
- The implementations **XGBoost / LightGBM / CatBoost** are **strong baselines on tabular data**; overfitting is controlled with `learning_rate`/`n_estimators`/`max_depth`/`subsample` (see [Regularization](../regularization/), [Overfitting](../overfitting/)).
- In time series, it is a top method on **lag / rolling / calendar features** (M5 winner) and excels at forecasting many series in bulk.
- **Fatal warning: it cannot extrapolate trends** — usually **detrend / difference before using GBDT**, and evaluate with **time series cross-validation**.

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
