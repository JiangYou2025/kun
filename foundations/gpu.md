---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/gpu/
title: "GPU 与并行计算"
no_comments: true
---

> 出自[计算机基础](../cs/) · [深度学习基础](../dl/) · [基础课总览](../)

**GPU（图形处理器）**原本是为渲染游戏画面而生的芯片，它有成千上万个小核心，特别擅长**同时**做大量相似的简单运算——比如[矩阵乘法](../matrix-multiplication/)。这正是训练深度模型的算力来源。

## 直观理解

CPU 和 GPU 的区别，像「几位博士」对「一千名小学生」：

- **CPU** 有少数几个非常强的核心，擅长复杂、有先后依赖的任务——像几位博士，逻辑强、能处理难题，但人少。
- **GPU** 有海量较弱的核心，擅长把同一种简单运算**铺开同时算**——像一千名小学生，每人算一道加法题，瞬间全做完。

[神经网络](../neural-network/)的核心运算是矩阵乘法和加法，**天生可以拆成无数互不依赖的小乘加**。把它们一股脑丢给 GPU 的上千核心并行处理，速度往往比 CPU 快几十到上百倍。这就是「**并行计算**」：把一个大任务切成许多能同时进行的小任务。

## 核心要点

- **并行的前提**：任务之间**互相独立**。矩阵里每个输出元素的计算互不依赖，所以能并行；而像[动态规划](../dynamic-programming/)那样后一步依赖前一步的，就难以并行。
- **[向量化](../vectorization/)是钥匙**：要让 GPU 发力，你得用**整块数组/张量**的运算来表达计算，而不是写 Python 循环。一个 [batch](../batch/) 的样本被堆成一个大张量，一次性算完。
- **显存（VRAM）是瓶颈**：GPU 有自己独立的内存，模型、数据、中间激活都要放进去。显存不够，batch size 就得调小。
- **数据搬运有代价**：CPU 内存 ↔ GPU 显存之间来回拷数据很慢，要尽量减少。

## 一个例子

用 PyTorch 把同一个矩阵乘法分别放在 CPU 和 GPU 上：

```python
import torch, time

A = torch.randn(8192, 8192)
B = torch.randn(8192, 8192)

# 在 CPU 上
t = time.time()
_ = A @ B
print(f"CPU: {time.time() - t:.3f}s")

# 搬到 GPU 上（如果有的话）
if torch.cuda.is_available():
    A_g, B_g = A.cuda(), B.cuda()       # 拷到显存
    torch.cuda.synchronize()
    t = time.time()
    _ = A_g @ B_g                       # 上千核心并行算
    torch.cuda.synchronize()            # 等 GPU 真正算完再计时
    print(f"GPU: {time.time() - t:.3f}s")
```

典型结果是 GPU 比 CPU 快几十倍。注意两个细节：`.cuda()` 把张量搬进显存；`synchronize()` 是因为 GPU 调用是**异步**的，不同步就会把时间算错。

## 在时间序列预测中的意义

训练 **KUN / Kernel U-Net** 这类模型几乎离不开 GPU：

- 一个 [batch](../batch/) 的滑动窗口被堆成 `(batch, 时间步, 特征)` 的张量，卷积/下采样对整批并行计算，GPU 把它们一次吃完。
- 序列越长、模型越深，矩阵运算量越大，GPU 的加速比越明显——CPU 上要训练一天的模型，GPU 上可能一小时搞定。
- 但要喂饱 GPU，代码必须**彻底[向量化](../vectorization/)**：用 [NumPy](../numpy/) / PyTorch 的张量运算，而不是 Python 里逐元素的 `for` 循环，否则上千核心大部分时间在空转。

## 常见误区

- **以为 GPU 自动让一切变快**：只有**可并行、计算密集**的任务才受益。小数据、强依赖的串行逻辑，GPU 反而因数据搬运而更慢。
- **忽略显存上限**：模型太大或 batch 太大会「CUDA out of memory」，需要减小 batch 或用梯度累积。
- **还在写 Python 循环**：循环跑在 CPU 上，GPU 闲着。必须用张量整体运算来表达。
- **忘了同步就计时**：GPU 调用异步返回，测速要先 `synchronize()`。

---

[← 计算机基础](../cs/) · [← 深度学习基础](../dl/) · [基础课总览](../)
