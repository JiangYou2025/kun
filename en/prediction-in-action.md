---
updated: "2026-06-04"
lang: en
ref: prediction-in-action
permalink: /en/prediction-in-action/
title: "A Successful Prediction"
lead: "What is the essence of prediction? Starting from the data already observed, find a rule, then extend it to where you have not yet looked. This page lets you experience it first-hand with a small artillery game: adjust the parameters → fit the trajectory → hit the target."
prev: forecasting
next: math-ml-foundations
---

## Prediction = fitting + extrapolation

On the previous page we saw that prediction is everywhere. But how is "prediction" actually done?

The most basic approach has just two steps:

1. **Fit**: find a curve that passes as closely as possible through the data points you already have.
2. **Extrapolate**: extend that curve into the future to obtain the predicted values.

This is exactly like artillery fire — you observe the trajectory of a few shells, adjust the cannon's **starting position** and **launch angle** so that the trajectory curve fits those observed points, and finally hit the distant target.

## 🎯 Artillery fire: you predict the trajectory

<div class="game" markdown="0">
  <h3 style="margin-top:0">Adjust the cannon and hit the target!</h3>
  <p class="hint">The scene shows <strong>blue observed points</strong> (known trajectory data) and a <strong>red bullseye</strong> (the target). Drag the sliders to adjust the cannon's <strong>horizontal position</strong> and <strong>launch angle</strong>. The guide line shows only the first half of the trajectory — where the second half lands is up to your own judgment! There are 5 levels, with the noise increasing from level to level.</p>

  <canvas id="art-canvas" width="560" height="260" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>

  <div style="display:flex;flex-wrap:wrap;gap:18px;margin:14px 0;align-items:center">
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">Cannon horizontal position x₀</span>
      <input type="range" id="art-x0" min="0" max="100" value="0" step="1" style="width:100%">
      <span id="art-x0-val" style="font-size:.85rem;font-weight:600">0</span>
    </label>
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">Launch angle θ</span>
      <input type="range" id="art-angle" min="15" max="80" value="45" step="0.5" style="width:100%">
      <span id="art-angle-val" style="font-size:.85rem;font-weight:600">45°</span>
    </label>
  </div>
  <div class="bar2" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
    <button id="art-fire" type="button" style="padding:8px 24px;font-size:1rem;font-weight:600;border-radius:6px;background:var(--accent);color:var(--bg);border:none;cursor:pointer">🚀 Fire!</button>
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

    // Each level: the true x0 and angle (fixed speed V0, height = 0)
    var levels=[
      {x0:10, angle:50, name:'Level 1 · Precise data',   nObs:7, noise:1},
      {x0:25, angle:42, name:'Level 2 · Slight jitter',   nObs:6, noise:4},
      {x0:5,  angle:62, name:'Level 3 · More noise',   nObs:5, noise:10},
      {x0:35, angle:35, name:'Level 4 · Sparse data',   nObs:3, noise:12},
      {x0:15, angle:55, name:'Level 5 · Extreme noise',   nObs:3, noise:22}
    ];
    var cur=0,total=0,fired=false,sc=1;
    var GND=H-26; // ground y in pixels

    function rad(d){return d*Math.PI/180;}

    // Parabola starting from x0, angle a, speed V0, y0=0
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
      // Auto-scale: keep the whole trajectory + bullseye inside the view
      var maxX=0,maxY=0;
      real.forEach(function(p){if(p.x>maxX)maxX=p.x;if(p.y>maxY)maxY=p.y;});
      maxX=Math.max(maxX,last.x)*1.15; // leave a 15% margin for the user's offset
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

      // Ground
      ctx.fillStyle='rgba(94,234,212,0.05)';ctx.fillRect(0,GND,W,H-GND);
      ctx.strokeStyle='#262b38';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,GND);ctx.lineTo(W,GND);ctx.stroke();
      ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';
      ctx.fillText('distance →',W-62,H-4);

      // Observed points
      lv.obs.forEach(function(p){
        ctx.beginPath();ctx.arc(sx(p.x),sy(p.y),5,0,Math.PI*2);
        ctx.fillStyle='#5eead4';ctx.fill();
        ctx.strokeStyle='#0f1117';ctx.lineWidth=1.5;ctx.stroke();
      });

      // Bullseye (on the ground)
      var tx=sx(lv.target.x),ty=GND;
      ctx.beginPath();ctx.arc(tx,ty,12,0,Math.PI*2);ctx.fillStyle='rgba(239,68,68,0.15)';ctx.fill();
      ctx.strokeStyle='#ef4444';ctx.lineWidth=2.5;ctx.stroke();
      ctx.beginPath();ctx.arc(tx,ty,3,0,Math.PI*2);ctx.fillStyle='#ef4444';ctx.fill();
      ctx.fillStyle='#ef4444';ctx.font='bold 10px sans-serif';ctx.fillText('target',tx+14,ty-4);

      // Cannon (on the ground)
      var cx0=parseFloat(x0S.value),ca=rad(parseFloat(angleS.value));
      var cannonX=sx(cx0);
      // Carriage
      ctx.fillStyle='#e6e8ee';ctx.fillRect(cannonX-6,GND-6,12,6);
      // Barrel
      ctx.beginPath();ctx.moveTo(cannonX,GND-3);
      ctx.lineTo(cannonX+Math.cos(ca)*24,GND-3-Math.sin(ca)*24);
      ctx.strokeStyle='#e6e8ee';ctx.lineWidth=3;ctx.stroke();

      // Preview dashed line (first half only)
      if(!ut){
        var pv=traj(cx0,parseFloat(angleS.value));
        var half=Math.floor(pv.length/2);
        ctx.setLineDash([5,4]);ctx.strokeStyle='#818cf8';ctx.lineWidth=1.5;ctx.beginPath();
        for(var hi=0;hi<half;hi++){if(hi===0)ctx.moveTo(sx(pv[hi].x),sy(pv[hi].y));else ctx.lineTo(sx(pv[hi].x),sy(pv[hi].y));}
        ctx.stroke();ctx.setLineDash([]);
        if(half>0){var hp=pv[half-1];ctx.fillStyle='#818cf8';ctx.font='bold 16px sans-serif';ctx.fillText('?',sx(hp.x)+6,sy(hp.y)-2);}
      }

      // Trajectory after firing (solid line)
      if(ut){
        ctx.strokeStyle='#818cf8';ctx.lineWidth=2.5;ctx.beginPath();
        ut.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();
        var lp=ut[ut.length-1];
        ctx.beginPath();ctx.arc(sx(lp.x),sy(lp.y),5,0,Math.PI*2);ctx.fillStyle='#818cf8';ctx.fill();
      }

      // True trajectory (the answer)
      if(showR){
        ctx.setLineDash([3,3]);ctx.strokeStyle='#5eead4';ctx.lineWidth=1.5;ctx.beginPath();
        lv.real.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();ctx.setLineDash([]);
      }

      ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
      ctx.fillText('Level '+(cur+1)+'/'+levels.length+': '+lv.name,40,16);
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
      var hm=dist<5?'🎯 Perfect hit!':dist<15?'👍 Very close!':dist<30?'Not bad, just a little off.':'💥 Way off.';
      msgEl.innerHTML=hm+' Landing offset '+Math.round(dist)+', fitting error '+Math.round(fe)+'. This level: <b>'+rs+'/100</b>';
      if(cur<levels.length-1){
        fireBtn.textContent='Next level →';
        fireBtn.onclick=function(){cur++;lv=genLv();fired=false;msgEl.innerHTML='';fireBtn.textContent='🚀 Fire!';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }else{
        var avg=Math.round(total/levels.length);
        scoreEl.innerHTML='🏆 Total score <b>'+total+'/'+(levels.length*100)+'</b>, average '+avg;
        fireBtn.textContent='Start over';
        fireBtn.onclick=function(){cur=0;total=0;lv=genLv();fired=false;msgEl.innerHTML='';scoreEl.innerHTML='';fireBtn.textContent='🚀 Fire!';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }
    }
    fireBtn.onclick=doFire;
    upd();
  })();
  </script>
