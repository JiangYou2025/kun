---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/model-families/
title: "Model Families"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**Model families** are the main classes of models in [machine learning](../ml/) — linear models, decision trees and ensembles, SVMs, k-nearest neighbors (kNN), and [neural networks](../neural-network/). Each family rests on different **assumptions**, and so each has the settings where it shines. This lesson does not dig deep into any single model; instead it draws a "**map**" with you: the core idea of each family, its strengths and weaknesses, and when to choose it.

## Intuition

Beginners often ask: "Which model is the best?" The answer is: **there is no "best model", only "the model best suited to the task at hand"**.

Behind this lies a famous theorem, the **No Free Lunch Theorem**: averaged over all possible problems, any two [algorithms](../algorithms/) perform equally well. In other words, a model is strong on a given task because its **assumptions (its inductive bias)** happen to match the true regularities of that task; on another task, the same assumptions may become a burden.

So the right mindset is not "find the silver bullet" but: **understand what each family of models assumes**, then check whether your data satisfies those assumptions. Below we take a "guided tour", family by family.

## A concrete example: several families on the same map

Imagine a binary classification task — red and blue points on a plane, and we must draw a boundary to separate them. Different model families draw boundaries of completely different shapes:

- A **linear model** draws a **straight line** (a hyperplane in higher dimensions);
- A **decision tree** draws a set of **horizontal and vertical steps** (axis-aligned rectangular blocks);
- An **SVM** with a kernel can draw a **smooth curve**, while trying to keep the boundary "far" from both classes;
- **kNN** produces a boundary that **hugs the data**, winding wherever the data goes;
- A **neural network** can draw **arbitrarily complex curves**, given enough data.

The same data, five "worldviews". That is the most intuitive picture of what "model families" means.

{% include fviz/model-families.html %}

## A tour of the model families

### Linear models

