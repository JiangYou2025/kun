---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/reproducibility/
title: "Reproducibility"
no_comments: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

**Reproducibility** means that when someone else (or you, on another machine) reruns the same code on the same data, they get **the same results**. It is achieved by fixing random seeds, locking the environment and recording the data, and it is the bare minimum for scientific research and trustworthy modelling.

## Intuition

Imagine you publish a claim: "the KUN model reduces the error by 10%". If someone runs your code and gets only a 3% reduction, or even worse — then the claim is **not trustworthy**.

The usual sources of irreproducibility are the many hidden "random" elements and "latent variables" in an experiment:

- Random weight initialization, random shuffling of the data, random deactivation in [Dropout](../dropout/);
- Different library versions ([NumPy](../numpy/) 1.24 vs 1.26) may produce slightly different numbers;
- You switched to a different batch of data or changed a hyperparameter, but forgot to write it down.

**Reproducibility means nailing down these "uncertainties" one by one**, so that the result can be recreated exactly. This is not a nice-to-have; it is a basic requirement of science.

## Key points

To make an experiment reproducible, you need to control at least three things:

- **Fix the random seeds**: give every source of randomness the same seed (Python, NumPy, PyTorch, CUDA).
- **Lock the environment**: record the [Python](../python/) version and the exact versions of all dependencies (`requirements.txt` / `environment.yml`), ideally isolated with `venv`/`conda`/Docker.
- **Fix the data and the splits**: record the data source, its version/snapshot, and how it is split into training/validation/test sets (use [Git](../git/) together with data versioning).

In addition: record the **configuration and hyperparameters**, record the code's **commit hash**, and **archive the results**. All of this is part of good [engineering practice](../engineering-practice/).

## An example

A piece of code that "nails down" the sources of randomness:

```python
import os, random
import numpy as np
import torch

def set_seed(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # Make cuDNN use deterministic algorithms (slightly slower, but reproducible)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
print(np.random.rand(3))     # The same three numbers on every run

# The DataLoader's shuffling order must be fixed too
g = torch.Generator(); g.manual_seed(42)
# loader = DataLoader(ds, batch_size=32, shuffle=True, generator=g)
```

As long as the seed and the environment are the same, `np.random.rand(3)` produces **exactly the same** numbers every time — this is the starting point of reproducibility. Combine it with `pip freeze > requirements.txt` to lock dependency versions, and others can reproduce your curves on their own machines.

{% include fviz/seed-runs.html %}

## Relevance to time series forecasting

When researching **KUN / Kernel U-Net**, reproducibility directly determines whether a conclusion holds up:

- **Telling real improvements from fake ones**: if you claim a newly added downsampling module is better, you must compare under **exactly the same seeds, data splits and [evaluation metrics](../evaluation-metrics/)**; otherwise you cannot tell genuine progress from random fluctuation. Running several seeds and reporting mean ± standard deviation is more convincing.
- **Preventing information leakage**: time series data must be split into training/test sets **by time**, with fixed split points; once the data is randomly shuffled, the model "peeks" at the future, and the results become inflated and cannot be reproduced in real settings.
- **Verifiable by peers**: publish the commit, configuration, seeds and environment together so that others can clone and rerun — this is the foundation of a credible paper.

## Summary

- Reproducibility = the same code + data yield the same results again; it is the bare minimum for a trustworthy experiment.
- Three nails: **fix the random seeds, lock the environment, fix the data and the splits**.
- Also record the configuration and the [Git](../git/) commit, and archive the results.
- Extra emphasis for time series: **split by time and prevent leakage of future information**; averaging over several seeds is more robust.

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
