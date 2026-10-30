---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2001 · Computing"
permalink: /en/history/e/gbdt/
title: "Gradient Boosting (Friedman, 2001)"
lead: "If “training a model” is seen as gradient descent in function space, which way should each step go? Friedman's answer: fit the negative gradient of the previous step — and take the step with a tree."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 8 · Machine Learning](../../08/).

### Background

In the late 1990s, two lines of **ensemble learning** rose side by side: Breiman's bagging and random forests (parallel, reducing variance) and Freund–Schapire's AdaBoost (sequential, reducing bias). AdaBoost worked astonishingly well, yet "why it works" long remained a mystery. In 1999–2001 Friedman offered a unified and profound view: boosting is essentially **gradient descent** in **function space**. From this came the **Gradient Boosting Machine (GBM/GBDT)**, which became one of the strongest baselines for tabular data and feature-based time series forecasting.

### The problem

A single decision tree is easy to interpret but has limited expressive power and high variance; to be both accurate and stable, many weak models must be combined. AdaBoost corresponds only to the special case of exponential loss and cannot be applied directly to regression, quantile, Poisson or other **arbitrary differentiable losses**. The core question was: **given any loss function, how can weak learners be stacked, systematically and step by step, into a strong learner?**

### Other approaches of the time (and their limits)

- **AdaBoost**: pioneering, but tied to the exponential loss, **sensitive to outliers and label noise**, and poorly explained.
- **Random forests (bagging)**: parallel, resistant to overfitting and easy to use, but they only reduce variance, do not actively reduce bias, and cannot be targeted at a custom loss.
- **Neural network regression**: expressive, but at the time training was unstable and tuning expensive on small and medium tabular or time series data, and they often fell short of tree ensembles.

### Method

Treat the prediction function $$ F(x) $$ as the object to optimize, with the goal of minimizing the expected loss $$ \sum_i L(y_i, F(x_i)) $$. At step $$ m $$, first compute for each sample the **negative gradient** of the loss with respect to the current prediction (the "pseudo-residuals"):

$$ r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}} $$

For squared loss this is exactly the ordinary **residual** $$ y_i - F_{m-1}(x_i) $$; for other losses it is its generalization. Then train a **regression tree** $$ h_m(x) $$ to fit these pseudo-residuals, and update the model with a step size (learning rate) $$ \nu $$:

$$ F_m(x) = F_{m-1}(x) + \nu\, \gamma_m\, h_m(x) $$

where $$ \gamma_m $$ is determined by a line search. The whole procedure moves through function space along the negative gradient, using "one tree" as the approximate descent direction for each step. Combined with **shrinkage** $$ \nu<1 $$, **row/column subsampling** and limits on tree depth as regularization, it resists overfitting effectively.

### Impact

GBDT has long dominated structured/tabular data: Kaggle competitions, risk control, recommendation and search ranking — it is everywhere. Later engineered implementations, **XGBoost (2016)**, **LightGBM** and **CatBoost**, pushed it to the limit with second-order approximations, histogram-based splits and leaf-wise growth. For time series, turning a series into features through sliding windows, lags, rolling statistics and calendar/holiday variables and then handing them to a GBDT is often a **strong baseline** that is hard to beat — in large forecasting competitions such as M5, LightGBM-style solutions ranked at the top.

### Significance and outlook

Friedman's insight — **viewing learning as gradient descent in function space** — goes beyond trees themselves. It is a bridge between boosting and modern optimization, and echoes the same spirit as deep learning's "iterative approximation along the gradient". In time series, GBDT together with [SVR](../svr/) established the "**features + strong learner**" paradigm; facing deep sequence models ([RNN/LSTM](../lstm/) and even Transformers), a well-tuned GBDT is still often the honest threshold for testing whether "depth is worth it". Simple, robust and interpretable, it has stood the test of time.
