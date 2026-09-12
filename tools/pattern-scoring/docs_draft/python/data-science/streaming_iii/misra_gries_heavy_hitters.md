# Misra-Gries Heavy Hitters

**File:** `python/data-science/streaming_iii/misra_gries_heavy_hitters.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Find all items that appear more than n/k times in a stream, using only k−1 counters.** Misra-Gries keeps at most k−1 counters. On each new item: increment its counter if it exists, open a new counter if there's room, otherwise decrement ALL counters (dropping any that hit zero). Every item with true frequency > n/k survives (zero false negatives), and each surviving counter undercounts its true frequency by at most n/k.

**When to use:** You need to find heavy hitters in one pass with O(k) space — the simplest and most elegant heavy-hitter algorithm.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | list (any hashable type) | duplicates are fine |
| `k` | int > 1, controls threshold n/k | larger = more counters, lower threshold |

---

## How inputs shape the output

- **Zero false negatives:** every item with true frequency > n/k is guaranteed to survive.
- **Count guarantee:** for every surviving counter, true − n/k ≤ counter ≤ true.
- **O(k) space:** at most k−1 counters at any time, regardless of stream length.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/misra_gries_heavy_hitters.py
Heavy hitters (>n/5): ['A']  true=['A']
Misra-Gries PASS
```

**Reading the output:** with A as the dominant hitter in a stream of 800 items and k=5 (threshold n/5 = 160), Misra-Gries correctly identifies A as the only heavy hitter.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| k ≤ 1 | AssertionError | need at least 2 for a threshold |
| all items equally frequent | may report none | correct — none exceeds n/k |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20