---
updated: "2026-06-03"
lang: en
ref: time-series
permalink: /en/time-series/
title: "What is a time series?"
lead: "One page to see what a time series looks like. It is mostly pictures, and it introduces only the two most basic words: variable and value. Formulas and methods (stationarity, autocorrelation, decomposition, sliding windows…) are in the introductory course."
next: forecasting
---

In one sentence: **a time series is the "values" of a variable laid out in a line along "time".** Let's look at a few pictures.

## What a time series looks like

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="Line chart of a time series">
  <defs>
    <marker id="ah-a" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <line x1="52" y1="248" x2="694" y2="248" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-a)"/>
  <line x1="52" y1="248" x2="52" y2="28" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-a)"/>
  <text x="688" y="270" fill="var(--muted)" font-size="14" text-anchor="end">Time →</text>
  <text x="44" y="34" fill="var(--muted)" font-size="14" text-anchor="end">Value</text>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"
    points="72,210 124,190 176,200 228,168 280,150 332,164 384,128 436,140 488,108 540,92 592,104 644,78"/>
  <g fill="var(--accent)">
    <circle cx="72" cy="210" r="3.5"/><circle cx="124" cy="190" r="3.5"/><circle cx="176" cy="200" r="3.5"/>
    <circle cx="228" cy="168" r="3.5"/><circle cx="280" cy="150" r="3.5"/><circle cx="332" cy="164" r="3.5"/>
    <circle cx="384" cy="128" r="3.5"/><circle cx="436" cy="140" r="3.5"/><circle cx="488" cy="108" r="3.5"/>
    <circle cx="540" cy="92" r="3.5"/><circle cx="592" cy="104" r="3.5"/><circle cx="644" cy="78" r="3.5"/>
  </g>
  <line x1="384" y1="128" x2="384" y2="248" stroke="var(--accent-2)" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="384" y1="128" x2="52" y2="128" stroke="var(--accent-2)" stroke-width="1" stroke-dasharray="4 3"/>
  <circle cx="384" cy="128" r="5.5" fill="none" stroke="var(--accent-2)" stroke-width="2"/>
  <text x="398" y="118" fill="var(--text)" font-size="14">One point = (time, value)</text>
</svg>
<figcaption class="figcap">The horizontal axis is <strong>time</strong>; the vertical axis is the <strong>value</strong> measured at each moment. Every point on the chart is a pair: "a certain time" and "the value at that time". Examples are everywhere: daily temperature, hourly electricity use, a stock's closing price, the number of patients seen each day.</figcaption>
</figure>

## Variable and value

There are only two words to remember:

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 230" role="img" aria-label="Diagram of a variable and its values">
  <defs>
    <marker id="ah-b" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <rect x="20" y="82" width="150" height="60" rx="10" fill="color-mix(in srgb,var(--accent) 14%,transparent)" stroke="var(--accent)"/>
  <text x="95" y="107" fill="var(--text)" font-size="14" text-anchor="middle" font-weight="600">Variable</text>
  <text x="95" y="128" fill="var(--muted)" font-size="13" text-anchor="middle">Temperature (°C)</text>
  <line x1="174" y1="112" x2="216" y2="112" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-b)"/>
  <text x="232" y="58" fill="var(--muted)" font-size="13">Values:</text>
  <g font-size="14" text-anchor="middle">
    <rect x="258" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="280" y="101" fill="var(--text)">12</text>
    <rect x="334" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="356" y="101" fill="var(--text)">14</text>
    <rect x="410" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="432" y="101" fill="var(--text)">13</text>
    <rect x="486" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="508" y="101" fill="var(--text)">16</text>
    <rect x="562" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="584" y="101" fill="var(--text)">18</text>
    <rect x="638" y="80" width="44" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)"/><text x="660" y="101" fill="var(--text)">21</text>
  </g>
  <g stroke="var(--border)" stroke-dasharray="3 3">
    <line x1="280" y1="112" x2="280" y2="158"/><line x1="356" y1="112" x2="356" y2="158"/><line x1="432" y1="112" x2="432" y2="158"/>
    <line x1="508" y1="112" x2="508" y2="158"/><line x1="584" y1="112" x2="584" y2="158"/><line x1="660" y1="112" x2="660" y2="158"/>
  </g>
  <line x1="232" y1="158" x2="704" y2="158" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-b)"/>
  <g font-size="12" text-anchor="middle" fill="var(--muted)">
    <text x="280" y="178">t₁</text><text x="356" y="178">t₂</text><text x="432" y="178">t₃</text>
    <text x="508" y="178">t₄</text><text x="584" y="178">t₅</text><text x="660" y="178">t₆</text>
  </g>
  <text x="700" y="200" fill="var(--muted)" font-size="13" text-anchor="end">Time →</text>
