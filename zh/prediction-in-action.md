---
updated: "2026-06-04"
lang: zh
ref: prediction-in-action
permalink: /zh/prediction-in-action/
title: "一次成功的预测"
lead: "上一篇我们知道了预测是什么。这一篇，你来亲手完成一次预测——用炮兵射击的方式，体会'观察已有数据 → 拟合规律 → 命中目标'的完整过程。"
prev: forecasting
next: kun
---

## 预测的本质：拟合 + 外推

所有预测都在做同一件事：

1. **观察**——收集已有的数据点
2. **拟合**——找到一条穿过这些点的规律（曲线）
3. **外推**——沿着这条规律，推算出还没发生的未来

这跟炮兵校射是一个道理：前几发炮弹的落点就是"历史数据"，你调整炮的位置和角度就是在"拟合模型"，最后一发命中目标就是"预测成功"。

## 来玩：炮兵校射

规则很简单：

- 画布上有**一个目标**（红色圆点）和**几个已知落点**（蓝色圆点）
- 拖动**炮的位置**（左侧滑块）和**发射角度**（右侧滑块）
- 调整好后点**发射**，你的炮弹会画出一条抛物线
- 目标：让炮弹的落点尽可能接近目标
- **共 3 关**，每关的目标位置和已知落点不同

关键体会：已知落点越多、分布越好，你就越容易找到正确的角度——这就是为什么**数据越充分，预测越准**。

