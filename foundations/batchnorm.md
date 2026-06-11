---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/batchnorm/
title: "BatchNorm（批归一化）"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**批归一化（BatchNorm, Batch Normalization）** 是一种放在网络层之间的操作：它在每个[小批量](../batch/)（mini-batch）上把某一层的输入"拉回"到均值 0、方差 1，再用两个可学习参数重新缩放和平移，从而让训练更稳定、收敛更快。

## 直观理解

训练时每一层的输入分布会随着前面层参数的更新而不断漂移——这叫**内部协变量偏移**（internal covariate shift）。下游层就像在追一个一直在动的靶子，学起来很费劲，学习率稍大就不稳定。

BatchNorm 的做法是：在每一层入口设一个"标准化关卡"，**不管前面传来的数据量级如何，先统一拉到一个稳定的范围**（零均值、单位方差），再交给本层。这样每层面对的输入分布相对稳定，于是：

- 可以用**更大的[学习率](../learning-rate/)**，训练更快；
- 对参数[初始化](../training-practice/)不那么敏感；
- 还带有轻微的[正则化](../regularization/)效果（因为每个样本的归一化依赖整个 batch，引入了一点噪声）。

## 数学表达

对一个含 $m$ 个样本的 mini-batch，针对某个特征维度，设这一维的取值为 $x_1, \dots, x_m$。

第一步，算出本批的均值和方差：

$$
\mu_B = \frac{1}{m}\sum_{i=1}^{m} x_i,
\qquad
\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m} (x_i - \mu_B)^2
$$

第二步，**归一化**（normalize）：

$$
\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

第三步，**缩放与平移**（scale and shift）：

$$
y_i = \gamma\,\hat{x}_i + \beta
$$

逐符号解释：

- $\mu_B,\ \sigma_B^2$：当前 batch 在该特征维上的均值与方差。
- $\epsilon$：一个极小常数（如 $10^{-5}$），防止分母为 0，保证数值稳定。
- $\hat{x}_i$：归一化后的值，分布约为均值 0、方差 1。
- $\gamma$（缩放）、$\beta$（平移）：**可学习参数**，每个特征维各一份，由[反向传播](../backpropagation/)更新。
- $y_i$：BN 的最终输出。

为什么归一化之后还要 $\gamma, \beta$？因为强行把每层都压成"标准正态"可能损失表达力。给网络 $\gamma, \beta$ 这两个旋钮，它可以在需要时**把分布学回去**（甚至当 $\gamma=\sqrt{\sigma_B^2+\epsilon},\ \beta=\mu_B$ 时恢复原始输入），所以 BN 不会削弱模型能力。

## 训练与推理的差别（关键）

这是 BN 最容易出错的地方。

- **训练时**：用的是**当前这一个 batch** 的 $\mu_B, \sigma_B^2$。同时悄悄维护一份全局的**滑动平均统计量**（running mean / running variance）：

$$
\mu_{run} \leftarrow (1-\alpha)\,\mu_{run} + \alpha\,\mu_B
$$

（方差同理，$\alpha$ 是动量，PyTorch 默认 0.1。）

- **推理时**：单个样本没有"batch"可言，也不该让预测结果依赖于碰巧一起喂进来的其他样本。所以推理时**不再用当前批统计量**，而是用训练阶段攒下来的 $\mu_{run}, \sigma_{run}^2$ 做固定的归一化：

$$
y = \gamma\,\frac{x - \mu_{run}}{\sqrt{\sigma_{run}^2 + \epsilon}} + \beta
$$

实践要点：在 PyTorch 中务必用 `model.eval()` 切到推理模式，BN 才会改用 running 统计量；忘记切换会导致预测随 batch 组成而抖动、结果变差。此外 BN 在 **batch 很小**（如 1~2）时统计量噪声大、效果差，这时常改用 LayerNorm。

## 一个具体例子

设某特征在一个 batch 里有 4 个值 $x = [1, 2, 3, 4]$，$\epsilon$ 忽略不计：

$$
\mu_B = \frac{1+2+3+4}{4} = 2.5,\qquad
\sigma_B^2 = \frac{(1.5)^2+(0.5)^2+(0.5)^2+(1.5)^2}{4} = 1.25
$$

$$
\hat{x} = \frac{[1,2,3,4] - 2.5}{\sqrt{1.25}} \approx [-1.342,\ -0.447,\ 0.447,\ 1.342]
$$

归一化后均值约 0、方差约 1。若学到 $\gamma=2,\ \beta=5$，输出 $y = 2\hat{x}+5 \approx [2.32,\ 4.11,\ 5.89,\ 7.68]$。对应代码：

```python
import torch, torch.nn as nn

net = nn.Sequential(
    nn.Linear(32, 64),
    nn.BatchNorm1d(64),   # 对 64 维特征各自归一化
    nn.ReLU(),
    nn.Linear(64, 1),
)
net.train(); y = net(torch.randn(16, 32))   # 训练：用 batch 统计量
net.eval();  y = net(torch.randn(16, 32))   # 推理：用 running 统计量
```

## 小结

- BN 在每个 batch 上**归一化**（减均值除标准差），再用可学习的 $\gamma,\beta$ **缩放平移**。
- $\epsilon$ 防止除零，$\gamma,\beta$ 保住表达力。
- **训练用 batch 统计量、推理用滑动平均统计量**——记得切 `eval()`。
- 它稳定分布、允许更大[学习率](../learning-rate/)、加速收敛，还带轻微正则化；小 batch 场景慎用。
- 与 [Dropout](../dropout/)、[早停](../early-stopping/) 同属常用的[训练实践](../training-practice/)工具。

[← 深度学习基础](../dl/) · [基础课总览](../)
