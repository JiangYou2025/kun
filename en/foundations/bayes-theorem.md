---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/bayes-theorem/
title: "Bayes' Theorem"
no_comments: true
math: true
---

> Part of [Math foundations](../math/) · [Foundations overview](../)

Bayes' theorem tells us how to **rationally update our prior judgment** when we see new evidence. It combines "what I believed beforehand" and "what the data says" in a single formula.

## Intuition

Imagine you wake up in the morning and, **beforehand**, you think there is a 30% chance of rain today (this is your "prior"). Then you open the curtains and see the sky covered in dark clouds (this is the "evidence"). The dark clouds make you **raise** your estimate of rain — but how far depends on two things:

- how often rainy days come with dark clouds (how well the evidence "fits" rain);
- whether dark clouds are also common on days without rain (how "ordinary" the evidence is).

Bayes' theorem turns this plain reasoning into a precise formula. Its core idea is: **new judgment = old judgment × the correction brought by the evidence**.

## Mathematical formulation

$$
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}
$$

What each symbol means:

- $P(A)$ — the **prior probability**: your belief in event $A$ (e.g. "rain") before seeing the evidence.
- $P(B\mid A)$ — the **likelihood**: the probability of observing evidence $B$ (e.g. "dark clouds") assuming $A$ is true.
- $P(A\mid B)$ — the **posterior probability**: your updated belief after seeing evidence $B$.
- $P(B)$ — the **marginal probability of the evidence**: the total probability of the evidence itself. It acts as a normalizer, guaranteeing that the posterior is a valid probability.

The denominator can be expanded with the **law of total probability**:

$$
P(B)=P(B\mid A)\,P(A)+P(B\mid \lnot A)\,P(\lnot A)
$$

This step is often forgotten, yet it is the key to the calculation — it adds up the probability of the evidence in the two cases "$A$ happens" and "$A$ does not happen".

## A concrete example

The classic "medical test" problem. A disease has a prevalence of $P(\text{sick})=1\%$ in the population. There is a test such that:

- a sick person tests positive with probability (sensitivity) $P(\text{pos}\mid\text{sick})=99\%$;
- a healthy person may also get a false positive, $P(\text{pos}\mid\text{healthy})=5\%$.

**You test positive. What is the probability that you are actually sick?** Many people intuitively say 99%, but let's compute it:

$$
P(\text{pos})=0.99\times0.01+0.05\times0.99=0.0099+0.0495=0.0594
$$

$$
P(\text{sick}\mid\text{pos})=\frac{0.99\times0.01}{0.0594}\approx 0.167
$$

Only about **16.7%**! The reason is that the healthy population is so large that, even with a false-positive rate of just 5%, the absolute number of false positives far exceeds the number of truly sick people. This is the famous **base rate fallacy**.

```python
prior   = 0.01            # P(sick)
sens    = 0.99            # P(pos|sick)
fpr     = 0.05            # P(pos|healthy)
evidence = sens*prior + fpr*(1-prior)
posterior = sens*prior / evidence
print(round(posterior, 3))   # 0.167
```

## Why it matters / where it is used

Bayes' theorem is a unified framework for **learning from data**:

- **Naive Bayes classifiers**: spam filtering and the like, which use it directly to compute "the probability that an email is spam given its words".
- **Bayesian inference**: treats model parameters as [random variables](../random-variable/) and uses data to update the prior into a posterior, which naturally yields **uncertainty estimates**.
- It pairs with [maximum likelihood](../maximum-likelihood/): maximum likelihood looks only at $P(B\mid A)$, while the Bayesian approach additionally multiplies by the prior $P(A)$.

## Relevance to time series forecasting

Forecasting is, in essence, "updating our beliefs about the future based on the history observed so far" — which is exactly the Bayesian form:

$$
P(\text{future}\mid\text{history})\propto P(\text{history}\mid\text{model})\,P(\text{model})
$$

- **Bayesian filtering / the Kalman filter**: each new observation updates the posterior of the state once; this is the core mechanism of online forecasting with state-space models.
- In deep models such as KUN (Kernel U-Net), the Bayesian formula is not written explicitly, but "using the evidence of the history window to correct our judgment about the next segment" is the same idea; and if you attach **confidence intervals** to a forecast, the language behind them is that of the posterior distribution.

## Summary

- Posterior $\propto$ likelihood $\times$ prior; the denominator is just normalization.
- Don't forget to expand $P(B)$ with the law of total probability.
- The prior matters: when something is **rare to begin with**, even highly sensitive evidence may not make it likely (the base rate fallacy).

[← Math foundations](../math/) · [Foundations overview](../)