<div class="game" id="artillery-game" markdown="0">
  <h3 style="margin-top:0">🎯 炮兵校射</h3>
  <p class="hint" id="art-hint">调整炮的高度和发射角度，让炮弹命中红色目标。蓝色点是前几发的落点记录，供你参考。</p>
  <svg id="art-svg" viewBox="0 0 640 360" style="width:100%;background:var(--surface,#161922);border-radius:8px">
    <!-- ground -->
    <rect x="0" y="320" width="640" height="40" fill="color-mix(in srgb,var(--accent) 15%,transparent)"/>
    <line x1="0" y1="320" x2="640" y2="320" stroke="var(--muted)" stroke-width="1"/>
    <!-- dynamic content -->
    <g id="art-dyn"></g>
  </svg>

  <div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:12px;align-items:center">
    <label style="flex:1;min-width:200px">
      <span style="font-size:.88rem;color:var(--muted)">炮的高度 <strong id="art-y-val">50%</strong></span>
      <input type="range" id="art-y" min="10" max="90" value="50" style="width:100%">
    </label>
    <label style="flex:1;min-width:200px">
      <span style="font-size:.88rem;color:var(--muted)">发射角度 <strong id="art-a-val">45°</strong></span>
      <input type="range" id="art-a" min="10" max="80" value="45" style="width:100%">
    </label>
    <button id="art-fire" type="button" style="padding:8px 24px;border-radius:6px;background:var(--accent);color:var(--bg);border:none;font-weight:600;font-size:.95rem;cursor:pointer">发射 🚀</button>
  </div>

  <p class="verdict" id="art-verdict" style="margin-top:8px;font-weight:600"></p>
  <div class="bar2" style="margin-top:4px">
    <button id="art-next" type="button" disabled style="padding:6px 18px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2,#1d212c);color:var(--text);cursor:pointer">下一关 →</button>
    <span id="art-score" style="font-size:.9rem;color:var(--muted)"></span>
  </div>

  <script>
  (function(){
    var NS='http://www.w3.org/2000/svg';
    var svg=document.getElementById('art-svg');
    var dyn=document.getElementById('art-dyn');
    var sliderY=document.getElementById('art-y');
    var sliderA=document.getElementById('art-a');
    var yVal=document.getElementById('art-y-val');
    var aVal=document.getElementById('art-a-val');
    var fireBtn=document.getElementById('art-fire');
    var nextBtn=document.getElementById('art-next');
    var verdict=document.getElementById('art-verdict');
    var scoreEl=document.getElementById('art-score');
    var hint=document.getElementById('art-hint');

    var GROUND=320, CANNON_X=40, G=9.8, SCALE=3.2;
    var levels=[
      {target:{x:420,y:260}, refs:[{x:200,y:290},{x:300,y:270},{x:350,y:265}]},
      {target:{x:500,y:230}, refs:[{x:180,y:300},{x:280,y:280},{x:380,y:255}]},
      {target:{x:550,y:200}, refs:[{x:150,y:310},{x:250,y:295},{x:400,y:240},{x:480,y:215}]}
    ];
    var lvl=0, shots=0, totalScore=0, fired=false;

    function el(tag,a){var e=document.createElementNS(NS,tag);for(var k in a)e.setAttribute(k,a[k]);return e;}

    function cannonY(){return GROUND-((+sliderY.value)/100)*(GROUND-40);}
    function angle(){return (+sliderA.value)*Math.PI/180;}

    function drawCannon(){
      var cy=cannonY(), a=angle();
      // cannon body
      var bx=CANNON_X+30*Math.cos(a), by=cy-30*Math.sin(a);
      dyn.appendChild(el('line',{x1:CANNON_X,y1:cy,x2:bx,y2:by,stroke:'var(--text)','stroke-width':4,'stroke-linecap':'round'}));
      // cannon base
      dyn.appendChild(el('circle',{cx:CANNON_X,cy:cy,r:8,fill:'var(--text)'}));
      // wheels
      dyn.appendChild(el('circle',{cx:CANNON_X-6,cy:cy+8,r:5,fill:'none',stroke:'var(--muted)','stroke-width':1.5}));
      dyn.appendChild(el('circle',{cx:CANNON_X+6,cy:cy+8,r:5,fill:'none',stroke:'var(--muted)','stroke-width':1.5}));
    }

    function render(){
      fired=false; fireBtn.disabled=false; nextBtn.disabled=true;
      while(dyn.firstChild) dyn.removeChild(dyn.firstChild);

      var L=levels[lvl];
      // target
      dyn.appendChild(el('circle',{cx:L.target.x,cy:L.target.y,r:10,fill:'#ef4444',opacity:0.9}));
      dyn.appendChild(el('circle',{cx:L.target.x,cy:L.target.y,r:4,fill:'#fff'}));
      var tl=el('text',{x:L.target.x,y:L.target.y-16,fill:'#ef4444','font-size':12,'text-anchor':'middle'}); tl.textContent='目标'; dyn.appendChild(tl);

      // reference points
      L.refs.forEach(function(p,i){
        dyn.appendChild(el('circle',{cx:p.x,cy:p.y,r:5,fill:'var(--accent)',opacity:0.8}));
        var lb=el('text',{x:p.x,y:p.y-10,fill:'var(--accent)','font-size':10,'text-anchor':'middle'}); lb.textContent='落点'+(i+1); dyn.appendChild(lb);
      });

      // label
      var ll=el('text',{x:320,y:16,fill:'var(--muted)','font-size':13,'text-anchor':'middle'});
      ll.textContent='第 '+(lvl+1)+' 关 / '+levels.length;
      dyn.appendChild(ll);

      drawCannon();
    }

    function updateCannon(){
      if(fired) return;
      // redraw without clearing everything - just re-render
      render();
    }

    sliderY.addEventListener('input',function(){yVal.textContent=sliderY.value+'%'; updateCannon();});
    sliderA.addEventListener('input',function(){aVal.textContent=sliderA.value+'°'; updateCannon();});

    function fire(){
      if(fired) return;
      fired=true; fireBtn.disabled=true; shots++;

      var cy=cannonY(), a=angle();
      var v0=48; // initial velocity
      var vx=v0*Math.cos(a), vy=v0*Math.sin(a);

      // compute trajectory
      var pts=[];
      for(var t=0;t<200;t++){
        var dt=t*0.06;
        var px=CANNON_X+vx*dt*SCALE;
        var py=cy-( vy*dt - 0.5*G*dt*dt )*SCALE;
        if(py>GROUND){
          // interpolate ground hit
          var tPrev=(t-1)*0.06;
          var pyPrev=cy-( vy*tPrev - 0.5*G*tPrev*tPrev )*SCALE;
          var frac=(GROUND-pyPrev)/(py-pyPrev);
          px=CANNON_X+vx*(tPrev+frac*0.06)*SCALE;
          py=GROUND;
          pts.push(px+','+py);
          break;
        }
        pts.push(px+','+py);
        if(px>650) break;
      }

      // draw trajectory
      dyn.appendChild(el('polyline',{points:pts.join(' '),fill:'none',stroke:'#fbbf24','stroke-width':2,'stroke-dasharray':'4 3','stroke-linecap':'round'}));

      // landing point
      var last=pts[pts.length-1].split(',');
      var lx=parseFloat(last[0]), ly=parseFloat(last[1]);
      dyn.appendChild(el('circle',{cx:lx,cy:ly,r:6,fill:'#fbbf24'}));

      // check distance to target
      var L=levels[lvl];
      var dx=lx-L.target.x, dy=ly-L.target.y;
      var dist=Math.sqrt(dx*dx+dy*dy);

      var msg, score;
      if(dist<15){
        msg='🎯 命中！偏差仅 '+Math.round(dist)+' 像素，完美预测！';
        score=100;
      } else if(dist<40){
        msg='👏 接近了！偏差 '+Math.round(dist)+' 像素，几乎命中。';
        score=Math.max(0, 80-Math.round(dist));
      } else if(dist<100){
        msg='🔍 还差一点，偏差 '+Math.round(dist)+' 像素。再试试？';
        score=Math.max(0, 50-Math.round(dist/3));
        fired=false; fireBtn.disabled=false;
        verdict.innerHTML=msg;
        return;
      } else {
        msg='💨 偏了不少，偏差 '+Math.round(dist)+' 像素。调整角度和高度再来。';
        score=0;
        fired=false; fireBtn.disabled=false;
        verdict.innerHTML=msg;
        return;
      }

      totalScore+=score;
      verdict.innerHTML=msg;

      if(lvl<levels.length-1){
        nextBtn.disabled=false;
        scoreEl.textContent='累计得分 '+totalScore+' / '+(levels.length*100);
      } else {
        // final
        var avg=Math.round(totalScore/levels.length);
        var pass=avg>=60;
        verdict.innerHTML+=('<br>'+(pass
          ? '🎉 <b>通关！</b>总分 '+totalScore+'/'+levels.length*100+'。你已经掌握了"观察→拟合→命中"的预测思维！'
          : '🔁 <b>还差一点。</b>总分 '+totalScore+'/'+levels.length*100+'。点"重新开始"再来一次。'));
        nextBtn.textContent='重新开始';
        nextBtn.disabled=false;
        nextBtn.dataset.mode='reset';
        scoreEl.textContent='最终得分 '+totalScore+'/'+levels.length*100;
      }
    }

    fireBtn.addEventListener('click',fire);
    nextBtn.addEventListener('click',function(){
      if(nextBtn.dataset.mode==='reset'){
        lvl=0; totalScore=0; shots=0;
        nextBtn.textContent='下一关 →';
        nextBtn.dataset.mode='next';
        scoreEl.textContent='';
      } else {
        lvl++;
      }
      verdict.innerHTML='';
      render();
    });

    render();
  })();
  </script>
