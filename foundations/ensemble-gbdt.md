---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/ensemble-gbdt/
title: "集成学习 / GBDT"
no_comments: true
math: true
---

> 出自[机器学习基础](../ml/) · [基础课总览](../)

**集成学习（ensemble learning）** 的思想是：把很多个**弱模型**组合起来，得到一个远比单个强的模型。其中 **GBDT（梯度提升决策树）**，以及它的工程实现 XGBoost / LightGBM / CatBoost，是**表格数据上最强的基线**，也是时间序列预测的顶尖方法之一。

## 直观理解

一个人可能判断失误，但一群人投票、取平均，往往比任何单个专家都准——这就是**群体智慧（wisdom of crowds）**。集成学习把这个道理用到模型上：单棵[决策树](../decision-tree/)又弱又不稳，但**把许多棵树聪明地组合起来**，错误彼此抵消，整体就又准又稳。

关键在于"怎么组合"。集成有两大流派，思路截然不同：

- **Bagging（装袋）**：让很多模型**并行、独立**地学，再平均/投票——主要目的是**降方差**。
- **Boosting（提升）**：让模型**串行、接力**地学，每一个专门修正前面的错误——主要目的是**降偏差**。

## 两大范式：Bagging vs Boosting

**Bagging（并行，降方差）**

代表是**随机森林（random forest）**。它的两个随机性是精髓：

1. **Bootstrap 采样**：每棵树用一份对训练集"有放回抽样"得到的子集来训练，于是每棵树看到的数据略有不同。
2. **随机特征子集**：每次分裂只从随机选出的一部分特征里挑，强迫不同的树关注不同角度。

这样训练出几百棵彼此**不太相关**的树，预测时分类取多数票、回归取平均。单棵树方差高（不稳），但很多棵独立的树一平均，**方差被大幅压低**，整体非常稳健。

**Boosting（串行，降偏差）**

模型不再独立，而是**一个接一个地接力**：每个新模型都专门去补上前面整体还没学好的地方。它直接攻击**偏差**——把一堆"还差点"的弱模型，逐步雕琢成一个强模型。GBDT 就属于这一派。

（关于偏差与方差的取舍，见[偏差—方差权衡](../bias-variance/)；关于这些模型在整个谱系里的位置，见[模型族](../model-families/)。）

## 原理：梯度提升 GBDT

**梯度提升（gradient boosting）** 是 Boosting 里最成功的[算法](../algorithms/)。核心思想异常优雅：**每一棵新树，去拟合当前模型还没解释掉的那部分误差。**

设当前的集成模型是 $F_{m-1}(x)$，我们训练一棵新树 $h_m(x)$ 去拟合它的**残差 / 负[梯度](../gradient/)**，然后把它加进来：

$$F_{m}(x) = F_{m-1}(x) + \eta\, h_m(x)$$

直觉版（用平方损失时）：第 $m$ 棵树就是去拟合**残差**

$$r_i = y_i - F_{m-1}(x_i)$$

也就是"目前还差多少"。更一般地，它拟合损失函数对当前预测的**负梯度**，所以叫"梯度"提升——这让它能适配各种损失函数（回归、分类、分位数等）。

公式里几个关键超参数：

- **[学习率](../learning-rate/) $\eta$（learning rate）**：每棵树只迈一小步。$\eta$ 小→学得慢但更稳、更不易过拟合，通常配合更多的树。
- **树的数量 $M$（`n_estimators`）**：接力多少棵。太多会过拟合，常配合早停。
- **树的深度（`max_depth`）**：每棵基树通常很浅（弱学习器），靠数量取胜。

注意 $\eta$ 和 $M$ 是一对此消彼长的搭档：**小 $\eta$ + 大 $M$** 往往效果最好，但训练更慢。

## 工程实现与正则化

直接手写 GBDT 很慢，实战几乎都用这三个高度优化的库：

- **XGBoost**：经典、稳健，竞赛常青树。
- **LightGBM**：基于直方图、按叶子生长，**又快又省内存**，大数据首选。
- **CatBoost**：对**类别特征**处理特别好，调参省心。

