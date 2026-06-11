---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/scientific-computing/
title: "科学计算栈"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**科学计算栈**指的是 Python 里做数值计算与数据分析的一套配合默契的工具链——以 [NumPy](../numpy/)（数组运算）、[Pandas](../pandas/)（表格/时序处理）和[向量化](../vectorization/)（用整块运算代替循环）为核心，往上还有 Matplotlib、SciPy、scikit-learn、PyTorch 等。

## 直观理解

这套工具栈像一个层层搭建的工厂流水线：

- **最底层是 [NumPy](../numpy/)**：紧凑、高速的多维数组，所有数值计算的「地基」。
- **往上是 [Pandas](../pandas/)**：给数组加上行列标签和时间索引，方便读数据、对齐、清洗。
- **[向量化](../vectorization/)是贯穿全栈的方法论**：用 `a + b` 这样的整体运算，让底层 C 代码一次算完，而不是写慢吞吞的 Python 循环。
- **再往上是专用库**：SciPy（科学函数）、scikit-learn（经典机器学习）、PyTorch（深度学习、[GPU](../gpu/) 加速）、Matplotlib（画图）。

关键在于它们**共享同一种数据表示**（数组），所以能无缝衔接：Pandas 的列就是 NumPy 数组，PyTorch 张量能和 NumPy 互转。**学会底层，整条栈都通了。**

## 核心要点

| 层 | 工具 | 干什么 |
|---|---|---|
| 数组核心 | [NumPy](../numpy/) | 多维数组、向量化数学、广播 |
| 表格/时序 | [Pandas](../pandas/) | 读取、对齐、重采样、缺失值 |
| 科学函数 | SciPy | 优化、信号、统计、FFT |
| 经典 ML | scikit-learn | 回归、聚类、预处理、评估 |
| 深度学习 | PyTorch | 张量、自动求导、GPU 训练 |
| 可视化 | Matplotlib | 画曲线、分布、热力图 |

贯穿其中的方法论是：**向量化优先、共享数组表示、必要时下沉到 GPU。**

## 一个例子

一条从原始数据到画图的小流水线，几个库无缝接力：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pandas：读入并补缺一条带时间索引的序列
idx = pd.date_range("2026-01-01", periods=100, freq="D")
s = pd.Series(np.random.randn(100).cumsum(), index=idx)  # NumPy 造数据
s = s.interpolate()

# Pandas + 向量化：滚动平均平滑
trend = s.rolling(7, min_periods=1).mean()

# 转成 NumPy 做点数值运算
residual = s.to_numpy() - trend.to_numpy()
print(f"残差标准差 = {residual.std():.3f}")

# Matplotlib 画图
plt.plot(s.index, s, label="原始")
plt.plot(s.index, trend, label="7日均线")
plt.legend(); plt.title("趋势分解")
# plt.show()
```

注意数据在 Pandas、NumPy、Matplotlib 之间**自由流动**，几乎不用手动转换——这正是统一栈的价值。

## 在时间序列预测中的意义

做 **KUN / Kernel U-Net** 这类预测，整条栈各司其职：

- **[Pandas](../pandas/)** 负责读多源数据、对齐时间、重采样、构造时间特征。
- **[NumPy](../numpy/)** 负责切滑动窗口、归一化、FFT 等[向量化](../vectorization/)运算。
- **PyTorch** 负责搭模型、自动求导、在 [GPU](../gpu/) 上训练。
- **Matplotlib** 负责把预测曲线、误差画出来看效果。

熟练在这几者间切换，是把一个时序想法**从数据走到结果**的核心工程能力。

## 小结

- 科学计算栈 = 以 [NumPy](../numpy/) + [Pandas](../pandas/) + [向量化](../vectorization/)为核心的 Python 数值工具链。
- 各库**共享数组表示**，能无缝衔接，所以掌握底层就掌握全局。
- 方法论：**向量化优先**，计算密集时下沉到 [GPU](../gpu/)。
- 它是把时序预测从「公式」落到「可运行实验」的工程载体。

---

[← 计算机基础](../cs/) · [基础课总览](../)
