---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/optimizer/
title: "优化器"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**优化器（optimizer）**是根据[反向传播](../backpropagation/)算出的梯度，去**实际更新网络参数**的算法。它决定了"知道往哪走"之后**具体怎么迈步**——步子多大、要不要参考历史方向、每个参数是否用不同步长。最常见的有 SGD、Momentum、[Adam](../adam/)。

## 直观理解

把训练想象成**在山谷里蒙眼下山**找最低点（损失最小）。反向传播告诉你脚下**最陡的下坡方向**（负梯度）。但光知道方向不够，你还得决定：

- 一步迈多大？（这就是[学习率](../learning-rate/)）
- 要不要像滚下山的球一样**带点惯性**，冲过小坑？（动量）
- 平缓的方向多走、陡峭的方向少走？（自适应步长）

不同的优化器，就是这些策略的不同组合。**优化器 = 把梯度变成参数更新的规则。**

## 原理：从最朴素到自适应

**最朴素的梯度下降（SGD）**：

$$
\theta_{t+1} = \theta_t - \eta\, g_t
$$

- $\theta_t$：第 $t$ 步的参数；$g_t = \nabla_\theta \mathcal{L}$ 是当前梯度；$\eta$ 是[学习率](../learning-rate/)（步长）。
- 含义：朝负梯度方向走 $\eta$ 那么远。简单，但容易在狭长山谷里来回震荡、收敛慢。

**加入动量（Momentum）**：累积一个"速度"，让更新带惯性：

$$
v_t = \beta v_{t-1} + g_t,\qquad
\theta_{t+1} = \theta_t - \eta\, v_t
$$

- $v_t$：速度（梯度的指数移动平均）；$\beta$（如 0.9）控制保留多少历史。
- 效果：在一致的方向上**加速**，在来回震荡的方向上**抵消**，更平稳更快。

**自适应步长（如 Adam）**：再给每个参数单独缩放步长——梯度一直很大的参数用小步，稀疏更新的参数用大步。这就是 [Adam](../adam/) 做的事，它结合了动量 + 逐参数自适应。

## 一个具体例子

最小化 $\mathcal{L}(\theta) = \theta^2$（最优解 $\theta=0$，梯度 $g=2\theta$）。从 $\theta_0 = 1$、$\eta=0.1$ 出发用 SGD：

$$
\theta_1 = 1 - 0.1\times(2\times1) = 0.8
$$
$$
\theta_2 = 0.8 - 0.1\times(2\times0.8) = 0.64
$$
$$
\theta_3 = 0.64 - 0.1\times(2\times0.64) = 0.512
$$

每步乘 0.8，稳稳地朝 0 收敛。

```python
import torch
theta = torch.tensor([1.0], requires_grad=True)
opt = torch.optim.SGD([theta], lr=0.1)        # 换成 torch.optim.Adam 即用 Adam
for step in range(3):
    opt.zero_grad()
    loss = theta**2
    loss.backward()                            # 反向传播算梯度
    opt.step()                                 # 优化器更新参数
    print(round(theta.item(), 3))             # 0.8, 0.64, 0.512
```

注意分工：`loss.backward()`（[反向传播](../backpropagation/) / [自动微分](../autodiff/)）**只算梯度**；`opt.step()`（优化器）**才更新参数**。

## 为什么重要 / 用在哪

- 优化器**直接决定训练能否收敛、收敛多快、最终精度多高**。同一个网络换优化器，结果可能天差地别。
- 它是除[学习率](../learning-rate/)之外最重要的训练旋钮。实践中，**[Adam](../adam/) 是默认首选**，省心且稳健；追求极致泛化时有人改用 SGD+Momentum 慢慢调。

## 在时间序列预测中的意义

训练像 [Kernel U-Net (KUN)](../../zh/kun/) 这样的预测模型时，长回看窗口、多尺度结构会让损失曲面更复杂、梯度尺度差异更大。这时**自适应优化器（Adam）的逐参数步长**特别有用——它能在不同尺度的参数间自动平衡，配合一个合理的[学习率](../learning-rate/)，让 KUN 又快又稳地收敛。

## 小结

- 优化器 = **把梯度转化为参数更新的规则**；梯度由反向传播提供。
- 演进路线：SGD → +动量（带惯性）→ +自适应步长（Adam）。
- 与[学习率](../learning-rate/)是一对搭档：优化器定"怎么走"，学习率定"走多远"。

[← 深度学习基础](../dl/) · [基础课总览](../)
