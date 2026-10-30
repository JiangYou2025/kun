---
updated: "2026-06-11"
lang: en
ref: linear-autoregression
permalink: /en/linear-autoregression/
title: "Autoregressive Forecasting with Linear Models"
lead: "Autoregression is the oldest and most central idea in time series forecasting: use the last few values to predict the next one, linearly. This page first lays out the mathematics of autoregression (AR) and works through a small example, then shows that the modern “linear model” is simply its one-shot generalization to many steps — which is exactly the seed of KUN's “linear kernel” on the next page."
prev: math-ml-foundations
next: kun
math: true
---

## 1. Autoregression: predicting the future from the past

The simplest and yet most profound assumption is this: **the future of a series is a linear combination of its own past.** That is the **autoregressive model (AutoRegressive, AR)**.

An autoregressive model of order $$p$$, $$\text{AR}(p)$$, is written:

$$x_t = c + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + \varepsilon_t$$

- $$x_{t-1}, \ldots, x_{t-p}$$ are the last $$p$$ observations (the **lookback window**);
- $$\phi_1, \ldots, \phi_p$$ are the **weights** to be learned, and $$c$$ is the constant term;
- $$\varepsilon_t$$ is unpredictable random noise (white noise).

Forecasting simply means dropping the noise term and taking the weighted sum with the learned weights:

$$\hat{x}_t = c + \phi_1 x_{t-1} + \cdots + \phi_p x_{t-p}$$

### Hands-on: click the sunspot series and see what the model is thinking

Remember the [sunspots](../applications/geophysics/)? In 1927 Yule invented autoregression precisely on them. Below, on a sunspot-like series, an $$\text{AR}(12)$$ (using the last 12 values to predict the next) is **fitted live** by least squares — **click any point on the curve** to see which data the model used to predict it, what weight each value was multiplied by, and how much each one contributes.

<div class="game" markdown="0">
<h3 style="margin-top:0">🌞 Click any point: see which 12 past values the model used and how it weighted them</h3>
<p class="hint">Every point to the right of the grey dashed line is clickable. Blue dots = the history window used for this prediction, yellow circle = the predicted value, solid dot = the true value.</p>

<canvas id="ar-canvas" width="640" height="300" style="width:100%;max-width:640px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>
<div id="ar-info" style="margin-top:12px;font-size:.9rem"></div>

<style>
#ar-info table{border-collapse:collapse;width:100%;max-width:560px;font-size:.84rem;margin-top:8px}
#ar-info th,#ar-info td{padding:3px 8px;text-align:right;border-bottom:1px solid var(--border)}
#ar-info th:first-child,#ar-info td:first-child{text-align:left}
.wbar{display:inline-block;height:9px;border-radius:2px;vertical-align:middle}
</style>

