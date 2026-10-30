---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/loss-function/
title: "Loss Functions"
no_comments: true
math: true
---

> Part of [Machine learning foundations](../ml/) · [Foundations overview](../)

A **loss function** is a function that **measures the gap between "the model's prediction" and "the true answer"**. In one sentence: the smaller the loss, the more accurate the prediction; and **training a model is, at heart, adjusting its parameters again and again to push this loss as low as possible**.

## Intuition

Imagine you are teaching a student to solve problems. For every problem, you give a "penalty": the more absurd the answer, the bigger the penalty; the closer to the correct answer, the smaller. This **penalty rule** is the loss function.

- It gives the model a **score** that tells it plainly: "this is how wrong you are right now."
- It is also the **compass** of **gradient descent**: the model does not know which way to adjust its parameters, but it only needs to look at "which direction makes the loss fall fastest" and follow it to become more and more accurate.

So the loss function plays two roles: it is both a **referee** (it scores) and a **guide** (it points the way). Without it, the model would be walking blindfolded, with no idea whether it is learning well or where to step next.

## Mathematical formulation

Suppose we have $n$ training samples $(x_i, y_i)$ and a model $f_\theta$ ($\theta$ denotes all adjustable parameters), whose prediction for the $i$-th sample is $\hat y_i = f_\theta(x_i)$. The **total loss** is usually written as the average of the per-sample losses:

$$\mathcal{L}(\theta)=\frac{1}{n}\sum_{i=1}^{n} \ell\big(y_i,\; f_\theta(x_i)\big)$$

Symbol by symbol:

- $\theta$: the model's **parameters** (for example the weights and bias of a [linear model](../linear-model/)). Training means finding a good $\theta$.
- $\ell(y_i, \hat y_i)$: the loss of a **single sample**, measuring how wrong this one prediction is.
- $\frac{1}{n}\sum$: **averages** the losses over all samples to get the overall "degree of error".
- $\mathcal{L}(\theta)$: view it as a **function of the parameters $\theta$** — this is exactly what gradient descent minimizes.

The specific form of $\ell$ depends on the task. Below we look at the two big families: regression and classification.

## Regression losses: predicting a number

When $y$ is a continuous value (house prices, temperatures, sales), the following are common.

**Mean squared error, MSE / squared loss**:

$$\ell = (y-\hat y)^2$$

It **squares** the error, so **large errors are magnified a lot** (an error of 2 costs 4 points, an error of 10 costs 100). Its advantages are that it is smooth everywhere, has nice mathematical properties and is easy to differentiate; its drawback is that it is **very sensitive to outliers** — a single wild point can drive the overall loss up and "pull" the model off course.

**Mean absolute error, MAE / absolute loss**:

$$\ell = |y-\hat y|$$

The error is not squared, only its absolute value is taken, so it is **more robust to outliers**: a single outlier is not overly amplified. The price is that it is not differentiable at $\hat y = y$ (there is a sharp corner), which requires special handling during optimization.

**Huber loss**: behaves like MSE (smooth) when the error is small and like MAE (robust) when the error is large, combining the strengths of both:

$$\ell_\delta(y,\hat y)=\begin{cases}\frac12 (y-\hat y)^2 & |y-\hat y|\le \delta\\[4pt]\delta\,\big(|y-\hat y|-\tfrac12\delta\big) & |y-\hat y|> \delta\end{cases}$$

$\delta$ is the switching point: errors within $\delta$ are squared (sensitive, smooth), and beyond $\delta$ the loss becomes linear (so outliers do not throw it off).

{% include fviz/loss-outlier.html %}

## Classification losses: predicting a class

When the task is classification (cat or dog, spam or not), the model usually outputs a **probability** $\hat p$. The most common choice here is **[cross-entropy](../cross-entropy/)**.

Multi-class ($K$ classes, $y_k$ is the one-hot true label, $\hat p_k$ is the predicted probability):

$$\ell = -\sum_{k=1}^{K} y_k \log \hat p_k$$

Binary ($y\in\{0,1\}$, $p$ is the predicted probability of the positive class):

$$\ell = -\big[\,y\log p+(1-y)\log(1-p)\,\big]$$

Intuition: cross-entropy rewards "giving a high probability to the right answer". If the truth is cat but the model gives cat only a probability of 0.1, then $-\log 0.1$ is large and the penalty is heavy; if it gives cat 0.99, $-\log 0.99$ is close to 0 and there is almost no penalty.

**Why use cross-entropy rather than "accuracy" directly as the loss?** Because **accuracy is not differentiable**: it only "jumps" at the moment a prediction flips class, so its curve is a staircase and its gradient is zero almost everywhere — when the model tweaks its parameters slightly, accuracy does not budge, and gradient descent cannot work at all. Cross-entropy, in contrast, is **smooth and differentiable**: every tiny change in probability changes the loss continuously, giving a useful gradient. This leads to a key requirement 👇

