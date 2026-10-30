---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1948 · Control / Communications"
permalink: /en/history/e/shannon/
title: "Measuring Information (Shannon, 1948)"
lead: "How much information a message carries, how fast a channel can transmit reliably, how densely a continuous signal must be sampled — Shannon quantified all three at once with entropy, and opened the information age."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the 1940s, the telephone, the telegraph and radar made "how to transmit information efficiently and reliably" a pressing engineering problem, yet there was no unified measure of "amount of information". In his 1948 paper "A Mathematical Theory of Communication", Claude Shannon founded **information theory** in a single stroke: he quantified information using probability and established the fundamental limits of communication. It is one of the most foundational papers of the 20th century.

### The problem

Three intertwined fundamental questions: **How much information does a random source carry on average? How many bits per second at most can a noisy channel transmit reliably? How densely must a continuous-time signal be sampled for it to be reconstructed perfectly from its samples?** Before Shannon, there were only rules of thumb for all of these, and no theoretical limits.

### Other approaches of the time (and their limits)

- **Engineering intuition that judged everything by bandwidth and signal-to-noise ratio**: it knew that more bandwidth and a higher SNR mean more and better transmission, but could not give a precise limit for "reliable transmission", nor tell apart the two tasks of source compression and channel transmission.
- **Hartley's logarithmic measure of information (1928)**: measured information by the $$\log$$ of the number of symbols, which was the right direction, but did not bring in **probability distributions**, so it could not capture the fact that "a source with unequal probabilities is more compressible".
- **Symbol-by-symbol engineering patches for error correction**: reduced error rates through repetition and parity checks, mostly ad hoc measures, with no knowledge of whether an arbitrarily low error rate was achievable on a given channel at all — exactly the question the channel coding theorem answers.

### Method

Shannon measured the average amount of information of a discrete source $$X$$ (in bits) by its **entropy**:

$$ H(X)=-\sum_{i} p_i\,\log_2 p_i $$

$$H$$ is the limit of lossless compression: the average code length cannot fall below $$H$$ bits per symbol. For an additive Gaussian channel with bandwidth $$B$$, signal power $$S$$ and noise power $$N$$, the **channel capacity** (the maximum rate at which an arbitrarily low error rate is achievable) is

$$ C=B\,\log_2\!\Big(1+\frac{S}{N}\Big)\quad(\text{bits/s}) $$

The **channel coding theorem** asserts that as long as the transmission rate satisfies $$R<C$$, there exist codes that make the error rate arbitrarily small; if $$R>C$$, reliable transmission is impossible. On the bridge between continuous and discrete, the **Nyquist–Shannon sampling theorem** states that a signal band-limited to $$B$$ hertz can be **perfectly reconstructed** from its samples as long as the sampling rate satisfies $$f_s\ge 2B$$:

$$ x(t)=\sum_{n=-\infty}^{\infty} x\!\Big(\frac{n}{2B}\Big)\,\mathrm{sinc}\big(2Bt-n\big) $$

Sampling below $$2B$$ causes **aliasing**: high frequencies masquerade as low ones, and the information cannot be recovered.

### Impact

Information theory turned "information" from a vague notion into a computable physical quantity, and drew three limits that cannot be crossed: compression down to the entropy, transmission up to the capacity, sampling at $$2B$$. In one stroke it laid the theoretical foundations of data compression, error-correcting codes, modulation and sampling, making "approaching the limit" the common goal of communications engineering.

### Significance and outlook

Entropy, mutual information, capacity and the sampling theorem remain the common language of communications, compression and statistical learning. The sampling theorem directly dictates how every digital time series is acquired — whether each stretch of your digital signal, each sensor record, faithfully represents the original continuous process is decided by $$f_s\ge 2B$$. Entropy and mutual information in turn lead to the loss functions of modern machine learning (cross-entropy), feature selection and representation learning. This step of Shannon's is the true starting point of the digital age.
