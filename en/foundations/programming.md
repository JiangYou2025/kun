---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/programming/
title: "Programming"
no_comments: true
---

> Part of [Computer science foundations](../cs/) · [Foundations overview](../)

**Programming** means breaking an idea down into explicit instructions that a computer can execute step by step. It is the basic skill for making mathematics and models "run" and for doing hands-on experiments. All the examples in this course use [Python](../python/).

## Intuition

Programming is a lot like writing a recipe for a cook who is **extremely obedient but has no common sense whatsoever**:

- You cannot say "stir-fry until it's about done" — you have to write "stir-fry over medium heat for 3 minutes".
- The cook follows the instructions to the letter, but if you get a step wrong (sugar instead of salt), they will never correct it; they will faithfully cook the wrong dish.

So the core of programming is not memorizing syntax but **breaking vague ideas down into precise, unambiguous, ordered steps** — this "computational thinking" is the real skill, and syntax is just the tool for expressing it.

## Key points

Almost every program is built from these few building blocks:

- **Variables**: give data a name and store it, `lr = 0.001`.
- **Data types**: numbers, strings, lists, dictionaries and so on (see [data structures](../data-structures/)).
- **Control flow**:
  - Conditionals `if / else`: take different branches depending on the situation.
  - Loops `for / while`: do something repeatedly.
- **Functions**: package a piece of logic, give it a name and reuse it, avoiding duplicated code.
- **Modules / libraries**: ready-made functionality written by others, such as [NumPy](../numpy/) and [Pandas](../pandas/).

Habits for writing good code: **clear names, short functions, one function doing one thing, helpful error messages** — these belong to [engineering practice](../engineering-practice/).

## An example

Translating the idea "compute the moving average of a sequence" into code:

```python
def moving_average(series, window):
    """Moving average of series with the given window; returns a new list"""
    if window <= 0:                      # defensive: check the arguments
        raise ValueError("window must be positive")
    result = []
    for i in range(len(series)):
        start = max(0, i - window + 1)   # left edge of the window
        chunk = series[start : i + 1]    # the numbers inside the window
        result.append(sum(chunk) / len(chunk))
    return result

data = [10, 12, 14, 13, 15, 16]
print(moving_average(data, 3))
# [10.0, 11.0, 12.0, 13.0, 14.0, 14.666...]
```

Notice that it uses every building block: a **function** to encapsulate, an **argument check** (if), a **loop** to iterate, and **variables** to hold intermediate results. Once you have learned [vectorization](../vectorization/), you will find that [NumPy](../numpy/)/[Pandas](../pandas/) can do the same thing faster in one line — but only by understanding the loop version do you see what vectorization saves you.

## Relevance to time series forecasting

In time series forecasting, programming runs through everything:

- **Data preprocessing**: reading files, aligning timestamps, filling gaps, cutting sliding windows — all of it is code.
- **Implementing and modifying models**: to get **KUN / Kernel U-Net** running, tune its structure or add modules, you need to be able to read and change code.
- **Running experiments, plotting, computing metrics**: behind every conclusion is a script that can be rerun.

Only if you can program can you move from "reading papers" to "verifying and improving things yourself". **If you cannot run the code, a model is just a picture to you.**

## Summary

- Programming = breaking ideas down into precise, ordered, unambiguous instructions; the core is computational thinking, not memorizing syntax.
- Building blocks: variables, data types, control flow (if / loops), functions, libraries.
- Good code: clear names, short functions, error handling — which leads on to [engineering practice](../engineering-practice/).
- This course uses [Python](../python/); it is your entry point to every hands-on experiment.

---

[← Computer science foundations](../cs/) · [Foundations overview](../)
