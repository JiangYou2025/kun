---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1997 · Computing"
permalink: /en/history/e/lstm/
title: "Long Short-Term Memory (Hochreiter · Schmidhuber, 1997)"
lead: 'In an ordinary RNN, gradients decay exponentially through time. LSTM builds a "conveyor belt" that barely decays, then uses three gates to decide what to remember, what to forget and what to let out.'
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 7 · Neural Networks](../../07/).

### Background

By the mid-1990s, the potential of [recurrent neural networks (RNNs)](../rnn/) for processing sequences was recognized, but their **vanishing / exploding gradient** problem had become a practical roadblock. Hochreiter's work pinned down the cause precisely: during backpropagation through time, the gradient is repeatedly multiplied by the same set of factors, so the error signal decays or blows up exponentially through time, and the network cannot learn dependencies that are far apart. For sequence models to truly "remember things from far back", this had to be cured at the level of the architecture.

### The problem

The difficulty can be stated precisely: in BPTT, the gradient of the loss with respect to early states is a long product of Jacobians, whose spectral properties make the error signal either vanish or explode. **Can one design a recurrent unit in which the error signal flows through time almost losslessly (neither vanishing nor exploding), so that long-range dependencies can be learned stably?**

### Other approaches of the time (and their limits)

- **Gradient clipping + plain RNN**: can contain exploding gradients but does nothing against vanishing ones, so long-range dependencies still cannot be learned.
- **Second-order / specialized optimizers**: try to get around pathological gradients, but are expensive and unstable, and do not address the structural root cause.
- **Echo state networks / time-constant RNNs (somewhat later)**: mitigate the problem with fixed random recurrent weights or multi-scale time constants. The ideas are novel, but either the recurrent layer is not trained or the expressive power is limited.

### Method

The core of LSTM is a **cell state** $$c_t$$ that acts as an "information conveyor belt" running through time. Its update is mainly **additive** rather than repeatedly multiplicative, which forms a **Constant Error Carousel**: the error can flow back through time with almost no decay. Around it sit three **gates** (sigmoid $$\sigma$$ gates with values in $$[0,1]$$) that regulate writing, keeping and reading information:

$$ f_t=\sigma(W_f[h_{t-1},x_t]+b_f),\quad i_t=\sigma(W_i[h_{t-1},x_t]+b_i),\quad o_t=\sigma(W_o[h_{t-1},x_t]+b_o) $$

The candidate information and the cell / hidden state updates are:

$$ \tilde{c}_t=\tanh(W_c[h_{t-1},x_t]+b_c),\qquad c_t=f_t\odot c_{t-1}+i_t\odot \tilde{c}_t,\qquad h_t=o_t\odot \tanh(c_t) $$

Intuitively, the **forget gate** $$f_t$$ decides how much old memory to keep, the **input gate** $$i_t$$ decides how much new information to write, and the **output gate** $$o_t$$ decides how much is currently exposed to the outside. The key is the additive path $$c_t=f_t\odot c_{t-1}+\dots$$: when $$f_t\approx 1$$, the gradient of $$c_t$$ with respect to $$c_{t-1}$$ is approximately 1, and the error signal can cross hundreds or thousands of steps with almost no decay. That is the mathematical root of its ability to learn long-range dependencies.

### Impact

LSTM can reliably learn dependencies hundreds or even thousands of steps apart, far beyond a plain RNN. It long dominated sequence tasks such as speech recognition, handwriting recognition, machine translation and language modelling (until the Transformer era), and spawned leaner variants such as the GRU. "Gating + an additive memory channel" became the standard paradigm of sequence modelling.

### Significance and outlook

LSTM solved head-on the long-range dependency problem that had plagued RNNs for years, through architectural innovation rather than more aggressive optimization, and it is one of the foundational works of deep learning for sequences. It brought the idea of "controllable memory" into neural networks and deeply influenced the later attention mechanism (which likewise chooses "which part of the history to attend to"). Even today, with Transformers dominant, the intuitions of gating and state passing remain alive in all kinds of state-space sequence models and efficient long-sequence architectures.
