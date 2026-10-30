---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/gpu/
title: "GPUs and Parallel Computing"
no_comments: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

A **GPU (graphics processing unit)** is a chip originally built to render game graphics. It has thousands of small cores and is especially good at doing large numbers of similar, simple operations **at the same time** — such as [matrix multiplication](../matrix-multiplication/). This is exactly where the computing power for training deep models comes from.

## Intuition

The difference between a CPU and a GPU is like "a few PhDs" versus "a thousand primary-school pupils":

- A **CPU** has a few very powerful cores and excels at complex tasks with sequential dependencies — like a few PhDs: strong at logic and able to handle hard problems, but there aren't many of them.
- A **GPU** has a huge number of weaker cores and excels at **spreading the same simple operation out and computing it all at once** — like a thousand pupils, each doing one addition problem, and the whole set is done in an instant.

The core operations of a [neural network](../neural-network/) are matrix multiplications and additions, which **naturally break down into countless independent little multiply-adds**. Hand them all to the GPU's thousands of cores to process in parallel, and it is often tens to hundreds of times faster than a CPU. This is "**parallel computing**": splitting one big task into many small tasks that can run simultaneously.

## Key points

- **The precondition for parallelism**: tasks must be **independent of each other**. Each output element of a matrix product is computed independently, so it can be parallelized; whereas something like [dynamic programming](../dynamic-programming/), where each step depends on the previous one, is hard to parallelize.
- **[Vectorization](../vectorization/) is the key**: to make the GPU work hard, you must express the computation as operations on **whole arrays/tensors**, not as Python loops. The samples of a [batch](../batch/) are stacked into one big tensor and computed in a single go.
- **GPU memory (VRAM) is the bottleneck**: the GPU has its own separate memory, and the model, the data and the intermediate activations all have to fit in it. Not enough VRAM means lowering the batch size.
- **Moving data has a cost**: copying data back and forth between CPU memory and GPU memory is slow and should be minimized.

## An example

Running the same matrix multiplication on the CPU and on the GPU with PyTorch:

```python
import torch, time

A = torch.randn(8192, 8192)
B = torch.randn(8192, 8192)

# On the CPU
t = time.time()
_ = A @ B
print(f"CPU: {time.time() - t:.3f}s")

# Move to the GPU (if there is one)
if torch.cuda.is_available():
    A_g, B_g = A.cuda(), B.cuda()       # copy to GPU memory
    torch.cuda.synchronize()
    t = time.time()
    _ = A_g @ B_g                       # thousands of cores compute in parallel
    torch.cuda.synchronize()            # wait for the GPU to actually finish before timing
    print(f"GPU: {time.time() - t:.3f}s")
```

A typical result is that the GPU is dozens of times faster than the CPU. Note two details: `.cuda()` moves the tensors into GPU memory; `synchronize()` is needed because GPU calls are **asynchronous**, and without synchronizing the timing will be wrong.

{% include fviz/gpu-crossover.html %}

## Why it matters for time series forecasting

Training models like **KUN / Kernel U-Net** is almost impossible without a GPU:

- The sliding windows of a [batch](../batch/) are stacked into a tensor of shape `(batch, time steps, features)`; convolutions and downsampling are computed in parallel over the whole batch, and the GPU devours it in one go.
- The longer the sequences and the deeper the model, the more matrix computation there is, and the more pronounced the GPU's speed-up — a model that takes a day to train on a CPU may be done in an hour on a GPU.
- But to keep the GPU fed, the code must be **fully [vectorized](../vectorization/)**: use [NumPy](../numpy/) / PyTorch tensor operations rather than element-by-element `for` loops in Python, or the thousands of cores will sit idle most of the time.

## Common misconceptions

- **Thinking a GPU automatically makes everything faster**: only **parallelizable, compute-intensive** tasks benefit. With small data or strongly dependent sequential logic, a GPU can actually be slower because of data transfer.
- **Ignoring the memory limit**: a model or batch that is too large triggers "CUDA out of memory"; you need to reduce the batch size or use gradient accumulation.
- **Still writing Python loops**: loops run on the CPU while the GPU sits idle. Express the computation as whole-tensor operations.
- **Timing without synchronizing**: GPU calls return asynchronously, so call `synchronize()` before measuring speed.

---

[← Computer Science Fundamentals](../cs/) · [← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
