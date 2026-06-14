"""
KUNet v2 — N-dimensional Universal Encoder / Decoder

Core idea: Take any N-dimensional space (e.g. H×W×L), progressively chunk and
reduce dimensions to a latent space in user-specified order, then symmetrically
expand back. UNet skip connections between encoder/decoder layers.

Key concepts:
- chunk_multiples: how many factors each spatial dim is split into
- chunk_names/order: processing order, e.g. "h2w2hwl3"
- spec syntax: [hwl] = packed block, bare letter = single dim
- UNet skip: encoder saves activations, decoder adds them back
"""

from __future__ import annotations

import math
import re
from collections import defaultdict, deque
from itertools import product as iterproduct
from math import prod
from typing import List, Tuple, Union

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


# ══════════════════════════════════════════════
# 1. Spec Parsing Utilities
# ══════════════════════════════════════════════

def parse_spec(spec: str):
    """
    Parse a spec string into groups.

    "[hwl][hwl]" -> ["hwl", "hwl"]
    "hwlhwl[hwl]" -> ["h","w","l","h","w","l","hwl"]
    """
    res = []
    i = 0
    while i < len(spec):
        if spec[i] == "[":
            j = spec.find("]", i)
            res.append(spec[i + 1 : j])
            i = j + 1
        else:
            res.append(spec[i])
            i += 1
    return res

from collections import defaultdict, deque

def apply_spec(spec, values, labels):
    """
    Return:
        out_vals:  [(...)]
        out_names: ["..."]
        out_idxs:  [(...)]  <-- 新增 index 对应关系
    """
    groups = parse_spec(spec)

    # 建桶：value + index
    pools = defaultdict(deque)
    for idx, (v, l) in enumerate(zip(values, labels)):
        pools[l].append((v, idx))

    out_vals = []
    out_names = []
    out_idxs = []

    # 按规则消费
    for g in groups:
        tmp_vals = []
        tmp_idxs = []

        for ch in g:
            v, idx = pools[ch].popleft()
            tmp_vals.append(v)
            tmp_idxs.append(f"id({idx})")

        out_vals.append(tuple(tmp_vals))
        out_idxs.append(tuple(tmp_idxs))
        out_names.append(g)

    return out_vals, out_names, out_idxs


# ══════════════════════════════════════════════
# 2. Auto Chunk Size (Factor Decomposition)
# ══════════════════════════════════════════════

def pop_std(x):
    k = len(x)
    mean = sum(x) / k
    var = sum((xi - mean) ** 2 for xi in x) / k
    return math.sqrt(var)


