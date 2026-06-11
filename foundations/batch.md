---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/batch/
title: "batch（批）"
no_comments: true
math: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**batch（批）**指的是训练[神经网络](../neural-network/)时，一次性喂给模型的一小组样本。模型按这一批数据计算[梯度](../gradient/)、更新一次参数，然后换下一批，循环往复。

## 直观理解

假设你要根据 10000 道练习题来调整自己的解题思路。有三种节奏：

- **一题一改**：做完一道题立刻反思、调整。反应快，但单题的随机性大，思路容易左右摇摆。这对应 **batch size = 1**（随机[梯度下降](../gradient-descent/)，SGD）。
- **全做完再改**：把 10000 道全做完，统计整体错误再一次性调整。方向最准，但太慢、太耗内存，而且每轮只调一次。这对应 **full batch**。
- **每 32 道一改**：做 32 道题就反思调整一次。既有一定的统计稳定性，又能频繁更新。这就是 **mini-batch**，也是实践中几乎总在用的折中方案。

**batch 的本质是「效率」和「稳定性」之间的权衡。**

## 核心要点

- **batch size**：一批里有多少样本。常见取值 16、32、64、128、256，常取 2 的幂以契合 [GPU](../gpu/) 内存对齐。
- **iteration（迭代）**：处理完一个 batch、更新一次参数，叫一次迭代。
- **epoch（轮）**：把整个训练集完整过一遍叫一个 epoch。
  - 关系：`一个 epoch 的迭代数 = 样本总数 / batch size`（向上取整）。

batch size 的影响：

- **越大**：梯度估计越平滑稳定，越能吃满 GPU 并行，但占内存更多，且有时[泛化](../generalization/)略差。
- **越小**：更新更频繁、内存占用小，但梯度噪声大、训练抖动。

## 一个例子

PyTorch 用 `DataLoader` 自动把数据切成批：

```python
import torch
from torch.utils.data import TensorDataset, DataLoader

# 假设有 1000 条样本，每条 7 个特征
X = torch.randn(1000, 7)
y = torch.randn(1000, 1)

loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

for epoch in range(3):
    for xb, yb in loader:        # 每次拿一个 batch
        # xb.shape == (32, 7)，最后一批可能不足 32
        pred = model(xb)         # 一次前向：整批一起算
        loss = loss_fn(pred, yb)
        loss.backward()          # 按这批算梯度
        optimizer.step()         # 更新一次参数
        optimizer.zero_grad()
```

1000 / 32 ≈ 32 次迭代为一个 epoch。注意 `xb` 的第一维就是 batch 维——整批样本被**堆叠成一个张量**一次性算完，这正是 [GPU](../gpu/) 和[向量化](../vectorization/)发挥威力的地方。

## 在时间序列预测中的意义

训练 **KUN / Kernel U-Net** 这类预测模型时：

- 每个样本通常是一个**滑动窗口**：用过去 `L` 步预测未来 `H` 步。一个 batch 就是 `(batch_size, L, 特征数)` 的张量。
- batch 维让我们能**并行算很多个窗口**，把 GPU 喂饱，大幅缩短训练时间。
- 时序数据要小心：`shuffle=True` 打乱的是**样本（窗口）之间**的顺序，不会打乱单个窗口**内部**的时间顺序——内部顺序绝不能动，否则就破坏了时间结构。

## 常见误区

- **把 batch size 和模型容量混为一谈**：batch size 只影响训练动态，不改变模型能学多复杂。
- **以为 batch 越大越好**：大 batch 省时间，但内存可能爆，且有时需要相应调大[学习率](../learning-rate/)。
- **时序数据里乱 shuffle**：可以打乱窗口顺序，但绝不能打乱窗口内部时间步，也要避免训练窗口「偷看」到验证集未来的数据。
- **忘了最后一批不满**：1000 个样本、batch=32，最后一批只有 8 个，代码要能正确处理。

---

[← 计算机基础](../cs/) · [基础课总览](../)
