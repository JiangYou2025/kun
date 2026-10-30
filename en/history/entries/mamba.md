---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2023 · Control / Communications"
permalink: /en/history/e/mamba/
title: "A State Space That Chooses (Mamba, 2023)"
lead: 'Make the parameters of a state-space model depend on the input: "selectivity" gives it the ability to forget and to focus, and combined with a hardware-aware parallel scan, it models very long sequences in linear time.'
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

The Transformer's self-attention buys direct connections between arbitrary positions at a cost of $$O(L^2)$$, and struggles once sequences get long. Another thread comes from control theory's **state-space models (SSMs)**: a hidden state is updated recursively through time, which is naturally linear in time. Structured SSMs such as S4 had already shown that discretizing a classical continuous-time system and parameterizing it carefully can match Transformers on long-sequence benchmarks, with $$O(L)$$ recurrent inference. Mamba (Gu and Dao, 2023) is the key leap along this line.

### The problem

Earlier SSMs were mostly **linear time-invariant (LTI)**: the transition matrices $$A,B,C$$ are fixed, independent of the content currently being seen. That makes them efficient, but they lack a core ability: **selectively remembering or forgetting based on content**. Attention is powerful precisely because it allocates weights dynamically according to the input. **Can SSMs also acquire this content-dependent selectivity without losing the efficiency of linear time?**

### Other approaches of the time (and their limits)

- **Self-attention Transformers**: extremely strong content selectivity, but $$O(L^2)$$ compute and memory, which makes very long sequences expensive.
- **Linear time-invariant SSMs ([S4](../s4/) and others)**: linear time and stable over long ranges, but the parameters do not depend on the input, so different content cannot be treated differently, and fine-grained "focus / ignore" behaviour is hard.
- **Linear attention / gated convolutions**: faster, but often at the cost of expressiveness, with quality on long sequences below that of full attention.

### Method

Mamba introduces the **selective SSM**: the discretization step $$\Delta$$ as well as $$B,C$$ become **functions of the current input**, so the same mechanism can change its memory dynamics according to content. Its continuous form is

$$ \frac{dh(t)}{dt} = A\,h(t) + B\,x(t),\qquad y(t) = C\,h(t) $$

After discretization (zero-order hold), we obtain the recurrence $$h_t = \bar{A}h_{t-1} + \bar{B}x_t,\; y_t = C h_t$$, where

$$ \bar{A} = \exp(\Delta A),\qquad \bar{B} = (\Delta A)^{-1}(\exp(\Delta A)-I)\,\Delta B $$

The key is that $$\Delta,B,C$$ now depend on $$x_t$$: a large step $$\Delta$$ writes new information strongly (focus), while a small one preserves the old state (skip / forget). The price is that the model is no longer time-invariant and cannot be computed in one pass as a convolution. Mamba's answer is a **hardware-aware parallel scan**: the intrinsically sequential recurrence is unrolled efficiently on GPUs with a prefix-sum-style parallel algorithm, and kernel fusion keeps the intermediate states in fast SRAM, so training is parallel while inference remains an $$O(L)$$ recurrence.

### Impact

On long-sequence tasks in language, audio and genomics, Mamba matches or exceeds Transformers of the same size; its inference throughput scales linearly with sequence length, and with long contexts its advantages in memory and speed are substantial. It shows that content-dependent selectivity need not be a monopoly of attention; it can also grow inside a state-space model.

### Significance and outlook

Mamba stitches together the state-space language of control theory and the "selectivity" of modern deep learning, offering a strong candidate backbone for "linear-time long-sequence modelling". This is especially fitting for time series, which are themselves the product of sampling continuous systems: the continuous-time foundations of SSMs share a natural origin with them (see how [Neural CDE](../neural-cde/) handles irregular sampling). In the present age of large models and [KUN](../kun/), Mamba, alongside attention and convolution, has become one of the pluggable "per-layer operator" options: [Kernel U-Net](../kun/) argues precisely for decoupling the multi-scale structure from the specific operator, and the selective SSM is a high-quality kernel that balances efficiency with long-range memory. From Yule's linear recurrences to today's state spaces that "choose", time series modelling has kept advancing along the same main line.
