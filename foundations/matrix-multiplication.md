---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/matrix-multiplication/
title: "矩阵乘法"
no_comments: true
math: true
---

> 出自[数学基础](../math/) · [基础课总览](../)

矩阵乘法是[线性代数](../linear-algebra/)最核心的运算：它把一组向量做**线性变换**，也是把多个线性变换**串联**成一个的方式。神经网络的每一层、注意力机制，底层都是矩阵乘法。

## 直观理解

可以从两个角度理解 $C=AB$：

- **变换的复合**：如果 $B$ 是"先做一个变换"、$A$ 是"再做一个变换"，那么 $AB$ 就是"一口气完成这两个变换"的单个矩阵。先 $B$ 后 $A$，顺序不能反——这就是它**不可交换**的根源。
- **行点积列**：结果矩阵第 $i$ 行第 $j$ 列的元素，是 $A$ 的第 $i$ **行**和 $B$ 的第 $j$ **列**做点积。"行碰列"是手算的口诀。

## 数学表达

设 $A\in\mathbb{R}^{m\times k}$，$B\in\mathbb{R}^{k\times n}$，则积 $C=AB\in\mathbb{R}^{m\times n}$：

$$
C_{ij}=\sum_{l=1}^{k} A_{il}\,B_{lj}
$$

**形状规则**（最常踩的坑）：$A$ 的**列数**必须等于 $B$ 的**行数**（都是 $k$），结果形状是"$A$ 的行 × $B$ 的列"：

$$
(m\times k)\cdot(k\times n)=(m\times n)
$$

重要性质：

- **不满足交换律**：一般 $AB\ne BA$；
- 满足结合律 $A(BC)=(AB)C$ 与分配律；
- $(AB)^\top=B^\top A^\top$（转置后顺序反过来）。

## 一个具体例子

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad
B=\begin{pmatrix}5&6\\7&8\end{pmatrix}
$$

$$
C_{11}=1\cdot5+2\cdot7=19,\quad C_{12}=1\cdot6+2\cdot8=22
$$
$$
C_{21}=3\cdot5+4\cdot7=43,\quad C_{22}=3\cdot6+4\cdot8=50
$$

$$
AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}
$$

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)        # [[19 22] [43 50]]
print(B @ A)        # [[23 34] [31 46]]  ≠ A@B，验证不可交换
```

## 为什么重要 / 用在哪

- **神经网络前向计算**：每个全连接层就是 $\mathbf{y}=W\mathbf{x}+\mathbf{b}$，一次矩阵–向量乘法。
- **注意力机制**：$\text{softmax}(QK^\top/\sqrt{d})\,V$，连续多次矩阵乘法。
- **批处理**：把一批样本堆成矩阵，一次乘法同时处理所有样本——这是 GPU 高效的关键。计算量约为 $O(mkn)$，所以模型规模直接决定算力需求。

## 在时间序列预测中的意义

- KUN（Kernel U-Net）的卷积、核投影、线性层，落到硬件上全是矩阵乘法；预测延迟与显存占用很大程度由这些乘法的规模决定。
- 多变量序列（时间 × 变量）的变换、多个序列的批量预测，都是把数据排成矩阵后一次性相乘完成。

## 常见误区

- **维度对不上**最常见：务必检查"内维相等"（$A$ 列 = $B$ 行）。
- 别把矩阵乘法和**逐元素乘法**（Hadamard，`*` 或 `np.multiply`）搞混，二者完全不同。
- 顺序敏感：$AB\ne BA$，转置时记得 $(AB)^\top=B^\top A^\top$。

[← 数学基础](../math/) · [基础课总览](../)
