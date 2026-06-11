---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/backpropagation/
title: "反向传播"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**反向传播（backpropagation）**是高效计算损失函数对网络中**每一个权重的梯度**的算法。它本质上是**链式法则**在多层网络上的系统化应用：误差从输出层"倒着"一层层传回去，沿途告诉每个参数"你应该往哪个方向、调多少"。

## 直观理解

[前向传播](../forward-propagation/)算出预测后，我们会得到一个误差（损失）。问题是：网络里成千上万个权重，**到底是谁的错、错了多少**？

想象一条流水线生产出了次品。我们从成品端往回追责：先看最后一道工序对误差贡献多大，再看它怎么受上一道工序影响……一路把"责任"按比例分摊回每个工位。反向传播就是这套**自动追责系统**——它给每个权重算出一个梯度，表示"这个权重稍微变大一点，损失会怎么变"。

关键洞察：**直接对每个权重单独求导太慢**（参数量是百万级）。反向传播聪明地**复用中间结果**，从后往前一次扫描就把所有梯度都算出来，代价仅相当于多做一次前向传播。

## 链式法则：跨层推导

设损失为 $\mathcal{L}$。我们要的是 $\dfrac{\partial \mathcal{L}}{\partial W^{(l)}}$ 和 $\dfrac{\partial \mathcal{L}}{\partial b^{(l)}}$。回忆前向公式 $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$，$a^{(l)} = \sigma(z^{(l)})$。

定义每层的**误差项（error）** $\delta^{(l)} = \dfrac{\partial \mathcal{L}}{\partial z^{(l)}}$，它表示"该层激活前的值变化对损失的影响"。

**输出层**（第 $L$ 层）：

$$
\delta^{(L)} = \frac{\partial \mathcal{L}}{\partial a^{(L)}} \odot \sigma'\big(z^{(L)}\big)
$$

**向前一层层递推**（这是反向传播的核心递推式）：

$$
\delta^{(l)} = \big( W^{(l+1)\top}\, \delta^{(l+1)} \big) \odot \sigma'\big(z^{(l)}\big)
$$

有了每层的 $\delta^{(l)}$，梯度就很简单：

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}} = \delta^{(l)}\, a^{(l-1)\top},
\qquad
\frac{\partial \mathcal{L}}{\partial b^{(l)}} = \delta^{(l)}
$$

符号解释：

- $\delta^{(l)}$：第 $l$ 层的误差信号（与该层神经元数同维）。
- $W^{(l+1)\top}$：下一层权重矩阵的**转置**——它把误差从第 $l+1$ 层"映射回"第 $l$ 层。
- $\odot$：**逐元素相乘**（Hadamard 积）。
- $\sigma'(z^{(l)})$：[激活函数](../activation-function/)在该层的**导数**，决定信号能否顺畅传回。
- $a^{(l-1)}$：来自前向传播保存的上一层激活值。

注意那个 $\sigma'(z^{(l)})$ 连乘项——它正是[梯度消失 / 爆炸](../vanishing-exploding-gradient/)的根源：层数越多，越多个导数被乘在一起。

## 一个具体例子

考虑最简单的两层链：$z_1 = w_1 x$，$a_1 = \sigma(z_1)$，$z_2 = w_2 a_1$，$\hat y = z_2$，损失 $\mathcal{L} = \tfrac12 (\hat y - y)^2$。设 $\sigma$ 为 Sigmoid。

从后往前算：

$$
\frac{\partial \mathcal{L}}{\partial \hat y} = \hat y - y
\;\Rightarrow\;
\delta_2 = \hat y - y
$$

$$
\frac{\partial \mathcal{L}}{\partial w_2} = \delta_2 \cdot a_1
$$

往回传一层：

$$
\delta_1 = (w_2 \cdot \delta_2)\cdot \sigma'(z_1),
\qquad
\frac{\partial \mathcal{L}}{\partial w_1} = \delta_1 \cdot x
$$

代入数字：$x=1,\, w_1=0.5,\, w_2=2,\, y=1$。前向：$z_1=0.5$，$a_1=\sigma(0.5)\approx0.622$，$\hat y = 2\times0.622=1.244$。

反向：$\delta_2 = 1.244-1 = 0.244$；$\partial\mathcal{L}/\partial w_2 = 0.244\times0.622 \approx 0.152$。
Sigmoid 导数 $\sigma'(z_1)=a_1(1-a_1)=0.622\times0.378\approx0.235$。
$\delta_1 = 2\times0.244\times0.235 \approx 0.115$；$\partial\mathcal{L}/\partial w_1 = 0.115\times1 = 0.115$。

```python
import numpy as np
sig = lambda z: 1/(1+np.exp(-z))
x, w1, w2, y = 1.0, 0.5, 2.0, 1.0
z1 = w1*x; a1 = sig(z1); yhat = w2*a1          # 前向
d2 = yhat - y                                   # 输出误差
gw2 = d2*a1
d1 = w2*d2*(a1*(1-a1))                           # 传回一层
gw1 = d1*x
print(round(gw1,3), round(gw2,3))               # 0.115 0.152
```

## 为什么重要 / 用在哪

- **没有反向传播就没有现代深度学习**。它让训练百万参数的网络在计算上变得可行。
- 它产出的梯度交给[优化器](../optimizer/)（如 [Adam](../adam/)），按[学习率](../learning-rate/)更新权重：$W \leftarrow W - \eta\, \partial\mathcal{L}/\partial W$。
- 现实中你几乎不必手写它——[自动微分](../autodiff/)框架会自动完成。但理解它的递推式，才能诊断训练不收敛、梯度爆炸等问题。

## 常见误区

- **"反向传播 = 梯度下降"**——不是。反向传播只负责**算梯度**；怎么用梯度更新参数是[优化器](../optimizer/)的事。
- **"它学习参数"**——它不更新参数，只提供方向信息。
- **"它和前向传播无关"**——恰恰相反，它**重度依赖**前向传播保存的中间值 $a^{(l)}, z^{(l)}$。

[← 深度学习基础](../dl/) · [基础课总览](../)
