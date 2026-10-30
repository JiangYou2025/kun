---
updated: "2026-06-11"
layout: history
lang: en
era: "Prehistory story 9 · Method"
permalink: /en/prehistory/ceres-least-squares/
title: "Ceres & Least Squares"
lead: "On New Year's Day 1801, an astronomer discovered a new celestial body, “Ceres”; after only 40 days of records it was swallowed by the Sun's glare and lost. Where in the vast starry sky would it reappear?"
math: true
prev: /prehistory/playfair-chart/
next: /prehistory/snow-cholera/
---

> This is one of the short stories of [Prehistory & Contemporary Applications](../).

### Found on New Year's Day, lost in a flash

On 1 January 1801, the Italian astronomer Giuseppe Piazzi, at his observatory in Palermo, discovered a faint, slowly moving star. It lay between Mars and Jupiter — exactly where astronomers of the time had been searching hard for a planet that “ought” to exist but had never been found. This body, later named **Ceres**, instantly became the focus of all Europe.

But before anyone could get a good look at it, trouble struck: Piazzi had tracked it for only about **41 days** when Ceres moved too close to the Sun's direction and vanished into the glare of dawn and dusk. It had traced an arc of just about 3 degrees across the sky. When it re-emerged months later on the other side of the Sun, no one knew where to look. A newly won planet seemed about to be lost forever.

### The difficulty: too few observations, too risky an extrapolation

The difficulty was this: the world had only a short, noisy series of position observations, while determining an orbit requires fixing six orbital elements. With so few points, each carrying errors, such an extrapolation was extremely risky — get the parameters slightly wrong and the predicted position could be off by an enormous distance, and then sweeping the whole sky with a telescope pointed in the wrong direction would never find it again.

### The solution: minimize the sum of squared errors

Carl Friedrich Gauss, just **24 years old**, provided an elegant answer. His idea was not to force the orbit through every observation (which was neither possible nor desirable, since every point carries noise), but to choose the set of orbital parameters $\theta$ that minimizes the sum of squared errors between the predicted positions and **all** the observations:

$$\hat\theta=\arg\min_{\theta}\sum_i\big(y_i-f(x_i;\theta)\big)^2.$$

This is **least squares**. It lets all the observations “vote” together on the result, automatically letting random errors cancel each other out, and yields the most robust orbit. From it Gauss calculated where Ceres should reappear and sent his forecast to the astronomers. At the end of December 1801, von Zach and Olbers did indeed recapture the nearly lost asteroid close to the position Gauss had predicted. (Around the same time, Legendre in France independently proposed least squares and was the first to publish it formally, in 1805; Gauss claimed he had long been using it, which sparked a famous priority dispute.)

### What it means for time series today

From then on, least squares became the universal tool for **fitting a model to a noisy series and then forecasting**. It is the common ancestor of linear regression, the [Kalman filter](../../history/04/), and the many forms of “minimizing a loss function” in modern machine learning — however complex the model, the idea of “tuning the parameters so that the total error between prediction and data is smallest” starts here. An asteroid that was nearly lost gave birth to the basic paradigm of data fitting.
