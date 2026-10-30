---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/decision-tree/
title: "Decision Tree"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

A **decision tree** is a model made of a chain of "yes/no" questions (if-else splits): it cuts the feature space, one slice at a time, into a number of regions and gives a prediction for each region. It is intuitive and easy to interpret, and it is the basic building block of powerful models such as [random forests](../model-families/) and [GBDT](../ensemble-gbdt/).

## Intuition

Imagine playing "Twenty Questions": first you ask "Does it move?", then "Is it bigger than a cat?"… Each question cuts the possibilities in half, and after a few rounds you can pin down the answer. A decision tree does exactly this — **it breaks a complex prediction problem into a flowchart of simple questions**.

Take the example of deciding "is today a good day for an outdoor run":

```
Temperature > 32°C ?
├── Yes → don't run (too hot)
└── No  → Is it raining ?
          ├── Yes → don't run
          └── No  → Wind speed > 8 m/s ?
                    ├── Yes → don't run
                    └── No  → go for a run!
```

- Each **internal node** is a test on some feature (such as `temperature > 32`).
- Each edge is one outcome of the test (yes / no).
- Each **leaf** gives the final prediction.

The whole tree slices the feature space into "rectangular regions", and samples falling into the same region share the same prediction. This structure closely resembles the way people make decisions, which makes it **particularly easy to explain** — you can trace a path and say exactly "why the model decided this".

## How it works: recursive binary splitting

How does a tree "grow"? The core mechanism is **recursive binary splitting**:

1. Look at all the samples in the current node and try every feature and every possible split point.
2. Pick the cut that makes the child nodes "purest" and split the data in two.
3. Repeat the process on each child until a stopping condition is met (the node is pure enough, has too few samples, or the maximum depth is reached).

The key lies in step 2 — **how do we measure a "good" split**? That depends on the type of task.

**Classification**: we want each child node after the split to be as "pure" as possible (dominated by a single class). Two measures are common.

**Gini impurity**: the probability of being wrong if you draw a sample at random and then guess its class at random according to the class proportions in the node.

$$Gini = 1 - \sum_k p_k^2$$

where $p_k$ is the proportion of class $k$ in the node. When a node contains only one class, $Gini=0$ (perfectly pure); it is largest when the classes are evenly mixed.

**Entropy** and **information gain**: [entropy](../entropy/) measures the "disorder" of a node.

$$H = -\sum_k p_k \log p_k$$

The entropy before the split minus the weighted average entropy of the children after the split is the **information gain**. The larger the gain, the more this cut "tidies up" the data, and the more it is worth making.

Whether you use Gini or entropy, the idea is the same: **choose the split that makes the children purest and reduces uncertainty the most**.

**Regression**: a leaf must output a number, so instead we minimize the **variance / mean squared error (MSE)** within the child nodes:

$$\text{MSE} = \frac{1}{n}\sum_{i}(y_i - \bar{y})^2$$

We pick the cut that minimizes the weighted sum of the two children's MSE — that is, the one that keeps the $y$ values in each region as tightly clustered as possible.

**Leaves give the prediction**: a classification leaf outputs the **majority class** of its samples; a regression leaf outputs the **mean** of its $y$ values.

{% include fviz/tree-split.html %}

## Overfitting and how to control it

Decision trees have a dangerous talent: if you let one keep growing, it can memorize the training set **word for word** — every sample gets its own leaf and the training error is 0, but this is textbook [overfitting](../overfitting/), and it falls apart on new data. A tree that is too deep memorizes noise, not patterns.

Ways to control it (all in the spirit of [regularization](../regularization/): accept a bit more bias in exchange for lower variance):

- **Pruning**: grow the tree fully first, then cut off the branches that do not help on the validation set.
- **`max_depth`**: limit the maximum depth so the tree cannot ask too many rounds of questions.
- **`min_samples_leaf` / `min_samples_split`**: require each leaf (or each split) to contain at least a certain number of samples, preventing a separate leaf from being created for individual samples.

