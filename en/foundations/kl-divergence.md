---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/kl-divergence/
title: "KL Divergence"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

The KL divergence (Kullback–Leibler divergence) measures the extra cost (the information lost) incurred by "**approximating the true distribution $p$ with a distribution $q$**". It is always non-negative and **asymmetric** — swapping the two distributions changes the result.

## Intuition

Suppose the truth follows the distribution $p$, but all you have is an approximate model $q$. If you design codes for events and make decisions according to $q$ while the world actually runs according to $p$, you will **waste** some bits — and the amount wasted is the KL divergence.

- The closer $q$ is to $p$, the less is wasted and the closer the KL gets to 0;
- when $q=p$, nothing is wasted at all, and KL = 0;
- the further $q$ strays from $p$, the larger the KL.

You can read it as "**the information distance from $p$ to $q$**", but be careful: it is not a true distance (it is asymmetric and does not satisfy the triangle inequality).

## Mathematical formulation

Discrete form:

$$
D_{\mathrm{KL}}(p\parallel q)=\sum_i p_i\log\frac{p_i}{q_i}
$$

- $p_i$ — the probability under the true distribution (the weight that decides which events "matter");
- $q_i$ — the probability under the approximating distribution;
- $\log\dfrac{p_i}{q_i}$ — how far $q$ deviates from $p$ on event $i$.

Its relationship with [entropy](../entropy/) and [cross-entropy](../cross-entropy/) is very important:

$$
D_{\mathrm{KL}}(p\parallel q)=\underbrace{-\sum_i p_i\log q_i}_{\text{cross-entropy }H(p,q)}-\underbrace{\Big(-\sum_i p_i\log p_i\Big)}_{\text{entropy }H(p)}=H(p,q)-H(p)
$$

That is, **KL divergence = cross-entropy − entropy**. Since $H(p)$ is a constant, minimizing the cross-entropy during training is the same as minimizing the KL divergence.

Two key properties:

- **Non-negativity**: $D_{\mathrm{KL}}(p\parallel q)\ge 0$, with equality if and only if $p=q$ (Gibbs' inequality).
- **Asymmetry**: $D_{\mathrm{KL}}(p\parallel q)\ne D_{\mathrm{KL}}(q\parallel p)$.

{% include fviz/kl-asym.html %}

## A concrete example

True $p=[0.5,0.5]$, approximation $q=[0.9,0.1]$ (base 2):

$$
D_{\mathrm{KL}}(p\parallel q)=0.5\log_2\frac{0.5}{0.9}+0.5\log_2\frac{0.5}{0.1}\approx 0.5(-0.848)+0.5(2.322)\approx 0.737
$$

The other way round, $D_{\mathrm{KL}}(q\parallel p)\approx 0.531$ — **the two are not equal**, a direct illustration of the asymmetry.

```python
import numpy as np
def kl(p, q):
    p, q = np.array(p), np.array(q)
    return np.sum(p * np.log2(p / q))
print(round(kl([0.5, 0.5], [0.9, 0.1]), 3))  # 0.737
print(round(kl([0.9, 0.1], [0.5, 0.5]), 3))  # 0.531  ≠ the value above
```

## Why it matters / where it is used

- **Variational autoencoders (VAEs)**: the [loss](../loss-function/) includes a KL term that keeps the latent distribution close to a standard normal.
- **Variational inference**: a tractable $q$ is used to approximate a complex posterior, and the objective is to minimize the KL.
- **Model distillation and [reinforcement learning](../reinforcement-learning/) (e.g. PPO)**: a KL constraint keeps the new policy / distribution from changing too abruptly relative to the old one.
- It is the quantity "really" being optimized behind the [cross-entropy](../cross-entropy/) loss.

## What it means for time series forecasting

- In probabilistic forecasting, the KL divergence measures how far the "**predicted future distribution**" is from the "**actual distribution**".
- Detecting **distribution drift** (concept drift): when the KL between the training-time and post-deployment data distributions grows, it signals that the model should be retrained.
- If KUN (Kernel U-Net) outputs forecasts in probabilistic or quantile form, its training objective can be written as minimizing the KL between the predicted distribution and the true distribution.

## Common pitfalls

- **It is not a distance**: it is asymmetric and violates the triangle inequality, so do not use it like a Euclidean distance; if you need a symmetric version, use the JS divergence.
- When some $q_i=0$ while $p_i>0$, the KL becomes infinite — in practice, smooth or clip $q$.
- The direction matters: $D_{\mathrm{KL}}(p\parallel q)$ (forward, "covers" the truth) and $D_{\mathrm{KL}}(q\parallel p)$ (reverse, "focuses" on a mode) behave differently, and picking the wrong one affects the quality of the approximation.

[← Math foundations](../math/) · [Foundations overview](../)
