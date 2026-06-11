---
updated: "2026-06-11"
lang: zh
ref: linear-autoregression
permalink: /zh/linear-autoregression/
title: "使用线性模型进行自回归预测"
lead: "自回归是时间序列预测最古老、也最核心的想法：用过去的几个值，线性地预测下一个。本页先讲清自回归（AR）的数学、做一个小例子，再说明现代的“线性模型”其实就是把它一次推广到多步——这也正是下一页 KUN “线性核”的雏形。"
prev: math-ml-foundations
next: kun
math: true
---

## 1. 自回归：用过去预测未来

最朴素也最深刻的假设是：**一个序列的未来，是它自己过去的线性组合。** 这就是**自回归模型 (AutoRegressive, AR)**。

一个 $$p$$ 阶自回归模型 $$\text{AR}(p)$$ 写成：

$$x_t = c + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + \varepsilon_t$$

- $$x_{t-1}, \ldots, x_{t-p}$$ 是过去 $$p$$ 个观测值（**回看窗口**）；
- $$\phi_1, \ldots, \phi_p$$ 是要学的**权重**， $$c$$ 是常数项；
- $$\varepsilon_t$$ 是无法预测的随机噪声（白噪声）。

预测就是把噪声项扔掉、用学到的权重做加权和：

$$\hat{x}_t = c + \phi_1 x_{t-1} + \cdots + \phi_p x_{t-p}$$

### 最简单的情形：AR(1)

$$x_t = c + \phi\, x_{t-1} + \varepsilon_t$$

一个系数 $$\phi$$ 就决定了序列的“性格”：

- **|φ| < 1**：序列**平稳**，会不断被拉回长期均值 μ = c/(1−φ)——这叫**均值回复**（利率、温度、库存常是这样）。
- **φ = 1**：变成**随机游走**（下一个值 = 上一个值 + 随机噪声），没有回归的力，股价常被这样近似。
- **|φ| > 1**：发散，现实中很少见。

把"均值回复"变成一个能玩的**蛛网图 (cobweb)** 👇

<div class="game" markdown="0">
<h3 style="margin-top:0">🎯 均值回复小游戏：点几下，看它爬回中线</h3>
<p class="hint">这是 AR(1)：<b>x' = c + φ·x</b>（取 c=4、φ=0.6，长期均值 μ=10）。<strong>每点一下画布就迭代一步</strong>：竖线走到 AR 直线（= 算出下一个值），横线回到 <b>y=x 中线</b>。蓝色折线像爬楼梯一样收敛到中线与 AR 直线的交点——那就是均值 μ。点「换个起点」从别处出发，照样回到同一点。</p>
<canvas id="cw-canvas" width="352" height="344" style="width:100%;max-width:352px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:pointer"></canvas>
<div style="margin-top:10px"><button id="cw-reset">换个起点</button> <span id="cw-info" style="font-size:.9rem;color:var(--muted)"></span></div>

<style>
#cw-reset{padding:5px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;font-size:.86rem}
#cw-reset:hover{opacity:.85}
</style>

<script>
(function(){
  var cv=document.getElementById('cw-canvas'); if(!cv) return;
  var ctx=cv.getContext('2d'); var info=document.getElementById('cw-info');
  var W=352,H=344, ML=38,MR=14,MT=14,MB=30, PW=W-ML-MR, PH=H-MT-MB;
  var XMAX=20, c=4, phi=0.6, mu=c/(1-phi), TAU=Math.PI*2;
  function f(x){ return c+phi*x; }
  function gx(v){ return ML+PW*v/XMAX; }
  function gy(v){ return MT+PH*(1-v/XMAX); }
  var pts=[], steps=0;

  function status(){
    var cur=pts[pts.length-1][0];
    info.innerHTML='第 '+steps+' 步：x = '+cur.toFixed(2)+'　·　离均值 μ=10 还差 '+Math.abs(cur-mu).toFixed(2);
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.25)';ctx.lineWidth=1;ctx.strokeRect(ML,MT,PW,PH);
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
    ctx.fillStyle='#9aa3b2';ctx.fillText('x（当前）',ML+PW/2-22,H-9);
    ctx.save();ctx.translate(12,MT+PH/2+26);ctx.rotate(-TAU/4);ctx.fillText("x'（下一步）",0,0);ctx.restore();
  }
  function step(){
    var x=pts[pts.length-1][0], fx=f(x);
    pts.push([x,fx]); pts.push([fx,fx]); steps++;
    draw(); status();
  }
  function reset(start){
    var x0=(start==null)?(2+Math.random()*16):start;
    pts=[[x0,x0]]; steps=0; draw(); status();
  }
  cv.addEventListener('click',step);
  document.getElementById('cw-reset').addEventListener('click',function(){ reset(); });
  reset(17);
})();
</script>
</div>