<script>
(function(){
  var canvas=document.getElementById('ar-canvas');
  if(!canvas) return;
  var ctx=canvas.getContext('2d');
  var info=document.getElementById('ar-info');
  var W=640,H=300,p=12,N=140;
  var ML=40,MR=14,MT=16,MB=26, PW=W-ML-MR, PH=H-MT-MB;
  var i,j,k,t;

  // 1) Generate a sunspot-like series (deterministic, non-negative, period of about 11 steps)
  var y=[];
  for(t=0;t<N;t++){
    var base=85+72*Math.sin(2*Math.PI*t/11)+24*Math.sin(2*Math.PI*t/5.5+1.0);
    var wig=16*Math.sin(t*1.7)*Math.cos(t*0.41)+10*Math.sin(t*0.9+0.5);
    var v=base+wig; if(v<0)v=0; y.push(v);
  }

  // 2) Solve a linear system by Gaussian elimination
  function solve(A,b){
    var nn=b.length,r,c,ii;
    for(c=0;c<nn;c++){
      var piv=c;
      for(r=c+1;r<nn;r++) if(Math.abs(A[r][c])>Math.abs(A[piv][c])) piv=r;
      var ta=A[c];A[c]=A[piv];A[piv]=ta; var tb=b[c];b[c]=b[piv];b[piv]=tb;
      var d=A[c][c]; if(Math.abs(d)<1e-9) d=d<0?-1e-9:1e-9;
      for(r=0;r<nn;r++){ if(r===c) continue; var f=A[r][c]/d; for(ii=c;ii<nn;ii++) A[r][ii]-=f*A[c][ii]; b[r]-=f*b[c]; }
    }
    var x=[]; for(ii=0;ii<nn;ii++) x.push(b[ii]/A[ii][ii]); return x;
  }

  // 3) Least-squares fit of AR(p) (with intercept + a light ridge to stabilize the weights)
  var n=p+1, A=[], bv=[];
  for(i=0;i<n;i++){ A.push(new Array(n).fill(0)); bv.push(0); }
  for(t=p;t<N;t++){
    var feat=[1]; for(k=1;k<=p;k++) feat.push(y[t-k]);
    for(i=0;i<n;i++){ for(j=0;j<n;j++) A[i][j]+=feat[i]*feat[j]; bv[i]+=feat[i]*y[t]; }
  }
  var md=0; for(i=1;i<n;i++) md+=A[i][i]; md/=p;
  for(i=1;i<n;i++) A[i][i]+=0.05*md;
  var coef=solve(A,bv);   // coef[0]=intercept, coef[k]=weight of lag k

  function predict(tt){ var s=coef[0]; for(var kk=1;kk<=p;kk++) s+=coef[kk]*y[tt-kk]; return s; }

  var ymin=Math.min.apply(null,y), ymax=Math.max.apply(null,y), TAU=Math.PI*2;
  function X(idx){ return ML+PW*idx/(N-1); }
  function Y(val){ return MT+PH*(1-(val-ymin)/(ymax-ymin)); }

  var sel=N-1;

  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.4)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(X(p-0.5),MT);ctx.lineTo(X(p-0.5),MT+PH);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';ctx.fillText('needs ≥12 past values',X(p)+4,MT+12);

    if(sel!==null){ ctx.fillStyle='rgba(129,140,248,0.13)';ctx.fillRect(X(sel-p),MT,X(sel-1)-X(sel-p),PH); }

    ctx.strokeStyle='#5eead4';ctx.lineWidth=2;ctx.beginPath();
    for(i=0;i<N;i++){ var xx=X(i),yy=Y(y[i]); if(i===0)ctx.moveTo(xx,yy); else ctx.lineTo(xx,yy); }
    ctx.stroke();
    for(i=0;i<N;i++){ ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(X(i),Y(y[i]),1.8,0,TAU);ctx.fill(); }

    if(sel!==null){
      for(k=1;k<=p;k++){ var id=sel-k; ctx.fillStyle='#818cf8';ctx.beginPath();ctx.arc(X(id),Y(y[id]),3.4,0,TAU);ctx.fill(); }
      ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(X(sel),Y(y[sel]),4,0,TAU);ctx.fill();
      var pv=predict(sel);
      ctx.strokeStyle='rgba(251,191,36,0.55)';ctx.setLineDash([2,3]);ctx.lineWidth=1.5;
      ctx.beginPath();ctx.moveTo(X(sel),Y(pv));ctx.lineTo(X(sel),Y(y[sel]));ctx.stroke();ctx.setLineDash([]);
      ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;ctx.beginPath();ctx.arc(X(sel),Y(pv),5,0,TAU);ctx.stroke();
    }
  }

  function renderInfo(){
    if(sel===null){ info.innerHTML=''; return; }
    var pv=predict(sel), av=y[sel], maxc=0, kk, rows='';
    for(kk=1;kk<=p;kk++){ var cc=Math.abs(coef[kk]*y[sel-kk]); if(cc>maxc)maxc=cc; }
    for(kk=1;kk<=p;kk++){
      var w=coef[kk], val=y[sel-kk], contr=w*val;
      var bw=maxc>0?Math.round(Math.abs(contr)/maxc*64):0;
      var col=contr>=0?'#5eead4':'#ef4444';
      rows+='<tr><td>x<sub>t−'+kk+'</sub></td><td>'+w.toFixed(3)+'</td><td>'+val.toFixed(1)+'</td><td>'+contr.toFixed(1)+'</td><td><span class="wbar" style="width:'+bw+'px;background:'+col+'"></span></td></tr>';
    }
    info.innerHTML='<div>Predicting point <strong>t = '+sel+'</strong>: ŷ = intercept '+coef[0].toFixed(1)+' + Σ(weight × past value) = <strong style="color:#fbbf24">'+pv.toFixed(1)+'</strong> · true value <strong style="color:#5eead4">'+av.toFixed(1)+'</strong> (error '+(pv-av>=0?'+':'')+(pv-av).toFixed(1)+')</div>'+
      '<table><thead><tr><th>Past value used</th><th>Weight w</th><th>Value x</th><th>Contribution w·x</th><th></th></tr></thead><tbody>'+rows+'</tbody></table>';
  }

  canvas.addEventListener('click',function(e){
    var rect=canvas.getBoundingClientRect();
    var cx=(e.clientX-rect.left)*(W/rect.width);
    var idx=Math.round((cx-ML)/PW*(N-1));
    if(idx<p)idx=p; if(idx>N-1)idx=N-1;
    sel=idx; draw(); renderInfo();
  });

  draw(); renderInfo();
})();
</script>
</div>

