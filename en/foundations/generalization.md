---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/generalization/
title: "Generalization"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Generalization** is a model's ability to keep performing well on new data it has **never seen**. It is the true goal of machine learning — we do not train a model to memorize the training set, but to make accurate predictions on real data in the future.

## Intuition

Imagine two students preparing for an exam.

- The first **memorizes** past exam questions and their answers by rote. He gets full marks on the mock test (which uses past questions), but as soon as the real exam has new questions, he is lost.
- The second **understands the underlying principles**. He may not get every past question right, but faced with a new question he can still work out the answer.

Only the second student has truly "learned" — that is **generalization**. In machine learning:

- The first student corresponds to **overfitting**: the model memorizes the noise and accidental details of the training data; training error is very low, but it falls apart on new data.
- The second student corresponds to good generalization: the model captures the **repeatable patterns** in the data, so it stays solid on unseen data.

In a sentence: **we want "understanding", not "recitation"**. Generalization ability measures exactly how much the model has understood versus memorized. See [Overfitting](../overfitting/).

## Training error vs generalization error

We care about two kinds of error:

- **Training error**: the model's average error on the training set. This is what we can see directly and optimize.
- **Generalization error**: the model's expected error over the **entire data distribution**, i.e. its average performance on all possible new data. This is what we really want to minimize, but it cannot be observed directly.

The difference between the two is the key quantity:

$$\text{generalization gap} = R(f) - R_{emp}(f)$$

- Small gap: what the model learned on the training set transfers to new data; it generalizes well.
- Large gap: the model has overfit; its good training score is "hollow".

A common but dangerous mistake: focusing only on pushing training error down. Training error can be driven all the way to 0 (as long as the model is complex enough and memorizes hard enough), but generalization error usually first falls and then rises — exactly the signal of overfitting.

{% include fviz/learning-curve.html %}

## Mathematical formulation: empirical risk vs expected risk

To make this intuition rigorous, we introduce two "risks".

Let the [loss function](../loss-function/) be $L(y, f(x))$ (measuring the gap between the prediction $f(x)$ and the true value $y$).

The **empirical risk** is the average loss over the $n$ training samples at hand:

$$R_{emp}(f) = \frac{1}{n}\sum_{i=1}^{n} L\big(y_i, f(x_i)\big)$$

The **expected risk** is the expected loss under the true data distribution:

$$R(f) = \mathbb{E}_{(x,y)}\big[L(y, f(x))\big]$$

What we really want to minimize is $R(f)$, but the distribution is unknown, so it cannot be computed. We settle for minimizing the computable $R_{emp}(f)$ — this is **Empirical Risk Minimization (ERM)**.

Why is approximating $R$ with $R_{emp}$ reasonable? The key is the **iid assumption**: we assume the training samples are drawn **independently and identically distributed** from the same distribution. Under this premise, by the law of large numbers, when the sample size $n$ is large enough, $R_{emp}(f)$ converges to $R(f)$ — the average approaches the expectation.

But be careful:

- With too few samples, $R_{emp}$ and $R$ can be far apart, and the model easily mistakes noise for pattern.
- If the iid assumption is broken (for example, the future data distribution differs from the past), the approximation fails — this is especially common in time series, as discussed below.

## How to estimate generalization

Since $R(f)$ cannot be computed, we **estimate** it by "holding out part of the data and pretending it is the future".

- **Held-out test set**: split the data into a training set and a test set; the model learns only on the training set, and at the end we look at its test-set performance **only once** to estimate the generalization error. The test set must never take part in training or tuning, or the "exam questions leak".
- **Cross-validation**: split the data into $k$ folds, take turns using one fold as the validation set and the rest as the training set, repeat $k$ times and average. This estimates generalization more robustly, which is especially useful when data is limited. See [Cross-validation](../cross-validation/).

The core principle in one sentence: **evaluation must be out-of-sample**. Praising yourself on data you have already seen means nothing.

## What improves generalization

Improving generalization is, at heart, finding a balance between "learning the real pattern" and "not memorizing noise". Common tools:

- **More data**: the more data, the closer $R_{emp}$ is to $R$, and the harder it is for the model to get by on memorization. This is often the most cost-effective option.
- **Regularization**: add constraints or penalties to limit the model's complexity, forcing it to learn simple, general patterns. See [Regularization](../regularization/).
- **Simpler models**: when performance is similar, prefer models with fewer parameters and less complexity (Occam's razor).
- **[Early stopping](../early-stopping/)**: watch the validation error during training and stop as soon as it starts to rise, so the model doesn't drift ever further into rote memorization.

All of these are closely tied to the **bias–variance trade-off**:

$$\text{generalization error} \approx \text{bias}^2 + \text{variance} + \text{irreducible noise}$$

- Model too simple → high **bias** (cannot learn the pattern, underfitting).
- Model too complex → high **variance** (too sensitive to the training data, overfitting).

A model that generalizes well is one that strikes a balance between bias and variance. See [Bias–variance trade-off](../bias-variance/).

## Why it matters for time series forecasting

In time series forecasting, **generalization means predicting a future you have not yet seen**. There are a few points unique to this setting that require extra care.

- **Split in time order**: never shuffle randomly before splitting into training/test! You must train on **past** data and test on **later** data. Otherwise the model "sees the future" (data leakage), the evaluation looks absurdly good, and the deployed model is a disaster.
- **Distribution shift / concept drift**: the trickiest thing about time series is that the future distribution may be **different** from the past. User behaviour changes, policies change, market conditions change, and patterns learned in the past can stop working. This directly violates the iid assumption, so even a model that generalizes well on historical data should not be blindly trusted for the distant future.
- **Out-of-sample evaluation**: evaluation should mimic the real forecasting scenario, typically with **rolling forecasts / time series cross-validation** — fix a point in time, train only on data before it, forecast the period after it, then move the point forward and repeat. Only the error obtained this way truly reflects the model's ability to face the future.

Remember: in time series, "generalization" is not just "doing well on new samples", but "staying robust on **new time periods** and possibly **new distributions**".

## Summary

- **Generalization** is a model's ability to perform well on unseen data, and it is the **true goal** of machine learning.
- Focus on **generalization error**, not just training error; their difference is the **generalization gap**, and a large gap means overfitting.
- In theory we want to minimize the **expected risk $R(f)$**; in practice we approximate it with the **empirical risk $R_{emp}(f)$** (ERM), which is justified by the **iid assumption** and enough data.
- Estimate generalization with a **held-out test set** and **cross-validation**; the principle is **out-of-sample evaluation**.
- To improve generalization: **more data, regularization, simpler models, early stopping**; at heart, balancing **bias and variance**.
- In time series, **split by time**, watch out for **distribution / concept drift**, and use **rolling out-of-sample evaluation**.

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
