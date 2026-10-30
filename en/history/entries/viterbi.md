---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1967 · Control / Communications"
permalink: /en/history/e/viterbi/
title: "The Viterbi Algorithm (Viterbi, 1967)"
lead: "Among exponentially many possible paths, how do you efficiently find the single most likely sequence of hidden states? Viterbi used dynamic programming to give optimal decoding — and it still runs at the lowest layers of communication and speech systems today."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

In the 1960s, digital communication faced a hard problem: after a signal passes through encoding and a noisy channel, the receiver observes only a corrupted output and must **infer backwards** the sequence most likely to have been sent. Convolutional codes were the powerful error-correcting codes of the day, and their encoding process can be seen as a finite-state machine making state transitions over time. The later widely used **hidden Markov model (HMM)** has the same structure: hidden states evolve as a Markov chain, and each state emits observable symbols with certain probabilities.

### The problem

Given a sequence of observations, find the most likely sequence of hidden states. With length $$T$$ and $$M$$ states, there are as many as $$M^T$$ possible state paths — **exhaustive search is infeasible**. Greedily picking the best state at each time step, on the other hand, misses the global optimum because of the transition constraints between states. **How can one find the globally most likely path without enumerating exponentially many paths?**

### Other approaches of the time (and their limits)

- **Symbol-by-symbol maximum a posteriori decoding**: picks the most likely state independently at each time. It ignores the transition constraints, so the resulting sequence may be inconsistent as a whole, or even illegal.
- **Exhaustive search**: theoretically optimal, but its $$M^T$$ complexity makes it infeasible for any practical length.
- **Heuristics such as sequential/feedback decoding**: usable in some cases, but with no guarantee of optimality, and performance degrades with noise.

### Method

Viterbi used **dynamic programming** to exploit the Markov structure of the problem. Define the probability of the best partial path that reaches time $$t$$ and ends in state $$j$$:

$$ \delta_t(j)=\max_{i}\;\delta_{t-1}(i)\,a_{ij}\,b_j(o_t) $$

where $$a_{ij}$$ is the state transition probability and $$b_j(o_t)$$ the probability that state $$j$$ emits observation $$o_t$$. The essence of this recursion is that the prefix of the globally optimal path into state $$j$$ must itself be the optimal path into some predecessor $$i$$ — so at each time only one best incoming path needs to be kept for each of the $$M$$ states, and the complexity drops from $$M^T$$ to

$$ O(T\,M^2) $$

At the same time, backpointers $$\psi_t(j)=\arg\max_i\,\delta_{t-1}(i)\,a_{ij}$$ record the best predecessor; choosing $$\arg\max_j \delta_T(j)$$ at the end and tracing back along the pointers yields the globally most likely state sequence. Practical implementations usually work with logarithms, turning products into sums to avoid numerical underflow.

### Impact

The Viterbi algorithm became the standard maximum-likelihood decoder for convolutional codes, deeply shaping the reliability of systems such as deep-space communication and mobile communication (GSM, CDMA). Within the HMM framework it is also the standard tool for "decoding the most likely state sequence" in speech recognition, part-of-speech tagging and biological sequence analysis.

### Significance and outlook

For time series modelling, the Viterbi algorithm is one of the cornerstones of inference in **state space / latent-variable sequence models**: when we assume an observed sequence is driven by a hidden chain of dynamic states, it efficiently finds the optimal state trajectory. Together with the forward–backward algorithm and the [Kalman filter](../kalman/), it belongs to the family of "sequence inference on dynamic models", and it foreshadowed the broad paradigm of using dynamic programming for sequence alignment and decoding. More than half a century later, it still runs steadily at the very bottom of communication and language processing systems.
