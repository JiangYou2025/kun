---
updated: "2026-06-04"
lang: zh
ref: wave-types
permalink: /zh/wave-types/
title: "波的类型与预测"
lead: "现实中的时间序列几乎都是多种波形的叠加。认识这些基本波形——趋势、周期、衰减、突变——才能选对预测工具。这一页用可交互的图让你亲手拆解波形。"
prev: prediction-in-action
next: frontier-2026
---

## 为什么要理解波形？

上一页你用抛物线拟合弹道。但现实中的数据很少只有一种形状——股价、温度、用电量、心电图，几乎都是**多种波形叠加**的结果。

理解波形 = 理解数据的"骨架"。骨架看对了，预测就成功了一半。

## 六种基本波形

<div class="game" markdown="0">
<h3 style="margin-top:0">🌊 认识基本波形</h3>
<p class="hint">点击下面的标签切换波形类型，观察它们的形状特点和现实对应。</p>

<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px">
  <button class="wave-btn active" data-wave="sine">正弦波</button>
  <button class="wave-btn" data-wave="trend">趋势</button>
  <button class="wave-btn" data-wave="damped">衰减波</button>
  <button class="wave-btn" data-wave="square">方波</button>
  <button class="wave-btn" data-wave="composite">复合波</button>
  <button class="wave-btn" data-wave="noise">噪声</button>
</div>

<canvas id="wave-canvas" width="700" height="280" style="width:100%;border-radius:10px;border:1px solid var(--border);background:var(--surface)"></canvas>
<p id="wave-desc" style="margin-top:10px;font-size:.93rem;color:var(--muted)"></p>

