---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2020s · Computing"
permalink: /en/history/e/kun/
title: "Separating Structure from Operators (Kernel U-Net, 2020s)"
lead: "A U-shaped hierarchy takes charge of “multi-scale structure”, while pluggable kernels (linear/MLP/attention) take charge of “per-layer operators” — KUN separates the two and restores the balance between efficiency and accuracy."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 10 · Large Models and KUN](../../10/).

### Background

By the mid-2020s the debate over long-sequence forecasting had reached a stalemate. On one side, [DLinear](../dlinear/) reminded everyone that "linear extrapolation is already strong"; on the other, [PatchTST](../patchtst/) showed that "with the right tokenization, attention is still powerful"; and there were newcomers like [Mamba](../mamba/), a linear-time state space model. Each backbone had its strengths, yet each was locked into its own monolithic design: swapping an operator often meant rewriting the whole model.

### The problem

Look closely and these methods are actually answering **two different questions**: first, "how to organize information across multiple time scales" (trend/season, local/global, coarse/fine); second, "which operator to use for the transformation at a given scale" (linear, MLP, attention, SSM). Yet existing architectures often entangle the two. **Can "multi-scale structure" be decoupled from "per-layer operators", so that the structure is stably reused and operators are swapped as needed?**

### Other approaches of the time (and their limits)

- **One backbone for everything (a particular Transformer, or purely linear)**: structure and operator are bundled together, so changing the operator means changing the model, making it hard to compare "the structure's contribution" with "the operator's contribution" systematically.
- **Reducing length once with patches (PatchTST)**: cuts the series into blocks at a single fixed granularity, lacking a path of level-by-level abstraction and reconstruction across scales.
- **Heavy global attention modelling**: scale information is learned implicitly through attention, which is expensive, hard to interpret and inefficient on long sequences.

### Method

Kernel U-Net (KUN) borrows the **hierarchical encoder–decoder** idea of U-Net from computer vision and abstracts it. The encoder downsamples the series level by level, producing multi-scale representations from fine to coarse; the decoder upsamples level by level and, through skip connections, fuses the features of the corresponding scale to reconstruct the forecast window. The key innovation is to abstract the concrete transformation at each layer into a **pluggable kernel** $$K_\ell$$:

$$ h^{(\ell+1)} = \mathrm{Down}\big(K_\ell(h^{(\ell)})\big),\qquad K_\ell \in \{\text{Linear},\,\text{MLP},\,\text{Attention},\,\dots\} $$

The U-shaped hierarchy decides "at which scale to look", and the kernel $$K_\ell$$ decides "how to compute at that scale". One can therefore use cheap linear/MLP kernels in the shallow layers (fine granularity, long sequences) to keep costs down, and use expressive kernels such as attention only in the deep layers (coarse granularity, short sequences) — placing the expensive operator at the scale where it costs least. The overall complexity is roughly

$$ \mathcal{O}\!\left(\sum_{\ell} c(K_\ell)\cdot L_\ell\right),\qquad L_{\ell+1}=L_\ell / r $$

where $$L_\ell$$ is the sequence length at layer $$\ell$$, decaying geometrically with the downsampling rate $$r$$, and $$c(K_\ell)$$ is the per-step cost of that layer's kernel. Once structure and operators are decoupled, the most cost-effective combination can be assembled for each dataset like building blocks.

### Impact

On long-sequence forecasting benchmarks, KUN achieves competitive or even leading accuracy with lower compute and memory. More importantly, it provides a **unified testbed**: fix the U-shaped structure and swap only the kernels, and one can cleanly measure "how much gain the multi-scale structure brings and how much each kind of operator contributes" — a direct continuation of the question DLinear raised.

### Significance and outlook

KUN's significance lies in a design philosophy: **first separate structure from operators, then optimize each on its own**. This puts the seemingly opposed lines of recent years (linear vs attention vs SSM) in their proper places — they are simply different kernels that can be placed at different scales of the same U-shaped backbone. In the era of time series [foundation models](../foundation-models/), such a pluggable, scalable hierarchical architecture is especially valuable: for "one model to forecast every series", one needs a backbone that can accommodate heterogeneous scales while flexibly swapping kernels according to the data and the compute budget. From the selective kernel of [Mamba](../mamba/) to the continuous path operator of [Neural CDE](../neural-cde/), all of them could one day become a layer in KUN. Separating structure from operators may well be a pragmatic road towards general-purpose time series models.
