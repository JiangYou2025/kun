---
updated: "2026-06-03"
layout: history
lang: en
era: "Paradoxes of time 1 · Philosophy"
permalink: /en/paradoxes/zeno-arrow/
title: "The Arrow (Zeno's Arrow)"
lead: "An arrow in flight, at any single “instant”, sits at one definite position — and if it is at rest at every moment, how can a flight pieced together from countless moments of rest possibly be “motion”?"
math: true
prev: /paradoxes/
next: /paradoxes/achilles-tortoise/
---

> This is one of the [paradoxes of time](../).

In Elea in the 5th century BC, Zeno set out to defend his teacher Parmenides. Parmenides held that true “being” is one, unchanging and motionless, and that the motion and change we see are mere illusions. Zeno's task was a proof by contradiction — he devised a set of paradoxes designed specifically to make the common-sense belief that “motion really exists” contradict itself.

The difficulty lies in chopping time into pieces: if time is made up of “nows” that have no duration, then in each “now” the arrow occupies a fixed position and covers no distance at all, so it is at rest. But how can countless “rests” add up to “flight”?

People of the time could only strike back at the level of concepts. Aristotle objected that time is not strung together from indivisible “nows” one bead at a time, and that treating a continuum as a pile of points is itself the mistake — but he had no tools for handling “infinity” and “instantaneousness” precisely, so the debate stayed suspended for nearly two thousand years.

The real answer came from calculus. Newton and Leibniz in the 17th century, followed by the rigorous theory of limits of Cauchy and Weierstrass in the 19th, gave “instantaneous velocity” a clean definition: it is not how far the arrow travels within one instant (that is zero, of course), but the **rate of change** of displacement with respect to time

$$v(t)=\lim_{\Delta t\to 0}\frac{x(t+\Delta t)-x(t)}{\Delta t}=\frac{dx}{dt}.$$

Motion is not hidden in an isolated instant but in the **limiting trend** around it. A question once dismissed as sophistry ultimately forced out humanity's most powerful language for describing change — the source of every later differential equation, and of the modelling of “rates of change” in time series.
