---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/course/wave-types/
title: "Wave Types and Forecasting"
lead: "Real-world time series are almost always a superposition of several waveforms. Only by recognizing the basic ones — trend, cycle, decay, abrupt change — can you pick the right forecasting tool. This page lets you take waveforms apart yourself with an interactive chart."
prev: /course/04/
next: /course/05/
---

## Why understand waveforms?

In the artillery mini-game you fitted a trajectory with a parabola. But real data rarely has just one shape — stock prices, temperature, electricity consumption, ECGs are almost all the result of **several waveforms superimposed**.

Understanding waveforms = understanding the "skeleton" of the data. Read the skeleton correctly and the forecast is half done.

## Six basic waveforms

<div class="game" markdown="0">
<h3 style="margin-top:0">🌊 Meet the basic waveforms</h3>
<p class="hint">Click the labels below to switch between waveform types and observe their shapes and real-world counterparts.</p>

<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px">
  <button class="wave-btn active" data-wave="sine">Sine wave</button>
  <button class="wave-btn" data-wave="trend">Trend</button>
  <button class="wave-btn" data-wave="damped">Damped wave</button>
  <button class="wave-btn" data-wave="square">Square wave</button>
  <button class="wave-btn" data-wave="composite">Composite wave</button>
  <button class="wave-btn" data-wave="noise">Noise</button>
</div>