> **See what is going on?** The same set of weights $$w_1,\dots,w_{12}$$ is **shared by every time step** — that is the "rule the model has learned". When you click a different point, all that changes is the 12 past values it acts on, so each point gets a different "contribution breakdown". Extend this single weighted sum to "output $$H$$ values at once" and you have the **linear model** discussed below; stack it in a U-shaped hierarchy and you have **KUN**.

### The simplest case: AR(1)

$$x_t = c + \phi\, x_{t-1} + \varepsilon_t$$

A single coefficient $$\phi$$ determines the "character" of the series:

- **−1 < φ < 1** (i.e. the absolute value of φ is less than 1): the series is **stationary** and keeps being pulled back towards its long-run mean μ = c/(1−φ) — this is called **mean reversion** (interest rates, temperatures and inventories often behave this way).
- **φ = 1**: it becomes a **random walk** (next value = previous value + random noise), with no restoring force; stock prices are often approximated this way.
- **φ > 1 or φ < −1** (absolute value greater than 1): it diverges, which is rare in practice.

Here is "mean reversion" turned into a **small interactive plot**, so you can watch a value being pulled back to the midline step by step 👇

<div class="game" markdown="0">
<h3 style="margin-top:0">🎯 Mean-reversion mini-game: click to take a step and watch it climb back to the midline</h3>
<p class="hint">This is AR(1): <b>x' = c + φ·x</b> (long-run mean μ = c/(1−φ); every parameter set below gives μ=10). <strong>Each click on the canvas performs one iteration</strong>: the vertical segment goes to the AR line (= computing the next value), the horizontal segment comes back to the <b>y=x midline</b>. Click a few more times and the blue path converges to the intersection of the midline and the AR line — that is μ. Click <strong>“Change parameters”</strong> to switch to a different φ: <b>the closer φ is to 1, the slower the climb</b>; <b>with a negative φ it spirals back and forth around μ as it converges</b>.</p>
<canvas id="cw-canvas" width="352" height="344" style="width:100%;max-width:352px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:pointer"></canvas>
<div style="margin-top:10px"><button id="cw-reset">Change parameters</button> <span id="cw-info" style="font-size:.9rem;color:var(--muted)"></span></div>

<style>
#cw-reset{padding:5px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;font-size:.86rem}
#cw-reset:hover{opacity:.85}
</style>

