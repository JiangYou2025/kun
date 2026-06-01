---
layout: history
lang: zh
permalink: /history/
title: "时间序列百年史 · 目录"
lead: "从 1927 年 Yule 的自回归到今天的深度学习与基础模型——时间序列分析与预测的一百年。一篇序章 + 10 章正文，以叙述讲清每个方法的来龙去脉，并写出关键公式、解释其含义。"
---

## 这是什么 (About)

一部关于**时间序列 (time series)** 方法演进的百年编年史：从统计学的奠基，到状态空间与 Box–Jenkins 范式，再到机器学习与深度学习的浪潮，直至 Transformer、基础模型与 **Kernel U-Net (KUN)**。

> 配套内容：[时间序列入门讲义](../course/) · [使用 KUN](../zh/kun/)

## 时间线 (Timeline)

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
<tr class="r-math"><td class="yr">1900</td><td><span class="badge d-math">数学</span></td><td>Bachelier</td><td>随机游走为股价建模：数理金融与布朗运动之始</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1905</td><td><span class="badge d-phys">物理</span></td><td>Einstein · Smoluchowski</td><td>布朗运动理论 → 数学上的 Wiener 过程</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1906</td><td><span class="badge d-math">数学</span></td><td>Markov</td><td>马尔可夫链：无记忆性（AR/HMM/MDP/MCMC 的骨架）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1908</td><td><span class="badge d-phys">物理</span></td><td>Langevin</td><td>Langevin 方程：摩擦项 + 随机力</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1927</td><td><span class="badge d-math">数学</span></td><td>Yule · Walker</td><td>自回归 AR(p)、Yule–Walker 方程</td><td><a href="01/">1</a></td></tr>
<tr class="r-math"><td class="yr">1927</td><td><span class="badge d-math">数学</span></td><td>Slutsky</td><td>Slutsky 效应：滤波制造伪周期</td><td><a href="01/">1</a></td></tr>
<tr class="r-phys"><td class="yr">1930</td><td><span class="badge d-phys">物理</span></td><td>Ornstein · Uhlenbeck</td><td>均值回复随机过程，离散化即 AR(1)</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1933</td><td><span class="badge d-math">数学</span></td><td>Kolmogorov</td><td>概率论公理化、遍历定理（时间均值=系综均值）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1934</td><td><span class="badge d-math">数学</span></td><td>Khinchin</td><td>Wiener–Khinchin 定理：自协方差 ↔ 功率谱</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1934</td><td><span class="badge d-math">数学</span></td><td>Lévy</td><td>Lévy 过程、稳定分布（重尾）、鞅理论奠基</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1938</td><td><span class="badge d-math">数学</span></td><td>Wold</td><td>Wold 分解：平稳过程 = 确定项 + MA(∞)</td><td><a href="02/">2</a></td></tr>
<tr class="r-ctrl"><td class="yr">1940s</td><td><span class="badge d-ctrl">控制</span></td><td>Wiener · Kolmogorov</td><td>最优线性预测 = 条件期望（投影）</td><td><a href="02/">2</a></td></tr>
<tr class="r-math"><td class="yr">1944</td><td><span class="badge d-math">数学</span></td><td>Itô</td><td>随机微积分、Itô 引理 → 连续时间金融的引擎</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1945</td><td><span class="badge d-math">数学</span></td><td>Wald</td><td>序贯分析 / SPRT、最优停时（变点检测之源）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1948</td><td><span class="badge d-ctrl">控制</span></td><td>Wiener</td><td>《控制论》、Wiener–Hopf 最优滤波器</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1949</td><td><span class="badge d-math">数学</span></td><td>Kac · Feynman</td><td>Feynman–Kac / 路径积分：PDE 解 = 路径期望</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1950s</td><td><span class="badge d-cs">计算机</span></td><td>Brown</td><td>简单指数平滑 SES（在线 O(1) 更新）</td><td><a href="03/">3</a></td></tr>
<tr class="r-phys"><td class="yr">1951</td><td><span class="badge d-phys">物理</span></td><td>Hurst</td><td>R/S 重标极差、长程依赖（尼罗河洪水）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1952</td><td><span class="badge d-math">数学</span></td><td>Robbins</td><td>多臂赌博机、序贯实验设计（探索 vs 利用）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1953</td><td><span class="badge d-math">数学</span></td><td>Doob</td><td>鞅理论：公平游戏 → 有效市场 / 无套利定价</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1957</td><td><span class="badge d-ctrl">控制</span></td><td>Holt</td><td>Holt 线性趋势法（水平 + 趋势递推）</td><td><a href="03/">3</a></td></tr>
<tr class="r-ctrl"><td class="yr">1957</td><td><span class="badge d-ctrl">控制</span></td><td>Bellman</td><td>动态规划、Bellman 方程、马尔可夫决策过程</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1960</td><td><span class="badge d-ctrl">控制</span></td><td>Kálmán</td><td>卡尔曼滤波、状态空间模型（预测—更新）</td><td><a href="04/">4</a></td></tr>
<tr class="r-ctrl"><td class="yr">1960</td><td><span class="badge d-ctrl">控制</span></td><td>Winters</td><td>Holt–Winters 季节性指数平滑</td><td><a href="04/">4</a></td></tr>
<tr class="r-math"><td class="yr">1963</td><td><span class="badge d-math">数学</span></td><td>Mandelbrot</td><td>金融收益重尾、分数布朗运动与长记忆</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1963</td><td><span class="badge d-phys">物理</span></td><td>Lorenz</td><td>确定性混沌、洛伦兹吸引子（可预测性极限）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1970</td><td><span class="badge d-cs">计算机</span></td><td>Box · Jenkins</td><td>ARIMA/SARIMA 与三阶段建模方法论</td><td><a href="05/">5</a></td></tr>
<tr class="r-math"><td class="yr">1973</td><td><span class="badge d-math">数学</span></td><td>Black · Scholes · Merton</td><td>期权定价：几何布朗运动 + Itô 引理</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1976</td><td><span class="badge d-math">数学</span></td><td>Malliavin</td><td>Malliavin 微积分：对随机性求导，SDE 密度与 Greeks</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1970s–80s</td><td><span class="badge d-ctrl">控制</span></td><td>Åström · Ljung</td><td>系统辨识：从输入输出拟合 ARX/ARMAX</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1981</td><td><span class="badge d-phys">物理</span></td><td>Takens</td><td>延迟嵌入定理：单变量序列重构相空间</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1982</td><td><span class="badge d-cs">计算机</span></td><td>Engle</td><td>ARCH：让条件方差随时间变化</td><td><a href="06/">6</a></td></tr>
<tr class="r-phys"><td class="yr">1983</td><td><span class="badge d-phys">物理</span></td><td>Grassberger · Procaccia</td><td>关联维数：从序列估计吸引子分形维</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1986</td><td><span class="badge d-cs">计算机</span></td><td>Bollerslev</td><td>GARCH(1,1)：更简洁的波动率模型</td><td><a href="06/">6</a></td></tr>
<tr class="r-cs"><td class="yr">1987</td><td><span class="badge d-cs">计算机</span></td><td>Engle · Granger</td><td>协整、误差修正模型、ADF 单位根检验</td><td><a href="06/">6</a></td></tr>
<tr class="r-cs"><td class="yr">1988–89</td><td><span class="badge d-cs">计算机</span></td><td>Sutton · Barto · Watkins</td><td>强化学习：时序差分 (TD) 与 Q-learning</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1990</td><td><span class="badge d-phys">物理</span></td><td>Sugihara · May</td><td>非线性预测：区分混沌与噪声（后启 CCM 因果）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1994</td><td><span class="badge d-phys">物理</span></td><td>Peng et al.</td><td>DFA 去趋势波动分析：提取长程相关</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1990s</td><td><span class="badge d-cs">计算机</span></td><td>RNN</td><td>循环神经网络、BPTT 与梯度消失问题</td><td><a href="07/">7</a></td></tr>
<tr class="r-cs"><td class="yr">1997</td><td><span class="badge d-cs">计算机</span></td><td>Hochreiter · Schmidhuber</td><td>LSTM：门控 + 细胞状态（常误差环）</td><td><a href="07/">7</a></td></tr>
<tr class="r-math"><td class="yr">1998</td><td><span class="badge d-math">数学</span></td><td>Lyons</td><td>粗糙路径理论 + 路径签名：序列的通用特征映射</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1999</td><td><span class="badge d-phys">物理</span></td><td>Mantegna · Stanley</td><td>经济物理：金融序列的标度律、幂律与胖尾</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2000s</td><td><span class="badge d-cs">计算机</span></td><td>SVR</td><td>支持向量回归：ε-不敏感损失 + 核技巧</td><td><a href="08/">8</a></td></tr>
<tr class="r-cs"><td class="yr">2001</td><td><span class="badge d-cs">计算机</span></td><td>Friedman</td><td>梯度提升 GBDT（函数空间梯度下降）</td><td><a href="08/">8</a></td></tr>
<tr class="r-phys"><td class="yr">2005–10</td><td><span class="badge d-phys">物理</span></td><td>Mezić · Schmid</td><td>Koopman 算子 / 动态模态分解：高维序列的相干模态</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">2014–18</td><td><span class="badge d-math">数学</span></td><td>Gatheral · Jaisson · Rosenbaum</td><td>粗糙波动率：波动率轨迹是 H&lt;½ 的分数布朗运动</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2015–16</td><td><span class="badge d-cs">计算机</span></td><td>DQN · AlphaGo</td><td>深度强化学习（Atari、围棋）= 决策化的序列学习</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2017</td><td><span class="badge d-cs">计算机</span></td><td>Vaswani et al.</td><td>Transformer：自注意力，任意位置直接交互</td><td><a href="09/">9</a></td></tr>
<tr class="r-cs"><td class="yr">2017–19</td><td><span class="badge d-cs">计算机</span></td><td>Amazon DeepAR</td><td>自回归 RNN 概率预测、跨序列全局模型</td><td><a href="09/">9</a></td></tr>
<tr class="r-cs"><td class="yr">2019</td><td><span class="badge d-cs">计算机</span></td><td>N-BEATS</td><td>纯前馈 + 残差堆叠的可解释深度模型</td><td><a href="09/">9</a></td></tr>
<tr class="r-phys"><td class="yr">2019</td><td><span class="badge d-phys">物理</span></td><td>Raissi · Lu</td><td>PINN 物理信息网络、DeepONet 神经算子（解 PDE）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">2020</td><td><span class="badge d-phys">物理</span></td><td>Li et al.</td><td>傅里叶神经算子 FNO：学习函数到函数的映射</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2022</td><td><span class="badge d-cs">计算机</span></td><td>DLinear</td><td>分解 + 单层线性，竟超越复杂 Transformer</td><td><a href="10/">10</a></td></tr>
<tr class="r-cs"><td class="yr">2023</td><td><span class="badge d-cs">计算机</span></td><td>PatchTST</td><td>分块 token + 通道独立，降维并保留局部语义</td><td><a href="10/">10</a></td></tr>
<tr class="r-phys"><td class="yr">2022–23</td><td><span class="badge d-phys">物理</span></td><td>FourCastNet · GraphCast</td><td>数据驱动天气预报 = 全球尺度时空时间序列预测</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">2020s</td><td><span class="badge d-math">数学</span></td><td>Neural CDE · 签名核</td><td>粗糙路径/签名用于不规则、缺失值序列的机器学习</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2020s</td><td><span class="badge d-cs">计算机</span></td><td>Kernel U-Net (KUN)</td><td>层次化 U 形 + 可插拔核（线性/MLP/注意力）</td><td><a href="10/">10</a></td></tr>
<tr class="r-cs"><td class="yr">2020s</td><td><span class="badge d-cs">计算机</span></td><td>TimesFM · Chronos · Moirai</td><td>海量预训练的时间序列基础模型（零样本预测）</td><td><a href="10/">10</a></td></tr>
</tbody>
</table>
</div>

> 上表也是全书的章节导航：每行最右的「章」可直接跳转到对应章节。序章专讲 1900–1950 的数学 / 物理 / 控制论源头，正文 1–10 章按年代展开。

## 阅读约定 (Conventions)

- 每章以叙述的方式讲清来龙去脉，并写出关键**公式**、解释其含义。
- 序章专门梳理数学家、物理学家与控制论/通信工程对时间序列的奠基性贡献。
- 文中年份、人名、论文为编者整理，引用前请再行核对。
- 第 10 章收束于 KUN，呼应 [使用 KUN](../zh/kun/) 的动手教程。