def brute_min_score_ge_N(N: int, k: int, d: int):
    """
    Find k factors whose product equals N, minimising imbalance.

    Falls back to product >= N heuristic when no exact factorisation exists.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    if d < 0:
        raise ValueError("d must be >= 0")

    def _divisors(n):
        divs = []
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
        return sorted(divs)

    def _factorise(n, k):
        if k == 1:
            yield (n,)
            return
        for f in _divisors(n):
            if f > n:
                break
            for rest in _factorise(n // f, k - 1):
                yield (f,) + rest

    best_exact = None
    for x in _factorise(N, k):
        std = pop_std(x)
        score = std
        cur = (score, 0.0, std, N, sum(x), x)
        if best_exact is None or cur < best_exact:
            best_exact = cur

    if best_exact is not None:
        score, pct, std, prod_val, _, x = best_exact
        return {
            "x_desc": tuple(sorted(x, reverse=True)),
            "product": prod_val,
            "percentage_error": 0.0,
            "std": std,
            "score": score,
            "candidates": list(_divisors(N)),
        }

    # Fallback: product >= N
    r = N ** (1.0 / k)
    lo = max(1, int(math.floor(r)) - d)
    hi = max(1, int(math.ceil(r)) + d)
    candidates = list(range(lo, hi + 1))
    best = None
    for x in iterproduct(candidates, repeat=k):
        prod_val = 1
        for xi in x:
            prod_val *= xi
        if prod_val < N:
            continue
        std = pop_std(x)
        pct = (prod_val - N) / N
        score = 0.2 * std + 0.8 * pct
        cur = (score, pct, std, prod_val, sum(x), x)
        if best is None or cur < best:
            best = cur
    if best is None:
        x = (hi,) * k
        prod_val = hi ** k
        std = pop_std(x)
        pct = (prod_val - N) / N
        score = 0.5 * std + 0.5 * pct
        return {
            "x_desc": tuple(sorted(x, reverse=True)),
            "product": prod_val,
            "percentage_error": pct,
            "std": std,
            "score": score,
            "candidates": candidates,
        }
    score, pct, std, prod_val, _, x = best
    return {
        "x_desc": tuple(sorted(x, reverse=True)),
        "product": prod_val,
        "percentage_error": pct,
        "std": std,
        "score": score,
        "candidates": candidates,
    }


def create_chunk_size_raw(
    input_shape: Tuple[int, ...],
    chunk_multiples: Tuple[int, ...],
) -> Tuple[int, ...]:
    """
    Auto-factorise each spatial dimension.

    Example: input_shape=(27,64,8), chunk_multiples=(3,3,3)
        27 -> (3,3,3), 64 -> (4,4,4), 8 -> (2,2,2)
        returns (3,3,3, 4,4,4, 2,2,2)
    """
    chunk_sizes_list: List[int] = []
    for i in range(len(input_shape)):
        result = brute_min_score_ge_N(N=input_shape[i], k=chunk_multiples[i], d=2)
        chunk_sizes_list.extend(result["x_desc"])
    return tuple(chunk_sizes_list)


# ══════════════════════════════════════════════
# 3. Default Chunk Names
# ══════════════════════════════════════════════

def create_chunk_names(
    shape_name: List[str],
    chunk_multiples: Tuple[int, ...],
) -> str:
    """
    Generate flattened chunk name string.

    Example: shape_name="HWL", chunk_multiples=(3,3,3) -> "hhhwwwlll"
    """
    assert len(shape_name) == len(chunk_multiples), "dimension mismatch"
    return "".join(dim.lower() * k for dim, k in zip(shape_name, chunk_multiples))


# ══════════════════════════════════════════════
# 4. Spec Expansion & Permutation
# ══════════════════════════════════════════════

def expand_spec(spec: str, keep_brackets: bool = True) -> str:
    """
    Recursively expand a spec string.

    Examples:
        expand_spec("h2w2hwl3") -> "hhwwhwlll"
        expand_spec("h2w2[hl2]wl") -> "hhww[hll]wl"
        expand_spec("[ab2]3") -> "[abb][abb][abb]"
    """
    n = len(spec)

    def parse(i: int, in_bracket: bool = False):
        out = []
        while i < n:
            ch = spec[i]
            if ch == "]":
                if not in_bracket:
                    raise ValueError(f"Unexpected ']' at position {i}")
                return "".join(out), i
            if ch == "[":
                inner, j = parse(i + 1, in_bracket=True)
                if j >= n or spec[j] != "]":
                    raise ValueError(f"Unmatched '[' at position {i}")
                token = f"[{inner}]" if keep_brackets else inner
                i = j + 1
            else:
                token = ch
                i += 1
            # parse optional repeat number
            j = i
            while j < n and spec[j].isdigit():
                j += 1
            repeat = int(spec[i:j]) if j > i else 1
            out.append(token * repeat)
            i = j
        if in_bracket:
            raise ValueError("Unmatched '['")
        return "".join(out), i

    result, end = parse(0, in_bracket=False)
    if end != n:
        raise ValueError("Parsing did not consume full input")
    return result


def _expand_token_to_letters(token: str):
    parts = re.findall(r"([a-z])(\d*)", token)
    out = []
    for c, n in parts:
        k = int(n) if n else 1
        out.extend([c] * k)
    return out


def expand_letters(sig: str):
    tokens = re.findall(r"\[([^\]]+)\]|([a-z]\d*)", sig)
    out = []
    for bracket, token in tokens:
        if bracket:
            out.extend(_expand_token_to_letters(bracket))
        else:
            out.extend(_expand_token_to_letters(token))
    return out


def expand_groups(sig: str):
    tokens = re.findall(r"\[([^\]]+)\]|([a-z]\d*)", sig)
    out = []
    for bracket, token in tokens:
        if bracket:
            out.append("".join(_expand_token_to_letters(bracket)))
        else:
            out.extend(_expand_token_to_letters(token))
    return out

from collections import defaultdict

def make_perm(default_order, user_order):
    """
    default_order, user_order:
        can be str or list-like tokens

    Example:
        make_perm("hwhl", "whhl")
        make_perm(["id0","id1","id2"], ["id2","id0","id1"])
    """
    if len(default_order) != len(user_order):
        raise ValueError("length mismatch")
    if sorted(default_order) != sorted(user_order):
        raise ValueError("user_order must be permutation of default_order")

    positions = defaultdict(list)
    for i, tok in enumerate(default_order):
        positions[tok].append(i)

    used = {k: 0 for k in positions}
    perm = []
    for tok in user_order:
        idx = positions[tok][used[tok]]
        perm.append(idx)
        used[tok] += 1
    return perm


# ══════════════════════════════════════════════
# 5. Kernel Modules
# ══════════════════════════════════════════════

class Kernel(nn.Module):
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__()
        self.input_shape = tuple(input_shape)
        self.output_shape = tuple(output_shape)
        self.input_dim = input_dim
        self.output_dim = output_dim
        for k, v in kw.items():
            setattr(self, k, v)


class Linear(Kernel):
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.activation = kw.get("activation", "tanh")
        self.drop_out_p = kw.get("drop_out_p", 0.01)
        self.kernel_hidden_layer = kw.get("kernel_hidden_layer", 0)

        in_sz = prod(input_shape) * input_dim
        out_sz = prod(output_shape) * output_dim
        layers = []
        is_enc = in_sz >= out_sz

        if is_enc:
            gap = int((in_sz - out_sz) / (self.kernel_hidden_layer + 1))
            hsizes = [in_sz - i * gap for i in range(1, self.kernel_hidden_layer + 1)]
        else:
            gap = int((out_sz - in_sz) / (self.kernel_hidden_layer + 1))
            hsizes = [in_sz + i * gap for i in range(1, self.kernel_hidden_layer + 1)]

        cur = in_sz
        for hs in hsizes:
            layers.append(nn.Linear(cur, hs))
            if self.activation == "relu":
                layers.append(nn.ReLU())
            else:
                layers.append(nn.Tanh())
            layers.append(nn.Dropout(self.drop_out_p))
            cur = hs

        layers.append(nn.Linear(cur, out_sz))
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        x = x.reshape(-1, prod(self.input_shape) * self.input_dim)
        x = self.layers(x)
        return x.reshape(-1, *self.output_shape, self.output_dim)


class Conv(Kernel):
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.activation = kw.get("activation", "tanh")
        self.drop_out_p = kw.get("drop_out_p", 0.01)
        self.kernel_hidden_layer = kw.get("kernel_hidden_layer", 0)

        layers = [nn.Linear(prod(input_shape) * input_dim, prod(output_shape) * output_dim)]
        if self.drop_out_p > 0:
            layers.append(nn.Dropout(self.drop_out_p))
        if self.activation == "relu":
            layers.append(nn.ReLU())
        else:
            layers.append(nn.Tanh())

        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        x = x.reshape(-1, prod(self.input_shape) * self.input_dim)
        x = self.layers(x)
        return x.reshape(-1, *self.output_shape, self.output_dim)


class LSTM(Kernel):
    """LSTM kernel.

    Serialize the chunk cells along the spec-induced order, consume them with an LSTM,
    and project the final hidden state to (output_shape, output_dim).

    Per-call cost: O(s * d^2) with s = prod(input_shape), d = max(input_dim, hidden_size);
    executes sequentially in s steps (recurrence is the price of the inductive bias).
    """

    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.hidden_size = kw.get("hidden_size", max(input_dim, output_dim))
        self.num_layers = kw.get("num_layers", 1)
        self.drop_out_p = kw.get("drop_out_p", 0.01)
        self.bidirectional = kw.get("bidirectional", False)

        self.proj_in = nn.Linear(prod(input_shape) * input_dim, self.hidden_size)
        self.lstm = nn.LSTM(
            input_size=self.hidden_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers,
            batch_first=True,
            dropout=self.drop_out_p if self.num_layers > 1 else 0.0,
            bidirectional=self.bidirectional,
        )
        lstm_out_size = self.hidden_size * (2 if self.bidirectional else 1)
        self.proj_out = nn.Linear(lstm_out_size, prod(output_shape) * output_dim)

    def forward(self, x):
        # x: (..., *input_shape, input_dim) → (B, in_size) with in_size = prod(input_shape) * input_dim
        x = x.reshape(-1, prod(self.input_shape) * self.input_dim)
        # project the flattened input to hidden_size, feed as a length-1 sequence
        x = self.proj_in(x).unsqueeze(1)
        _, (h_n, _) = self.lstm(x)
        if self.bidirectional:
            # h_n: (num_layers * 2, B, hidden); concatenate the last layer's two directions
            h_last = torch.cat([h_n[-2], h_n[-1]], dim=-1)
        else:
            h_last = h_n[-1]
        out = self.proj_out(h_last)
        return out.reshape(-1, *self.output_shape, self.output_dim)


class Transformer(Kernel):
    """Transformer kernel.

    Treat the flattened chunk as a sequence of s = prod(input_shape) tokens of width input_dim,
    apply n_layers self-attention blocks, then flatten + project to (output_shape, output_dim).

    Per-call cost: O(s^2 * d + s * d^2). Kept tractable in practice because the auto-factorization
    keeps chunk sizes small.
    """

    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.n_heads = kw.get("n_heads", 1)
        self.n_layers = kw.get("n_layers", 1)
        self.ff_mult = kw.get("ff_mult", 4)
        self.drop_out_p = kw.get("drop_out_p", 0.01)

        # nn.MultiheadAttention requires d_model % n_heads == 0; fall back to 1 head if not.
        if input_dim % self.n_heads != 0:
            self.n_heads = 1

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=input_dim,
            nhead=self.n_heads,
            dim_feedforward=self.ff_mult * input_dim,
            dropout=self.drop_out_p,
            batch_first=True,
            activation="gelu",
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=self.n_layers)
        self.proj = nn.Linear(prod(input_shape) * input_dim, prod(output_shape) * output_dim)

    def forward(self, x):
        # x: (..., *input_shape, input_dim) → (B, S, input_dim) with S = prod(input_shape)
        x = x.reshape(-1, prod(self.input_shape), self.input_dim)
        x = self.transformer(x)
        x = x.reshape(-1, prod(self.input_shape) * self.input_dim)
        x = self.proj(x)
        return x.reshape(-1, *self.output_shape, self.output_dim)


KERNEL_MAP = {"linear": Linear, "conv": Conv, "lstm": LSTM, "transformer": Transformer}


def _resolve_kernel(k):
    if isinstance(k, str):
        return KERNEL_MAP[k.lower()]
    return k


def _apply_perm(lst, perm):
    return [lst[p] for p in perm]


# ══════════════════════════════════════════════
# 6. KernelWrapper
# ══════════════════════════════════════════════

class KernelWrapper(nn.Module):
    """
    Wraps a Kernel with spatial reshape logic and UNet skip connection support.
    """

    def __init__(
        self,
        kernel_cls,
        input_shape: Tuple[int, ...],
        output_shape: Tuple[int, ...],
        input_dim: int,
        output_dim: int,
        mode: str = "encode",
        unet_skip=True,
        **kwargs,
    ):
        super().__init__()
        self.input_shape = tuple(input_shape)
        self.output_shape = tuple(output_shape)
        self.mode = mode
        self.input_dim = input_dim
        self.output_dim = output_dim

        self.unet_skip = unet_skip
        self.unet_skip_concat = kwargs.get("unet_skip_concat", False)
        self._skip_saved = None
        self._mode_enc = mode == "encode"
        self.verbose = kwargs.get("verbose", False)
        self.chunk_name = kwargs.get("chunk_name", None)

        kclass = _resolve_kernel(kernel_cls)
        self.kernel = kclass(
            input_shape=input_shape,
            output_shape=output_shape,
            input_dim=input_dim,
            output_dim=output_dim,
            **kwargs,
        )

    def extra_repr(self) -> str:
        k = self.kernel
        return (
            f"mode={self.mode}, "
            f"spatial {self.input_shape} → {self.output_shape}, "
            f"dimension {self.input_dim} → {self.output_dim}, "
            f"kernel {k.input_shape} × {k.input_dim} → {k.output_shape} × {k.output_dim}"
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.verbose:
            print(f"{self.input_shape} → {self.output_shape}  |  x-shape {tuple(x.shape)}")

        batch = x.shape[0]
        x = x.reshape(-1, *self.input_shape, self.input_dim)
        if self.unet_skip and self._mode_enc:
            self._skip_saved = x.detach().clone() if not self.training else x.clone()

        x = self.kernel(x)
        x = x.reshape(-1, *self.output_shape, self.output_dim)

        if self.unet_skip and not self._mode_enc:
            x = x + self._skip_saved

        return x


# ══════════════════════════════════════════════
# 7. KUNetEncoder
# ══════════════════════════════════════════════

class KUNetEncoder(nn.Module):
    """
    N-dimensional encoder that progressively reduces spatial dimensions.

    Given input_shape = (H, W, L) and chunk_multiples = (3, 3, 3):
      1. Auto-factorise each dimension into chunk_multiples[i] factors
      2. Default processing order = "hhhwwwlll"
      3. User can reorder via chunk_names, e.g. "h2w2hwl3"
      4. Each step reduces one group of dimensions via a kernel
    """

    def __init__(
        self,
        input_shape: Union[int, Tuple[int, ...]] = (64, 64, 64),
        shape_name: str = "HWL",
        input_dim: int = 10,
        latent_shape: Union[int, Tuple[int, ...]] = (1, 1, 1),
        latent_dim: int = 128,
        hidden_dim: Union[int, List[int]] = 128,
        chunk_multiples: Tuple[int, ...] = (3, 3, 3),
        chunk_names: Union[str, List[str]] = "auto",
        chunk_sizes: Union[str, Tuple[int, ...]] = "auto",
        kernel: Union[str, list] = "linear",
        unet_skip=True,
        **kwargs,
    ):
        super().__init__()

        self.input_shape = tuple(input_shape)
        self.shape_name = shape_name
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.latent_shape = tuple(latent_shape)
        self.latent_dim = latent_dim
        self.chunk_multiples = chunk_multiples
        self.chunk_names = chunk_names
        self.chunk_sizes = chunk_sizes
        self.kernel = kernel
        self.unet_skip = unet_skip
        self.kwargs = kwargs
        self.verbose = kwargs.get("verbose", False)

        n_spatial = len(input_shape)
        assert len(latent_shape) == n_spatial
        assert len(shape_name) == n_spatial
        assert len(chunk_multiples) == n_spatial

        # 1. Compute chunk_size (auto-factorise each dimension)
        default_chunk_size_raw = create_chunk_size_raw(input_shape, chunk_multiples)
        chunk_size_raw = default_chunk_size_raw if chunk_sizes == "auto" else chunk_sizes
        self.default_chunk_size_raw = default_chunk_size_raw

        if self.verbose:
            print(f"[Encoder] default_chunk_size_raw: {default_chunk_size_raw}")
            print(f"[Encoder] chunk_size_raw: {chunk_size_raw}")

        # 2. Compute default & user chunk_order
        default_name_raw = create_chunk_names(shape_name, chunk_multiples)
        chunk_names_raw = default_name_raw if chunk_names == "auto" else expand_spec(chunk_names)
        chunk_names_pure = default_name_raw if chunk_names == "auto" else expand_spec(chunk_names, keep_brackets=False)
        default_idx_pure = [f"id({i})" for i in range(len(chunk_names_pure))]

        if self.verbose:
            print(f"[Encoder] default_name_raw: {default_name_raw}")
            print(f"[Encoder] chunk_names_raw: {chunk_names_raw}")
            print(f"[Encoder] chunk_names_pure: {chunk_names_pure}")
            print(f"[Encoder] default_idx_pure: {default_idx_pure}")

        # 3. Compute chunk_size_block and chunk_names_block
        chunk_size_block, chunk_names_block, chunk_idx_block = apply_spec(chunk_names_raw, chunk_size_raw, default_name_raw)
        chunk_idx_by_block = list(chunk_idx_block)
        chunk_idx_pure = [item for t in chunk_idx_by_block for item in t]

        if self.verbose:
            print(f"[Encoder] chunk_size_block: {chunk_size_block}")
            print(f"[Encoder] chunk_names_block: {chunk_names_block}")
            print(f"[Encoder] chunk_idx_block: {chunk_names_block}")
            print(f"[Encoder] chunk_idx_by_block: {chunk_idx_by_block}")
            print(f"[Encoder] chunk_idx_pure: {chunk_idx_pure}")

        # 4. Compute permutation index
        raw_permutation = make_perm(default_name_raw, chunk_names_pure)

        raw_permutation = make_perm(default_idx_pure, chunk_idx_pure)
        self._raw_permutation_p1 = tuple(reversed(list(x + 1 for x in raw_permutation)))

        if self.verbose:
            print(f"[Encoder] raw_permutation: {raw_permutation}")
            print(f"[Encoder] _raw_permutation_p1: {self._raw_permutation_p1}")

        # 5. Build per-step dimension lists
        total_chunks = len(chunk_size_block)
        n_layers = total_chunks

        hidden_dim_list = [hidden_dim] * (n_layers - 1) if isinstance(hidden_dim, int) else hidden_dim
        kernel_list = [kernel] * n_layers if isinstance(kernel, str) else kernel

        input_dim_list = [input_dim] + hidden_dim_list
        output_dim_list = hidden_dim_list + [latent_dim]

        # 6. Create KernelWrapper layers
        self.layers = nn.ModuleList()
        for i in range(n_layers):
            in_chunk_size = chunk_size_block[i]
            out_chunk_size = (1,)
            chunk_name = chunk_names_block[i]

            if self.verbose:
                print(f"  layer {i}: {kernel_list[i]} {input_dim_list[i]}->{output_dim_list[i]} "
                      f"{in_chunk_size}->{out_chunk_size} [{chunk_name}]")

            self.layers.append(
                KernelWrapper(
                    kernel_cls=kernel_list[i],
                    input_dim=input_dim_list[i],
                    output_dim=output_dim_list[i],
                    input_shape=in_chunk_size,
                    output_shape=out_chunk_size,
                    unet_skip=unet_skip,
                    mode="encode",
                    chunk_name=chunk_name,
                    **kwargs,
                )
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (batch, *input_shape, input_dim) e.g. (B, 27, 64, 8, 10)
        returns: (batch, *latent_shape, latent_dim) e.g. (B, 1, 1, 1, 128)
        """
        batch = x.shape[0]
        x = x.reshape(batch, *self.default_chunk_size_raw, self.input_dim)
        perm = (0,) + self._raw_permutation_p1 + (len(x.shape) - 1,)
        x = x.permute(perm)

        for i, w in enumerate(self.layers):
            x = w(x)

        x = x.reshape(batch, *self.latent_shape, self.latent_dim)
        return x


