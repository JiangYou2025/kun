---
updated: "2026-06-11"
lang: en
ref: kun
permalink: /en/kun/
title: "Frontier Problems in Time Series, 2026"
lead: "After nearly a century of development, time-series forecasting has built up a large toolkit of mature methods. Yet in 2026 researchers are still asking: can we do better? This page surveys the six hottest frontier challenges today and looks at how Kernel U-Net tries to answer some of them."
prev: linear-autoregression
next: kernel-u-net
math: true
---

## Where forecasting stands today

After a hundred years of development (from Yule's autoregression in 1927 to today), time-series forecasting has accumulated a large set of mature tools. But researchers keep asking: **can we do better?**

In 2026, the field's hottest directions can be grouped into six frontier problems.

## 🧩 Six frontier problems

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌍</div>
    <h3>Foundation Models</h3>
    <p>GPT transformed NLP — can foundation models do the same for time series? Models such as TimesFM (Google), Chronos (Amazon) and Moirai (Salesforce) are pretrained on massive amounts of time-series data in pursuit of "zero-shot forecasting": predicting without ever seeing your data. But time series are far more diverse in distribution than text, and how well this transfers is still an open question.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> can a single model handle electricity, finance, weather and healthcare all at once?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📏</div>
    <h3>Ultra-Long Horizon</h3>
    <p>Traditional models already struggle to forecast 96 steps ahead, yet real-world needs often run to thousands or even tens of thousands of steps: annual power planning, climate-change modeling, genome sequence analysis. The O(N²) complexity of Transformers prevents them from handling ultra-long sequences directly, which has given rise to linear attention, state-space models (Mamba/S4) and hierarchical architectures.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> how do we keep the ability to model long-range dependencies at O(N) complexity?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🎯</div>
    <h3>Uncertainty Quantification</h3>
    <p>A point forecast (a single number) is far from enough — decision-makers need to know "how sure are you?" Probabilistic forecasting, quantile regression and conformal prediction are becoming standard. From 2024 to 2026, conformal prediction has grown explosively thanks to its "distribution-free, finite-sample coverage guarantee".</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> how do we produce prediction intervals that are both narrow and reliable?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚨</div>
    <h3>Anomaly Prediction</h3>
    <p>In many settings the question is not "what is the next value?" but "is something going to go wrong?": equipment failure, grid overload, cardiac arrhythmia. The difficulty is that anomalies are rare and take many shapes, and the goal is shifting from "detection after the fact" to "early warning". A common approach: first model the normal patterns, then treat clear deviations as a signal.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> with very few anomalous examples whose shapes keep changing, how do we spot an anomaly in advance rather than after the fact?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌐</div>
    <h3>Spatio-Temporal Forecasting</h3>
    <p>Weather forecasts, traffic flow, epidemic spread — these data change not only over time but also have structure in space. GraphCast (DeepMind) uses graph neural networks for global weather forecasting and has surpassed traditional numerical models in accuracy. Modeling temporal dependence and spatial topology at the same time is the central difficulty of spatio-temporal forecasting.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> how do we fuse graph structure (space) with sequence structure (time)?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🛡️</div>
    <h3>Generalization</h3>
    <p>Models shine on clean benchmark datasets and then collapse in the real world: missing data, sensor drift, sudden distribution shifts (COVID was one enormous distribution shift). How can a model avoid breaking down in "situations it has never seen"? Domain adaptation, transfer learning, meta-learning and online learning are the main weapons today.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Core challenge:</strong> how do we keep a model effective in new domains and under new distributions?</p>
  </div>
</div>

## Answering these questions with Kernel U-Net

Faced with these challenges, the exploration this site offers is **KUN (Kernel U-Net)**. KUN splits a model into two parts: a fixed **U-shaped skeleton**, and an **interchangeable kernel** at every level. So responding to a new problem rarely means redesigning the model; it usually takes a change in just one place: **swap a kernel**, **add a component to the skeleton**, or **change the output head**. The table below gives the entry point for each of the six problems. Most of them are explorations still in progress, not finished answers:

| Frontier problem | What changes | KUN's approach |
|------------------|--------------|----------------|
| Foundation models | Swap the kernel | Use MoE (mixture-of-experts) kernels and more levels, and see whether data from more domains can be trained into a single base model |
| Very long sequences | Add a component | Add a memory layer to the U-shaped skeleton to remember a longer history; level-by-level downsampling also shortens the sequence at deep levels, so they can afford heavier kernels |
| Uncertainty quantification | Change the output head | Point forecasts by default; quantile regression or conformal prediction can be attached to the output to give prediction intervals |
| Anomaly prediction | Change the output head | Replace "predict future values" with "predict the future distribution (density)", and raise an early warning when actual observations fall into low-density regions |
| Spatio-temporal forecasting | Change the skeleton | Apply the hierarchy along the spatial axes as well, so the level-by-level downsampling / upsampling covers both time and space |
| Generalization | Swap the kernel | Adaptive forecasting: choose or adapt each level's kernel according to the characteristics of the data, to transfer to unseen domains and distributions |

The core intuition: **write the skeleton once, and realise new ideas by swapping kernels and adding components.** These frontier questions therefore do not require a giant model; ordinary compute is enough to get started. Each new direction means writing one new kernel or module and plugging it into the same lightweight skeleton.

> KUN's full ideas, layer-by-layer architecture, complexity analysis and getting-started tutorial all live on a dedicated page:
> **[Understanding Kernel U-Net in depth](../kernel-u-net/)**.

## Where to go next

- **To see how KUN responds to these challenges**: read [Understanding Kernel U-Net in depth](../kernel-u-net/), which covers everything from the U-shaped structure to a step-by-step tutorial.
- **To shore up your math / machine-learning foundations**: go back to the [foundations course](../foundations/).
- **To see how these problems came about step by step**: read the [history of time series](../history/).

<div class="hint">This page only takes stock of the "problems"; KUN, as one possible "answer", is covered in detail in <a href="{{ '/en/kernel-u-net/' | relative_url }}">Understanding Kernel U-Net in depth</a>.</div>
