---
updated: "2026-06-03"
lang: en
ref: forecasting
permalink: /en/forecasting/
title: "What is forecasting?"
lead: "Forecasting means using the past you already know to guess the future you don't. This page builds your intuition with pictures, a small game and a few real-world scenarios — the methods and formulas live in the introductory course."
prev: time-series
next: prediction-in-action
---

In one sentence: **forecasting = looking at a stretch of history and drawing the part that hasn't happened yet.**

## What forecasting does

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="Inferring the future from history">
  <defs>
    <marker id="ah-f" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <rect x="404" y="34" width="286" height="214" fill="color-mix(in srgb,var(--accent-2) 8%,transparent)"/>
  <line x1="52" y1="248" x2="694" y2="248" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <line x1="52" y1="248" x2="52" y2="28" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <text x="688" y="270" fill="var(--muted)" font-size="14" text-anchor="end">time →</text>
  <text x="44" y="34" fill="var(--muted)" font-size="14" text-anchor="end">value</text>
  <!-- uncertainty band -->
  <polygon points="404,150 466,124 528,110 590,114 652,100 652,132 590,146 528,142 466,156 404,150"
    fill="color-mix(in srgb,var(--accent-2) 16%,transparent)"/>
  <!-- history (solid line) -->
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="70,210 120,196 170,202 220,176 270,184 320,158 370,166 404,150"/>
  <g fill="var(--accent)">
    <circle cx="70" cy="210" r="3.5"/><circle cx="120" cy="196" r="3.5"/><circle cx="170" cy="202" r="3.5"/>
    <circle cx="220" cy="176" r="3.5"/><circle cx="270" cy="184" r="3.5"/><circle cx="320" cy="158" r="3.5"/>
    <circle cx="370" cy="166" r="3.5"/><circle cx="404" cy="150" r="4"/>
  </g>
  <!-- forecast (dashed line) -->
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"
    points="404,150 466,140 528,126 590,130 652,116"/>
  <!-- now -->
  <line x1="404" y1="34" x2="404" y2="248" stroke="var(--accent-2)" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="404" y="28" fill="var(--text)" font-size="13" text-anchor="middle">now</text>
  <text x="228" y="288" fill="var(--accent)" font-size="13" text-anchor="middle">looking back · known history</text>
  <text x="548" y="288" fill="var(--accent-2)" font-size="13" text-anchor="middle">forecast · not yet happened</text>
</svg>
<figcaption class="figcap">The solid line on the left is the <strong>known history</strong>, up to "now"; the dashed line on the right is the model's forecast of the <strong>future</strong>. The shaded band widens to the right because the further ahead you look, the less sure you can be — a good forecast gives a <strong>range</strong>, not just a single line.</figcaption>
</figure>

## Try it: you make the forecast

No formulas yet — just get a feel for it with your intuition.

