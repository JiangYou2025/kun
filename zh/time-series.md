---
lang: zh
ref: time-series
permalink: /zh/time-series/
title: "什么是时间序列？"
lead: "一页看懂时间序列长什么样。这里以图为主，只点出最基本的两个词——变量和值。公式与方法（平稳性、自相关、分解、滑动窗口…）放在入门讲义里。"
next: forecasting
---

一句话：**时间序列就是把一个变量的“值”沿着“时间”排成的一条线。** 下面用几张图来看。

## 时间序列长什么样

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="一条时间序列的折线图">
  <defs>
    <marker id="ah-a" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <line x1="52" y1="248" x2="694" y2="248" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-a)"/>
  <line x1="52" y1="248" x2="52" y2="28" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-a)"/>
  <text x="688" y="270" fill="var(--muted)" font-size="14" text-anchor="end">时间 →</text>
  <text x="44" y="34" fill="var(--muted)" font-size="14" text-anchor="end">值</text>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"
    points="72,210 124,190 176,200 228,168 280,150 332,164 384,128 436,140 488,108 540,92 592,104 644,78"/>
  <g fill="var(--accent)">
    <circle cx="72" cy="210" r="3.5"/><circle cx="124" cy="190" r="3.5"/><circle cx="176" cy="200" r="3.5"/>
    <circle cx="228" cy="168" r="3.5"/><circle cx="280" cy="150" r="3.5"/><circle cx="332" cy="164" r="3.5"/>
    <circle cx="384" cy="128" r="3.5"/><circle cx="436" cy="140" r="3.5"/><circle cx="488" cy="108" r="3.5"/>
    <circle cx="540" cy="92" r="3.5"/><circle cx="592" cy="104" r="3.5"/><circle cx="644" cy="78" r="3.5"/>
  </g>
  <line x1="384" y1="128" x2="384" y2="248" stroke="var(--accent-2)" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="384" y1="128" x2="52" y2="128" stroke="var(--accent-2)" stroke-width="1" stroke-dasharray="4 3"/>
  <circle cx="384" cy="128" r="5.5" fill="none" stroke="var(--accent-2)" stroke-width="2"/>
  <text x="398" y="118" fill="var(--text)" font-size="14">一个点 =（时间, 值）</text>
</svg>
<figcaption class="figcap">横轴是<strong>时间</strong>，纵轴是每个时刻测到的<strong>值</strong>。图上每一个点，就是“某个时间”和“那个时间的值”配成的一对。例子无处不在：每日气温、每小时用电量、股票收盘价、每天的就诊人数。</figcaption>
</figure>

## 变量和值

只需要记住两个词：

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 230" role="img" aria-label="变量与值的示意图">
  <defs>
    <marker id="ah-b" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <rect x="20" y="82" width="150" height="60" rx="10" fill="color-mix(in srgb,var(--accent) 14%,transparent)" stroke="var(--accent)"/>
  <text x="95" y="107" fill="var(--text)" font-size="14" text-anchor="middle" font-weight="600">变量</text>
  <text x="95" y="128" fill="var(--muted)" font-size="13" text-anchor="middle">气温 (°C)</text>
  <line x1="174" y1="112" x2="216" y2="112" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-b)"/>
  <text x="232" y="58" fill="var(--muted)" font-size="13">值：</text>
  <g font-size="14" text-anchor="middle">
    <rect x="258" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="280" y="101" fill="var(--text)">12</text>
    <rect x="334" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="356" y="101" fill="var(--text)">14</text>
    <rect x="410" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="432" y="101" fill="var(--text)">13</text>
    <rect x="486" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="508" y="101" fill="var(--text)">16</text>
    <rect x="562" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="584" y="101" fill="var(--text)">18</text>
    <rect x="638" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="660" y="101" fill="var(--text)">21</text>
  </g>
  <g stroke="var(--border)" stroke-dasharray="3 3">
    <line x1="280" y1="112" x2="280" y2="158"/><line x1="356" y1="112" x2="356" y2="158"/><line x1="432" y1="112" x2="432" y2="158"/>
    <line x1="508" y1="112" x2="508" y2="158"/><line x1="584" y1="112" x2="584" y2="158"/><line x1="660" y1="112" x2="660" y2="158"/>
  </g>
  <line x1="232" y1="158" x2="704" y2="158" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-b)"/>
  <g font-size="12" text-anchor="middle" fill="var(--muted)">
    <text x="280" y="178">t₁</text><text x="356" y="178">t₂</text><text x="432" y="178">t₃</text>
    <text x="508" y="178">t₄</text><text x="584" y="178">t₅</text><text x="660" y="178">t₆</text>
  </g>
  <text x="700" y="200" fill="var(--muted)" font-size="13" text-anchor="end">时间 →</text>
