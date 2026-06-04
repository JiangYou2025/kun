---
updated: "2026-06-04"
lang: zh
ref: prediction-in-action
permalink: /zh/prediction-in-action/
title: "一次成功的预测"
lead: "预测的本质是什么？根据已有的观测数据，找到一条规律，然后把它延伸到未看到的地方。这一页用一个炮兵射击小游戏让你亲手体验：调整参数 → 拟合弹道 → 命中目标。"
prev: forecasting
next: wave-types
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
  <p class="hint">画面中有 <strong>蓝色观测点</strong>（已知弹道数据）和一个 <strong>红色靶心</strong>（目标）。拖动滑块调整<strong>发射角度</strong>、<strong>速度</strong>和<strong>高度</strong>，让抛物线穿过蓝色点并命中靶心。点击"发射"看结果。共 3 关。</p>

  <canvas id="art-canvas" width="560" height="280" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>

  <div style="display:flex;flex-wrap:wrap;gap:18px;margin:14px 0;align-items:center">
    <label style="flex:1;min-width:200px">
      <span style="font-size:.9rem;color:var(--muted)">发射角度 θ</span>
      <input type="range" id="art-angle" min="20" max="75" value="45" step="0.5" style="width:100%">
      <span id="art-angle-val" style="font-size:.85rem;font-weight:600">45°</span>
    </label>
    <label style="flex:1;min-width:200px">
      <span style="font-size:.9rem;color:var(--muted)">发射速度 v₀</span>
      <input type="range" id="art-speed" min="60" max="160" value="100" step="1" style="width:100%">
      <span id="art-speed-val" style="font-size:.85rem;font-weight:600">100</span>
    </label>
    <label style="flex:1;min-width:200px">
      <span style="font-size:.9rem;color:var(--muted)">发射高度 y₀</span>
      <input type="range" id="art-y0" min="0" max="120" value="20" step="1" style="width:100%">
      <span id="art-y0-val" style="font-size:.85rem;font-weight:600">20</span>
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
    var W=560,H=280,g=9.8,scale=1.8;
    var angleS=document.getElementById('art-angle'),speedS=document.getElementById('art-speed'),y0S=document.getElementById('art-y0');
    var angleV=document.getElementById('art-angle-val'),speedV=document.getElementById('art-speed-val'),y0V=document.getElementById('art-y0-val');
    var fireBtn=document.getElementById('art-fire'),msgEl=document.getElementById('art-msg'),scoreEl=document.getElementById('art-score');

    var levels=[
      {angle:42,speed:85,y0:20,name:'平原射击'},
      {angle:55,speed:70,y0:40,name:'高地射击'},
      {angle:35,speed:100,y0:8,name:'远程轰炸'}
    ];
    var cur=0,total=0,fired=false;

    function rad(d){return d*Math.PI/180;}
    function traj(a,v,y0,n){
      var r=rad(a),vx=v*Math.cos(r),vy=v*Math.sin(r),pts=[];
      for(var i=0;i<=n;i++){var t=i*0.06;var x=vx*t,y=y0+vy*t-0.5*g*t*t;if(y<0){pts.push({x:x,y:0});break;}pts.push({x:x,y:y});}
      return pts;
    }
    function genLv(){
      var lv=levels[cur],real=traj(lv.angle,lv.speed,lv.y0,300);
      var n=Math.floor(real.length*0.55),obs=[];
      for(var i=0;i<5;i++){var idx=Math.floor((i+0.5)*n/5);var p=real[idx];obs.push({x:p.x+(Math.random()-0.5)*3,y:p.y+(Math.random()-0.5)*3});}
      var last=real[real.length-1];
      return {obs:obs,target:{x:last.x,y:0},real:real,name:lv.name};
    }
    var lv=genLv();
    function sx(x){return 30+x*scale;}
    function sy(y){return H-26-y*scale;}

    function draw(ut,showR){
      ctx.clearRect(0,0,W,H);
      // 地面
      ctx.fillStyle='rgba(94,234,212,0.06)';ctx.fillRect(0,H-24,W,24);
      ctx.strokeStyle='#262b38';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,H-24);ctx.lineTo(W,H-24);ctx.stroke();
      ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';ctx.fillText('距离 →',W-50,H-6);ctx.fillText('高度',6,18);

      // 观测点
      lv.obs.forEach(function(p){
        ctx.beginPath();ctx.arc(sx(p.x),sy(p.y),6,0,Math.PI*2);ctx.fillStyle='#5eead4';ctx.fill();
        ctx.strokeStyle='#0f1117';ctx.lineWidth=2;ctx.stroke();
      });
      // 靶心
      var tx=sx(lv.target.x),ty=sy(lv.target.y);
      ctx.beginPath();ctx.arc(tx,ty,14,0,Math.PI*2);ctx.fillStyle='rgba(239,68,68,0.15)';ctx.fill();
      ctx.strokeStyle='#ef4444';ctx.lineWidth=2.5;ctx.stroke();
      ctx.beginPath();ctx.arc(tx,ty,4,0,Math.PI*2);ctx.fillStyle='#ef4444';ctx.fill();
      ctx.fillStyle='#ef4444';ctx.font='bold 11px sans-serif';ctx.fillText('目标',tx+18,ty+4);

      // 大炮
      var cy0=parseFloat(y0S.value),ca=rad(parseFloat(angleS.value));
      ctx.fillStyle='#e6e8ee';ctx.fillRect(sx(0)-8,sy(cy0)-4,16,8);
      ctx.beginPath();ctx.moveTo(sx(0),sy(cy0));ctx.lineTo(sx(0)+Math.cos(ca)*28,sy(cy0)-Math.sin(ca)*28);
      ctx.strokeStyle='#e6e8ee';ctx.lineWidth=3;ctx.stroke();

      // 预览虚线
      if(!ut){
        var pv=traj(parseFloat(angleS.value),parseFloat(speedS.value),parseFloat(y0S.value),300);
        ctx.setLineDash([5,4]);ctx.strokeStyle='#818cf8';ctx.lineWidth=1.5;ctx.beginPath();
        pv.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();ctx.setLineDash([]);
      }
      // 发射轨迹
      if(ut){
        ctx.strokeStyle='#818cf8';ctx.lineWidth=2.5;ctx.beginPath();
        ut.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();
        var lp=ut[ut.length-1];ctx.beginPath();ctx.arc(sx(lp.x),sy(lp.y),5,0,Math.PI*2);ctx.fillStyle='#818cf8';ctx.fill();
      }
      // 真实弹道
      if(showR){
        ctx.setLineDash([3,3]);ctx.strokeStyle='#5eead4';ctx.lineWidth=1.5;ctx.beginPath();
        lv.real.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();ctx.setLineDash([]);
      }
      ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';ctx.fillText('第 '+(cur+1)+'/'+levels.length+' 关：'+lv.name,40,16);
    }

    function fitErr(){
      var t=traj(parseFloat(angleS.value),parseFloat(speedS.value),parseFloat(y0S.value),300),err=0;
      lv.obs.forEach(function(o){var m=Infinity;t.forEach(function(p){var d=Math.hypot(p.x-o.x,p.y-o.y);if(d<m)m=d;});err+=m;});
      return err/lv.obs.length;
    }

    function upd(){angleV.textContent=angleS.value+'°';speedV.textContent=speedS.value;y0V.textContent=y0S.value;if(!fired)draw(null,false);}
    angleS.addEventListener('input',upd);speedS.addEventListener('input',upd);y0S.addEventListener('input',upd);

    function doFire(){
      if(fired)return;fired=true;
      var t=traj(parseFloat(angleS.value),parseFloat(speedS.value),parseFloat(y0S.value),300);
      var lp=t[t.length-1],dist=Math.abs(lp.x-lv.target.x),fe=fitErr();
      draw(t,true);
      var hs=Math.max(0,100-Math.round(dist*2)),fs=Math.max(0,100-Math.round(fe*5));
      var rs=Math.round(hs*0.6+fs*0.4);total+=rs;
      var hm=dist<5?'🎯 完美命中！':dist<15?'👍 很接近！':dist<30?'还行，差一点。':'💥 偏了不少。';
      msgEl.innerHTML=hm+' 落点偏差 '+Math.round(dist)+' 米，拟合误差 '+Math.round(fe)+' 米。本关 <b>'+rs+'/100</b>';
      if(cur<levels.length-1){
        fireBtn.textContent='下一关 →';
        fireBtn.onclick=function(){cur++;lv=genLv();fired=false;msgEl.innerHTML='';fireBtn.textContent='🚀 发射！';fireBtn.onclick=doFire;angleS.value=45;speedS.value=100;y0S.value=20;upd();};
      }else{
        var avg=Math.round(total/levels.length);
        scoreEl.innerHTML='🏆 总分 <b>'+total+'/'+(levels.length*100)+'</b>，平均 '+avg;
        fireBtn.textContent='重新开始';
        fireBtn.onclick=function(){cur=0;total=0;lv=genLv();fired=false;msgEl.innerHTML='';scoreEl.innerHTML='';fireBtn.textContent='🚀 发射！';fireBtn.onclick=doFire;angleS.value=45;speedS.value=100;y0S.value=20;upd();};
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
| 调整角度、速度、高度 | 调整模型参数（权重、超参） |
| 抛物线穿过观测点 | 模型拟合历史数据 |
| 抛物线延伸到靶心 | 模型外推到未来 |
| 命中靶心 | 预测准确 |

**三个关键洞察：**

- **参数够用就好。** 三个滑块（角度、速度、高度）足以描述一条抛物线。时间序列模型也是——参数太多反而会"过拟合"，在训练数据上完美，在新数据上崩溃。
- **观测点的覆盖范围很重要。** 如果所有观测点都挤在起点附近，你很难判断远处的落点。同理，历史数据太短或模式太单一，预测就不可靠。
- **外推越远越难。** 靶心越远，一点角度偏差就会被放大成巨大的落点误差。预测未来也是如此——预测一天后比预测一个月后容易得多。

> 但现实中的时间序列远不止抛物线那么简单——它们是各种**波形**的叠加。下一页我们来认识波的类型，以及为什么理解波形对预测至关重要。