<div class="game" markdown="0">
  <h3 style="margin-top:0">🎯 Guess the next value</h3>
  <p class="hint">The observed area first shows <strong>one full cycle</strong>, then <strong>half</strong> of the next. Spot the pattern, then click (or tap) to the <strong>right</strong> of "now" where you think the next value will land. <strong>5 rounds</strong> in total, and you get a score at the end.</p>
  <svg id="fc-svg" viewBox="0 0 560 280" role="img" aria-label="Mini-game: guess the next value">
    <line x1="34" y1="248" x2="540" y2="248" stroke="var(--muted)" stroke-width="1.3"/>
    <line x1="34" y1="248" x2="34" y2="20" stroke="var(--muted)" stroke-width="1.3"/>
    <g id="fc-dyn"></g>
  </svg>
  <p class="verdict" id="fc-verdict"></p>
  <div class="bar2">
    <button id="fc-next" type="button">Next →</button>
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
    // each h is "one full cycle (6 points) + half a cycle (3 points)" = 9 points; t is the value at the next phase
    var rounds=[
      {h:[190,200,150,95,90,140, 190,200,150],   t:95,  n:'Bubble tea shop daily sales'},
      {h:[200,130,85,150,110,80, 200,130,85],     t:150, n:'Hourly foot traffic'},
      {h:[95,92,98,110,185,195, 95,92,98],         t:110, n:'Website visits'},
      {h:[140,132,145,158,150,138, 140,132,145],   t:158, n:'Server room temperature'},
      {h:[200,175,188,150,165,120, 138,90,110],    t:70,  n:'Stock price'}
    ];
    var MAX=5;
    var idx=0, answered=false, played=0, totErr=0;
    function el(tag,a){var e=document.createElementNS(NS,tag);for(var k in a)e.setAttribute(k,a[k]);return e;}
    function val(y){return Math.round((bot-y)/2);}
    function guide(){return 'Click to the right of "now" and guess where the next value will land. ('+MAX+' rounds)';}
    function render(){
      answered=false; btn.disabled=true; while(dyn.firstChild) dyn.removeChild(dyn.firstChild);
      var r=rounds[idx];
      var pts=xs.map(function(x,i){return x+','+r.h[i];}).join(' ');
      dyn.appendChild(el('polyline',{points:pts,fill:'none',stroke:'var(--accent)','stroke-width':2.6,'stroke-linejoin':'round','stroke-linecap':'round'}));
      xs.forEach(function(x,i){dyn.appendChild(el('circle',{cx:x,cy:r.h[i],r:3.6,fill:'var(--accent)'}));});
      dyn.appendChild(el('line',{x1:nowX,y1:top,x2:nowX,y2:bot,stroke:'var(--accent-2)','stroke-width':1,'stroke-dasharray':'4 3'}));
      var nl=el('text',{x:nowX+4,y:top+12,fill:'var(--muted)','font-size':12}); nl.textContent='now'; dyn.appendChild(nl);
      var q=el('text',{x:futX,y:140,fill:'var(--muted)','font-size':24,'text-anchor':'middle',id:'fc-q'}); q.textContent='?'; dyn.appendChild(q);
      var lab=el('text',{x:40,y:18,fill:'var(--muted)','font-size':13}); lab.textContent='Scenario '+(played+1)+'/'+MAX+': '+r.n; dyn.appendChild(lab);
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
      var tl=el('text',{x:futX+12,y:r.t+4,fill:'var(--accent)','font-size':12}); tl.textContent='actual'; dyn.appendChild(tl);
      var ul=el('text',{x:futX+12,y:uy+4,fill:'var(--accent-2)','font-size':12}); ul.textContent='your guess'; dyn.appendChild(ul);
      var err=Math.abs(val(uy)-val(r.t)), pct=Math.round(100*err/Math.max(1,val(r.t)));
      var msg=pct<=5?'Spot on!':pct<=15?'Very close!':pct<=30?'Not bad.':'A bit off.';
      answered=true; played++; totErr+=pct;
      if(played<MAX){
        verdict.innerHTML='Round '+played+': off by <b>'+pct+'%</b>. '+msg+' Click "Next" to continue.';
        scoreEl.textContent='Progress '+played+'/'+MAX+' · average error so far '+Math.round(totErr/played)+'%';
        btn.textContent='Next →'; btn.dataset.mode='next'; btn.disabled=false;
      } else {
        finish(pct,msg);
      }
    }
    function finish(lastPct,lastMsg){
      var avg=Math.round(totErr/MAX), sc=Math.max(0,100-avg), pass=avg<=20;
      verdict.innerHTML='Round '+MAX+': off by <b>'+lastPct+'%</b>.<br>'+(pass
        ? '🎉 <b>Passed!</b> Average error over 5 rounds: '+avg+'%, score <b>'+sc+'/100</b>. You already have a good intuition for forecasting — read on.'
        : '🔁 <b>Try again.</b> Average error over 5 rounds: '+avg+'%, score <b>'+sc+'/100</b> — click "Restart" and get a better feel for the patterns before moving on.');
      scoreEl.textContent='Final score '+sc+'/100';
      btn.textContent='Restart'; btn.dataset.mode='reset'; btn.disabled=false;
    }
    function next(){ idx=(idx+1)%rounds.length; render(); verdict.innerHTML=guide(); }
    function reset(){ idx=0; played=0; totErr=0; scoreEl.textContent=''; render(); verdict.innerHTML=guide(); btn.textContent='Next →'; btn.dataset.mode='next'; }
    svg.addEventListener('click',answer);
    svg.addEventListener('touchstart',answer,{passive:false});
    btn.addEventListener('click',function(){ if(btn.dataset.mode==='reset') reset(); else next(); });
    reset();
  })();
  </script>
</div>

