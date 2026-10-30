---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 4 · Transportation"
permalink: /en/applications/transport/
title: "Transportation & Mobility"
lead: "Congestion on one road spreads downstream through the network — from the very start, traffic forecasting has never been about a single curve, but about an entire graph evolving over time."
math: false
prev: /applications/retail/
next: /applications/health/
---

> This is scenario 4 of the [time series applications](../) section.

## Data and tasks

- **Data**: speed / flow from road-network sensors (inductive loops, cameras), travel demand, vehicle and pedestrian trajectories, ride-hailing orders.
- **Tasks**: short-term traffic state forecasting, estimated time of arrival (ETA), trajectory prediction, origin–destination (OD) demand forecasting.

## What makes it special

- **Spatio-temporal coupling**: upstream congestion propagates downstream and neighbouring road segments are highly correlated — by nature a **graph-structured** problem.
- **Strong periodicity + event shocks**: daily / weekly commuting patterns are stable, but accidents, weather and large events can suddenly disrupt them.
- **Real-time requirements**: navigation and dispatch need updates within seconds.

## Common methods

- **Spatio-temporal graph neural networks (STGNN)**: DCRNN, Graph WaveNet and others model the road network as a graph, capturing spatial topology and temporal evolution together.
- Classical baseline: a seasonal ARIMA run separately on each road segment (course [8](../../course/08/)) as a point of comparison.
- Trajectory prediction mostly uses sequence models / Transformers ([10](../../course/10/)).
- For the full picture of spatio-temporal forecasting, see [Open problems in time series 2026 · spatio-temporal forecasting](../../kun/).

## A representative case: navigation ETA

Modern map applications abstract the whole road network into a graph and use **graph neural networks** to fuse real-time traffic conditions into arrival-time predictions (the 2020 work by DeepMind and Google Maps markedly reduced ETA errors). Transportation has thus become one of the most mature real-world arenas for "spatio-temporal forecasting" — spatial structure and temporal dynamics must be modelled together, and neither can be left out.

---

**Key terms:** spatio-temporal forecasting, road-network graph, STGNN, DCRNN, ETA, trajectory prediction, OD matrix.
