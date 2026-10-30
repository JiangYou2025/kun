---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/data-structures/
title: "Data Structures"
no_comments: true
math: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

**Data structures** are ways of organizing and storing data. Choose the right one and common operations (lookup, insertion, deletion) are fast; choose the wrong one and the same [algorithm](../algorithms/) can be orders of magnitude slower.

## Intuition

Data structures are like storage tools, each good at something different:

- An **array (list)** is like a row of numbered lockers: if you know the number, you can grab the item instantly ($O(1)$), but to insert one in the middle, everything after it has to shift.
- A **hash table (dict)** is like an indexed dictionary: say the "key" and you flip straight to the matching "value", $O(1)$ on average.
- A **stack** is like a pile of plates: you can only take from and put on the top (last in, first out).
- A **queue** is like a line at the ticket counter: first come, first served (first in, first out).
- **Trees / graphs** are like a family tree or a subway map: they express hierarchy and connections.

**There is no "best" data structure, only the one best suited to the operations at hand.**

## Key points

Complexity differs greatly across structures and operations:

| Structure | Access by position | Search by value | Insert/delete | Typical use |
|---|---|---|---|---|
| Array list | $O(1)$ | $O(n)$ | Middle $O(n)$ | Sequential storage, random access |
| Hash table dict/set | — | $O(1)$ amortized | $O(1)$ amortized | Deduplication, counting, lookup tables |
| Stack/queue | — | $O(n)$ | Ends $O(1)$ | Undo, breadth-first search, buffering |
| Balanced tree | — | $O(\log n)$ | $O(\log n)$ | Ordered sets, range queries |

Remember one central trade-off: **trading space for time**. A hash table uses a bit more memory in exchange for near-instant lookups.

## An example

The same task — "find which elements occur more than once" — has wildly different complexity depending on the structure:

```python
# Naive approach: use a list, compare each element against all the others -> O(n^2)
def dups_slow(arr):
    seen, out = [], []
    for x in arr:
        if x in seen:        # "in list" is an O(n) linear scan!
            out.append(x)
        seen.append(x)
    return out

# Smart approach: use a set, O(1) lookup -> O(n) overall
def dups_fast(arr):
    seen, out = set(), []
    for x in arr:
        if x in seen:        # "in set" is O(1) on average
            out.append(x)
        seen.add(x)
    return out
```

The logic is almost identical; we just swapped `list` for `set`. On a million elements, `dups_fast` finishes almost instantly while `dups_slow` may run for a very long time — **changing the data structure is more effective than buying a faster machine.**

Here is another very common trick — counting with a `dict`:

```python
from collections import Counter
counts = Counter(["a", "b", "a", "c", "a"])
print(counts)            # Counter({'a': 3, 'b': 1, 'c': 1})
print(counts["a"])      # 3, retrieved in O(1)
```

## Why it matters for time series forecasting

- **Sliding windows**: cutting a long series into samples of "past L steps → future H steps" relies on efficient array slicing; with [NumPy](../numpy/)'s `stride_tricks` you can even generate all windows without copying.
- **Caching intermediate results**: [dynamic programming](../dynamic-programming/) (e.g. DTW, Viterbi) relies on 2-D arrays to store the answers to subproblems.
- **Feature lookup tables**: when mapping timestamps to features such as holidays or day of the week, a `dict` makes lookups $O(1)$.
- The downsampling and skip connections of **KUN / Kernel U-Net** are, at heart, efficient indexing and rearrangement on the tensor (multidimensional array) data structure.

## Summary

- Data structures determine how fast operations are; together with [algorithms](../algorithms/) and [Big-O complexity](../big-o/) they form a trinity.
- The central trade-off is **space for time**: hash tables/caches spend more memory to buy faster lookups.
- Rule of thumb: **use `set`/`dict` for frequent lookups, `list` for sequential access, and [NumPy](../numpy/) arrays for bulk numerical work.**
- A small change like swapping `list` for `set` can often turn $O(n^2)$ into $O(n)$.

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
