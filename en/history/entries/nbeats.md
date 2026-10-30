---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2019 · Computing"
permalink: /en/history/e/nbeats/
title: "N-BEATS: Purely Feed-Forward Forecasting (Oreshkin et al., 2019)"
lead: "Do deep models really need recurrence or attention to forecast time series? With a stack of feed-forward blocks and double residuals, N-BEATS cleanly outperformed the statistical baselines."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 9 · Deep Learning](../../09/).

### Background

By 2018, deep learning faced an awkward fact: in large forecasting competitions such as M3 and M4, **pure statistical methods and simple combinations often beat complex neural networks**. Even the winner of the M4 competition was a hybrid of statistics and machine learning. This raised a doubt: could a pure deep model win on univariate forecasting on its own, without relying on hand-crafted time series feature engineering?

### The problem

Most deep forecasters of the time were based on [RNNs](../rnn/): sequential, hard to train, and often criticized as "black boxes". **Could one design a purely deep architecture, with no time-series-specific components (such as recurrence, attention or decomposable statistical priors), that both led in accuracy and could optionally retain interpretability?**

### Other approaches of the time (and their limits)

- **Statistical baselines (ARIMA / ETS / Theta)**: robust and interpretable, but of limited expressiveness, and hard to use for jointly learning complex patterns across many series.
- **RNN-style deep forecasting (such as [DeepAR](../deepar/))**: expressive, but trained sequentially and weak on interpretability.
- **Hand-built statistical + ML hybrids (the M4 winner)**: highly accurate but complex to engineer, dependent on extensive manual design, and hard to reuse end to end.

### Method

N-BEATS breaks forecasting down into a stack of **fully connected blocks**. Each block reads the lookback window and produces two outputs: a **backcast** (a reconstruction of its own input) and a **forecast** (a prediction of the future). The blocks are chained by **doubly residual stacking**: each block subtracts the part it has explained from the input and passes the residual on to the next block:

$$ x^{(\ell)}=x^{(\ell-1)}-\widehat{x}^{(\ell)}_{\text{back}},\qquad \widehat{y}=\sum_{\ell}\widehat{y}^{(\ell)}_{\text{fore}} $$

Each block first uses several fully connected layers to produce expansion coefficients, then projects them onto a set of **basis functions** $$g$$:

$$ \widehat{y}^{(\ell)}_{\text{fore}}=\sum_{i} \theta_i\, g_i $$

In the **generic version**, $$g$$ is learnable; in the **interpretable version**, a polynomial basis (trend) and a Fourier basis (seasonality) are deliberately chosen, so that separate stacks produce a trend component and a seasonal component, and the forecast can be read by humans. The whole network has no recurrence and can be trained in parallel.

### Impact

N-BEATS **outperformed across the board** strong baselines, including the M4 winner, on several public benchmarks such as M3, M4 and Tourism, without using any time-series-specific feature engineering. It also showed good **transferability**: a model trained on one group of datasets remained competitive on unseen datasets, foreshadowing the possibility of "pretrain, then forecast zero-shot".

### Significance and outlook

With the plainest feed-forward structure, N-BEATS proved that **a pure deep model can beat statistical baselines on its own**, and through double residuals and basis projection it elegantly balanced accuracy with interpretability. It inspired later patch-based and decomposable forecasters, and the direction of pushing "pretrain and transfer" toward time series foundation models ([../foundation-models/](../foundation-models/)). Amid the rush toward the [Transformer](../transformer/), it is also a reminder that a simple architecture, if well designed, can still be highly competitive.
