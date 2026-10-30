---
updated: "2026-06-11"
lang: zh
ref: kun
permalink: /zh/kun/
title: "2026 时间序列前沿问题"
lead: "经过近百年发展，时间序列预测已经积累了大量成熟工具。但 2026 年，研究者仍在追问：我们能做得更好吗？本页梳理当下最热的六大前沿挑战，并看 Kernel U-Net 如何尝试回应其中几个。"
prev: linear-autoregression
next: kernel-u-net
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
    <p>传统模型预测 96 步已经吃力，但现实需求常常是数千甚至数万步：年度电力规划、气候变化建模、基因序列分析。Transformer 的 O(N²) 复杂度让它无法直接处理超长序列，催生了线性注意力、状态空间模型（Mamba/S4）和层次化架构等方案。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何在 O(N) 复杂度下保持长程依赖的建模能力？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🎯</div>
    <h3>不确定性量化 · Uncertainty</h3>
    <p>点预测（给一个数字）远远不够——决策者需要知道"你有多确定"。概率预测、分位数回归、共形预测（conformal prediction）正在成为标配。2024–2026 年，共形预测因其"无分布假设的有限样本覆盖保证"爆发式增长。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何给出既窄又可靠的预测区间？</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚨</div>
    <h3>异常预测 · Anomaly Prediction</h3>
    <p>很多场景关心的不是"下一个值是多少"，而是"会不会出事"：设备故障、电网过载、心律失常。难点在于异常稀少且形态多变，目标又正从"事后检测"转向"提前预警"。常用思路：先对正常模式建模，再把明显偏离当作信号。</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>核心挑战：</strong>如何在异常样本极少、形态又不断变化的情况下，提前而非事后识别出它？</p>
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

## 尝试用 Kernel U-Net 回答这些问题

面对这些挑战，本站给出的探索是 **KUN（Kernel U-Net）**。KUN 把模型拆成两部分：一套固定的 **U 形骨架**，和每一层上**可替换的核**。因此回应一个新问题，往往不必重新设计模型，只需改动其中一处：**换一个核**、**给骨架加一个组件**，或者**换一个输出头**。下表列出六大问题各自的切入点：已有论文的方向在右栏列出论文，标注“（正在研发）”的方向仍在进行中。

| 前沿问题 | 改哪里 | KUN 的思路 |
|---------|-------|-----------|
| 基础模型（正在研发） | 换核 | 把核换成 MoE（混合专家）核并加深层数，看能否把更多领域的数据训练进同一个底座 |
| 超长序列（正在研发） | 加组件 | 在 U 形骨架上增加记忆层，记住更远的历史；逐层下采样又让深层的序列变短，深层也负担得起更重的核 |
| 不确定性量化（正在研发） | 换输出头 | 默认输出点预测；输出端可以接分位数回归或共形预测，给出预测区间 |
| 异常预测 | 换输出头 | 把“预测未来的数值”换成“预测未来的分布（密度）”，当实际观测落进低密度区域时，就提前发出异常预警<br>📄 [Anomaly Prediction: A Novel Approach with Explicit Delay and Horizon (ICCP 2024)](https://arxiv.org/abs/2408.04377) |
| 时空预测 | 改骨架 | 沿空间坐标轴也做层次化处理，让逐层下采样 / 上采样同时覆盖时间与空间<br>📄 [Enhancing Spatio-Temporal Forecasting with Spatial Neighbourhood Fusion: A Case Study on Mobility in Peru (ICASSP 2026)](https://arxiv.org/abs/2507.00031) |
| 泛化性 | 换核 | 做自适应预测：按数据的特征为每一层选择或调整核，迁移到没见过的领域与分布<br>📄 [Dynamic Perturbed Adaptive Method for Infinite Task-Conflicting Time Series (arXiv 2025)](https://arxiv.org/abs/2505.11902) |

它的核心直觉是：**骨架只写一次，新想法靠换核、加组件来实现。** 所以这些前沿研究不必动辄堆到超大模型，普通算力也能上手：每尝试一个新方向，就是写一个新核或一个新模块，再把它接到同一套轻量骨架上。

> KUN 的完整思想、逐层架构、复杂度分析与上手教程，都放在专门的一页：
> **[深入理解 Kernel U-Net](../kernel-u-net/)**。

## 接下来去哪

- **想看 KUN 怎么回应这些挑战**：读 [深入理解 Kernel U-Net](../kernel-u-net/)，从 U 形结构到分步教程一次讲透。
- **想补数学 / 机器学习地基**：回到 [基础课](../../foundations/)。
- **想看这些问题怎么一步步来的**：读 [时间序列发展史](../../history/)。

<div class="hint">本页只盘点"问题"；KUN 作为其中一种"答案"，细节都在 <a href="{{ '/zh/kernel-u-net/' | relative_url }}">深入理解 Kernel U-Net</a>。</div>
