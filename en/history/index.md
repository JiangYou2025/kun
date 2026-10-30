---
updated: "2026-06-03"
layout: history
lang: en
permalink: /en/history/
title: "A History of Time Series · Contents"
lead: "From Yule's autoregression in 1927 to today's deep learning and foundation models — a hundred years of time-series analysis and forecasting. A prologue plus 10 chapters that tell the story behind each method, write out its key formulas and explain what they mean."
---

## What this is

A century-long chronicle of how **time-series** methods evolved: from the foundations laid by statistics, through state space and the Box–Jenkins paradigm, to the waves of machine learning and deep learning, and on to Transformers, foundation models and **Kernel U-Net (KUN)**.

> Companion material: [Introductory lecture notes on time series](../course/) · [Using KUN](../kun/)
>
> Three parallel essays: [Prehistory and modern applications](../prehistory/) · [The nature of time](../nature-of-time/) · [Paradoxes of time](../paradoxes/)

## Timeline

Filter this hundred-year timeline by **domain** — mathematicians laid the theory, physicists supplied the physical intuition behind stochastic processes, cybernetics and communication engineering turned prediction into engineering that can be computed recursively online, and computer science pushed it into machine learning and deep learning. Click a tag below to see a single domain, or click **All** to see the full story of how the four domains intertwine.

<div class="tl" markdown="0">
<input class="tl-radio" type="radio" name="tlf" id="tl-all" checked>
<input class="tl-radio" type="radio" name="tlf" id="tl-math">
<input class="tl-radio" type="radio" name="tlf" id="tl-phys">
<input class="tl-radio" type="radio" name="tlf" id="tl-ctrl">
<input class="tl-radio" type="radio" name="tlf" id="tl-cs">
<div class="tl-tabs">
  <label for="tl-all">All</label>
  <label for="tl-math" class="d-math"><span class="dot"></span>Mathematicians</label>
  <label for="tl-phys" class="d-phys"><span class="dot"></span>Physicists</label>
  <label for="tl-ctrl" class="d-ctrl"><span class="dot"></span>Cybernetics / Communications</label>
  <label for="tl-cs" class="d-cs"><span class="dot"></span>Computer science</label>
</div>
<table class="tl-table">
<thead><tr><th>Year</th><th>Domain</th><th>Person</th><th>Key contribution</th><th>Chapter</th></tr></thead>
<tbody>
{% for item in site.data.timeline %}{% case item.domain %}{% when 'math' %}{% assign dlabel = 'Mathematics' %}{% when 'phys' %}{% assign dlabel = 'Physics' %}{% when 'ctrl' %}{% assign dlabel = 'Control' %}{% else %}{% assign dlabel = 'Computing' %}{% endcase %}<tr class="r-{{ item.domain }}"><td class="yr">{{ item.year }}</td><td><span class="badge d-{{ item.domain }}">{{ dlabel }}</span></td><td><a href="{{ '/en/history/e/' | append: item.slug | append: '/' | relative_url }}">{{ item.person_en | default: item.person }}</a></td><td>{{ item.contribution_en | escape }}</td><td><a href="{{ '/en/history/' | append: item.chap_url | relative_url }}">{% if item.chap_url == 'foundations/' %}Prologue{% else %}{{ item.chap }}{% endif %}</a></td></tr>
{% endfor %}
</tbody>
</table>
</div>

> The table above also serves as the book's chapter navigation: the "Chapter" entry at the far right of each row jumps straight to the corresponding chapter. The prologue traces, discipline by discipline, the roots that span the century (mathematics · physics · control/communications · sequential decision-making · scientific computing); Chapters 1–10 then unfold chronologically.

## Further essays

The main text follows the line of methods that starts from the theory of stochastic processes around 1900. Each of the essays below has its own page and circles this main line from a different angle:

- [**Task History**](../tasks/) — the history tells how the tools evolved; this tells how the problems evolved: from flood prediction 3,000 years ago to today's multimodal time series.
- [**Applications in the Wild**](../applications/) — how time series are put to work, domain by domain: ten scenarios spanning finance, energy, retail, transportation, healthcare, meteorology, industry, signals, geophysics and language.
- [**Prehistory & Applications**](../prehistory/) — how humans "read time series" before the 19th century, through timekeeping, observation and naive methods, plus a catalog of time-series applications across fields.
- [**The Nature of Time**](../nature-of-time/) — an interdisciplinary inquiry into "time" itself, through philosophy, physics and literature.
- [**Paradoxes of Time**](../paradoxes/) — from Zeno to the grandfather paradox, the famous paradoxes that force us to think "time" through clearly.

## Reading conventions

- Each chapter tells the story behind its methods in narrative form, writes out the key **formulas** and explains what they mean.
- The prologue traces, discipline by discipline (mathematics · physics · control/communications · sequential decision-making · scientific computing), the roots spanning the century; there are also three parallel essays: [Prehistory and modern applications](../prehistory/), [The nature of time](../nature-of-time/) and [Paradoxes of time](../paradoxes/).
- Years, names and papers cited in the text were compiled by the editor; please double-check them before citing.
- Chapter 10 closes with KUN, echoing the hands-on tutorial in [Using KUN](../kun/).
