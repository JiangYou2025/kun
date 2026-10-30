---
updated: "2026-06-11"
layout: history
lang: en
era: "Application scenario 10 · Sequence modelling"
permalink: /en/applications/language/
title: "Language & Sequences"
lead: "Text, music, code and DNA are all sequences of symbols arranged in order — close relatives of time series. This kinship has led the two fields to borrow each other's models again and again."
math: false
prev: /applications/geophysics/
---

> This is scenario 10 — and the last one — of the [time series applications](../) section.

## Data and tasks

- **Data**: text, speech transcripts, music, source code, DNA / protein sequences.
- **Tasks**: language modelling (predicting the next token), sequence labelling, machine translation, sequence generation.

## Similarities and differences with numerical time series

- **Similar**: both are fundamentally ordered sequences, and the core of both is "using the past to predict the future".
- **Different**: the symbols are **discrete** (not continuous values), dependencies can span extremely long distances, and there is no fixed sampling interval.

## Family of methods (closely shared with time series)

- RNN / LSTM (course [9](../../course/09/), history [7](../../history/07/)).
- **Transformer / self-attention** (course [10](../../course/10/), history [9](../../history/09/)) — the same architecture now feeds back into numerical time series, giving rise to PatchTST and iTransformer.
- It is precisely because of this interchange that Chronos can **discretise** numerical values **into tokens** and reuse a language-model architecture directly for forecasting (course [10](../../course/10/)).

## A representative case: architectures migrating in both directions

LSTM and the Transformer, invented in NLP, have been borrowed heavily by time series; conversely, time series foundation models (such as Chronos) borrow the paradigm of language models. The two fields share the same "sequence modelling" backbone — which is exactly why this course places language alongside time series: **sequences come first, time series follow**.

> You have now been round all [ten scenarios](../). Go back to the [applications index](../), or continue with the [introductory course](../../course/) and the [history](../../history/).

---

**Key terms:** language model, token, self-attention, sequence labelling, Chronos, sequence modelling.
