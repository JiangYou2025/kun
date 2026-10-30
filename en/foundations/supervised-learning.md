---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/supervised-learning/
title: "Supervised Learning"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Supervised learning** means that every sample in the training data comes with a "reference answer" (a label), and the model's task is to learn a mapping rule from **input** to **output**, so that it can also give the correct output when it sees new inputs.

## Intuition

Imagine a student working through an exercise book where the **correct answer** is printed next to every problem. The student reads the problem (the input), writes down an answer, then checks it against the reference answer and adjusts their reasoning whenever they got it wrong. The more problems they do, the more accurate they become on similar problems next time.

Supervised learning is exactly this process:

- **The problem** = the input features $x$ (for example a house's floor area and number of rooms).
- **The reference answer** = the label $y$ (for example the house's actual sale price).
- **The student's way of solving it** = the model $f$.
- **Checking answers and correcting mistakes** = measuring the error with a **[loss function](../loss-function/)**, then adjusting the model.

The key point: someone (or some source) must have prepared the answers in advance. Without labels, it isn't supervised learning — that is called [unsupervised learning](../unsupervised-learning/).

## Mathematical formulation

We have a labelled **dataset**:

$$
\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}
$$

where each $x_i \in X$ is an input (a single number or a vector) and each $y_i \in Y$ is the corresponding correct output. The goal is to learn a function:

$$
f: X \to Y
$$

such that $f(x_i)$ is as close as possible to $y_i$. How do we measure "close"? With a **loss function** $L(\hat{y}, y)$, which scores "the gap between the prediction $\hat{y}=f(x)$ and the true value $y$". Training means driving the average loss over all samples as low as possible:

$$
\min_{f}\ \frac{1}{n}\sum_{i=1}^{n} L\big(f(x_i),\, y_i\big)
$$

- For tasks that predict continuous values, the **mean squared error (MSE)** is common: $L(\hat{y}, y) = (\hat{y}-y)^2$.
- For tasks that predict categories, classification losses such as **[cross-entropy](../cross-entropy/)** are common.

## The two main subtypes: regression and classification

Supervised learning splits into two big families according to "the type of the output $y$":

- **Regression**: $y$ is a **continuous value**. Examples: predicting house prices from floor area, predicting tomorrow's sales from historical sales, predicting temperature. The output is a real number.
- **Classification**: $y$ is a **discrete category**. Examples: deciding whether an email is spam (yes/no), recognizing whether a picture shows a cat or a dog, deciding whether a transaction is fraudulent. The output is a label.

One sentence to tell them apart: **asking "how much" is regression; asking "which class" is classification.**

## A concrete example

Train the simplest possible regression model with [Python](../python/)'s `scikit-learn` — predicting house prices from floor area:

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Input X: floor area of the house (square metres), one sample per row
X = np.array([[50], [60], [80], [100], [120]])
# Label y: the corresponding sale price (in units of 10,000 yuan) — this is the "reference answer"
y = np.array([150, 175, 230, 280, 330])

model = LinearRegression()
model.fit(X, y)          # Learn f: area -> price

print(model.predict([[90]]))   # Predict the price of a 90 m² house
```

The `fit` step is "practising against the reference answers": the model automatically finds the straight line that best fits the data, minimizing the mean squared error between predicted and actual prices. For a classification task, just replace `LinearRegression` with `LogisticRegression` and make `y` a category label (such as 0/1).

## Why it matters (where it is used)

Supervised learning is the **most widely applied and most mature** branch of [machine learning](../ml/). Whenever you can collect paired data of "input + correct answer", you can almost always apply it: credit scoring, medical diagnosis, recommender systems, speech recognition, machine translation… It stands in contrast to the other two major paradigms:

- [Unsupervised learning](../unsupervised-learning/): the data has **no** labels, and the goal is to discover hidden structure (such as [clustering](../clustering/) and dimensionality reduction).
- [Reinforcement learning](../reinforcement-learning/): there are no ready-made answers; learning happens by trial and error through **rewards from interacting with an environment**.

Supervised learning works so well precisely because "clear answers" make the training objective very clear, and evaluation is straightforward too — just check whether the predictions on unseen samples are right.

## Relevance to time series forecasting

This is the single most important point of this lesson: **time series forecasting is, at heart, supervised learning.** On the surface a time series is just a string of numbers with no labels, but we can "supervise" it with a **sliding window** — artificially constructing paired $(X, y)$ data.

Here's how: take the values at the previous $k$ consecutive time steps as the features $X$, and the immediately following value $y_t$ as the label:

$$
X = [\,x_{t-k},\, \dots,\, x_{t-2},\, x_{t-1}\,] \quad\Longrightarrow\quad y = x_t
$$

A concrete numerical example. Suppose the raw series is:

```
Time:   1   2   3   4   5   6   7
Value: 10  12  13  15  16  18  19
```

With a window length of $k = 3$, slide forward in time and the series turns into a **supervised learning table**:

| Features $x_{t-3}, x_{t-2}, x_{t-1}$ | Label $y = x_t$ |
| :--- | :--- |
| 10, 12, 13 | 15 |
| 12, 13, 15 | 16 |
| 13, 15, 16 | 18 |
| 15, 16, 18 | 19 |

With this table, the forecasting problem becomes exactly the regression problem described above: learn an $f$ that takes three historical values as input and outputs the next value. From there, linear regression, tree models or [neural networks](../neural-network/) can all be trained on it directly.

**A detail you must not miss: split by time.** For evaluation, you cannot randomly shuffle and then split into training/test sets as in ordinary supervised learning, because that lets the model "peek at the future". The correct approach is to **split in time order** — train on earlier data and test on later data, simulating the real situation of "standing in the present and predicting the future".

## Summary

- **Supervised learning** = labelled data, learning a mapping $f$ from input $x$ to output $y$, trained by minimizing a **loss function**.
- Two main subtypes: **regression** (continuous output, asks "how much") and **classification** (discrete categories, asks "which class").
- It contrasts with [unsupervised learning](../unsupervised-learning/) (no labels, find structure) and [reinforcement learning](../reinforcement-learning/) (trial and error via rewards).
- **Time series forecasting is supervised learning**: use a **sliding window** to turn the series into an $(X, y)$ table and predict the future from the past.
- Always **split by time** for evaluation, to avoid "peeking" caused by training on future data.

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
