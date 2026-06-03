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
> 三篇并列专题：[史前史与应用](../prehistory/) · [时间的本质](../nature-of-time/) · [时间悖论](../paradoxes/)

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

## 时间序列任务史

上面的时间线讲的是**方法**——模型、算法、理论工具怎样一步步被发明出来。但"方法"终归是为了解决**任务**。下表换一个视角：按时间顺序列出时间序列能够解决的典型任务，以及这些任务最早被提出或首次被有效解决的大致年代。

| 年代 | 任务 | 一句话说明 | 典型方法 |
|------|------|-----------|---------|
| ~前 3000 | 洪水/天象预测 | 尼罗河水位、巴比伦月食周期 | 经验规律、周期表 |
| 1662 | 死亡率预测 (生命表) | Graunt 根据伦敦死亡记录编第一张生命表 | 频率统计 |
| 1682 | 彗星回归预测 | 哈雷预言 76 年后彗星回归 | 轨道力学 + 趋势外推 |
| 1801 | 轨道预测 | 高斯用最小二乘法预测谷神星位置 | 最小二乘法 |
| 1843 | 周期发现 | Schwabe 发现太阳黑子 ~11 年周期 | 目视周期 |
| 1900 | 股价建模 | Bachelier 用随机游走描述巴黎国债 | 布朗运动 |
| 1927 | 经济指标预测 | Yule 用 AR 模型预测太阳黑子数 | AR(p) |
| 1940s | 信号预测 (军事) | Wiener–Kolmogorov 最优线性预滤波 | 谱方法、最优滤波 |
| 1950s | 库存/销售预测 | Brown 指数平滑用于工业库存管理 | SES, Holt–Winters |
| 1960 | 导航/定位跟踪 | 卡尔曼滤波用于阿波罗登月导航 | Kalman Filter |
| 1970 | 宏观经济预测 | Box–Jenkins ARIMA 用于 GDP、通胀预测 | ARIMA / SARIMA |
| 1970s | 语音识别 | HMM 用于电话语音转录 | HMM + Viterbi |
| 1973 | 期权定价 | Black–Scholes 给欧式期权定价 | 几何布朗运动 + Itô |
| 1980s | 风险管理 (VaR) | GARCH 建模波动率聚集 → 估计尾部风险 | ARCH / GARCH |
| 1987 | 多变量协整 | Engle–Granger 做宏观变量长期均衡预测 | 协整 / ECM |
| 1990s | 设备故障预测 | 工厂传感器时间序列 → 预测性维护 | RNN, 规则系统 |
| 1997 | 长序列记忆 | LSTM 解决梯度消失，处理长依赖序列 | LSTM |
| 2000s | 电力负荷预测 | 电网调度需要未来 24h–7d 负荷曲线 | GBDT, SVR, 集成 |
| 2000s | 搜索/广告点击预测 | 互联网公司预测 CTR 随时间变化 | 在线学习、GBDT |
| 2010s | 医疗时间序列 | ICU 生理指标 → 预测脓毒症、死亡率 | LSTM, GRU |
| 2010s | 自动驾驶轨迹预测 | 预测周围车辆/行人未来轨迹 | 序列到序列, GNN |
| 2017 | 全局概率预测 | DeepAR 跨商品/门店联合预测 | 自回归 RNN |
| 2017 | 异常检测 | 服务器/网络流量异常 → 告警 | Autoencoder, LSTM |
| 2019 | 可解释预测 | N-BEATS 做时间序列预测并输出趋势/季节分解 | 残差堆叠 |
| 2020 | 天气预报 (数据驱动) | GraphCast 用数据直接做全球天气预报 | GNN, FNO |
| 2020s | 时间序列分类 | 心电图分类、工业振动信号故障诊断 | Transformer, CNN |
| 2020s | 时间序列生成 | 生成逼真的金融/医疗合成数据 | Diffusion, GAN |
| 2020s | 时间序列问答 | 用自然语言问"下周销量？" → LLM 回答 | LLM + 时间序列嵌入 |
| 2023– | 零样本预测 | 不需要训练，直接对新数据做预测 | TimesFM, Chronos |
| 2024– | 多模态时间序列 | 文本+图像+传感器序列联合建模 | 多模态 Transformer |

> 一个任务往往比首次解决它的方法活得更久——"预测"本身从 3000 年前就开始了，但方法从经验规律走到随机过程、再走到深度学习，换了一遍又一遍。上面的方法时间线讲的是**工具的进化**，这张表讲的是**问题的进化**——或者更准确地说，是人类**用时间序列的视角去理解世界的边界**如何一步步扩大。

## 延伸专题

正文是从 1900 年随机过程理论起步的方法主线。下面三篇专题各成一页，从不同侧面环绕这条主线：

- [**史前史与应用** (Prehistory & Applications)](../prehistory/) — 19 世纪以前人类"看时间序列"的计时、观测与朴素方法，以及时间序列在各领域的应用清单。
- [**时间的本质** (The Nature of Time)](../nature-of-time/) — 哲学、物理、文学对"时间"本身的跨学科追问。
- [**时间悖论** (Paradoxes of Time)](../paradoxes/) — 从芝诺到祖父悖论，那些逼我们把"时间"想清楚的著名悖论。

## 阅读约定

- 每章以叙述的方式讲清来龙去脉，并写出关键**公式**、解释其含义。
- 序章按学科（数学 · 物理 · 控制/通信 · 序贯决策 · 科学计算）梳理跨越百年的源头；另有[史前史与应用](../prehistory/)、[时间的本质](../nature-of-time/)、[时间悖论](../paradoxes/)三篇并列专题。
- 文中年份、人名、论文为编者整理，引用前请再行核对。
- 第 10 章收束于 KUN，呼应 [使用 KUN](../zh/kun/) 的动手教程。
