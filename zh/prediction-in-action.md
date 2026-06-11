---
updated: "2026-06-04"
lang: zh
ref: prediction-in-action
permalink: /zh/prediction-in-action/
title: "一次成功的预测"
lead: "预测的本质是什么？根据已有的观测数据，找到一条规律，然后把它延伸到未看到的地方。这一页用一个炮兵射击小游戏让你亲手体验：调整参数 → 拟合弹道 → 命中目标。"
prev: forecasting
next: math-ml-foundations
---

## 预测 = 拟合 + 外推

上一页我们知道了预测无处不在。但"预测"到底怎么做？

最朴素的思路只有两步：

1. **拟合 (Fit)**：找到一条曲线，尽量穿过已有的数据点。
2. **外推 (Extrapolate)**：把这条曲线延伸到未来，得到预测值。

这和炮兵射击一模一样——你观察到几枚炮弹的落点轨迹，调整大炮的**起始位置**和**发射角度**，让弹道曲线拟合这些观测点，最终命中远处的目标。

## 🎯 炮兵射击：你来预测弹道

<div class="game" markdown="0">
  <h3 style="margin-top:0">调整大炮，命中目标！</h3>
  <p class="hint">画面中有 <strong>蓝色观测点</strong>（已知弹道数据）和一个 <strong>红色靶心</strong>（目标）。拖动滑块调整大炮的<strong>水平位置</strong>和<strong>发射角度</strong>。辅助线只显示前半段弹道——后半段落在哪里，靠你自己判断！共 5 关，噪声逐关加大。</p>

  <canvas id="art-canvas" width="560" height="260" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>

  <div style="display:flex;flex-wrap:wrap;gap:18px;margin:14px 0;align-items:center">
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">大炮水平位置 x₀</span>
      <input type="range" id="art-x0" min="0" max="100" value="0" step="1" style="width:100%">
      <span id="art-x0-val" style="font-size:.85rem;font-weight:600">0</span>
    </label>
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">发射角度 θ</span>
      <input type="range" id="art-angle" min="15" max="80" value="45" step="0.5" style="width:100%">
      <span id="art-angle-val" style="font-size:.85rem;font-weight:600">45°</span>
    </label>
  </div>
  <div class="bar2" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
    <button id="art-fire" type="button" style="padding:8px 24px;font-size:1rem;font-weight:600;border-radius:6px;background:var(--accent);color:var(--bg);border:none;cursor:pointer">🚀 发射！</button>
    <span id="art-msg" style="font-size:.95rem"></span>
    <span id="art-score" style="margin-left:auto;font-size:.9rem;color:var(--muted)"></span>
  </div>

  <script>
  (function(){
    var canvas=document.getElementById('art-canvas');
    if(!canvas)return;
    var ctx=canvas.getContext('2d');
    var W=560,H=260,g=9.8,V0=80;
    var x0S=document.getElementById('art-x0'),angleS=document.getElementById('art-angle');
    var x0V=document.getElementById('art-x0-val'),angleV=document.getElementById('art-angle-val');
    var fireBtn=document.getElementById('art-fire'),msgEl=document.getElementById('art-msg'),scoreEl=document.getElementById('art-score');

    // 每关：真实的 x0 和 angle（速度固定 V0，高度=0）
    var levels=[
      {x0:10, angle:50, name:'第1关 · 精准数据',   nObs:7, noise:1},
      {x0:25, angle:42, name:'第2关 · 轻微抖动',   nObs:6, noise:4},
      {x0:5,  angle:62, name:'第3关 · 噪声加大',   nObs:5, noise:10},
      {x0:35, angle:35, name:'第4关 · 数据稀疏',   nObs:3, noise:12},
      {x0:15, angle:55, name:'第5关 · 极端噪声',   nObs:3, noise:22}
    ];
    var cur=0,total=0,fired=false,sc=1;
    var GND=H-26; // 地面 y 像素

    function rad(d){return d*Math.PI/180;}

    // 从 x0 出发、角度 a、速度 V0、y0=0 的抛物线
    function traj(x0,a){
      var r=rad(a),vx=V0*Math.cos(r),vy=V0*Math.sin(r),pts=[];
      for(var i=0;i<=500;i++){
        var t=i*0.04;
        var x=x0+vx*t, y=vy*t-0.5*g*t*t;
        if(y<0&&i>0){pts.push({x:x,y:0});break;}
        pts.push({x:x,y:y});
      }
      return pts;
    }

    function genLv(){
      var lv=levels[cur], real=traj(lv.x0,lv.angle);
      var nObs=lv.nObs||5, noise=lv.noise||2;
      var n=Math.floor(real.length*0.55),obs=[];
      for(var i=0;i<nObs;i++){
        var idx=Math.floor((i+0.5)*n/nObs);
        var p=real[idx];
        obs.push({x:p.x,y:p.y+(Math.random()-0.5)*noise});
      }
      var last=real[real.length-1];
      // 自动缩放：让整条弹道+靶心都在画面内
      var maxX=0,maxY=0;
      real.forEach(function(p){if(p.x>maxX)maxX=p.x;if(p.y>maxY)maxY=p.y;});
      maxX=Math.max(maxX,last.x)*1.15; // 留 15% 余量给用户偏移
      maxY=maxY*1.2;
      sc=(W-50)/maxX;
      var scY=(H-50)/maxY;
      if(scY<sc) sc=scY;
      return {obs:obs,target:{x:last.x,y:0},real:real,name:lv.name,maxX:maxX};
    }
    var lv=genLv();

    function sx(x){return 25+x*sc;}
    function sy(y){return GND-y*sc;}

    function draw(ut,showR){
      ctx.clearRect(0,0,W,H);
      ctx.save();ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();

      // 地面
      ctx.fillStyle='rgba(94,234,212,0.05)';ctx.fillRect(0,GND,W,H-GND);
      ctx.strokeStyle='#262b38';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,GND);ctx.lineTo(W,GND);ctx.stroke();
      ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';
      ctx.fillText('距离 →',W-50,H-4);

      // 观测点
      lv.obs.forEach(function(p){
        ctx.beginPath();ctx.arc(sx(p.x),sy(p.y),5,0,Math.PI*2);
        ctx.fillStyle='#5eead4';ctx.fill();
        ctx.strokeStyle='#0f1117';ctx.lineWidth=1.5;ctx.stroke();
      });

      // 靶心（在地面上）
      var tx=sx(lv.target.x),ty=GND;
      ctx.beginPath();ctx.arc(tx,ty,12,0,Math.PI*2);ctx.fillStyle='rgba(239,68,68,0.15)';ctx.fill();
      ctx.strokeStyle='#ef4444';ctx.lineWidth=2.5;ctx.stroke();
      ctx.beginPath();ctx.arc(tx,ty,3,0,Math.PI*2);ctx.fillStyle='#ef4444';ctx.fill();
      ctx.fillStyle='#ef4444';ctx.font='bold 10px sans-serif';ctx.fillText('目标',tx+14,ty-4);

      // 大炮（在地面上）
      var cx0=parseFloat(x0S.value),ca=rad(parseFloat(angleS.value));
      var cannonX=sx(cx0);
      // 炮身
      ctx.fillStyle='#e6e8ee';ctx.fillRect(cannonX-6,GND-6,12,6);
      // 炮管
      ctx.beginPath();ctx.moveTo(cannonX,GND-3);
      ctx.lineTo(cannonX+Math.cos(ca)*24,GND-3-Math.sin(ca)*24);
      ctx.strokeStyle='#e6e8ee';ctx.lineWidth=3;ctx.stroke();

      // 预览虚线（只画前半段）
      if(!ut){
        var pv=traj(cx0,parseFloat(angleS.value));
        var half=Math.floor(pv.length/2);
        ctx.setLineDash([5,4]);ctx.strokeStyle='#818cf8';ctx.lineWidth=1.5;ctx.beginPath();
        for(var hi=0;hi<half;hi++){if(hi===0)ctx.moveTo(sx(pv[hi].x),sy(pv[hi].y));else ctx.lineTo(sx(pv[hi].x),sy(pv[hi].y));}
        ctx.stroke();ctx.setLineDash([]);
        if(half>0){var hp=pv[half-1];ctx.fillStyle='#818cf8';ctx.font='bold 16px sans-serif';ctx.fillText('?',sx(hp.x)+6,sy(hp.y)-2);}
      }

      // 发射后轨迹（实线）
      if(ut){
        ctx.strokeStyle='#818cf8';ctx.lineWidth=2.5;ctx.beginPath();
        ut.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();
        var lp=ut[ut.length-1];
        ctx.beginPath();ctx.arc(sx(lp.x),sy(lp.y),5,0,Math.PI*2);ctx.fillStyle='#818cf8';ctx.fill();
      }

      // 真实弹道（答案）
      if(showR){
        ctx.setLineDash([3,3]);ctx.strokeStyle='#5eead4';ctx.lineWidth=1.5;ctx.beginPath();
        lv.real.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();ctx.setLineDash([]);
      }

      ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
      ctx.fillText('第 '+(cur+1)+'/'+levels.length+' 关：'+lv.name,40,16);
      ctx.restore();
    }

    function fitErr(){
      var t=traj(parseFloat(x0S.value),parseFloat(angleS.value)),err=0;
      lv.obs.forEach(function(o){var m=Infinity;t.forEach(function(p){var d=Math.hypot(p.x-o.x,p.y-o.y);if(d<m)m=d;});err+=m;});
      return err/lv.obs.length;
    }

    function upd(){
      x0V.textContent=x0S.value;
      angleV.textContent=angleS.value+'°';
      if(!fired)draw(null,false);
    }
    x0S.addEventListener('input',upd);
    angleS.addEventListener('input',upd);

    function doFire(){
      if(fired)return;fired=true;
      var t=traj(parseFloat(x0S.value),parseFloat(angleS.value));
      var lp=t[t.length-1],dist=Math.abs(lp.x-lv.target.x),fe=fitErr();
      draw(t,true);
      var hs=Math.max(0,100-Math.round(dist)),fs=Math.max(0,100-Math.round(fe*3));
      var rs=Math.round(hs*0.6+fs*0.4);total+=rs;
      var hm=dist<5?'🎯 完美命中！':dist<15?'👍 很接近！':dist<30?'还行，差一点。':'💥 偏了不少。';
      msgEl.innerHTML=hm+' 落点偏差 '+Math.round(dist)+'，拟合误差 '+Math.round(fe)+'。本关 <b>'+rs+'/100</b>';
      if(cur<levels.length-1){
        fireBtn.textContent='下一关 →';
        fireBtn.onclick=function(){cur++;lv=genLv();fired=false;msgEl.innerHTML='';fireBtn.textContent='🚀 发射！';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }else{
        var avg=Math.round(total/levels.length);
        scoreEl.innerHTML='🏆 总分 <b>'+total+'/'+(levels.length*100)+'</b>，平均 '+avg;
        fireBtn.textContent='重新开始';
        fireBtn.onclick=function(){cur=0;total=0;lv=genLv();fired=false;msgEl.innerHTML='';scoreEl.innerHTML='';fireBtn.textContent='🚀 发射！';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }
    }
    fireBtn.onclick=doFire;
    upd();
  })();
  </script>
</div>

## 这和时间序列预测有什么关系？

你刚才做的事，和时间序列预测的本质完全一样：

| 炮兵射击 | 时间序列预测 |
|---------|------------|
| 蓝色观测点 | 历史数据（已知的过去） |
| 调整位置和角度 | 调整模型参数（权重、超参） |
| 抛物线穿过观测点 | 模型拟合历史数据 |
| 抛物线延伸到靶心 | 模型外推到未来 |
| 命中靶心 | 预测准确 |

**三个关键洞察：**

- **参数够用就好。** 两个滑块（位置、角度）就足以描述一条抛物线。时间序列模型也是——参数太多反而会"过拟合"，在训练数据上完美，在新数据上崩溃。
- **观测点的覆盖范围很重要。** 如果所有观测点都挤在起点附近，你很难判断远处的落点。同理，历史数据太短或模式太单一，预测就不可靠。
- **外推越远越难。** 靶心越远，一点角度偏差就会被放大成巨大的落点误差。预测未来也是如此——预测一天后比预测一个月后容易得多。

> 你刚才是用眼睛和手在调参数。但凭什么这条曲线就是对的？下一页我们补上预测背后的**数学与机器学习**地基：用函数描述规律、用优化自动找到最好的曲线、用泛化判断有没有学过头。
