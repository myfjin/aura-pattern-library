# lossy counting frequent

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: list, support: float, eps: float) → Tuple[Set, Dict]`

## What it does

Lossy Counting for frequent items (Manku & Motwani, 2002).
Core idea: divide the stream into buckets of width w = ceil(1/eps). Store each item as
(freq, delta) where delta is the max possible undercount at insertion (current_bucket-1).
At every bucket boundary, delete any item whose freq+delta <= current_bucket. Output items
with freq >= (s-eps)*N. This guarantees ZERO false negatives for true frequency >= s*N,
and no reported item has true frequency < (s-eps)*N.
When: find frequent items in one pass with a provable error/space tradeoff (eps < s).

## Guarantee

When it runs, lossy counting frequent guarantees not false_neg; true_c - eps * N <= freqs[it] <= true_c; truth[it] >= (support - eps) * N (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not false_neg`
- `true_c - eps * N <= freqs[it] <= true_c`
- `truth[it] >= (support - eps) * N`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