</svg>
<figcaption class="figcap"><strong>变量</strong>是你在观察、测量的那个东西（气温、用电量、股价）；<strong>值</strong>是它在每个时间点取到的数字。一条时间序列 = 一个变量，在一连串时间点上的一串值。</figcaption>
</figure>

## 一个变量，还是好几个？

<div class="fig-2" markdown="0">
<figure class="fig">
<svg viewBox="0 0 320 190" role="img" aria-label="单变量时间序列">
  <line x1="30" y1="160" x2="300" y2="160" stroke="var(--muted)" stroke-width="1.3"/>
  <line x1="30" y1="160" x2="30" y2="22" stroke="var(--muted)" stroke-width="1.3"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"
    points="40,128 86,116 132,132 178,100 224,112 270,82 296,92"/>
  <text x="40" y="42" fill="var(--accent)" font-size="13">气温</text>
</svg>
<figcaption class="figcap"><strong>单变量</strong>：只跟踪一个变量。</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 190" role="img" aria-label="多变量时间序列">
  <line x1="30" y1="160" x2="300" y2="160" stroke="var(--muted)" stroke-width="1.3"/>
  <line x1="30" y1="160" x2="30" y2="22" stroke="var(--muted)" stroke-width="1.3"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,128 86,116 132,132 178,100 224,112 270,82 296,92"/>
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,96 86,108 132,90 178,118 224,96 270,120 296,104"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,142 86,134 132,146 178,138 224,150 270,136 296,148"/>
  <g font-size="12">
    <text x="44" y="40" fill="var(--accent)">气温</text>
    <text x="120" y="40" fill="var(--accent-2)">湿度</text>
    <text x="196" y="40" fill="#fbbf24">电力</text>
  </g>
</svg>
<figcaption class="figcap"><strong>多变量</strong>：同时记录好几个常常彼此相关的变量。KUN 正是为多变量场景设计的。</figcaption>
</figure>
</div>

## 数据里常见的几种“形状”

把图看熟，比记定义更重要——大多数序列里都藏着下面这几种形状。

<div class="fig-2" markdown="0">
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="趋势">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="40,128 88,118 136,104 184,90 232,74 288,52"/>
</svg>
<figcaption class="figcap"><strong>趋势</strong>：长期往一个方向走（如逐年增长的人口）。</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="季节性">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="40,82 64,52 88,46 112,68 136,100 160,116 184,108 208,80 232,50 256,46 280,66 300,98"/>
</svg>
<figcaption class="figcap"><strong>季节性</strong>：按固定周期反复（如每年夏天的冰淇淋销量）。</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="噪声">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"
    points="40,92 64,60 88,108 112,72 136,118 160,58 184,104 208,80 232,120 256,64 280,100 300,78"/>
</svg>
<figcaption class="figcap"><strong>噪声</strong>：不规则、抓不住的随机起伏。</figcaption>
</figure>
</div>

## 想再往下看？

<div class="note" markdown="1">
**这一页只为“看懂图”。** 想要真正的技术内容——平稳性、差分、自相关、分解公式、怎么把序列切成训练样本——请看系统的 [时间序列入门讲义](../../course/)。准备好动手预测了，就翻到下一篇 [如何做预测](../forecasting/)。
</div>
