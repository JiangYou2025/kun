---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/activation-function/
title: "激活函数"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**激活函数（activation function）**是作用在每个[神经元](../neuron/)加权和之后的**非线性函数**。它是[神经网络](../neural-network/)拥有"表达复杂关系"能力的关键——**没有它，再深的网络也只等价于一层线性变换**。

## 为什么必须非线性

回忆[前向传播](../forward-propagation/)：每层做 $z = Wa + b$。如果不加激活函数，把多层叠起来：

$$
W_2(W_1 x + b_1) + b_2 = (W_2 W_1)\,x + (W_2 b_1 + b_2)
$$

无论叠多少层，结果**仍是 $x$ 的线性函数**！深度完全白费。激活函数 $\sigma$ 在每层引入一道"弯折"，让网络能逼近**任意复杂的非线性关系**（这就是通用逼近定理的直觉）。

## 三个经典激活函数

**Sigmoid**：把输入压到 $(0,1)$。

$$
\sigma(x) = \frac{1}{1+e^{-x}},\qquad
\sigma'(x) = \sigma(x)\big(1-\sigma(x)\big)
$$

导数最大值在 $x=0$ 处仅为 $0.25$，且两端趋近 0。这意味着误差信号每经过一层 Sigmoid 至少要乘上 $\le0.25$ 的因子——深层网络里连乘后迅速趋于 0，造成[梯度消失](../vanishing-exploding-gradient/)。如今多用于二分类的输出层，少用于隐藏层。

**Tanh**：把输入压到 $(-1,1)$，是 Sigmoid 的"零中心"版。

$$
\tanh(x) = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}},\qquad
\tanh'(x) = 1 - \tanh^2(x)
$$

零中心（输出有正有负）让训练比 Sigmoid 略好，导数最大值为 1（在 $x=0$）。但两端依旧饱和，深层仍会梯度消失。常见于 [RNN](../rnn/)/[LSTM](../lstm/)。

**ReLU**：最常用的隐藏层激活，简单粗暴。

$$
\mathrm{ReLU}(x) = \max(0, x),\qquad
\mathrm{ReLU}'(x) = \begin{cases}1 & x>0\\ 0 & x<0\end{cases}
$$

**为什么 ReLU 能缓解梯度消失**：在正区间导数**恒为 1**，误差信号反向传播时不会被反复缩小——连乘 1 还是 1。这让很深的网络也能训练。代价是负区间导数为 0，神经元可能"死亡"（永远输出 0）。改进版 **Leaky ReLU**（$x<0$ 时给一个小斜率 $0.01x$）缓解了这个问题。

## 一个具体例子

设某神经元加权和 $z = -0.5$，比较三种激活的输出与"梯度能传回多少"（即导数）：

| 激活 | 输出 | 导数（该点的梯度因子） |
|---|---|---|
| Sigmoid | $\sigma(-0.5)\approx0.378$ | $0.378(1-0.378)\approx0.235$ |
| Tanh | $\tanh(-0.5)\approx-0.462$ | $1-0.462^2\approx0.787$ |
| ReLU | $\max(0,-0.5)=0$ | $0$（负区间） |

设想 10 层全用 Sigmoid，梯度因子约 $0.235^{10}\approx 5\times10^{-7}$——**几乎消失**。这正是深层网络弃用 Sigmoid、改用 ReLU 的原因。

```python
import numpy as np
sigmoid = lambda x: 1/(1+np.exp(-x))
tanh    = np.tanh
relu    = lambda x: np.maximum(0, x)
z = -0.5
print(sigmoid(z), tanh(z), relu(z))   # 0.378  -0.462  0.0
```

## 怎么选

- **隐藏层默认用 ReLU**（或 GELU、Leaky ReLU）——快、稳、抗梯度消失。
- **二分类输出层用 Sigmoid**（输出概率），多分类用 Softmax。
- **回归输出层一般不加激活**（直接输出实数）——时间序列预测的输出层通常如此。
- [RNN](../rnn/)/[LSTM](../lstm/) 内部常见 Tanh 与 Sigmoid 配合做门控。

## 常见误区

- **"输出层也要加 ReLU"**——预测实数时不要，否则永远输不出负值。
- **"激活函数越复杂越好"**——ReLU 这么简单却最常用；复杂度不等于效果。
- **"Sigmoid 适合做深层隐藏层"**——恰恰相反，它会导致[梯度消失](../vanishing-exploding-gradient/)。

[← 深度学习基础](../dl/) · [基础课总览](../)
