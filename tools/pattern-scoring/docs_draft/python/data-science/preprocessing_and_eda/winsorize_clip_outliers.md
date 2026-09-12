# Winsorization and Clipping

**File:** `python/data-science/preprocessing_and_eda/winsorize_clip_outliers.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Cap extreme values at percentile thresholds (winsorization) or hard bounds (clipping).** Reduces influence of outliers while preserving sample count and general structure. Interior values untouched.

**When to use:** Outlier mitigation before analysis, handling measurement errors, reducing leverage of extreme observations.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], numeric values | |
| `limits` | tuple, (lower_pct, upper_pct) as fraction | |
| `min_val`, `max_val` | float, hard bounds for clipping | |

---

## How inputs shape the output

- **Count unchanged** — no samples removed.
- **Extreme values are capped** — within winsorized bounds.
- **Range is much tighter after winsorization** — < 70% of original range.
- **Clipping enforces hard bounds** — all values in [min, max].

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/winsorize_clip_outliers.py
winsorize_clip_outliers.py: PASS
```

**Reading the output:** data with 4 extreme outliers (2, 200, -50, 250) is winsorized at 5th/95th percentiles. Range drops from ~300 to < 70% of that. Clipping to [10, 90] enforces hard bounds.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all identical values | winsorization is a no-op | correct |
| limits sum > 1 | may invert bounds | needs valid limits |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20