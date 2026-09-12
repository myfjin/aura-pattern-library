# Lossy Counting for Frequent Items

**File:** `python/data-science/streaming_iii/lossy_counting_frequent.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Find all items that appear more than s·N times in a stream, in one pass, with bounded memory.** Lossy Counting (Manku & Motwani, 2002) divides the stream into buckets of width w = ceil(1/ε). Each item is stored as (freq, delta) where delta is the maximum possible undercount at insertion. At every bucket boundary, items with freq+delta ≤ current_bucket are pruned. Output items with freq ≥ (s−ε)·N. Zero false negatives for true frequency ≥ s·N, and no reported item has true frequency < (s−ε)·N.

**When to use:** You need to find frequent items in one pass with a provable error/space tradeoff — network traffic analysis, trending topics, any "what's popular?" on a stream.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | list (any hashable type) | duplicates are fine |
| `support` | float in (0, 1), frequency threshold s | larger = fewer items reported |
| `eps` | float in (0, support), error parameter | must be < support |

---

## How inputs shape the output

- **Zero false negatives:** every item with true frequency ≥ s·N is guaranteed to be reported.
- **Bounded false positives:** no reported item has true frequency < (s−ε)·N.
- **Count guarantee:** reported frequencies undercount the true count by at most ε·N (never overcount).

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/lossy_counting_frequent.py
Lossy Counting: frequent=['A', 'B'], true=['A', 'B']
Lossy Counting PASS
```

**Reading the output:** with A at ~30% and B at ~20% in a 10,000-item stream, Lossy Counting with support=0.10 correctly identifies both as frequent. Zero false negatives, zero false positives.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| eps ≥ support | AssertionError | error must be smaller than threshold |
| empty stream | empty result | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20