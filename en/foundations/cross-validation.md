---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/cross-validation/
title: "Cross-Validation"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Cross-validation (CV)** means **splitting the data several times** and letting a different portion take its turn as the validation set, so that you can **evaluate models, select models and tune hyperparameters more robustly**. For time series, the splits must **strictly follow chronological order** — never shuffle the data at random.

## Intuition

Suppose you make a single "train / test" split: 80% for training, 20% for testing, and you compute one score. The problem is that **this score contains an element of luck**.

If that 20% happens to be "easy", the score is too high; if it happens to be "hard", the score is too low. Change the random seed and the score might jump from 0.90 to 0.83. If you use such a **highly jittery** single score to compare two models or tune a hyperparameter, you may well pick the wrong one — the difference you see might be nothing but noise.

**The core idea of cross-validation**: rather than splitting once and relying on a single roll of the dice, **split many times so that every portion of the data serves once as the validation set**, then **average** the scores. Averaging dilutes the luck and gives a steadier, more trustworthy estimate.

An analogy: judging a student's level from a single exam easily gives a distorted picture; sit five exams and take the average, and you get much closer to their true level.

## K-fold cross-validation

The most common approach is **k-fold cross-validation**, which works as follows:

1. Randomly (note: time series must **not** be randomized — see below) divide the data into $k$ equal parts, each called a **fold**. Typical choices are $k=5$ or $k=10$.
2. Round 1: use fold 1 as the validation set and the remaining $k-1$ folds as the training set; train, score, and obtain $\text{score}_1$.
3. Round 2: use fold 2 as the validation set and the rest for training; obtain $\text{score}_2$.
4. … and so on until fold $k$, giving $\text{score}_k$.
5. **Average** the $k$ scores to get the model's cross-validation score:

$$\text{CV score} = \frac{1}{k}\sum_{i=1}^{k}\text{score}_i$$

This way every sample **serves as validation data exactly once** and also takes part in training, so data usage is high and the estimate is more stable. Besides the mean, we also look at the **standard deviation** of the $k$ scores — it tells you how stable the model's performance really is.

**LOOCV (leave-one-out cross-validation)** is the extreme case of k-fold: set $k=n$ (the total number of samples), keep just **one** sample for validation each time and train on all the others. It uses almost all the data for training, so its bias is small, but it requires $n$ training runs — a huge computational cost — and its variance is relatively high, so it is usually used only on small datasets.

## CV is for model selection / tuning, not the final score

This is the point beginners confuse most often: **cross-validation is a tool for "model selection" and "hyperparameter tuning", not for producing a final, unbiased score.**

Why? Because when you use the CV score to **repeatedly pick** the best hyperparameters, you are in effect "catering" to those validation folds — the best configuration you select is somewhat "[overfitted](../overfitting/)" to the validation data. So the CV score is **slightly optimistic**.

The correct workflow splits the data into three parts:

- **Training set**: used to fit the model parameters.
- **Validation set (produced by CV rotating inside the training data)**: used to tune hyperparameters and select models.
- **Test set (held out separately and never touched)**: run only **once** at the very end, as an unbiased estimate of true generalization.

In one sentence: **CV helps you "choose"; the held-out test set lets you "report the score"**. This is also the key principle for splitting data in the [training pipeline](../training-pipeline/), and it directly determines whether your assessment of the model's [generalization](../generalization/) can be trusted.

## A concrete example

For ordinary (non-time-series) data, sklearn's `cross_val_score` does it in one line:

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(scores)            # 5 scores, e.g. [0.91 0.88 0.90 0.87 0.92]
print(scores.mean())     # mean: 0.896  <- this is the CV score
print(scores.std())      # standard deviation: smaller means more stable
```

For **time series**, you must switch to `TimeSeriesSplit`, which guarantees the training set always comes before the validation set:

```python
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

tscv = TimeSeriesSplit(n_splits=5)          # forward, chronological splits
scores = cross_val_score(model, X, y, cv=tscv, scoring="neg_mean_absolute_error")
print(-scores.mean())                        # mean MAE
```

Note: the folds produced by `TimeSeriesSplit` are **not equal-sized, non-overlapping** random blocks, but a rolling structure in which "the training set keeps growing and the validation set always lies in the future".

## Why it matters for time series forecasting

This is the **most important** part of this page. Time series data have a "direction of time": the future cannot be used to predict the past, so cross-validation needs special treatment.

**Why does ordinary k-fold go wrong?** Ordinary k-fold first **shuffles** the data and then splits it into folds. This means a fold's training set may contain data that occurred **later than the validation samples**. The model effectively "peeks at the future" before predicting the past — this is called **look-ahead leakage (data leakage)**. The result: the cross-validation score is **absurdly inflated**, and as soon as the model goes live and faces the genuinely unknown future, it falls apart.

**The correct approach: walk-forward / rolling-origin validation.** Always keep **training time < validation time**. Cut the time axis into several segments from early to late and advance step by step:

```
Round 1  train[1..100]            validate[101..120]
Round 2  train[1..120]            validate[121..140]
Round 3  train[1..140]            validate[141..160]
...
```

This is exactly the logic of `TimeSeriesSplit`: each round simulates the real situation of "standing at some point in time and using the past to predict the future".

**Expanding window vs. sliding window** — two common variants:

- **Expanding window**: the training set keeps **growing**, including all of the history (as above). Suitable when the patterns in the data are stable and you want to use as much history as possible.
- **Sliding window**: the training set has a **fixed length** and moves forward with time as a whole (dropping the oldest data, adding the newest). Suitable when the patterns **drift** and recent data are more representative.

**Gap / embargo**: when features contain information spanning several steps, such as rolling means or lagged terms, the end of the training set and the start of the validation set may **overlap in time** and cause leakage. The fix is to **leave a small gap** (gap / embargo) between training and validation sets so that neighboring samples cannot "seep" into each other.

## Common pitfalls

- **Randomly shuffled k-fold on time series**: directly causes look-ahead leakage — inflated scores and collapse in production. Always split time series in chronological order.
- **Fitting feature scaling on the full dataset**: computing the mean / standard deviation (or normalizing) on all the data before splitting leaks information from the validation / test sets into training. The right way is to **`fit` only on the training folds** and then `transform` the validation fold — put it inside a `Pipeline` so CV handles it automatically.
- **Tuning hyperparameters on the test set**: once the test set has been "seen" and used to choose parameters, it is no longer unbiased, and the score will be overly optimistic. Use the test set only once, at the very end.
- **Ignoring the variance across folds**: looking only at the mean and not the standard deviation can hide the fact that the model is extremely unstable in certain time periods.

## Summary

- Cross-validation = split several times, validate in turn, and average, giving a **more robust** evaluation than a single split.
- K-fold: divide into $k$ parts, hold out one at a time for validation, and average the scores $\frac1k\sum_i\text{score}_i$; LOOCV is the extreme version with $k=n$.
- CV is for **selecting models / tuning hyperparameters**; the final unbiased score comes from a **separately held-out test set**.
- Time series must **never be randomly shuffled** — use **forward / rolling** validation such as `TimeSeriesSplit`, ensure training time < validation time, and add a gap/embargo when needed.

Related concepts: [Loss function](../loss-function/) · [Training pipeline](../training-pipeline/) · [Overfitting](../overfitting/) · [Generalization](../generalization/)

---

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
