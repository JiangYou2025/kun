---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/dynamic-programming/
title: "Dynamic Programming"
no_comments: true
math: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

**Dynamic programming (DP)** is an [algorithmic](../algorithms/) paradigm: break a large problem into many **overlapping** smaller problems, **store** the answer to each small problem, and so avoid computing the same thing over and over.

## Intuition

The classic example is the Fibonacci sequence $F(n) = F(n-1) + F(n-2)$.

What happens if you recurse directly? Computing $F(5)$ requires $F(4)$ and $F(3)$; computing $F(4)$ in turn requires $F(3)$ and $F(2)$… **$F(3)$ gets computed several times**, the repetition grows worse the deeper you go, and the total time is exponential, $O(2^n)$.

The insight of dynamic programming is: **compute $F(3)$ once, write it down, and next time just look it up.** Each subproblem is then computed only once, and the complexity drops immediately to $O(n)$.

A problem is usually amenable to DP when it satisfies two conditions:

- **Overlapping subproblems**: the same small problems are needed again and again (otherwise caching is pointless).
- **Optimal substructure**: the optimal solution to the large problem can be assembled from optimal solutions to the smaller ones.

{% include fviz/fib-memo.html %}

## Key points

DP comes in two equivalent implementation styles:

- **Top-down + memoization**: recurse as usual, but cache results already computed and return them directly next time.
- **Bottom-up + tabulation**: start from the smallest subproblems and fill in a table (array) step by step up to the target.

Three steps for designing a DP:

1. **Define the state**: which variables describe a subproblem (e.g. "the optimal solution for the first i elements").
2. **Write the state transition equation**: how a larger state is derived from smaller ones.
3. **Fix the base cases**: what the answers to the smallest subproblems are.

## An example

Compare naive recursion with the cached version:

```python
# Naive recursion: exponential O(2^n), absurdly slow already at n=40
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# Bottom-up DP: O(n) time, O(1) space
def fib_dp(n):
    if n < 2:
        return n
    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur   # keep only the two most recent states
    return cur

print(fib_dp(50))      # 12586269025, result in an instant
```

[Python](../python/) also has a built-in decorator that adds memoization in one line:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
# With the cache, the originally exponential recursion immediately becomes O(n)
```

## Why it matters for time series forecasting

Dynamic programming is the core engine of many classic time series algorithms:

- **DTW (dynamic time warping)**: measures how similar two sequences are when they run "out of sync" at different speeds. It uses a 2-D DP table in which each cell $D[i][j]$ holds the minimum cumulative distance for aligning the two sequences' prefixes, with the transition equation:

  $$D[i][j] = d(a_i, b_j) + \min\big(D[i-1][j],\ D[i][j-1],\ D[i-1][j-1]\big)$$

- **The Viterbi algorithm**: finds the most likely state sequence in a hidden Markov model, using DP to search an exponentially large space of paths efficiently for the optimum.
- **Change-point detection, optimal segmentation**: cutting a series into segments so that the total error is minimized is also commonly solved with DP.

When these algorithms face long sequences, it is precisely DP's "compute once, store it" that brings an exponential brute-force search down to polynomial time.

## Common pitfalls

- **Thinking DP is just recursion**: recursion is only one way of writing it; the soul of DP is **caching the answers to subproblems**. Without overlapping subproblems, caching is useless.
- **An unclear state definition**: if the state is not defined correctly, the transition equation is bound to be wrong. First work out clearly "what describes a subproblem".
- **Forgetting the base cases**: if the initial values of the smallest subproblems are missing or wrong, the whole table collapses.
- **Not optimizing space**: many DPs depend only on the most recent one or two states (as with Fibonacci), so space can drop from $O(n)$ to $O(1)$.

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