<style>
.wave-btn{padding:6px 14px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;font-size:.88rem;font-weight:500;transition:all .15s}
.wave-btn.active{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.wave-btn:hover{opacity:0.85}
</style>

<script>
(function(){
  var canvas=document.getElementById('wave-canvas');
  if(!canvas)return;
  var ctx=canvas.getContext('2d');
  var W=700,H=280,mid=H/2;
  var descEl=document.getElementById('wave-desc');
  var btns=document.querySelectorAll('.wave-btn');

  var waves={
    sine:{
      fn:function(x){return Math.sin(x*0.05)*80;},
      color:'#5eead4',
      desc:'📐 正弦波 — 最基础的周期信号。一天内的温度变化、潮汐、交流电都近似正弦。周期固定、幅度恒定，是傅里叶变换的基石：任何周期信号都能拆成正弦波的叠加。预测正弦波只需找到频率和相位，是最"好预测"的类型。',
      pred:'✅ 极易预测：只要确定周期和幅度'
    },
    trend:{
      fn:function(x){return -60+x*0.55+Math.sin(x*0.08)*15;},
      color:'#fbbf24',
      desc:'📈 趋势 — 值随时间持续上升或下降。GDP 增长、全球气温升高、摩尔定律下的芯片性能，都带有明显趋势。趋势可以是线性的、指数的、甚至对数的。预测趋势的关键是判断趋势会持续还是会反转。',
      pred:'⚠️ 中等难度：趋势何时反转是最大不确定性'
    },
    damped:{
      fn:function(x){return Math.sin(x*0.06)*80*Math.exp(-x*0.005);},
      color:'#f0abfc',
      desc:'🔔 衰减波 — 振荡幅度随时间递减。地震后的余震、弹簧阻尼振动、药物在血液中的浓度衰减。物理系统中非常常见。预测衰减波需要同时估计频率和衰减率。',
      pred:'⚠️ 中等难度：频率容易找，衰减率需要足够长的观测'
    },
    square:{
      fn:function(x){return Math.sign(Math.sin(x*0.04))*60;},
      color:'#fb923c',
      desc:'⬜ 方波 — 在两个值之间突然切换。开关信号、工厂排班（白班/夜班）、交通灯周期。方波的特征是变化发生在瞬间，中间保持恒定。预测方波需要找准切换的时间点。',
      pred:'✅ 若周期固定则易预测，不规则切换则难'
    },
    composite:{
      fn:function(x){return Math.sin(x*0.03)*40+Math.sin(x*0.12)*25+x*0.15-30+Math.sin(x*0.007)*50;},
      color:'#818cf8',
      desc:'🎼 复合波 — 多种频率 + 趋势的叠加，这才是现实数据最常见的形态。用电量 = 年周期 + 周周期 + 日周期 + 长期趋势 + 随机波动。分解复合波是时间序列分析的核心技术（傅里叶变换、小波分解、STL 分解等）。',
      pred:'⚠️ 需要分解后分别预测各成分，再合并'
    },
    noise:{
      fn:function(x){return (Math.sin(x*37.7)*43758.5453%1-0.5)*120;},
      color:'#ef4444',
      desc:'🎲 纯噪声 — 完全随机，没有可利用的规律。掷骰子、量子测量、高频股票价格中的微观波动。纯噪声是不可预测的——这是信息论的基本定理。任何声称能预测纯噪声的模型，都是在过拟合。',
      pred:'❌ 不可预测：这是预测的理论边界'
    }
  };

  var curWave='sine';

  function draw(){
    ctx.clearRect(0,0,W,H);
    // 网格
    ctx.strokeStyle='rgba(150,160,180,0.1)';ctx.lineWidth=1;
    for(var i=0;i<W;i+=50){ctx.beginPath();ctx.moveTo(i,0);ctx.lineTo(i,H);ctx.stroke();}
    for(var j=0;j<H;j+=40){ctx.beginPath();ctx.moveTo(0,j);ctx.lineTo(W,j);ctx.stroke();}
    // 中线
    ctx.strokeStyle='rgba(150,160,180,0.3)';ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(0,mid);ctx.lineTo(W,mid);ctx.stroke();ctx.setLineDash([]);

    var w=waves[curWave];
    // 已知部分 (0-70%)
    var split=Math.floor(W*0.7);
    ctx.strokeStyle=w.color;ctx.lineWidth=2.5;ctx.beginPath();
    for(var x=0;x<split;x++){var y=mid-w.fn(x);if(x===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);}
    ctx.stroke();

    // 预测部分 (70-100%)
    ctx.setLineDash([5,4]);ctx.strokeStyle=w.color;ctx.lineWidth=2;ctx.globalAlpha=0.6;ctx.beginPath();
    for(var x2=split;x2<W;x2++){var y2=mid-w.fn(x2);if(x2===split)ctx.moveTo(x2,y2);else ctx.lineTo(x2,y2);}
    ctx.stroke();ctx.setLineDash([]);ctx.globalAlpha=1;

    // 分割线
    ctx.strokeStyle='rgba(150,160,180,0.5)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(split,0);ctx.lineTo(split,H);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
    ctx.fillText('← 已知',split-50,18);ctx.fillText('预测 →',split+8,18);

    descEl.innerHTML=w.desc+'<br><strong>'+w.pred+'</strong>';
  }

  btns.forEach(function(btn){
    btn.addEventListener('click',function(){
      btns.forEach(function(b){b.classList.remove('active');});
      btn.classList.add('active');
      curWave=btn.dataset.wave;
      draw();
    });
  });

  draw();
})();
</script>
</div>

## 从波形到预测策略

不同波形需要不同的预测工具：

| 波形 | 预测难度 | 适合的方法 | 现实例子 |
|------|---------|-----------|---------|
| 正弦波 | ⭐ | 傅里叶分析、三角拟合 | 潮汐、日温差、交流电 |
| 趋势 | ⭐⭐ | 线性回归、指数平滑 | GDP、人口增长、通胀 |
| 衰减波 | ⭐⭐ | 参数化物理模型 | 余震、药物代谢、弹簧振动 |
| 方波 | ⭐⭐ | 变点检测、HMM | 排班、交通灯、设备开关 |
| 复合波 | ⭐⭐⭐ | 分解 + 分别预测（STL、小波） | 用电、销量、气温 |
| 纯噪声 | ⭐⭐⭐⭐⭐ | **不可预测**——只能给出概率分布 | 骰子、量子噪声 |

## 现实数据 = 复合波 + 噪声

几乎所有真实的时间序列，都是**信号（可预测的波形）+ 噪声（不可预测的随机部分）**的混合。

预测要做的事，本质上就是三步：

1. **分解**：把数据拆成趋势、季节性、残差（噪声）。
2. **分别预测**：用适合的方法预测每个成分。
3. **合并**：把预测结果加在一起。

> 这就引出一个问题：2026 年最前沿的预测研究在解决什么问题？下一页带你看看。
