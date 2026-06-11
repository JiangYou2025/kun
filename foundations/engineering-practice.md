---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/engineering-practice/
title: "工程实践"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**工程实践**指的是一套让代码**可协作、可复现、可维护**的工作习惯——版本控制、固定随机种子、隔离环境、写测试等。它不改变模型本身，却决定了你的研究能否被别人（和半年后的自己）信任和复用。

## 直观理解

把做机器学习实验想象成开一家厨房：

- 没有工程实践 = 凭感觉炒菜。今天好吃，明天再做却复现不出味道，因为你不记得放了多少盐（随机种子）、用的哪批食材（数据版本）、什么炉灶（依赖版本）。
- 有工程实践 = 标准化菜谱。份量、火候、食材批次都记录在案，**换个人、换个厨房，也能做出一模一样的菜**。

科研和工业界最大的痛点之一就是「**别人跑不出我的结果**」，甚至「**我自己也跑不出上个月的结果**」。工程实践就是来根治这个问题的。

## 核心要点

几个最该养成的习惯：

- **版本控制**：用 [Git](../git/) 记录每一次改动，能回溯、能对比、能多人协作。
- **[可复现性](../reproducibility/)**：固定随机种子，锁定依赖版本，记录数据快照。
- **环境隔离**：用 `venv` / `conda` / Docker 把项目依赖关在独立环境里，避免「在我机器上能跑」。
- **配置与代码分离**：超参数、路径写进配置文件，别硬编码散落各处。
- **写测试与断言**：关键函数加单元测试，关键假设加 `assert`，让 bug 早暴露。
- **日志而非 print**：用 `logging` 分级记录，实验可追溯。

## 一个例子

一段「工程化」的实验脚手架长这样：

```python
import logging, random, json
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")

def set_seed(seed: int = 42):
    """固定所有随机源，保证可复现"""
    random.seed(seed)
    np.random.seed(seed)
    # 若用 torch：torch.manual_seed(seed)

# 配置和代码分离
config = {"seed": 42, "lookback": 96, "horizon": 24, "lr": 1e-3}

def main(cfg):
    set_seed(cfg["seed"])
    logging.info("实验开始，配置：%s", cfg)
    assert cfg["horizon"] > 0, "预测步长必须为正"   # 关键假设显式检查
    # ... 加载数据、训练、评估 ...
    metrics = {"mae": 0.123}
    # 把配置和结果一起存档，方便日后比对
    with open("run.json", "w", encoding="utf-8") as f:
        json.dump({"config": cfg, "metrics": metrics}, f, ensure_ascii=False, indent=2)
    logging.info("完成，指标：%s", metrics)

if __name__ == "__main__":
    main(config)
```

关键不在代码量，而在**每一次实验都能凭存档原样重来**。

## 在时间序列预测中的意义

训练 **KUN / Kernel U-Net** 这类模型时，工程实践尤其要紧：

- **结果可比**：换了模型结构想看是否更好，必须保证种子、数据切分、评估指标完全一致，否则分不清是「真变好」还是「随机波动」。
- **数据切分纪律**：时序数据要**按时间**划分训练/验证/测试，绝不能随机打乱导致「未来信息泄漏」。这条纪律靠工程规范来保证。
- **长实验可恢复**：训练几小时的模型要定期存 checkpoint，崩了能续跑。
- **论文/复现**：把 [Git](../git/) commit、配置、环境一起记录，别人 clone 下来就能复现你的曲线。

## 小结

- 工程实践 = 让代码可协作、可复现、可维护的习惯集合。
- 三根支柱：**[版本控制](../git/)、[可复现性](../reproducibility/)、环境隔离**。
- 它不提高模型精度，但**保证你的精度是可信、可重来的**。
- 在时序里还多一条铁律：**严格按时间切分数据，杜绝信息泄漏。**

---

[← 计算机基础](../cs/) · [基础课总览](../)
