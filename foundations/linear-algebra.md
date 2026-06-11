---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/linear-algebra/
title: "线性代数"
no_comments: true
math: true
---

> 出自[数学基础](../math/) · [基础课总览](../)

线性代数研究**向量、矩阵与线性变换**。神经网络的每一层运算、几乎所有降维与表示方法，都建立在它之上——可以说它是[机器学习](../ml/)的"母语"。

## 直观理解

把数据想成**空间中的点（向量）**：一张图片是几万维空间里的一个点，一段时间序列是一串数构成的向量。**矩阵**则是"作用在这些点上的操作"——它能旋转、拉伸、压缩、投影整个空间。

所以"训练模型"在几何上常常意味着：**寻找一组合适的线性变换（矩阵）**，把杂乱的数据点搬到一个更容易区分、更容易预测的新空间里。线性代数就是描述这些点和操作的语言。

## 数学表达

**向量** $\mathbf{x}\in\mathbb{R}^n$ 是 $n$ 个数的有序列表，可看作空间中的箭头。

**矩阵** $A\in\mathbb{R}^{m\times n}$ 是 $m$ 行 $n$ 列的数表，代表一个从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的**线性变换**。

核心运算——**矩阵–向量乘法**：

$$
\mathbf{y}=A\mathbf{x},\qquad y_i=\sum_{j} A_{ij}\,x_j
$$

把输入向量 $\mathbf{x}$ 变换成输出向量 $\mathbf{y}$（详见[矩阵乘法](../matrix-multiplication/)）。

几个反复出现的概念：

- **点积** $\mathbf{a}\cdot\mathbf{b}=\sum_i a_i b_i$，衡量两向量的相似 / 投影；
- **[范数](../norm/)** $\lVert\mathbf{x}\rVert$，向量的长度；
- **线性无关 / 秩（rank）**：一组向量能"撑起"几维空间；
- **特征值与特征向量** $A\mathbf{v}=\lambda\mathbf{v}$：变换中方向不变、只被缩放 $\lambda$ 倍的特殊方向；
- **[SVD](../svd/)**：任意矩阵都能分解为"旋转—缩放—旋转"。

## 一个具体例子

一个全连接层 $\mathbf{y}=W\mathbf{x}+\mathbf{b}$。设输入 2 维、输出 2 维：

$$
W=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad \mathbf{x}=\begin{pmatrix}3\\4\end{pmatrix}
\ \Rightarrow\
W\mathbf{x}=\begin{pmatrix}1\cdot3+0\cdot4\\0\cdot3+2\cdot4\end{pmatrix}=\begin{pmatrix}3\\8\end{pmatrix}
$$

这个 $W$ 把空间在 $y$ 方向拉伸 2 倍、$x$ 方向不变。

```python
import numpy as np
W = np.array([[1, 0], [0, 2]])
x = np.array([3, 4])
print(W @ x)   # [3 8]
```

## 为什么重要 / 用在哪

- **每一层[神经网络](../neural-network/)**本质都是矩阵乘法 + 非线性，[注意力机制](../attention/)是 $QK^\top V$ 的矩阵运算。
- **降维与压缩**：[PCA](../pca/)、[SVD](../svd/)、嵌入（embedding）都靠线性代数。
- **[GPU](../gpu/) 加速**：硬件就是为大规模矩阵乘法优化的，这是深度学习能跑起来的物理前提。

## 在时间序列预测中的意义

- 把历史窗口排成向量 / 矩阵后，KUN（Kernel U-Net）的卷积、核映射、上下采样在底层全是矩阵运算。
- 多变量时间序列天然是矩阵（时间 × 变量），变量间的相关结构可用协方差矩阵、低秩分解来分析。
- 高效的批量预测依赖把许多序列堆叠成大矩阵一次性计算。

## 小结

- 向量 = 空间中的点，矩阵 = 作用其上的线性变换。
- 矩阵乘法、范数、秩、特征值/SVD 是核心工具。
- 它是神经网络前向计算、降维与 GPU 加速的共同基础。

[← 数学基础](../math/) · [基础课总览](../)
