---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/training-pipeline/
title: "The Training Pipeline"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

**The training pipeline** is the **end-to-end workflow** that runs from defining the task and the loss, through splitting and validating the data, all the way to tuning hyperparameters, final evaluation and deployment. It is not an algorithm but a **standard "assembly line / sequence of steps" for doing machine learning**.

## Intuition

Think of training a model as **cooking a dish**: you don't just start stir-frying at random. You first decide what dish to make (the task), prepare and wash the ingredients (the data), follow the recipe step by step (the pipeline), taste and adjust the seasoning along the way (tuning), and check the flavor one last time before serving (evaluation on the test set).

Machine learning is the same. The most common beginner mistake is to **focus only on "which model to pick and which parameter to tune"** while ignoring the whole process before and after. In fact, **a disciplined pipeline often matters more for success than switching to a fancier model** — because the pipeline hides countless traps that let you "fool yourself" (data leakage above all).

This lesson takes the pipeline apart, one step at a time.

## The standard steps (in order)

**1. Define the problem and the metric.** First be clear: what are you predicting? Is it regression or classification? Which [evaluation metric](../evaluation-metrics/) defines "good" (RMSE? accuracy? MAPE?)? The metric must be fixed before you start; otherwise it is all too easy later to "pick a flattering metric to brag with".

**2. Prepare the data.** This includes **cleaning** (handling missing values, outliers and duplicates), **feature engineering** (constructing useful input features), and **standardization / normalization** (bringing features measured in different units onto comparable scales). This step usually takes the most time and has the largest effect on results.

**3. Split the data.** Divide the data into three parts: **training / validation / test sets** (see the next section). Ordinary data can be split at random; but **time series must be split by time** — this is the single most important point.

**4. Choose a model + define the loss function.** Pick a [model family](../model-families/) ([linear models](../linear-model/), trees, neural networks…) and choose a [loss function](../loss-function/) — it defines "what counts as wrong" during training. The model and the loss must match the task.

**5. Train (fit the parameters).** Run an optimization algorithm (usually [gradient descent](../gradient-descent/)) on the **training set**, adjusting the parameters again and again to lower the loss and "fit" the model to the data.

**6. Validate and tune hyperparameters.** **Hyperparameters** (the [learning rate](../learning-rate/), tree depth, regularization strength $\lambda$, and so on) cannot be learned on the training set; they must be chosen on the **validation set**. [Cross-validation](../cross-validation/) is commonly used to estimate performance more reliably, together with **grid search** or **random search** to try different combinations systematically.

**7. Final evaluation on the test set.** Once the model and hyperparameters are chosen, run it once on the **never-touched test set** to obtain an honest estimate of true [generalization](../generalization/). **The test set can be used only once** — look at it a few more times and it has "leaked", and the estimate can no longer be trusted.

**8. Deploy and monitor.** After going live you must keep watching: the real world changes (**concept drift**), the model gradually degrades, and it needs **periodic retraining**.

## The roles of the three datasets

This is the backbone of the whole pipeline, so keep them clearly apart:

| Dataset | Who uses it | Role |
|---|---|---|
| **Training set (train)** | The model's parameters | **Learn** — gradient descent fits the parameters on it |
| **Validation set (validation)** | You (the person tuning) | **Select** — compare different hyperparameters/models and pick the best |
| **Test set (test)** | Nobody, until the very end | **Examine** — a one-time, honest estimate of generalization |

An easy-to-remember analogy: the training set is the **workbook you practice with every day**, the validation set is the **mock exam** (used to adjust your revision strategy), and the test set is the **final national exam** (taken only once — peeking at it in advance is cheating). If you repeatedly use the test set to pick models, it degrades into a second validation set, you **[overfit](../overfitting/) to the test set**, and you end up overly optimistic about real-world performance.

## The biggest trap: data leakage

**Data leakage** means **information the model should never have seen sneaks into training** (especially future information or test-set information), so offline metrics look absurdly good and everything collapses once deployed.

The most classic case: **standardizing or selecting features before splitting**. For example, if you compute the mean and variance on **all the data** to standardize it, the training set has "peeked" at the statistics of the validation/test sets — that is leakage.

The right way: **every preprocessing step that "learns something from the data" must be fit on the training set only, and then used to transform the validation/test sets**.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Bundle "standardization + model" into one Pipeline —
# key benefit: in cross-validation the scaler is fit only on each fold's training part, avoiding leakage automatically
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  Ridge()),
])

param_grid = {"model__alpha": [0.1, 1.0, 10.0]}   # tune the regularization-strength hyperparameter

grid = GridSearchCV(pipe, param_grid, cv=5, scoring="neg_mean_squared_error")
grid.fit(X_train, y_train)        # cross-validate on the training set only to choose hyperparameters

print(grid.best_params_)
# The test set is used only once, at the very end:
final_score = grid.score(X_test, y_test)
```

The essence of using a `Pipeline` is that it guarantees steps like standardization are **"locked inside" the training part of each fold**, so no information from the validation/test data can leak in. Calling `fit_transform` by hand on the whole `X` is the leakage mistake beginners make most often.

## Relevance to time series forecasting

The time series training pipeline has a few **special but mandatory** rules, because the data has a **temporal order** and cannot be shuffled at random like ordinary data.

- **You must split in chronological order.** The training set comes first and the test set after (for example, train on the first 80% of the time span and test on the last 20%). **Never shuffle at random** — otherwise you are "using the future to predict the past", a textbook case of leakage.
- **Use time series cross-validation (walk-forward / rolling).** Ordinary K-fold cannot be used (it scrambles the time order); instead, move **step by step forward**: each time, "train on the past and predict the immediately following future", then roll the window forward. Only then does validation match the real forecasting scenario. See [cross-validation](../cross-validation/) for details.
- **Guard feature engineering against future leakage.** When building **rolling statistics** (moving average, moving standard deviation, and so on), **use only data from before the current time step**. If your moving average includes the "future", the model will "cheat" offline and is bound to fail once deployed.
- **Monitor concept drift and retrain periodically.** The patterns in a time series change over time (holidays, policy, market shifts). After going live, keep monitoring the error, and **retrain** on new data as soon as performance starts to slip.
- **Always compare against a naive baseline.** Time series have a very strong opponent: the **naive forecast** ("tomorrow = today", or "tomorrow = the same day last week"). If your complex model cannot beat it, it has not learned anything real. Every result should first be compared with this baseline.

## Common mistakes / summary

- **Thinking only about choosing models and tuning parameters while ignoring the whole pipeline** — the traps in the pipeline are often more fatal than the choice of model.
- **Data leakage**: standardizing / selecting features before splitting, or letting future information into training — prevent it with a `Pipeline` + fitting only on the training set.
- **Reusing the test set**: the test set can be used only once; use it more and you overfit to it, the estimate turns optimistic, and the honest assessment of [generalization](../overfitting/) is compromised.
- **Splitting / shuffling time series at random**: you must split by time, validate walk-forward, and build rolling features from the past only.
- **No baseline**: always compare with the naive forecast first to confirm the model really adds value.
- **Treating deployment as the finish line**: monitor **concept drift** and retrain periodically.
- In one sentence: training pipeline = **define the metric → prepare the data → split into three → choose a model and define the [loss](../loss-function/) → train → tune with [cross-validation](../cross-validation/) → examine once on the test set → deploy and monitor**, guarding against leakage and [overfitting](../overfitting/) throughout.

[← Machine learning foundations](../ml/) · [Foundations overview](../)
