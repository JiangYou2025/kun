---
updated: "2026-06-11"
layout: history
lang: en
era: "Prehistory story 11 · Method"
permalink: /en/prehistory/jevons-sunspots/
title: "Jevons' Sunspot Theory"
lead: "In the 1870s, a leading economist became convinced that commercial crises also came in roughly 11-year rounds — and that the hidden driver was nothing less than sunspots. It is the most famous case in the prehistory of “seeing a cycle that isn't there”."
math: false
prev: /prehistory/snow-cholera/
next: /prehistory/kelvin-tides/
---

> This is one of the short stories from [Prehistory and Modern Applications](../).

### A tempting coincidence

William Stanley Jevons was one of the foremost economists of his day. He noticed a tempting coincidence: Britain's commercial crises seemed to arrive roughly once a decade, and [sunspots also run in cycles of about 11 years](../sunspot-cycle/). Could two cycles so close in length be a mere accident? He boldly proposed a causal chain: sunspots → influence on climate and weather → harvest outcomes → grain prices → business cycles and crises. A grand hypothesis that strung astronomy, meteorology, agriculture and economics together on a single thread.

### The difficulty: only a handful of crisis years

The difficulty lay precisely in how little data there was. The years in history that genuinely qualified as "commercial crises" could be counted on your fingers. Deciding from such a tiny number of points whether they formed a **real cycle** rather than pure coincidence was statistically almost impossible. Worse, whenever the two cycles failed to line up, Jevons repeatedly **adjusted** the sunspot period he used (10.45 years at one moment, some other figure at the next) so that the crisis years would land in the "right" places.

### The solution (really, the lesson): a cycle tuned into existence

That was exactly the problem: once you allow yourself to fine-tune the period and you have only a few data points, you can **always** make a curve "fit". Jevons' hypothesis did not survive scrutiny — the sample was too small, the period was bent to suit the data, and every link in the causal chain was weak. Later generations came to treat it as a cautionary tale: in short series, people very easily "see" cycles that do not exist, and then invent an appealing causal story for the spurious cycle. This temptation of **spurious correlation / spurious periodicity** remains one of the most common traps in time series analysis to this day.

### What it means for time series today

Jevons' failure threw into sharp relief an urgent need: could there be an **objective test** that tells us whether a "cycle" in a series is a genuine signal or just fluctuations that happen to appear in the noise? It was precisely this question that, in 1898, gave rise to [Schuster's periodogram](../) — the first tool for testing whether a "hidden periodicity is significant", leading straight to twentieth-century spectral analysis. By adding a "what went wrong" dimension to this set of prehistory stories, its lesson is clear: **however convincing a rhythm looks, first ask whether it can withstand a test**. That is also the first lesson that the analysis of [economic and financial](../../applications/finance/) series must always keep in mind.
