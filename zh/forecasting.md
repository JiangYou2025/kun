---
updated: "2026-06-03"
lang: zh
ref: forecasting
permalink: /zh/forecasting/
title: "什么是预测？"
lead: "预测，就是用已经知道的过去，去猜还不知道的未来。这一页用图、一个小游戏和几个真实场景帮你建立直觉——方法与公式都放在入门讲义里。"
prev: time-series
next: kun
---

一句话：**预测 (forecasting) = 看着一段历史，往后画出还没发生的部分。**

## 预测在做什么

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="用历史推断未来">
  <defs>
    <marker id="ah-f" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <rect x="404" y="34" width="286" height="214" fill="color-mix(in srgb,var(--accent-2) 8%,transparent)"/>
  <line x1="52" y1="248" x2="694" y2="248" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <line x1="52" y1="248" x2="52" y2="28" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <text x="688" y="270" fill="var(--muted)" font-size="14" text-anchor="end">时间 →</text>
  <text x="44" y="34" fill="var(--muted)" font-size="14" text-anchor="end">值</text>
  <!-- 不确定带 -->
  <polygon points="404,150 466,124 528,110 590,114 652,100 652,132 590,146 528,142 466,156 404,150"
    fill="color-mix(in srgb,var(--accent-2) 16%,transparent)"/>
  <!-- 历史（实线） -->
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="70,210 120,196 170,202 220,176 270,184 320,158 370,166 404,150"/>
  <g fill="var(--accent)">
    <circle cx="70" cy="210" r="3.5"/><circle cx="120" cy="196" r="3.5"/><circle cx="170" cy="202" r="3.5"/>
    <circle cx="220" cy="176" r="3.5"/><circle cx="270" cy="184" r="3.5"/><circle cx="320" cy="158" r="3.5"/>
    <circle cx="370" cy="166" r="3.5"/><circle cx="404" cy="150" r="4"/>
  </g>
  <!-- 预测（虚线） -->
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"
    points="404,150 466,140 528,126 590,130 652,116"/>
  <!-- 现在 -->
  <line x1="404" y1="34" x2="404" y2="248" stroke="var(--accent-2)" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="404" y="28" fill="var(--text)" font-size="13" text-anchor="middle">现在</text>
  <text x="228" y="288" fill="var(--accent)" font-size="13" text-anchor="middle">回看 · 已知的历史</text>
  <text x="548" y="288" fill="var(--accent-2)" font-size="13" text-anchor="middle">预测 · 还没发生</text>
</svg>
<figcaption class="figcap">左边实线是<strong>已知的历史</strong>，到“现在”为止；右边虚线是模型对<strong>未来</strong>的预测。阴影越往右越宽，是因为越远越没把握——好的预测给的是一个<strong>范围</strong>，而不只是一根线。</figcaption>
</figure>

## 来玩一下：你来预测

不用任何公式，先用直觉感受一次。

