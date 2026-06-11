---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/pandas/
title: "Pandas"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**Pandas** 是 [Python](../python/) 处理**表格数据**的主力库。它的核心是 `DataFrame`（带行列标签的二维表）和 `Series`（带索引的一维序列）。对时间序列来说，它最擅长**按时间索引**做对齐、重采样和缺失值处理。

## 直观理解

可以把 `DataFrame` 想成「会编程的 Excel 表」：

- 每一列是一个 `Series`，底层是一个 [NumPy](../numpy/) 数组，所以运算又快又支持[向量化](../vectorization/)。
- 每一行/列都有**标签（索引）**。这是 Pandas 比裸 NumPy 更强的地方——它能**按标签自动对齐**。比如把两条起止时间不同的序列相加，Pandas 会自动按时间戳对齐，对不上的位置填 `NaN`，而不是傻乎乎地按位置硬加。

对时间序列，把时间戳设成索引后，「取某一周的数据」「按月汇总」「填补缺失的小时」都变成一两行代码。

## 核心要点

- **DataFrame / Series**：带标签的表格 / 序列。
- **DatetimeIndex**：以时间戳为索引，解锁全部时序功能。
- **选择数据**：`df["col"]` 取列，`df.loc[标签]` 按标签选，`df.iloc[位置]` 按位置选。
- **重采样 `resample`**：改变时间频率，如把分钟数据聚合成小时（降采样）或插值成更细（升采样）。
- **滚动窗口 `rolling`**：移动平均、滚动标准差等。
- **缺失值**：`isna` / `fillna` / `interpolate` / `dropna`。
- **分组聚合 `groupby`**：按类别分组再统计。

## 一个例子

一段典型的时序预处理：

```python
import pandas as pd
import numpy as np

# 构造一条每小时的序列，故意缺几个点
idx = pd.date_range("2026-01-01", periods=8, freq="h")
s = pd.Series([10, 11, np.nan, 13, 14, np.nan, 16, 17], index=idx)

# 1) 线性插值补缺
s = s.interpolate()

# 2) 滚动平均（窗口=3）平滑噪声
s_smooth = s.rolling(window=3, min_periods=1).mean()

# 3) 重采样：每小时 → 每天求和
daily = s.resample("D").sum()

print(s_smooth.round(2))
print(daily)
```

`interpolate()` 之所以能正确插值，正是因为索引是时间——Pandas 知道点与点之间隔多久。

时间对齐的魔力：

```python
a = pd.Series([1, 2, 3], index=pd.date_range("2026-01-01", periods=3))
b = pd.Series([10, 20], index=pd.date_range("2026-01-02", periods=2))
print(a + b)
# 2026-01-01     NaN   ← b 没有这天
# 2026-01-02    12.0   ← 2 + 10，自动按日期对齐
# 2026-01-03    23.0   ← 3 + 20
```

## 在时间序列预测中的意义

喂给 **KUN / Kernel U-Net** 的数据，几乎都要先过一遍 Pandas：

- **对齐多条序列**：不同传感器、不同股票的采样时间不一致，靠时间索引自动对齐成一张整齐的表。
- **重采样到统一频率**：模型通常要求等间隔输入，`resample` 把杂乱频率规整化。
- **构造时间特征**：从 `DatetimeIndex` 一行提取小时、星期、是否节假日等，作为额外特征。
- **划分训练/测试**：用 `df.loc["2020":"2023"]` 这样**按时间**切分，避免随机打乱导致未来信息泄漏。
- **处理完后转 NumPy**：`df.values` 或 `.to_numpy()` 交给模型张量化。

## 常见误区

- **不设时间索引就用时序功能**：`resample` / `rolling` 的时间语义依赖 `DatetimeIndex`。
- **链式赋值踩 `SettingWithCopyWarning`**：修改子集要用 `df.loc[...] = ...`，别 `df[...][...] = ...`。
- **在大表上逐行 `apply`/循环**：慢。优先用向量化的列运算或 `groupby`。
- **时序切分用了 shuffle**：训练/测试必须按时间先后切，乱序会让模型「偷看未来」。

---

[← 计算机基础](../cs/) · [基础课总览](../)