</div>

## 从炮弹到预测：完全同构

刚才的游戏里，你在不知不觉中完成了一次预测的全流程：

| 炮兵校射 | 时间序列预测 |
|----------|-------------|
| 前几发炮弹的落点 | 历史数据 $x_1, x_2, \dots, x_T$ |
| 调整炮的高度和角度 | 拟合模型参数 $\theta$ |
| 抛物线方程 $y = v_0 t \sin\alpha - \frac{1}{2}g t^2$ | 预测模型 $\hat{x}_{T+h} = f_\theta(x_{1:T})$ |
| 命中目标 | 预测值接近真实值 |
| 偏差（像素距离） | 预测误差（MAE / RMSE） |

**核心一句话：** 预测就是先用已有数据"校准"一个模型，再让这个模型去"命中"还没出现的值。

## 为什么有时打不准？

在游戏里你可能也发现了：

- **参考点太少**——只有 1–2 个落点时，很难判断正确的角度。数据越少，预测越难。
- **参考点分布不好**——如果落点都挤在一起，对远处目标的推断就不可靠。这叫**外推风险**。
- **规律不够稳定**——如果每次发射的重力、风速都在变（真实世界的噪声），同样的参数也可能打偏。

这三个问题，正是时间序列预测中最核心的挑战：**数据量**、**分布**和**噪声**。

## 接下来

你已经用直觉完成了"观察→拟合→命中"的完整预测过程。下一篇，我们来看一个真正的深度学习模型——**Kernel U-Net (KUN)**——是怎么把同样的事情做到极致的。

<div class="note" markdown="1">
- 回顾预测的概念和应用场景：[什么是预测？](../forecasting/)
- 直接上手现代模型：[使用 KUN →](../kun/)
</div>
