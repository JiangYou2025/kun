---
updated: "2026-06-11"
layout: history
lang: en
permalink: /en/tasks/
title: "A History of Time Series Tasks · The Co-evolution of Tasks and Computing"
lead: "The history tells how methods were invented; here we take another angle: whether a class of time series tasks can be done, and when, is often decided not by mathematics but by the computing technology of the day — the price of storage, memory and compute, or the arrival of a specific product (the hand-cranked calculator, the onboard computer, the mainframe, the personal computer, the GPU, the TPU cluster) is what turned a new task from \"impossible to compute / unthinkable\" into \"doable\"."
---

> A companion piece to the [history of time series](../history/). The history covers **the evolution of tools**; this page covers **the evolution of tasks**, and emphasises an often-overlooked causal chain: **progress in computing technology (or the arrival of a product) → a new class of tasks becomes feasible for the first time**. Each era first names that generation's key computing power, then lists which **task types** it "unlocked".
>
> For the **concrete applications** of these tasks in each industry (finance, energy, healthcare, transportation, meteorology…), see the companion pieces [prehistory and modern applications](../prehistory/) and [time series applications](../applications/); this page does not repeat them.

## Antiquity — 19th century: manual records and hand calculation

In this period there were no "computers". The enabling technologies were **writing and calendars** (so that observations could be recorded), **logarithm tables and slide rules** (turning laborious multiplication and division into addition and subtraction), and, in the 19th century, **mechanical analogue computers**. The ceiling on tasks was how much one person could compute with pen and paper.

| Period | Task | Enabling technology / product | In one line: how technology made the task possible |
|------|------|----------------|------------------------------|
| ~3000 BC | Flood / celestial prediction | Calendars, clay tablet / papyrus records, period tables | Nile water levels, Babylonian lunar eclipses — only once long series could be **recorded** could period tables be used to extrapolate |
| 1662 | Mortality forecasting (life tables) | Printed death registers (Bills of Mortality) + arithmetic | Graunt **compiled** the London death lists **into tables**: the first life table |
| 1682 | Predicting a comet's return | Newtonian mechanics + logarithm tables / slide rules | Halley computed the orbit by hand and predicted the comet's return 76 years later |
| 1801 | Orbit / position prediction | Least squares + hand calculation | Gauss reconstructed the orbit of Ceres from a handful of observations |
| 1876 | Tide prediction | Kelvin's tide-predicting machine (mechanical analogue computer) | Harmonic synthesis with gears: **for the first time a machine "computed"** future tide levels |

## 1900 — 1960s: from mechanical calculators to onboard computers

The computing power of the first half of the 20th century was **hand-cranked / electric mechanical calculators**; the Second World War brought **analogue and electronic computers**, and by the 1960s **integrated circuits and onboard computers** had appeared. The deepest lesson of this period: **the shape of memory and compute directly determines the shape of algorithms**.

| Period | Task | Enabling technology / product | In one line: how technology made the task possible |
|------|------|----------------|------------------------------|
| 1900 | Stock price modelling | Hand calculation + probability theory | Bachelier described the prices of French government bonds with a random walk |
| 1927 | Forecasting economic / natural indicators | Hand-cranked and electric mechanical calculators | Mechanical calculators made solving regressions feasible; Yule fitted an AR model to predict sunspots |
| 1940s | Signal / target prediction (military) | WWII fire control · analogue computers | Anti-aircraft fire control had to extrapolate target positions from noisy tracks → Wiener–Kolmogorov optimal filtering |
| 1950s | Inventory / sales forecasting | Early electronic computers (expensive, compute scarce) | **Compute was expensive**, giving rise to O(1) recursive exponential smoothing, able to forecast tens of thousands of SKUs cheaply |
| 1960 | Navigation / position tracking | Apollo Guidance Computer (integrated circuits, KB-scale memory) | **Tiny memory → the recursive** Kalman filter was a perfect fit, enabling real-time positioning for the Moon landing |

> Note these two rows, the 1950s and the 1960s: exponential smoothing won because compute was expensive at the time; the Kalman filter takes the recursive "predict–update" form because the onboard computer had only a few KB of memory and could not store the whole history. **Constraints shaped the methods.**

## 1970s — 1990s: mainframes, personal computers and industrial sensing

In the 1970s **mainframes** made iterative numerical optimisation affordable for the first time; in the 1980s **personal computers / workstations** brought modelling power into offices and trading rooms; in the 1990s **industrial sensors + data acquisition (SCADA) + cheap storage** made "continuously recording equipment state" the norm.

