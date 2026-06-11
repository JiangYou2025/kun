---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/training-practice/
title: "训练实践"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**训练实践** 指的是一整套让神经网络"训得动、训得稳、训得好"的工程技巧——从参数初始化、归一化、正则化，到学习率调度、早停和训练监控。它们各自简单，合起来却决定了一个模型能否真正可用。

**相关：** [Dropout](../dropout/) · [BatchNorm](../batchnorm/) · [早停](../early-stopping/)

## 直观理解

训练一个网络很像照料一锅在炖的汤：火太大（学习率太高）会糊，火太小（学习率太低）半天不熟；食材没洗净（数据没归一化）味道发苦；调料一次放太多（模型太复杂）会齁（过拟合）。所谓训练实践，就是这套"火候 + 配料 + 尝味道"的经验集合——目标是让[损失](../backpropagation/)平稳下降、并且模型在**没见过的数据**上也表现好。

下面按训练的生命周期，过一遍这个工具箱。

## 起步：初始化与数据/特征归一化

- **权重初始化**：不能全设成 0（那样所有[神经元](../neuron/)对称、学不出东西），也不能太大太小（会立刻[梯度爆炸或消失](../vanishing-exploding-gradient/)）。常用 Xavier / He 初始化，按层的输入输出规模自动设定权重方差。
- **输入归一化**：把每个特征缩放到相近量级（如减均值除标准差），否则量级大的特征会主导梯度，训练扭曲。
- **层间归一化**：[BatchNorm](../batchnorm/) 在每个 batch 上把层输入拉回零均值单位方差再缩放平移，稳定分布、允许更大学习率；小 batch 或序列任务里则常用 LayerNorm。

## 防过拟合：正则化三件套

过拟合 = 训练集很好、验证集很差。常用对策：

- **[Dropout](../dropout/)**：训练时随机失活一部分神经元，强迫网络不依赖个别单元，相当于隐式集成多个子网络。
- **权重衰减（L2 正则）**：在损失里加一项 $\frac{\lambda}{2}\lVert w\rVert^2$ 惩罚过大的权重，让模型更平滑：

$$
L_{\text{total}} = L_{\text{data}} + \frac{\lambda}{2}\sum_w w^2
$$

其中 $\lambda$ 控制正则强度，越大越偏向简单模型。

- **[早停](../early-stopping/)**：盯住验证损失，不再下降就停、并回退到最佳版本，是几乎零成本的正则化。
- **数据增强 / 更多数据**：根本上最有效——数据越多、越多样，越难过拟合。

## 调火候：学习率与优化器

[学习率](../learning-rate/) 是最关键的超参数。配合[优化器](../optimizer/)（如 Adam、SGD+Momentum）使用，常见技巧：

- **学习率调度（lr schedule）**：训练后期把学习率调小，便于收敛到更优的解。常见有 step decay、cosine annealing：

$$
\eta_t = \eta_{\min} + \tfrac{1}{2}(\eta_{\max}-\eta_{\min})\Big(1 + \cos\tfrac{t}{T}\pi\Big)
$$

- **warmup（预热）**：开头几百步用很小的学习率慢慢升上来，避免一开始就把参数冲乱（训练 Transformer 时几乎必备）。
- **梯度裁剪**：把梯度范数限制在阈值内，专治[梯度爆炸](../vanishing-exploding-gradient/)，是训练 [RNN](../rnn/) / [LSTM](../lstm/) 的标配。

## 尝味道：监控训练/验证损失

训练时一定要**同时画出训练损失和验证损失曲线**，它能一眼看出问题：

- **欠拟合（underfitting）**：训练损失都降不下去 → 模型太弱 / 学习率太小 / 训练不够。对策：加大模型、训久点、调学习率。
- **过拟合（overfitting）**：训练损失低、验证损失却开始**上升** → 模型在背训练集。对策：上文的正则化三件套、减小模型、加数据。
- **理想状态**：两条线都降，且验证损失贴着训练损失，差距不大。

经验法则：**先把模型做大到能过拟合一个小数据子集**（验证流程没 bug），再逐步加正则把验证损失压下来。这个"先过拟合、再正则化"的节奏比一上来就猛加正则更高效。

## 一个具体的训练循环

把上面的要点拼进一个最小可用的 PyTorch 训练框架：

```python
import torch, torch.nn as nn

opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)  # 含权重衰减
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)    # lr 调度

best, wait, patience = float("inf"), 0, 10
for epoch in range(epochs):
    model.train()                                   # Dropout / BN 进入训练模式
    for x, y in train_loader:
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # 梯度裁剪
        opt.step()
    sched.step()

    model.eval()                                    # 推理模式：BN 用running、Dropout 关
    with torch.no_grad():
        val = sum(loss_fn(model(x), y) for x, y in val_loader)
    if val < best:                                  # 早停 + 保存最佳
        best, wait = val, 0; torch.save(model.state_dict(), "best.pt")
    else:
        wait += 1
        if wait >= patience: break
```

## 小结

- **起步**：合理初始化 + 输入归一化 + 层间归一化（[BatchNorm](../batchnorm/)）。
- **防过拟合**：[Dropout](../dropout/)、权重衰减、[早停](../early-stopping/)、加数据。
- **调火候**：[学习率](../learning-rate/)调度 + warmup + [优化器](../optimizer/) + 梯度裁剪。
- **看曲线**：用训练/验证损失诊断欠拟合 vs 过拟合，先过拟合再正则。
- 这些通用实践同样用于训练 [RNN](../rnn/)、[LSTM](../lstm/)、[Transformer](../transformer/) 以及本站的多尺度模型 **Kernel U-Net（KUN）**。

[← 深度学习基础](../dl/) · [基础课总览](../)
