---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 1 · Finance"
permalink: /en/applications/finance/
title: "Finance & Economics"
lead: "Markets are the most tempting and the most brutal battlefield for time series: huge amounts of data, instant feedback and real money — but also an extremely low signal-to-noise ratio and treacherous tails."
math: false
next: /applications/energy/
---

> This is scenario 1 of the [time series applications](../) section.

## Data and tasks

- **Data**: stock prices / returns, exchange rates, interest rates, cryptocurrencies, trading volume and volatility, plus macro series such as GDP, CPI and the unemployment rate.
- **Tasks**: return direction / point forecasts, **volatility forecasting**, risk measures (VaR / ES), pairs trading and cointegration, high-frequency market making, fraud and anomaly detection.

## Why it is especially hard

- **Extremely low signal-to-noise ratio**: close to the "efficient market hypothesis" — the predictable part is tiny, and models very easily mistake noise for signal and overfit.
- **Non-stationarity and structural breaks**: crises, policies and regulatory changes can make historical patterns suddenly stop working.
- **Heavy tails and volatility clustering**: extreme market moves are far more frequent than a normal distribution predicts, and "big swings come in clusters".
- **Backtesting traps**: look-ahead bias, survivorship bias, overfitting to history — beautiful offline, losing money live.

## Common methods

- Returns themselves are close to white noise, so the firepower shifts to **volatility**: ARCH / GARCH (history [6](../../history/06/)).
- **Cointegration + error correction** underpin pairs trading ([6](../../history/06/)).
- Classical baselines: ARIMA (course [8](../../course/08/)), exponential smoothing ([12](../../course/12/)).
- Machine learning / deep learning for feature-based forecasting ([13](../../course/13/), [9](../../course/09/)), but it **must be backtested strictly in time order** ([2](../../course/02/)), otherwise data leakage manufactures fake returns.

## A representative case: volatility clustering

In 2003 Engle received the Nobel Prize in Economics for the ARCH model. The direction of returns is almost unpredictable, but "a volatile day today means a volatile day tomorrow is likely" is a remarkably robust regularity. By seizing on exactly this, **risk management and option pricing** became the most successful real-world use of time series in finance — what is forecast is not the ups and downs, but uncertainty itself.

---

**Key terms:** returns, volatility, GARCH, VaR / ES, cointegration, efficient market hypothesis, heavy tails, backtesting bias.
