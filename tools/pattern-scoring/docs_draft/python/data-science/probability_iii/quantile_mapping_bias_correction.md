# Quantile Mapping Bias Correction

**File:** `python/data-science/probability_iii/quantile_mapping_bias_correction.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Correct distributional bias by matching quantiles.** Maps a biased distribution onto a reference distribution via quantile alignment. For each point in the biased data, find its quantile, then map to the reference value at the same quantile. Post-correction quantiles match the reference.

**When to use:** Bias correction in climate models, sensor calibration, any setting where a systematic shift needs to be removed while preserving the distribution shape.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data_biased` | List[float], biased observations | |
| `data_reference` | List[float], reference (true) distribution | |

---

## How inputs shape the output

- **Corrected median matches reference median** within 1.0 unit.
- **Full distribution is aligned** — not just the mean.
- **Non-parametric** — no distributional assumptions.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/quantile_mapping_bias_correction.py
PASS
```

**Reading the output:** biased data (N(5,1)) is corrected to match reference (N(0,1)). The corrected median is within 1.0 of the reference median.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| reference too small | quantile mapping is coarse | needs enough reference data |
| biased data outside reference range | extrapolation | may clip extreme values |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20