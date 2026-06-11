---
updated: "2026-06-11"
lang: zh
ref: kun
permalink: /zh/kun/
title: "2026 前沿问题与 KUN（Kernel U-Net）"
lead: "先看清 2026 年时间序列预测的六大前沿挑战，再理解 KUN（Kernel U-Net）如何回应它们——本页给出 KUN 背后的思想，以及在你自己数据上运行它的分步教程。"
prev: linear-autoregression
math: true
---

## 预测领域的现状

经过一百年的发展（从 1927 年 Yule 的自回归到今天），时间序列预测已经积累了大量成熟的工具。但研究者们仍然在追问：**我们能做得更好吗？**

2026 年，这个领域最热的方向可以归纳为六大前沿问题。

## 🧩 六大前沿问题

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌍</div>
    <h3>基础模型 · Foundation Models</h3>
    <p>GPT 改变了 NLP，基础模型能否改变时间序列？TimesFM（Google）、Chronos（Amazon）、Moirai（Salesforce）等模型在海量时序数据上预训练，追求"零样本预测"——不看你的数据也能预测。但时间序列的分布多样性远超文本，迁移效果仍是开放问题。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>一个模型能通吃电力、金融、天气、医疗吗？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📏</div>
    <h3>超长序列 · Ultra-Long Horizon</h3>
    <p>传统模型预测 96 步已经吃力，但现实需求常常是数千甚至数万步：年度电力规划、气候变化建模、基因序列分析。Transformer 的 O(N²) 复杂度让它无法直接处理超长序列，催生了线性注意力、状态空间模型（Mamba/S4）和层次化架构（如 KUN）等方案。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何在 O(N) 复杂度下保持长程依赖的建模能力？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🎯</div>
    <h3>不确定性量化 · Uncertainty</h3>
    <p>点预测（给一个数字）远远不够——决策者需要知道"你有多确定"。概率预测、分位数回归、共形预测（conformal prediction）正在成为标配。2024–2026 年，共形预测因其"无分布假设的有限样本覆盖保证"爆发式增长。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何给出既窄又可靠的预测区间？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🔀</div>
    <h3>多任务冲突 · Task Conflicts</h3>
    <p>现实中往往需要同时预测多个变量（多变量预测）、多个时间尺度（多步预测）、甚至多个下游任务（预测 + 异常检测 + 分类）。这些任务的梯度方向经常冲突，导致联合训练比单独训练还差。多任务优化（如 MGDA、PCGrad、Nash-MTL）和动态权重方法是当前热点。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>当任务互相拖后腿时，如何让所有任务同时进步？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌐</div>
    <h3>时空预测 · Spatio-Temporal</h3>
    <p>天气预报、交通流量、疫情传播——这些数据不仅随时间变化，还在空间上有结构。GraphCast（DeepMind）用图神经网络做全球天气预报，精度超过了传统数值模式。如何同时建模时间依赖和空间拓扑关系，是时空预测的核心难题。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何融合图结构（空间）和序列结构（时间）？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🛡️</div>
    <h3>泛化性 · Generalization</h3>
    <p>模型在干净的基准数据集上表现优秀，但到了真实世界就崩溃：数据缺失、传感器漂移、突发分布偏移（COVID 就是一次巨大的分布偏移）。如何让模型在"没见过的情况"下也不崩溃？域适应、迁移学习、元学习、在线学习是当前的主要武器。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何让模型在新领域、新分布下依然有效？</p>
  </div>
</div>

## 这些问题之间的关系

这六个方向并非孤立的——它们彼此交织：

```
基础模型 ←→ 超长序列（需要高效架构支撑大模型）
    ↕              ↕
不确定性 ←→ 泛化性（不确定性量化是泛化决策的前提）
    ↕              ↕
多任务 ←→ 时空预测（时空本身就是多任务问题）
```

**没有任何一个方法能同时完美解决所有问题。** 这就是为什么时间序列预测仍然是一个活跃的研究领域——也是为什么我们设计了 KUN。

