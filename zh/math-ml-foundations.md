---
updated: "2026-06-11"
lang: zh
ref: math-ml-foundations
permalink: /zh/math-ml-foundations/
title: "数学和机器学习基础"
lead: "上一页你亲手拟合了一条弹道——那其实就是机器学习的核心：用数学描述规律、用优化找到最好的规律、用数据把规律学出来。这一页只做个引子，把你领到系统的基础课。"
prev: prediction-in-action
next: linear-autoregression
---

## 预测背后的三件事

炮兵游戏里你不停调角度和力度，直到命中目标。机器学习要做的，就是把这个"调参 → 拟合 → 预测"的循环**自动化**，而这背后是三块地基：

- **用函数描述规律** —— 一条规律就是"输入 → 输出"的映射，参数就是可调的"旋钮"。
- **用优化找到最好的参数** —— 定义一个损失函数衡量好坏，再用梯度下降把它降到最低。
- **用机器学习从数据学规律** —— 关键不是记住训练数据，而是在没见过的数据上也准（泛化，别过拟合）。

> 想要直觉和公式？下面的基础课把每一块都展开讲清楚——这一页不重复，只负责把你送过去。

## 系统补这块地基

这几门[基础课](../../foundations/)是更完整的概念地图，只搭框架、讲概念，按需查阅即可：

- [📐 **数学基础**](../../foundations/math/) —— [微积分](../../foundations/calculus/)、[线性代数](../../foundations/linear-algebra/)、[概率统计](../../foundations/probability-statistics/)、[优化](../../foundations/optimization/)、[信息论](../../foundations/information-theory/)
- [💻 **计算机基础**](../../foundations/cs/) —— [编程](../../foundations/programming/)、[数据结构](../../foundations/data-structures/)与[算法](../../foundations/algorithms/)、[科学计算栈](../../foundations/scientific-computing/)、[工程实践](../../foundations/engineering-practice/)
- [🤖 **机器学习基础**](../../foundations/ml/) —— [监督](../../foundations/supervised-learning/) / [无监督学习](../../foundations/unsupervised-learning/)、[模型族](../../foundations/model-families/)、[训练流程](../../foundations/training-pipeline/)、[泛化](../../foundations/generalization/)与[评估](../../foundations/evaluation-metrics/)
- [🧠 **深度学习基础**](../../foundations/dl/) —— [神经网络](../../foundations/neural-network/)、[反向传播](../../foundations/backpropagation/)、[优化器](../../foundations/optimizer/)、[常见架构](../../foundations/architectures/)、[训练实践](../../foundations/training-practice/)

想要方法与公式的系统讲解，也可以直接看[时间序列入门讲义（17 讲）](../../course/)。

## 为什么这对预测重要

真实的时间序列，既有可预测的规律，也有不可预测的噪声。模型的本事就是**学到规律、忽略噪声**——既不过于简单而漏掉趋势和周期，也不过于复杂而把随机抖动当成规律。现代预测模型（包括后面要讲的 KUN）参数动辄上百万，表达力越强，越要在"学得够"和"别学过头"之间取得平衡。

> 下一页，我们就把这套数学落到第一个具体模型上：用**线性模型**做**自回归预测**。
