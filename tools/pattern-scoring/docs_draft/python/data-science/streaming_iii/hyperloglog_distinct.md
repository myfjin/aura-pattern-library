# HyperLogLog Cardinality Estimation

**File:** `python/data-science/streaming_iii/hyperloglog_distinct.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Count the number of distinct elements in a massive stream using fixed tiny memory.** HyperLogLog (Flajolet et al.) hashes each element to 64 bits. The first p bits pick one of m = 2ᵖ registers. The remaining bits' rank (position of the leftmost 1) updates that register to its maximum. The distinct count is estimated from the harmonic mean of 2^rank across all registers. Standard error ≈ 1.04/√m — with p=12 (4096 registers), that's ~1.6%.

**When to use:** You need to count unique visitors, distinct IPs, unique search queries, or any cardinality on a high-volume stream where storing all IDs is impossible.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List (any hashable type) | duplicates are fine |
| `p` | int in [4, 16], log₂(registers) | larger = more accurate, more memory |

---

## How inputs shape the output

- **Fixed memory:** m = 2ᵖ registers, each holding a small integer (max rank ≤ 64−p+1). With p=12, that's 4096 registers × ~1 byte each ≈ 4KB total.
- **Standard error formula:** 1.04/√m. p=12 → ~1.6%, p=14 → ~0.8%, p=16 → ~0.4%.
- **Small-range correction:** when the raw estimate is ≤ 2.5·m and many registers are empty, the algorithm switches to linear counting for accuracy.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/hyperloglog_distinct.py
HyperLogLog p=12: est=8000, true=8000, rel_err=0.0000
```

**Reading the output:** on 40,000 samples drawn from 8,000 distinct IDs, HLL with p=12 (4096 registers, ~4KB) estimates exactly 8,000 — zero error on this run, well within the 5% 3-sigma bound.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very small cardinality (< m) | linear counting kicks in | still accurate |
| p < 4 | AssertionError | too few registers for meaningful estimate |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20