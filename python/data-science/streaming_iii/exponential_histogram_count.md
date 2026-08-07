# exponential histogram count

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[int], window: int, eps: float) → int`

## What it does

Exponential histogram / DGIM count of 1s in a sliding window (Datar-Gionis-Indyk-Motwani).
Core idea: to count the 1-bits among the last N arrivals in O((1/eps) log N) space, keep
buckets each holding a power-of-2 count and the timestamp of its most recent 1. Allow at
most k/2+1 buckets of each size (k = ceil(1/eps)); when exceeded, merge the two oldest of
that size into one double-size bucket. Expire buckets that fall out of the window. Estimate
= (sum of bucket sizes) - (half the oldest in-window bucket). Relative error <= 1/k = eps.
When: count events in a sliding window under strict memory with a provable error bound.

## Guarantee

When it runs, exponential histogram count guarantees rel <= eps + 1e-09; _bucket_count(stream, N, eps) < N // 10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rel <= eps + 1e-09`
- `_bucket_count(stream, N, eps) < N // 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
