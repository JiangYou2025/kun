---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/entropy/
title: "Entropy"
no_comments: true
math: true
---

> Part of [Math Fundamentals](../math/) · [Foundations overview](../)

Entropy measures how much **uncertainty** a [random variable](../random-variable/) carries: the harder the outcome is to guess, the higher the entropy; the more certain the outcome, the lower the entropy. It is the cornerstone of [information theory](../information-theory/), and it also captures "the minimum amount of information needed to describe something".

## Intuition

Think of entropy as "**the average number of yes/no questions you need to ask to guess the answer**".

- A **fair coin**, heads and tails at 50% each: you need at least 1 question ("Is it heads?"), so the entropy is 1 bit.
- A **rigged coin** that lands heads 99% of the time: you barely need to ask, so the entropy is close to 0.
- A **fair 16-sided die**, every face equally likely: hardest to guess, entropy = 4 bits.

The pattern: **the more uniform and the more possibilities → the more uncertain → the higher the entropy**; the more skewed toward one outcome → the more certain → the lower the entropy. Entropy reaches its maximum for the uniform distribution.

## Mathematical formulation

The Shannon entropy of a discrete random variable $X$:

$$
H(X)=-\sum_i p_i \log p_i
$$

- $p_i$ — the probability of event $i$;
- by convention $0\log 0 = 0$;
- with $\log$ in base 2 the unit is the **bit**; in base $e$ the unit is the **nat**.

Why $-\log p$? Because the "amount of information" carried by a single event is defined as $-\log p_i$: **the rarer the event, the more information its occurrence brings** ("the sun rose as usual today" carries almost no information; "it snowed today (in the desert)" carries a huge amount). Entropy is the probability-weighted **average** of this information, i.e. the expectation $\mathbb{E}[-\log p]$.

## A concrete example

Compare the entropy of two coins (base 2):

Fair coin $p=[0.5,0.5]$:

$$
H=-(0.5\log_2 0.5+0.5\log_2 0.5)=-(0.5\cdot(-1)+0.5\cdot(-1))=1\ \text{bit}
$$

Biased coin $p=[0.9,0.1]$:

$$
H=-(0.9\log_2 0.9+0.1\log_2 0.1)\approx 0.469\ \text{bits}
$$

The second is more certain, so its entropy is smaller.

```python
import numpy as np
def entropy(p):
    p = np.array(p)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))
print(round(entropy([0.5, 0.5]), 3))   # 1.0
print(round(entropy([0.9, 0.1]), 3))   # 0.469
```

## Why it matters / where it is used

- **[Decision trees](../decision-tree/)**: use "information gain" (the drop in entropy before vs after a split) to choose the most discriminative feature.
- **[Loss functions](../loss-function/)**: [cross-entropy](../cross-entropy/) and [KL divergence](../kl-divergence/) are both built on entropy.
- **Compression theory**: entropy gives the theoretical lower bound for lossless compression — the average code length can never be shorter than the entropy.

## Why it matters for time series forecasting

- Entropy directly characterizes **forecasting difficulty**: for a high-entropy series (close to a random walk, very noisy), predictability has a theoretical ceiling no matter how strong the model is.
- When assessing "how much information" a feature or a history window carries, entropy provides a quantitative tool.
- If training KUN (Kernel U-Net) involves probabilistic or classification-style outputs, the lower bound of its loss (cross-entropy) is exactly the entropy of the true distribution — you can never push the loss below the uncertainty inherent in the data itself.

## Summary

- Entropy = average uncertainty = average information $\mathbb{E}[-\log p]$.
- The uniform distribution has maximum entropy; a certain event has entropy 0.
- It is the common source of cross-entropy, KL divergence, information gain and the compression limit, and the theoretical yardstick of forecasting difficulty.

[← Math Fundamentals](../math/) · [Foundations overview](../)