<div class="game" markdown="0">
  <h3 style="margin-top:0">🎯 猜猜下一个值</h3>
  <p class="hint">观察区里先画出<strong>一个完整的周期</strong>，再画<strong>半个</strong>——看懂规律，把鼠标（或手指）点在“现在”<strong>右侧</strong>，猜下一个值会落在哪里。<strong>共 5 题</strong>，最后给你打个分。</p>
  <svg id="fc-svg" viewBox="0 0 560 280" role="img" aria-label="猜下一个值的小游戏">
    <line x1="34" y1="248" x2="540" y2="248" stroke="var(--muted)" stroke-width="1.3"/>
    <line x1="34" y1="248" x2="34" y2="20" stroke="var(--muted)" stroke-width="1.3"/>
    <g id="fc-dyn"></g>
  </svg>
  <p class="verdict" id="fc-verdict"></p>
  <div class="bar2">
    <button id="fc-next" type="button">下一题 →</button>
    <span class="score" id="fc-score"></span>
  </div>
  <script>
  (function(){
    var NS='http://www.w3.org/2000/svg';
    var svg=document.getElementById('fc-svg'); if(!svg) return;
    var dyn=document.getElementById('fc-dyn');
    var verdict=document.getElementById('fc-verdict');
    var btn=document.getElementById('fc-next');
    var scoreEl=document.getElementById('fc-score');
    var xs=[40,85,130,175,220,265,310,355,400], nowX=424, futX=460, top=28, bot=240;
    // 每条 h 都是「一个完整周期(6点) + 半个周期(3点)」= 9 点；t 即下一个相位的值
    var rounds=[
      {h:[190,200,150,95,90,140, 190,200,150],   t:95,  n:'奶茶店日销量'},
      {h:[200,130,85,150,110,80, 200,130,85],     t:150, n:'每小时客流量'},
      {h:[95,92,98,110,185,195, 95,92,98],         t:110, n:'网站访问量'},
      {h:[140,132,145,158,150,138, 140,132,145],   t:158, n:'机房温度'},
      {h:[200,175,188,150,165,120, 138,90,110],    t:70,  n:'股价'}
    ];
    var MAX=5;
    var idx=0, answered=false, played=0, totErr=0;
    function el(tag,a){var e=document.createElementNS(NS,tag);for(var k in a)e.setAttribute(k,a[k]);return e;}
    function val(y){return Math.round((bot-y)/2);}
    function guide(){return '把点击落在“现在”右侧，猜猜下一个值会落在哪里。（共 '+MAX+' 题）';}
    function render(){
      answered=false; btn.disabled=true; while(dyn.firstChild) dyn.removeChild(dyn.firstChild);
      var r=rounds[idx];
      var pts=xs.map(function(x,i){return x+','+r.h[i];}).join(' ');
      dyn.appendChild(el('polyline',{points:pts,fill:'none',stroke:'var(--accent)','stroke-width':2.6,'stroke-linejoin':'round','stroke-linecap':'round'}));
      xs.forEach(function(x,i){dyn.appendChild(el('circle',{cx:x,cy:r.h[i],r:3.6,fill:'var(--accent)'}));});
      dyn.appendChild(el('line',{x1:nowX,y1:top,x2:nowX,y2:bot,stroke:'var(--accent-2)','stroke-width':1,'stroke-dasharray':'4 3'}));
      var nl=el('text',{x:nowX+4,y:top+12,fill:'var(--muted)','font-size':12}); nl.textContent='现在'; dyn.appendChild(nl);
      var q=el('text',{x:futX,y:140,fill:'var(--muted)','font-size':24,'text-anchor':'middle',id:'fc-q'}); q.textContent='?'; dyn.appendChild(q);
      var lab=el('text',{x:40,y:18,fill:'var(--muted)','font-size':13}); lab.textContent='场景 '+(played+1)+'/'+MAX+'：'+r.n; dyn.appendChild(lab);
    }
    function pt(evt){var p=svg.createSVGPoint();var s=evt.touches&&evt.touches[0]?evt.touches[0]:evt;p.x=s.clientX;p.y=s.clientY;return p.matrixTransform(svg.getScreenCTM().inverse());}
    function answer(evt){
      if(answered || played>=MAX) return;
      var p=pt(evt);
      if(p.x < nowX-12) return;
      if(evt.cancelable) evt.preventDefault();
      var uy=Math.max(top,Math.min(bot,p.y)), r=rounds[idx];
      var q=document.getElementById('fc-q'); if(q) q.parentNode.removeChild(q);
      dyn.appendChild(el('line',{x1:xs[xs.length-1],y1:r.h[r.h.length-1],x2:futX,y2:uy,stroke:'var(--accent-2)','stroke-width':2,'stroke-dasharray':'5 4'}));
      dyn.appendChild(el('circle',{cx:futX,cy:uy,r:6,fill:'none',stroke:'var(--accent-2)','stroke-width':2.4}));
      dyn.appendChild(el('circle',{cx:futX,cy:r.t,r:5,fill:'var(--accent)'}));
      dyn.appendChild(el('line',{x1:futX,y1:uy,x2:futX,y2:r.t,stroke:'#fbbf24','stroke-width':2.4}));
      var tl=el('text',{x:futX+12,y:r.t+4,fill:'var(--accent)','font-size':12}); tl.textContent='真实值'; dyn.appendChild(tl);
      var ul=el('text',{x:futX+12,y:uy+4,fill:'var(--accent-2)','font-size':12}); ul.textContent='你的预测'; dyn.appendChild(ul);
      var err=Math.abs(val(uy)-val(r.t)), pct=Math.round(100*err/Math.max(1,val(r.t)));
      var msg=pct<=5?'神预测！':pct<=15?'很准！':pct<=30?'还不错。':'差了点。';
      answered=true; played++; totErr+=pct;
      if(played<MAX){
        verdict.innerHTML='第 '+played+' 题：差 <b>'+pct+'%</b>。 '+msg+' 点“下一题”继续。';
        scoreEl.textContent='进度 '+played+'/'+MAX+' · 当前平均误差 '+Math.round(totErr/played)+'%';
        btn.textContent='下一题 →'; btn.dataset.mode='next'; btn.disabled=false;
      } else {
        finish(pct,msg);
      }
    }
    function finish(lastPct,lastMsg){
      var avg=Math.round(totErr/MAX), sc=Math.max(0,100-avg), pass=avg<=20;
      verdict.innerHTML='第 '+MAX+' 题：差 <b>'+lastPct+'%</b>。<br>'+(pass
        ? '🎉 <b>通过！</b>5 题平均误差 '+avg+'%，得分 <b>'+sc+'/100</b>。你已经对“预测”有了不错的直觉，可以继续往下读了。'
        : '🔁 <b>再试试。</b>5 题平均误差 '+avg+'%，得分 <b>'+sc+'/100</b>——点“重新开始”，多体会几次规律再过关。');
      scoreEl.textContent='最终得分 '+sc+'/100';
      btn.textContent='重新开始'; btn.dataset.mode='reset'; btn.disabled=false;
    }
    function next(){ idx=(idx+1)%rounds.length; render(); verdict.innerHTML=guide(); }
    function reset(){ idx=0; played=0; totErr=0; scoreEl.textContent=''; render(); verdict.innerHTML=guide(); btn.textContent='下一题 →'; btn.dataset.mode='next'; }
    svg.addEventListener('click',answer);
    svg.addEventListener('touchstart',answer,{passive:false});
    btn.addEventListener('click',function(){ if(btn.dataset.mode==='reset') reset(); else next(); });
    reset();
  })();
  </script>
