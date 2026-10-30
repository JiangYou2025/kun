---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/batchnorm/
title: "BatchNorm (Batch Normalization)"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Batch normalization (BatchNorm, BN)** is an operation placed between network layers: on each [mini-batch](../batch/) it "pulls" a layer's inputs back to mean 0 and variance 1, then rescales and shifts them with two learnable parameters, making training more stable and convergence faster.

## Intuition

During training, the distribution of each layer's inputs keeps drifting as the parameters of the preceding layers are updated — this is called **internal covariate shift**. Downstream layers are like chasing a target that never stops moving: learning is hard, and a slightly larger learning rate makes things unstable.

BatchNorm's approach is to set up a "standardization checkpoint" at the entrance of each layer: **whatever the scale of the incoming data, first bring it into a stable range** (zero mean, unit variance), then pass it on to the layer. Each layer thus sees a relatively stable input distribution, and so:

- you can use a **larger [learning rate](../learning-rate/)** and train faster;
- the model is less sensitive to parameter [initialization](../training-practice/);
- it also has a mild [regularization](../regularization/) effect (because each sample's normalization depends on the whole batch, a little noise is introduced).

## Mathematical formulation

For a mini-batch of $m$ samples, take one feature dimension and let its values be $x_1, \dots, x_m$.

Step one, compute the batch mean and variance:

$$
\mu_B = \frac{1}{m}\sum_{i=1}^{m} x_i,
\qquad
\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m} (x_i - \mu_B)^2
$$

Step two, **normalize**:

$$
\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

Step three, **scale and shift**:

$$
y_i = \gamma\,\hat{x}_i + \beta
$$

Symbol by symbol:

- $\mu_B,\ \sigma_B^2$: the mean and variance of the current batch along this feature dimension.
- $\epsilon$: a tiny constant (e.g., $10^{-5}$) that prevents a zero denominator and ensures numerical stability.
- $\hat{x}_i$: the normalized value, distributed with roughly mean 0 and variance 1.
- $\gamma$ (scale), $\beta$ (shift): **learnable parameters**, one pair per feature dimension, updated by [backpropagation](../backpropagation/).
- $y_i$: the final output of BN.

Why still need $\gamma, \beta$ after normalizing? Because forcing every layer into a "standard normal" could cost expressive power. Giving the network the two knobs $\gamma, \beta$ lets it **learn the distribution back** when needed (it even recovers the original input when $\gamma=\sqrt{\sigma_B^2+\epsilon},\ \beta=\mu_B$), so BN does not weaken the model.

## Training vs. inference (crucial)

This is where BN most often goes wrong.

- **During training**: the $\mu_B, \sigma_B^2$ of **the current batch** are used. At the same time, a global set of **running statistics** (running mean / running variance) is quietly maintained:

$$
\mu_{run} \leftarrow (1-\alpha)\,\mu_{run} + \alpha\,\mu_B
$$

(Likewise for the variance; $\alpha$ is the momentum, 0.1 by default in PyTorch.)

- **During inference**: a single sample has no "batch" to speak of, and predictions should not depend on whichever other samples happen to be fed in alongside it. So at inference time **the current batch statistics are no longer used**; instead, the $\mu_{run}, \sigma_{run}^2$ accumulated during training provide a fixed normalization:

$$
y = \gamma\,\frac{x - \mu_{run}}{\sqrt{\sigma_{run}^2 + \epsilon}} + \beta
$$

Practical point: in PyTorch, always call `model.eval()` to switch to inference mode so that BN uses the running statistics; forgetting to switch makes predictions fluctuate with the batch composition and degrades results. In addition, when the **batch is very small** (e.g., 1–2), BN's statistics are noisy and it performs poorly; LayerNorm is often used instead.

## A concrete example

Suppose a feature takes 4 values in one batch, $x = [1, 2, 3, 4]$, and $\epsilon$ is negligible:

$$
\mu_B = \frac{1+2+3+4}{4} = 2.5,\qquad
\sigma_B^2 = \frac{(1.5)^2+(0.5)^2+(0.5)^2+(1.5)^2}{4} = 1.25
$$

$$
\hat{x} = \frac{[1,2,3,4] - 2.5}{\sqrt{1.25}} \approx [-1.342,\ -0.447,\ 0.447,\ 1.342]
$$

After normalization the mean is about 0 and the variance about 1. If the network has learned $\gamma=2,\ \beta=5$, the output is $y = 2\hat{x}+5 \approx [2.32,\ 4.11,\ 5.89,\ 7.68]$. The corresponding code:

```python
import torch, torch.nn as nn

net = nn.Sequential(
    nn.Linear(32, 64),
    nn.BatchNorm1d(64),   # normalize each of the 64 features separately
    nn.ReLU(),
    nn.Linear(64, 1),
)
net.train(); y = net(torch.randn(16, 32))   # training: uses batch statistics
net.eval();  y = net(torch.randn(16, 32))   # inference: uses running statistics
```

## Summary

- BN **normalizes** on each batch (subtract the mean, divide by the standard deviation), then **scales and shifts** with the learnable $\gamma,\beta$.
- $\epsilon$ prevents division by zero; $\gamma,\beta$ preserve expressive power.
- **Batch statistics for training, running statistics for inference** — remember to switch to `eval()`.
- It stabilizes distributions, allows a larger [learning rate](../learning-rate/), speeds up convergence, and adds mild regularization; use it with care when batches are small.
- Together with [Dropout](../dropout/) and [early stopping](../early-stopping/), it is one of the common [training practice](../training-practice/) tools.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
