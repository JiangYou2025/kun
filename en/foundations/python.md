---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/python/
title: "Python"
no_comments: true
---

> Part of [Computer science foundations](../cs/) · [Foundations overview](../)

**Python** is the main programming language of data science and [machine learning](../ml/). Its syntax is concise, it is quick to pick up, and it has an extremely rich ecosystem including [NumPy](../numpy/), [Pandas](../pandas/) and PyTorch. All the hands-on examples in this course use Python.

## Intuition

If [programming](../programming/) is "writing ideas as instructions", then Python is an instruction language that is **especially close to natural language**. It is deliberately kept simple:

```python
for name in ["Alice", "Bob"]:
    print(f"Hello, {name}")
```

You can almost read it out literally — "for each name in the list, print a greeting". No semicolons, no curly braces; code blocks are marked by indentation. **Precisely because the barrier to entry is low, researchers can spend their energy on "ideas" rather than "wrestling with the language"**, which is why it has become the de facto standard for scientific computing.

But Python has a price: it is an **interpreted** language, and element-by-element loops in pure Python are slow — exactly the gap that [NumPy](../numpy/)'s [vectorization](../vectorization/) fills.

## Key points

A few of the most frequently used language features:

- **Dynamic typing**: variables need no type declaration; after `x = 3` you can still write `x = "abc"`.
- **Core data structures**: `list`, `dict`, `set`, `tuple` (see [data structures](../data-structures/) for details).
- **List comprehensions**: build a list in one line, `[x**2 for x in range(5)]` → `[0,1,4,9,16]`.
- **Functions and default arguments**: `def f(x, lr=0.01): ...`.
- **A rich standard library plus a third-party ecosystem**: just `import` and use.
- **Package management and environments**: install packages with `pip`, isolate environments with `venv`/`conda` (part of [engineering practice](../engineering-practice/)).

## An example

A short demo of a few characteristic Python constructs:

```python
# List comprehension + condition
evens = [x for x in range(10) if x % 2 == 0]   # [0,2,4,6,8]

# Dictionary: look up a feature from a timestamp
holiday = {"2026-01-01": "New Year's Day", "2026-05-01": "Labour Day"}
print(holiday.get("2026-01-01", "Workday"))      # New Year's Day
print(holiday.get("2026-03-15", "Workday"))      # Workday (default value)

# Tuple unpacking: a function returning several values
def min_max(xs):
    return min(xs), max(xs)

lo, hi = min_max([3, 7, 1, 9])
print(lo, hi)                                     # 1 9

# f-string formatting
mae = 0.12345
print(f"Test MAE = {mae:.3f}")                    # Test MAE = 0.123
```

These idioms are concise yet highly expressive, and they are used constantly in everyday data work.

## Relevance to time series forecasting

Python carries this course all the way from data to model:

- **Data processing**: [Pandas](../pandas/) reads, aligns and resamples time series.
- **Numerical computation**: [NumPy](../numpy/) performs [vectorized](../vectorization/) operations such as windowing, normalization and FFTs.
- **Modelling and training**: PyTorch builds and trains **KUN / Kernel U-Net**, accelerated on the [GPU](../gpu/).
- **Visualization and reporting**: Matplotlib plots forecast curves and error distributions.

The whole [scientific computing stack](../scientific-computing/) grows on Python — **mastering Python means holding the key to practical time series forecasting.**

## Common pitfalls

- **Thinking Python is too slow for scientific computing**: pure Python loops are indeed slow, but by pushing the computation down to the C level with [NumPy](../numpy/), the speed is more than enough.
- **Bad indentation**: Python uses indentation to delimit code blocks, and mixing spaces and tabs raises an error straight away.
- **The mutable default argument trap**: in `def f(x, cache=[])` the `[]` is created only once and shared across calls; use `None` instead and initialize it inside the function.
- **Not isolating environments**: if all projects share one set of packages, versions will clash sooner or later; get into the habit of using `venv`/`conda`.

---

[← Computer science foundations](../cs/) · [Foundations overview](../)