</svg>
<figcaption class="figcap">The <strong>variable</strong> is the thing you observe or measure (temperature, electricity use, a stock price); a <strong>value</strong> is the number it takes at each point in time. A time series = one variable, with a string of values over a sequence of time points.</figcaption>
</figure>

## One variable, or several?

<div class="fig-2" markdown="0">
<figure class="fig">
<svg viewBox="0 0 320 190" role="img" aria-label="Univariate time series">
  <line x1="30" y1="160" x2="300" y2="160" stroke="var(--muted)" stroke-width="1.3"/>
  <line x1="30" y1="160" x2="30" y2="22" stroke="var(--muted)" stroke-width="1.3"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"
    points="40,128 86,116 132,132 178,100 224,112 270,82 296,92"/>
  <text x="40" y="42" fill="var(--accent)" font-size="13">Temperature</text>
</svg>
<figcaption class="figcap"><strong>Univariate</strong>: tracks a single variable.</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 190" role="img" aria-label="Multivariate time series">
  <line x1="30" y1="160" x2="300" y2="160" stroke="var(--muted)" stroke-width="1.3"/>
  <line x1="30" y1="160" x2="30" y2="22" stroke="var(--muted)" stroke-width="1.3"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,128 86,116 132,132 178,100 224,112 270,82 296,92"/>
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,96 86,108 132,90 178,118 224,96 270,120 296,104"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"
    points="40,142 86,134 132,146 178,138 224,150 270,136 296,148"/>
  <g font-size="12">
    <text x="44" y="40" fill="var(--accent)">Temp.</text>
    <text x="120" y="40" fill="var(--accent-2)">Humidity</text>
    <text x="196" y="40" fill="#fbbf24">Power</text>
  </g>
</svg>
<figcaption class="figcap"><strong>Multivariate</strong>: records several variables at once, which are often related to one another. KUN is designed precisely for the multivariate case.</figcaption>
</figure>
</div>

## Common "shapes" in the data

Getting familiar with the pictures matters more than memorizing definitions — most series hide the following shapes.

<div class="fig-2" markdown="0">
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="Trend">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="40,128 88,118 136,104 184,90 232,74 288,52"/>
</svg>
<figcaption class="figcap"><strong>Trend</strong>: a long-term movement in one direction (such as a population growing year after year).</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="Seasonality">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="40,82 64,52 88,46 112,68 136,100 160,116 184,108 208,80 232,50 256,46 280,66 300,98"/>
</svg>
<figcaption class="figcap"><strong>Seasonality</strong>: repeats on a fixed cycle (such as ice-cream sales every summer).</figcaption>
</figure>
<figure class="fig">
<svg viewBox="0 0 320 170" role="img" aria-label="Noise">
  <line x1="28" y1="142" x2="300" y2="142" stroke="var(--muted)" stroke-width="1.2"/>
  <line x1="28" y1="142" x2="28" y2="20" stroke="var(--muted)" stroke-width="1.2"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"
    points="40,92 64,60 88,108 112,72 136,118 160,58 184,104 208,80 232,120 256,64 280,100 300,78"/>
</svg>
<figcaption class="figcap"><strong>Noise</strong>: irregular random fluctuations with no pattern to grab onto.</figcaption>
</figure>
</div>

## Want to go further?

<div class="note" markdown="1">
**This page is only about "reading the picture".** For the real technical content — stationarity, differencing, autocorrelation, decomposition formulas, how to cut a series into training samples — see the systematic [introductory course on time series](../course/). When you are ready to make forecasts yourself, turn to the next page, [How to forecast](../forecasting/).
</div>
