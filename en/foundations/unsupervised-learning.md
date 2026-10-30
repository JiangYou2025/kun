---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/unsupervised-learning/
title: "Unsupervised Learning"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**Unsupervised learning** means that the training data has **no labels at all** — there is no "correct answer" to check against — and the model's goal is to **discover hidden structure and patterns** in the data on its own.

## Intuition

If [supervised learning](../supervised-learning/) is like "practicing with a teacher who grades your work against the answer key", then unsupervised learning is like having **no teacher**: a huge pile of data lies in front of you, nobody tells you what is right or which item belongs to which category, and you have to observe, generalize, and figure out the patterns yourself.

An everyday example: you tip a basket of unlabeled fruit onto the table, and nobody tells you what they are called. Yet you will naturally **sort them into a few piles** by "size, color, shape" — a pile of red round ones, a pile of yellow long ones. You don't know the "correct name" of each pile, but you have discovered the **organizational structure** of the data itself. That is what unsupervised learning does.

Because there are no labels, the goal of unsupervised learning is not "is the prediction right?" but "**reveal the patterns inherent in the data**".

## Main tasks

Unsupervised learning covers a few typical tasks:

- **Clustering**: automatically put similar samples in the same group. The representative [algorithm](../algorithms/) is **K-means**. See [clustering](../clustering/) for details.
- **Dimensionality reduction**: compress high-dimensional data into fewer dimensions while preserving as much information as possible, for visualization and downstream modeling. The representative method is principal component analysis; see [PCA (principal component analysis)](../pca/).
- **Anomaly detection**: find "outliers" that differ markedly from most samples, such as credit-card fraud or equipment failures.
- **Density estimation**: estimate how the data is distributed in space, to understand "where data usually appears".

## How it works (mathematical intuition)

The [optimization](../optimization/) objectives behind the different tasks differ, but all of them revolve around "measuring similarity / information":

**Clustering**: split $n$ samples into $K$ groups so that **within-group distances are as small as possible** (samples in the same group are similar to each other). K-means minimizes the sum of squared distances from every sample to the center $\mu_k$ of its cluster:

$$
\min_{\{\mu_k\}}\ \sum_{k=1}^{K}\ \sum_{x \in C_k} \lVert x - \mu_k \rVert^2
$$

where $C_k$ is the $k$-th cluster and $\mu_k$ its center.

**Dimensionality reduction (PCA)**: look for a new set of coordinate directions along which the **variance of the projected data is as large as possible** — the larger the variance, the more information is retained. This is equivalent to finding the eigenvector directions corresponding to the largest eigenvalues of the covariance matrix. The intuition: keep the few directions in which the data is "most spread out" and drop the directions where it barely varies.

Note: **the label $y$ appears in neither objective** — only the data $x$ itself. That is the hallmark of "unsupervised".

## A concrete example

A K-means clustering run with `scikit-learn`. Note that we pass only `X` and **provide no labels whatsoever**:

```python
from sklearn.cluster import KMeans
import numpy as np

# Only the inputs X, no y! Each row is a sample with two features
X = np.array([
    [1, 2], [1.5, 1.8], [1, 0.6],     # looks like one cluster
    [8, 8], [9, 11], [8.5, 9],        # looks like another cluster
])

model = KMeans(n_clusters=2, n_init=10, random_state=0)
labels = model.fit_predict(X)   # automatically splits the samples into 2 groups

print(labels)            # e.g. [0 0 0 1 1 1]
print(model.cluster_centers_)   # the centers of the two clusters
```

The model does not know what the "correct grouping" is; based only on the distances between samples, it finds the two centers of concentration by itself. PCA works similarly: `from sklearn.decomposition import PCA`, then `PCA(n_components=2).fit_transform(X)` compresses high-dimensional data down to 2 dimensions — again without needing any labels.

## Why it matters (where it is used)

In the real world, **labeled data is often expensive** — it requires manual annotation, which costs time and money — while **unlabeled data is plentiful and easy to obtain**. Unsupervised learning lets us extract value directly from this raw data:

- Use **clustering** for customer segmentation, document categorization, image grouping.
- Use **dimensionality reduction** to compress data, remove noise, and support visual exploration.
- Use **anomaly detection** to uncover fraud, intrusions, and failures.

It is often the **first step** of a modeling workflow: understand the structure of the data without supervision first, then decide how to proceed. The fundamental difference from [supervised learning](../supervised-learning/) (labeled data, learning a mapping) is simply — **whether there is an answer key**.

## Relevance to time series forecasting

Although forecasting itself is a [supervised learning](../supervised-learning/) task, unsupervised learning is a very powerful "auxiliary tool" for time series:

- **Clustering similar series/segments**: when you have hundreds or thousands of series (for example, sales across many stores), you can first **cluster** series with similar behavior into groups and model each group separately, which is often more accurate than "one model for everything".
- **Dimensionality reduction across many related series**: when there are a great many variables, use [PCA](../pca/) to compress the many correlated series into a few **principal components**, reducing both noise and computation.
- **Anomaly detection**: identify abrupt change points, sensor faults, or unusual events in a series, so they do not contaminate the training data or mislead the forecast.
- **Using cluster labels / PCA components as features**: in a supervised forecasting table, adding "which group this series belongs to" or "the first few principal components" as extra features can noticeably improve forecasts.
- **Regime detection**: identify different "regimes", such as bull/bear phases of a market or normal/abnormal operating states of a machine, so the forecasting model can adopt a different strategy for each.

In one sentence: **unsupervised learning helps you "understand" the structure of the data, and supervised learning then "makes" the forecast from it.** The two are often used together.

## Summary

- **Unsupervised learning** = the data has **no labels**; the goal is to discover hidden structure rather than predict a correct answer.
- Main tasks: **clustering** (grouping), **dimensionality reduction** (compression, e.g. PCA), **anomaly detection**, **density estimation**.
- Intuition behind the methods: clustering **minimizes within-group distance**, PCA **maximizes projected variance**, and neither objective contains the label $y$.
- Its value: unlabeled data is plentiful and easy to obtain, so structure can be mined directly for segmentation, denoising, and finding anomalies.
- In time series it is often an **auxiliary tool**: clustering series, dimensionality reduction, anomaly detection, providing extra features, regime detection — working hand in hand with [supervised learning](../supervised-learning/).

[← Machine learning foundations](../ml/) · [Foundations overview](../)
