---
updated: "2026-06-11"
lang: zh
ref: kernel-u-net
permalink: /zh/kernel-u-net/
title: "深入理解 Kernel U-Net（KUN）"
lead: "KUN 用一个 U 形的对称结构，把一条时间序列“从细到粗、再从粗到细”地走一遍，每个节点上换用一个可插拔的核。这一页把这套结构逐层拆开：它要解决什么问题、每一层在做什么、为什么高效、怎么上手，以及它和 DLinear、Transformer 的本质区别。"
prev: kun
math: true
---

> 这是 [2026 时间序列前沿问题](../kun/) 一页的**展开篇**：那一页讲清楚 KUN 想回应哪些挑战，本页把 KUN 的**思想、逐层架构、复杂度，以及上手教程**一次讲透。

## 一句话定位

**KUN（Kernel U-Net）= U-Net 的层次化形状 + 可插拔的核。** 它把图像分割里 [U-Net](../../foundations/u-net/) 的“编码器下采样、解码器上采样、跳跃连接”搬到时间序列上，并把每个节点上固定的卷积，换成一个可以自由选择的小函数——线性、[MLP](../../foundations/mlp/) 或[注意力](../../foundations/attention/)。

## KUN 要解决什么问题

回顾 [2026 时间序列前沿问题](../kun/)，长时域预测有两个绕不开的矛盾：

1. **多尺度**——一条真实序列同时叠着长期趋势、中期周期、短期高频细节，像多种波形的复合。只盯单一尺度的模型都不完整。
2. **效率 vs. 表达力**——[Transformer](../../foundations/transformer/) 用自注意力捕捉长程依赖，但复杂度是 $O(L^2)$，序列一长就吃不消；而极简的线性模型（DLinear）又快又强，却难以表达复杂结构。

KUN 的回答是：**用层次结构天然地分离尺度，用可插拔核在“快”和“强”之间自由滑动。**

## 先看清：一条序列是“多尺度”的

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

近处的细节（明天比今天高一点点）和远处的轮廓（这一年整体在涨）是**两种不同粒度**的信息，它们需要被分别看清、再合起来。这正是 KUN 的 U 形所做的事：编码器把序列一层层**变粗**（先看细节、再看大轮廓），解码器再一层层**变细**地重建出预测——一次把所有尺度都照顾到。

## 核心思想：为什么是 U 形

图像里的 U-Net 先把图一层层缩小、看清“全局轮廓”，再一层层放大、补回“局部细节”，并用跳跃连接把两端缝合。时间序列同理：

```
输入窗口 (L 步)
   │  切分成 patch（片段）
   ▼
[ 编码器 ]  patch → patch → patch → ⋯ → 潜在表示   （下采样：单元更少、更粗、尺度更大）
   │            │       │       │
   │          skip    skip    skip                  （跳跃连接：把细节直送对应层）
   ▼            ▼       ▼       ▼
[ 解码器 ]  patch ← patch ← patch ← ⋯ ← 潜在表示   （上采样：从粗到细重建）
   │
   ▼
预测时域 (H 步)
```

**每往下一层，看到的尺度就更粗一级**：靠近输入的浅层捕捉局部、高频的细节；越深的层看到越长、越粗的上下文。一条序列很少只活在单一尺度上，而 U 形一次就把多个尺度都照顾到了。

## 架构逐层拆解

### 1. 切 patch（分块）

输入是一个长度为 $L$、通道数为 $C$（变量个数）的窗口，形状 $(L, C)$。KUN 先把它沿时间切成若干 **patch（片段）**，作为最细一层的单元。

### 2. 编码器：逐层下采样

每一层把相邻的若干 patch **聚合（chunk）**成一个更粗的单元，时间分辨率随之降低、单元变少：

