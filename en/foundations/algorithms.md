---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/algorithms/
title: "Algorithms"
no_comments: true
math: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

An **algorithm** is a clear, finite sequence of steps for solving a class of problems. Given an input, executing these steps one by one is guaranteed to produce the correct output. It is the "soul" of a program, while [data structures](../data-structures/) are the "body" it operates on.

## Intuition

Imagine you need to find the name "Zhang Wei" in a thick paper phone book.

- **The clumsy way**: start at page one and turn page after page until you find it. This is called **linear search**; in the worst case you have to go through the whole book.
- **The clever way**: open the book in the middle, check whether "Zhang" is in the first or the second half, discard one half, then open the remaining half in the middle… Each look eliminates half. This is called **binary search**.

Both methods will find the person, but their efficiency is worlds apart. For a phone book of 1 million people, linear search needs up to 1 million looks in the worst case, binary search only about 20 (because $2^{20} \approx 10^6$). **This is the power of algorithms: for the same problem, a good algorithm can be tens of millions of times faster.**

Algorithms are concerned not only with "can it be solved" but even more with "how much time and memory does it take to solve". The yardstick for this is [Big-O complexity](../big-o/).

## Key points

An algorithm usually has to satisfy a few properties:

- **Finiteness**: a finite number of steps; it must stop (no infinite loops).
- **Definiteness**: every step is clear and unambiguous.
- **Input and output**: it takes in data and produces a result.
- **Effectiveness**: every step can be completed in finite time.

When designing algorithms, the most common "recipes" (paradigms) include:

- **Brute force**: try every possibility. Simple but often slow.
- **Divide and conquer**: split a big problem into small ones, solve them separately, then combine (e.g., merge sort, binary search).
- **Greedy**: at each step pick what currently looks best, hoping for a global optimum.
- **[Dynamic programming](../dynamic-programming/)**: break the problem into overlapping subproblems and cache intermediate results to avoid recomputation.

## An example

The Python code below compares linear search and binary search:

```python
def linear_search(arr, target):
    """Scan from start to end, worst case O(n)"""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):
    """Requires arr to be sorted; halves the range each time, O(log n)"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1     # target is in the right half
        else:
            hi = mid - 1     # target is in the left half
    return -1

data = list(range(1_000_000))   # sorted: 0,1,2,...,999999
print(binary_search(data, 987654))   # output: 987654
```

`binary_search` needs only about 20 comparisons on a million elements; `linear_search` needs up to 1 million in the worst case. Note that binary search has a **precondition**: the data must already be sorted — a perfect illustration of how algorithms and data structures work together.

## Relevance to time series forecasting

Time series analysis is full of algorithms:

- **DTW (Dynamic Time Warping)** uses [dynamic programming](../dynamic-programming/) to align two sequences that run at different speeds.
- **FFT (Fast Fourier Transform)** reduces computing a spectrum from $O(n^2)$ to $O(n\log n)$, making periodicity analysis feasible on long sequences.
- When training models such as **KUN / Kernel U-Net**, efficiently slicing long sequences into windows and performing convolutional downsampling are, at heart, problems of algorithm and data structure design.

When the data grows from a few thousand to several million time points, **an $O(n^2)$ implementation may simply fail to run**, whereas an $O(n\log n)$ version finishes in seconds. Choosing the right algorithm often helps more than buying a faster machine.

## Summary

- Algorithm = a finite, definite sequence of steps that solves a problem; the yardstick of quality is [complexity](../big-o/).
- The same problem can have many algorithms, whose efficiency may differ by several orders of magnitude.
- Common paradigms: brute force, divide and conquer, greedy, [dynamic programming](../dynamic-programming/).
- Algorithms and [data structures](../data-structures/) are inseparable — only with the right structure can an algorithm be fast.

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
