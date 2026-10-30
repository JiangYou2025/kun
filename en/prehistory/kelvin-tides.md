---
updated: "2026-06-11"
layout: history
lang: en
era: "Prehistory story 12 · Method · Computation"
permalink: /en/prehistory/kelvin-tides/
title: "Kelvin's Tide Machine"
lead: "The tide in a harbour is the sum of dozens of astronomical cycles. Forecasting the water level for every hour of next year by hand would take forever. Kelvin built a brass machine to “add up the sine waves” for us."
math: false
prev: /prehistory/jevons-sunspots/
next: /prehistory/sunspot-cycle/
---

> This is one of the short stories from [Prehistory and Modern Applications](../).

### The tide is a sum of cycles

The tide seems to be nothing more than rising and falling water, yet behind it a whole ensemble of astronomical cycles is playing together: lunar, solar, semidiurnal, diurnal, fortnightly… Each tide-generating force corresponds to a sine wave called a **harmonic constituent**. The water level at a given harbour is approximately the sum of dozens of such sine waves, each with its own amplitude and phase, which must first be **fitted** from many years of local tide-gauge observations. This was one of the great real-world applications of Fourier's harmonic analysis.

### The difficulty: adding dozens of sine waves until the end of time

The difficulty lay in the sheer workload of prediction. Once the amplitudes and phases of dozens of constituents had been determined, forecasting a harbour's tide for **every hour** of the coming year meant evaluating each of those sine waves at every instant and adding them up. With pen and paper, a single year's tide table could break a person — and shipping, harbours and navies needed those tables every day.

### The solution: let a machine add the sine waves

Around 1876, William Thomson (Lord Kelvin) built the **tide-predicting machine**: an analogue computer made of pulleys, gears and wire. Each wheel in the machine generated the sine wave of one constituent, its radius corresponding to the amplitude and its initial angle to the phase; a single wire ran over all the wheels and **summed** their displacements **automatically**, its end driving a pen that **drew** an entire year of hour-by-hour tide levels on a rotating paper roll. A few hours of turning the handle produced a tide table that would otherwise have taken months to compute. Machines of this kind stayed in service for more than half a century and were still in use in the mid-twentieth century — the tidal timing of the Normandy landings in the Second World War relied on their descendants.

### What it means for time series today

Kelvin's machine made both steps of time series analysis concrete: first **decompose** (split the observed series into a set of harmonic components), then **synthesize/extrapolate** (add the components back together and extend them into the future to make a forecast). This "analysis–synthesis" paradigm is the intellectual core of later spectral analysis and of every frequency-domain forecasting method. And as a device that "builds the regularities into hardware so that turning a handle yields a forecast", it is also a modern echo, two thousand years later, of the [Antikythera mechanism](../antikythera/) — humanity's fascination with "automatic forecasting machines" runs from bronze gears all the way to today's forecasting systems.