- **Core idea**: take a **linear combination** of the features, $\hat{y}=w_1x_1+\dots+w_dx_d+b$, then (for classification) pass it through a sigmoid.
- **Strengths**: **interpretable** (each weight $w_i$ is that feature's effect), fast to train, the **baseline** you should run first on almost any task.
- **Weaknesses**: limited expressiveness, helpless with **non-linear** relationships; **sensitive to feature scale**, so standardization (scaling) is usually needed first.
- **Best for**: features roughly linear in the target, a need for interpretability, high-dimensional data with possibly few samples. See [Linear models](../linear-model/).

### Decision trees and ensembles

- **Core idea**: cut the feature space into small blocks with a series of **if-else** rules and give each block a prediction. A single tree is a [decision tree](../decision-tree/); combining many trees gives [ensemble learning / GBDT](../ensemble-gbdt/).
- **Strengths**: naturally handle non-linearity and feature interactions, need no standardization, cope with mixed feature types; **GBDT and random forests are among the strongest baselines on tabular data**.
- **Weaknesses**: a single tree has **high variance** (prone to [overfitting](../overfitting/)) and is sensitive to small changes in the training data; most importantly, tree models **cannot extrapolate trends** — their predictions always stay within the range seen during training.
- **Best for**: structured/tabular data, complex feature relationships, high out-of-the-box accuracy.

### Support vector machines (SVM)

- **Core idea**: find a **maximum-margin** separating boundary that stays as far as possible from the nearest samples; use a **kernel** function to map the data implicitly into a high-dimensional space and so handle non-linearity.
- **Strengths**: excellent on **small-to-medium, high-dimensional** problems, elegant theory, strong generalization.
- **Weaknesses**: slow to train on **large datasets** (cost grows quickly with the number of samples), kernel and parameters need tuning, middling interpretability.
- **Best for**: few samples but many dimensions (e.g. text, genetic data). See [SVM](../svm/).

### k-nearest neighbors (kNN)

- **Core idea**: **lazy learning** — do nothing at training time; at prediction time, find the $k$ nearest neighbors and let them vote or average. Entirely based on **distance**.
- **Strengths**: extremely simple idea, no training needed, naturally supports multi-class problems.
- **Weaknesses**: slow predictions (distances to all points must be computed every time), sensitive to the distance metric and to feature scales, and especially hurt by the **curse of dimensionality** — in high dimensions, "nearest" and "farthest" become almost indistinguishable.
- **Best for**: low dimensions, small data, quick prototypes or baselines.

### Neural networks

- **Core idea**: stack many layers of **linear transformation + non-linear activation**, learning feature representations from data end to end.
- **Strengths**: extremely expressive and flexible; far ahead of the field on unstructured data such as **images, text and sequences**.
- **Weaknesses**: **data-hungry**, costly to train, complex to tune, hard to interpret.
- **Best for**: large datasets, complex tasks, rich raw signals (pixels, characters, waveforms).

## A comparison table

| Model family | Core idea | Strengths | Weaknesses | Best for |
|---|---|---|---|---|
| Linear models | Linear combination of features | Interpretable, fast, good baseline | Struggles with non-linearity | Near-linear, interpretability needed |
| Trees/ensembles | if-else partitioning | Strong on tabular data, no scaling | High variance (single tree), no extrapolation | Structured/tabular data |
| SVM | Maximum margin + kernel | Strong on high-dim small samples | Slow on big data | High-dim, small samples |
| kNN | Nearest-neighbor vote | Minimal, no training | Curse of dimensionality, slow prediction | Low-dim, small data |
| Neural networks | Many non-linear layers | Very flexible, strong on unstructured data | Data-hungry, hard to interpret | Images/text/sequences |

## Why it matters: how to choose

Faced with a new task, you can "filter" with these questions:

1. **How much data is there?** With little data, favor linear models/SVMs/trees; consider neural networks only with lots of data.
2. **Is it tabular data?** Yes — GBDT is usually the first choice; no (images/text/speech) — neural networks.
3. **Is interpretability needed?** Yes — a linear model or a single tree; no — ensembles or neural networks are fine.
4. **Is the relationship highly non-linear?** Yes — trees/kernel SVMs/neural networks; roughly linear — a linear model is enough.
5. **What are the training and deployment costs?** With limited resources, do not reach for a big network right away.

Remember the **No Free Lunch Theorem**: rather than agonizing over which is stronger in theory, **compare them on your own data with [cross-validation](../cross-validation/)**.

## Relevance to time series forecasting

In time series forecasting, each of these families has its place:

- **Linear autoregression (e.g. AR)**: predicts the future as a linear combination of the past few steps; the most classic **baseline**, and the one to run first.
- **GBDT with feature engineering**: turn "lagged values, moving averages, holidays, day of week" and so on into features for a GBDT — today this is **one of the strongest methods for tabular time series forecasting**, used by the winners of many forecasting competitions. But beware that it **cannot extrapolate trends**: a series with a long-term upward trend should be differenced first.
- **Neural networks ([RNN](../rnn/) / [LSTM](../lstm/) / [Transformer](../transformer/))**: excel at **complex, long-range, multivariate** sequences and are very powerful when data is plentiful, but they are costly and prone to overfitting.

The golden rule in practice: **start with a simple baseline (linear/GBDT), get it working and quantify its error, then decide whether to upgrade to a neural network**. Often the simple baseline is already good enough.

## Summary

- **There is no best model, only the most suitable one** — that is the spirit of the No Free Lunch Theorem.
- Each family wins through different **assumptions**: linear models through linearity, trees through partitioning, SVMs through margins, kNN through distance, neural networks through stacked non-linearities.
- Choose based on five points: **data size, whether the data is tabular, interpretability, degree of non-linearity, training cost**.
- For time series: **linear autoregression as the baseline → GBDT with features → neural networks only for complex, long sequences**.
- Always go **simple first, then complex**, and validate on your own data with cross-validation.

Further reading: [Linear models](../linear-model/) · [Decision trees](../decision-tree/) · [Ensemble learning / GBDT](../ensemble-gbdt/) · [SVM](../svm/) · [Supervised learning](../supervised-learning/) · [Unsupervised learning](../unsupervised-learning/)

---

[← Machine learning foundations](../ml/) · [Foundations overview](../)