<script>
(function(){
  var cv=document.getElementById('cw-canvas'); if(!cv) return;
  var ctx=cv.getContext('2d'); var info=document.getElementById('cw-info');
  var W=352,H=344, ML=38,MR=14,MT=14,MB=30, PW=W-ML-MR, PH=H-MT-MB;
  var XMAX=20, TAU=Math.PI*2;
  // A set of parameters, all with μ = 10, differing only in φ — see how the path changes
  var PARAMS=[
    {c:4,  phi:0.6},   // medium speed, monotone climb
    {c:7,  phi:0.3},   // converges very fast
    {c:1.5,phi:0.85},  // converges very slowly
    {c:13, phi:-0.3},  // slight back-and-forth spiral
    {c:16, phi:-0.6}   // clear spiral around μ
  ];
  var pidx=0, c=PARAMS[0].c, phi=PARAMS[0].phi, mu=c/(1-phi);
  function f(x){ return c+phi*x; }
  function gx(v){ return ML+PW*v/XMAX; }
  function gy(v){ return MT+PH*(1-v/XMAX); }
  var pts=[], steps=0;

  function status(){
    var cur=pts[pts.length-1][0];
    info.innerHTML='φ = '+phi.toFixed(2)+', c = '+c.toFixed(1)+' (μ = '+mu.toFixed(0)+') · step '+steps+': x = '+cur.toFixed(2)+', distance to μ: '+Math.abs(cur-mu).toFixed(2);
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.25)';ctx.lineWidth=1;ctx.strokeRect(ML,MT,PW,PH);
    // Axes: x axis (bottom edge), y axis (left edge) + ticks + origin O
    ctx.strokeStyle='rgba(150,160,180,0.7)';ctx.lineWidth=1.3;
    ctx.beginPath();
    ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(XMAX),gy(0));
    ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(0),gy(XMAX));
    ctx.stroke();
    ctx.fillStyle='#9aa3b2';ctx.font='10px sans-serif';
    for(var tk=5;tk<=XMAX;tk+=5){
      ctx.beginPath();ctx.moveTo(gx(tk),gy(0));ctx.lineTo(gx(tk),gy(0)+4);ctx.stroke();
      ctx.beginPath();ctx.moveTo(gx(0),gy(tk));ctx.lineTo(gx(0)-4,gy(tk));ctx.stroke();
      ctx.fillText(tk,gx(tk)-5,gy(0)+15);
      ctx.fillText(tk,gx(0)-20,gy(tk)+3);
    }
    ctx.fillStyle='#9aa3b2';ctx.beginPath();ctx.arc(gx(0),gy(0),2.6,0,TAU);ctx.fill();
    ctx.fillText('O',gx(0)-11,gy(0)+13);
    ctx.strokeStyle='rgba(150,160,180,0.75)';ctx.setLineDash([5,4]);ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(XMAX),gy(XMAX));ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle='#818cf8';ctx.lineWidth=2;
    ctx.beginPath();ctx.moveTo(gx(0),gy(f(0)));ctx.lineTo(gx(XMAX),gy(f(XMAX)));ctx.stroke();
    ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(gx(mu),gy(mu),5,0,TAU);ctx.fill();
    ctx.strokeStyle='#5eead4';ctx.lineWidth=1.8;ctx.beginPath();
    for(var i=0;i<pts.length;i++){ var px=gx(pts[i][0]),py=gy(pts[i][1]); if(i===0)ctx.moveTo(px,py); else ctx.lineTo(px,py); }
    ctx.stroke();
    var last=pts[pts.length-1];
    ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(gx(last[0]),gy(last[1]),4,0,TAU);ctx.fill();
    ctx.font='11px sans-serif';
    ctx.fillStyle='#9aa3b2';ctx.fillText('y = x',gx(XMAX)-32,gy(XMAX)+13);
    ctx.fillStyle='#818cf8';ctx.fillText('x → c+φx',gx(XMAX)-60,gy(f(XMAX))-6);
    ctx.fillStyle='#fbbf24';ctx.fillText('μ',gx(mu)+7,gy(mu)+4);
    ctx.fillStyle='#9aa3b2';ctx.fillText('x (current)',ML+PW/2-22,H-9);
    ctx.save();ctx.translate(12,MT+PH/2+26);ctx.rotate(-TAU/4);ctx.fillText("x' (next step)",0,0);ctx.restore();
    ctx.fillStyle='#818cf8';ctx.font='12px sans-serif';ctx.fillText('φ = '+phi.toFixed(2),ML+6,MT+14);
  }
  var MAXSTEPS=14;
  function step(){
    if(steps>=MAXSTEPS) return;
    var x=pts[pts.length-1][0], fx=f(x);
    pts.push([x,fx]); pts.push([fx,fx]); steps++;
    draw(); status();
  }
  function reset(start){
    var x0=(start==null)?(2+Math.random()*16):start;
    pts=[[x0,x0]]; steps=0; draw(); status();
  }
  cv.addEventListener('click',step);
  document.getElementById('cw-reset').addEventListener('click',function(){
    pidx=(pidx+1)%PARAMS.length;
    c=PARAMS[pidx].c; phi=PARAMS[pidx].phi; mu=c/(1-phi);
    reset(17);
  });
  reset(17);
})();
</script>
</div>

