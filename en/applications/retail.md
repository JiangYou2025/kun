---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 3 · Retail & supply chain"
permalink: /en/applications/retail/
title: "Retail & Supply Chain"
lead: "Millions of SKUs, one curve per store per day — the difficulty of retail forecasting lies not in how complex any single series is, but in their sheer number, their sparse and intermittent nature, and the repeated disruption of promotions and holidays."
math: false
prev: /applications/energy/
next: /applications/transport/
---

> This is scenario 3 of the [time series applications](../) section.

## Data and tasks

- **Data**: daily / weekly sales per SKU × store, prices, promotion flags, inventory, weather and holiday calendars.
- **Tasks**: demand forecasting, replenishment and safety stock, dynamic pricing, cold start for new products.

## What makes it special

- **Massive numbers of series**: millions of SKU×store combinations make series-by-series modelling impractical, so **global models** are needed (one model consumes all the series).
- **Intermittent demand**: many series are full of zeros (lots of products simply sell nothing on a given day), and ordinary models break down.
- **Strong exogenous shocks**: promotions, markdowns, holidays and price elasticity often explain sales better than the historical trend.
- **Business-oriented evaluation**: what matters is stock-out rate, inventory turnover and weighted quantile loss, not simply MAE.

## Common methods

- Methods specialised for intermittent demand: **Croston / SBA**.
- The global deep probabilistic model **DeepAR** (history [9](../../history/09/)), which learns what tens of millions of series have in common in one go.
- GBDT + rich calendar / promotion features (course [13](../../course/13/)).
- **Quantile forecasts** that directly serve safety-stock decisions ([14](../../course/14/)).

## A representative case: the M5 competition

The 2020 M5 competition (hierarchical Walmart sales) all but defined today's retail forecasting paradigm: the winning solution used **LightGBM + heavy feature engineering**, while the probabilistic track was dominated by global neural networks. It also brought "**evaluation by quantiles**" to the fore — because a replenishment decision fundamentally needs a particular quantile of the distribution, not its mean.

---

**Key terms:** intermittent demand, Croston, global model, DeepAR, promotion / calendar features, quantile loss, safety stock.
