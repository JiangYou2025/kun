---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/transformer/
title: "Transformer"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**Transformer** 是一种完全基于[注意力](../attention/)（自注意力）的[神经网络](../neural-network/)架构。它抛弃了循环结构，**并行处理整段序列、一步直连任意两个位置**，能高效捕捉长程依赖，是现代序列建模（含所有大语言模型）的主流骨架。

## 直观理解

在 Transformer 之前，序列建模主要靠 [RNN](../rnn/) / [LSTM](../lstm/)：像读书一样一个字一个字往后读，信息靠"记忆"一步步传递。问题是——读得越远，前面的信息越容易被冲淡，而且必须**串行**，没法并行加速。

Transformer 的思路完全不同：**把整段序列一次性铺开，让每个位置同时"看"所有位置**，按相关性自行决定关注谁。没有"传话"的损耗，没有串行的瓶颈。代价是它本身不知道顺序，所以要额外**告诉它每个位置在哪**（位置编码）。

## 原理

一个 Transformer 由若干相同的**块（block）** 堆叠，每块包含两个子层，各自配一个残差连接和层归一化：

**子层 1：多头自注意力**

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left( \frac{QK^{\top}}{\sqrt{d_k}} \right) V
$$

其中 $Q, K, V$ 都由输入线性投影得到，$d_k$ 是每个头的维度，$\sqrt{d_k}$ 做缩放（细节见[注意力](../attention/)）。多头 = 并行多套，关注不同方面后拼接。

**子层 2：逐位置前馈网络**（其实就是一个小 [MLP](../mlp/)，对每个位置独立作用）

$$
\mathrm{FFN}(x) = W_2\,\sigma\!\left(W_1 x + b_1\right) + b_2
$$

- $W_1, W_2$：两层权重（中间维度通常放大 4 倍）；
- $\sigma$：[激活函数](../activation-function/)（如 ReLU/GELU）。

**残差 + 层归一化**包住每个子层，缓解[梯度消失 / 爆炸](../vanishing-exploding-gradient/)、让深层可训练：

$$
x \leftarrow \mathrm{LayerNorm}\big(x + \mathrm{Sublayer}(x)\big)
$$

**位置编码（Positional Encoding）**：因为自注意力对顺序"无感"，要给输入加上携带位置信息的向量，例如正弦式

$$
PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right),\qquad
PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)
$$

- $pos$：位置序号；$i$：维度索引；$d$：模型维度。不同频率的正余弦让每个位置有独一无二的"指纹"。

## 一个具体例子

最小的编码器块（PyTorch 内置）：

```python
import torch, torch.nn as nn

layer = nn.TransformerEncoderLayer(
    d_model=64, nhead=4,           # 模型维 64，4 个注意力头
    dim_feedforward=256,           # FFN 中间层 64*4
    batch_first=True,
)
encoder = nn.TransformerEncoder(layer, num_layers=2)

x = torch.randn(8, 96, 64)         # (批量, 序列长=96, 特征=64)
out = encoder(x)                   # (8, 96, 64)，每个位置都已融合全局信息
```

`x` 的每个时间步进去时只带自己的信息，出来时已经"看过"全部 96 步并按相关性融合。

## 为什么重要 / 用在哪

- **并行训练**：整段序列一次算完，远快于必须串行的 RNN。
- **长程依赖强**：任意两位置一步直连，关系不随距离衰减。
- **可扩展**：堆得越深、数据越多，效果越好——这正是大模型时代的基石。
- 时序领域也有大量 Transformer 变体（Informer、Autoformer、PatchTST 等）。

## 在时间序列预测中的意义

Transformer 把注意力带来的"长程直连"优势用到了预测上，能直接关联跨周期的远端时刻。但它继承了注意力的硬伤：自注意力在长度 $L$ 的序列上是 **$O(L^2)$** 的时间与显存开销。时间序列的历史窗口动辄上千甚至上万步，二次方代价会让标准 Transformer 又慢又吃显存。

本站主推模型 **Kernel U-Net (KUN)** 给出的是另一条路：借鉴 [U-Net](../u-net/) 的**多尺度编码—解码**结构，在时间轴上逐级下采样，把长程依赖放到**更短的粗粒度序列**上以更低成本建模，而不是在全长序列上硬扛 $O(L^2)$。需要强调的是，**这不是"注意力 vs. Transformer"的对立**——注意力依然可以作为某个尺度上的局部组件嵌入 KUN；KUN 改变的是整体复杂度结构，用多分辨率换取在长序列上的高效。

## 常见误区

- **"Transformer 天生懂顺序"**：不懂。顺序信息全靠**位置编码**注入，去掉它打乱输入结果不变。
- **"注意力是 $O(L)$"**：标准自注意力是 $O(L^2)$，这正是长序列预测要做高效化（或换 KUN 这类多尺度结构）的原因。
- **"Transformer 永远比 RNN/[CNN](../cnn/)/MLP 强"**：不一定。在中短时序、数据有限时，简单的 [MLP](../mlp/) 或多尺度模型常常更省、更准。

[← 深度学习基础](../dl/) · [基础课总览](../)
