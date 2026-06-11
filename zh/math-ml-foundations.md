---
updated: "2026-06-11"
lang: zh
ref: math-ml-foundations
permalink: /zh/math-ml-foundations/
title: "数学和机器学习基础"
lead: "上一页你亲手拟合了一条弹道。但凭什么这条曲线就是对的？这一页用最少的数学语言，讲清预测背后的三件事：用函数描述规律、用优化找到最好的规律、用机器学习从数据里把规律学出来。只讲直觉，不堆公式。"
prev: prediction-in-action
next: frontier-2026
math: true
---

## 从"手动调参"到"自动学习"

上一页的炮兵游戏里，你不停地调角度和力度，直到弹道命中目标。这其实就是预测的核心循环——只不过你是用眼睛和手在做。机器学习要做的，是把这个循环**自动化**：

1. 用一个**函数**描述可能的规律；
2. 定义什么叫"拟合得好"；
3. 让计算机**自动**找到最好的那条曲线。

这三步分别对应三块基础：函数、优化、机器学习。下面逐个拆开。

## 1. 函数：用数学描述规律

一条规律，本质上就是"输入 → 输出"的映射。我们写成：

$$\hat{y} = f_\theta(x)$$

- $x$ 是输入（时间、过去的观测值……）
- $\hat{y}$ 是预测输出
- $\theta$ 是**参数**——炮兵游戏里的角度和力度，就是这里的 $\theta$

换一组 $\theta$，就换一条曲线。所有可能的 $\theta$ 张成一个"曲线的空间"，预测就是在这个空间里**挑一条最贴合数据的**。

> 直觉：函数是"形状的模板"，参数是"旋钮"。直线 $f(x)=ax+b$ 有两个旋钮，抛物线有三个，神经网络有上百万个。旋钮越多，能拟合的形状越复杂——但也越容易"想多了"（见第 3 节）。

## 2. 优化：怎样算"拟合得好"

要让计算机自动调旋钮，先得告诉它**什么是好**。办法是定义一个**损失函数**，衡量预测和真实值差多少。最常用的是均方误差：

$$L(\theta) = \frac{1}{n}\sum_{i=1}^{n}\big(y_i - f_\theta(x_i)\big)^2$$

差得越多，$L$ 越大。于是"拟合得好"就变成了一个明确的目标：**让 $L$ 最小**。

怎么找最小值？想象 $L$ 是一片山谷，你蒙着眼睛站在山坡上，想走到谷底。最稳的办法是：**摸出脚下最陡的下坡方向，迈一小步，再重复**。这就是**梯度下降**——现代几乎所有模型的训练方式：

$$\theta \leftarrow \theta - \eta \,\nabla L(\theta)$$

其中 $\eta$ 是**学习率**，也就是每步迈多大。步子太大会越过谷底来回震荡，太小则慢得让人崩溃。

<div class="game" markdown="0">
<h3 style="margin-top:0">🎯 亲手体验：拟合 vs 过拟合</h3>
<p class="hint">拖动滑块改变模型复杂度（多项式次数），观察曲线如何从"太简单"走向"想太多"。</p>

<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:10px">
  <label style="font-size:.9rem">模型复杂度：<strong id="deg-val">1</strong> 次</label>
  <input id="deg-slider" type="range" min="1" max="12" value="1" style="flex:1;min-width:160px">
</div>

<canvas id="fit-canvas" width="560" height="280" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface)"></canvas>
<p id="fit-desc" style="margin-top:10px;font-size:.93rem;color:var(--muted)"></p>

