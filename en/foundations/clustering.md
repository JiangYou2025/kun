---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/clustering/
title: "Clustering"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**Clustering** is an **[unsupervised learning](../unsupervised-learning/)** method: without any labels, it automatically puts samples that are similar to each other into the same group (cluster), so that "members of a group are as similar as possible, and groups are as different as possible".

## Intuition

Imagine you get a large pile of supermarket sales records, but nobody tells you which stores are "large downtown stores", "small suburban stores" or "holiday-spike stores". Clustering **lets the data speak for itself**: based on how "close" samples are in feature space, it groups nearby points together.

The key word here is **similarity**, usually measured by a **distance**. The closer two samples are, the more likely they belong to the same cluster. The most common choice is the **Euclidean distance**:

$$d(x, y) = \sqrt{\sum_{i=1}^{p}(x_i - y_i)^2}$$

where $x, y$ are two samples (each with $p$ features). Unlike **[supervised learning](../supervised-learning/)** (which has a ground truth), clustering has no "correct grouping"; whether the result is good must be judged by business meaning and metrics together.

## How it works: the K-means [algorithm](../algorithms/)

The most classic and widely used clustering algorithm is **K-means**. You first specify the number of clusters $k$, and the algorithm then iterates:

1. **Randomly initialize** $k$ centers (centroids) — for example, pick $k$ samples at random as starting points;
2. **Assign**: assign each point to the cluster represented by its **nearest center**;
3. **Update**: recompute each cluster's center as **the mean of all points in that cluster**;
4. **Repeat** steps 2 and 3 until the centers no longer move noticeably (**convergence**).

Intuitively, this is a back-and-forth tug between "assign" and "update": points follow their nearest center, centers are pulled to the average position of their points, and eventually everything settles.

### What it minimizes

K-means actually minimizes the **within-cluster sum of squares (WCSS)**, also called the **inertia**:

$$J = \sum_{j=1}^{k}\sum_{x\in C_j}\|x-\mu_j\|^2$$

Symbol by symbol:

- $k$: the total number of clusters (which you specify);
- $C_j$: the set of all samples in the $j$-th cluster;
- $x$: a sample (a vector) belonging to cluster $C_j$;
- $\mu_j$: the center of the $j$-th cluster, equal to the mean of all its $x$;
- $\|x-\mu_j\|^2$: the **squared Euclidean distance** from a sample to its center;
- the double sum: first add up the squared distances from all points to their center within each cluster, then sum over all clusters.

The smaller $J$, the more tightly the points in each cluster gather around their center, and the more "solid" the clusters. The "assign" step lets each point choose its nearest center, and the "update" step places each center at the mean — both steps decrease $J$, so the algorithm is guaranteed to converge (but possibly to a **local optimum**, which is why it is common to run several times with different initializations and keep the best; sklearn does this by default).

{% include fviz/kmeans.html %}

## How to choose k

You have to pick $k$ yourself — so how do you choose it sensibly? Two common tools:

- **The elbow method**: plot $J$ (the inertia) for different values of $k$. The larger $k$, the smaller $J$, but the decrease slows down; the $k$ where the curve shows a clear "bend" (like an elbow) is often the most cost-effective choice.
- **The silhouette coefficient**: for each sample compute $s = \dfrac{b - a}{\max(a, b)}$, where $a$ is its average distance to the other points in **its own cluster** and $b$ its average distance to the points of the **nearest other cluster**. The closer $s$ is to 1, the better the separation; close to 0 means the sample lies on a boundary; negative means it may have been misassigned. Choose the $k$ with the highest average silhouette coefficient over all samples.

## A concrete example

Run K-means with scikit-learn (note: **standardize first**):

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([[1.0, 2.0], [1.2, 1.8], [5.0, 8.0],
              [5.2, 8.1], [9.0, 1.0], [8.7, 1.2]])

# 1) Standardize: give each feature mean 0 and variance 1, so features with large scales don't dominate the distance
X_scaled = StandardScaler().fit_transform(X)

# 2) Train KMeans; n_init=10 means try 10 different initializations and keep the best result
km = KMeans(n_clusters=3, n_init=10, random_state=0)
labels = km.fit_predict(X_scaled)

print("Cluster label of each sample:", labels)        # e.g. [0 0 1 1 2 2]
print("Cluster centers:", km.cluster_centers_)
print("Within-cluster sum of squares (inertia):", km.inertia_)
print("Silhouette coefficient:", silhouette_score(X_scaled, labels))
```

`fit_predict` returns the cluster each sample belongs to; `inertia_` is the $J$ above; `silhouette_score` helps you assess whether this $k$ is a good choice.

## Limitations and other methods

K-means is simple and efficient, but keep its assumptions in mind:

- **It assumes clusters are "spherical" and of similar size**: on elongated, ring-shaped or very unevenly dense clusters, K-means does poorly;
- **It is sensitive to initialization**: it can get stuck in a local optimum (mitigated by `k-means++` initialization and multiple `n_init` runs);
- **It is sensitive to scale**: distances are dominated by features with large values, so you **must standardize the features first**;
- **$k$ must be specified in advance**, and it is also fairly sensitive to outliers.

Alternatives:

- **Hierarchical clustering**: no need to fix $k$ in advance; it repeatedly merges (or splits) clusters to build a tree diagram (a **dendrogram**), which you can "cut" at any height to get the number of clusters you want. It suits situations where you want to see nested structure.
- **DBSCAN**: **density**-based clustering that can find clusters of arbitrary shape and automatically labels points in sparse regions as **noise/outliers**. It does not need $k$, but parameters such as the neighborhood radius must be tuned well.

## Relevance to time series forecasting

Clustering is very useful in time series forecasting:

- **Similar series share a model**: group stores, sensors or users with similar behavior into a few classes and train one model per class (instead of one per series for thousands of series), which saves compute and is more robust;
- **Identifying states/regimes**: cluster different time periods by their features to distinguish **regimes** such as "calm period / high-volatility period / promotion period", which makes piecewise modeling easier;
- **As a feature**: feed the **cluster id** to the downstream forecasting model as a categorical feature, so the model knows "which class this series belongs to".

A few reminders: **always standardize** before clustering; for raw time series waveforms, plain Euclidean distance is not necessarily appropriate — consider an alignment distance such as **dynamic time warping (DTW)**, or first extract statistical features (mean, volatility, trend, strength of periodicity) and then cluster.

## Summary

- **Clustering** groups similar samples without supervision, measuring closeness by **distance/similarity**.
- **K-means** iterates "assign to the nearest center — update to the cluster mean", minimizing the **within-cluster sum of squares** $J=\sum_j\sum_{x\in C_j}\|x-\mu_j\|^2$.
- To choose $k$, use the **elbow method** and the **silhouette coefficient**; always **standardize** the features first.
- K-means assumes spherical clusters and is sensitive to initialization and scale; **hierarchical clustering** and **DBSCAN** are common alternatives.
- In time series forecasting it can be used to **group similar series to share models**, **identify regimes** and **serve as a feature** — remember to standardize and choose the right distance.

Further reading: [Unsupervised learning](../unsupervised-learning/) · [PCA (principal component analysis)](../pca/) · [Linear models](../linear-model/)

[← Machine learning foundations](../ml/) · [Foundations overview](../)
