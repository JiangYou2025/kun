---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 2 · Energy"
permalink: /en/applications/energy/
title: "Energy & Power"
lead: "Electricity cannot be stored at scale, so supply and demand must balance in real time — which makes power load forecasting one of the time series tasks with the most direct consequences: get it slightly wrong and you either waste fuel or cut the power."
math: false
prev: /applications/finance/
next: /applications/retail/
---

> This is scenario 2 of the [time series applications](../) section.

## Data and tasks

- **Data**: regional / building power load, wind and solar output, electricity prices, gas consumption, and weather variables such as temperature and irradiance.
- **Tasks**: short-term load forecasting (STLF), renewable power forecasting, electricity price forecasting, demand response and dispatch optimisation.

## What makes it special

- **Multiple seasonality**: three overlapping cycles — daily (morning and evening peaks), weekly (weekdays/weekends) and yearly (cold and warm seasons).
- **Strong coupling with weather**: temperature drives air-conditioning and heating load, wind speed / irradiance drive renewable output; weather is the number-one exogenous variable.
- **Very real consequences**: forecasts directly drive unit dispatch, errors carry real monetary and physical costs, and supply and demand must be balanced at every moment.
- **Probabilistic forecasts are a must**: to decide how much spinning reserve to hold, the grid needs an "output distribution", not just a single point.

## Common methods

- Multi-seasonal baselines + **Holt-Winters / multi-seasonal ETS** (course [12](../../course/12/)).
- Regression / GBDT with exogenous weather variables ([13](../../course/13/)).
- Deep learning for long and multivariate series, outputting probabilistic forecasts directly ([9](../../course/09/), [14](../../course/14/)).

## A representative case: probabilistic forecasting of renewable output

Wind and solar output swing sharply with the weather, and grid dispatch does not need "output at 18:00 tomorrow = 42 MW" but rather "how likely is it to fall below 30 MW". **Quantile / probabilistic forecasting** ([14](../../course/14/)) has therefore become standard for grid dispatch — only by quantifying the uncertainty can reserve capacity be planned sensibly.

---

**Key terms:** load forecasting (STLF), multiple seasonality, exogenous variables, probabilistic / quantile forecasting, demand response, renewable output.
