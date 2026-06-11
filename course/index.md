---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /course/
title: "时间序列入门 · 讲义目录"
lead: "一门关于时间序列分析与预测的入门课程，共 17 讲。本页只列出框架与标题，内容随后逐讲补充。参考 tsamardzic/nlp_intro 的讲义形式编排。"
---

## 课程简介

本讲义带你从零开始理解**时间序列 (time series)**：它是什么、如何分析、如何做**预测 (forecasting)**，并最终走到现代深度学习模型，包括本仓库的 **Kernel U-Net (KUN)**。

> 配套站点（中 / 英 / 法）：[时间序列](../zh/time-series/) · [如何预测](../zh/forecasting/) · [使用 KUN](../zh/kun/)
>
> 想了解方法的来龙去脉？见 [时间序列发展史](../history/)。
>
> 需要补数学或机器学习的地基？见独立的[基础课](../foundations/)：数学 / 计算机 / 机器学习 / 深度学习。

## 讲义目录

| # | 讲题 | 主题 |
|---|------|------|
| 1 | [导论：时间序列与预测任务](01/) | Introduction |
| 2 | [数据：数据集与如何准备数据](02/) | Data & preparation |
| 3 | [线性模型：拟合与预测](03/) | Linear models |
| 4 | [可视化：分析结果与画图](04/) | Visualization & analysis |
| 5 | [成分与分解](05/) | Components & decomposition |
| 6 | [平稳性、差分与变换](06/) | Stationarity & transforms |
| 7 | [自相关：ACF 与 PACF](07/) | Autocorrelation |
| 8 | [经典模型：AR / MA / ARIMA / SARIMA](08/) | Classical models |
| 9 | [深度学习模型：RNN / LSTM / GRU 与 TCN](09/) | Deep learning models |
| 10 | [Transformer 与时间序列](10/) | Transformers |
| 11 | [Kernel U-Net](11/) | Kernel U-Net |
| 12 | [特殊数据与变换：log 变换（金融 / 社交数据）与指数平滑](12/) | Special data & transforms |
| 13 | [任务与模型选择：不同任务怎么用模型](13/) | Tasks & model selection |
| 14 | [概率预测](14/) | Probabilistic forecasting |
| 15 | [多变量预测](15/) | Multivariate forecasting |
| 16 | [动力系统](16/) | Dynamical systems |
| 17 | [流匹配与扩散](17/) | Flow matching & diffusion |

## 补充专题

- [**波的类型与预测**](wave-types/) —— 用一块可交互的画布认识趋势、周期、衰减、方波、复合波与噪声六种基本波形，以及各自的预测难度。配合第 4、5 讲一起看。

## 动手案例

配套的可运行 Jupyter 案例（合成数据，克隆即跑）放在仓库的 [`notebooks/`](https://github.com/JiangYou2025/kun/tree/main/notebooks) 目录：

1. [探索与分解](https://github.com/JiangYou2025/kun/blob/main/notebooks/01_explore_and_decompose.ipynb) — 第 4、5 讲
2. [预测基线与评估](https://github.com/JiangYou2025/kun/blob/main/notebooks/02_forecasting_baselines.ipynb) — 第 3、4 讲
3. [滑动窗口神经网络预测（KUN 思想）](https://github.com/JiangYou2025/kun/blob/main/notebooks/03_kun_style_window_forecast.ipynb) — 第 9、11 讲

## 如何使用

- 按顺序阅读，每一讲都建立在前一讲之上。
- 每讲只列**标题与小节框架**，便于先建立全局地图，再逐步填充细节。
- 第 11 讲会落到 **KUN**，并链接到[使用 KUN](../zh/kun/) 的动手教程。
