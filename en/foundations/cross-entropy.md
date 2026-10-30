---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/cross-entropy/
title: "Cross-Entropy"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Cross-entropy measures the average cost of "**describing the true distribution with the distribution predicted by a model**". It is the most common [loss function](../loss-function/) for classification tasks — the closer the model gets to the truth, the smaller the cross-entropy.

## Intuition

[Entropy](../entropy/) measures "the average number of bits needed to encode what actually happens optimally". Cross-entropy asks a more realistic question: **if I use a "wrong" code (based on the model's prediction $q$) to describe events that actually occur (the true distribution $p$), how many bits do I spend on average?**

As soon as the prediction $q$ departs from the truth $p$, you end up using longer codes and paying an extra cost. The more accurate the prediction, the closer this cost gets to the lower bound set by the entropy; the further off the prediction, the higher the cost. So "minimizing cross-entropy" is equivalent to "making the predicted distribution as close as possible to the true distribution".

## Mathematical formulation

For discrete distributions, the cross-entropy between the true distribution $p$ and the predicted distribution $q$ is:

$$
H(p,q)=-\sum_i p_i \log q_i
$$

- $p_i$ — the true probability of class $i$ (in classification it is often one-hot: 1 for the correct class, 0 for the others);
- $q_i$ — the probability the model predicts for class $i$;
- with $\log$ in base 2 the unit is the bit; in base $e$ (common in machine learning) the unit is the nat.

Its relationship to [entropy](../entropy/) and the [KL divergence](../kl-divergence/) is:

$$
H(p,q)=H(p)+D_{\mathrm{KL}}(p\parallel q)
$$

Since $H(p)$ (the entropy of the true distribution) is a constant, **minimizing cross-entropy = minimizing the KL divergence = bringing $q$ close to $p$**.

When $p$ is one-hot (say the correct class is $c$), the formula collapses to a compact form:

$$
H(p,q)=-\log q_c
$$

that is, the "**negative log-likelihood**" — it only penalizes you for assigning too low a probability to the correct answer.

{% include fviz/cross-entropy.html %}

## A concrete example

Three classes; the true label is class 1, one-hot $p=[1,0,0]$.

- Model A predicts $q=[0.7,0.2,0.1]$: loss $=-\log 0.7\approx 0.357$.
- Model B predicts $q=[0.3,0.4,0.3]$: loss $=-\log 0.3\approx 1.204$.

Model A gives the correct class a higher probability and has a smaller cross-entropy, which is exactly what we want.

```python
import numpy as np
def cross_entropy(p, q):
    q = np.clip(q, 1e-12, 1.0)        # avoid log(0)
    return -np.sum(p * np.log(q))
p = np.array([1, 0, 0])
print(round(cross_entropy(p, [0.7, 0.2, 0.1]), 3))  # 0.357
print(round(cross_entropy(p, [0.3, 0.4, 0.3]), 3))  # 1.204
```

## Why it matters / where it is used

- **The default loss for classification**: image classification and next-word prediction in language models almost all use cross-entropy (together with a softmax output producing probabilities).
- **A neat gradient**: for the softmax + cross-entropy combination, the gradient is exactly $q-p$ (prediction minus truth), simple and stable, which makes training easy.
- It is equivalent to **maximum likelihood**: minimizing cross-entropy is performing [maximum likelihood estimation](../maximum-likelihood/).

## Relevance to time series forecasting

- When forecasting is framed as a **classification problem** (e.g. predicting "up / flat / down", or discretizing values into bins for probabilistic forecasting), cross-entropy is the natural loss.
- Probabilistic forecasting models output a distribution over future values, and cross-entropy (or its continuous generalization) is used to assess "how well the predicted distribution fits the values that actually occurred".
- Even though regression tasks such as KUN (Kernel U-Net) commonly use MSE, understanding cross-entropy helps you pick the right loss when you need **probabilistic outputs / quantile forecasts**.

## Common pitfalls

- **Cross-entropy is not symmetric**: $H(p,q)\ne H(q,p)$, so the order of the arguments cannot be swapped.
- Remember to clip $q$ numerically (to keep $\log 0$ from becoming infinite).
- Cross-entropy $\ge$ entropy $H(p)$, with equality if and only if $q=p$ — it can never be cheaper than "knowing the truth".

[← Math foundations](../math/) · [Foundations overview](../)