| Period | Task | Enabling technology / product | In one line: how technology made the task possible |
|------|------|----------------|------------------------------|
| 1970 | Macroeconomic forecasting | Mainframes (IBM System/360 and others) | **Iterative maximum likelihood** became runnable for the first time; Box–Jenkins ARIMA became the paradigm |
| 1970s | Speech recognition | DARPA programmes + mainframes | Enough compute for HMM + Viterbi dynamic programming to transcribe telephone speech |
| 1973 | Option pricing | Handheld calculators + mainframes | The Black–Scholes formula + numerical computation gave rise to pricing at exchange scale |
| 1980s | Risk management (VaR) | Personal computers / workstations + econometrics software | The spread of PCs brought GARCH volatility modelling into trading rooms |
| 1987 | Multivariate cointegration | Workstations + statistical software | Engle–Granger forecasting of long-run equilibria between macro variables |
| 1990s | Equipment failure prediction | Industrial sensors + SCADA + cheap storage | Only once sensor series could be **continuously collected and stored** did predictive maintenance become possible |
| 1997 | Modelling long-range dependencies | The CPUs of the day (GPUs had not yet arrived) | LSTM solved vanishing gradients with gating — but its real breakthrough had to wait for the GPU era |

## 2000s — 2010s: internet-scale data, clusters and GPUs

This was the turning point for computing: **the internet brought massive amounts of sequential data**, **server clusters + data warehouses** made storage and parallel computing cheap, and from 2007 **NVIDIA GPUs + CUDA** cut the cost of training deep networks by an order of magnitude — after AlexNet in 2012, deep sequence models took off.

| Period | Task | Enabling technology / product | In one line: how technology made the task possible |
|------|------|----------------|------------------------------|
| 2012 | **Deep learning takes off (turning point)** | NVIDIA GPU + CUDA (AlexNet) | General-purpose GPU computing slashed the cost of training deep networks, and sequence modelling shifted gear |
| 2017 | Global probabilistic forecasting | Cloud GPUs (e.g. AWS) + large-scale series collections | DeepAR trains jointly across thousands of series and outputs probability distributions |
| 2017 | Anomaly detection | Large-scale monitoring / telemetry infrastructure | Server and network-traffic telemetry → real-time alerting with Autoencoder/LSTM |
| 2019 | Interpretable forecasting | GPU clusters | N-BEATS, purely feed-forward with residual stacking, outputs a trend/seasonality decomposition |

## 2020s — today: accelerator clusters and foundation models

Once computing entered the era of **large-scale GPU / TPU clusters + massive pre-training**, tasks changed in kind: instead of training a separate model for each problem, one **pre-trains a general-purpose model** to solve tasks it has never seen. The surplus of compute, in turn, drove the "generalisation" of tasks.

| Period | Task | Enabling technology / product | In one line: how technology made the task possible |
|------|------|----------------|------------------------------|
| 2020s | Time series classification | GPU | ECG classification, fault diagnosis from industrial vibration signals, Transformer / CNN |
| 2020s | Time series generation | GPU + diffusion / generative model frameworks | Generating realistic synthetic financial and medical data |
| 2023– | Zero-shot forecasting | Large-scale pre-training + accelerator clusters | TimesFM and Chronos pre-train one model that forecasts new series without training |
| 2024– | Multimodal / conversational time series | LLM inference infrastructure | Text + images + sensors combined, asking in natural language "Next week's sales?" |

## How compute "unlocks" tasks

> **Methods do not evolve out of thin air: each step up in computing technology unlocks a new batch of tasks.**

Linking the five eras above together, several clear causal threads emerge:

1. **Storage decides whether there can be a series at all**: without means of recording such as clay tablets, death registers, SCADA or data warehouses, there is no data to analyse — failure prediction and CTR prediction both had to wait until things "could be stored".
2. **The shape of memory decides the shape of algorithms**: the Apollo onboard computer had only KB-scale memory, which forced the recursive "predict–update" structure of the Kalman filter; if you cannot store the whole history, you can only update online.
3. **The price of compute decides the complexity of methods**: when compute was expensive, O(1) exponential smoothing won; only once compute became cheap did complex deep networks pay off.
4. **New products directly open up new tasks**: the tide-predicting machine, the mainframe, the personal computer, the GPU, the TPU cluster — the arrival of each generation's landmark product corresponds to a batch of tasks that "could not be computed before" becoming feasible for the first time.
5. **Surplus compute drives "generalisation"**: once the cost of pre-training a large model becomes acceptable, tasks move from "one model per problem" to "one model for everything" (foundation models, zero-shot, multimodality).

> Back to [the main history](../history/) · [prehistory and modern applications](../prehistory/) · [the nature of time](../nature-of-time/) · [paradoxes of time](../paradoxes/)
