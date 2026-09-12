# Welford Decayed Streaming Moments

**File:** `python/data-science/streaming_iii/welford_decayed_moments.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Track mean and variance on a non-stationary stream where recent samples matter more than old ones.** Uses a decay-weighted running mean and M2 (Welford-style) so that recent samples dominate. On a stream whose level shifts, the decayed mean tracks the recent level while the plain global mean lags halfway between old and new.

**When to use:** You need to track mean/variance on streams with concept drift or regime changes — sensor monitoring, financial volatility tracking, any "what's happening now?" on a changing process.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | list of numeric values | any scale |
| `decay` | float in (0, 1), decay factor | 0.95 = ~20 samples half-life |

---

## How inputs shape the output

- **Decay-weighted:** a sample t steps in the past has weight decay^t. decay=0.95 gives a half-life of ~14 steps.
- **Tracks regime changes:** on a stream that shifts from N(0,1) to N(10,1), the decayed mean recovers the new level (~10) while the global mean lags at ~5.
- **Variance reflects recent spread:** the decayed variance tracks the current regime's variance (~1), not the pooled cross-regime spread (~25).

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/welford_decayed_moments.py
decayed_mean=9.876  global_mean=5.012  recent=10.012
Welford decayed moments PASS
```

**Reading the output:** after a shift from N(0,1) to N(10,1) at the midpoint, the decayed mean (9.88) tracks the recent level (~10) while the global mean (5.01) sits halfway between regimes.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| decay = 0 | only the last sample matters | extreme case |
| decay → 1 | approaches global mean | no decay |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20