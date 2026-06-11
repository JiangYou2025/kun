---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/cs/
title: "计算机基础"
lead: "编程、数据结构与算法、科学计算栈与工程实践——把模型真正跑起来所需的计算机功底。只搭框架、讲概念。"
prev: /foundations/math/
next: /foundations/ml/
---

> 这是一张**概念地图**：列出做数据与建模时该会的计算机基本功，深入掌握靠动手练习。

## 1. [编程](../programming/)基础（[Python](../python/)）

数据科学的通用语言。

- **基本类型与[数据结构](../data-structures/)**：数 / 字符串 / 列表 / 字典 / 集合
- **控制流**：条件、循环、函数
- **面向对象与模块**：类、包、导入
- **环境管理**：`venv` / `conda`，依赖与[可复现性](../reproducibility/)

## 2. 数据结构与[算法](../algorithms/)

写出又对又快的代码。

- **核心数据结构**：数组、哈希表、栈 / 队列、树、图
- **复杂度分析（[Big-O](../big-o/)）**：时间与空间代价
- **常见算法**：排序、搜索、递归、[动态规划](../dynamic-programming/)
- **数值稳定性**：浮点误差、溢出与下溢

## 3. 科学计算栈

时间序列与机器学习的日常工具。

- **[NumPy](../numpy/)**：N 维数组与**[向量化](../vectorization/)**运算（比 Python 循环快几个数量级）
- **[Pandas](../pandas/)**：表格 / 时间索引、重采样、对齐
- **Matplotlib**：可视化
- **关键思想**：用**向量化**替代显式循环

```python
import numpy as np
x = np.arange(1000)
y = x ** 2          # 向量化：一行胜过 for 循环
```

## 4. 计算机系统常识

理解性能从何而来。

- **内存与缓存**：数据放在哪决定快慢
- **CPU vs [GPU](../gpu/)**：并行计算为何让深度学习成为可能
- **并行与批处理**：[批量 (batch)](../batch/) 运算的硬件动机
- **存储格式**：CSV / Parquet / 二进制的取舍

## 5. [工程实践](../engineering-practice/)

让工作可复现、可协作。

- **版本控制（[Git](../git/)）**：提交、分支、协作
- **Jupyter Notebook**：交互式探索与展示
- **可复现性**：固定随机种子、记录依赖版本
- **调试与日志**：定位问题，而不是盲改

---

**关键术语：** [Python](../python/)、[数据结构](../data-structures/)、[Big-O 复杂度](../big-o/)、[动态规划](../dynamic-programming/)、[NumPy](../numpy/)、[向量化](../vectorization/)、[Pandas](../pandas/)、[GPU 并行](../gpu/)、[batch](../batch/)、[Git](../git/)、[可复现性](../reproducibility/)。
