---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/maximum-likelihood/
title: "Maximum Likelihood"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Maximum likelihood estimation (MLE) is a method for **finding parameters**: among all possible parameter values, it picks the one that makes "**the data we actually observed**" most probable. The training objective of many models is, at heart, maximum likelihood.

## Intuition

You find a coin, flip it 10 times and get 7 heads and 3 tails. Question: roughly what is the probability $p$ of heads for this coin?

Intuition says 0.7. Maximum likelihood turns this intuition into a principle: **choose the $p$ under which "7 heads, 3 tails" is most likely to happen**.

- If $p=0.1$, getting 7 heads is almost impossible;
- If $p=0.7$, getting 7 heads is quite natural;
- So 0.7 is the parameter that "best explains the data".

Maximum likelihood means "**make the model as unsurprised as possible by the data that actually occurred**".

## The math

Let the data $x_1,\dots,x_n$ be independent and identically distributed, and let $\theta$ be the model parameters. The **likelihood function** is the joint probability of the data under those parameters:

$$
L(\theta)=\prod_{i=1}^{n} p(x_i\mid\theta)
$$

Products are awkward to work with, so we take the logarithm to turn them into sums (the log is monotonic and does not move the location of the maximum), which gives the **log-likelihood**:

$$
\ell(\theta)=\sum_{i=1}^{n}\log p(x_i\mid\theta)
$$

The maximum likelihood estimate is:

$$
\hat\theta_{\text{MLE}}=\arg\max_\theta\ \ell(\theta)
$$

In practice one equivalently **minimizes the negative log-likelihood** (NLL), which connects directly to [loss functions](../loss-function/) / [gradient descent](../gradient-descent/):

$$
\hat\theta=\arg\min_\theta\ \Big(-\sum_i\log p(x_i\mid\theta)\Big)
$$

## A concrete example

Back to 7 heads and 3 tails. The likelihood is $L(p)=p^7(1-p)^3$; taking logs:

$$
\ell(p)=7\log p+3\log(1-p)
$$

Set the derivative to zero:

$$
\ell'(p)=\frac{7}{p}-\frac{3}{1-p}=0\ \Rightarrow\ 7(1-p)=3p\ \Rightarrow\ p=0.7
$$

Sure enough it is 0.7, in agreement with intuition.

```python
import numpy as np
ps = np.linspace(0.01, 0.99, 99)
ll = 7*np.log(ps) + 3*np.log(1-ps)
print(round(ps[np.argmax(ll)], 2))   # 0.7
```

## Why it matters / where it is used

- **A unified training principle**: MLE for linear regression (assuming Gaussian noise) gives exactly **least squares**; MLE for classification gives exactly the [cross-entropy](../cross-entropy/) loss.
- It complements the [Bayesian](../bayes-theorem/) approach: MLE looks only at the likelihood $p(\text{data}\mid\theta)$, while the Bayesian approach also multiplies by a prior $p(\theta)$ (adding a regularization term amounts to adding a prior, i.e. MAP estimation).
- With large samples, MLE has good statistical properties (consistency, asymptotic efficiency).

## Relevance to time series forecasting

- The parameters of classical models (AR, ARIMA, GARCH) are mostly fitted by maximum likelihood.
- In probabilistic forecasting, the training objective is often written as "maximize the log-likelihood of future observations" — for example, making the Gaussian distribution output by the model fit the true values as closely as possible.
- KUN (Kernel U-Net) uses MSE for point forecasts, which is precisely "maximum likelihood under Gaussian noise"; switching to probabilistic forecasting, the loss is written directly as the negative log-likelihood.

## Common pitfalls

- The likelihood is **not** the probability of the parameters: $L(\theta)$ is "the probability of the data as a function of $\theta$", and it does not integrate to 1 over $\theta$.
- With small samples, MLE can [**overfit**](../overfitting/) (e.g. it underestimates the variance); adding a prior / regularization (MAP) is then more robust.
- Remember to use the **log**-likelihood: products easily underflow, while sums are more stable and easier to differentiate.

[← Math foundations](../math/) · [Foundations overview](../)
