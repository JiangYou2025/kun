---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/big-o/
title: "Big-O Complexity"
no_comments: true
math: true
---

> Part of [Computer science foundations](../cs/) · [Foundations overview](../)

**Big-O notation** describes roughly **how the time or memory** an [algorithm](../algorithms/) needs **grows** as the input size $n$ gets larger. It is the standard yardstick for whether an algorithm "scales".

## Intuition

Big-O does not care about "how many milliseconds it ran", but about "**when the data doubles, how many times larger does the cost get**". It deliberately ignores constants and lower-order terms and looks only at the "shape" of the growth.

As an analogy, suppose you need to notify a group of people:

- Post one announcement in the group chat — one step, no matter how many people. This is $O(1)$, **constant time**.
- Phone everyone one by one — double the people, double the calls. This is $O(n)$, **linear**.
- Have everyone shake hands with everyone else — double the people, four times the handshakes. This is $O(n^2)$, **quadratic**.

$$O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(2^n)$$

The further left, the better. Watch out for **exponential** growth such as $O(2^n)$: at $n=50$ it is already an astronomical number, and the algorithm basically "won't finish".

{% include fviz/big-o.html %}

## Key points

How do you read off the complexity of a piece of code? Look at how the loops are nested:

- No loops, just a few assignments → $O(1)$.
- One loop that scans the data once → $O(n)$.
- Two nested loops that each run $n$ times → $O(n^2)$.
- The problem size is halved at each step → a $\log n$ appears.
- Divide and conquer + a full scan at each level (e.g. merge sort) → $O(n\log n)$.

Two simplification rules:

- **Drop constant factors**: $O(3n)$ is written $O(n)$.
- **Keep only the highest-order term**: $O(n^2 + n)$ is written $O(n^2)$.

By default, Big-O describes an upper bound on growth in the **worst case**.

## An example

The three functions below each have a different complexity:

```python
def first(arr):              # O(1): look only at the first element
    return arr[0]

def total(arr):             # O(n): one pass
    s = 0
    for x in arr:
        s += x
    return s

def all_pairs(arr):         # O(n^2): compare every pair once
    dups = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                dups.append((i, j))
    return dups
```

The rough effect when the data grows from 1,000 to 1 million (1,000 times more):

| Complexity | Data ×1000, time roughly ×… |
|---|---|
| $O(1)$ | ×1 (almost unchanged) |
| $O(n)$ | ×1000 |
| $O(n\log n)$ | a bit more than ×1000 |
| $O(n^2)$ | **×1 million** |

`all_pairs` finishes instantly on 1,000 elements, but may run for hours on 1 million — **this is why complexity matters more than how fast your machine is**.

## Relevance to time series forecasting

In long-sequence forecasting, complexity directly determines feasibility:

- Naive [self-attention](../attention/) ([Transformer](../transformer/)) is $O(n^2)$ in the sequence length $n$; as sequences get longer, both memory and time blow up — which is exactly the problem the various "efficient attention" methods try to solve.
- The **FFT** reduces spectral analysis from $O(n^2)$ to $O(n\log n)$, which is what makes periodicity analysis of long sequences feasible.
- **KUN / Kernel U-Net** shortens the sequence by downsampling layer by layer, avoiding expensive operations at the original length; in essence it trades structure for lower complexity.

When the data grows from a few thousand time points to millions, **the difference between $O(n^2)$ and $O(n\log n)$ is the difference between "won't finish" and "results in a few seconds".**

## Common misconceptions

- **Treating Big-O as an exact number of seconds**: it only describes the growth trend; it is not a stopwatch. On small data, $O(n^2)$ may even be faster than $O(n\log n)$ (smaller constants).
- **Ignoring space complexity**: memory is also measured with Big-O, and you must account for it carefully, especially when trading memory (caching) for speed.
- **Assuming the highest-order term always dominates**: this only holds when $n$ is large enough; for small $n$ the constant terms may matter more.
- **Confusing "worst case" with "average"**: binary search is $O(\log n)$ in the worst case, but only on the precondition that "the data is already sorted".

---

[← Computer science foundations](../cs/) · [Foundations overview](../)
