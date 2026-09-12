# Concept-Drift Ensemble vs. Frozen Single Learner

**File:** `python/data-science/streaming_iii/concept_drift_ensemble.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Show that a drift-aware ensemble adapts to a changing concept while a frozen single learner gets stuck on the old one.** On a stream whose label distribution flips at the midpoint, the ensemble spawns a fresh learner per window and weights each by its recent accuracy. The frozen learner predicts the pre-drift majority forever.

**When to use:** You need to demonstrate why adaptive models matter in streaming classification — the demo measures the ensemble beating the frozen model on post-drift data by a provable margin.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `y` | List[int] (0/1 labels) | binary only |
| `window` | int > 0, window size | larger = smoother but slower to adapt |

---

## How inputs shape the output

- **The gap is the signal:** the ensemble's post-drift accuracy minus the frozen learner's is the measure that matters — not either number alone.
- **Window size controls adaptation speed:** smaller windows = faster to detect the flip but noisier. The demo's window=50 on a 4000-sample stream gives clean separation.
- **Weighting by recent accuracy:** each learner's vote is weighted by its accuracy on the most recent window, so stale learners fade out naturally.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/concept_drift_ensemble.py
post-drift: ensemble=0.847  frozen-single=0.153
Concept-drift ensemble PASS
```

**Reading the output:** after the concept flips from P(y=1)=0.15 to P(y=1)=0.85, the ensemble recovers to ~85% accuracy while the frozen learner, stuck predicting the old majority (0), collapses to ~15%. The gap of ~0.69 proves adaptation.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| no concept drift | both learners perform similarly | ensemble doesn't hurt on stationary data |
| very small window | ensemble may not beat frozen | not enough data per learner |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20