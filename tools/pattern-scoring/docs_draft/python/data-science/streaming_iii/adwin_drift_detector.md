# ADWIN0 Adaptive Windowing Drift Detector

**File:** `python/data-science/streaming_iii/adwin_drift_detector.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Detect when a data stream's distribution has genuinely changed, with a provable false-alarm guarantee.** ADWIN (Bifet & Gavalda, 2007) keeps a window of recent values. After each new value arrives, it tries every split of the window into an older part W₀ and newer part W₁. If |mean(W₀) − mean(W₁)| exceeds a variance-aware Hoeffding bound, a real change is declared and the older part is dropped.

**When to use:** You need to detect distribution shift online — classifier error rate monitoring, sensor drift detection, any stream where you need to know "did the process change?" with a statistical guarantee.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float], values in [0,1] | out-of-range values break the bound |
| `delta` | float in (0, 1), false-positive target | delta ≤ 0 or ≥ 1 breaks the math |

---

## How inputs shape the output

- **delta controls false alarms:** delta=0.05 means ≤5% chance of false drift on a stationary stream. Smaller delta = harder to trigger, fewer false positives, slower detection.
- **Window adapts automatically:** no fixed window size — the algorithm grows and shrinks the window based on what the data says.
- **Stride sampling for efficiency:** checks every `max(1, n//32)`-th split rather than every single one, which is faithful for any real shift.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/adwin_drift_detector.py
stationary: detected=False at -1 (want False)
shift: detected=True at 324 (want True, soon after 300)
ADWIN PASS
```

**Reading the output:** on a stationary Bernoulli(0.2) stream, ADWIN correctly reports no drift. On a stream where the error rate jumps from 0.2 → 0.6 at index 300, ADWIN flags the drift at index 324 — within one window of the change point.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all-identical values | no drift ever detected | correct — no change to detect |
| very small delta (< 0.001) | may never fire | too strict for short streams |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20