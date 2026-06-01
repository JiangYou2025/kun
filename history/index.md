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
<tr class="r-ctrl"><td class="yr">1948</td><td><span class="badge d-ctrl">控制</span></td><td>Shannon</td><td>信息论：熵、信道容量、Nyquist–Shannon 采样定理</td><td><a href="foundations/">序</a></td></tr>
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
<tr class="r-ctrl"><td class="yr">1967</td><td><span class="badge d-ctrl">控制</span></td><td>Viterbi</td><td>维特比算法：HMM / 卷积码的动态规划解码</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1970</td><td><span class="badge d-cs">计算机</span></td><td>Box · Jenkins</td><td>ARIMA/SARIMA 与三阶段建模方法论</td><td><a href="05/">5</a></td></tr>
<tr class="r-math"><td class="yr">1973</td><td><span class="badge d-math">数学</span></td><td>Black · Scholes · Merton</td><td>期权定价：几何布朗运动 + Itô 引理</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">1976</td><td><span class="badge d-math">数学</span></td><td>Malliavin</td><td>Malliavin 微积分：对随机性求导，SDE 密度与 Greeks</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1970s–80s</td><td><span class="badge d-ctrl">控制</span></td><td>Åström · Ljung</td><td>系统辨识：从输入输出拟合 ARX/ARMAX</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1980</td><td><span class="badge d-ctrl">控制</span></td><td>Cutler · Ramaker</td><td>模型预测控制 MPC：用滚动预测做闭环决策</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1981</td><td><span class="badge d-phys">物理</span></td><td>Takens</td><td>延迟嵌入定理：单变量序列重构相空间</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1982</td><td><span class="badge d-cs">计算机</span></td><td>Engle</td><td>ARCH：让条件方差随时间变化</td><td><a href="06/">6</a></td></tr>
<tr class="r-phys"><td class="yr">1983</td><td><span class="badge d-phys">物理</span></td><td>Grassberger · Procaccia</td><td>关联维数：从序列估计吸引子分形维</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1986</td><td><span class="badge d-cs">计算机</span></td><td>Bollerslev</td><td>GARCH(1,1)：更简洁的波动率模型</td><td><a href="06/">6</a></td></tr>
<tr class="r-cs"><td class="yr">1987</td><td><span class="badge d-cs">计算机</span></td><td>Engle · Granger</td><td>协整、误差修正模型、ADF 单位根检验</td><td><a href="06/">6</a></td></tr>
<tr class="r-cs"><td class="yr">1988–89</td><td><span class="badge d-cs">计算机</span></td><td>Sutton · Barto · Watkins</td><td>强化学习：时序差分 (TD) 与 Q-learning</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1990</td><td><span class="badge d-phys">物理</span></td><td>Sugihara · May</td><td>非线性预测：区分混沌与噪声（后启 CCM 因果）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1993</td><td><span class="badge d-ctrl">控制</span></td><td>Gordon et al.</td><td>粒子滤波 / 序贯蒙特卡洛：非线性非高斯状态估计</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">1994</td><td><span class="badge d-ctrl">控制</span></td><td>Evensen</td><td>集合卡尔曼滤波 EnKF：数值天气预报的数据同化</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1994</td><td><span class="badge d-phys">物理</span></td><td>Peng et al.</td><td>DFA 去趋势波动分析：提取长程相关</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">1990s</td><td><span class="badge d-cs">计算机</span></td><td>RNN</td><td>循环神经网络、BPTT 与梯度消失问题</td><td><a href="07/">7</a></td></tr>
<tr class="r-cs"><td class="yr">1997</td><td><span class="badge d-cs">计算机</span></td><td>Hochreiter · Schmidhuber</td><td>LSTM：门控 + 细胞状态（常误差环）</td><td><a href="07/">7</a></td></tr>
<tr class="r-math"><td class="yr">1998</td><td><span class="badge d-math">数学</span></td><td>Lyons</td><td>粗糙路径理论 + 路径签名：序列的通用特征映射</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">1999</td><td><span class="badge d-phys">物理</span></td><td>Mantegna · Stanley</td><td>经济物理：金融序列的标度律、幂律与胖尾</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2000s</td><td><span class="badge d-cs">计算机</span></td><td>SVR</td><td>支持向量回归：ε-不敏感损失 + 核技巧</td><td><a href="08/">8</a></td></tr>
<tr class="r-cs"><td class="yr">2001</td><td><span class="badge d-cs">计算机</span></td><td>Friedman</td><td>梯度提升 GBDT（函数空间梯度下降）</td><td><a href="08/">8</a></td></tr>
<tr class="r-ctrl"><td class="yr">2001–04</td><td><span class="badge d-ctrl">控制</span></td><td>Jaeger</td><td>回声状态网络 / 储备池计算：低成本预测混沌序列</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">2005–10</td><td><span class="badge d-phys">物理</span></td><td>Mezić · Schmid</td><td>Koopman 算子 / 动态模态分解：高维序列的相干模态</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">2006</td><td><span class="badge d-ctrl">控制</span></td><td>Donoho · Candès · Tao</td><td>压缩感知：稀疏信号的亚奈奎斯特采样与重构</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">2010</td><td><span class="badge d-ctrl">控制</span></td><td>Andrieu et al.</td><td>粒子 MCMC：非线性状态空间模型的参数推断</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">2014–18</td><td><span class="badge d-math">数学</span></td><td>Gatheral · Jaisson · Rosenbaum</td><td>粗糙波动率：波动率轨迹是 H&lt;½ 的分数布朗运动</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2015–16</td><td><span class="badge d-cs">计算机</span></td><td>DQN · AlphaGo</td><td>深度强化学习（Atari、围棋）= 决策化的序列学习</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2017</td><td><span class="badge d-cs">计算机</span></td><td>Vaswani et al.</td><td>Transformer：自注意力，任意位置直接交互</td><td><a href="09/">9</a></td></tr>
<tr class="r-cs"><td class="yr">2017–19</td><td><span class="badge d-cs">计算机</span></td><td>Amazon DeepAR</td><td>自回归 RNN 概率预测、跨序列全局模型</td><td><a href="09/">9</a></td></tr>
<tr class="r-cs"><td class="yr">2019</td><td><span class="badge d-cs">计算机</span></td><td>N-BEATS</td><td>纯前馈 + 残差堆叠的可解释深度模型</td><td><a href="09/">9</a></td></tr>
<tr class="r-phys"><td class="yr">2019</td><td><span class="badge d-phys">物理</span></td><td>Raissi · Lu</td><td>PINN 物理信息网络、DeepONet 神经算子（解 PDE）</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-phys"><td class="yr">2020</td><td><span class="badge d-phys">物理</span></td><td>Li et al.</td><td>傅里叶神经算子 FNO：学习函数到函数的映射</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">2020–21</td><td><span class="badge d-ctrl">控制</span></td><td>Gu et al. (HiPPO · S4)</td><td>深度状态空间模型：Kalman 状态空间反超 Transformer</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2022</td><td><span class="badge d-cs">计算机</span></td><td>DLinear</td><td>分解 + 单层线性，竟超越复杂 Transformer</td><td><a href="10/">10</a></td></tr>
<tr class="r-cs"><td class="yr">2023</td><td><span class="badge d-cs">计算机</span></td><td>PatchTST</td><td>分块 token + 通道独立，降维并保留局部语义</td><td><a href="10/">10</a></td></tr>
<tr class="r-phys"><td class="yr">2022–23</td><td><span class="badge d-phys">物理</span></td><td>FourCastNet · GraphCast</td><td>数据驱动天气预报 = 全球尺度时空时间序列预测</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-ctrl"><td class="yr">2023</td><td><span class="badge d-ctrl">控制</span></td><td>Mamba (Gu · Dao)</td><td>选择性状态空间模型：线性时间扫描的长序列建模</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-math"><td class="yr">2020s</td><td><span class="badge d-math">数学</span></td><td>Neural CDE · 签名核</td><td>粗糙路径/签名用于不规则、缺失值序列的机器学习</td><td><a href="foundations/">序</a></td></tr>
<tr class="r-cs"><td class="yr">2020s</td><td><span class="badge d-cs">计算机</span></td><td>Kernel U-Net (KUN)</td><td>层次化 U 形 + 可插拔核（线性/MLP/注意力）</td><td><a href="10/">10</a></td></tr>
<tr class="r-cs"><td class="yr">2020s</td><td><span class="badge d-cs">计算机</span></td><td>TimesFM · Chronos · Moirai</td><td>海量预训练的时间序列基础模型（零样本预测）</td><td><a href="10/">10</a></td></tr>
</tbody>
</table>
</div>