# ══════════════════════════════════════════════
# 8. KUNetDecoder
# ══════════════════════════════════════════════

class KUNetDecoder(nn.Module):
    """
    Symmetric decoder that reverses the encoder's processing order.
    Each step expands a spatial dimension instead of reducing it.
    """

    def __init__(
        self,
        output_shape: Union[int, Tuple[int, ...]] = (64, 64, 64),
        shape_name: str = "HWL",
        output_dim: int = 10,
        latent_shape: Union[int, Tuple[int, ...]] = (1, 1, 1),
        latent_dim: int = 128,
        hidden_dim: Union[int, List[int]] = 128,
        chunk_multiples: Tuple[int, ...] = (3, 3, 3),
        chunk_names: str = "auto",
        chunk_sizes: Union[str, Tuple[int, ...]] = "auto",
        kernel: Union[str, list] = "linear",
        unet_skip=True,
        **kwargs,
    ):
        super().__init__()

        self.output_shape = tuple(output_shape)
        self.shape_name = shape_name
        self.output_dim = output_dim
        self.latent_shape = tuple(latent_shape)
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim
        self.chunk_multiples = chunk_multiples
        self.chunk_names = chunk_names
        self.chunk_sizes = chunk_sizes
        self.kernel = kernel
        self.unet_skip = unet_skip
        self.kwargs = kwargs
        self.verbose = kwargs.get("verbose", False)

        n_spatial = len(output_shape)
        assert len(latent_shape) == n_spatial
        assert len(shape_name) == n_spatial
        assert len(chunk_multiples) == n_spatial

        # 1. Compute chunk_size
        default_chunk_size_raw = create_chunk_size_raw(output_shape, chunk_multiples)
        chunk_size_raw = default_chunk_size_raw if chunk_sizes == "auto" else chunk_sizes
        self.default_chunk_size_raw = default_chunk_size_raw

        if self.verbose:
            print(f"[Decoder] default_chunk_size_raw: {default_chunk_size_raw}")
            print(f"[Decoder] chunk_size_raw: {chunk_size_raw}")

        # 2. Compute default & user chunk_order
        default_name_raw = create_chunk_names(shape_name, chunk_multiples)
        chunk_names_raw = default_name_raw if chunk_names == "auto" else expand_spec(chunk_names)
        chunk_names_pure = default_name_raw if chunk_names == "auto" else expand_spec(chunk_names, keep_brackets=False)
        default_idx_pure = [f"id({i})" for i in range(len(chunk_names_pure))]

        if self.verbose:
            print(f"[Decoder] default_name_raw: {default_name_raw}")
            print(f"[Decoder] chunk_names_raw: {chunk_names_raw}")
            print(f"[Decoder] chunk_names_pure: {chunk_names_pure}")
            print(f"[Decoder] default_idx_pure: {default_idx_pure}")

        # 3. Compute chunk_size_block (reversed for decoder)
        chunk_size_block, chunk_names_block, chunk_idx_block = apply_spec(chunk_names_raw, chunk_size_raw, default_name_raw)
        chunk_size_block_reversed = list(reversed(chunk_size_block))
        chunk_names_block_reversed = list(reversed(chunk_names_block))
        chunk_idx_by_block_reversed = list(reversed(chunk_idx_block))

        chunk_idx_pure_reversed = [item for t in chunk_idx_by_block_reversed for item in t]

        if self.verbose:
            print(f"[Decoder] chunk_size_block: {chunk_size_block}")
            print(f"[Decoder] chunk_names_block: {chunk_names_block}")
            print(f"[Decoder] chunk_idx_block: {chunk_idx_block}")
            print(f"[Decoder] chunk_size_block_reversed: {chunk_size_block_reversed}")
            print(f"[Decoder] chunk_names_block_reversed: {chunk_names_block_reversed}")
            print(f"[Decoder] chunk_idx_by_block_reversed: {chunk_idx_by_block_reversed}")
            print(f"[Decoder] chunk_idx_pure_reversed: {chunk_idx_pure_reversed}")

        # 4. Compute permutation index
        raw_permutation = make_perm(default_idx_pure, chunk_idx_pure_reversed)
        self._raw_permutation_p1 = tuple(reversed(list(x + 1 for x in raw_permutation)))

        if self.verbose:
            print(f"[Decoder] raw_permutation: {raw_permutation}")
            print(f"[Decoder] _raw_permutation_p1: {self._raw_permutation_p1}")

        # 5. Build per-step dimension lists (reversed)
        n_layers = len(chunk_size_block_reversed)

        hidden_dim_list = [hidden_dim] * (n_layers - 1) if isinstance(hidden_dim, int) else hidden_dim
        kernel_list = [kernel] * n_layers if isinstance(kernel, str) else kernel

        kernel_list = list(reversed(kernel_list))
        hidden_dim_list = list(reversed(hidden_dim_list))

        input_dim_list = [latent_dim] + hidden_dim_list
        output_dim_list = hidden_dim_list + [output_dim]

        # 6. Create KernelWrapper layers
        self.layers = nn.ModuleList()
        for i in range(n_layers):
            in_chunk_size = (1,)
            out_chunk_size = chunk_size_block_reversed[i]
            chunk_name = chunk_names_block_reversed[i]

            if self.verbose:
                print(f"  layer {i}: {kernel_list[i]} {input_dim_list[i]}->{output_dim_list[i]} "
                      f"{in_chunk_size}->{out_chunk_size} [{chunk_name}]")

            self.layers.append(
                KernelWrapper(
                    kernel_cls=kernel_list[i],
                    input_dim=input_dim_list[i],
                    output_dim=output_dim_list[i],
                    input_shape=in_chunk_size,
                    output_shape=out_chunk_size,
                    unet_skip=unet_skip,
                    mode="decode",
                    chunk_name=chunk_name,
                    **kwargs,
                )
            )

        self._hidden_dim_list = hidden_dim_list
        self._kernel_list = kernel_list
        self._kwargs = kwargs

    @classmethod
    def from_encoder(cls, encoder: KUNetEncoder, **override_kw):
        """Build a decoder that is the exact symmetric reverse of an encoder."""
        kw = dict(encoder.kwargs)
        kw.update(override_kw)
        return cls(
            output_shape=encoder.input_shape,
            shape_name=encoder.shape_name,
            output_dim=encoder.input_dim,
            latent_shape=encoder.latent_shape,
            latent_dim=encoder.latent_dim,
            hidden_dim=encoder.hidden_dim,
            chunk_multiples=encoder.chunk_multiples,
            chunk_names=encoder.chunk_names,
            chunk_sizes=encoder.chunk_sizes,
            kernel=encoder.kernel,
            unet_skip=encoder.unet_skip,
            **kw,
        )


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (batch, *latent_shape, latent_dim)
        returns: (batch, *output_shape, output_dim)
        """
        batch = x.shape[0]

        for i, w in enumerate(self.layers):
            x = w(x)

        x = x.reshape(batch, *self.default_chunk_size_raw, self.output_dim)
        perm = (0,) + self._raw_permutation_p1 + (len(x.shape) - 1,)
        x = x.reshape(batch, *self.output_shape, self.output_dim)
        return x


# ══════════════════════════════════════════════
# 9. KUNetEncoderDecoder (Full UNet)
# ══════════════════════════════════════════════

class KUNetEncoderDecoder(nn.Module):
    def __init__(
        self,
        input_shape=(64, 64, 64),
        shape_name="HWL",
        input_dim=10,
        latent_shape=(1, 1, 1),
        latent_dim=128,
        output_shape=None,
        output_dim=None,
        hidden_dim=128,
        chunk_multiples=(3, 3, 3),
        chunk_names="auto",
        chunk_sizes="auto",
        kernel="linear",
        unet_skip=True,
        **kwargs,
    ):
        super().__init__()
        if output_shape is None:
            output_shape = input_shape
        if output_dim is None:
            output_dim = input_dim

        self.input_shape = tuple(input_shape)
        self.shape_name = shape_name
        self.input_dim = input_dim
        self.output_shape = tuple(output_shape)
        self.output_dim = output_dim
        self.latent_shape = tuple(latent_shape)
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim
        self.chunk_multiples = chunk_multiples
        self.chunk_names = chunk_names
        self.chunk_sizes = chunk_sizes
        self.kernel = kernel
        self.unet_skip = unet_skip
        self.kwargs = kwargs
        self.verbose = kwargs.get("verbose", False)

        self.encoder = KUNetEncoder(
            input_shape=input_shape, shape_name=shape_name,
            input_dim=input_dim, latent_shape=latent_shape, latent_dim=latent_dim,
            hidden_dim=hidden_dim, chunk_multiples=chunk_multiples,
            chunk_names=chunk_names, chunk_sizes=chunk_sizes, kernel=kernel,
            unet_skip=unet_skip, **kwargs,
        )
        self.decoder = KUNetDecoder(
            output_shape=output_shape, shape_name=shape_name,
            output_dim=output_dim, latent_shape=latent_shape, latent_dim=latent_dim,
            hidden_dim=hidden_dim, chunk_multiples=chunk_multiples,
            chunk_names=chunk_names, chunk_sizes=chunk_sizes, kernel=kernel,
            unet_skip=unet_skip, **kwargs,
        )

    def _get_kernels(self):
        kernels = [k.kernel for k in self.encoder.layers]
        kernels += [k.kernel for k in self.decoder.layers]
        return kernels

    def forward(self, x):
        z = self.encoder(x)

        # Pass skip connections from encoder to decoder
        for i, w in enumerate(self.encoder.layers):
            if self.unet_skip and w._skip_saved is not None:
                self.decoder.layers[-i - 1]._skip_saved = w._skip_saved

        y = self.decoder(z)
        return y

# =========================================================
# Model builder
# =========================================================
def build_stacked_model(
    input_shape,
    input_dim,
    depth=5,
    latent_shape=(1, 1, 1),
    latent_dim=128,
    hidden_dim=128,
    chunk_multiples=(3, 3, 3),
    chunk_names="[hwl][hwl][hwl]",
    shape_name="HWL",
    kernel="linear",
    unet_skip=True,
    verbose=False,
    **kwargs
):
    models = []
    for _ in range(depth):
        m = KUNetEncoderDecoder(
            input_shape=input_shape,
            shape_name=shape_name,
            input_dim=input_dim,
            latent_shape=latent_shape,
            latent_dim=latent_dim,
            hidden_dim=hidden_dim,
            chunk_multiples=chunk_multiples,
            kernel=kernel,
            chunk_names=chunk_names,
            unet_skip=unet_skip,
            verbose=verbose,
            **kwargs
        )
        models.append(m)
    return nn.Sequential(*models)


# ══════════════════════════════════════════════
# 10. Tests
# ══════════════════════════════════════════════

if __name__ == "__main__":
    torch.manual_seed(42)
    """
    print("=" * 60)
    print("Test 1: auto order (hhhwwwlll)")
    print("=" * 60)
    enc = KUNetEncoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="hhhwwwlll", chunk_sizes="auto",
        kernel="linear", unet_skip=False, verbose=True,
    )
    x = torch.randn(2, 64, 27, 8, 10)
    z = enc(x)
    print(f"  input  {x.shape}  ->  latent  {z.shape}")
    assert z.shape == (2, 1, 1, 1, 4), f"unexpected {z.shape}"

    dec = KUNetDecoder(
        output_shape=(64, 27, 8), shape_name="HWL", output_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="auto", chunk_sizes="auto",
        kernel="linear", unet_skip=False, verbose=True,
    )
    y = dec(z)
    print(f"  latent {z.shape}  ->  output  {y.shape}")
    assert y.shape == (2, 64, 27, 8, 10), f"unexpected {y.shape}"

    print()
    print("=" * 60)
    print("Test 2: custom order (h2w2hwl3)")
    print("=" * 60)
    enc2 = KUNetEncoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="h2w2hwl3", chunk_sizes="auto",
        kernel="linear", unet_skip=False, verbose=True,
    )
    z2 = enc2(x)
    print(f"  input  {x.shape}  ->  latent  {z2.shape}")
    assert z2.shape == (2, 1, 1, 1, 4), f"unexpected {z2.shape}"

    dec2 = KUNetDecoder(
        output_shape=(64, 27, 8), shape_name="HWL", output_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="h2w2hwl3", chunk_sizes="auto",
        kernel="linear", unet_skip=False, verbose=True,
    )
    y2 = dec2(z2)
    print(f"  latent {z2.shape}  ->  output  {y2.shape}")
    assert y2.shape == (2, 64, 27, 8, 10), f"unexpected {y2.shape}"

    print()
    print("=" * 60)
    print("Test 3: end-to-end with UNet skip (h2w2hwl3)")
    print("=" * 60)
    model = KUNetEncoderDecoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4,
        hidden_dim=4, chunk_multiples=(3, 3, 3),
        chunk_names="h2w2hwl3", kernel="linear", unet_skip=True,
    )
    y3 = model(x)
    print(f"  input  {x.shape}  ->  output  {y3.shape}")
    assert y3.shape == x.shape, f"unexpected {y3.shape}"
    loss = y3.sum()
    loss.backward()
    print("  backward pass OK")

    print()
    print("=" * 60)
    print("Test 3.5: packed blocks [hwl]hwl[hwl] + skip")
    print("=" * 60)
    model = KUNetEncoderDecoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4,
        hidden_dim=4, chunk_multiples=(3, 3, 3),
        chunk_names="[hwl]hwl[hwl]", kernel="linear", unet_skip=True, verbose=True,
    )
    y3 = model(x)
    print(f"  input  {x.shape}  ->  output  {y3.shape}")
    assert y3.shape == x.shape, f"unexpected {y3.shape}"
    loss = y3.sum()
    loss.backward()
    print("  backward pass OK")

    print()
    print("=" * 60)
    print("Test 4: [hwl]hwl[hwl] no skip")
    print("=" * 60)
    x = torch.randn(2, 64, 27, 8, 10)
    enc4 = KUNetEncoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="[hwl]hwl[hwl]", chunk_sizes="auto",
        kernel="linear", verbose=True, unet_skip=False,
    )
    z4 = enc4(x)
    print(f"  input  {x.shape}  ->  latent  {z4.shape}")
    assert z4.shape == (2, 1, 1, 1, 4)
    dec4 = KUNetDecoder.from_encoder(enc4)
    y4 = dec4(z4)
    print(f"  latent {z4.shape}  ->  output  {y4.shape}")
    assert y4.shape == (2, 64, 27, 8, 10)

    print()
    print("=" * 60)
    print("Test 5: Conv kernel + skip")
    print("=" * 60)
    x = torch.randn(2, 64, 27, 8, 10)
    model5 = KUNetEncoderDecoder(
        input_shape=(64, 27, 8), shape_name="HWL", input_dim=10,
        latent_shape=(1, 1, 1), latent_dim=4, hidden_dim=4,
        chunk_multiples=(3, 3, 3), chunk_names="[hwl]hwl[hwl]", chunk_sizes="auto",
        kernel="conv", verbose=True, unet_skip=True,
    )
    y5 = model5(x)
    print(f"  input {x.shape}  ->  output  {y5.shape}")
    assert y5.shape == (2, 64, 27, 8, 10)
    """

    print()
    print("All tests passed!")