### It is really just a linear regression

Treat the lookback window as features and the next value as the label, and AR is a standard **linear regression**: use $$(x_{t-1}, \ldots, x_{t-p})$$ to predict $$x_t$$. Slide this window **step by step along the series** and you get one training sample after another — $$(x_1,\ldots,x_p)\to x_{p+1}$$, $$(x_2,\ldots,x_{p+1})\to x_{p+2}$$, and so on.

The parameters can therefore be solved for directly by **least squares** (classical statistics also uses the **Yule–Walker equations**; the two are equivalent). This is the "use optimization to find the best rule" of [step 4](../math-ml-foundations/), landing on time series as its first concrete model.

## 2. From one step to many: the linear model

Classical AR **predicts only one step** at a time. To forecast $$H$$ steps ahead, the traditional approach is **recursive**: predict $$\hat{x}_{t}$$, then feed it back as if it were a true value to predict $$\hat{x}_{t+1}$$ … but the errors **accumulate** from one step to the next.

The modern approach is more direct — **predict the whole future segment in one go**. This is the so-called "**linear model**": **a single linear layer** (weight matrix $$W$$, bias $$b$$) maps the lookback window $$x_{t-L+1:t}$$ of length $$L$$ in one shot to the future $$\hat{x}_{t+1:t+H}$$ of length $$H$$:

$$\hat{x}_{t+1:t+H} \;=\; W\,x_{t-L+1:t} + b, \qquad W \in \mathbb{R}^{H \times L},\; b \in \mathbb{R}^{H}$$

Here the input is $$L$$ past values, the output is $$H$$ future values, and $$W$$ is an $$H \times L$$ weight matrix. Written out for each future time step, it is $$H$$ weighted sums side by side:

$$\hat{x}_{t+h} \;=\; \sum_{i=1}^{L} W_{h,i}\,x_{t-L+i} + b_h, \qquad h = 1, 2, \dots, H$$

Each $$\hat{x}_{t+h}$$ is **a weighted sum over the entire lookback window** — exactly a "scaled-up" version of the AR weighted sum: classical AR is just the special case $$H=1$$ (a single output row) with $$L=p$$.

Put side by side, they turn out to be two scales of the same idea:

| | Classical AR | Linear model |
|---|---|---|
| Input | The last $$p$$ values | The last $$L$$ values (lookback window) |
| Output | **1** value (the next step) | **$$H$$** values (the whole future segment) |
| Essence | $$1$$-dimensional linear map | Linear map $$L \to H$$ |
| Multi-step | Recursive, errors accumulate | Direct multi-output, no accumulation |

So, in one sentence: **a linear model is vectorized, multi-output autoregression.** Extend the AR weighted sum from "computing one number" to "computing a whole row of numbers at once", and that is what you get.

So how big is the difference between "recursion accumulates errors" and "direct multi-output does not"? Click and see 👇

<div class="game" markdown="0">
<h3 style="margin-top:0">🔮 Click any time step: compare “recursive single-step” with “direct multi-output”</h3>
<p class="hint"><strong>Click a forecast origin t</strong> on the curve. Both models use the <b>L=16</b> values before it to forecast <b>H=18</b> steps ahead: <span style="color:#818cf8;font-weight:600">blue = direct multi-output</span> (one linear layer computes the whole segment at once), <span style="color:#f59e0b;font-weight:600">orange = recursive single-step</span> (predict one step, feed it back as a true value, then predict the next), <span style="color:#5eead4;font-weight:600">teal = the true future</span>. Watch how orange drifts further and further off.</p>