> 上表也是全书的章节导航：每行最右的「章」可直接跳转到对应章节。序章按学科梳理跨越百年的源头（数学 · 物理 · 控制/通信 · 序贯决策 · 科学计算），正文 1–10 章按年代展开。

## 史前史与应用 (Prehistory & Applications)

上面的时间线从 1900 年的随机过程理论起步。但人类"看时间序列"的历史要久远得多——在严格的方法之前，先有了**零散的长期观测**与**朴素的周期/趋势方法**。下面两张清单分别梳理 **19 世纪末以前的史前史**，以及时间序列在各领域的**应用**。

### 史前史：19 世纪以前 (Prehistory)

上面的时间线从 1900 年的随机过程理论起步，但人类"看时间序列"的历史要久远得多。它分三股先后涌现：先是**为度量时间而生的计时与历法**（日晷、水钟、历法），随后是**漫长的观测积累**（天文、水文、人口、物价的长期记录），最后到 17–19 世纪才出现**朴素的方法**（生命表、折线图、谐波分析、最小二乘、移动平均），并在 1898 年 Schuster 的**周期图**处与现代谱分析接轨。下表用「类别」列把三者区分开。

| 年代 | 类别 | 人物 / 文明 | 探索（零散的数据或方法） |
|------|------|------------|--------------------------|
| ~前 3000 | 计时·历法 | 古埃及 / 美索不达米亚 | **日晷、水钟、阴阳历**：把时间切成可计量的单位 |
| ~前 3000–2000 | 观测 | 巨石阵 (Stonehenge) | 巨石对准至日，追踪太阳的周年回归 |
| ~前 1600 | 观测 | 巴比伦 | **天文日记**：系统记录行星位置与日月食（历法与天象预测） |
| 古代起 | 观测 | 古埃及 | **尼罗河水位计 (Nilometer)**：逐年记录洪水水位，跨千年的环境序列 |
| 前 800– | 观测 | 中国史官 | **太阳黑子、彗星、日食、地震**的连续记录——现存最长观测序列之一 |
| ~前 150 | 方法 | Hipparchus 喜帕恰斯 | 比对跨世纪观测，发现**岁差**；编制星表 |
| ~前 100 | 计时·方法 | 安提基特拉机械 | 以齿轮模拟天体、预测日月食的"古代计算机" |
| ~150 | 方法 | Ptolemy 托勒密 | 《天文学大成》**本轮模型**：周期叠加预测行星运动 |
| ~800–900 | 观测 | 玛雅 | **德累斯顿抄本**：金星与日食表、长计历 |
| 1088 | 计时 | 苏颂（水运仪象台） | 水力驱动的中国天文钟：连续报时与天象 |
| 1213 | 方法 | 中世纪欧洲 | **伦敦桥潮汐表**：最早的潮汐预测表之一 |
| 1582 | 计时·历法 | 格里高利历 | 校正历法漂移，统一长期时间标度 |
| 1580s | 观测 | Tycho Brahe 第谷 | 数十年**精密连续**的行星位置观测 |
| 1609 | 方法 | Kepler 开普勒 | 从第谷数十年的**火星位置序列**中归纳出行星运动三定律 |
| 1610 | 观测 | Galileo 伽利略 | **逐夜记录木星四卫星的位置**——一份经典的早期时间序列数据集；并观测太阳黑子移动、以摆计时 |
| 1656 | 计时 | Huygens 惠更斯 | **摆钟**：把计时精度提升一个数量级 |
| 1662 | 方法 | John Graunt | 《死亡数字观察》：首张**生命表**，分析伦敦死亡序列 |
| 1693/1705 | 方法 | Halley 哈雷 | 生命表；并据历史记录预言**哈雷彗星**的回归周期 |
| 1786 | 方法 | William Playfair | 发明**折线图**：第一次把数据画成"随时间变化的曲线" |
| 1807/1822 | 方法 | Fourier 傅里叶 | **谐波分析**：把周期信号分解为正弦叠加 |
| 1805/1809 | 方法 | Legendre · Gauss | **最小二乘**：用观测序列拟合天体轨道（谷神星） |
| 1835 | 方法 | Quetelet 凯特勒 | "**社会物理学**"：把统计平均用于社会与人口序列 |
| 1843 | 观测·方法 | Schwabe | 发现约 **11 年的太阳黑子周期** |
| 1847 | 方法 | Buys-Ballot | **周期检测表**：从序列中寻找隐藏周期 |
| 1848– | 观测 | Wolf 沃尔夫 | **沃尔夫太阳黑子数**序列（后来正是 Yule 建模的对象） |
| 1854 | 方法·应用 | John Snow · William Farr | 霍乱与死亡的**时序统计**，公共卫生序列分析的雏形 |
| 1862/1875 | 方法 | Jevons · Juglar | **经济周期**、商业波动，乃至太阳黑子—景气假说 |
| 1876 | 方法·计算 | Kelvin (W. Thomson) | **潮汐预测机**：用谐波分析机械合成潮汐序列 |
| 1884 | 方法 | Poynting | 用**移动平均**平滑价格序列、剥离趋势 |
| 1886 | 方法 | Galton | **回归**与"回归到均值" |
| 1898 | 方法 | Schuster | 发明**周期图 (periodogram)**：检验隐藏周期——直通 20 世纪谱分析 |

