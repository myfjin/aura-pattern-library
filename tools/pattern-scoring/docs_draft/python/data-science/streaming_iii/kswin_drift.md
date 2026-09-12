# KSWIN — Kolmogorov-Smirnov Windowing Drift Detector

**File:** `python/data-science/streaming_iii/kswin_drift.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Detect distribution shift in a data stream using the Kolmogorov-Smirnov two-sample test.** KSWIN maintains two windows from the stream and applies the KS test to check whether they come from the same distribution. The KS statistic measures the maximum absolute difference between the empirical CDFs; if it exceeds a critical value derived from the significance level α, drift is declared.

**When to use:** You need a non-parametric drift detector that makes no assumptions about the underlying distribution — works for any continuous-valued stream.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float] | continuous values |
| `window_size` | int > 0, size of each window | larger = more reliable, slower to react |
| `alpha` | float in (0, 1), significance level | smaller = fewer false positives |

---

## How inputs shape the output

- **Non-parametric:** the KS test makes no distributional assumptions — it works for Gaussian, uniform, exponential, or any other continuous distribution.
- **Critical value from Kolmogorov distribution:** √(−½·ln(α/2) / n) — an approximation that's accurate for moderate window sizes.
- **Two-window design:** compares the first `window_size` samples against the last `window_size` samples. A shift between them triggers detection.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/kswin_drift.py
KSWIN on stationary: False (should be False)
KSWIN on shifted: True (should be True)
```

**Reading the output:** on a stationary N(50, 5) stream, KSWIN correctly reports no drift. On a stream that shifts from N(50, 5) to N(65, 5) at the midpoint, KSWIN detects the shift.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| stream shorter than 2× window | returns False | not enough data for two windows |
| very small shift (< 1σ) | may not detect | KS test needs a real difference |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20