---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2020s · Computer science"
permalink: /en/history/e/foundation-models/
title: "One Model to Forecast Every Series (TimesFM · Chronos · Moirai, 2020s)"
lead: "Pre-train on vast amounts of heterogeneous series, then forecast zero-shot or few-shot out of the box — time series foundation models try to turn “train one model per task” into “one model for every series”."
math: true
---

> This is an entry in the [History of Time Series](../../) timeline, filed under [Chapter 10 · Large models and KUN](../../10/).

### Background

Language and vision entered the "foundation model" era long ago: pre-train one general-purpose model on huge amounts of data, then transfer it downstream zero-shot or with fine-tuning. Time series lagged behind for a long time — every domain, every dataset typically trained its own specialized model. But once works like [PatchTST](../patchtst/) tokenized series reliably and self-supervised pre-training across datasets proved feasible, a wave of **time series foundation models** — TimesFM, Chronos, Moirai and others — emerged in 2023–2024.

### The problem

"General purpose" is much harder for time series than for language. Series differ wildly in **sampling frequency** (seconds / hours / months), **units and scale**, **number of channels** and **periodic structure**, and there is no ready-made unified "vocabulary". **Can one pre-train a model on such a vast, heterogeneous collection of series so that it gives reliable forecasts on new data directly, without retraining?**

### Other currents of the time (and their limits)

- **Task-specific models (including classical [ARIMA](../box-jenkins/) and all kinds of deep networks)**: respectable accuracy, but every new dataset requires retraining and tuning, so transfer and cold starts are costly.
- **Purely statistical automation (auto-ARIMA / exponential smoothing libraries)**: robust and usable zero-shot, but of limited expressiveness, and hard to make use of knowledge shared across domains.
- **Early general-purpose attempts**: lacked a unified input representation and a sufficiently diverse pre-training corpus, so their generalization and zero-shot ability were limited.

### The method

These models take different routes but share a common recipe: **unified tokenization + large-scale autoregressive / masked pre-training**. Take the discretization approach (as in Chronos): first map the real-valued series onto a finite "vocabulary" by quantiles or bins, then predict the next token autoregressively, like a language model:

$$ p_\theta(x_{1:T}) = \prod_{t=1}^{T} p_\theta\big(x_t \mid x_{1:t-1}\big) $$

The model minimizes the negative log-likelihood over a huge corpus spanning domains and frequencies:

$$ \mathcal{L}(\theta) = -\,\mathbb{E}_{x\sim\mathcal{D}}\sum_{t} \log p_\theta\big(x_t \mid x_{1:t-1}\big) $$

To absorb the heterogeneity, each team has its own tricks: TimesFM uses a patch-based decoder-only Transformer and handles different horizons in a unified way; Moirai introduces multiple patch sizes and "any-variate" attention to accommodate different frequencies and multivariate data; Chronos quantizes values into tokens and reuses language model architectures directly. Once trained, faced with a new series it has never seen, the model only needs to be fed the history and asked to continue it, yielding a **zero-shot forecast** — and most of them output quantiles / probability intervals rather than single points.

### Results

On a broad range of zero-shot benchmarks, these foundation models often **come close to or even beat** specialized models carefully tuned for a single dataset, while eliminating per-task training. They also show language-model-style scaling: the more data and parameters, and the broader the coverage, the better the zero-shot generalization — for the first time, time series had a realistic path to "pre-train once, use everywhere".

### Significance and outlook

Time series foundation models bring this century-long history to a new point of convergence: from Yule's [autoregression](../yule-ar/) and Box–Jenkins [ARMA](../box-jenkins/) to [Transformers](../patchtst/), [Mamba](../mamba/) and [Neural CDEs](../neural-cde/), all the accumulated inductive biases may now be melted into one general-purpose model pre-trained on vast numbers of series. The challenges remain real: heterogeneous sampling and missing data (where the continuous-path view of [Neural CDEs](../neural-cde/) may help), efficiency over very long contexts (where [Mamba](../mamba/)'s linear time is a candidate), and how to unify multi-scale structure with a scalable backbone whose kernels can be swapped — exactly the direction of the answer offered by [Kernel U-Net](../kun/). "One model to forecast every series" has not yet been fully realized, but the direction is clear: give time series, like language, foundation models of their own. A century later, Yule's single step of "using the past to predict the next value" is being amplified without limit through pre-training.
