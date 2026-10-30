---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/dropout/
title: "Dropout"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Dropout** is a [regularization](../regularization/) technique: during training it randomly sets the outputs of a fraction of [neurons](../neuron/) to zero, forcing the network not to rely too heavily on any few units, which reduces [overfitting](../overfitting/) and improves [generalization](../generalization/).

## Intuition

Picture a project team that always relies on one or two star members to do everything: the moment they take leave, the whole team grinds to a halt. Try a different management style: at every meeting, randomly tell some people "you're not speaking today". Over time, everyone has to learn to work independently and cover for each other, and the team as a whole becomes more resilient.

Dropout does this to neurons. During training, **every [batch](../batch/) randomly makes a set of neurons "absent"** (their output becomes 0), and the remaining neurons must be able to get the job done in all sorts of "incomplete formations". The features the network learns thus become **redundant and robust**, rather than betting everything on one fragile pathway.

There is also an elegant interpretation: each random dropout amounts to training a **different subnetwork**, and the final model approximates an "ensemble" of exponentially many subnetworks — and ensembles are generally less prone to overfitting than a single model.

## How it works: the training-time mask

Let the output vector of some layer be $x = (x_1, x_2, \dots, x_n)$, and fix a **keep probability** $p$ (e.g. $p=0.8$ means each unit has an 80% chance of being kept). During training, draw an independent 0/1 mask for each unit:

$$
m_i \sim \text{Bernoulli}(p), \qquad \tilde{x}_i = m_i \cdot x_i
$$

- $m_i$: the mask for unit $i$, equal to 1 (kept) with probability $p$ and 0 (dropped) with probability $1-p$.
- $1-p$ is called the **drop rate**, commonly 0.2 – 0.5.
- $\tilde{x}_i$: the output after dropout; dropped units simply become 0 and take no part in this forward and backward pass.

Note: units set to zero receive **no [gradient](../gradient/)** in this step, so this really is "randomly training a subnetwork".

## Scaling at inference time (a key detail)

At test/inference time we **no longer drop units at random** — we want a deterministic prediction from the whole network. But this creates a problem: during training each unit is active only with probability $p$ on average, so the next layer's expected input is $p\cdot x$; at inference all units are active and the input suddenly becomes $x$, magnified by a factor of $1/p$, so the distributions no longer match.

The fix is to **rescale so that the expectations match**. There are two equivalent ways:

1. **Scale at inference**: at prediction time, multiply the weights (or activations) by $p$ so that the output returns to its expected training-time magnitude.
2. **Inverted Dropout (more common)**: during training, divide the kept units by $p$; at inference, **do nothing at all**:

$$
\text{Training: }\ \tilde{x}_i = \frac{m_i \cdot x_i}{p}, \qquad \text{Inference: }\ \tilde{x}_i = x_i
$$

Either way, the goal is to ensure that **the expected output is the same at training and inference time**. Modern frameworks (such as PyTorch's `nn.Dropout`) use Inverted Dropout by default, and it is only active in `model.train()` mode and switched off automatically in `model.eval()` mode — be sure to remember this.

## A concrete example

Let the drop rate be $1-p = 0.5$ (i.e. $p=0.5$) and a layer's output be $x = [2, 4, 6, 8]$. In one training step the sampled mask is $m = [1, 0, 1, 0]$; with Inverted Dropout:

$$
\tilde{x} = \frac{[1,0,1,0]\odot[2,4,6,8]}{0.5} = \frac{[2,0,6,0]}{0.5} = [4, 0, 12, 0]
$$

The two kept units are doubled to compensate for the half that was dropped. Checking the expectation: $\mathbb{E}[\tilde{x}_1] = 0.5\times 4 + 0.5\times 0 = 2 = x_1$, matching the original value. At inference we simply use $[2,4,6,8]$. The corresponding code:

```python
import torch, torch.nn as nn

net = nn.Sequential(
    nn.Linear(64, 128), nn.ReLU(),
    nn.Dropout(p=0.3),          # here p is the "drop rate"
    nn.Linear(128, 1),
)
net.train()   # training: Dropout is active
y = net(torch.randn(16, 64))
net.eval()    # inference: Dropout is switched off automatically, no randomness
```

Note that in PyTorch, the `p` in `nn.Dropout(p=...)` is the **drop probability**, the opposite of the keep probability $p$ in the formulas above — don't mix them up.

## Common pitfalls

- **Thinking neurons are still dropped at random during inference**: they are not. Inference is deterministic; Dropout only acts during training.
- **Forgetting to switch to `eval()` mode**: if you evaluate while still in `train()` mode, predictions are random and results are weaker.
- **Thinking a higher drop rate is always better**: too high (e.g. 0.8) throws away too much information and leads to underfitting; 0.2–0.5 is typical.
- **Stacking it mindlessly with [BatchNorm](../batchnorm/)**: using both together sometimes causes interference; a common practice is to prefer BN, or to place Dropout after BN, in the fully connected layers near the output.

## Why it matters for time series forecasting

Time series samples are strongly correlated and models easily overfit the noise of the training period. Dropout (and its variants such as recurrent dropout and temporal dropout) is a common way to constrain model complexity and improve generalization to future data. Together with [early stopping](../early-stopping/), weight decay and the like, it forms the anti-overfitting toolbox of [training practice](../training-practice/), and it is also used in structures such as this site's multi-scale model **Kernel U-Net (KUN)**.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
