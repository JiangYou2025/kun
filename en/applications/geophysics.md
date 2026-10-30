---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 9 · Astronomy & geophysics"
permalink: /en/applications/geophysics/
title: "Astronomy & Geophysics"
lead: "From sunspots to tides and earthquakes, nature has left us humanity's longest observational series. It was precisely these century-spanning records that gave birth to modern time series theory."
math: false
prev: /applications/signal/
next: /applications/language/
---

> This is scenario 9 of the [time series applications](../) section.

## Data and tasks

- **Data**: sunspot numbers, stellar light curves, seismic waves, GPS crustal deformation, sea level / tides, the geomagnetic field.
- **Tasks**: period detection, transient and exoplanet detection, earthquake early warning, tide prediction, space weather forecasting.

## What makes it special

- **Very long time spans**: observations can cover a century or even geological time scales, but sampling is often irregular and has gaps.
- **Rare major events**: high-impact events such as great earthquakes and strong flares have very few samples, which makes supervised learning difficult.
- **Physical periods + noise**: the signal is often several deterministic periods superimposed on strong noise, and extracting hidden periodicities is the central problem.

## Common methods

- **Spectral analysis / the periodogram** to look for hidden periodicities (prehistory · [the sunspot cycle](../../prehistory/sunspot-cycle/)).
- **Harmonic analysis** for tide prediction — decompose the tide into sinusoidal components of the astronomical tide-generating forces and extrapolate them (prehistory and modern applications).
- Template matching / anomaly detection to catch transients (such as gravitational waves and flares).
- Sequence classification with the **transit method** to find exoplanets in light curves.

## A representative case: the sunspot cycle

Wolf's sunspot series is one of the most famous datasets in the history of time series. In 1927 Yule proposed the **autoregressive model** (history [1](../../history/01/)) precisely to explain its "irregular 11-year cycle" — explaining the present by the series' own past rather than assuming a perfect sine wave. A single astronomical record directly ignited modern time series analysis.

---

**Key terms:** periodogram, harmonic analysis, sunspots, transit method, earthquake early warning, space weather.
