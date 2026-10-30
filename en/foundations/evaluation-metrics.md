---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/evaluation-metrics/
title: "Evaluation Metrics"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Evaluation metrics** are the **quantitative standards** used to judge how good a model is. A metric must **match the business goal**, and it should be reported on a **test set** the model has never seen.

## Intuition

**A metric is the "ruler you score with" — pick the wrong ruler and you will misjudge even an excellent model.**

The same model can look completely different under different metrics. Take a model that forecasts sales: its average error looks small, but it is wildly wrong on a few big promotion days. If what your business fears most is "getting stock wrong for a promotion", that nice "small average error" is meaningless.

So learning evaluation metrics is not just about memorizing formulas; it is about understanding **what each ruler measures, what it is sensitive to, and when it can fool you** — and then **choosing the right ruler for the business goal**.

## Regression metrics

Regression tasks predict **continuous values** (temperature, sales, stock prices). Let the true values be $y_i$, the predictions $\hat y_i$, and the number of samples $n$.

**Mean Absolute Error (MAE)**

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}\left|y_i-\hat y_i\right|$$

The average absolute size of the error, in the same units as $y$; intuitive and **insensitive to outliers**.

**Mean Squared Error (MSE)**

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2$$

Squaring before averaging **heavily penalizes large errors**; but the units are the square of $y$'s, which makes it hard to interpret.

**Root Mean Squared Error (RMSE)**

$$\text{RMSE} = \sqrt{\text{MSE}}$$

Taking the square root brings it back to **the same units as $y$**: it keeps the "heavy penalty on large errors" while being easy to interpret, and is one of the most widely used regression metrics.

**Coefficient of determination $R^2$**

$$R^2 = 1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}$$

Expresses how much better the model is than "just predicting the mean". $R^2=1$ is perfect, $R^2=0$ is no better than guessing the mean, and it **can be negative** (worse than the mean).

**Mean Absolute Percentage Error (MAPE)**

$$\text{MAPE} = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i-\hat y_i}{y_i}\right|$$

Expresses error as a **percentage**, making series of different magnitudes comparable; but when $y_i$ is close to 0, the tiny denominator makes the value **explode** — its fatal weakness.

**Symmetric MAPE (sMAPE)** replaces the denominator with half the sum of the true and predicted values, which mitigates the division-by-small-values problem:

$$\text{sMAPE} = \frac{1}{n}\sum_{i=1}^{n}\frac{|y_i-\hat y_i|}{(|y_i|+|\hat y_i|)/2}$$

**Mean Absolute Scaled Error (MASE)** divides the error by the error of a **naive baseline** (such as "predict with the previous value"), producing a dimensionless relative score: $\text{MASE}<1$ means the model beats the naive baseline, $>1$ means it does worse than the naive baseline. It is robust to zeros and especially common in time series.

## Classification metrics

Classification tasks predict a **class** (such as "yes / no", "fraud / normal").

**Accuracy** = the fraction of correct predictions. Simple, but extremely misleading under **class imbalance**: if 99% of samples are "normal", a useless model that "predicts normal for everything" also scores 99% accuracy while catching no fraud at all.

Metrics based on the **confusion matrix** (true positives TP, false positives FP, true negatives TN, false negatives FN) are more reliable:

$$\text{precision} = \frac{TP}{TP+FP},\qquad \text{recall} = \frac{TP}{TP+FN}$$

- **Precision**: of everything you flagged as "positive", how much really is? (cares about "no false alarms")
- **Recall**: of all the true positives, how many did you catch? (cares about "no misses")

The two usually trade off against each other, and are combined in the **F1 score** (the **harmonic mean** of precision and recall):

$$F_1 = \frac{2\cdot\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}}$$

**ROC curve / AUC**: varying the decision threshold traces a curve of "true positive rate vs false positive rate"; the area under the curve, **AUC**, measures the model's overall ranking ability — $0.5$ is random guessing, $1.0$ is perfect.

