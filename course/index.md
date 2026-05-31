---
layout: lecture
lang: zh
permalink: /course/
title: "时间序列入门 · 讲义目录"
lead: "一门关于时间序列分析与预测的入门课程，共 15 讲。本页只列出框架与标题，内容随后逐讲补充。参考 tsamardzic/nlp_intro 的讲义形式编排。"
---

## 课程简介 (About)

本讲义带你从零开始理解**时间序列 (time series)**：它是什么、如何分析、如何做**预测 (forecasting)**，并最终走到现代深度学习模型，包括本仓库的 **Kernel U-Net (KUN)**。

> 配套站点（中 / 英 / 法）：[时间序列](../zh/time-series/) · [如何预测](../zh/forecasting/) · [使用 KUN](../zh/kun/)

## 讲义目录 (Table of Contents)

| # | 讲题 | 主题 |
|---|------|------|
| 1 | [导论：时间序列与预测任务](01/) | Introduction |
| 2 | [数据：数据集、基准与格式](02/) | Data & benchmarks |
| 3 | [探索性分析与可视化](03/) | EDA & visualization |
| 4 | [成分与分解](04/) | Components & decomposition |
| 5 | [平稳性、差分与变换](05/) | Stationarity & transforms |
| 6 | [自相关：ACF 与 PACF](06/) | Autocorrelation |
| 7 | [评估：指标、切分与回测](07/) | Evaluation |
| 8 | [基线模型](08/) | Baselines |
| 9 | [经典模型：AR / MA / ARIMA / SARIMA](09/) | Classical models |
| 10 | [指数平滑：ETS 与 Holt-Winters](10/) | Exponential smoothing |
| 11 | [特征工程与机器学习模型](11/) | Feature engineering & ML |
| 12 | [深度学习：RNN / LSTM / GRU 与 TCN](12/) | Deep learning |
| 13 | [Transformer 与时间序列](13/) | Transformers |
| 14 | [现代预测模型：DLinear、N-BEATS 与 Kernel U-Net](14/) | Modern forecasters & KUN |
| 15 | [概率预测、多变量与实战流程](15/) | Probabilistic & pipeline |

## 动手案例 (Hands-on notebooks)

配套的可运行 Jupyter 案例（合成数据，克隆即跑）放在仓库的 [`notebooks/`](https://github.com/JiangYou2025/kun/tree/main/notebooks) 目录：

1. [探索与分解](https://github.com/JiangYou2025/kun/blob/main/notebooks/01_explore_and_decompose.ipynb) — 第 3、4 讲
2. [预测基线与评估](https://github.com/JiangYou2025/kun/blob/main/notebooks/02_forecasting_baselines.ipynb) — 第 7、8 讲
3. [滑动窗口神经网络预测（KUN 思想）](https://github.com/JiangYou2025/kun/blob/main/notebooks/03_kun_style_window_forecast.ipynb) — 第 11、14 讲

## 如何使用 (How to use)

- 按顺序阅读，每一讲都建立在前一讲之上。
- 每讲只列**标题与小节框架**，便于先建立全局地图，再逐步填充细节。
- 第 14 讲会落到 **KUN**，并链接到[使用 KUN](../zh/kun/) 的动手教程。
