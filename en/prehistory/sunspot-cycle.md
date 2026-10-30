---
updated: "2026-06-11"
layout: history
lang: en
era: "Prehistory story 13 · Observation · Method"
permalink: /en/prehistory/sunspot-cycle/
title: "The Sunspot Cycle"
lead: "An amateur astronomer, hoping to find a planet hidden near the Sun, counted the spots on the Sun every day for years on end — he never found the planet, but stumbled upon a rhythm that had been hidden for a thousand years."
math: false
prev: /prehistory/kelvin-tides/
next: /prehistory/
---

> This is one of the short stories from [Prehistory and Modern Applications](../), and also the bridge from this set of stories to the [main history](../../history/).

### Seventeen years of counting sunspots to find a planet

In the early nineteenth century, the German pharmacist and amateur astronomer Heinrich Schwabe had an obsession: he believed an unknown planet was hiding inside the orbit of Mercury (later dubbed "Vulcan"), and that it would cast a small black dot as it crossed the solar disc. To catch it, from 1826 onwards Schwabe set up his telescope whenever the weather was clear and recorded, day by day, the number and positions of the spots on the Sun's disc — and he kept it up for seventeen years.

Vulcan never appeared (it does not exist). But in this pile of day-after-day sunspot counts, Schwabe stumbled upon something unexpected. Later, the Swiss astronomer Rudolf Wolf collected, weighted and standardized observations from many places and periods, compiling them into the "**Wolf sunspot number**" series that continues to this day — one of the most important long-term time series in the history of astronomy.

### The difficulty: noise, or a cycle?

The difficulty was this: the number of sunspots jumps around from day to day and looks chaotic. Was it just random commotion on the surface of the Sun, or was some cycle hidden underneath? A year or two of observations could never tell; only by putting a sufficiently long run of continuous counts side by side could any regularity emerge.

### The solution: discovering a rhythm that is "not quite exact"

By accumulating and comparing many years of continuous counts, Schwabe announced in **1843** that the number of sunspots rises and falls in a cycle of roughly **11 years**, from few to many and back to few. It was a remarkable discovery. But people soon noticed a troublesome fact — the cycle is **not "exact"**: sometimes a round lasts nine years, sometimes fourteen; the height of the peaks is sometimes strong, sometimes weak. Try to fit it with a sine curve of fixed frequency and fixed amplitude, and no matter what you do the fit is poor.

### What it means for time series today

This is the archetype of a **quasi-periodic** phenomenon: a clear rhythm that is nevertheless not strictly periodic, its length and strength both drifting. It brought complete defeat to deterministic harmonic models — those that write a signal as the sum of a few fixed sine waves.

It was precisely this puzzle of "why does the cycle drift?" that directly prompted Yule's answer in 1927: instead of viewing the sunspot numbers as a sine wave plus noise, he described them with a **stochastic process** — a second-order autoregression, AR(2) — in which each year's sunspot number is determined by the values of the previous two years plus a random shock. The drifting cycle thus turned from "a nuisance that won't fit" into "a natural consequence of stochastic dynamics". This sunspot series is the protagonist of [Chapter 1 of the history](../../history/01/) — and here the prehistory hands the baton to modern time series analysis.