{% include fviz/roc.html %}

## Loss functions vs evaluation metrics

These two concepts look alike but play different roles:

- A **[loss function](../loss-function/)** is what gets **optimized** (minimized) during training; it must be **differentiable** so that [gradient descent](../gradient-descent/) can work (e.g. MSE, [cross-entropy](../cross-entropy/)).
- An **evaluation metric** is the score **reported** to people after training; it **need not be differentiable** and can be whatever best reflects the business (e.g. MAE, F1, AUC, MASE).

Example: a classifier is trained with **cross-entropy** as its loss (differentiable, easy to optimize), but the final report usually uses **F1 / AUC** (not differentiable, but a better reflection of "did we catch the fraud"). In one sentence: **the loss function is "for the optimizer during training", the evaluation metric is "for people after training".**

## A concrete example

```python
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             r2_score, f1_score, classification_report)
import numpy as np

# Regression
y_true = [3.0, 5.0, 2.5, 7.0]
y_pred = [2.8, 4.5, 3.0, 6.0]
print("MAE :", mean_absolute_error(y_true, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
print("R2  :", r2_score(y_true, y_pred))

# Classification
yc_true = [0, 1, 1, 0, 1]
yc_pred = [0, 1, 0, 0, 1]
print("F1  :", f1_score(yc_true, yc_pred))
print(classification_report(yc_true, yc_pred))   # precision / recall / F1 all at once
```

## Why it matters: match the business goal

More metrics is not better; what matters is **aiming at what you really care about**:

- Medical screening fears **missed diagnoses** most → prioritize **recall**.
- Spam filtering fears **blocking legitimate mail** most → prioritize **precision**.
- In inventory forecasting, large errors are costly → use **RMSE**, which **heavily penalizes large errors**.
- To explain to your boss "how many units off we are on average" → use **MAE**, whose units are intuitive.

Choosing the wrong metric means optimizing a target that "looks pretty but is useless".

## Why it matters for time series forecasting

- **Numerical forecasts** usually use **RMSE / MAE**: RMSE cares more about occasional large errors, MAE is more robust and easier to explain.
- **Use MAPE with caution**: as soon as the series contains **zeros or very small values**, MAPE gets blown up and distorted. In that case **sMAPE** or **MASE** is more stable.
- **Prefer MASE**: it compares the model's error with that of the **naive forecast (using the previous period's value as the prediction)**, naturally answering the question you should ask first: "how much better is my model than doing nothing?"
- **Evaluate in time order, out of sample (on the future)**: train on the past and score on a future period the model has not seen; otherwise the score is meaningless (see walk-forward validation in [Cross-validation](../cross-validation/)).
- **Look at per-horizon error**: the next step is usually predicted accurately, but error **grows with the forecast horizon** for steps far ahead. Reporting the error **separately for each horizon** is more informative than a single overall average.
- **Always compare against the naive baseline**: for any fancy model, first make sure it really beats the naive baseline of "predict today with yesterday's value"; otherwise its complexity is worthless.

## Summary

- An evaluation metric = the ruler for judging a model; **the wrong ruler leads to misjudgment** — match the business goal and report on the **test set**.
- Regression: MAE (robust), MSE/RMSE (heavy penalty on large errors, RMSE in the same units), $R^2$, MAPE (breaks on zeros), sMAPE / MASE (more stable, comparable).
- Classification: accuracy (misleading under imbalance), precision, recall, F1, confusion matrix, ROC/AUC.
- The **loss function** is optimized (differentiable), the **evaluation metric** is reported (need not be differentiable) — don't confuse them.
- Time series: evaluate in time order on the future, look at per-horizon error, use MAPE with care and MASE generously, and **always compare against the naive baseline**.

Related concepts: [Loss function](../loss-function/) · [Training pipeline](../training-pipeline/) · [Overfitting](../overfitting/) · [Generalization](../generalization/)

---

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