## KUN 在这张图里的位置

KUN（Kernel U-Net）试图在其中几个方向上做出贡献：

| 前沿问题 | KUN 的回应 |
|---------|-----------|
| 超长序列 | 层次化 U 形架构，逐层下采样/上采样，O(N) 复杂度 |
| 多任务 | 对称式编码器-解码器，天然适合多变量联合预测 |
| 泛化性 | 可插拔核函数（线性/MLP/注意力），适应不同数据特征 |


> 下面我们就正式拆开 KUN：先看整体思想，再一步步上手。

## 一张图看懂思想

KUN 借用了图像分割中 **U-Net** 的形状：一个不断压缩输入的**编码器**，和一个不断把它扩张回预测的**对称解码器**，信息在对应的层级之间流动。

```
输入窗口
   │  切分成 patch（片段）
   ▼
[ 编码器 ]  patch → patch → patch        （下采样：单元更少、更粗）
   │            │      │       │
   │         skip   skip    skip          （对应层级相连）
   ▼            ▼      ▼       ▼
[ 解码器 ]  patch ← patch ← patch        （上采样：重建分辨率）
   │
   ▼
预测时域
```

让 KUN 得名的关键之处在于：在 U 形的每个节点上，执行的运算是一个**可插拔的核（kernel）**，而不是固定的卷积。一个核就是一个把片段映射到片段的小函数——它可以是**线性层、MLP、RNN 或注意力模块**。你为每个层级选择核，于是同一套骨架既可以做得很轻量，也可以做得很有表达力。

## 什么是“多尺度”的序列

要理解 KUN 为什么长成 U 形，先要看清一件事：**一条真实的时间序列，往往同时藏着好几个“尺度”。**

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 380" role="img" aria-label="一条序列分解成多个尺度">
  <text x="12" y="40" fill="var(--muted)" font-size="13">原始序列</text>
  <text x="12" y="56" fill="var(--muted)" font-size="11">（你看到的）</text>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="175,72 222,58 269,66 316,44 363,58 410,36 457,50 504,28 551,44 598,22 645,36 690,16"/>
  <text x="430" y="116" fill="var(--muted)" font-size="13" text-anchor="middle">拆开看 ＝ 多个尺度叠加 ↓</text>
  <line x1="160" y1="128" x2="700" y2="128" stroke="var(--border)"/>

  <text x="12" y="178" fill="var(--accent)" font-size="13">粗尺度</text>
  <text x="12" y="194" fill="var(--muted)" font-size="11">长期趋势</text>
  <line x1="175" y1="200" x2="690" y2="200" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,190 269,180 363,164 457,146 551,130 645,114 690,106"/>

  <text x="12" y="262" fill="var(--accent-2)" font-size="13">中尺度</text>
  <text x="12" y="278" fill="var(--muted)" font-size="11">周期</text>
  <line x1="175" y1="262" x2="690" y2="262" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,262 222,238 269,262 316,286 363,262 410,238 457,262 504,286 551,262 598,238 645,262 690,286"/>

  <text x="12" y="340" fill="#fbbf24" font-size="13">细尺度</text>
  <text x="12" y="356" fill="var(--muted)" font-size="11">高频细节</text>
  <line x1="175" y1="338" x2="690" y2="338" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="175,338 215,324 255,350 295,328 335,352 375,322 415,346 455,330 495,352 535,326 575,348 615,330 655,346 690,332"/>
</svg>
<figcaption class="figcap">同一条序列里同时叠着：<strong>粗</strong>的长期趋势、<strong>中</strong>等的周期、<strong>细</strong>的高频起伏。只盯着任何一个尺度都不完整——这就是说一条序列是<strong>多尺度 (multi-scale)</strong> 的。</figcaption>
</figure>

近处的细节（明天比今天高一点点）和远处的轮廓（这一年整体在涨）是**两种不同粒度**的信息，它们需要被分别看清、再合起来。这正是 KUN 的 U 形所做的事：编码器把序列一层层**变粗**（先看细节、再看大轮廓），解码器再一层层**变细**地重建出预测——一次把所有尺度都照顾到。下一节就讲为什么这个设计有效。

