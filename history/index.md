---
layout: history
lang: zh
permalink: /history/
title: "时间序列百年史 · 目录"
lead: "从 1927 年 Yule 的自回归到今天的深度学习与基础模型——时间序列分析与预测的一百年。一篇序章 + 10 章正文，每节按“背景 → 问题 → 解决方法 → 效果 → 价值”展开，并写出关键公式、逐一分析。"
---

## 这是什么 (About)

一部关于**时间序列 (time series)** 方法演进的百年编年史：从统计学的奠基，到状态空间与 Box–Jenkins 范式，再到机器学习与深度学习的浪潮，直至 Transformer、基础模型与 **Kernel U-Net (KUN)**。

> 配套内容：[时间序列入门讲义](../course/) · [使用 KUN](../zh/kun/)

## 时间线 (Timeline)

| 章 | 时期 | 主题 | 关键词 |
|----|------|------|--------|
| 序  | [1900–1950](foundations/) | 跨学科源头：数学家 · 物理学家 · 控制论 | Kolmogorov · Wiener · Uhlenbeck · Kalman |
| 1  | [1920s](01/) | 起源：自回归的诞生 | Yule · Slutsky · Walker |
| 2  | [1930s–1940s](02/) | 理论奠基 | Wold 分解 · Wiener–Kolmogorov 预测理论 |
| 3  | [1950s](03/) | 指数平滑的兴起 | Brown · Holt |
| 4  | [1960s](04/) | 状态空间与卡尔曼滤波 | Kalman · Holt–Winters |
| 5  | [1970s](05/) | Box–Jenkins 与 ARIMA 范式 | Box · Jenkins · ARIMA |
| 6  | [1980s](06/) | 波动率与协整 | ARCH · 单位根 · 协整 |
| 7  | [1990s](07/) | 非线性与早期神经网络 | GARCH · RNN · LSTM |
| 8  | [2000s](08/) | 机器学习时代 | SVM · 集成 · 特征工程 |
| 9  | [2010s](09/) | 深度学习革命 | DeepAR · seq2seq · Attention |
| 10 | [2020s](10/) | 大模型、线性回归与 Kernel U-Net | Transformer · DLinear · PatchTST · KUN |

## 阅读约定 (Conventions)

- 每节遵循统一逻辑：**背景 → 问题 → 解决方法 → 效果 → 价值**，并给出关键**公式**与**公式分析**。
- 序章专门梳理数学家、物理学家与控制论/通信工程对时间序列的奠基性贡献。
- 文中年份、人名、论文为编者整理，引用前请再行核对。
- 第 10 章收束于 KUN，呼应 [使用 KUN](../zh/kun/) 的动手教程。
