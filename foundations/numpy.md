---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/numpy/
title: "NumPy"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**NumPy** 是 [Python](../python/) 数值计算的基石。它提供了一个高效的多维数组类型 `ndarray`，以及一整套在整块数组上做[向量化](../vectorization/)运算的函数。几乎所有科学计算和[机器学习](../ml/)库（Pandas、scikit-learn、PyTorch）都建立在它之上。

## 直观理解

Python 自带的 `list` 很灵活，但慢：它的每个元素都是一个独立的 Python 对象，散落在内存各处，运算时还要逐个解释执行。

NumPy 的 `ndarray` 不一样——它把**同一种类型的数字紧凑地排在连续内存里**，运算交给底层用 C 写的循环一次性完成。结果就是：**同样一个计算，NumPy 往往比纯 Python 快几十到上百倍**，代码还更短。

一句话：**NumPy 让你像写数学公式一样写代码，把循环交给底层去跑。**

## 核心要点

- **ndarray**：N 维数组，有 `shape`（形状）、`dtype`（元素类型）两个核心属性。
- **[向量化](../vectorization/)**：`a + b`、`a * 2`、`np.sqrt(a)` 直接作用于整个数组，无需写循环。
- **广播（broadcasting）**：形状不同但兼容的数组能自动对齐运算，例如「矩阵每一行都减去同一个向量」。
- **切片与索引**：`a[1:5]`、`a[:, 0]`、`a[a > 0]`（布尔索引）灵活又高效，且多为**视图**（不复制数据）。
- **轴（axis）**：聚合时指定方向，`a.mean(axis=0)` 按列平均，`axis=1` 按行平均。

## 一个例子

感受向量化的威力——给一万个数都加上平方：

```python
import numpy as np

a = np.arange(1_000_000, dtype=float)

# NumPy 方式：一行，底层 C 循环
b = a ** 2 + 1          # 整个数组一次算完

# 等价的纯 Python：慢得多
# b = [x**2 + 1 for x in a]
```

广播让「按列标准化」非常优雅：

```python
X = np.random.randn(1000, 5)          # 1000 个样本，5 个特征
mean = X.mean(axis=0)                  # 形状 (5,)，每列均值
std  = X.std(axis=0)                   # 形状 (5,)
X_norm = (X - mean) / std              # (1000,5) 自动减去/除以 (5,)
print(X_norm.mean(axis=0).round(6))    # 每列均值约 0
print(X_norm.std(axis=0).round(6))     # 每列标准差约 1
```

`(1000, 5)` 的矩阵和 `(5,)` 的向量能直接运算，就是**广播**：向量被自动「复制」到每一行——但其实并不真的复制，省内存又省时间。

## 在时间序列预测中的意义

NumPy 是时序数据处理的底层引擎：

- **滑动窗口**：把长序列切成「过去 L 步 → 未来 H 步」的训练样本，可以用 `np.lib.stride_tricks.sliding_window_view` 零拷贝生成所有窗口，比 Python 循环快几个数量级。

  ```python
  series = np.arange(10)
  windows = np.lib.stride_tricks.sliding_window_view(series, 3)
  # 形状 (8, 3)，每行是一个长度 3 的窗口，无额外内存拷贝
  ```

- **批量数学**：差分、归一化、滚动统计、FFT 频谱，全是数组级运算。
- **承上启下**：[Pandas](../pandas/) 的列底层就是 NumPy 数组；喂给 **KUN / Kernel U-Net** 的张量也由 NumPy 数组转成。掌握 NumPy，整条[科学计算栈](../scientific-computing/)都通了。

## 常见误区

- **还在写 Python `for` 循环逐元素处理数组**：这放弃了 NumPy 的全部优势，应改用[向量化](../vectorization/)。
- **混淆视图与拷贝**：切片通常返回**视图**，改它会改原数组；要独立副本得显式 `.copy()`。
- **忽视 dtype**：整数数组做除法或溢出会出意外结果，必要时用 `astype(float)`。
- **形状不匹配**：广播规则要从**右往左**对齐维度，搞错就会报 `shape mismatch`。

---

[← 计算机基础](../cs/) · [基础课总览](../)
