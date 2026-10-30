---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/svm/
title: "SVM (Support Vector Machine)"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**The SVM (Support Vector Machine)** is a method for classification (it can also do regression). Its core idea is to find the boundary between two classes that has the **largest margin**; with the help of the **kernel trick**, it can also handle nonlinear problems with ease.

## Intuition

Suppose there are two clusters of points on a plane, one red and one blue, and you need to draw a line that separates them. There are infinitely many lines that can do it — but which one is the "best"?

The SVM's answer is: **find the line that keeps both classes as far from it as possible**. Picture building the **widest possible street** between the two classes: the line down the middle of the street is the decision boundary, and the width of the street is the **margin**. The wider the street, the more "room to spare" the model has when judging new data, and the better its **[generalization](../generalization/)**.

What actually determines the width and position of the street are only the few **points touching the edges of the street** — these are called **support vectors**. The other, more distant points can move around without affecting the result at all. That is where the SVM gets its name, and it is one of its defining features: **the model is determined by only a handful of key samples**.

## How it works: the maximum margin

Let the decision surface (a hyperplane) be

$$w^\top x + b = 0$$

For a point $x$, the sign of $w^\top x + b$ tells us which side of the decision surface it lies on. One can derive that the **margin** between the two edges is

$$\text{margin} = \frac{2}{\|w\|}$$

Making the margin **as large as possible** is equivalent to making $\|w\|$ **as small as possible**. The SVM's optimization objective can therefore be written in an elegant form:

$$\min_{w,b}\ \frac{1}{2}\|w\|^2 \quad \text{s.t.}\quad y_i\,(w^\top x_i + b) \ge 1,\ \forall i$$

Here $y_i \in \{-1, +1\}$ is the class label. The constraint $y_i(w^\top x_i + b)\ge 1$ means "every point must stay on the correct side of the street, outside its edge". The points that **lie exactly on the edge** (where equality holds) are the **support vectors**.

## Soft margin and the parameter C

Real data is often noisy and overlapping, and insisting that "every point is classified correctly" can make the margin very narrow, or leave the problem with no solution at all. Hence the **soft margin**: a few points are allowed to cross the boundary, but at a price. The optimization objective becomes

$$\min_{w,b}\ \frac{1}{2}\|w\|^2 + C\sum_i \xi_i$$

where $\xi_i \ge 0$ is each point's **slack variable**, measuring how far it crosses the boundary, and $C$ is the **penalty coefficient (the [regularization](../regularization/) parameter)**, which controls the trade-off:

- **Large C** → violations are heavily penalized → the model tries to classify every point correctly → narrow margin, prone to **[overfitting](../overfitting/)**;
- **Small C** → more violations are tolerated → wider margin, more robust, but possibly **underfitting**.

So $C$ essentially balances "margin width" against "classification errors", and it is a key hyperparameter that must be tuned.

## The kernel trick

What if the data simply cannot be separated by a straight line? The SVM's secret weapon is the **kernel trick**: it maps the data **implicitly** into a higher-dimensional space where it may become linearly separable — and it does so **without actually computing the high-dimensional coordinates**. All it needs is a **kernel function** $K(x_i, x_j)$ that replaces the inner product in the high-dimensional space. Common kernels:

- **Linear kernel**: $K(x, x') = x^\top x'$, which gives the ordinary linear SVM.
- **Polynomial kernel**: $K(x, x') = (x^\top x' + c)^d$, which can fit polynomial-shaped boundaries.
- **RBF (Gaussian) kernel**: $K(x, x') = \exp(-\gamma\|x - x'\|^2)$, the most widely used and most flexible. $\gamma$ controls each point's "radius of influence": large $\gamma$ → small range of influence, a wiggly boundary, prone to overfitting; small $\gamma$ → a smooth boundary.

For regression tasks there is **SVR (Support Vector Regression)**. The idea is symmetric: instead of asking for "no points inside the margin", it lets predictions fall within a "tube" of width $\varepsilon$ around the true values and penalizes only the points that leave the tube.

## A concrete example (sklearn)

```python
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=200, noise=0.2, random_state=0)  # nonlinear data

# Standardize first, then apply an RBF-kernel SVM — standardization is crucial for SVMs
clf = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1.0, gamma="scale")   # C and gamma are the key hyperparameters
)
clf.fit(X, y)

print("Accuracy:", clf.score(X, y))
print("Number of support vectors:", clf.named_steps["svc"].n_support_)
```

Note that **feature scaling (StandardScaler)** must come first: kernel functions (especially RBF) depend on distances between samples, and inconsistent units let features with large values "drown out" the others.

## Why it matters (where it is used)

- It performs very well on **small-to-medium, high-dimensional** data — text classification and bioinformatics, where there are "many features but not that many samples", were once the SVM's home turf.
- The **maximum margin** brings good generalization and a degree of robustness to noise.
- The kernel trick lets it capture complex **nonlinear** relationships without explicitly lifting the data into higher dimensions.
- It belongs to a different [model family](../model-families/) from [decision trees](../decision-tree/) and [ensemble learning / GBDT](../ensemble-gbdt/); each excels on different kinds of data, so they are worth trying side by side.

## Relevance to time series forecasting

For time series, you can forecast with **SVR + lag features**: use the past few values $y_{t-1}, \dots, y_{t-p}$ as inputs and predict $y_t$. Compared with a linear autoregression, an SVR with an RBF kernel can capture **nonlinear relationships** between the lag features. Practical points:

- **Always scale the features** — for SVM/SVR this is not optional, it is required.
- **The choice of kernel** determines how complex the patterns it can express are; RBF is the default first choice.
- **Tuning C and gamma is critical**, usually by grid search with [cross-validation](../cross-validation/); get them wrong and it is easy to overfit or underfit.
- Keep in mind that SVMs are **slow on large data** (training cost grows roughly with the square of the number of samples, or faster). When the data is very large, [ensemble learning / GBDT](../ensemble-gbdt/) is often both fast and accurate, and the more practical choice.

## Summary

- **SVM = finding the separating hyperplane with the largest margin**: $w^\top x + b = 0$, margin $=\frac{2}{\|w\|}$, maximizing the margin ⇔ minimizing $\frac12\|w\|^2$.
- **Support vectors** are the key samples lying on the edge of the margin; the model is determined by them alone.
- **Soft margin + parameter C** trade off "margin width" against "classification errors".
- **The kernel trick** (linear / polynomial / RBF) lifts the data implicitly to handle nonlinearity; the regression version is **SVR**.
- Well suited to small-to-medium, high-dimensional data; for time series you can use **SVR on lag features**, but you must **scale the features and carefully tune C and gamma**, and on large data it is less efficient than [GBDT](../ensemble-gbdt/).

[← Machine learning foundations](../ml/) · [Foundations overview](../)
