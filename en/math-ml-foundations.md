---
updated: "2026-06-11"
lang: en
ref: math-ml-foundations
permalink: /en/math-ml-foundations/
title: "Mathematics and Machine Learning Foundations"
lead: "On the previous page you fitted a trajectory by hand — and that is the heart of machine learning: describe a pattern with mathematics, find the best pattern with optimization, and learn the pattern from data. This page is only an introduction that points you to the systematic foundation courses."
prev: prediction-in-action
next: linear-autoregression
---

## Three things behind forecasting

In the artillery game you kept adjusting the angle and the power until you hit the target. What machine learning does is **automate** this "tune → fit → predict" loop, and it rests on three foundations:

- **Describe patterns with functions** — a pattern is an "input → output" mapping, and the parameters are the adjustable "knobs".
- **Find the best parameters with optimization** — define a loss function that measures how good a fit is, then drive it down to its minimum with gradient descent.
- **Learn patterns from data with machine learning** — the point is not to memorize the training data but to be accurate on data you have never seen (generalization — don't overfit).

> Want the intuition and the formulas? The foundation courses below explain each piece in full — this page doesn't repeat them; it just sends you there.

## Building the foundations systematically

These [foundation courses](../foundations/) form a more complete concept map. They only lay out the framework and explain the concepts, so consult them as needed:

- [📐 **Mathematics**](../foundations/math/) — [calculus](../foundations/calculus/), [linear algebra](../foundations/linear-algebra/), [probability and statistics](../foundations/probability-statistics/), [optimization](../foundations/optimization/), [information theory](../foundations/information-theory/)
- [💻 **Computer science**](../foundations/cs/) — [programming](../foundations/programming/), [data structures](../foundations/data-structures/) and [algorithms](../foundations/algorithms/), [the scientific computing stack](../foundations/scientific-computing/), [engineering practice](../foundations/engineering-practice/)
- [🤖 **Machine learning**](../foundations/ml/) — [supervised](../foundations/supervised-learning/) / [unsupervised learning](../foundations/unsupervised-learning/), [model families](../foundations/model-families/), [the training pipeline](../foundations/training-pipeline/), [generalization](../foundations/generalization/) and [evaluation](../foundations/evaluation-metrics/)
- [🧠 **Deep learning**](../foundations/dl/) — [neural networks](../foundations/neural-network/), [backpropagation](../foundations/backpropagation/), [optimizers](../foundations/optimizer/), [common architectures](../foundations/architectures/), [training practice](../foundations/training-practice/)

For a systematic treatment of the methods and formulas, you can also go straight to the [introductory time series lecture notes (17 lectures)](../course/).

## Why this matters for forecasting

A real time series contains both predictable patterns and unpredictable noise. A model's skill lies in **learning the patterns while ignoring the noise** — neither so simple that it misses the trend and the cycles, nor so complex that it mistakes random jitter for a pattern. Modern forecasting models (including KUN, which comes later) often have millions of parameters; the more expressive a model is, the more it must strike a balance between "learning enough" and "not learning too much".

> On the next page we bring this mathematics down to a first concrete model: **autoregressive forecasting** with a **linear model**.
