---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/pca/
title: "PCA (Principal Component Analysis)"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**PCA (Principal Component Analysis)** is the most widely used **linear dimensionality reduction** method: it finds the **directions of greatest variance** in the data and projects high-dimensional data onto a few of those directions, keeping as much information as possible in fewer dimensions.

## Intuition

Imagine a cloud of points scattered over a plane, stretched out overall along some diagonal direction. If we **rotate the coordinate axes** so that the new first axis lines up exactly with the cloud's "longest" direction and the second axis, perpendicular to it, lines up with the next-longest direction, we find that almost all of the "spread" shows up along the first axis, while there is hardly any variation along the second.

If we then keep only the coordinate on the first axis, we have squeezed two-dimensional data into one dimension while losing almost no information. That is the core idea of PCA — **turn the coordinate system towards the directions in which the data is most spread out, then throw away the directions with almost no variation**. These new directions are called **principal components**; they are mutually **orthogonal** and sorted by "explained variance" from largest to smallest.

Why measure information by **variance**? Because a large variance means the samples are well separated along that direction and carry a lot of differences; along a direction with variance close to 0, all samples look nearly the same, so keeping it is useless.

## Principle and mathematics

The standard PCA procedure is as follows. Let the data matrix $X$ have $n$ rows (samples) and $p$ columns (features).

1. **Centering / standardization**: first subtract each feature's mean (centering). If the features are on different scales, also divide by the standard deviation (standardization). **This step is essential**; otherwise the result is skewed by the features with large values.

2. **Compute the covariance matrix** (on the centered $X$):

$$\Sigma = \frac{1}{n} X^\top X$$

where $X^\top$ is the transpose of $X$, and $\Sigma$ is a $p\times p$ symmetric matrix whose diagonal holds each feature's variance and whose off-diagonal entries are the pairwise covariances between features.

3. **Eigendecomposition**: find the **eigenvectors** and **eigenvalues** of $\Sigma$:

$$\Sigma\, v_i = \lambda_i\, v_i$$

- The **eigenvectors** $v_i$ are the directions of the **principal components** (mutually orthogonal, forming the new coordinate axes);
- The **eigenvalues** $\lambda_i$ give the **variance** of the data along $v_i$, i.e. "how much variance" that principal component explains.

Sort the eigenvalues in decreasing order $\lambda_1 \ge \lambda_2 \ge \cdots$; the corresponding eigenvectors are the first, second, … principal components.

4. **Projection**: take the first $m$ principal components to form the matrix $W=[v_1, \dots, v_m]$ and project the data onto them:

$$Z = X W$$

$Z$ is the $n\times m$ low-dimensional representation ($m < p$).

### How many principal components to keep

Use the **cumulative explained variance ratio**: the explained variance ratio of the $i$-th principal component is $\dfrac{\lambda_i}{\sum_j \lambda_j}$. Add these up from largest to smallest and see how many components it takes to reach, say, **90% or 95%** of the total variance; keep that many.

### Connection with [SVD](../svd/)

In practice one rarely performs the eigendecomposition itself; instead one applies the **singular value decomposition (SVD)** $X = U S V^\top$ directly to the centered $X$: the columns of $V$ are the principal directions, and the squared singular values $S^2$ are proportional to the eigenvalues $\lambda$. SVD is numerically more stable, and sklearn's `PCA` uses it internally.

## A concrete example

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Suppose X has many columns that are highly correlated with one another
X = np.random.RandomState(0).randn(200, 8)
X[:, 1] = X[:, 0] * 0.9 + 0.1 * X[:, 1]   # create correlation artificially

# 1) Standardize/center first — this is required
X_scaled = StandardScaler().fit_transform(X)

# 2) Fit PCA
pca = PCA(n_components=4)
Z = pca.fit_transform(X_scaled)            # Z is the reduced data (200, 4)

print("Explained variance ratio per component:", pca.explained_variance_ratio_)
print("Cumulative explained variance ratio:", np.cumsum(pca.explained_variance_ratio_))
# e.g. [0.31 0.18 0.14 0.12] -> cumulative [0.31 0.49 0.63 0.75]
```

`explained_variance_ratio_` tells you what fraction of the total variance each principal component retains, and `cumsum` helps you decide how many components are enough.

## Why it matters (where it is used)

PCA has a very wide range of uses:

- **Visualization**: squeeze dozens of dimensions down to 2–3 and draw a scatter plot to inspect [clusters](../clustering/) and outliers directly;
- **Decorrelation**: principal components are mutually orthogonal, which naturally removes linear correlation between features;
- **Compression**: approximate the original data with a few components, saving storage and computation;
- **Denoising**: directions with very small variance are often noise, and dropping them makes the signal cleaner;
- **As downstream features**: feeding the reduced components into regression / classification / forecasting models lowers the dimension, speeds up training and mitigates [overfitting](../overfitting/).

## Relevance to time series forecasting

In time series forecasting, PCA is especially well suited to situations with "too many features that are correlated with each other":

- **Compressing lag features**: when you build a large number of **lag features**, they are often highly correlated; PCA can compress them into a few components and avoid **multicollinearity**;
- **Reducing many series / factor models**: hundreds or thousands of correlated series (stocks in the same industry, sensors in the same region) can be summarized by PCA into a few **common factors (factor models)** that capture the shared drivers;
- **Denoising and speed-up**: removing low-variance directions reduces noise and can markedly speed up downstream model training.

**Important warning — avoid future leakage**: PCA "learns" its principal directions, so it must be **`fit` on the training set only**, and the same transformation then used to `transform` the validation and test sets. Split the data **by time**, and **never fit PCA on the whole series (including the future)**; otherwise future information leaks into the past, the evaluation is inflated, and the model falls apart as soon as it goes live. Likewise, the means and variances used for standardization may only come from training-set statistics.

## Summary

- **PCA** rotates the coordinate axes to find the **orthogonal directions of greatest variance (principal components)**, achieving **linear dimensionality reduction**.
- Procedure: **centering/standardization → covariance matrix $\Sigma=\frac1n X^\top X$ → eigendecomposition**, which gives the principal components (eigenvectors) and explained variances (eigenvalues); in practice it is usually implemented with **SVD**.
- Use the **cumulative explained variance ratio** to decide how many components to keep (e.g. enough to reach 90%–95%).
- **Always standardize/center first**, otherwise features on large scales dominate.
- In time series forecasting it can **compress correlated lag features, extract common factors, denoise and speed things up, and mitigate multicollinearity**; be sure to **fit on the training set only and split by time, to avoid future leakage**.

Further reading: [Clustering](../clustering/) · [Unsupervised learning](../unsupervised-learning/) · [Linear models](../linear-model/)

[← Machine learning foundations](../ml/) · [Foundations overview](../)
