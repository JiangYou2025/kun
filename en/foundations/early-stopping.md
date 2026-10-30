---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/early-stopping/
title: "Early Stopping"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Early stopping** is a simple and effective way to prevent [overfitting](../overfitting/): during training you keep watching performance on the validation set, and as soon as it **stops improving**, you stop training early and roll back to the best-performing version of the model.

## Intuition

A student drilling practice problems gets better and better at first; but if they keep grinding through the same problem set, they start **memorizing the answers** — even the details and the typos — and then fail on new problems. The best moment to stop is just when "accuracy on new problems" begins to fall.

Model training is the same. As the number of epochs grows:

- the **training [loss](../loss-function/)** almost always decreases monotonically (the model fits the training data ever more closely);
- the **validation loss** usually falls first and then rises — early on the model learns real patterns, later it starts learning the **noise** of the training set, and generalization deteriorates.

The minimum of the validation loss is the "sweet spot" where the model's [generalization](../generalization/) is best. Early stopping automatically finds this point and stops near it, sparing you from watching it by hand and avoiding wasted compute on training all the way into overfitting.

## How it works: the algorithm

Early stopping relies on three hyperparameters:

- **patience**: how many consecutive epochs without improvement before stopping, e.g. 10.
- **min_delta (minimum improvement)**: an improvement must exceed this threshold to count as "genuinely better", filtering out tiny fluctuations.
- **monitored metric**: usually the validation loss $L_{val}$ (lower is better), but it can also be accuracy or the like.

The algorithm:

```python
best = float("inf"); wait = 0; best_weights = None
for epoch in range(max_epochs):
    train_one_epoch()
    val = evaluate_on_validation()          # validation loss
    if val < best - min_delta:              # a real improvement
        best = val
        best_weights = copy_weights()       # save the current best model
        wait = 0
    else:
        wait += 1
        if wait >= patience:                # no progress for patience epochs in a row
            break
model.load(best_weights)                     # roll back to the best version
```

Two key points:

1. **Save the best weights.** By the time you detect "no progress", the model has already trained for patience extra epochs and may have deteriorated, so you must roll back to the version with the lowest validation loss.
2. **Patience provides a buffer.** The validation loss often jitters, so you cannot stop the moment it rises; patience lets us tolerate short-term fluctuations and act only on sustained deterioration.

## A concrete example

Let patience=3 and min_delta=0. Suppose a training run produces the following validation losses:

| epoch | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|------|---|---|---|---|---|---|---|
| $L_{val}$ | 0.50 | 0.42 | 0.39 | 0.40 | 0.41 | 0.43 | 0.45 |
| wait | 0 | 0 | 0 | 1 | 2 | 3 ✋ | – |

Epoch 3 reaches the minimum of 0.39, which is saved. Then epochs 4, 5 and 6 bring no improvement three times in a row, wait reaches patience=3, so training **stops** at epoch 6 and the model is **rolled back to the weights from epoch 3**. Even if epoch 7 might (or might not) bounce back, we don't gamble — early stopping chooses to stop safely at the known best point.

{% include fviz/early-stop.html %}

## Why it matters / where it is used

- **Almost cost-free [regularization](../regularization/)**: it doesn't change the network architecture or the loss function — it just "knows when to quit" — yet it can significantly improve generalization.
- **Saves time and compute**: avoids pointlessly training to the very end.
- **Implicit complexity control**: the longer you train, the more effective degrees of freedom the model has; early stopping effectively limits this effective complexity, and has something in common with L2 regularization.
- It is **complementary** to [Dropout](../dropout/), [BatchNorm](../batchnorm/), weight decay and the like; they are often used together and together form the anti-overfitting routine of [training practice](../training-practice/).

## Common pitfalls

- **Watching only the training loss**: the training loss keeps falling, so it will never tell you to stop; you must judge with an **independent validation set**.
- **Not saving the best weights**: the model at the moment you stop is often not the best one; forget to roll back and the effort is wasted.
- **Patience too small**: you get fooled by normal jitter and stop too early, in an underfitted state.
- **Early stopping on the test set**: that leaks test-set information into model selection, and the evaluation is no longer fair — early stopping must be based on the validation set.

## Why it matters for time series forecasting

Time series models are especially prone to mistaking incidental noise in the training period for real patterns; early stopping is a routine way to control this overfitting and ensure generalization to future data. When training [RNNs](../rnn/), [LSTMs](../lstm/) and even this site's multi-scale model **Kernel U-Net (KUN)**, early stopping on the validation loss is one of the default engineering practices.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
