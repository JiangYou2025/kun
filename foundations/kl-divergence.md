---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/kl-divergence/
title: "KL 散度"
no_comments: true
math: true
---

> 出自[数学基础](../math/) · [基础课总览](../)

KL 散度（Kullback–Leibler divergence）衡量"**用一个分布 $q$ 去近似真实分布 $p$**"所付出的额外代价（信息损失）。它总是非负，且**不对称**——交换两个分布结果会变。

## 直观理解

假设真相服从分布 $p$，但你手上只有一个近似模型 $q$。如果你按照 $q$ 来为各种事件设计编码、做决策，而世界其实按 $p$ 运行，你就会**浪费**一些比特——浪费的多少，就是 KL 散度。

- $q$ 越接近 $p$，浪费越少，KL 越接近 0；
- 当 $q=p$ 时，没有任何浪费，KL = 0；
- $q$ 越偏离 $p$，KL 越大。

可以把它读作"**从 $p$ 到 $q$ 的信息距离**"，但要小心：它不是真正的距离（不对称、不满足三角不等式）。

## 数学表达

离散形式：

$$
D_{\mathrm{KL}}(p\parallel q)=\sum_i p_i\log\frac{p_i}{q_i}
$$

- $p_i$ —— 真实分布的概率（权重，决定哪些事件"重要"）；
- $q_i$ —— 近似分布的概率；
- $\log\dfrac{p_i}{q_i}$ —— 在事件 $i$ 上 $q$ 偏离 $p$ 的程度。

它与[熵](../entropy/)、[交叉熵](../cross-entropy/)的关系非常重要：

$$
D_{\mathrm{KL}}(p\parallel q)=\underbrace{-\sum_i p_i\log q_i}_{\text{交叉熵 }H(p,q)}-\underbrace{\Big(-\sum_i p_i\log p_i\Big)}_{\text{熵 }H(p)}=H(p,q)-H(p)
$$

即 **KL 散度 = 交叉熵 − 熵**。由于 $H(p)$ 是常数，训练中最小化交叉熵就等于最小化 KL 散度。

两条关键性质：

- **非负性**：$D_{\mathrm{KL}}(p\parallel q)\ge 0$，等号当且仅当 $p=q$（吉布斯不等式）。
- **不对称**：$D_{\mathrm{KL}}(p\parallel q)\ne D_{\mathrm{KL}}(q\parallel p)$。

## 一个具体例子

真实 $p=[0.5,0.5]$，近似 $q=[0.9,0.1]$（以 2 为底）：

$$
D_{\mathrm{KL}}(p\parallel q)=0.5\log_2\frac{0.5}{0.9}+0.5\log_2\frac{0.5}{0.1}\approx 0.5(-0.848)+0.5(2.322)\approx 0.737
$$

反过来 $D_{\mathrm{KL}}(q\parallel p)\approx 0.531$，**两者不相等**，直观印证了不对称性。

```python
import numpy as np
def kl(p, q):
    p, q = np.array(p), np.array(q)
    return np.sum(p * np.log2(p / q))
print(round(kl([0.5, 0.5], [0.9, 0.1]), 3))  # 0.737
print(round(kl([0.9, 0.1], [0.5, 0.5]), 3))  # 0.531  ≠ 上面
```

## 为什么重要 / 用在哪

- **变分自编码器（VAE）**：[损失](../loss-function/)里有一项 KL，约束隐变量分布靠近标准正态。
- **变分推断**：用可计算的 $q$ 去近似复杂后验，目标就是最小化 KL。
- **模型蒸馏、[强化学习](../reinforcement-learning/)（如 PPO）**：用 KL 约束新旧策略 / 分布别变化太猛。
- 它是[交叉熵](../cross-entropy/)损失背后的"真正"被优化的量。

## 在时间序列预测中的意义

- 概率预测中，KL 散度可衡量"**预测的未来分布**"与"**实际分布**"差多远。
- 检测**分布漂移**（concept drift）：训练期与上线后数据分布的 KL 变大，提示模型该重新训练了。
- 若 KUN（Kernel U-Net）输出概率 / 分位数形式的预测，其训练目标可写成最小化预测分布对真实分布的 KL。

## 常见误区

- **不是距离**：不对称、不满足三角不等式，别当成欧氏距离用；需要对称版可用 JS 散度。
- 当某个 $q_i=0$ 而 $p_i>0$ 时 KL 变成无穷——实践中要给 $q$ 加平滑或裁剪。
- 方向有讲究：$D_{\mathrm{KL}}(p\parallel q)$（前向，"覆盖"真相）和 $D_{\mathrm{KL}}(q\parallel p)$（反向，"聚焦"众数）行为不同，选错会影响近似效果。

[← 数学基础](../math/) · [基础课总览](../)
