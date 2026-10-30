---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/attention/
title: "Attention"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Attention** is a mechanism that, when a model processes a given position in a sequence, **weights the other positions by their relevance** and then aggregates their information. It lets the model "skip over distance" and focus directly on the parts that truly matter; it is the core of the [Transformer](../transformer/).

## Intuition

When you read the sentence "The latte at this café is great — **it** is worth coming back to", on seeing "it" you automatically link it back to "café". This ability to "look back at relevant content when needed" is attention.

The mechanism can be compared to **looking something up in a dictionary**:

- You hold a **Query**: "What do I want to know?"
- Each dictionary entry has a **Key**: "What question can I answer?"
- And a corresponding **Value**: "The content I actually carry."

Attention first compares the Query with every Key to get a set of weights saying "how much attention it deserves", then uses these weights to take a weighted average of all the Values. **Relevant positions get large weights, irrelevant ones get small weights.**

## Mathematical formulation

The most common form is **Scaled Dot-Product Attention**:

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left( \frac{Q K^{\top}}{\sqrt{d_k}} \right) V
$$

- $Q \in \mathbb{R}^{L \times d_k}$: the query matrix; each row is the query vector of one position, and $L$ is the sequence length;
- $K \in \mathbb{R}^{L \times d_k}$: the key matrix;
- $V \in \mathbb{R}^{L \times d_v}$: the value matrix;
- $Q K^{\top} \in \mathbb{R}^{L \times L}$: the dot-product similarity matrix between every query and every key;
- $\sqrt{d_k}$: a scaling factor that prevents large dot products from pushing the softmax into its saturated region, where the [gradient](../gradient/) is tiny;
- $\mathrm{softmax}$: normalizes each row into weights that sum to 1;
- the final multiplication by $V$: a weighted sum of all the values.

$Q, K, V$ are usually all obtained from the same input $X$ by linear transformations ($Q = XW_Q$, etc.); when all three come from the same sequence, this is called **Self-Attention**.

**Multi-head attention** runs $h$ copies of the formula above in parallel (each focusing on a different aspect) and concatenates them, letting the model capture several kinds of dependencies at once, such as "syntactic relations" and "numerical correlations".

{% include fviz/attention-heat.html %}

## A concrete example

Suppose the sequence has only 3 positions, and the dot products of a query with the three keys (after dividing by $\sqrt{d_k}$) are $[2.0,\ 0.0,\ 1.0]$. Softmax:

$$
\frac{[e^{2}, e^{0}, e^{1}]}{e^{2}+e^{0}+e^{1}} = \frac{[7.39,\ 1.00,\ 2.72]}{11.11} \approx [0.66,\ 0.09,\ 0.25]
$$

So the output is $\approx 0.66\,V_1 + 0.09\,V_2 + 0.25\,V_3$: position 1 is the most relevant (weight 0.66) and dominates the result. This is what "relevance-weighted aggregation" looks like in concrete terms.

## Why it matters / where it is used

- **Direct access to long-range dependencies**: unlike an [RNN](../rnn/), which must pass information step by step, attention **connects any two positions in a single step**, so long-distance relations no longer decay with distance.
- **Fully parallel**: the whole $QK^\top$ is computed in one matrix multiplication, so training is much faster than with recurrent structures.
- **Interpretable**: visualizing the attention weights shows "where the model is looking".
- It is the foundational component of the [Transformer](../transformer/) and of almost every large language model.

## Relevance to time series forecasting

Attention lets a forecasting model **directly align time points that are far apart** — for example, linking "this morning" to "the same time slot last week" to capture periodicity; this is its advantage in long-sequence forecasting.

But there is an unavoidable cost: the similarity matrix $QK^\top$ has size $L \times L$, so **both computation and memory are $O(L^2)$**. When the history window spans thousands of steps, this quadratic cost becomes very expensive.

This is precisely one of the starting points of this site's featured model, **Kernel U-Net (KUN)**: rather than performing expensive $O(L^2)$ attention over the full-length sequence, KUN uses [U-Net](../u-net/)-style **multi-scale downsampling** to capture long-range structure on shorter, coarser sequences at a lower cost. **Attention is not rejected** — it can perfectly well be embedded as a component at one of the scales; what KUN changes is "at which granularity, and at what cost" long-range dependencies are modeled.

## Summary

- Attention = weighting and aggregating **Values** by **Query–Key similarity**; relevant items get more attention.
- Self-attention **connects any two points in a sequence in a single step**, capturing long-range dependencies in parallel.
- The cost is $O(L^2)$, which is expensive on long sequences — this is the motivation for KUN's multi-scale alternative.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
