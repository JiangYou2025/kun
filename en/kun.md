---
lang: en
ref: kun
permalink: /en/kun/
title: "Using KUN — Kernel U-Net"
lead: "KUN (Kernel U-Net) is a hierarchical, symmetric architecture for long-horizon multivariate time-series forecasting. This page explains the idea behind it and gives you a step-by-step recipe to run it on your own data."
prev: forecasting
math: true
---

## The idea in one picture

KUN borrows its shape from the **U-Net** used in image segmentation: an **encoder** that progressively compresses the input, and a **symmetric decoder** that progressively expands it back to a prediction, with information flowing between matching levels.

```
input window
   │  split into patches
   ▼
[ Encoder ]  patch → patch → patch        (downsampling: fewer, coarser units)
   │            │      │       │
   │         skip   skip    skip          (matching levels are linked)
   ▼            ▼      ▼       ▼
[ Decoder ]  patch ← patch ← patch        (upsampling: rebuild the resolution)
   │
   ▼
forecast horizon
```

The twist that gives KUN its name: at every node of the U, the operation is a **pluggable kernel** rather than a fixed convolution. A kernel is just a small function that maps one segment to another — it can be a **linear layer, an MLP, an RNN, or an attention block**. You choose the kernel per level, so the same skeleton can be made lightweight or expressive depending on your data.

## Why this design works

- **Hierarchy matches time.** Short patches near the input capture local, high-frequency detail; deeper levels see longer, coarser context. A series rarely lives at a single scale, and the U captures several at once.
- **Symmetry keeps it efficient.** Because the decoder mirrors the encoder, the model reconstructs a full horizon without a quadratic blow-up in length — an advantage over plain Transformers on long sequences.
- **Kernels make it flexible.** Linear kernels give a fast, strong baseline (in the spirit of DLinear); attention kernels add capacity where the data needs it. You trade compute for accuracy by swapping kernels, not by rewriting the model.
- **Direct multi-output.** KUN predicts the whole horizon at once, avoiding the error accumulation of recursive forecasting.

## Step-by-step: forecasting with KUN

> **Note on the API.** The snippets below show the *shape* of a typical training pipeline so you can adapt them to KUN's actual interface in this repository. Replace the import path, class name, and argument names with the real ones from the code once they are published. Treat this as a template, not copy-paste-ready code.

### 1. Get the code and install

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # or: pip install -e .
```

### 2. Shape your data

KUN expects the sliding-window format from the [Time Series](./../time-series/) page: an input of length `L` (lookback) mapping to an output of length `H` (horizon), with `C` channels (variables).

```python
# x: array of shape (num_samples, L, C)  -> the lookback windows
# y: array of shape (num_samples, H, C)  -> the targets to predict
```

Always **normalise per channel** (subtract the train mean, divide by the train std) and **split by time**.

### 3. Configure the model

```python
from kun import KernelUNet            # adjust to the real import

model = KernelUNet(
    input_len=336,     # L — lookback window
    pred_len=96,       # H — forecast horizon
    n_channels=7,      # C — number of variables
    patch_sizes=[16, 8, 4],   # how each level splits the sequence
    kernel="linear",          # "linear" | "mlp" | "attention" — per-level kernels
)
```

Start with `kernel="linear"` and a short horizon. It trains in seconds and gives you the baseline to beat — exactly the discipline from the [Forecasting](./../forecasting/) page.

### 4. Train

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.L1Loss()          # MAE — robust and interpretable

for epoch in range(50):
    for xb, yb in train_loader:
        opt.zero_grad()
        pred = model(xb)             # (batch, H, C)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.step()
```

### 5. Evaluate and forecast

```python
model.eval()
with torch.no_grad():
    pred = model(x_test)             # forecast the held-out horizon
mae = (pred - y_test).abs().mean()
print("Test MAE:", mae.item())
```

Compare this number against the **seasonal-naïve baseline**. If KUN wins, you have a real model; if not, revisit your windows, normalisation, and split.

## A sensible tuning order

1. **Lookback `L`** — longer context usually helps long horizons, up to a point.
2. **Patch sizes** — more levels = more hierarchy; keep each patch size a divisor of the level's length.
3. **Kernel choice** — move from `linear` → `mlp` → `attention` only if the validation error justifies the extra cost.
4. **Learning rate & epochs** — use early stopping on the validation MAE.

## Where to go next

- Re-read [How to forecast](./../forecasting/) and run the baselines first — KUN is only meaningful relative to them.
- Open an issue or read the source on [GitHub](https://github.com/JiangYou2025/kun) to find the exact, current API.

<div class="note">
  <strong>Citing KUN.</strong> If KUN helps your research or product, please cite the Kernel U-Net work by Jiang You and link back to this repository.
</div>