### 它其实就是一个线性回归

把回看窗口当作特征、把下一个值当作标签，AR 就是一个标准的**线性回归**：用 $$(x_{t-1}, \ldots, x_{t-p})$$ 去预测 $$x_t$$ 。让这个窗口在序列上**逐步向后滑动**，就得到一行行训练样本—— $$(x_1,\ldots,x_p)\to x_{p+1}$$ 、 $$(x_2,\ldots,x_{p+1})\to x_{p+2}$$ ，依此类推。

于是参数可以用**最小二乘**直接解出来（经典统计里也用 **Yule–Walker 方程**，两者等价）。这正是[第 4 步](../math-ml-foundations/)里说的“用优化找最好的规律”，落到时间序列上的第一个具体模型。

## 2. 从单步到多步：线性模型

经典 AR 一次**只预测一步**。要预测未来 $$H$$ 步，传统做法是**递归**：预测出 $$\hat{x}_{t}$$ ，再把它当成真实值代回去预测 $$\hat{x}_{t+1}$$ ……但每一步的误差会**层层累积**。

现代的做法更干脆——**一次性把整段未来都预测出来**。这就是近年大热的“**线性模型**”（如 DLinear、NLinear）：用**一个线性层**（权重矩阵 $$W$$ 、偏置 $$b$$ ），把长度为 $$L$$ 的回看窗口 $$x_{t-L+1:t}$$ 一次映射到长度为 $$H$$ 的未来 $$\hat{x}_{t+1:t+H}$$ ：

$$\hat{x}_{t+1:t+H} \;=\; W\,x_{t-L+1:t} + b, \qquad W \in \mathbb{R}^{H \times L},\; b \in \mathbb{R}^{H}$$

其中输入是 $$L$$ 个历史值、输出是 $$H$$ 个未来值， $$W$$ 是一个 $$H \times L$$ 的权重矩阵。把它展开到每一个未来时刻，就是 $$H$$ 个并排的加权和：

$$\hat{x}_{t+h} \;=\; \sum_{i=1}^{L} W_{h,i}\,x_{t-L+i} + b_h, \qquad h = 1, 2, \dots, H$$

每个 $$\hat{x}_{t+h}$$ 都是**整段回看窗口的一个加权和**——这正是 AR 那条加权和的“放大版”：经典 AR 不过是它在 $$H=1$$ （只输出一行）、 $$L=p$$ 时的特例。

对照一下就会发现，它和 AR 是同一个想法的两种规模：

| | 经典 AR | 线性模型 (DLinear 等) |
|---|---|---|
| 输入 | 过去 $$p$$ 个值 | 过去 $$L$$ 个值（回看窗口） |
| 输出 | **1** 个值（下一步） | **$$H$$** 个值（整段未来） |
| 本质 | $$1$$ 维线性映射 | $$L \to H$$ 的线性映射 |
| 多步 | 递归，误差累积 | 直接多输出，无累积 |

所以一句话：**线性模型就是向量化的、多输出的自回归。** 把 AR 那条加权和从“算一个数”扩成“一次算一整排数”，就得到了它。

别小看这么简单的结构：2022 年的 **DLinear**（先把序列分解成趋势 + 季节，再各用一个线性层）在多个长序列基准上**击败了一众复杂的 Transformer**（见讲义[第 13 讲](../../course/13/)），让整个领域重新认识到——**线性映射本身，就是一个极强的基线**。

## 动手：点击太阳黑子序列，看模型在想什么

还记得[太阳黑子](../../applications/geophysics/)吗？1927 年 Yule 正是用它发明了自回归。下面在一段类太阳黑子序列上，用最小二乘**实时拟合**一个 $$\text{AR}(12)$$ （用过去 12 个值预测下一个）——**点击曲线上任意一点**，看模型预测它时用了哪些数据、每个数据乘了多大的权重、各贡献多少。

