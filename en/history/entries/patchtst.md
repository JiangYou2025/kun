---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2023 · Computing"
permalink: /en/history/e/patchtst/
title: "Patches as Words (PatchTST, 2023)"
lead: "Cut the series into patches and treat each one as a token, then model every channel independently — the Transformer regained its strength on time series and answered the doubts about whether attention was still needed."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 10 · Large Models and KUN](../../10/).

### Background

The single linear layer of [DLinear](../dlinear/) had badly embarrassed the Transformer on long-horizon forecasting, and for a while the community wondered whether attention had any role left to play. But experience from NLP and vision suggested that a Transformer's success or failure often lies not in attention itself but in **how the input is tokenized**. ViT achieved great success by cutting images into patches and treating them as tokens, and this offered time series a direct source of inspiration.

### The problem

Early time-series Transformers commonly made two mistakes. First, they treated **every time point** as a token: as the series grows longer, the number of tokens explodes, $$O(L^2)$$ attention becomes unaffordable, and a single point carries almost no meaning. Second, they **mixed all variables into one vector** at each time step before feeding them to the model, letting unrelated channels interfere with each other. **Could one shorten the sequence, preserve local meaning, and isolate the noise between channels all at once?**

### Other approaches of the time (and their limits)

- **Time-series Transformers with point-wise tokens (Informer and others)**: attention operates on individual time steps. Limits: each point carries little information and the sequences are too long, forcing sparse approximations that end up losing patterns.
- **Channel-mixing models**: all variables at each time step are concatenated into one vector and encoded together. Limits: weakly related or even unrelated series are forced to share a representation, which introduces crosstalk and hurts generalization.
- **Pure linear baselines (DLinear)**: simple and effective, but their expressive power is limited to linear maps, making it hard to model complex nonlinear local shapes and interactions across segments.

### Method

PatchTST does two things. The first is **patching**: a univariate series is cut into patches of length $$P$$ with stride $$S$$, and each patch serves as one token. For a series of length $$L$$, the number of tokens drops from $$L$$ to

$$ N = \left\lfloor \frac{L-P}{S} \right\rfloor + 1 $$

The attention complexity falls accordingly from $$O(L^2)$$ to $$O(N^2)$$, and each token carries the meaning of a whole stretch of local waveform. The second is **channel independence**: all variables **share the same** Transformer weights but go through the forward pass separately, never mixing inside attention — this amounts to splitting a multivariate problem into a batch of univariate problems that share one model, which reduces crosstalk and lets the vast number of sub-series act as data augmentation. Combined with masked self-supervised pretraining (randomly hiding some patches and asking the model to reconstruct them), its representational power improves further.

### Impact

On the main long-horizon benchmarks, PatchTST **comprehensively overtook** DLinear and earlier Transformer variants, with a particularly clear advantage at long look-back windows; after self-supervised pretraining it also showed considerable transfer ability. It proved that when the Transformer lost to a linear model, the fault lay in the tokenization, not in attention being useless.

### Significance and outlook

PatchTST reset the rules for time-series Transformers — **patching + channel independence** became almost the default configuration of subsequent work. The step of "cutting a series into chunks and treating them as words" is also the key interface on the way to [foundation models](../foundation-models/): large-scale pretrained models such as TimesFM, Chronos and Moirai all depend on some form of patching or tokenization to discretize continuous series into tokens a Transformer can ingest. It also makes an interesting contrast with [Kernel U-Net](../kun/): PatchTST shortens the sequence in one go with patches of fixed granularity, whereas KUN downsamples step by step across several scales with its U-shaped hierarchy — both are answering the same question: "how can operators be made to work at the right scale?" From DLinear's pointed challenge to PatchTST's forceful reply, time-series modelling went through a necessary recalibration.
