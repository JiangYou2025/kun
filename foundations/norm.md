---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/norm/
title: "范数"
no_comments: true
math: true
---

> 出自[数学基础](../math/) · [基础课总览](../)

范数是衡量向量"**长度 / 大小**"的函数。同一个向量，用不同范数量出来的"长度"不同；机器学习里最常用 $\ell_1$ 与 $\ell_2$，它们也是[正则化](../regularization/)、距离度量的核心工具。

## 直观理解

"从家到公司有多远"取决于你怎么走：

- 直线飞过去（$\ell_2$，欧氏距离）；
- 沿着横平竖直的街道走（$\ell_1$，曼哈顿 / 出租车距离）；
- 只关心走得最远的那一个方向（$\ell_\infty$）。

范数就是把"大小 / 距离"这个朴素概念形式化，并允许有多种合理的度量方式。它还衡量"一个向量稀不稀疏、有多极端"，这正是正则化要利用的。

## 数学表达

对向量 $\mathbf{x}=(x_1,\dots,x_n)$：

**$\ell_2$ 范数（欧氏长度）**

$$
\lVert\mathbf{x}\rVert_2=\sqrt{\sum_i x_i^2}
$$

**$\ell_1$ 范数（绝对值之和）**

$$
\lVert\mathbf{x}\rVert_1=\sum_i |x_i|
$$

**$\ell_\infty$ 范数（最大绝对值）**

$$
\lVert\mathbf{x}\rVert_\infty=\max_i |x_i|
$$

它们都是更一般的 **$\ell_p$ 范数** 的特例：

$$
\lVert\mathbf{x}\rVert_p=\Big(\sum_i |x_i|^p\Big)^{1/p}
$$

任何范数都满足三条公理：非负（且仅零向量为 0）、绝对齐次 $\lVert c\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$、三角不等式 $\lVert\mathbf{x}+\mathbf{y}\rVert\le\lVert\mathbf{x}\rVert+\lVert\mathbf{y}\rVert$。

## 一个具体例子

取 $\mathbf{x}=(3,-4)$：

$$
\lVert\mathbf{x}\rVert_2=\sqrt{3^2+(-4)^2}=\sqrt{25}=5
$$
$$
\lVert\mathbf{x}\rVert_1=|3|+|-4|=7,\qquad \lVert\mathbf{x}\rVert_\infty=\max(3,4)=4
$$

同一个向量，三种"长度"各不相同。

```python
import numpy as np
x = np.array([3, -4])
print(np.linalg.norm(x, 2))     # 5.0
print(np.linalg.norm(x, 1))     # 7.0
print(np.linalg.norm(x, np.inf))# 4.0
```

## 为什么重要 / 用在哪

- **正则化**：在损失里加范数惩罚来限制模型复杂度、抑制[过拟合](../overfitting/)。
  - **L2 正则（岭回归 / weight decay）**：加 $\lambda\lVert\mathbf{w}\rVert_2^2$，让权重整体变小、更平滑。
  - **L1 正则（Lasso）**：加 $\lambda\lVert\mathbf{w}\rVert_1$，会把一些权重精确压到 0，得到**稀疏**模型，可做特征选择。
- **距离与相似度**：KNN、[聚类](../clustering/)用 $\ell_2$ 距离；误差度量 MSE 是 $\ell_2$、MAE 是 $\ell_1$。
- **梯度裁剪**：按梯度的 $\ell_2$ 范数缩放，防止[梯度](../gradient/)爆炸。

## 在时间序列预测中的意义

- 预测误差的度量本身就是范数：**MSE/RMSE = $\ell_2$**（对大误差敏感），**MAE = $\ell_1$**（对异常值更稳健）。选哪个取决于你更怕大错还是更怕被离群点带偏。
- 训练 KUN（Kernel U-Net）时加 weight decay（L2）有助于在长序列上稳住[泛化](../generalization/)；需要稀疏、可解释的特征时可考虑 L1。

## 常见误区

- **L1 vs L2 的几何直觉**：L1 的"菱形"约束边界有尖角，容易在坐标轴上取到最优 → 产生稀疏解；L2 的"圆形"边界则让权重平滑收缩但一般不为 0。
- $\ell_2$ 范数与它的平方常被混用：损失里多用**平方** $\lVert\cdot\rVert_2^2$（可导且无根号，便于求导）。
- 范数永远非负，且只有零向量范数为 0。

[← 数学基础](../math/) · [基础课总览](../)