## Why a loss must be "differentiable"

Gradient-based training (gradient descent and its many variants) relies on **differentiating the loss** to obtain $\nabla_\theta \mathcal{L}$, then updating the parameters in the direction that decreases the loss:

$$\theta \leftarrow \theta - \eta\,\nabla_\theta \mathcal{L}(\theta)$$

For this step to work, the loss must be (almost everywhere) **differentiable**, so that the derivative can tell us "which way to adjust and by how much". This is why we use cross-entropy rather than accuracy, and squared loss rather than a 0/1 "right or wrong" judgment — **to be optimizable, a loss must first be differentiable**.

## How the loss function connects to other concepts

- **Training = minimizing the loss**: the whole training process is about using [gradient descent](../ml/) to keep pushing $\mathcal{L}(\theta)$ down. The loss function defines "what good means", and the [optimization](../optimization/) [algorithm](../algorithms/) takes care of "how to get better".
- **Relation to regularization**: [regularization](../regularization/) simply **adds a penalty term** $\lambda\,\Omega(\theta)$ to the loss, giving $\mathcal{L}(\theta)+\lambda\,\Omega(\theta)$, which forces the model not to become too complex and thereby curbs [overfitting](../overfitting/).
- **Loss function vs. evaluation metric**: these two are easily confused. **The loss function is for "optimizing"** (it must be differentiable and is used during training), while an [evaluation metric](../evaluation-metrics/) is for "reporting" (it is meant for people and can be non-differentiable, such as accuracy, F1 or MAPE). A common practice: optimize cross-entropy during training, then report accuracy to the boss. The two point the same way, but they are not the same thing.

## A small concrete example

Compute the squared loss by hand to feel how "large errors are amplified". Three samples, with true and predicted values as follows:

```python
y      = [3.0, 5.0, 10.0]
y_hat  = [2.5, 5.5,  7.0]   # the first two are off by 0.5, the last by 3

errors = [yi - pi for yi, pi in zip(y, y_hat)]   # [0.5, -0.5, 3.0]
mse = sum(e**2 for e in errors) / len(errors)    # (0.25+0.25+9)/3 = 3.17
mae = sum(abs(e) for e in errors) / len(errors)  # (0.5+0.5+3)/3   = 1.33
```

Look at the point that is off by 3: in MAE it contributes 3, in MSE it contributes $3^2=9$ — **MSE amplifies this large error much more**, so a model minimizing MSE will try harder to accommodate this outlier.

## What it means for time series forecasting

In time series forecasting, the choice of loss function directly determines "what the model cares about":

- **MSE**: because it amplifies large errors, it **heavily penalizes predictions that miss spikes badly**. If what you fear most is "the occasional big miss" (for example in power grid dispatch), MSE is a good fit.
- **MAE**: **more robust to anomalies / outlying fluctuations**. If your series often contains sudden noise or a few absurd values and you do not want them to pull the model off course, MAE is steadier.
- **Quantile loss / pinball loss**: when you want not just a point forecast but a **probabilistic / interval forecast** ("tomorrow's sales have a 90% chance of falling within some range"), use the quantile loss. For the $\tau$-th quantile it is defined as:

$$\ell_\tau(y,\hat y)=\max\big(\tau\,(y-\hat y),\;(\tau-1)(y-\hat y)\big)$$

It **penalizes over- and under-prediction asymmetrically**: train separately with different values of $\tau$ (such as 0.1, 0.5, 0.9) and you can draw the upper and lower bounds of a prediction interval.

The core principle in one sentence: **choose the loss to match the cost of your mistakes**. Is under-stocking more costly than over-stocking? Then do not blindly use the symmetric MSE; switch to an asymmetric quantile loss.

## Summary

- A **loss function** measures the gap between predictions and true values; it is the **referee + compass** of training; training = minimizing the loss.
- Total loss $\mathcal{L}(\theta)=\frac1n\sum_i \ell(y_i, f_\theta(x_i))$, where $\ell$ depends on the task.
- Regression: **MSE** amplifies large errors and is sensitive to outliers; **MAE** is robust but has a sharp corner; **Huber** is a compromise.
- Classification: **cross-entropy** is smooth and differentiable, far better than non-differentiable accuracy.
- The loss must be **differentiable** for gradient descent to work.
- **Loss (for optimizing) ≠ evaluation metric (for reporting)**; [regularization](../regularization/) adds a penalty term to the loss.
- Time series: MSE targets spikes, MAE resists anomalies, **quantile loss** produces interval forecasts — choose according to the cost of being wrong.

[← Machine learning foundations](../ml/) · [Foundations overview](../)
