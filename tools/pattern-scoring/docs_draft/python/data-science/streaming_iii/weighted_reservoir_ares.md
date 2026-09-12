# Weighted Reservoir Sampling — A-Res

**File:** `python/data-science/streaming_iii/weighted_reservoir_ares.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Sample k items proportional to their weight in one pass over a weighted stream.** The Efraimidis-Spirakis A-Res algorithm gives each item a key u^(1/weight) with u ~ Uniform(0,1) and keeps the k items with the largest keys in a min-heap. The resulting sample is a weighted sample without replacement: P(item in sample) grows with its weight.

**When to use:** You need a weighted random sample from a stream where items have different importance — survey sampling with unequal probabilities, weighted A/B test monitoring, any "sample proportional to importance" problem.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[Tuple[value, weight]] | weight > 0 |
| `k` | int > 0, sample size | larger = more representative |

---

## How inputs shape the output

- **Weighted inclusion probability:** for k=1, P(item i is picked) = w_i / sum(w). The demo verifies this empirically over 40,000 trials.
- **Monotone in weight:** heavier items are picked strictly more often than lighter ones.
- **One pass, O(k) memory:** uses a min-heap of size k.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/weighted_reservoir_ares.py
empirical p=['0.067', '0.133', '0.200', '0.267', '0.333']  exact=['0.067', '0.133', '0.200', '0.267', '0.333']
max deviation = 0.0023
Weighted reservoir (A-Res) PASS
```

**Reading the output:** with weights [1, 2, 3, 4, 5] (total 15), the empirical inclusion probabilities match the exact w_i/15 within 0.0023 — the weighted law holds.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| weight ≤ 0 | item skipped | correct — zero/negative weight items excluded |
| k > stream length | returns all items | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20