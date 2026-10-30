---
updated: "2026-06-11"
lang: en
ref: kernel-u-net
permalink: /en/kernel-u-net/
title: "Understanding Kernel U-Net (KUN) in Depth"
lead: "KUN uses a symmetric U-shaped structure to walk a time series \"from fine to coarse, then from coarse back to fine\", swapping in a pluggable kernel at every node. This page takes the structure apart layer by layer: what problem it solves, what each layer does, why it is efficient, how to get started, and how it fundamentally differs from DLinear and the Transformer."
prev: kun
math: true
---

> This is the **in-depth companion** to the [Frontier problems in time series, 2026](../kun/) page: that page explains which challenges KUN sets out to answer; this one covers KUN's **ideas, layer-by-layer architecture, complexity, and a hands-on tutorial** in full.

## KUN in one sentence

**KUN (Kernel U-Net) = the hierarchical shape of a U-Net + pluggable kernels.** It takes the "downsampling encoder, upsampling decoder, skip connections" design of the [U-Net](../foundations/u-net/) from image segmentation, carries it over to time series, and replaces the fixed convolution at each node with a small function you are free to choose: linear, an [MLP](../foundations/mlp/), or [attention](../foundations/attention/).

## What problem KUN solves

Recall [Frontier problems in time series, 2026](../kun/): long-horizon forecasting faces two unavoidable tensions.

1. **Multiple scales** — a real series stacks a long-term trend, mid-range cycles and short-term high-frequency detail on top of each other, like a composite of several waveforms. A model that looks at only one scale is incomplete.
2. **Efficiency vs. expressiveness** — the [Transformer](../foundations/transformer/) captures long-range dependencies with self-attention, but its complexity is $O(L^2)$, which becomes unaffordable for long sequences; a minimalist linear model (DLinear), on the other hand, is fast and strong but struggles to express complex structure.

KUN's answer: **separate the scales naturally with a hierarchical structure, and slide freely between "fast" and "powerful" with pluggable kernels.**

## First, see clearly: a series is "multi-scale"

To understand why KUN is shaped like a U, you first need to see one thing clearly: **a real time series often hides several "scales" at once.**

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 380" role="img" aria-label="A series decomposed into several scales">
  <text x="12" y="40" fill="var(--muted)" font-size="13">Raw series</text>
  <text x="12" y="56" fill="var(--muted)" font-size="11">(what you see)</text>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="175,72 222,58 269,66 316,44 363,58 410,36 457,50 504,28 551,44 598,22 645,36 690,16"/>
  <text x="430" y="116" fill="var(--muted)" font-size="13" text-anchor="middle">Taken apart = several scales added together ↓</text>
  <line x1="160" y1="128" x2="700" y2="128" stroke="var(--border)"/>

  <text x="12" y="178" fill="var(--accent)" font-size="13">Coarse scale</text>
  <text x="12" y="194" fill="var(--muted)" font-size="11">long-term trend</text>
  <line x1="175" y1="200" x2="690" y2="200" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,190 269,180 363,164 457,146 551,130 645,114 690,106"/>

  <text x="12" y="262" fill="var(--accent-2)" font-size="13">Mid scale</text>
  <text x="12" y="278" fill="var(--muted)" font-size="11">cycles</text>
  <line x1="175" y1="262" x2="690" y2="262" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"
    points="175,262 222,238 269,262 316,286 363,262 410,238 457,262 504,286 551,262 598,238 645,262 690,286"/>

  <text x="12" y="340" fill="#fbbf24" font-size="13">Fine scale</text>
  <text x="12" y="356" fill="var(--muted)" font-size="11">high-freq. detail</text>
  <line x1="175" y1="338" x2="690" y2="338" stroke="var(--border)" stroke-dasharray="3 4"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"
    points="175,338 215,324 255,350 295,328 335,352 375,322 415,346 455,330 495,352 535,326 575,348 615,330 655,346 690,332"/>
</svg>
<figcaption class="figcap">A single series stacks together a <strong>coarse</strong> long-term trend, <strong>mid-scale</strong> cycles and <strong>fine</strong> high-frequency fluctuations. Looking at any one scale alone gives an incomplete picture — this is what it means for a series to be <strong>multi-scale</strong>.</figcaption>
</figure>

Nearby detail (tomorrow a little higher than today) and the distant outline (this whole year has been rising) are information at **two different granularities**; each needs to be seen clearly on its own and then put back together. That is exactly what KUN's U shape does: the encoder makes the series **coarser** layer by layer (first the details, then the big outline), and the decoder reconstructs the forecast by making it **finer** layer by layer — taking care of every scale in one pass.

## Core idea: why a U shape

An image U-Net first shrinks the image layer by layer to see the "global outline", then enlarges it layer by layer to restore "local detail", stitching the two ends together with skip connections. Time series work the same way:

```
Input window (L steps)
   │  split into patches (segments)
   ▼
[ Encoder ]  patch → patch → patch → ⋯ → latent representation   (downsampling: fewer, coarser units at larger scales)
   │            │       │       │
   │          skip    skip    skip                               (skip connections: send details straight to the matching level)
   ▼            ▼       ▼       ▼
[ Decoder ]  patch ← patch ← patch ← ⋯ ← latent representation   (upsampling: reconstruct from coarse to fine)
   │
   ▼
Forecast horizon (H steps)
```

**Each level down sees a scale one step coarser**: shallow layers close to the input capture local, high-frequency detail; deeper layers see longer, coarser context. A series rarely lives at a single scale, and the U shape takes care of several scales at once.

## The architecture, layer by layer

### 1. Patching

The input is a window of length $L$ with $C$ channels (the number of variables), of shape $(L, C)$. KUN first cuts it along time into several **patches (segments)**, which form the units of the finest level.

### 2. Encoder: downsampling level by level

Each level **aggregates (chunks)** several adjacent patches into one coarser unit, so the temporal resolution drops and there are fewer units:

$$\text{Encoder:}\quad (L, C) \xrightarrow{\;k_1\;} (L/k_1,\, C') \xrightarrow{\;k_2\;} \cdots \xrightarrow{\;\;} (1,\, C_{\text{latent}})$$

where $k_l$ is the downsampling rate of level $l$ (set by `patch_sizes`). At the deepest point, the entire sequence is compressed into a **latent representation** that encodes the coarsest, global information (for example, "this whole year has been rising").

### 3. Decoder: upsampling level by level

The decoder mirrors the encoder: each level **expands** coarse units back to a finer resolution, reconstructing all the way to the forecast length $H$:

$$\text{Decoder:}\quad (1,\, C_{\text{latent}}) \xrightarrow{\;\;} \cdots \xrightarrow{\;\;} (H,\, C)$$

### 4. Skip connections

The output of each encoder level is wired directly to the matching level of the decoder. That way, when reconstructing from coarse to fine, **details are not lost in compression** — this is the connection in the U-Net's name that "skips the middle and spans the two ends".

### 5. Direct multi-output

KUN **outputs the entire forecast horizon at once** (direct multi-output), rather than predicting one step and feeding it back in to predict the next. This avoids the **error accumulation** of recursive forecasting — the further ahead you go, the more the errors of the recursive approach snowball.

## The key to its name: interchangeable kernels

The U shape is the skeleton; **the kernel is KUN's soul**. At every node of the U, the operation that "maps one group of segments to another" is not a hard-wired convolution but a **module you can swap out wholesale**, $\mathcal{K}_l$:

$$\text{Level } l\text{:}\quad \mathbf{z}_{l+1} = \mathcal{K}_l(\mathbf{z}_l)$$

### A fixed skeleton, swappable kernels

KUN splits a model into two parts:

- **The skeleton** decides how to cut, shrink and rebuild: patching, level-by-level downsampling, symmetric upsampling, skip connections and direct multi-output. This part is the same for every model and only has to be written once.
- **The kernel** does one thing only: at its level, turn one group of segments into another.

The only contract between them: a kernel takes an input of shape (segments, channels) and returns an output of the agreed shape. Any network that honours this interface can be dropped into any level of the U. So:

> **Building a new model = writing a new kernel**, not designing a new architecture from scratch. The new kernel automatically inherits the multi-scale structure, skip connections and direct multi-output that the skeleton provides.

### Swap the kernel, get a new model

| Kernels per level | Resulting model | Characteristics |
|-------------------|-----------------|-----------------|
| **Linear** everywhere | Hierarchical linear model | Tiny cost, $O(L)$; same idea as DLinear — a fast, strong baseline |
| **[MLP](../foundations/mlp/)** everywhere | Hierarchical MLP | Adds a moderate amount of nonlinearity |
| Linear at shallow levels, **[attention](../foundations/attention/)** at deep ones | Hybrid model | Attention only sees the short, downsampled sequence, so the cost stays under control |
| **LSTM / convolution** | Hierarchical RNN / CNN | Reuses classic operators as they are |
| **A kernel you write yourself** (state-space model, MoE, Fourier operator…) | Your new model | You write only the kernel; the skeleton is ready-made |

The repository's [`kun_lib_v2.py`](https://github.com/JiangYou2025/kun/blob/main/notebooks/kun_lib_v2.py) already ships four kernels: linear, conv, lstm and transformer. Each level can use a different kernel, and you can mix in kernels of your own.

### Writing your own kernel

A kernel is just a small module that inherits from `Kernel`: the constructor receives the input/output shapes and channel counts, and `forward` performs the mapping. Here is a GRU wrapped as a kernel in about a dozen lines:

```python
import torch.nn as nn
from math import prod
from kun_lib_v2 import Kernel

class GRUKernel(Kernel):
    """Example: a GRU as a kernel"""
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.rnn = nn.GRU(input_dim, output_dim, batch_first=True)
        self.resize = nn.Linear(prod(input_shape), prod(output_shape))

    def forward(self, x):                       # (..., *input_shape, input_dim)
        x = x.reshape(-1, prod(self.input_shape), self.input_dim)
        h, _ = self.rnn(x)                      # (batch, n_segments, output_dim)
        h = self.resize(h.transpose(1, 2)).transpose(1, 2)   # n_segments -> target n_segments
        return h.reshape(-1, *self.output_shape, self.output_dim)

# linear built-ins for the first two levels, your own GRU kernel at the deepest one (list length = number of levels)
kernel = ["linear", "linear", GRUKernel]
```

**The key point**: you try new ideas and trade compute against accuracy by **swapping kernels**, not by rewriting the model. "Designing a new model" becomes "giving one level a different $\mathcal{K}_l$". And since the deep kernels operate on a **sequence that has already been downsampled and shortened**, even with attention the cost is far lower than running $O(L^2)$ self-attention directly on the original long sequence.

## Complexity: why O(L)

| Property | DLinear | Transformer | **KUN** |
|------|---------|-------------|---------|
| Multi-scale | ✗ | Partial (patches) | ✓ Naturally hierarchical |
| Interpretability | Trend + seasonality | Attention maps | Each level corresponds to one scale |
| Kernel / operator | Linear only | Attention only | Linear / MLP / attention, **your choice** |
| Complexity | $O(L)$ | $O(L^2)$ | $O(L)$ (linear kernel) |
| Skip connections | ✗ | ✗ | ✓ Preserves detail |
| Multi-step output | Direct | Direct / recursive | Direct multi-output |

Hierarchical downsampling makes the sequence length shrink **geometrically** with depth, so even if the deep levels use heavier kernels, the total cost stays in check. On long-horizon, multivariate tasks this lets KUN get both "the efficiency of a linear model" and "expressiveness close to that of an attention model".

## Design philosophy: let the data decide the complexity

The judgement behind KUN matches the trend of the past decade (see [History, chapter 10](../history/10/)): **how complex a model should be ought to be decided by the data, not by betting on the heaviest architecture from the start.**

- Simple data → use linear kernels everywhere, and KUN reduces to an efficient hierarchical linear model;
- Complex data → swap in attention kernels at the levels that need them, adding capacity on demand.

Unifying "hierarchical modelling" and "flexible kernel choice" in one symmetric framework — that is KUN's exploration of **structured, efficient design** in the era of large models.

## Step-by-step tutorial: forecasting with KUN

> **A note on the API.** The snippets below show the *shape* of a typical training workflow, so you can adapt them to KUN's actual interface in this repository. Once the code is officially released, replace the import paths, class names and argument names with the real ones from the code. Treat this as a template, not as copy-and-run code.

### 1. Get the code and install it

```bash
git clone https://github.com/JiangYou2025/kun.git
cd kun
pip install -r requirements.txt   # or: pip install -e .
```

### 2. Prepare the data

KUN expects the sliding-window format described on the [time series](../time-series/) page: inputs of length `L` (the lookback) mapped to outputs of length `H` (the horizon), with `C` channels (variables).

```python
# x: array of shape (n_samples, L, C)  -> lookback windows
# y: array of shape (n_samples, H, C)  -> targets to predict
```

Be sure to **normalize per channel** (subtract the training-set mean, divide by the training-set standard deviation) and to **split by time**.

### 3. Configure the model

```python
from kun import KernelUNet            # change to the real import path

model = KernelUNet(
    input_len=336,     # L — lookback window
    pred_len=96,       # H — forecast horizon
    n_channels=7,      # C — number of variables
    patch_sizes=[16, 8, 4],   # how each level splits the sequence
    kernel="linear",          # "linear" | "mlp" | "attention" — the kernel for each level
)
```

Start with `kernel="linear"` and a shorter horizon. It trains in seconds and gives you a baseline to beat — exactly the discipline stressed on the [how to forecast](../forecasting/) page.

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

Compare this number with a **seasonal naive baseline**. If KUN wins, you have a genuinely useful model; if not, go back and check your windows, normalization and splitting.

## A sensible tuning order

1. **Lookback length `L`** — longer context usually helps long horizons, but only up to a point.
2. **Patch sizes** — more levels mean a stronger hierarchy; try to make each patch size divide the length at its level.
3. **Kernel choice** — upgrade from `linear` → `mlp` → `attention` only when the validation error shows the extra cost is worth it.
4. **Learning rate and epochs** — use early stopping based on validation MAE.

## Where to go next

- **To run it yourself**: see the [step-by-step tutorial](#step-by-step-tutorial-forecasting-with-kun) above, starting from a linear-kernel, short-horizon baseline.
- **To get your baselines solid first**: reread [how to forecast](../forecasting/) — KUN only means something relative to a baseline.
- **To see its place in the history of methods**: read [History, chapter 10 · Large models, linear regression and Kernel U-Net](../history/10/).
- **For a course perspective**: see [Lecture 11 · Kernel U-Net](../course/11/), which compares N-BEATS, DLinear and KUN.
- **To read the source / ask questions**: the [GitHub repository](https://github.com/JiangYou2025/kun).

<div class="note">
  <strong>Citing KUN.</strong> If KUN helps your research or product, please cite Jiang You's Kernel U-Net work and include a link to this repository.
</div>
