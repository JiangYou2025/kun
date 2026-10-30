---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1990s · Computing"
permalink: /en/history/e/rnn/
title: "Recurrent Neural Networks and BPTT (Elman · Jordan · Werbos, 1990s)"
lead: "Give the network a “memory”: feed the hidden state of the previous moment back in at this one. The price is that gradients, as they flow back through time, vanish or explode exponentially."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Chapter 7 · Neural Networks](../../07/).

### Background

From the late 1980s into the 1990s, feedforward neural networks matured thanks to the backpropagation algorithm, but they had a built-in limitation: the input dimension is fixed and samples are independent, which makes them naturally ill-suited to **variable-length, ordered** sequences. In language, speech and time series, "now" depends on "the past", and feedforward networks have no mechanism for keeping history. Researchers wanted to equip networks with a "memory", so that dependencies along the time dimension could be encoded into an internal state.

### The problem

The core difficulty has two layers. First, **how can a network carry state across time steps**, so that its output depends not only on the current input but on the entire sequence seen so far? Second, once feedback connections through time are introduced, **how can it be trained** — standard backpropagation is designed for acyclic feedforward graphs, while a recurrent structure forms loops through time.

### Other approaches of the time (and their limits)

- **Fixed-window feedforward networks / time-delay neural networks (TDNN)**: concatenate the past $$k$$ steps into a fixed-length input. Simple and effective, but any dependency outside the window is invisible, so arbitrarily long histories cannot be captured.
- **Linear state-space models (such as ARMA and the Kalman filter)**: they have a recursive state and a complete theory, but their expressive power is limited by the linearity assumption, making it hard to model complex nonlinear sequence structure.
- **Hidden Markov models (HMMs)**: the mainstream of sequence modelling, but their states are discrete and they rely on the Markov assumption and fairly strong conditional-independence structure, which limits them when expressing continuous, high-dimensional dynamics.

### Method

The **recurrent neural network (RNN)** introduces a hidden state $$h_t$$ that is updated recursively over time, storing "memory" in it explicitly. The Elman network and the Jordan network feed back the hidden layer and the output, respectively, into the input. The basic recursion is:

$$ h_t=f\big(W x_t + U h_{t-1} + b\big),\qquad \hat{y}_t=g\big(V h_t + c\big) $$

where $$W$$ processes the current input, $$U$$ connects the previous hidden state back in, and $$f$$ is a nonlinear activation (such as $$\tanh$$). The same set of weights is shared across all time steps, so sequences of any length can be processed. Training uses **backpropagation through time (BPTT, Werbos)**: the recurrent structure is "unrolled" along time into a very deep feedforward graph, and standard backpropagation is then applied, with the gradient having to pass through every time step in turn.

But this is exactly what exposes the RNN's fatal weakness. The gradient of the loss with respect to an early hidden state contains a long product of Jacobian matrices:

$$ \frac{\partial h_t}{\partial h_{k}}=\prod_{\tau=k+1}^{t}\frac{\partial h_\tau}{\partial h_{\tau-1}}=\prod_{\tau=k+1}^{t}\operatorname{diag}\!\big(f'\big)\,U^{\top} $$

When the eigenvalues of these factors stay below 1, the product **decays exponentially** with the time span $$t-k$$ — the gradient vanishes and early information cannot be learned; when they exceed 1, it **grows exponentially** — the gradient explodes and training diverges. This is the famous **long-range dependency problem**.

### Impact

The RNN allowed neural networks to process variable-length sequences natively for the first time, and showed promise in language modelling, speech, control and other tasks. But vanishing and exploding gradients made it hard in practice to learn dependencies far apart in time: in theory it can remember an arbitrarily long history, but in practice it can reliably use only the last few steps. Exploding gradients can be mitigated by clipping, but vanishing gradients are structural.

### Significance and outlook

The RNN established the sequence-modelling paradigm of "recursive hidden state + backpropagation through time", and it also put the long-range dependency problem squarely on the table. It was precisely to overcome vanishing gradients that the [LSTM](../lstm/) of 1997 built a "constant error carousel" out of gates and a cell state, after which GRUs, attention mechanisms and eventually the Transformer arrived in turn. When we talk today about the "memory" and "long-range dependencies" of sequence models, we are still using the language laid down in the RNN era.
