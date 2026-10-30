---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/scientific-computing/
title: "The Scientific Computing Stack"
no_comments: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

The **scientific computing stack** is the well-coordinated toolchain for numerical computation and data analysis in [Python](../python/). At its core are [NumPy](../numpy/) (array operations), [Pandas](../pandas/) (tabular/time series processing) and [vectorization](../vectorization/) (replacing loops with whole-block operations), with Matplotlib, SciPy, scikit-learn, PyTorch and others built on top.

## Intuition

The stack is like a factory assembly line built up layer by layer:

- **At the bottom is [NumPy](../numpy/)**: compact, high-speed multidimensional arrays, the "foundation" of all numerical computing.
- **Above it is [Pandas](../pandas/)**: it adds row/column labels and time indexes to arrays, making it easy to read, align and clean data.
- **[Vectorization](../vectorization/) is the methodology running through the whole stack**: use whole-array operations like `a + b` so the underlying C code computes everything at once, instead of writing sluggish Python loops.
- **Further up are the specialized libraries**: SciPy (scientific functions), scikit-learn (classical [machine learning](../ml/)), PyTorch ([deep learning](../dl/), [GPU](../gpu/) acceleration), Matplotlib (plotting).

The key is that they **share the same data representation** (the array), so they fit together seamlessly: a Pandas column is a NumPy array, and PyTorch tensors convert to and from NumPy. **Master the bottom layer and the whole stack opens up.**

## Key points

| Layer | Tool | What it does |
|---|---|---|
| Array core | [NumPy](../numpy/) | Multidimensional arrays, vectorized math, broadcasting |
| Tables/time series | [Pandas](../pandas/) | Reading, alignment, resampling, missing values |
| Scientific functions | SciPy | [Optimization](../optimization/), signal processing, statistics, FFT |
| Classical ML | scikit-learn | Regression, [clustering](../clustering/), preprocessing, evaluation |
| Deep learning | PyTorch | Tensors, automatic differentiation, GPU training |
| Visualization | Matplotlib | Plotting curves, distributions, heatmaps |

The methodology running through it all: **vectorize first, share the array representation, and drop down to the GPU when needed.**

## An example

A small pipeline from raw data to a plot, with several libraries passing the baton seamlessly:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pandas: load a time-indexed series and fill in missing values
idx = pd.date_range("2026-01-01", periods=100, freq="D")
s = pd.Series(np.random.randn(100).cumsum(), index=idx)  # NumPy generates the data
s = s.interpolate()

# Pandas + vectorization: smooth with a rolling mean
trend = s.rolling(7, min_periods=1).mean()

# Convert to NumPy for some numerical work
residual = s.to_numpy() - trend.to_numpy()
print(f"Residual standard deviation = {residual.std():.3f}")

# Plot with Matplotlib
plt.plot(s.index, s, label="Original")
plt.plot(s.index, trend, label="7-day moving average")
plt.legend(); plt.title("Trend decomposition")
# plt.show()
```

Notice how the data **flows freely** between Pandas, NumPy and Matplotlib with almost no manual conversion — this is exactly the value of a unified stack.

## Relevance to time series forecasting

When building forecasting models such as **KUN / Kernel U-Net**, each part of the stack has its own job:

- **[Pandas](../pandas/)** reads multi-source data, aligns timestamps, resamples, and builds time features.
- **[NumPy](../numpy/)** handles [vectorized](../vectorization/) operations such as slicing sliding windows, normalization and FFT.
- **PyTorch** builds the model, performs automatic differentiation and trains on the [GPU](../gpu/).
- **Matplotlib** plots the forecast curves and errors so you can see how well it works.

Switching fluently between these tools is the core engineering skill for taking a time series idea **from data to results**.

## Summary

- The scientific computing stack = the Python numerical toolchain centered on [NumPy](../numpy/) + [Pandas](../pandas/) + [vectorization](../vectorization/).
- The libraries **share the array representation** and fit together seamlessly, so mastering the bottom layer means mastering the whole.
- Methodology: **vectorize first**, and drop down to the [GPU](../gpu/) when the computation is heavy.
- It is the engineering vehicle that turns time series forecasting from "formulas" into "runnable experiments".

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