</div>

玩几局你大概就会发现：**只要前面露出了一个完整的周期，下一个值往往就能照着推出来**——拿“上一个周期里同相位的值”来当预测，这正是预测最朴素、也最难打败的一招（即**季节朴素法**）。而趋势越复杂、规律越弱（比如那条股价），才越难猜。

## 预测无处不在

同一件事——“用过去猜未来”——换上不同的数据，就成了各行各业每天都在做的决定：

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌦️</div>
    <h3>天气 · 气候</h3>
    <p>一场漏报的暴雨能让城市排水瘫痪、航班停飞、农田绝收，单次灾害损失常以数十亿计。气象预报员利用数值天气模型和雷达回波数据，提前 6–72 小时预测降水量和落区，据此发布预警、启动排水泵站、安排航班备降。这套提前部署每年为一个中等城市减少数十亿元的气象灾害损失，全国尺度上占 GDP 的 0.1%–0.3%。</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">⚡</div>
    <h3>用电 · 能源</h3>
    <p>电网供需必须逐秒平衡，一旦失衡就面临大面积跳闸甚至全网崩溃，2021 年德州大停电造成了近 2000 亿美元经济损失。调度员使用负荷预测模型，提前 24 小时预判峰值负荷和风电光伏出力曲线，据此安排火电机组启停、储能充放电时段和跨区调度方案。精准预测让电厂避免了拉闸限电，每年为一个省级电网节省上千万元的调峰燃料费。</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📦</div>
    <h3>销量 · 库存</h3>
    <p>备多了资金压死在仓库、备少了爆款断货丢客户——全球零售业每年因库存失误损失超过 1.1 万亿美元。供应链团队利用时间序列模型预测每个 SKU 未来 1–4 周的销量走势，据此提前下采购单、分配仓间调拨和安排促销节奏。预测准确率每提升 1 个百分点，库存周转率可改善 2%–3%，直接释放数千万的运营资金。</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚗</div>
    <h3>交通 · 出行</h3>
    <p>城市早晚高峰的拥堵每年造成人均数百小时的通勤浪费，仅北京一城的拥堵成本就超千亿元。交通指挥中心利用历史与实时车流数据，提前 30 分钟预测每条路段的流量变化，据此调整信号灯配时、开启潮汐车道和发布分流引导。这些提前安排能将平均通勤时间缩短 10%–15%，每天改善数百万人的出行体验。</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🏥</div>
    <h3>健康 · 疾病</h3>
    <p>传染病暴发时，ICU 床位和呼吸机一旦耗尽，死亡率会成倍跳升——COVID-19 期间多国医疗系统曾因此被击穿。流行病学家利用时间序列和 SIR 类模型预测未来 2–4 周的病例增长趋势，据此提前征调医护、调拨呼吸机和扩建方舱。提前两周的准确预测能让医院从容应对而非被动挤兑，将重症死亡率降低 20%–30%。</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📈</div>
    <h3>金融 · 风险</h3>
    <p>"黑天鹅"事件一旦到来，没有控住仓位的机构可能在一天内爆仓出局——2008 年雷曼兄弟倒闭引发了 22 万亿美元的全球市值蒸发。风控团队利用 GARCH、VaR 等波动率模型预测尾部风险和极端损失概率，据此提前削减杠杆、买入对冲期权和调整保证金水平。准确的风险预测让机构将极端行情下的最大回撤控制在可承受范围内，避免一夜出局。</p>
  </div>
</div>

## 那“怎么预测”呢？

这一页只想让你<strong>看懂、玩懂“预测是什么”</strong>。真正“怎么做”——完整的工作流、必须打败的基线、从经典模型到深度学习、以及如何<strong>诚实地衡量预测好坏</strong>——都整理在系统的入门讲义里：

<div class="note" markdown="1">
- 想要方法与公式：[时间序列入门讲义](../../course/)，其中 [第 7 讲 · 评估](../../course/07/)（指标、切分、回测）和 [第 8 讲 · 基线](../../course/08/) 正是“衡量好坏”和“先打败基线”这两块。
- 想直接上手一个现代模型：翻到下一篇 [使用 KUN](../kun/)。
</div>