<canvas id="ms-canvas" width="640" height="320" style="width:100%;max-width:640px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>
<div id="ms-info" style="margin-top:10px;font-size:.9rem;color:var(--muted)"></div>

<script>
(function(){
  var cv=document.getElementById('ms-canvas'); if(!cv) return;
  var ctx=cv.getContext('2d'); var info=document.getElementById('ms-info');
  var W=640,CH=320, ML=42,MR=12,MT=16,MB=28, PW=W-ML-MR, PH=CH-MT-MB;
  var N=170, L=16, H=18, TAU=Math.PI*2;
  var i,j,k,t,h;

  // A series with two incommensurate periods + an irregular term: period 23 is longer than L=16, so the single-step model cannot fit it perfectly
  var y=[];
  for(t=0;t<N;t++){
    var b=52+26*Math.sin(TAU*t/23)+13*Math.sin(TAU*t/9+0.6);
    var irr=7*Math.sin(t*0.7)*Math.cos(t*0.27)+5*Math.sin(t*1.3+0.4);
    y.push(b+irr);
  }

  function solve(A,b){
    var nn=b.length,r,c,ii;
    for(c=0;c<nn;c++){
      var piv=c;
      for(r=c+1;r<nn;r++) if(Math.abs(A[r][c])>Math.abs(A[piv][c])) piv=r;
      var ta=A[c];A[c]=A[piv];A[piv]=ta; var tb=b[c];b[c]=b[piv];b[piv]=tb;
      var d=A[c][c]; if(Math.abs(d)<1e-9) d=d<0?-1e-9:1e-9;
      for(r=0;r<nn;r++){ if(r===c) continue; var fa=A[r][c]/d; for(ii=c;ii<nn;ii++) A[r][ii]-=fa*A[c][ii]; b[r]-=fa*b[c]; }
    }
    var x=[]; for(ii=0;ii<nn;ii++) x.push(b[ii]/A[ii][ii]); return x;
  }
  function fit(rows,tgt,m){   // least squares with a light ridge
    var A=[],bv=[],r,a,ii;
    for(a=0;a<m;a++){ A.push(new Array(m).fill(0)); bv.push(0); }
    for(r=0;r<rows.length;r++){ var fr=rows[r],tv=tgt[r];
      for(a=0;a<m;a++){ for(ii=0;ii<m;ii++) A[a][ii]+=fr[a]*fr[ii]; bv[a]+=fr[a]*tv; } }
    var md=0; for(a=1;a<m;a++) md+=A[a][a]; md/=(m-1);
    for(a=1;a<m;a++) A[a][a]+=0.04*md;
    return solve(A,bv);
  }

  // Single-step AR(L) — used recursively
  var rA=[],tA=[];
  for(t=L;t<N;t++){ var fr=[1]; for(k=1;k<=L;k++) fr.push(y[t-k]); rA.push(fr); tA.push(y[t]); }
  var coefAR=fit(rA,tA,L+1);

  // Direct multi-output — one linear model trained per horizon (= one row of the matrix W)
  var coefDir=[];
  for(h=1;h<=H;h++){
    var rows=[],tg=[];
    for(t=L-1;t+h<N;t++){ var fr=[1]; for(i=0;i<L;i++) fr.push(y[t-L+1+i]); rows.push(fr); tg.push(y[t+h]); }
    coefDir.push(fit(rows,tg,L+1));
  }

  function recursive(o){
    var hist=[]; for(k=0;k<L;k++) hist.push(y[o-k]);   // hist[0]=y[o] (lag 1)
    var out=[];
    for(h=0;h<H;h++){ var s=coefAR[0]; for(k=1;k<=L;k++) s+=coefAR[k]*hist[k-1];
      out.push(s); hist.unshift(s); hist.pop(); }
    return out;
  }
  function direct(o){
    var out=[];
    for(h=1;h<=H;h++){ var c=coefDir[h-1],s=c[0]; for(i=0;i<L;i++) s+=c[i+1]*y[o-L+1+i]; out.push(s); }
    return out;
  }

  var ymin=Math.min.apply(null,y), ymax=Math.max.apply(null,y), pad=(ymax-ymin)*0.08;
  ymin-=pad; ymax+=pad;
  function X(idx){ return ML+PW*idx/(N-1); }
  function Y(v){ return MT+PH*(1-(v-ymin)/(ymax-ymin)); }

  var o=Math.round(N*0.5);

  function draw(){
    ctx.clearRect(0,0,W,CH);
    ctx.fillStyle='rgba(129,140,248,0.10)';ctx.fillRect(X(o-L+1),MT,X(o)-X(o-L+1),PH);
    ctx.strokeStyle='rgba(150,160,180,0.6)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(X(o),MT);ctx.lineTo(X(o),MT+PH);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';
    ctx.fillText('origin t',X(o)+4,MT+11);
    ctx.fillText('lookback L='+L,X(o-L+1)+2,MT+PH-5);

    ctx.strokeStyle='#5eead4';ctx.lineWidth=2;ctx.beginPath();
    for(i=0;i<N;i++){ var xx=X(i),yy=Y(y[i]); if(i===0)ctx.moveTo(xx,yy); else ctx.lineTo(xx,yy); }
    ctx.stroke();

    var dr=direct(o), rc=recursive(o);
    function fc(arr,col){
      ctx.strokeStyle=col;ctx.lineWidth=2;ctx.setLineDash([5,3]);ctx.beginPath();
      ctx.moveTo(X(o),Y(y[o]));
      for(h=1;h<=H;h++) ctx.lineTo(X(o+h),Y(arr[h-1]));
      ctx.stroke();ctx.setLineDash([]);
      for(h=1;h<=H;h++){ ctx.fillStyle=col;ctx.beginPath();ctx.arc(X(o+h),Y(arr[h-1]),2.2,0,TAU);ctx.fill(); }
    }
    fc(dr,'#818cf8'); fc(rc,'#f59e0b');

    var maeD=0,maeR=0;
    for(h=1;h<=H;h++){ var tv=y[o+h]; maeD+=Math.abs(dr[h-1]-tv); maeR+=Math.abs(rc[h-1]-tv); }
    maeD/=H; maeR/=H;
    info.innerHTML='Mean error from origin <strong style="color:var(--text)">t='+o+'</strong> over the next <strong style="color:var(--text)">H='+H+'</strong> steps: '+
      '<span style="color:#818cf8;font-weight:600">direct '+maeD.toFixed(2)+'</span> vs '+
      '<span style="color:#f59e0b;font-weight:600">recursive '+maeR.toFixed(2)+'</span>'+
      (maeR>maeD?' → recursive is larger, and drifts further the further out it goes (errors accumulate step by step)':'');
  }

  cv.addEventListener('click',function(e){
    var rect=cv.getBoundingClientRect();
    var cx=(e.clientX-rect.left)*(W/rect.width);
    var idx=Math.round((cx-ML)/PW*(N-1));
    if(idx<L-1)idx=L-1; if(idx>N-1-H)idx=N-1-H;
    o=idx; draw();
  });
  draw();
})();
</script>
</div>

Do not underestimate such a simple structure: a single linear layer alone can match, or even beat, far more complex models on several long-horizon benchmarks (see [lecture 10](../course/10/) of the course notes), which made the whole field realize that **a linear mapping is, in itself, an extremely strong baseline**.

## 3. On the way to KUN

By now the power of linear autoregression is clear, but it also has a ceiling: **a single linear layer sees only one scale**. Real series often hide a long-term trend, mid-range cycles and high-frequency detail all at once (multiple scales).

On the next page, **KUN (Kernel U-Net)** takes exactly this "linear mapping" as a **pluggable kernel** and stacks it in a U-shaped hierarchy — so the same idea is generalized across multiple scales. In other words, **you have already learned KUN's most basic building block**.

---

**Key terms:** autoregression AR(p), AR(1) and mean reversion, random walk, least squares / Yule–Walker, lookback window, recursive vs. direct multi-step, linear model, linear kernel.