These hyperparameters should all be chosen by [cross-validation](../cross-validation/), and behind them lies the [bias–variance trade-off](../bias-variance/): the deeper and more complex the tree → low bias, high variance; limit it appropriately → find the sweet spot of best generalization.

## A concrete example (sklearn)

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

# No constraints: tends to memorize the training set
deep = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)
print("Unconstrained  train:", deep.score(Xtr, ytr), " test:", deep.score(Xte, yte))

# With depth and leaf constraints: more stable, more interpretable
clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(Xtr, ytr)
print("Limited depth  train:", clf.score(Xtr, ytr), " test:", clf.score(Xte, yte))

# Print the whole tree as text — this is what makes it interpretable
print(export_text(clf, feature_names=load_iris().feature_names))
```

You will see that the unconstrained tree's training score is often 1.0, yet its test score is not necessarily higher; and the rules printed by `export_text` let anyone read "the criteria the model uses to decide".

## Strengths and weaknesses

**Strengths**

- **Highly interpretable**: the whole tree is a set of if-else rules that you can explain directly to non-technical people.
- **No feature scaling needed**: splits only look at "greater/less than some threshold", so they are insensitive to units and need no standardization.
- **Naturally handles mixed features**: works with both numerical and categorical features, and is relatively robust to missing values and outliers.
- Automatically captures **nonlinear** relationships and **interactions between features**.

**Weaknesses**

- **High variance, unstable**: change the training data slightly and the split points may change a lot, producing a completely different tree.
- A single tree overfits easily and its accuracy is often mediocre — which is exactly why **ensembles** are used to rescue it.

## Why it matters for time series forecasting

In time series forecasting, we usually first turn the series into a table: **lag features** ($t-1, t-7, \dots$), **calendar features** (day of week, holiday or not, month) and so on serve as inputs, which are then fed to the model. On such a table, a decision tree can do two things that [linear models](../linear-model/) do poorly:

- Capture **nonlinear thresholds**, such as the turning point where "electricity demand surges once the temperature exceeds 30°C".
- Capture **feature interactions**, such as a peak that only appears on "weekend + sunny day".

But a single tree is too weak and too unstable, and is rarely used alone in practice — its real value is as the **base learner of GBDT** (see [ensemble learning / GBDT](../ensemble-gbdt/)).

There is also one **crucial warning**:

> **Trees cannot extrapolate trends.**

A tree's prediction is always the **mean of the training samples in some leaf**, so its output **can never go beyond the range of values seen during training**. If a series rises over the long run (such as steadily growing sales), then when faced with a future value higher than anything in history, the tree can only output "the highest level it has seen", and so it systematically **underestimates the trend**. For series with a clear trend, the common practice is to **detrend / difference first, then model the remainder with tree-based models**.

## Summary

- A **decision tree** cuts the feature space into regions with a chain of if-else splits, and its leaves give the predictions; it is intuitive and easy to interpret.
- It grows by **recursive binary splitting**: classification uses **Gini $Gini=1-\sum_k p_k^2$ or entropy $H=-\sum_k p_k\log p_k$**, regression minimizes the children's **variance/MSE**.
- Leaf prediction = **majority class** (classification) or **mean** (regression).
- It **overfits** easily and is controlled by **pruning, `max_depth`, `min_samples_leaf`** and similar settings (see [regularization](../regularization/), [bias–variance trade-off](../bias-variance/)).
- Strengths: interpretable, no scaling needed, handles mixed features; weaknesses: **high variance, unstable**.
- In time series it captures nonlinearity and interactions on **lag/calendar features**; a single tree is weak but is the cornerstone of [GBDT](../ensemble-gbdt/); it **cannot extrapolate trends**, so trending series should be detrended/differenced first. See also [model families](../model-families/) for its place in the family of models.

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