<canvas id="wave-canvas" width="560" height="260" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface)"></canvas>
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
  var W=560,H=260,mid=H/2;
  var descEl=document.getElementById('wave-desc');
  var btns=document.querySelectorAll('.wave-btn');

  var waves={
    sine:{
      fn:function(x){return Math.sin(x*0.05)*80;},
      color:'#5eead4',
      desc:'📐 Sine wave — the most basic periodic signal. Daily temperature swings, tides and alternating current are all roughly sinusoidal. Fixed period, constant amplitude: it is the cornerstone of the Fourier transform, since any periodic signal can be decomposed into a sum of sine waves. Forecasting a sine wave only requires finding its frequency and phase, making it the "easiest to forecast" type.',
      pred:'✅ Very easy to forecast: just determine the period and amplitude'
    },
    trend:{
      fn:function(x){return -80+x*0.3+Math.sin(x*0.08)*12;},
      color:'#fbbf24',
      desc:'📈 Trend — values keep rising or falling over time. GDP growth, global warming and chip performance under Moore\'s law all show a clear trend. A trend can be linear, exponential or even logarithmic. The key to forecasting a trend is judging whether it will continue or reverse.',
      pred:'⚠️ Medium difficulty: when the trend reverses is the biggest uncertainty'
    },
    damped:{
      fn:function(x){return Math.sin(x*0.06)*80*Math.exp(-x*0.005);},
      color:'#f0abfc',
      desc:'🔔 Damped wave — the amplitude of oscillation decreases over time. Aftershocks following an earthquake, damped spring vibrations, the decay of a drug\'s concentration in the blood. Very common in physical systems. Forecasting a damped wave requires estimating both the frequency and the decay rate.',
      pred:'⚠️ Medium difficulty: the frequency is easy to find, the decay rate needs a long enough observation'
    },
    square:{
      fn:function(x){return Math.sign(Math.sin(x*0.04))*60;},
      color:'#fb923c',
      desc:'⬜ Square wave — switches abruptly between two values. On/off signals, factory shifts (day/night), traffic-light cycles. The hallmark of a square wave is that changes happen instantly, with constant values in between. Forecasting a square wave means pinpointing the switching times.',
      pred:'✅ Easy to forecast if the period is fixed, hard if switching is irregular'
    },
    composite:{
      fn:function(x){return Math.sin(x*0.03)*35+Math.sin(x*0.12)*20+x*0.08-20+Math.sin(x*0.007)*30;},
      color:'#818cf8',
      desc:'🎼 Composite wave — a superposition of several frequencies plus a trend, the most common form of real data. Electricity consumption = yearly cycle + weekly cycle + daily cycle + long-term trend + random fluctuation. Decomposing composite waves is the core technique of time-series analysis (Fourier transform, wavelet decomposition, STL decomposition, etc.).',
      pred:'⚠️ Decompose first, forecast each component separately, then recombine'
    },
    noise:{
      fn:function(x){return (Math.sin(x*37.7)*43758.5453%1-0.5)*120;},
      color:'#ef4444',
      desc:'🎲 Pure noise — completely random, with no exploitable pattern. Dice rolls, quantum measurements, the micro-fluctuations in high-frequency stock prices. Pure noise is unpredictable — a basic theorem of information theory. Any model that claims to forecast pure noise is overfitting.',
      pred:'❌ Unpredictable: this is the theoretical limit of forecasting'
    }
  };

  var curWave='sine';

  function draw(){
    ctx.clearRect(0,0,W,H);
    // grid
    ctx.strokeStyle='rgba(150,160,180,0.1)';ctx.lineWidth=1;
    for(var i=0;i<W;i+=50){ctx.beginPath();ctx.moveTo(i,0);ctx.lineTo(i,H);ctx.stroke();}
    for(var j=0;j<H;j+=40){ctx.beginPath();ctx.moveTo(0,j);ctx.lineTo(W,j);ctx.stroke();}
    // centre line
    ctx.strokeStyle='rgba(150,160,180,0.3)';ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(0,mid);ctx.lineTo(W,mid);ctx.stroke();ctx.setLineDash([]);

    var w=waves[curWave];
    // known part (0-70%)
    var split=Math.floor(W*0.7);
    ctx.strokeStyle=w.color;ctx.lineWidth=2.5;ctx.beginPath();
    for(var x=0;x<split;x++){var y=mid-w.fn(x);if(x===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);}
    ctx.stroke();

    // forecast part (70-100%)
    ctx.setLineDash([5,4]);ctx.strokeStyle=w.color;ctx.lineWidth=2;ctx.globalAlpha=0.6;ctx.beginPath();
    for(var x2=split;x2<W;x2++){var y2=mid-w.fn(x2);if(x2===split)ctx.moveTo(x2,y2);else ctx.lineTo(x2,y2);}
    ctx.stroke();ctx.setLineDash([]);ctx.globalAlpha=1;

    // split line
    ctx.strokeStyle='rgba(150,160,180,0.5)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(split,0);ctx.lineTo(split,H);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
    ctx.fillText('← Known',split-62,18);ctx.fillText('Forecast →',split+8,18);

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

## From waveform to forecasting strategy

Different waveforms call for different forecasting tools:

| Waveform | Difficulty | Suitable methods | Real-world examples |
|------|---------|-----------|---------|
| Sine wave | ⭐ | Fourier analysis, trigonometric fitting | Tides, daily temperature range, alternating current |
| Trend | ⭐⭐ | Linear regression, exponential smoothing | GDP, population growth, inflation |
| Damped wave | ⭐⭐ | Parametric physical models | Aftershocks, drug metabolism, spring vibration |
| Square wave | ⭐⭐ | Change-point detection, HMM | Shift schedules, traffic lights, equipment on/off |
| Composite wave | ⭐⭐⭐ | Decomposition + separate forecasts (STL, wavelets) | Electricity use, sales, air temperature |
| Pure noise | ⭐⭐⭐⭐⭐ | **Unpredictable** — only a probability distribution can be given | Dice, quantum noise |

## Real data = composite wave + noise

Almost every real time series is a mixture of **signal (predictable waveforms) + noise (the unpredictable random part)**.

Forecasting essentially comes down to three steps:

1. **Decompose**: split the data into trend, seasonality and residual (noise).
2. **Forecast separately**: forecast each component with a suitable method.
3. **Recombine**: add the forecasts back together.

> Splitting "composite wave = signal + noise" apart and forecasting each part separately is the subject of [Lecture 4 · Components and decomposition](../04/); the "stationary / unpredictable" part is handled in [Lecture 5 · Stationarity](../05/).
