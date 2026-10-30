---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/engineering-practice/
title: "Engineering Practice"
no_comments: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

**Engineering practice** refers to a set of working habits that make code **collaborative, reproducible and maintainable** — version control, fixed random seeds, isolated environments, writing tests and so on. It does not change the model itself, but it decides whether your research can be trusted and reused by others (and by yourself six months from now).

## Intuition

Think of running [machine learning](../ml/) experiments as running a kitchen:

- No engineering practice = cooking by feel. Today the dish is delicious, but tomorrow you can't reproduce the taste, because you don't remember how much salt you added (the random seed), which batch of ingredients you used (the data version), or which stove (the dependency versions).
- With engineering practice = a standardized recipe. Quantities, heat and ingredient batches are all on record, so **a different cook in a different kitchen can make exactly the same dish**.

One of the biggest pain points in research and industry is "**other people can't reproduce my results**", and even "**I can't reproduce my own results from last month**". Engineering practice exists to cure exactly this.

## Key points

The habits most worth building:

- **Version control**: use [Git](../git/) to record every change, so you can go back, compare, and collaborate with others.
- **[Reproducibility](../reproducibility/)**: fix random seeds, pin dependency versions, record data snapshots.
- **Environment isolation**: use `venv` / `conda` / Docker to keep the project's dependencies in a separate environment, avoiding "it works on my machine".
- **Separate configuration from code**: put hyperparameters and paths in a configuration file instead of hard-coding them all over the place.
- **Write tests and assertions**: add unit tests to key functions and `assert`s to key assumptions, so bugs surface early.
- **Logging instead of print**: use `logging` with levels so experiments can be traced.

## An example

An "engineered" experiment scaffold looks like this:

```python
import logging, random, json
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")

def set_seed(seed: int = 42):
    """Fix all sources of randomness to ensure reproducibility"""
    random.seed(seed)
    np.random.seed(seed)
    # If using torch: torch.manual_seed(seed)

# Configuration kept separate from code
config = {"seed": 42, "lookback": 96, "horizon": 24, "lr": 1e-3}

def main(cfg):
    set_seed(cfg["seed"])
    logging.info("Experiment started, config: %s", cfg)
    assert cfg["horizon"] > 0, "forecast horizon must be positive"   # check key assumptions explicitly
    # ... load data, train, evaluate ...
    metrics = {"mae": 0.123}
    # Archive the configuration and results together for later comparison
    with open("run.json", "w", encoding="utf-8") as f:
        json.dump({"config": cfg, "metrics": metrics}, f, ensure_ascii=False, indent=2)
    logging.info("Done, metrics: %s", metrics)

if __name__ == "__main__":
    main(config)
```

The point is not the amount of code, but that **every experiment can be rerun exactly from its archive**.

## Why it matters for time series forecasting

When training models such as **KUN / Kernel U-Net**, engineering practice matters all the more:

- **Comparable results**: if you change the model architecture and want to know whether it is better, the seed, data split and [evaluation metrics](../evaluation-metrics/) must be exactly the same; otherwise you can't tell "a real improvement" from "random fluctuation".
- **Discipline in splitting data**: time series data must be split into training/validation/test sets **by time**, never shuffled at random, which would cause "future information leakage". This discipline is upheld by engineering conventions.
- **Recoverable long experiments**: a model that trains for hours should save checkpoints regularly, so that it can resume after a crash.
- **Papers/reproduction**: record the [Git](../git/) commit, configuration and environment together, so that others can clone the repository and reproduce your curves.

## Summary

- Engineering practice = the set of habits that make code collaborative, reproducible and maintainable.
- Three pillars: **[version control](../git/), [reproducibility](../reproducibility/), environment isolation**.
- It doesn't raise model accuracy, but it **guarantees that your accuracy is trustworthy and repeatable**.
- In time series there is one more iron rule: **split data strictly by time and eliminate information leakage.**

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
