---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/git/
title: "Git"
no_comments: true
---

> 出自[计算机基础](../cs/) · [基础课总览](../)

**Git** 是一个分布式版本控制工具。它给你的项目拍下一连串「快照」，让你能随时回到任何历史版本、查看每行代码是谁在何时改的、以及多人安全地协作。它是[工程实践](../engineering-practice/)与[可复现性](../reproducibility/)的基础设施。

## 直观理解

把 Git 想成代码的「游戏存档系统」：

- 每次 `commit` 就是**存一个档**，记录此刻所有文件的状态，并附一句说明「我改了什么」。
- 想试个大胆的改动？开一个 `branch`（分支），相当于另存一个平行存档，搞砸了随时丢掉，不影响主线。
- 改坏了？`checkout` 回到之前任何一个存档。
- 多人协作时，每人在自己的分支上干活，最后 `merge`（合并）汇总——Git 会帮你把各自的改动拼起来。

和按日期手动复制 `项目_最终版_v2_真的最终.zip` 相比，Git 让历史**清晰、可回溯、不丢失**。

## 核心要点

Git 有三个关键区域：

- **工作区**：你正在编辑的文件。
- **暂存区（staging）**：用 `git add` 挑出这次想提交的改动。
- **仓库（repo）**：用 `git commit` 永久记录下来。

最常用的命令循环：

```bash
git status                 # 看看改了哪些文件
git add .                  # 把改动放进暂存区
git commit -m "修复窗口切分越界的 bug"   # 存档并写说明
git log --oneline          # 查看历史
git push                   # 推送到远程（如 GitHub）
```

分支与协作：

```bash
git branch feature-kun     # 新建分支
git checkout feature-kun   # 切过去（或 git switch）
git merge feature-kun      # 把它合回主分支
git pull                   # 拉取别人的最新改动
```

## 一个例子

一次典型的「试错」流程：

```bash
# 主分支上代码是好的，我想试个新损失函数
git checkout -b try-new-loss      # 新建并切到实验分支

# ... 改代码、跑实验 ...
git add train.py
git commit -m "实验：换成 Huber 损失"

# 效果不好，干脆放弃整条分支
git checkout main
git branch -D try-new-loss        # 主分支毫发无损

# 如果效果好，就合并进来
# git checkout main && git merge try-new-loss
```

`git diff` 还能精确看到改了哪几行：

```bash
git diff HEAD~1 train.py    # 对比上一个 commit
```

## 在时间序列预测中的意义

做 **KUN / Kernel U-Net** 这类研究时，Git 直接服务于结果的可信度：

- **实验可追溯**：每条实验曲线都对应一个 commit。半年后想复现某个最佳结果，`git checkout <那次的 commit>` 即可回到当时一字不差的代码。
- **对照清晰**：「加了下采样到底有没有用？」用分支做 A/B，`git diff` 一目了然。
- **协作不踩脚**：多人改不同模块互不干扰，合并时冲突也有迹可循。
- **配合复现**：把代码版本（commit 哈希）和配置、随机种子一起记录，就构成了完整的[复现](../reproducibility/)凭证。

实用提醒：用 `.gitignore` 把大数据集、模型权重、`__pycache__` 等排除在外——**Git 管代码，不管几个 G 的数据。**

## 小结

- Git = 代码的版本控制 + 协作系统，核心动作是 `add` → `commit` → `push`。
- 三区：工作区 / 暂存区 / 仓库；分支让你安全地试错。
- 每个 commit 写清楚「改了什么」，历史才有价值。
- 它是[工程实践](../engineering-practice/)和[可复现性](../reproducibility/)的地基——**没有版本控制，就谈不上可信的实验。**

---

[← 计算机基础](../cs/) · [基础课总览](../)
