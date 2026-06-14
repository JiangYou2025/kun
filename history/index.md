---
updated: "2026-06-03"
layout: history
lang: zh
permalink: /history/
title: "时间序列发展史 · 目录"
lead: "从 1927 年 Yule 的自回归到今天的深度学习与基础模型——时间序列分析与预测的一百年。一篇序章 + 10 章正文，以叙述讲清每个方法的来龙去脉，并写出关键公式、解释其含义。"
---

## 这是什么

一部关于**时间序列 (time series)** 方法演进的百年编年史：从统计学的奠基，到状态空间与 Box–Jenkins 范式，再到机器学习与深度学习的浪潮，直至 Transformer、基础模型与 **Kernel U-Net (KUN)**。

> 配套内容：[时间序列入门讲义](../course/) · [使用 KUN](../zh/kun/)
>
> 三篇并列专题：[史前史与当代应用](../prehistory/) · [时间的本质](../nature-of-time/) · [时间悖论](../paradoxes/)

## 时间线

按**领域**筛选这条百年时间线——数学家奠定理论、物理学家给出随机过程的物理直觉、控制论/通信工程把预测变成可在线递推的工程、计算机科学把它推进到机器学习与深度学习。点击下面的标签只看某一域，点 **全部** 看四域交织的完整脉络。

<div class="tl" markdown="0">
<input class="tl-radio" type="radio" name="tlf" id="tl-all" checked>
<input class="tl-radio" type="radio" name="tlf" id="tl-math">
<input class="tl-radio" type="radio" name="tlf" id="tl-phys">
<input class="tl-radio" type="radio" name="tlf" id="tl-ctrl">
<input class="tl-radio" type="radio" name="tlf" id="tl-cs">
<div class="tl-tabs">
  <label for="tl-all">全部</label>
  <label for="tl-math" class="d-math"><span class="dot"></span>数学家</label>
  <label for="tl-phys" class="d-phys"><span class="dot"></span>物理学家</label>
  <label for="tl-ctrl" class="d-ctrl"><span class="dot"></span>控制论 / 通信</label>
  <label for="tl-cs" class="d-cs"><span class="dot"></span>计算机</label>
</div>
<table class="tl-table">
<thead><tr><th>年份</th><th>领域</th><th>人物</th><th>关键贡献</th><th>章</th></tr></thead>
<tbody>
{% for item in site.data.timeline %}{% case item.domain %}{% when 'math' %}{% assign dlabel = '数学' %}{% when 'phys' %}{% assign dlabel = '物理' %}{% when 'ctrl' %}{% assign dlabel = '控制' %}{% else %}{% assign dlabel = '计算机' %}{% endcase %}<tr class="r-{{ item.domain }}"><td class="yr">{{ item.year }}</td><td><span class="badge d-{{ item.domain }}">{{ dlabel }}</span></td><td><a href="{{ '/history/e/' | append: item.slug | append: '/' | relative_url }}">{{ item.person }}</a></td><td>{{ item.contribution | escape }}</td><td><a href="{{ '/history/' | append: item.chap_url | relative_url }}">{{ item.chap }}</a></td></tr>
{% endfor %}
</tbody>
</table>
</div>

> 上表也是全书的章节导航：每行最右的「章」可直接跳转到对应章节。序章按学科梳理跨越百年的源头（数学 · 物理 · 控制/通信 · 序贯决策 · 科学计算），正文 1–10 章按年代展开。

## 延伸专题

正文是从 1900 年随机过程理论起步的方法主线。下面三篇专题各成一页，从不同侧面环绕这条主线：

- [**时间序列任务史** (Task History)](../tasks/) — 发展史讲工具的进化，这里讲问题的进化：从 3000 年前的洪水预测到今天的多模态时间序列。
- [**时间序列应用** (Applications in the Wild)](../applications/) — 按领域看时间序列如何落地：金融、能源、零售、交通、医疗、气象、工业、信号、地球物理、语言共十个场景。
- [**史前史与当代应用** (Prehistory & Applications)](../prehistory/) — 19 世纪以前人类"看时间序列"的计时、观测与朴素方法，以及时间序列在各领域的应用清单。
- [**时间的本质** (The Nature of Time)](../nature-of-time/) — 哲学、物理、文学对"时间"本身的跨学科追问。
- [**时间悖论** (Paradoxes of Time)](../paradoxes/) — 从芝诺到祖父悖论，那些逼我们把"时间"想清楚的著名悖论。

## 阅读约定

- 每章以叙述的方式讲清来龙去脉，并写出关键**公式**、解释其含义。
- 序章按学科（数学 · 物理 · 控制/通信 · 序贯决策 · 科学计算）梳理跨越百年的源头；另有[史前史与当代应用](../prehistory/)、[时间的本质](../nature-of-time/)、[时间悖论](../paradoxes/)三篇并列专题。
- 文中年份、人名、论文为编者整理，引用前请再行核对。
- 第 10 章收束于 KUN，呼应 [使用 KUN](../zh/kun/) 的动手教程。
