---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2017 · Computing"
permalink: /en/history/e/transformer/
title: "The Transformer and Self-Attention (Vaswani et al., 2017)"
lead: "Recurrent networks must unroll step by step through time. Could any two positions talk to each other directly, with the whole sequence computed in parallel? Self-attention made it happen."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 9 · Deep Learning](../../09/).

### Background

From 2014 on, the workhorses of sequence modelling were the [RNN](../rnn/) and its gated variants [LSTM](../lstm/) and GRU, combined with an encoder–decoder architecture and an "attention" mechanism for machine translation. Attention started out as an add-on to the RNN: at each decoding step it looks back at all the encoder's hidden states and weights them by relevance. It had already shown that "making distant information directly reachable" is extremely useful.

### The problem

But recurrent structures have two hard flaws. The first is that they are **sequential**: the hidden state $$h_t=f(h_{t-1},x_t)$$ must be computed step by step in time order, so there is no parallelism along the sequence length and training is slow. The second is the **decay of long-range dependencies**: information has to propagate through $$O(n)$$ steps to get from one end of the sequence to the other, and gradients tend to vanish along the way. **Could the recurrence be removed, so that any two positions connect in a single step while the whole sequence is processed in parallel?**

### Other approaches of the time (and their limits)

- **Pure LSTM/GRU sequence-to-sequence**: expressive, but inherently sequential, with long information paths on long sequences and limited training throughput.
- **Convolutional sequence models (ConvS2S, ByteNet)**: parallelizable, but two distant positions still need a stack of $$O(\log n)$$ or $$O(n)$$ convolutional layers before they can interact.
- **Attention as an add-on**: the right direction, but still parasitic on a recurrent backbone, without replacing recurrence altogether.

### Method

The Transformer's slogan was "Attention is All You Need": replace recurrence entirely with self-attention. The input is projected into queries $$Q$$, keys $$K$$ and values $$V$$; each position computes a compatibility score with every position and takes a weighted sum:

$$ \mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V $$

where $$\sqrt{d_k}$$ is a scaling factor that keeps the dot products from growing so large that the softmax gradients saturate. **Multiple heads** learn relations in different subspaces in parallel, and **positional encodings** inject order information (self-attention by itself is permutation-invariant):

$$ PE_{(pos,2i)}=\sin\!\Big(\frac{pos}{10000^{2i/d}}\Big),\quad PE_{(pos,2i+1)}=\cos\!\Big(\frac{pos}{10000^{2i/d}}\Big) $$

The interaction path between any two positions has length $$O(1)$$, and an entire layer can be computed in parallel in one go (at the cost of an $$O(n^2)$$ attention matrix).

### Impact

On machine translation benchmarks, the Transformer set new BLEU records of the time with less training time. More far-reaching was its **scalability**: stacking more layers and adding more data kept improving performance, which directly gave rise to large-scale pretrained models such as BERT and GPT, and spilled over into vision, speech, time series forecasting and almost every other sequence domain.

### Significance and outlook

The Transformer switched sequence modelling from "recursion along time" to "global attention + parallelism", and became the common foundation of modern large models ([../foundation-models/](../foundation-models/)). It has also been widely adapted for time series forecasting (sparse attention, patched inputs and so on, to tame the $$O(n^2)$$ cost). And the quest for efficiency on very long sequences in turn led to state space models that embrace "linear recurrence" once again ([../s4/](../s4/), [../mamba/](../mamba/)) — history has staged a fascinating dialogue between recurrence and attention.