它们都是**表格数据的强基线**——拿到一份结构化数据，先上一个 GBDT 往往就能得到很难被超越的成绩。

GBDT 表达力极强，所以**防过拟合**是重点（见[正则化](../regularization/)、[过拟合](../overfitting/)）。常用旋钮：

- `learning_rate`（$\eta$）：调小更稳。
- `n_estimators`（$M$）：配合**早停**自动选最佳棵数。
- `max_depth` / `num_leaves`：限制单棵树复杂度。
- `subsample` / `colsample`：每棵树只用一部分样本/特征（把 Bagging 的随机性也引进来），既加速又降方差。

## 一个具体例子（sklearn / lightgbm）

```python
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=2000, n_features=20, noise=10, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

gbdt = GradientBoostingRegressor(
    n_estimators=300,     # M：树的数量
    learning_rate=0.05,   # η：学习率，小步慢走
    max_depth=3,          # 每棵基树很浅
    subsample=0.8,        # 每棵树随机用 80% 样本
    random_state=0,
)
gbdt.fit(Xtr, ytr)
print("测试 MSE:", mean_squared_error(yte, gbdt.predict(Xte)))
```

换成 LightGBM 几乎一样，但在大数据上快得多：

```python
import lightgbm as lgb
model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=31, subsample=0.8)
model.fit(Xtr, ytr)
```

试着把 `learning_rate` 调小、`n_estimators` 调大，体会"小步慢走更稳"的效果。

## 在时间序列预测中的意义（重点）

这是 GBDT 在实战中最闪光的舞台之一。把时间序列变成表格——构造**滞后特征**（$t-1, t-7, t-28$）、**滚动统计**（过去 7 天均值/最大值/标准差）、**日历特征**（星期、月份、节假日）——再喂给 GBDT，就是当今最强的预测套路之一。著名的 **M5 销量预测竞赛**冠军方案核心就是 LightGBM。

它尤其擅长**同时预测很多条相关序列**（比如成千上万个商品/门店）：把所有序列堆成一张大表、用一个 GBDT 一起学，模型能跨序列共享规律，省事又强大。

但有一个和[决策树](../decision-tree/)一模一样的**重要警告**：

> **GBDT 同样不能外推趋势。**

因为它的预测最终落在叶子的均值上，输出**走不出训练见过的范围**。面对长期上涨的序列，它会系统性地**低估未来**。标准对策是：**先去趋势 / 差分，再用 GBDT** 去建模剩下的平稳部分（或单独建一个趋势项，让 GBDT 只学残差里的非线性与季节性）。

最后，评估一定要用**时间序列交叉验证**（按时间顺序滚动切分、只用过去预测未来），**绝不能随机打乱**——否则会用未来信息预测过去，造成数据泄漏、把效果吹得虚高。详见[交叉验证](../cross-validation/)。

## 小结

- **集成学习**把许多弱模型组合成强模型，靠的是**群体智慧**。
- 两大范式：**Bagging**（并行、降方差，如随机森林：bootstrap + 随机特征）vs **Boosting**（串行、降偏差）。
- **GBDT** 是梯度提升：每棵新树拟合**残差/负梯度**，$F_m(x)=F_{m-1}(x)+\eta\,h_m(x)$；关键是**学习率 $\eta$、树数 $M$、深度**，小 $\eta$ + 大 $M$ 常最优。
- 工程实现 **XGBoost / LightGBM / CatBoost** 是**表格数据强基线**；防过拟合靠 `learning_rate`/`n_estimators`/`max_depth`/`subsample`（见[正则化](../regularization/)、[过拟合](../overfitting/)）。
- 时序里在**滞后/滚动/日历特征**上是顶尖方法（M5 冠军），擅长批量预测多条序列。
- **致命警告：不能外推趋势**——常**先去趋势/差分再用 GBDT**，并用**时间序列交叉验证**评估。

[← 机器学习基础](../ml/) · [基础课总览](../)
