---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/linear-model/
title: "Linear Models"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

A **linear model** makes predictions with a **linear combination** of the input features (a weighted sum plus a bias). It is simple, interpretable and fast to train — the **baseline model** to try first in almost any [machine learning](../ml/) task.

## Intuition

Imagine you want to predict a house's price from its floor area. The most naive idea is: **so much per square meter, plus a base price**. Written as a formula:

$$\text{price} \approx w \times \text{area} + b$$

Here $w$ (the slope) tells you "how much the price rises for each extra square meter", and $b$ (the intercept) is the "base price" when the area is 0. When you have several features (area, floor, distance to the subway…), you give each feature a weight and add them up — that is the whole secret of a linear model: **fitting the data with a straight line (or a plane in higher dimensions)**.

"Linear" does not mean the world is linear; it means **the model is linear in its parameters $w$**. Precisely because the structure is so simple, we can see clearly how much each feature contributes, and this **interpretability** is something many complex models cannot offer.

## Mathematical formulation: linear regression

For a sample with $d$ features $x = (x_1, x_2, \dots, x_d)$, the prediction of linear regression is

$$\hat{y} = w^\top x + b = \sum_{j=1}^{d} w_j x_j + b$$

- **Weights / coefficients** $w_j$: the "contribution rate" of the $j$-th feature to the prediction. $w_j > 0$ means the larger the feature, the larger the prediction; $w_j < 0$ means the opposite; $w_j \approx 0$ means the feature is essentially useless.
- **Intercept** $b$: the baseline prediction when all features are 0.

How do we find the "best" $w$ and $b$? We make the gap between the predictions $\hat{y}_i$ and the true values $y_i$ as small as possible, using the **mean squared error (MSE)** as the [loss](../loss-function/):

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}\left(y_i - \hat{y}_i\right)^2$$

The method that minimizes this error is called **least squares**. Remarkably, it has a **closed-form solution** — no iterations needed, it is computed in one step:

$$w = (X^\top X)^{-1} X^\top y$$

where $X$ is the feature matrix formed by stacking all samples as rows. This means linear regression trains extremely fast, which is a major reason it serves as a "just try it" baseline.

{% include fviz/linreg.html %}

## Mathematical formulation: logistic regression (classification)

If the task is **classification** (for example "will it rain tomorrow?"), outputting a raw real number is not appropriate; we want a **probability**. So the output of the linear part is passed through a **sigmoid function**, which squashes it into the interval $(0,1)$:

$$p = \sigma(w^\top x + b), \qquad \sigma(z) = \frac{1}{1 + e^{-z}}$$

The graph of $\sigma(z)$ is a smooth "S-shaped curve": it approaches 1 when $z$ is large, approaches 0 when $z$ is very negative, and equals exactly 0.5 at $z=0$. If $p > 0.5$, predict the positive class; otherwise, the negative class.

Logistic regression does not use MSE but the **[cross-entropy](../cross-entropy/)** loss:

$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^{n}\Big[y_i \log p_i + (1-y_i)\log(1-p_i)\Big]$$

It measures "how far the predicted probability distribution is from the true labels"; the loss is smallest when the model assigns high probabilities to positives and low probabilities to negatives.

## A concrete example (sklearn)

```python
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler

# ---- Linear regression: predict house price from area ----
X = np.array([[50], [60], [80], [100], [120]])   # area
y = np.array([150, 180, 240, 300, 360])          # price (in units of 10,000)

reg = LinearRegression().fit(X, y)
print("slope w =", reg.coef_, "intercept b =", reg.intercept_)
print("prediction for 90 m²:", reg.predict([[90]]))

# ---- Logistic regression: binary classification, remember to standardize features first ----
Xc = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 4.0], [4.0, 3.0]])
yc = np.array([0, 0, 1, 1])

scaler = StandardScaler()
Xc_scaled = scaler.fit_transform(Xc)             # coefficients are comparable only after scaling
clf = LogisticRegression().fit(Xc_scaled, yc)
print("predicted probabilities:", clf.predict_proba(scaler.transform([[2.5, 2.5]])))
```

Note the deliberate **feature scaling** here: when features have very different scales (for example "area" in the tens and "number of rooms" in single digits), not scaling makes the coefficients incomparable and also slows down or distorts the optimization. **Standardization (StandardScaler)** is practically standard preprocessing for linear models.

## Why it matters (where it is used)

- **A strong baseline**: before reaching for a complex model, run a linear model first. If it is already good enough, there is no need for anything fancier; if not, it gives you a reference line that "you must at least beat".
- **Fast**: a closed-form solution or simple [gradient descent](../gradient-descent/) trains in seconds, ideal for rapid experimentation.
- **Interpretable**: the coefficients tell you which features matter and in which direction, making the model easy to explain to others and handy for spotting data problems.
- When there are many features and [overfitting](../overfitting/) is a risk, it pairs naturally with [regularization](../regularization/), becoming **Ridge (L2)** and **Lasso (L1)**, which automatically shrink or even eliminate useless features.

## What it means for time series forecasting

In time series forecasting, the power of linear models is often underestimated. The key trick is to build **lag features**: use the values of the past few periods $y_{t-1}, y_{t-2}, \dots, y_{t-p}$ as input features to predict the current $y_t$. Linear regression then becomes

$$\hat{y}_t = w_1 y_{t-1} + w_2 y_{t-2} + \dots + w_p y_{t-p} + b$$

This is **essentially the AR (linear autoregressive) model**! In other words, the autoregression of classical time series analysis is simply "linear regression on lag features". It brings three benefits:

- it is an **extremely strong forecasting baseline**, which many flashy deep models do not reliably beat;
- **the coefficients tell you directly which lags matter** — for example, a large $w_1$ shows a strong dependence on the previous period, while a large $w_7$ may indicate a weekly cycle;
- when the lag order $p$ is large and there are many features, combining it with [regularization](../regularization/) (Lasso automatically picks out the few key lags) effectively prevents overfitting.

If the linear assumption is not enough, consider more flexible [model families](../model-families/) such as [decision trees](../decision-tree/), [ensemble learning / GBDT](../ensemble-gbdt/) or kernel methods.

## Summary

- **Linear model = weighted sum of features + bias**: $\hat{y} = w^\top x + b$, the simplest and most interpretable structure.
- **Linear regression** is fitted with MSE / least squares and has the closed-form solution $w=(X^\top X)^{-1}X^\top y$; **logistic regression** outputs probabilities via a sigmoid, is trained with cross-entropy, and is used for classification.
- The coefficients $w_j$ directly reflect the importance and direction of each feature; always apply **feature scaling** first so the coefficients are comparable.
- With many features, combine with [regularization](../regularization/) → Ridge / Lasso.
- In time series, **linear regression on lag features ≈ linear autoregression (AR)**, a fast and strong baseline whose coefficients also tell you which lags matter most.

[← Machine learning foundations](../ml/) · [Foundations overview](../)