<div class="game" markdown="0">
<h3 style="margin-top:0">🌞 点击任一点：看模型用了哪 12 个历史值、怎么加权</h3>
<p class="hint">灰色虚线右侧的点都可点击。蓝点 = 这次预测用到的历史窗口，黄圈 = 预测值，实心点 = 真实值。</p>

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

  // 1) 生成一段类太阳黑子序列（确定性、非负、约 11 步一个周期）
  var y=[];
  for(t=0;t<N;t++){
    var base=85+72*Math.sin(2*Math.PI*t/11)+24*Math.sin(2*Math.PI*t/5.5+1.0);
    var wig=16*Math.sin(t*1.7)*Math.cos(t*0.41)+10*Math.sin(t*0.9+0.5);
    var v=base+wig; if(v<0)v=0; y.push(v);
  }

  // 2) 高斯消元解线性方程组
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

  // 3) 最小二乘拟合 AR(p)（含截距 + 轻微 ridge 稳住权重）
  var n=p+1, A=[], bv=[];
  for(i=0;i<n;i++){ A.push(new Array(n).fill(0)); bv.push(0); }
  for(t=p;t<N;t++){
    var feat=[1]; for(k=1;k<=p;k++) feat.push(y[t-k]);
    for(i=0;i<n;i++){ for(j=0;j<n;j++) A[i][j]+=feat[i]*feat[j]; bv[i]+=feat[i]*y[t]; }
  }
  var md=0; for(i=1;i<n;i++) md+=A[i][i]; md/=p;
  for(i=1;i<n;i++) A[i][i]+=0.05*md;
  var coef=solve(A,bv);   // coef[0]=截距, coef[k]=滞后 k 的权重

  function predict(tt){ var s=coef[0]; for(var kk=1;kk<=p;kk++) s+=coef[kk]*y[tt-kk]; return s; }

  var ymin=Math.min.apply(null,y), ymax=Math.max.apply(null,y), TAU=Math.PI*2;
  function X(idx){ return ML+PW*idx/(N-1); }
  function Y(val){ return MT+PH*(1-(val-ymin)/(ymax-ymin)); }

  var sel=N-1;

  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.4)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(X(p-0.5),MT);ctx.lineTo(X(p-0.5),MT+PH);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';ctx.fillText('需 ≥12 个历史值',X(p)+4,MT+12);

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
    info.innerHTML='<div>预测第 <strong>t = '+sel+'</strong> 个点：ŷ = 截距 '+coef[0].toFixed(1)+' + Σ(权重×历史值) = <strong style="color:#fbbf24">'+pv.toFixed(1)+'</strong>　·　真实值 <strong style="color:#5eead4">'+av.toFixed(1)+'</strong>（误差 '+(pv-av>=0?'+':'')+(pv-av).toFixed(1)+'）</div>'+
      '<table><thead><tr><th>用到的历史值</th><th>权重 w</th><th>值 x</th><th>贡献 w·x</th><th></th></tr></thead><tbody>'+rows+'</tbody></table>';
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

> **看出门道了吗？** 同一组权重 $$w_1,\dots,w_{12}$$ 对**所有时刻通用**——这就是模型“学到的规律”；你点不同的点，变的只是它作用的那 12 个历史值，于是每个点的“贡献分解”都不一样。把这一行加权和扩成“一次输出 $$H$$ 个”，就是上一节的线性模型；再按 U 形层次堆叠，就是下一节的 KUN。

## 3. 通往 KUN

到这里，线性自回归的威力已经显现，但它也有天花板：**一层线性只能看一个尺度**。真实序列往往同时藏着长期趋势、中期周期和高频细节（多尺度）。

下一页的 **KUN（Kernel U-Net）** 正是把这里的“线性映射”当作一个**可插拔的核**，再按 U 形层次堆叠起来——于是同一个想法被推广到了多个尺度。换句话说，**你已经学会了 KUN 最基本的积木**。

---

**关键术语 (Key terms):** 自回归 AR(p)、AR(1) 与均值回复、随机游走、最小二乘 / Yule–Walker、回看窗口、递归 vs 直接多步、线性模型 (DLinear / NLinear)、线性核。
