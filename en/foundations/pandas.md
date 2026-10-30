---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/pandas/
title: "Pandas"
no_comments: true
---

> Part of [Computer science foundations](../cs/) · [Foundations overview](../)

**Pandas** is [Python](../python/)'s workhorse library for **tabular data**. Its core is the `DataFrame` (a two-dimensional table with row and column labels) and the `Series` (a one-dimensional sequence with an index). For time series, its greatest strength is aligning, resampling and handling missing values **by time index**.

## Intuition

You can think of a `DataFrame` as "a programmable Excel sheet":

- Each column is a `Series` backed by a [NumPy](../numpy/) array, so operations are fast and [vectorized](../vectorization/).
- Every row and column has a **label (index)**. This is where Pandas beats bare NumPy — it **aligns automatically by label**. For example, if you add two series with different start and end times, Pandas aligns them by timestamp and fills unmatched positions with `NaN`, instead of naively adding them position by position.

For time series, once the timestamps are set as the index, "take one week of data", "aggregate by month" and "fill in missing hours" each become one or two lines of code.

## Key points

- **DataFrame / Series**: labelled tables / sequences.
- **DatetimeIndex**: an index of timestamps, which unlocks all the time series features.
- **Selecting data**: `df["col"]` takes a column, `df.loc[label]` selects by label, `df.iloc[position]` selects by position.
- **Resampling with `resample`**: changing the time frequency, e.g. aggregating minute data into hours (downsampling) or interpolating to a finer grid (upsampling).
- **Rolling windows with `rolling`**: moving averages, rolling standard deviations, and so on.
- **Missing values**: `isna` / `fillna` / `interpolate` / `dropna`.
- **Group-and-aggregate with `groupby`**: group by category, then compute statistics.

## An example

A typical piece of time series preprocessing:

```python
import pandas as pd
import numpy as np

# Build an hourly series with a few points deliberately missing
idx = pd.date_range("2026-01-01", periods=8, freq="h")
s = pd.Series([10, 11, np.nan, 13, 14, np.nan, 16, 17], index=idx)

# 1) Fill the gaps by linear interpolation
s = s.interpolate()

# 2) Rolling mean (window=3) to smooth the noise
s_smooth = s.rolling(window=3, min_periods=1).mean()

# 3) Resample: hourly → daily sums
daily = s.resample("D").sum()

print(s_smooth.round(2))
print(daily)
```

`interpolate()` interpolates correctly precisely because the index is time — Pandas knows how far apart the points are.

The magic of time alignment:

```python
a = pd.Series([1, 2, 3], index=pd.date_range("2026-01-01", periods=3))
b = pd.Series([10, 20], index=pd.date_range("2026-01-02", periods=2))
print(a + b)
# 2026-01-01     NaN   ← b has no value for this day
# 2026-01-02    12.0   ← 2 + 10, aligned automatically by date
# 2026-01-03    23.0   ← 3 + 20
```

## Relevance to time series forecasting

Almost all the data fed to **KUN / Kernel U-Net** passes through Pandas first:

- **Aligning several series**: different sensors or different stocks are sampled at different times; the time index aligns them automatically into one tidy table.
- **Resampling to a common frequency**: models usually need evenly spaced inputs, and `resample` regularizes messy frequencies.
- **Building time features**: extract the hour, day of week, holiday flag and so on from a `DatetimeIndex` in one line, as extra features.
- **Train/test splitting**: split **by time** with something like `df.loc["2020":"2023"]`, to avoid leaking future information through random shuffling.
- **Converting to NumPy when done**: `df.values` or `.to_numpy()` hands the data to the model as tensors.

## Common pitfalls

- **Using time series features without a time index**: the time semantics of `resample` / `rolling` depend on a `DatetimeIndex`.
- **Chained assignment triggering `SettingWithCopyWarning`**: modify a subset with `df.loc[...] = ...`, not `df[...][...] = ...`.
- **Row-by-row `apply` / loops on large tables**: slow. Prefer vectorized column operations or `groupby`.
- **Shuffling when splitting a time series**: training and test sets must be split in chronological order; shuffling lets the model "peek at the future".

---

[← Computer science foundations](../cs/) · [Foundations overview](../)
