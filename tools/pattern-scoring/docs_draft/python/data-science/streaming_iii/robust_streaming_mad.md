# Robust Anomaly Detection via Median/MAD

**File:** `python/data-science/streaming_iii/robust_streaming_mad.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Flag outliers using a robust z-score that isn't corrupted by the outliers themselves.** The median and MAD (median absolute deviation) have a 50% breakdown point — half the data can be arbitrarily bad before the estimate breaks down. The robust z-score |x−med| / (1.4826·MAD) flags points above a threshold k. Unlike mean/std, a few gross outliers don't inflate the threshold and hide themselves.

**When to use:** Online outlier flagging with a low false-positive rate under heavy contamination — sensor fault detection, network anomaly detection, any setting where outliers are common enough to corrupt mean/std.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float] | any numeric values |
| `outlier_idx` | set of int, ground-truth outlier positions | for evaluation only |
| `k` | float > 0, robust z-score threshold | larger = fewer flags |

---

## How inputs shape the output

- **50% breakdown point:** median and MAD resist corruption even when 49% of the data is extreme outliers.
- **Normal consistency constant:** 1.4826 makes MAD consistent for the standard deviation at the normal distribution.
- **k=3.5 gives ~0.05% false-positive rate** on clean normal data (expected ~0.5 FPs per 1000).

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/robust_streaming_mad.py
planted=30  true_positives=30  false_positives=0
Robust MAD PASS
```

**Reading the output:** with 30 gross outliers (~30σ) planted among 1000 N(50,5) points, the robust z-score catches all 30 with zero false positives.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all values identical | MAD = 0, scale clamped | no outliers possible |
| k too small | many false positives | threshold too loose |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20