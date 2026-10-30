---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/training-practice/
title: "Training in Practice"
no_comments: true
math: true
---

> Part of [Deep learning foundations](../dl/) · [Foundations overview](../)

**Training in practice** refers to the whole set of engineering techniques that make a [neural network](../neural-network/) "trainable, stable, and good" — from parameter initialization, normalization and [regularization](../regularization/) to learning-rate schedules, early stopping and training monitoring. Each one is simple on its own, but together they decide whether a model is actually usable.

**Related:** [Dropout](../dropout/) · [BatchNorm](../batchnorm/) · [Early stopping](../early-stopping/)

## Intuition

Training a network is a lot like tending a simmering pot of soup: too much heat (a learning rate that is too high) and it burns; too little (a learning rate that is too low) and it takes forever to cook; unwashed ingredients (unnormalized data) make it taste bitter; too much seasoning at once (an overly complex model) makes it cloying ([overfitting](../overfitting/)). Training practice is this collection of "heat + ingredients + tasting" know-how — the goal is a [loss](../backpropagation/) that falls steadily and a model that also performs well on **data it has never seen**.

Below we go through this toolbox following the life cycle of training.

## Getting started: initialization and data/feature normalization

- **Weight initialization**: weights cannot all be set to 0 (then every [neuron](../neuron/) is symmetric and nothing can be learned), nor can they be too large or too small (that immediately causes [exploding or vanishing gradients](../vanishing-exploding-gradient/)). Xavier / He initialization is commonly used; it sets the weight variance automatically from the layer's input and output sizes.
- **Input normalization**: scale every feature to a similar magnitude (for example, subtract the mean and divide by the standard deviation); otherwise features with large magnitudes dominate the [gradient](../gradient/) and distort training.
- **Normalization between layers**: [BatchNorm](../batchnorm/) brings each layer's inputs back to zero mean and unit variance over each [batch](../batch/) and then scales and shifts them, stabilizing the distribution and allowing larger learning rates; with small batches or sequence tasks, LayerNorm is commonly used instead.

## Fighting overfitting: the regularization kit

Overfitting = great on the training set, poor on the validation set. Common remedies:

- **[Dropout](../dropout/)**: randomly deactivates some neurons during training, forcing the network not to rely on individual units — effectively an implicit ensemble of many sub-networks.
- **Weight decay (L2 regularization)**: add a term $\frac{\lambda}{2}\lVert w\rVert^2$ to the loss to penalize overly large weights and make the model smoother:

$$
L_{\text{total}} = L_{\text{data}} + \frac{\lambda}{2}\sum_w w^2
$$

where $\lambda$ controls the regularization strength; the larger it is, the more the model leans toward simplicity.

- **[Early stopping](../early-stopping/)**: watch the validation loss, stop once it no longer decreases, and roll back to the best version — regularization at almost zero cost.
- **Data augmentation / more data**: fundamentally the most effective — the more data and the more varied it is, the harder it is to overfit.

## Controlling the heat: learning rate and optimizer

The [learning rate](../learning-rate/) is the most important hyperparameter. It is used together with an [optimizer](../optimizer/) (such as [Adam](../adam/) or SGD+Momentum). Common techniques:

- **Learning-rate schedule (lr schedule)**: lower the learning rate later in training to help converge to a better solution. Common choices are step decay and cosine annealing:

$$
\eta_t = \eta_{\min} + \tfrac{1}{2}(\eta_{\max}-\eta_{\min})\Big(1 + \cos\tfrac{t}{T}\pi\Big)
$$

- **Warmup**: for the first few hundred steps, start from a very small learning rate and ramp it up slowly, so the parameters are not thrown into disarray at the start (almost essential when training Transformers).
- **Gradient clipping**: cap the gradient norm at a threshold — the specific cure for [exploding gradients](../vanishing-exploding-gradient/), and standard when training [RNNs](../rnn/) / [LSTMs](../lstm/).

## Tasting: monitoring training/validation loss

During training, always **plot the training loss and the validation loss curves together**; they reveal problems at a glance:

- **Underfitting**: even the training loss won't go down → the model is too weak / the learning rate is too small / not trained long enough. Remedies: a bigger model, longer training, a tuned learning rate.
- **Overfitting**: the training loss is low but the validation loss starts to **rise** → the model is memorizing the training set. Remedies: the regularization kit above, a smaller model, more data.
- **Ideal state**: both curves go down, and the validation loss stays close to the training loss, with only a small gap.

Rule of thumb: **first make the model big enough to overfit a small subset of the data** (verifying that the pipeline has no bugs), then gradually add regularization to push the validation loss down. This "overfit first, then regularize" rhythm is more efficient than piling on regularization from the start.

## A concrete training loop

Putting the points above together into a minimal working PyTorch training skeleton:

```python
import torch, torch.nn as nn

opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)  # includes weight decay
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)    # lr schedule

best, wait, patience = float("inf"), 0, 10
for epoch in range(epochs):
    model.train()                                   # Dropout / BN switch to training mode
    for x, y in train_loader:
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # gradient clipping
        opt.step()
    sched.step()

    model.eval()                                    # inference mode: BN uses running stats, Dropout off
    with torch.no_grad():
        val = sum(loss_fn(model(x), y) for x, y in val_loader)
    if val < best:                                  # early stopping + save the best
        best, wait = val, 0; torch.save(model.state_dict(), "best.pt")
    else:
        wait += 1
        if wait >= patience: break
```

## Summary

- **Getting started**: sensible initialization + input normalization + normalization between layers ([BatchNorm](../batchnorm/)).
- **Fighting overfitting**: [Dropout](../dropout/), weight decay, [early stopping](../early-stopping/), more data.
- **Controlling the heat**: [learning-rate](../learning-rate/) schedule + warmup + [optimizer](../optimizer/) + gradient clipping.
- **Reading the curves**: use training/validation loss to diagnose underfitting vs overfitting; overfit first, then regularize.
- These general practices apply equally to training [RNNs](../rnn/), [LSTMs](../lstm/), [Transformers](../transformer/) and this site's multi-scale model, **Kernel U-Net (KUN)**.

[← Deep learning foundations](../dl/) · [Foundations overview](../)
