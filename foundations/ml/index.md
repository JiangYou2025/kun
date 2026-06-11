---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/ml/
title: "机器学习基础"
lead: "监督 / 无监督学习、主流模型族、训练流程、泛化与评估——让模型从数据中学习的基本范式。只搭框架、讲概念。"
prev: /foundations/cs/
next: /foundations/dl/
math: true
---

> 这是一张**概念地图**：点出机器学习"在做什么、有哪些工具、怎么算学好了"，深入[算法](../algorithms/)留给专门教材。

## 1. 什么是机器学习？

不显式编写规则，而是**从数据中学习**映射 $f_\theta: X \to y$。

- **[监督学习](../supervised-learning/)**：有标签，学输入到输出（回归 / 分类）
- **[无监督学习](../unsupervised-learning/)**：无标签，找结构（[聚类](../clustering/) / 降维）
- **[强化学习](../reinforcement-learning/)**：与环境交互，最大化累计奖励
- 时间序列预测通常被建模为**监督学习**（过去窗口 → 未来值）

## 2. 主流[模型族](../model-families/)

- **[线性模型](../linear-model/)**：线性 / 逻辑回归——简单、可解释的起点
- **K 近邻 (KNN)**：靠"邻居"投票
- **[决策树](../decision-tree/)**：可解释的 if-else 划分
- **集成方法**：随机森林、[梯度提升](../ensemble-gbdt/) (GBDT / XGBoost)——表格数据的强基线
- **支持向量机 ([SVM](../svm/))**：最大间隔分类
- **聚类与降维**：K-means、[PCA](../pca/)

## 3. [训练流程](../training-pipeline/)

- **[损失函数](../loss-function/)**：回归用 MSE / MAE，分类用[交叉熵](../cross-entropy/)
- **[优化](../optimization/)**：[梯度下降](../gradient-descent/)或解析解，最小化损失
- **数据切分**：训练 / 验证 / 测试
- **[交叉验证](../cross-validation/)**：更稳健的超参选择（**时间序列要用按时间顺序的切分**，不能随机打乱）
- **超参数调优**：网格 / 随机 / 贝叶斯搜索

## 4. [泛化](../generalization/)：核心挑战

目标是在**没见过**的数据上表现好，而非记住训练集。

- **欠拟合**：太简单，高偏差
- **[过拟合](../overfitting/)**：太复杂，记住噪声，高方差
- **[偏差—方差权衡](../bias-variance/)**：找复杂度的平衡点
- **[正则化](../regularization/)**：$\ell_1$ / $\ell_2$、[早停](../early-stopping/)、剪枝——给模型加约束

## 5. [评估指标](../evaluation-metrics/)

- **回归**：MSE、RMSE、MAE、MAPE、$R^2$
- **分类**：准确率、精确率 / 召回率、F1、ROC-AUC
- **关键**：指标要匹配业务目标，并在**测试集**上报告

---

**关键术语：** [监督](../supervised-learning/) / [无监督](../unsupervised-learning/) / [强化学习](../reinforcement-learning/)、[线性模型](../linear-model/)、[决策树](../decision-tree/)、[集成 (GBDT)](../ensemble-gbdt/)、[SVM](../svm/)、[聚类](../clustering/)、[PCA](../pca/)、[损失函数](../loss-function/)、[交叉验证](../cross-validation/)、[过拟合](../overfitting/)、[偏差—方差权衡](../bias-variance/)、[正则化](../regularization/)、[评估指标](../evaluation-metrics/)。