> 史前史的逻辑是**观测先行、方法零散**：先有计时与历法把时间量化，再有天文/水文/人口/物价的长期记录积累数据，最后谐波分析、最小二乘、移动平均、周期图等给出最早的工具。它们在 1900 年后被随机过程理论统一，正式开启[上面的百年时间线](#时间线-timeline)。

### 应用领域 (Applications)

| 领域 | 典型应用 | 关联方法 / 章节 |
|------|---------|------------------|
| 天文 · 地球物理 | 行星轨道、太阳黑子、潮汐、地震 | 谐波分析、周期图（史前史） |
| 气象 · 气候 | 天气预报、气候变化、厄尔尼诺 | 数据同化（EnKF）、神经算子（[序](foundations/)） |
| 经济 · 金融 | GDP、通胀、股价、波动率、风险管理 | ARIMA（[5](05/)）、GARCH（[6](06/)）、随机微积分 |
| 工业 · 控制 | 质量控制、过程监控、预测性维护 | 状态空间、卡尔曼滤波、MPC（[4](04/)、[序](foundations/)） |
| 能源 | 电力/燃气负荷、可再生能源出力预测 | 指数平滑（[3](03/)）、深度学习（[9](09/)） |
| 零售 · 供应链 | 需求预测、库存补货、动态定价 | 全局模型 DeepAR、强化学习（[9](09/)、[序](foundations/)） |
| 通信 · 信号 | 语音编码、信道均衡、雷达跟踪 | LPC、Wiener/Kalman 滤波、Viterbi（[序](foundations/)） |
| 医学 · 生理 | 心率、脑电、流行病传播 | DFA、HMM、序列模型（[序](foundations/)、[7](07/)） |
| 交通 · 城市 | 车流、轨迹预测、时空预测 | 图神经网络、时空模型 |
| 自然语言 · 序列 | 语言模型、序列标注、生成 | RNN/LSTM（[7](07/)）、Transformer（[9](09/)） |

## 时间的本质：跨学科的探索 (The Nature of Time)

本书讲的是**时间序列**——沿时间排列的数据。但"时间"本身究竟是什么？这个问题比任何序列都古老，也吸引着哲学家、物理学家与文学家不断追问。下表是一份横跨**哲学、理论物理、文学与文化**的小小巡礼，作为对"时间"的一次致敬——它远比"测量时间上的数据"更深刻。

| 年代 | 类别 | 人物 / 作品 | 对"时间"的探索 |
|------|------|------------|------------------|
| 上古 | 文化·宗教 | 印度教 / 佛教宇宙观 | **循环时间**：劫 (kalpa)、轮回——时间周而复始，而非单向 |
| ~前 500 | 哲学 | Heraclitus 赫拉克利特 | "万物流变"：人不能两次踏进同一条河，时间即流变 |
| ~前 450 | 哲学 | Zeno 芝诺悖论 | 阿基里斯追龟：时间与运动的**无限可分** |
| ~前 350 | 哲学 | Aristotle 亚里士多德 | 《物理学》：时间是"运动按先后的计数与度量" |
| ~400 | 哲学 | Augustine 奥古斯丁 | 《忏悔录》：时间是心灵的延展、主观的流逝 |
| 1687 | 物理 | Newton 牛顿 | **绝对时间**：均匀流逝，独立于万物 |
| ~1715 | 哲学 | Leibniz 莱布尼茨 | **关系时间**：时间只是事件的先后秩序（反牛顿绝对时间）|
| 1781 | 哲学 | Kant 康德 | 时间是**先验的直观形式**，而非事物本身的属性 |
| 1850s | 物理 | Clausius · Boltzmann | **时间之箭**：熵增给出时间的方向性 |
| 1889 | 哲学 | Bergson 柏格森 | **绵延 (la durée)**：体验的时间 ≠ 钟表的空间化时间 |
| 1895 | 文学 | H.G. Wells《时间机器》 | 把时间设想为**第四维度**，开创时间旅行叙事 |
| 1905/1915 | 物理 | Einstein 爱因斯坦 | **相对论**：时间相对、同时性相对、引力使时间变慢；时空合一 |
| 1908 | 物理 | Minkowski 闵可夫斯基 | **四维时空**：空间与时间融为一个连续体 |
| 1908 | 哲学 | McTaggart | 《时间的非实在性》：A 序列(过去/现在/未来) vs B 序列(先/后) |
| 1913–27 | 文学 | Proust《追忆似水年华》 | 非自主记忆与**主观时间**的文学探索 |
| 1916 | 物理 | Schwarzschild · 黑洞 | 事件视界处时间的奇异行为；视界内时空角色互换 |
| 1927 | 哲学 | Heidegger《存在与时间》 | **时间性**作为"此在"(Dasein) 存在的根基 |
| 1931 | 艺术 | Dalí《记忆的永恒》 | 融化的钟表：时间的流动与主观性 |
| 1941 | 文学 | Borges《小径分岔的花园》 | **分岔 / 多重时间**，预示多世界叙事 |
| 1949 | 物理 | Gödel 哥德尔 | 旋转宇宙的广义相对论解：允许**闭合类时曲线**（时间旅行）|
| 1960s– | 物理 | 量子引力 · Wheeler–DeWitt | "时间问题"：基础物理层面，时间或许并不存在 |
| 1974/1988 | 物理 | Hawking 霍金 | 黑洞辐射、虚时间、《时间简史》、宇宙无边界 |
| 2017 | 物理 | Rovelli《时间的秩序》 | 圈量子引力：时间是**涌现的**，并非基本量 |

> 从循环到线性、从绝对到相对、从客观钟表到主观绵延、从热力学之箭到量子引力中"时间并不基本"——对时间本质的追问至今没有定论。而时间序列分析，只是在这条更宏大的追问之下，谦卑地处理"时间上的数据"。

## 阅读约定 (Conventions)

- 每章以叙述的方式讲清来龙去脉，并写出关键**公式**、解释其含义。
- 序章按学科（数学 · 物理 · 控制/通信 · 序贯决策 · 科学计算）梳理跨越百年的源头；上方另设**史前史**与**应用**两张独立清单。
- 文中年份、人名、论文为编者整理，引用前请再行核对。
- 第 10 章收束于 KUN，呼应 [使用 KUN](../zh/kun/) 的动手教程。

## 时间悖论 (Paradoxes of Time)

作为收尾——既然聊了时间的本质，就不能不提那些让哲学家与物理学家头疼了两千年的**时间悖论**。它们大多并非真正的矛盾，而是逼我们把"时间"想得更清楚。

| 悖论 | 领域 | 内容 | 解答 / 意义 |
|------|------|------|-------------|
| 飞矢不动 (Zeno) | 哲学 | 每一瞬间箭都静止，运动如何可能？ | 极限与微积分：瞬时速度的严格定义 |
| 阿基里斯追龟 (Zeno) | 哲学 | 追赶者似乎永远要先到对方的旧位置 | 无穷级数收敛：无限步可在有限时间完成 |
| 双生子佯谬 | 物理 · 狭义相对论 | 远行的双胞胎归来时更年轻 | 加速参考系不对称，并非真矛盾 |
| 谷仓–杆 (梯子) 悖论 | 物理 · 狭义相对论 | 长杆能否装进短谷仓？ | **同时性的相对性** |
| Loschmidt 可逆性佯谬 | 物理 · 热力学 | 可逆的微观定律为何给出不可逆的熵增？ | 统计性 + 低熵初始条件——**时间之箭** |
| 麦克斯韦妖 | 物理 · 热力学 | "妖"能否违反第二定律？ | 信息擦除必耗能（Landauer 原理）|
| 玻尔兹曼大脑 | 物理 · 宇宙学 | 随机涨落更易造出孤立大脑而非整个宇宙 | 对宇宙学初始条件的诘问 |
| 祖父悖论 | 时间旅行 | 回到过去杀死祖父，自己便不存在 | Novikov 自洽性 / 多世界分支 |
| 命定悖论 | 时间旅行 | 阻止过去的努力反而促成了它 | 自洽的因果回路 |
| 引导 / 自举悖论 | 时间旅行 | 信息或物体没有起源（因果闭环）| 信息究竟从何而来？ |
| 超光速反向电话 | 物理 · 相对论 | 超光速信号可向过去发信，破坏因果 | 因果律禁止超光速传递信息 |
| 时序保护猜想 | 物理 | 物理定律是否自动禁止时间旅行？ | Hawking："历史不可被改写" |
| McTaggart 悖论 | 哲学 | A 序列(过去/现在/未来)蕴含矛盾 | 推论："时间并不实在" |
| Newcomb 悖论 | 决策论 | 面对完美预测者，该拿一个还是两个盒子？ | 自由意志 vs 预测 / 决定论 |

> 多数悖论的"解"不是取消问题，而是**澄清概念**：芝诺催生了极限与微积分，可逆性佯谬逼出了统计力学与时间之箭，祖父悖论把"时间旅行"逼到自洽因果或多世界的墙角。时间序列只在时间轴上排数据，而这些悖论提醒我们：那根"时间轴"本身，远没有看上去那么理所当然。
