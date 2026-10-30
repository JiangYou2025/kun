---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/ml/
title: "Machine Learning Foundations"
lead: "Supervised / unsupervised learning, the main model families, the training pipeline, generalization and evaluation — the basic paradigm for letting models learn from data. We only build the framework and explain the concepts."
prev: /foundations/cs/
next: /foundations/dl/
math: true
---

> This is a **concept map**: it points out "what machine learning does, what tools it has, and how to tell whether a model has learned well". In-depth [algorithms](../algorithms/) are left to dedicated textbooks.

## 1. What is machine learning?

Instead of writing rules explicitly, we **learn from data** a mapping $f_\theta: X \to y$.

- **[Supervised learning](../supervised-learning/)**: with labels, learn the mapping from inputs to outputs (regression / classification)
- **[Unsupervised learning](../unsupervised-learning/)**: without labels, find structure ([clustering](../clustering/) / dimensionality reduction)
- **[Reinforcement learning](../reinforcement-learning/)**: interact with an environment to maximize cumulative reward
- Time series forecasting is usually framed as **supervised learning** (past window → future values)

## 2. The main [model families](../model-families/)

- **[Linear models](../linear-model/)**: linear / logistic regression — a simple, interpretable starting point
- **K-nearest neighbors (KNN)**: decided by a vote of "neighbors"
- **[Decision trees](../decision-tree/)**: interpretable if-else splits
- **Ensemble methods**: random forests, [gradient boosting](../ensemble-gbdt/) (GBDT / XGBoost) — strong baselines for tabular data
- **Support vector machines ([SVM](../svm/))**: maximum-margin classification
- **Clustering and dimensionality reduction**: K-means, [PCA](../pca/)

## 3. [The training pipeline](../training-pipeline/)

- **[Loss function](../loss-function/)**: MSE / MAE for regression, [cross-entropy](../cross-entropy/) for classification
- **[Optimization](../optimization/)**: [gradient descent](../gradient-descent/) or a closed-form solution to minimize the loss
- **Data splitting**: training / validation / test
- **[Cross-validation](../cross-validation/)**: more robust hyperparameter selection (**time series require chronological splits** and must not be randomly shuffled)
- **Hyperparameter tuning**: grid / random / Bayesian search

## 4. [Generalization](../generalization/): the central challenge

The goal is to perform well on **unseen** data, not to memorize the training set.

- **Underfitting**: too simple, high bias
- **[Overfitting](../overfitting/)**: too complex, memorizes noise, high variance
- **[Bias–variance trade-off](../bias-variance/)**: finding the right level of complexity
- **[Regularization](../regularization/)**: $\ell_1$ / $\ell_2$, [early stopping](../early-stopping/), pruning — constraining the model

## 5. [Evaluation metrics](../evaluation-metrics/)

- **Regression**: MSE, RMSE, MAE, MAPE, $R^2$
- **Classification**: accuracy, precision / recall, F1, ROC-AUC
- **Key point**: metrics must match the business objective and be reported on the **test set**

---

**Key terms:** [supervised](../supervised-learning/) / [unsupervised](../unsupervised-learning/) / [reinforcement learning](../reinforcement-learning/), [linear model](../linear-model/), [decision tree](../decision-tree/), [ensembles (GBDT)](../ensemble-gbdt/), [SVM](../svm/), [clustering](../clustering/), [PCA](../pca/), [loss function](../loss-function/), [cross-validation](../cross-validation/), [overfitting](../overfitting/), [bias–variance trade-off](../bias-variance/), [regularization](../regularization/), [evaluation metrics](../evaluation-metrics/).
