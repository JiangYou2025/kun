---
updated: "2026-06-11"
layout: history
lang: en
permalink: /en/applications/
title: "Applications in the Wild"
lead: "Theory and models ultimately have to land in real settings. This section is organised by domain, and each scenario spells out what the time series look like there, what has to be forecast or detected, what makes it hard, and which methods are commonly used — always linking back to the matching chapters of the course and the history."
---

> One of the sections alongside the [history](../history/), [prehistory and modern applications](../prehistory/), [the nature of time](../nature-of-time/) and [paradoxes of time](../paradoxes/). Companions: [introductory course](../course/) · [using KUN](../kun/).

## Why organise by scenario

The [history](../history/) tells how methods evolved, and the [course](../course/) tells how to use them; this section takes a different cut — **starting from the domain**. The task is always "predict the next stretch of the series", yet finance cares about risk and tails, power grids about peaks and dispatch, medicine about early warning, and meteorology about spatio-temporal fields. The shape of the data, the evaluation criteria and the acceptable costs all differ, and so does the choice of model.

As you read, you will keep meeting the same set of methods (ARIMA, exponential smoothing, GBDT, LSTM, Transformer, state space models) tailored anew to each scenario — which is exactly the process of matching tools to problems.

## Ten scenarios

| # | Scenario | Typical tasks | The difficulty in one line |
|---|------|---------|-----------|
| 1 | [Finance & economics](finance/) | Returns, volatility, risk | Extremely low signal-to-noise ratio; tails can kill |
| 2 | [Energy & power](energy/) | Load forecasting, renewable output | Strong seasonality + weather coupling + must be dispatchable |
| 3 | [Retail & supply chain](retail/) | Demand forecasting, replenishment and pricing | Huge numbers of intermittent series + promotions/holidays |
| 4 | [Transportation & mobility](transport/) | Traffic flow, ETA, trajectories | Spatio-temporally coupled network structure |
| 5 | [Healthcare & health](health/) | Vital signs, epidemics | High stakes, irregular sampling, must be interpretable |
| 6 | [Weather & climate](weather/) | Weather forecasting, climate projection | High-dimensional spatio-temporal fields, chaotic limit |
| 7 | [Industry & IoT](industry/) | Predictive maintenance, process monitoring | Many sensors + scarce fault labels |
| 8 | [Communications & signals](signal/) | Speech, channels, radar tracking | High sampling rates, hard real time, noise |
| 9 | [Astronomy & geophysics](geophysics/) | Sunspots, tides, earthquakes | Very long time spans, rare major events |
| 10 | [Natural language & sequences](language/) | Language models, sequence modelling | Discrete symbols, very long dependencies |

> One page per scenario. Reading them in order is recommended, but you can also jump straight to the domain you care about.
