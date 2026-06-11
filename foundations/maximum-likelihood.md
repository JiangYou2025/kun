---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/maximum-likelihood/
title: "极大似然"
no_comments: true
math: true
---

> 出自[数学基础](../math/) · [基础课总览](../)

极大似然估计（MLE）是一种**找参数**的方法：在所有可能的参数里，挑出那组能让"**我们实际观测到的数据**"出现概率最大的。许多模型的训练目标，本质上就是极大似然。

## 直观理解

你捡到一枚硬币，抛了 10 次，得到 7 正 3 反。问：这枚硬币正面概率 $p$ 大概是多少？

直觉会说 0.7。极大似然把这个直觉变成原则：**哪个 $p$ 让"7 正 3 反"这件事最可能发生，就选哪个 $p$**。

- 若 $p=0.1$，出现 7 正几乎不可能；
- 若 $p=0.7$，出现 7 正相当自然；
- 所以 0.7 是"最能解释数据"的参数。

极大似然就是"**让模型尽量不对已发生的数据感到意外**"。

## 数学表达

设数据 $x_1,\dots,x_n$ 独立同分布，模型参数为 $\theta$。**似然函数**是数据在该参数下出现的联合概率：

$$
L(\theta)=\prod_{i=1}^{n} p(x_i\mid\theta)
$$

连乘不好处理，取对数变成连加（对数单调，不改变最大值位置），得**对数似然**：

$$
\ell(\theta)=\sum_{i=1}^{n}\log p(x_i\mid\theta)
$$

极大似然估计：

$$
\hat\theta_{\text{MLE}}=\arg\max_\theta\ \ell(\theta)
$$

实践中常等价地**最小化负对数似然**（NLL），这就和[损失函数](../loss-function/) / [梯度下降](../gradient-descent/)对上了：

$$
\hat\theta=\arg\min_\theta\ \Big(-\sum_i\log p(x_i\mid\theta)\Big)
$$

## 一个具体例子

回到 7 正 3 反。似然 $L(p)=p^7(1-p)^3$，取对数：

$$
\ell(p)=7\log p+3\log(1-p)
$$

求导令其为零：

$$
\ell'(p)=\frac{7}{p}-\frac{3}{1-p}=0\ \Rightarrow\ 7(1-p)=3p\ \Rightarrow\ p=0.7
$$

果然是 0.7，和直觉一致。

```python
import numpy as np
ps = np.linspace(0.01, 0.99, 99)
ll = 7*np.log(ps) + 3*np.log(1-ps)
print(round(ps[np.argmax(ll)], 2))   # 0.7
```

## 为什么重要 / 用在哪

- **统一的训练原则**：线性回归（假设高斯噪声）的 MLE 恰好给出**最小二乘**；分类的 MLE 恰好给出[交叉熵](../cross-entropy/)损失。
- 它与[贝叶斯](../bayes-theorem/)互补：MLE 只看似然 $p(\text{数据}\mid\theta)$，贝叶斯额外乘上先验 $p(\theta)$（加正则项就相当于加先验，即 MAP 估计）。
- 大样本下 MLE 有良好统计性质（一致性、渐近有效性）。

## 在时间序列预测中的意义

- 经典模型（AR、ARIMA、GARCH）的参数大多用极大似然来拟合。
- 概率预测中，训练目标常写成"最大化未来观测的对数似然"——比如让模型输出的高斯分布尽量贴合真实值。
- KUN（Kernel U-Net）做点预测用 MSE，背后正是"高斯噪声下的极大似然"；若改成概率预测，损失就直接写成负对数似然。

## 常见误区

- 似然**不是**参数的概率：$L(\theta)$ 是"数据的概率随 $\theta$ 变化"，对 $\theta$ 不积分为 1。
- 小样本时 MLE 可能[**过拟合**](../overfitting/)（如方差估计偏小），这时加先验 / 正则（MAP）更稳。
- 记得用**对数**似然：连乘易下溢，连加更稳定，也便于求导。

[← 数学基础](../math/) · [基础课总览](../)
