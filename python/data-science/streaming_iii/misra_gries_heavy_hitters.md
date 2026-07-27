# misra gries heavy hitters

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: list, k: int) → Dict`

## What it does

Misra-Gries heavy hitters (k-1 counters).
Core idea: keep at most k-1 counters; on a new item increment its counter, else open one
if room, else decrement ALL counters (dropping any that hit zero). Every item with true
frequency > n/k survives (zero false negatives), and each surviving counter undercounts
its true frequency by at most n/k.
When: find heavy hitters in one pass in O(k) space.

## Guarantee

When it runs, misra gries heavy hitters guarantees not false_neg; truth[it] - threshold <= c <= truth[it] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not false_neg`
- `truth[it] - threshold <= c <= truth[it]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
