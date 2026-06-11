---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/mlp/
title: "MLP（多层感知机）"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**MLP（Multi-Layer Perceptron，多层感知机）** 是最基础的[神经网络](../neural-network/)：若干层全连接（fully-connected）层堆叠，前一层的每个神经元都连到后一层的每个神经元，中间夹着[激活函数](../activation-function/)。它是几乎所有现代架构的"积木"。

## 直观理解

"全连接"的意思是：**不挑食**。每个神经元都看上一层的全部信息，自己决定哪些重要、哪些忽略（靠学到的权重）。

这和 [CNN](../cnn/) 的"只看局部窗口"、注意力的"按相关性挑重点"形成对比。MLP 不预设任何结构假设，是最朴素、最通用的形式：给它足够多的神经元，它理论上能逼近任意连续函数（**通用逼近定理**）。代价是参数多、不利用数据本身的结构（比如时间的先后、像素的相邻）。

## 数学表达

一个 $L$ 层 MLP 就是把"线性变换 + 激活"反复套娃。设输入为 $\mathbf{x}$，记 $\mathbf{h}^{(0)} = \mathbf{x}$，则第 $l$ 层为：

$$
\mathbf{h}^{(l)} = \sigma\!\left( \mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)} \right), \quad l = 1, \dots, L
$$

- $\mathbf{h}^{(l-1)} \in \mathbb{R}^{d_{l-1}}$：第 $l-1$ 层输出（维度 $d_{l-1}$）；
- $\mathbf{W}^{(l)} \in \mathbb{R}^{d_l \times d_{l-1}}$：权重矩阵，把 $d_{l-1}$ 维映射到 $d_l$ 维；
- $\mathbf{b}^{(l)} \in \mathbb{R}^{d_l}$：偏置向量；
- $\sigma$：激活函数，逐元素作用（隐藏层常用 ReLU $\sigma(z)=\max(0,z)$）；
- 输出层通常**不加激活**（回归任务），直接 $\hat{\mathbf{y}} = \mathbf{W}^{(L)}\mathbf{h}^{(L-1)} + \mathbf{b}^{(L)}$。

**参数量**：第 $l$ 层有 $d_l \times d_{l-1} + d_l$ 个参数。这也是 MLP 的软肋——维度一高，权重矩阵就爆炸。

## 一个具体例子

手算一个极小的 MLP：输入 2 维，隐藏层 2 个神经元（ReLU），输出 1 维。

设 $\mathbf{x} = \begin{bmatrix}1\\2\end{bmatrix}$，

$$
\mathbf{W}^{(1)} = \begin{bmatrix}1 & 0\\-1 & 1\end{bmatrix},\quad
\mathbf{b}^{(1)} = \begin{bmatrix}0\\0\end{bmatrix}
$$

第 1 层线性部分：$\mathbf{W}^{(1)}\mathbf{x} = \begin{bmatrix}1\cdot1 + 0\cdot2\\ -1\cdot1 + 1\cdot2\end{bmatrix} = \begin{bmatrix}1\\1\end{bmatrix}$。

过 ReLU：$\mathbf{h}^{(1)} = \begin{bmatrix}\max(0,1)\\\max(0,1)\end{bmatrix} = \begin{bmatrix}1\\1\end{bmatrix}$。

输出层 $\mathbf{W}^{(2)} = \begin{bmatrix}2 & 3\end{bmatrix}$，$b^{(2)}=1$：

$$
\hat{y} = 2\cdot1 + 3\cdot1 + 1 = 6
$$

代码版本：

```python
import torch.nn as nn

mlp = nn.Sequential(
    nn.Linear(2, 2),
    nn.ReLU(),
    nn.Linear(2, 1),
)
```

## 为什么重要 / 用在哪

- **通用逼近器**：理论上能拟合任意复杂的输入—输出关系。
- **万能组件**：Transformer 每个块里的"前馈网络"就是一个 MLP；CNN/U-Net 最后的预测头也常是 MLP。学会它就理解了无数模型的一部分。
- **强 baseline**：在时间序列预测里，把整段历史拉平喂给 MLP（如 DLinear、N-BEATS 这类）往往出乎意料地强，是必备对照组。

## 在时间序列预测中的意义

最简单的预测做法：把长度为 $L$ 的历史窗口当成一个 $L$ 维向量，用 MLP 直接映射到 $H$ 维的未来：

```python
forecaster = nn.Sequential(
    nn.Linear(96, 256), nn.ReLU(),
    nn.Linear(256, 24),     # 96 步历史 -> 24 步预测
)
```

这种"拍平 + 全连接"简单高效，但有两个局限：**忽略了时间的顺序结构**（打乱输入顺序结果不变），且窗口越长参数越多。本站主推的 **Kernel U-Net (KUN)** 正是用[多尺度](../u-net/)的方式缓解这两点——在不同时间分辨率上用轻量"核"处理，而每个核内部的变换，本质仍是小型 MLP。所以 MLP 既是基线，也是更高级架构的内部零件。

## 常见误区

- **"MLP 没有激活也行"**：错。没有激活，多层会塌缩成一层线性，再深也白搭。
- **"层数越多越好"**：太深的纯 MLP 容易遇到[梯度消失 / 爆炸](../vanishing-exploding-gradient/)、过拟合，常需 [Dropout](../dropout/)、[BatchNorm](../batchnorm/) 等辅助。
- **"MLP 理解时间顺序"**：不会。它把输入当作无序向量，时序结构得靠 CNN/RNN/注意力或人为设计来引入。

[← 深度学习基础](../dl/) · [基础课总览](../)
