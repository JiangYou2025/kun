---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/dl/
title: "深度学习基础"
lead: "神经网络、反向传播、优化器、常见架构与训练实践——现代预测模型背后的引擎。只搭框架、讲概念。"
prev: /foundations/ml/
next: /foundations/
math: true
---

> 这是一张**概念地图**：点出深度学习"由什么组成、怎么训练、有哪些架构"，深入数学与实现留给专门教材。

## 1. 神经网络的构成

- **神经元**：加权求和 + 偏置，再过一个非线性
- **层与网络**：神经元堆成层，层堆成网络
- **前向传播**：输入逐层变换得到输出
- **激活函数**：ReLU、Sigmoid、Tanh、GELU——引入**非线性**，否则整个网络退化成线性模型

$$h = \sigma(Wx + b)$$

## 2. 如何训练：反向传播

- **损失函数**：衡量预测与真实的差距
- **反向传播**：用**链式法则**把误差从输出层逐层传回，算出每个参数的梯度
- **自动微分**：框架自动完成上述求导（你只写前向）
- **优化器**：SGD、Momentum、RMSProp、**Adam**（最常用）
- **学习率**：最关键的超参数，太大发散、太小太慢

## 3. 防止过拟合

深度模型参数极多，泛化是核心难题。

- **Dropout**：训练时随机丢弃神经元
- **批归一化 (BatchNorm) / 层归一化 (LayerNorm)**：稳定训练
- **早停 (early stopping)**：验证集变差就停
- **数据增强 / 权重衰减**：进一步正则化

## 4. 常见架构

| 架构 | 擅长 | 时间序列相关 |
|------|------|-------------|
| **MLP / 全连接** | 通用 | DLinear、N-BEATS |
| **CNN** | 局部模式 | TCN、卷积预测器 |
| **RNN / LSTM / GRU** | 序列、记忆 | 经典序列预测 |
| **Transformer / 注意力** | 长程依赖 | 现代序列模型 |
| **U-Net** | 多尺度 | **Kernel U-Net (KUN)** |

## 5. 训练实践

- **批大小 (batch size)** 与 **轮次 (epoch)**
- **GPU 加速**：让大模型训练可行
- **梯度问题**：梯度消失 / 爆炸，及其缓解（残差连接、归一化、梯度裁剪）
- **迁移学习与预训练**：复用已学到的表示

> 衔接主课：第 12–14 讲会把这些架构用到时间序列预测上，最终落到本仓库的 **Kernel U-Net (KUN)**。

---

**关键术语：** [神经元](../neuron/)、[激活函数](../activation-function/)、[前向传播](../forward-propagation/)、[反向传播](../backpropagation/)、[自动微分](../autodiff/)、[Adam](../adam/)、[学习率](../learning-rate/)、[Dropout](../dropout/)、[BatchNorm](../batchnorm/)、[早停](../early-stopping/)、[MLP](../mlp/)、[CNN](../cnn/)、[RNN](../rnn/) / [LSTM](../lstm/)、[Transformer](../transformer/)、[注意力](../attention/)、[U-Net](../u-net/)、[GPU](../gpu/)、[梯度消失 / 爆炸](../vanishing-exploding-gradient/)。