<script>
(function(){
  var canvas=document.getElementById('fit-canvas');
  if(!canvas)return;
  var ctx=canvas.getContext('2d');
  var W=560,H=280,padX=30,padY=24;
  var slider=document.getElementById('deg-slider');
  var degVal=document.getElementById('deg-val');
  var descEl=document.getElementById('fit-desc');

  // 固定的"真实规律"+噪声，用确定性伪随机保证每次刷新一致
  var seed=12345;
  function rnd(){seed=(seed*1103515245+12345)&0x7fffffff;return seed/0x7fffffff;}
  var pts=[];
  for(var i=0;i<14;i++){
    var t=i/13;
    var truth=0.5+0.35*Math.sin(t*Math.PI*1.5);   // 平滑的真实曲线
    var noisy=truth+(rnd()-0.5)*0.22;              // 加噪声
    pts.push({t:t,y:Math.max(0.05,Math.min(0.95,noisy))});
  }

  // 用最小二乘解多项式拟合（正规方程，规模小，直接高斯消元）
  function polyfit(deg){
    var n=deg+1, X=[], Y=[];
    for(var r=0;r<n;r++){
      X.push([]); var sy=0;
      for(var c=0;c<n;c++){
        var s=0;
        for(var k=0;k<pts.length;k++) s+=Math.pow(pts[k].t,r+c);
        X[r].push(s);
      }
      for(var k2=0;k2<pts.length;k2++) sy+=Math.pow(pts[k2].t,r)*pts[k2].y;
      Y.push(sy);
    }
    // 高斯消元
    for(var col=0;col<n;col++){
      var piv=X[col][col]||1e-9;
      for(var cc=col;cc<n;cc++)X[col][cc]/=piv; Y[col]/=piv;
      for(var rr=0;rr<n;rr++){
        if(rr===col)continue;
        var f=X[rr][col];
        for(var cc2=col;cc2<n;cc2++)X[rr][cc2]-=f*X[col][cc2];
        Y[rr]-=f*Y[col];
      }
    }
    return Y; // 系数
  }
  function evalPoly(coef,t){var s=0;for(var i=0;i<coef.length;i++)s+=coef[i]*Math.pow(t,i);return s;}

  function px(t){return padX+t*(W-2*padX);}
  function py(y){return H-padY-y*(H-2*padY);}

  function draw(){
    var deg=parseInt(slider.value,10);
    degVal.textContent=deg;
    ctx.clearRect(0,0,W,H);
    // 网格
    ctx.strokeStyle='rgba(150,160,180,0.12)';ctx.lineWidth=1;
    for(var gx=0;gx<=10;gx++){var x=px(gx/10);ctx.beginPath();ctx.moveTo(x,padY);ctx.lineTo(x,H-padY);ctx.stroke();}
    for(var gy=0;gy<=8;gy++){var y=py(gy/8);ctx.beginPath();ctx.moveTo(padX,y);ctx.lineTo(W-padX,y);ctx.stroke();}

    // 拟合曲线
    var coef=polyfit(deg);
    ctx.strokeStyle='#5eead4';ctx.lineWidth=2.5;ctx.beginPath();
    for(var s=0;s<=200;s++){
      var t=s/200, v=evalPoly(coef,t);
      var X=px(t),Yv=py(v);
      if(s===0)ctx.moveTo(X,Yv);else ctx.lineTo(X,Yv);
    }
    ctx.stroke();

    // 数据点
    ctx.fillStyle='#fbbf24';
    pts.forEach(function(p){ctx.beginPath();ctx.arc(px(p.t),py(p.y),4,0,Math.PI*2);ctx.fill();});

    var msg;
    if(deg<=1)msg='📉 <strong>欠拟合</strong>：直线太简单，抓不住数据的弯曲——偏差大。';
    else if(deg<=4)msg='✅ <strong>恰到好处</strong>：曲线顺着主趋势走，又不去追每个噪声点——泛化最好。';
    else msg='🌀 <strong>过拟合</strong>：曲线扭来扭去穿过几乎每个点，把噪声也"学"了进去——换一批新数据就会崩。';
    descEl.innerHTML=msg;
  }

  slider.addEventListener('input',draw);
  draw();
})();
</script>
</div>

## 3. 机器学习：从数据里把规律学出来

把前两节合起来，就是机器学习的基本范式：**不手写规则，而是给一堆数据，让模型自己调参数去拟合**。常见的两类：

- **监督学习**：数据带"标准答案"，学输入到输出的映射（预测就属于这类——用过去的窗口预测未来的值）。
- **无监督学习**：数据没有答案，找隐藏结构（聚类、降维）。

但机器学习真正的难点，不是"把训练数据拟合好"，而是**在没见过的数据上也表现好**——这叫**泛化**。上面的滑块演示就是这件事的缩影：

| 现象 | 表现 | 原因 |
|------|------|------|
| **欠拟合** | 训练、测试都差 | 模型太简单，偏差大 |
| **过拟合** | 训练好、测试差 | 模型太复杂，记住了噪声，方差大 |
| **刚刚好** | 训练、测试都不错 | 复杂度匹配数据 |

这就是著名的**偏差—方差权衡**。为了不让模型"想太多"，人们用各种**正则化**手段（限制旋钮乱动、提前停止训练等），并且永远在**没参与训练的测试集**上检验效果。

> 一句话总结：预测 = 选一个函数族（形状）+ 用优化找最好的参数（拟合）+ 用泛化判断学得好不好（不被噪声骗）。

## 为什么这些对预测很重要

回到时间序列。一条真实序列既有可预测的规律，也有不可预测的噪声。模型的本事，就是**学到规律、忽略噪声**——既不欠拟合（漏掉趋势和周期），也不过拟合（把随机抖动当成规律）。

而现代预测模型（包括后面要讲的 KUN）之所以强大，正是因为它们用了**参数极多的神经网络**——旋钮成百上千万。旋钮越多，能表达的规律越复杂，但过拟合的风险也越大。如何在"表达力"和"泛化"之间取得平衡，正是 2026 年前沿研究的核心战场之一。

> 下一页，我们就去看看：站在一百年方法演进的终点，今天的预测研究还在攻克哪些硬骨头？

---

**关键术语：** 函数 / 参数 $\theta$、损失函数、均方误差、梯度下降、学习率、监督 / 无监督学习、泛化、欠拟合 / 过拟合、偏差—方差权衡、正则化、测试集。