## 为什么这个设计有效

- **层次结构匹配时间。** 靠近输入的短 patch 捕捉局部、高频的细节；更深的层级看到更长、更粗的上下文。一条序列很少只存在于单一尺度上，而 U 形一次就能捕捉多个尺度。
- **对称带来高效。** 由于解码器镜像了编码器，模型可以重建出完整的时域，而不会随长度产生二次方的开销——这是相对于普通 Transformer 在长序列上的优势。
- **核带来灵活。** 线性核给出快速而强劲的基线（与 DLinear 思路一致）；注意力核在数据需要时增加容量。你通过替换核、而不是重写模型，来在算力和精度之间权衡。
- **直接多输出。** KUN 一次性预测整个时域，避免了递归预测的误差累积。

## 分步教程：用 KUN 做预测

> **关于 API 的说明。** 下面的代码片段展示的是一个典型训练流程的*形状*，方便你将其改写为本仓库中 KUN 真正的接口。等代码正式发布后，请把导入路径、类名和参数名替换成代码里真实的名字。请把它当作模板，而不是可直接复制运行的代码。

### 1. 获取代码并安装

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # 或者：pip install -e .
```

### 2. 整理数据

KUN 期望 [时间序列](./../time-series/) 一页里讲的滑动窗口格式：长度为 `L`（回看）的输入，映射到长度为 `H`（时域）的输出，共有 `C` 个通道（变量）。

```python
# x: 形状为 (样本数, L, C) 的数组  -> 回看窗口
# y: 形状为 (样本数, H, C) 的数组  -> 要预测的目标
```

务必**按通道归一化**（减去训练集均值、除以训练集标准差），并**按时间切分**。

### 3. 配置模型

```python
from kun import KernelUNet            # 改成真实的导入路径

model = KernelUNet(
    input_len=336,     # L —— 回看窗口
    pred_len=96,       # H —— 预测时域
    n_channels=7,      # C —— 变量个数
    patch_sizes=[16, 8, 4],   # 每个层级如何切分序列
    kernel="linear",          # "linear" | "mlp" | "attention" —— 每层的核
)
```

先从 `kernel="linear"` 和较短的时域开始。它几秒就能训练完，并给你一个要去超越的基线——这正是 [如何做预测](./../forecasting/) 一页强调的纪律。

### 4. 训练

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.L1Loss()          # MAE —— 鲁棒且可解释

for epoch in range(50):
    for xb, yb in train_loader:
        opt.zero_grad()
        pred = model(xb)             # (batch, H, C)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.step()
```

### 5. 评估与预测

```python
model.eval()
with torch.no_grad():
    pred = model(x_test)             # 预测留出的时域
mae = (pred - y_test).abs().mean()
print("测试集 MAE:", mae.item())
```

把这个数字和**季节性朴素基线**对比。如果 KUN 赢了，你就有了一个真正有用的模型；如果没赢，回头检查你的窗口、归一化和切分方式。

## 一个合理的调参顺序

1. **回看长度 `L`**——更长的上下文通常对长时域有帮助，但有上限。
2. **patch 大小**——层级越多，层次性越强；尽量让每个 patch 大小能整除该层级的长度。
3. **核的选择**——只有当验证误差能证明额外开销值得时，才从 `linear` → `mlp` → `attention` 升级。
4. **学习率与轮数**——基于验证集 MAE 做早停。

## 接下来去哪

- 重读 [如何做预测](./../forecasting/)，先把基线跑出来——KUN 只有相对于基线才有意义。
- 在 [GitHub](https://github.com/JiangYou2025/kun) 上提 issue 或阅读源码，以获得当前确切的 API。

<div class="note">
  <strong>引用 KUN。</strong> 如果 KUN 对你的研究或产品有帮助，请引用 Jiang You 的 Kernel U-Net 工作，并附上本仓库的链接。
</div>
