---
updated: "2026-06-11"
layout: history
lang: en
era: "Prehistory story 2 · Observation"
permalink: /en/prehistory/babylon-diaries/
title: "Babylonian Astronomical Diaries"
lead: "From the 7th century BC onward, Babylonian scribes inscribed on clay tablets, night after night, the phases of the Moon, the positions of the planets, the weather, grain prices and river levels — and kept it up for seven hundred years. What were they hoping to predict from this mass of numbers?"
math: false
prev: /prehistory/nilometer/
next: /prehistory/antikythera/
---

> This is one of the short stories of [Prehistory & Contemporary Applications](../).

### Seven hundred years of unbroken night shifts

From the Neo-Babylonian dynasty, through the Persian period, all the way to the Seleucid era, Babylonian scribes built the most systematic and enduring tradition of continuous observation known to humanity. They called this work *naṣāru ša ginê* — “regular watching”. The earliest surviving astronomical diary dates from about **652 BC**, the latest from around **61 BC**, spanning nearly six hundred years: an archive of continuous records rare in history.

On each tablet the scribes logged the sky night by night in cuneiform: near which star the Moon rose, the positions of each planet, when solar and lunar eclipses occurred, at what time the new crescent was first seen. What made it truly special was that they recorded these “affairs of heaven” and “affairs of earth” on the same tablet — that night's weather, the level of the Euphrates, and the market prices of barley, dates, sesame and wool. A single tablet was a multivariate time series of astronomy, weather, hydrology and prices.

### The difficulty: can an evil omen be predicted?

The difficulty was this: eclipses seemed to arrive without any pattern, and at the time they were regarded as the gravest of evil omens, even a threat to the king's life. Could they really be **predicted**? If the date of the next eclipse could be calculated in advance, the royal court could perform rites to ward off disaster beforehand and install a “substitute king” to absorb the ill fortune. The motive for prediction was naked political and religious need.

### The solution: fishing cycles out of a long series

It relied not on any dynamical theory but on the series itself, accumulated without interruption over centuries. Babylonian astronomers discovered in their records that eclipses were not random but recurred with a fixed rhythm — about **18 years and 11 days** (more precisely, 223 synodic months, about 18 years 11⅓ days). Later ages called this period the **Saros cycle**.

With it in hand, prediction became table lookup plus extrapolation: push today's eclipse record forward by one Saros, and you can infer future eclipses at the same phase. The Babylonians went further still and compiled “Goal-Year Texts”, which specifically copied out the observations from the corresponding cycle some years earlier to serve as the basis for forecasting the sky in the year at hand. It was an entirely data-driven forecasting pipeline, preceding any explanation of “why”.

### What it means for time series today

The data left by these anonymous scribes were directly inherited by the Greeks [Hipparchus and Ptolemy](../antikythera/), becoming the foundation of Western astronomy. Methodologically, this is the earliest example of “**discovering a cycle from a long series, then extrapolating by that cycle**”: no physical model, just a sufficiently long series of observations, from which a hidden repeating structure is identified and extended into the future. More than two thousand years later, when Yule applied autoregression to the [sunspot series](../sunspot-cycle/), he was still doing a refined version of the same thing — only replacing the “fixed cycle” with a statistical model driven by random disturbances.
