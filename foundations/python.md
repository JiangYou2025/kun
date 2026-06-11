---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/python/
title: "Python"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**Python** 是数据科学与机器学习的主力编程语言。它语法简洁、上手快，拥有 [NumPy](../numpy/)、[Pandas](../pandas/)、PyTorch 等极其丰富的生态。本课程所有动手案例都用 Python。

## 直观理解

如果说[编程](../programming/)是「把想法写成指令」，那 Python 就是一门**特别接近自然语言**的指令语言。它刻意做得简单：

```python
for name in ["张三", "李四"]:
    print(f"你好，{name}")
```

几乎可以照字面读出来——「对名单里的每个名字，打印一句问候」。没有分号、没有花括号，用缩进表示代码块。**正因为门槛低，研究者能把精力放在「想法」而非「和语言搏斗」上**，这也是它成为科学计算事实标准的原因。

但 Python 也有代价：它是**解释型**语言，逐元素的纯 Python 循环很慢——这正是要靠 [NumPy](../numpy/) 的[向量化](../vectorization/)来弥补的地方。

## 核心要点

几个最常用的语言特性：

- **动态类型**：变量不用声明类型，`x = 3` 之后还能 `x = "abc"`。
- **核心数据结构**：列表 `list`、字典 `dict`、集合 `set`、元组 `tuple`（详见[数据结构](../data-structures/)）。
- **列表推导式**：一行生成列表，`[x**2 for x in range(5)]` → `[0,1,4,9,16]`。
- **函数与默认参数**：`def f(x, lr=0.01): ...`。
- **丰富的标准库 + 第三方生态**：`import` 即用。
- **包管理与环境**：用 `pip` 装包，用 `venv`/`conda` 隔离环境（属于[工程实践](../engineering-practice/)）。

## 一个例子

几个 Python 特色语法的小演示：

```python
# 列表推导式 + 条件
evens = [x for x in range(10) if x % 2 == 0]   # [0,2,4,6,8]

# 字典：从时间戳查特征
holiday = {"2026-01-01": "元旦", "2026-05-01": "劳动节"}
print(holiday.get("2026-01-01", "工作日"))      # 元旦
print(holiday.get("2026-03-15", "工作日"))      # 工作日（默认值）

# 元组解包，函数返回多个值
def min_max(xs):
    return min(xs), max(xs)

lo, hi = min_max([3, 7, 1, 9])
print(lo, hi)                                     # 1 9

# f-string 格式化
mae = 0.12345
print(f"测试 MAE = {mae:.3f}")                    # 测试 MAE = 0.123
```

这些写法简洁但表达力很强，是日常处理数据时的高频工具。

## 在时间序列预测中的意义

Python 是这门课从数据到模型的全程载体：

- **数据处理**：[Pandas](../pandas/) 读取、对齐、重采样时间序列。
- **数值计算**：[NumPy](../numpy/) 做切窗口、归一化、FFT 等[向量化](../vectorization/)运算。
- **建模训练**：PyTorch 搭建并训练 **KUN / Kernel U-Net**，在 [GPU](../gpu/) 上加速。
- **可视化与汇报**：Matplotlib 画预测曲线、误差分布。

整条[科学计算栈](../scientific-computing/)都长在 Python 上——**学好 Python，等于拿到了进入时序预测实践的钥匙。**

## 常见误区

- **以为 Python 慢就不能做科学计算**：纯 Python 循环确实慢，但靠 [NumPy](../numpy/) 把计算下沉到 C 层，速度完全够用。
- **缩进不当**：Python 用缩进划分代码块，混用空格和 Tab 会直接报错。
- **可变默认参数的坑**：`def f(x, cache=[])` 里的 `[]` 只创建一次、会被多次调用共享，应改用 `None` 再在函数内初始化。
- **不隔离环境**：所有项目共用一套包，迟早版本打架；养成用 `venv`/`conda` 的习惯。

---

[← 计算机基础](../cs/) · [基础课总览](../)
