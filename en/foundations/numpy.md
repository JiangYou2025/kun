---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/numpy/
title: "NumPy"
no_comments: true
---

> Part of [Computer science foundations](../cs/) · [Foundations overview](../)

**NumPy** is the cornerstone of numerical computing in [Python](../python/). It provides an efficient multidimensional array type, `ndarray`, and a complete set of functions for [vectorized](../vectorization/) operations on whole arrays. Almost every scientific computing and [machine learning](../ml/) library (Pandas, scikit-learn, PyTorch) is built on top of it.

## Intuition

Python's built-in `list` is flexible but slow: each element is a separate Python object scattered around memory, and operations must be interpreted one element at a time.

NumPy's `ndarray` is different — it **packs numbers of a single type tightly into contiguous memory**, and hands the computation to low-level loops written in C that finish it in one go. The result: **the same computation is often tens to hundreds of times faster in NumPy than in pure Python**, and the code is shorter too.

In one sentence: **NumPy lets you write code the way you write mathematical formulas, leaving the loops to run underneath.**

## Key points

- **ndarray**: an N-dimensional array with two core attributes, `shape` and `dtype` (the element type).
- **[Vectorization](../vectorization/)**: `a + b`, `a * 2`, `np.sqrt(a)` act directly on the whole array, no loop needed.
- **Broadcasting**: arrays of different but compatible shapes are automatically aligned for operations, e.g. "subtract the same vector from every row of a matrix".
- **Slicing and indexing**: `a[1:5]`, `a[:, 0]`, `a[a > 0]` (boolean indexing) are flexible and efficient, and mostly return **views** (no data is copied).
- **Axes**: when aggregating, specify the direction: `a.mean(axis=0)` averages over each column, `axis=1` over each row.

## An example

Feel the power of vectorization — square a million numbers and add one:

```python
import numpy as np

a = np.arange(1_000_000, dtype=float)

# The NumPy way: one line, a C loop underneath
b = a ** 2 + 1          # the whole array computed at once

# The equivalent pure Python: much slower
# b = [x**2 + 1 for x in a]
```

Broadcasting makes "column-wise standardization" very elegant:

```python
X = np.random.randn(1000, 5)          # 1000 samples, 5 features
mean = X.mean(axis=0)                  # shape (5,), mean of each column
std  = X.std(axis=0)                   # shape (5,)
X_norm = (X - mean) / std              # (1000,5) automatically minus/divided by (5,)
print(X_norm.mean(axis=0).round(6))    # each column's mean is about 0
print(X_norm.std(axis=0).round(6))     # each column's std is about 1
```

A `(1000, 5)` matrix and a `(5,)` vector can be combined directly — that is **broadcasting**: the vector is automatically "copied" to every row — though it is not actually copied, saving both memory and time.

{% include fviz/broadcast.html %}

## Relevance to time series forecasting

NumPy is the low-level engine of time series data processing:

- **Sliding windows**: cutting a long series into "past L steps → future H steps" training samples can be done with `np.lib.stride_tricks.sliding_window_view`, which generates all windows without copying, orders of magnitude faster than a Python loop.

  ```python
  series = np.arange(10)
  windows = np.lib.stride_tricks.sliding_window_view(series, 3)
  # shape (8, 3); each row is a window of length 3, with no extra memory copy
  ```

- **Batch math**: differencing, normalization, rolling statistics and FFT spectra are all array-level operations.
- **The link between layers**: the columns of [Pandas](../pandas/) are NumPy arrays underneath; the tensors fed to **KUN / Kernel U-Net** are also converted from NumPy arrays. Master NumPy and the whole [scientific computing stack](../scientific-computing/) opens up.

## Common pitfalls

- **Still writing Python `for` loops to process arrays element by element**: this throws away all of NumPy's advantages; use [vectorization](../vectorization/) instead.
- **Confusing views and copies**: slicing usually returns a **view**, so modifying it modifies the original array; for an independent copy, call `.copy()` explicitly.
- **Ignoring dtype**: division or overflow in integer arrays can give surprising results; use `astype(float)` when needed.
- **Shape mismatches**: broadcasting rules align dimensions **from right to left**; get this wrong and you will see a `shape mismatch` error.

---

[← Computer science foundations](../cs/) · [Foundations overview](../)
