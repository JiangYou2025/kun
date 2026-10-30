---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/course/
title: "Introduction to Time Series · Lecture Notes"
lead: "An introductory course on time-series analysis and forecasting, in 17 lectures. This page lists only the framework and titles; the content is filled in lecture by lecture. The format follows the lecture notes of tsamardzic/nlp_intro."
---

## About the course

These notes take you from scratch to an understanding of **time series**: what they are, how to analyse them, how to **forecast** them, and finally on to modern deep-learning models, including this repository's **Kernel U-Net (KUN)**.

> Companion site (Chinese / English / French): [Time series](../time-series/) · [How to forecast](../forecasting/) · [Using KUN](../kun/)
>
> Curious where the methods came from? See the [history of time series](../history/).
>
> Need to shore up your maths or machine-learning foundations? See the separate [foundations course](../foundations/): mathematics / computer science / machine learning / deep learning.

## Lectures

| # | Lecture | Topic |
|---|------|------|
| 1 | [Introduction: time series and forecasting tasks](01/) | Introduction |
| 2 | [Data: datasets and how to prepare them](02/) | Data & preparation |
| 3 | [Linear models: fitting and forecasting](03/) | Linear models |
| 4 | [Visualization: analysing results and plotting](04/) | Visualization & analysis |
| 5 | [Components and decomposition](05/) | Components & decomposition |
| 6 | [Stationarity, differencing and transforms](06/) | Stationarity & transforms |
| 7 | [Autocorrelation: ACF and PACF](07/) | Autocorrelation |
| 8 | [Classical models: AR / MA / ARIMA / SARIMA](08/) | Classical models |
| 9 | [Deep-learning models: RNN / LSTM / GRU and TCN](09/) | Deep learning models |
| 10 | [Transformers and time series](10/) | Transformers |
| 11 | [Kernel U-Net](11/) | Kernel U-Net |
| 12 | [Special data and transforms: the log transform (financial / social data) and exponential smoothing](12/) | Special data & transforms |
| 13 | [Tasks and model selection: which model for which task](13/) | Tasks & model selection |
| 14 | [Probabilistic forecasting](14/) | Probabilistic forecasting |
| 15 | [Multivariate forecasting](15/) | Multivariate forecasting |
| 16 | [Dynamical systems](16/) | Dynamical systems |
| 17 | [Flow matching and diffusion](17/) | Flow matching & diffusion |

## Supplementary topics

- [**Wave types and forecasting**](wave-types/) — an interactive canvas introducing six basic waveforms (trend, periodic, damped, square, composite and noise) and how hard each one is to forecast. Read it alongside lectures 4 and 5.

## Hands-on examples

Companion runnable Jupyter examples (synthetic data, clone and run) live in the repository's [`notebooks/`](https://github.com/JiangYou2025/kun/tree/main/notebooks) folder:

1. [Exploration and decomposition](https://github.com/JiangYou2025/kun/blob/main/notebooks/01_explore_and_decompose.ipynb) — lectures 4 and 5
2. [Forecasting baselines and evaluation](https://github.com/JiangYou2025/kun/blob/main/notebooks/02_forecasting_baselines.ipynb) — lectures 3 and 4
3. [Sliding-window neural forecasting (the KUN idea)](https://github.com/JiangYou2025/kun/blob/main/notebooks/03_kun_style_window_forecast.ipynb) — lectures 9 and 11

## How to use these notes

- Read them in order; each lecture builds on the one before.
- Each lecture first lists only its **title and section outline**, so you can build a global map before filling in the details.
- Lecture 11 lands on **KUN** and links to the hands-on tutorial [Using KUN](../kun/).
