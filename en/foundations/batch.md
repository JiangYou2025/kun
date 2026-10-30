---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/batch/
title: "Batch"
no_comments: true
math: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

A **batch** is the small group of samples fed to the model at once when training a [neural network](../neural-network/). The model computes the [gradient](../gradient/) on this batch, updates its parameters once, then moves on to the next batch, over and over.

## Intuition

Suppose you want to refine your problem-solving approach based on 10,000 practice problems. There are three possible rhythms:

- **Adjust after every problem**: reflect and adjust right after each problem. Quick to react, but a single problem is very random, so your approach easily swings back and forth. This corresponds to **batch size = 1** (stochastic [gradient descent](../gradient-descent/), SGD).
- **Adjust only after finishing everything**: do all 10,000 problems, tally the overall mistakes, and adjust once. The direction is the most accurate, but it is too slow and too memory-hungry, and you only adjust once per round. This corresponds to **full batch**.
- **Adjust every 32 problems**: reflect and adjust after every 32 problems. You get some statistical stability while still updating frequently. This is the **mini-batch**, the compromise used almost always in practice.

**At its core, a batch is a trade-off between "efficiency" and "stability".**

## Key points

- **batch size**: how many samples are in one batch. Common values are 16, 32, 64, 128, 256, often powers of 2 to match [GPU](../gpu/) memory alignment.
- **iteration**: processing one batch and updating the parameters once is called one iteration.
- **epoch**: one complete pass over the whole training set is called an epoch.
  - Relationship: `iterations per epoch = total samples / batch size` (rounded up).

Effects of the batch size:

- **Larger**: smoother, more stable gradient estimates and better use of GPU parallelism, but more memory, and sometimes slightly worse [generalization](../generalization/).
- **Smaller**: more frequent updates and less memory, but noisy gradients and jittery training.

## An example

PyTorch uses a `DataLoader` to split data into batches automatically:

```python
import torch
from torch.utils.data import TensorDataset, DataLoader

# Suppose there are 1000 samples, each with 7 features
X = torch.randn(1000, 7)
y = torch.randn(1000, 1)

loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

for epoch in range(3):
    for xb, yb in loader:        # take one batch at a time
        # xb.shape == (32, 7); the last batch may have fewer than 32
        pred = model(xb)         # one forward pass: the whole batch at once
        loss = loss_fn(pred, yb)
        loss.backward()          # compute the gradient on this batch
        optimizer.step()         # update the parameters once
        optimizer.zero_grad()
```

1000 / 32 ≈ 32 iterations make one epoch. Note that the first dimension of `xb` is the batch dimension — the whole batch of samples is **stacked into one tensor** and computed in one go, which is exactly where the [GPU](../gpu/) and [vectorization](../vectorization/) show their power.

## Relevance to time series forecasting

When training forecasting models such as **KUN / Kernel U-Net**:

- Each sample is usually a **sliding window**: use the past `L` steps to predict the next `H` steps. A batch is then a tensor of shape `(batch_size, L, num_features)`.
- The batch dimension lets us **compute many windows in parallel**, keeping the GPU busy and greatly shortening training time.
- Be careful with temporal data: `shuffle=True` shuffles the order **between samples (windows)**, not the time order **inside** a single window — the internal order must never be touched, otherwise the temporal structure is destroyed.

## Common misconceptions

- **Confusing batch size with model capacity**: the batch size only affects training dynamics; it does not change how complex a model can learn.
- **Thinking the bigger the batch, the better**: a large batch saves time, but memory may run out, and sometimes the [learning rate](../learning-rate/) has to be increased accordingly.
- **Careless shuffling of time series data**: you may shuffle the order of windows, but never the time steps inside a window, and you must also prevent training windows from "peeking" at future data in the validation set.
- **Forgetting that the last batch is not full**: with 1000 samples and batch=32, the last batch has only 8 samples, and the code must handle it correctly.

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
