# Greenwald-Khanna ε-Approximate Quantile Summary

**File:** `python/data-science/streaming_iii/gk_quantile_summary.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Estimate any quantile of a stream with bounded error using far less memory than storing all values.** The GK algorithm maintains a sorted list of (value, g, delta) tuples where g is a lower bound on rank and delta is the maximum error. When the summary grows too large, it compresses by selectively dropping entries while preserving the ε-error guarantee.

**When to use:** You need approximate quantiles (median, quartiles, percentiles) on a large stream where storing all values is impractical — latency monitoring, sensor data, any "what's the 95th percentile?" on a firehose.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float] | any numeric values |
| `epsilon` | float in (0, 1), error tolerance | smaller = more memory |
| `q` | float in [0, 1], target quantile | 0.5 = median |

---

## How inputs shape the output

- **Error bound:** the estimated quantile is within 2·ε·n of the true quantile (in rank space). The demo's ε=0.01 on n=1000 gives error bound of 20 positions.
- **Compression keeps the guarantee:** when the summary exceeds 2k entries (k = 1/(2ε)), every other entry is dropped — the error bound is preserved.
- **Any quantile from one pass:** once built, the summary can answer any q without re-scanning the stream.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/gk_quantile_summary.py
GK median (ε=0.01): 49.9876
```

**Reading the output:** on 1000 samples from N(50, 10), the GK summary estimates the median at ~49.99 — within the ε error bound of the true median.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty stream | IndexError | needs guard |
| epsilon too small | summary grows large | memory-accuracy tradeoff |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20