After a few rounds you will probably notice: **as long as one full cycle is visible, the next value can usually be read straight off it** — using "the value at the same phase in the previous cycle" as the forecast is the simplest and hardest-to-beat trick in forecasting (the **seasonal naive method**). The more complex the trend and the weaker the pattern (like that stock price), the harder it is to guess.

## Forecasting is everywhere

The same idea — "use the past to guess the future" — applied to different data becomes the decisions that every industry makes every day:

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌦️</div>
    <h3>Weather · Climate</h3>
    <p>A single missed rainstorm can overwhelm a city's drainage, ground flights and wipe out harvests, with losses from one disaster often running into the billions. Forecasters use numerical weather models and radar echo data to predict rainfall amounts and locations 6–72 hours ahead, then issue warnings, start drainage pumping stations and arrange flight diversions. This advance preparation saves a mid-sized city billions of yuan in weather-related losses each year — 0.1%–0.3% of GDP at the national scale.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">⚡</div>
    <h3>Electricity · Energy</h3>
    <p>Supply and demand on the grid must balance second by second; any imbalance risks widespread tripping or even total grid collapse — the 2021 Texas blackout caused nearly 200 billion dollars in economic losses. Dispatchers use load forecasting models to anticipate peak load and wind and solar output curves 24 hours ahead, then schedule thermal unit start-ups and shutdowns, storage charging and discharging windows, and cross-regional dispatch. Accurate forecasts let power plants avoid rolling blackouts and save a provincial grid tens of millions of yuan in peaking fuel costs every year.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📦</div>
    <h3>Sales · Inventory</h3>
    <p>Stock too much and cash sits locked up in warehouses; stock too little and bestsellers sell out and customers walk away — global retail loses more than 1.1 trillion dollars a year to inventory mistakes. Supply-chain teams use time series models to forecast each SKU's sales over the next 1–4 weeks, then place purchase orders early, plan transfers between warehouses and time promotions. Every percentage point of extra forecast accuracy improves inventory turnover by 2%–3%, directly freeing up tens of millions in working capital.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚗</div>
    <h3>Traffic · Mobility</h3>
    <p>Morning and evening rush-hour congestion wastes hundreds of hours of commuting per person each year; in Beijing alone, the cost of congestion exceeds 100 billion yuan. Traffic control centers use historical and real-time traffic data to forecast flow on every road segment 30 minutes ahead, then adjust signal timing, open reversible lanes and publish diversion guidance. These advance measures can cut average commute times by 10%–15%, improving travel for millions of people every day.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🏥</div>
    <h3>Health · Disease</h3>
    <p>During an epidemic outbreak, once ICU beds and ventilators run out, death rates can multiply — during COVID-19, health systems in several countries were overwhelmed this way. Epidemiologists use time series and SIR-type models to forecast case growth over the next 2–4 weeks, then mobilize medical staff, redistribute ventilators and build field hospitals in advance. An accurate forecast two weeks ahead lets hospitals respond calmly instead of being swamped, cutting severe-case mortality by 20%–30%.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📈</div>
    <h3>Finance · Risk</h3>
    <p>When a "black swan" event strikes, an institution that hasn't controlled its positions can be wiped out in a single day — the collapse of Lehman Brothers in 2008 erased 22 trillion dollars of global market value. Risk teams use volatility models such as GARCH and VaR to forecast tail risk and the probability of extreme losses, then cut leverage, buy hedging options and adjust margin levels in advance. Accurate risk forecasts keep an institution's maximum drawdown in extreme markets within tolerable limits, so it doesn't go under overnight.</p>
  </div>
</div>

## So "how" do you forecast?

This page only aims to help you <strong>see and play your way to understanding "what forecasting is"</strong>. The actual "how" — the full workflow, the baselines you must beat, everything from classical models to deep learning, and how to <strong>honestly measure how good a forecast is</strong> — is laid out in the structured introductory course:

<div class="note" markdown="1">
- For methods and formulas: the [time series introductory course](../course/), in which [Lecture 2 · Data preparation](../course/02/) (splitting, backtesting, avoiding leakage), [Lecture 4 · Visualization](../course/04/) (analyzing results, inspecting residuals) and [Lecture 3 · Linear models](../course/03/) cover exactly "measuring quality" and "beating the baseline first".
- To experience forecasting hands-on: turn to the next page, [A successful forecast](../prediction-in-action/) — an artillery game that teaches fitting and extrapolation.
- To jump straight into a modern model: go to [Using KUN](../kun/).
</div>
