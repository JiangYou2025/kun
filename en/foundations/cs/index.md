---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/cs/
title: "Computer Science Fundamentals"
lead: "Programming, data structures and algorithms, the scientific computing stack and engineering practice — the computing skills you need to actually get models running. A framework of concepts only."
prev: /foundations/math/
next: /foundations/ml/
---

> This is a **concept map**: it lists the basic computing skills you should have for working with data and building models. Real mastery comes from hands-on practice.

## 1. [Programming](../programming/) basics ([Python](../python/))

The common language of data science.

- **Basic types and [data structures](../data-structures/)**: numbers / strings / lists / dictionaries / sets
- **Control flow**: conditionals, loops, functions
- **Object orientation and modules**: classes, packages, imports
- **Environment management**: `venv` / `conda`, dependencies and [reproducibility](../reproducibility/)

## 2. Data structures and [algorithms](../algorithms/)

Write code that is both correct and fast.

- **Core data structures**: arrays, hash tables, stacks / queues, trees, graphs
- **Complexity analysis ([Big-O](../big-o/))**: time and space costs
- **Common algorithms**: sorting, searching, recursion, [dynamic programming](../dynamic-programming/)
- **Numerical stability**: floating-point error, overflow and underflow

## 3. The scientific computing stack

Everyday tools for time series and machine learning.

- **[NumPy](../numpy/)**: N-dimensional arrays and **[vectorized](../vectorization/)** operations (orders of magnitude faster than Python loops)
- **[Pandas](../pandas/)**: tables / time indexes, resampling, alignment
- **Matplotlib**: visualization
- **Key idea**: replace explicit loops with **vectorization**

```python
import numpy as np
x = np.arange(1000)
y = x ** 2          # vectorized: one line beats a for loop
```

## 4. Computer systems basics

Understand where performance comes from.

- **Memory and caches**: where data lives determines how fast it is
- **CPU vs [GPU](../gpu/)**: why parallel computing made deep learning possible
- **Parallelism and batching**: the hardware motivation for [batch](../batch/) operations
- **Storage formats**: trade-offs between CSV / Parquet / binary

## 5. [Engineering practice](../engineering-practice/)

Make your work reproducible and collaborative.

- **Version control ([Git](../git/))**: commits, branches, collaboration
- **Jupyter Notebook**: interactive exploration and presentation
- **Reproducibility**: fix random seeds, record dependency versions
- **Debugging and logging**: locate problems instead of changing things blindly

---

**Key terms:** [Python](../python/), [data structures](../data-structures/), [Big-O complexity](../big-o/), [dynamic programming](../dynamic-programming/), [NumPy](../numpy/), [vectorization](../vectorization/), [Pandas](../pandas/), [GPU parallelism](../gpu/), [batch](../batch/), [Git](../git/), [reproducibility](../reproducibility/).
