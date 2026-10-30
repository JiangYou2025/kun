---
updated: "2026-06-03"
layout: history
lang: en
era: "Paradoxes of time 6 · Physics · Thermodynamics"
permalink: /en/paradoxes/maxwell-demon/
title: "Maxwell's Demon"
lead: "Imagine a little demon guarding a trapdoor in a partition, letting fast molecules through to one side and slow molecules to the other. It does no work, yet it makes one side hotter and the other colder, creating a temperature difference out of nothing — doesn't that violate the second law?"
math: true
prev: /paradoxes/loschmidt/
next: /paradoxes/boltzmann-brain/
---

> This is one of the [paradoxes of time](../).

Maxwell proposed this thought experiment in 1867, originally to show that the second law is statistical rather than absolute. But the “demon” soon became a genuine threat: it seemed able to make entropy decrease spontaneously.

The difficulty: the demon merely “sorts”, which seems to cost no energy, so why can't it get a temperature difference for free (and use it to drive a perpetual-motion machine)?

Generation after generation took their turn. In 1929 Szilárd reduced it to a single-molecule engine, pointed out that the demon must **measure** the molecule's state, and suspected that the cost was hidden in the measurement; later Brillouin argued that measurement consumes energy. But the real answer is subtler.

The final answer came from information theory and the physics of computation. In 1961 **Rolf Landauer** showed that measurement itself can in principle cost no energy, but the demon's memory is finite: sooner or later it must **erase** its records to make room, and erasing one bit of information necessarily dissipates at least

$$E\ge k_B T\ln 2$$

of energy, expelling the corresponding entropy into the environment. In 1982 Bennett completed the argument on this basis: the entropy the demon removes is exactly made up by the entropy produced when it clears its memory, and the second law emerges unscathed.

**Maxwell's demon brought “information” into physics** — information is not an abstract symbol; erasing it costs real energy. The Landauer limit is the lower bound on the energy cost of all computation today, linking the “bit” and the “joule” for good.
