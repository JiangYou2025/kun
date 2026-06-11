---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/reproducibility/
title: "可复现性"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**可复现性**指的是：同一份代码和数据，别人（或换台机器的你）重新运行，能得到**相同的结果**。它靠固定随机种子、锁定环境、记录数据来实现，是科学研究与可信建模的底线。

## 直观理解

想象你发表了一个结论：「KUN 模型把误差降低了 10%」。如果别人照你的代码跑出来却只降了 3%，甚至更差——那这个结论就**不可信**了。

不可复现的常见根源，是实验里藏着许多「随机」和「隐变量」：

- 权重的随机初始化、数据的随机打乱、Dropout 的随机失活；
- 不同版本的库（NumPy 1.24 vs 1.26）算出的数值可能有微小差异；
- 你换了一批数据、改了个超参，却忘了记下来。

**可复现性就是把这些「不确定」一个个钉死**，让结果可以被原样重来。这不是锦上添花，而是科学的基本要求。

## 核心要点

要让实验可复现，至少控制三件事：

- **固定随机种子**：给所有随机源设同一个种子（Python、NumPy、PyTorch、CUDA）。
- **锁定环境**：记录 Python 版本和所有依赖的精确版本（`requirements.txt` / `environment.yml`），最好用 `venv`/`conda`/Docker 隔离。
- **固定数据与切分**：记录数据来源、版本/快照，以及训练/验证/测试的切分方式（用 [Git](../git/) 配合数据版本管理）。

此外还要：记录**配置和超参**、记录代码的 **commit 哈希**、把**结果存档**。这些都属于[工程实践](../engineering-practice/)。

## 一个例子

一段把随机源「钉死」的代码：

```python
import os, random
import numpy as np
import torch

def set_seed(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # 让 cuDNN 走确定性算法（会略慢，但结果可复现）
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
print(np.random.rand(3))     # 每次运行都是同样的三个数

# DataLoader 也要固定打乱顺序
g = torch.Generator(); g.manual_seed(42)
# loader = DataLoader(ds, batch_size=32, shuffle=True, generator=g)
```

只要种子和环境一致，`np.random.rand(3)` 每次都吐出**完全相同**的数——这就是可复现的起点。配合 `pip freeze > requirements.txt` 锁住依赖版本，别人就能在自己机器上复现你的曲线。

## 在时间序列预测中的意义

研究 **KUN / Kernel U-Net** 时，可复现性直接决定结论是否站得住：

- **判断真假改进**：你说新加的下采样模块更好，必须在**完全相同的种子、数据切分、评估指标**下对比，否则分不清是真进步还是随机波动。多跑几个种子、报均值±标准差更可信。
- **杜绝信息泄漏**：时序数据必须**按时间**切分训练/测试，固定切分点；一旦随机打乱，模型「偷看」到未来，结果会虚高且无法在真实场景复现。
- **可被同行验证**：把 commit、配置、种子、环境一起公开，别人 clone 即可重跑——这是论文可信的基础。

## 小结

- 可复现性 = 同样的代码 + 数据，能再次得到同样的结果，是可信实验的底线。
- 三根钉子：**固定随机种子、锁定环境、固定数据与切分**。
- 还要记录配置、[Git](../git/) commit、并把结果存档。
- 时序里额外强调：**按时间切分、杜绝未来信息泄漏**；多种子取均值更稳。

---

[← 计算机基础](../cs/) · [基础课总览](../)