$$\text{编码器：}\quad (L, C) \xrightarrow{\;k_1\;} (L/k_1,\, C') \xrightarrow{\;k_2\;} \cdots \xrightarrow{\;\;} (1,\, C_{\text{latent}})$$

其中 $k_l$ 是第 $l$ 层的下采样率（由 `patch_sizes` 决定）。走到最深处，整段序列被压成一个**潜在表示**——它编码了最粗的全局信息（比如“这一年整体在涨”）。

### 3. 解码器：逐层上采样

解码器镜像编码器，每一层把粗单元**展开（expand）**回更细的分辨率，一路重建到预测长度 $H$：

$$\text{解码器：}\quad (1,\, C_{\text{latent}}) \xrightarrow{\;\;} \cdots \xrightarrow{\;\;} (H,\, C)$$

### 4. 跳跃连接

编码器每一层的输出，会直接连到解码器对应的同级层。这样从粗到细重建时，**细节不会在压缩中丢失**——这正是 U-Net 名字里那道“跳过中间、横跨两端”的连接。

### 5. 直接多输出

KUN **一次性输出整个预测时域**（direct multi-output），而不是预测一步、再把它喂回去预测下一步。这避免了递归预测的**误差累积**——预测越往后，递归方式的误差滚雪球越严重。

## 让它得名的关键：可插拔的核

U 形是骨架，**核（kernel）才是 KUN 的灵魂**。在 U 形的每个节点上，那个“把一组片段映射到另一组片段”的运算，并不是固定的卷积，而是一个可以替换的小函数 $\mathcal{K}_l$：

$$\text{第 } l \text{ 层：}\quad \mathbf{z}_{l+1} = \mathcal{K}_l(\mathbf{z}_l)$$

而 $\mathcal{K}_l$ 可以是：

| 核类型 | 表达力 | 开销 | 何时选它 |
|--------|--------|------|---------|
| **线性核** | 低 | 极小，$O(L)$ | 默认起点；与 DLinear 思路一致，又快又是强基线 |
| **[MLP](../../foundations/mlp/) 核** | 中 | 中 | 需要一点非线性时 |
| **[注意力](../../foundations/attention/)核** | 高 | 大，但只作用在被下采样后的短序列上 | 数据复杂、验证误差证明值得时 |

**关键在于**：你通过**替换核**、而不是重写模型，来在算力和精度之间权衡。把“算力 vs. 精度”的选择，变成了“给这一层换一个 $\mathcal{K}_l$”。而且注意力核作用的是**已经被下采样、变短了的序列**，所以即便用注意力，开销也远小于在原始长序列上直接做 $O(L^2)$ 自注意力。

## 复杂度：为什么是 O(L)

| 特性 | DLinear | Transformer | **KUN** |
|------|---------|-------------|---------|
| 多尺度 | ✗ | 部分（patch） | ✓ 天然层次 |
| 可解释 | 趋势 + 季节 | 注意力图 | 每层对应一个尺度 |
| 核 / 算子 | 仅线性 | 仅注意力 | 线性 / MLP / 注意力**可选** |
| 复杂度 | $O(L)$ | $O(L^2)$ | $O(L)$（线性核） |
| 跳跃连接 | ✗ | ✗ | ✓ 保留细节 |
| 多步输出 | 直接 | 直接 / 递归 | 直接多输出 |

层次化下采样让序列长度随层数**几何级缩短**，因此即便深层用了较重的核，总开销也被压住。在长时域、多变量任务上，这让 KUN 同时拿到“线性模型的效率”和“接近注意力模型的表达力”。

## 设计哲学：复杂度由数据说了算

KUN 背后的判断和这十年的潮流一致（详见[发展史第 10 章](../../history/10/)）：**模型该多复杂，应该由数据决定，而不是一开始就押注最重的架构。**

- 数据简单 → 全用线性核，KUN 退化成一个高效的层次化线性模型；
- 数据复杂 → 在需要的层级换上注意力核，按需增加容量。

把“层次化建模”和“灵活的核选择”统一进一个对称框架——这就是 KUN 在大模型时代里，对**结构化、高效设计**的一次探索。

## 分步教程：用 KUN 做预测

> **关于 API 的说明。** 下面的代码片段展示的是一个典型训练流程的*形状*，方便你将其改写为本仓库中 KUN 真正的接口。等代码正式发布后，请把导入路径、类名和参数名替换成代码里真实的名字。请把它当作模板，而不是可直接复制运行的代码。

### 1. 获取代码并安装

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # 或者：pip install -e .
```

### 2. 整理数据

KUN 期望 [时间序列](../time-series/) 一页里讲的滑动窗口格式：长度为 `L`（回看）的输入，映射到长度为 `H`（时域）的输出，共有 `C` 个通道（变量）。

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

先从 `kernel="linear"` 和较短的时域开始。它几秒就能训练完，并给你一个要去超越的基线——这正是 [如何做预测](../forecasting/) 一页强调的纪律。

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

- **想动手跑**：见上面的[分步教程](#分步教程用-kun-做预测)，从线性核 + 短时域的基线开始。
- **想先打牢基线**：重读 [如何做预测](../forecasting/)——KUN 只有相对于基线才有意义。
- **想看它在方法史里的位置**：读[发展史第 10 章 · 大模型、线性回归与 Kernel U-Net](../../history/10/)。
- **想要课程视角**：见[第 14 讲 · 现代预测模型](../../course/14/)，里面有 N-BEATS、DLinear 与 KUN 的对照。
- **想看源码 / 提问**：[GitHub 仓库](https://github.com/JiangYou2025/kun)。

<div class="note">
  <strong>引用 KUN。</strong> 如果 KUN 对你的研究或产品有帮助，请引用 Jiang You 的 Kernel U-Net 工作，并附上本仓库的链接。
</div>