</div>

## What does this have to do with time series forecasting?

What you just did is exactly the essence of time series forecasting:

| Artillery fire | Time series forecasting |
|---------|------------|
| Blue observed points | Historical data (the known past) |
| Adjusting position and angle | Adjusting model parameters (weights, hyperparameters) |
| The parabola passes through the observed points | The model fits the historical data |
| The parabola extends to the bullseye | The model extrapolates into the future |
| Hitting the bullseye | An accurate forecast |

**Three key insights:**

- **Just enough parameters is best.** Two sliders (position, angle) are enough to describe a parabola. The same goes for time series models — too many parameters lead to "overfitting": perfect on the training data, collapsing on new data.
- **The coverage of the observed points matters.** If all the observed points are crowded near the starting point, it is hard to judge where the shell will land far away. Likewise, if the historical data is too short or its patterns too uniform, the forecast will be unreliable.
- **The further you extrapolate, the harder it gets.** The further away the bullseye, the more a tiny angle error is amplified into a huge landing error. Predicting the future is the same — forecasting one day ahead is much easier than forecasting a month ahead.

> Just now you tuned the parameters with your eyes and hands. But what makes this curve the right one? On the next page we lay the **mathematical and machine learning** foundations underneath prediction: describing rules with functions, using optimization to find the best curve automatically, and using generalization to judge whether we have overlearned.
