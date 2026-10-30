---
updated: "2026-06-03"
layout: history
lang: en
era: "Paradoxes of time 2 · Philosophy"
permalink: /en/paradoxes/achilles-tortoise/
title: "Achilles and the Tortoise"
lead: "Give the tortoise a head start and let swift-footed Achilles chase it. By the time he reaches the tortoise's starting point, the tortoise has crept a little further; by the time he reaches that new point, it has crept a smaller bit further still… He seems always to have to reach the place where the other was “a moment ago”, and so he can never catch up. Yet in reality he overtakes it in a single stride — where is the mistake?"
math: true
prev: /paradoxes/zeno-arrow/
next: /paradoxes/twin/
---

> This is one of the [paradoxes of time](../).

This is the most famous paradox in Zeno's series, and it serves the same argument that “motion is an illusion”. Its force lies in the fact that every step of the reasoning looks flawless: the chase is broken down into infinitely many small stages of “first reach the old position”.

The difficulty is not physical but lies in **infinity**: to catch up, it seems one must first complete infinitely many steps, and intuitively “infinitely many steps” means “never finished”.

The ancients got stuck here. Aristotle pointed out that these infinitely many steps take place within a finite stretch of time and do not really require an infinite duration — but, as with the arrow, he lacked the arithmetic to add up “infinitely many ever-smaller quantities” and obtain a finite result.

The answer came from the **convergence of infinite series**. Suppose Achilles runs 10 times as fast as the tortoise, which starts with a lead of $d$. Then the times needed for the successive stages form a geometric sequence whose sum is

$$T=\frac{d/v}{\,1-1/10\,}=\frac{10}{9}\cdot\frac{d}{v}<\infty.$$

The total time of infinitely many steps is **finite**. Zeno sliced a finite span of time into infinitely many pieces and then slipped in the equivocation “infinitely many pieces = infinitely long”.

Clearing it up amounts to learning something profound: **the sum of infinitely many quantities can perfectly well be a finite number.** This is the very foundation of series, integrals, and all continuous-time modelling.
