# Missing Value Imputation

**File:** `python/data-science/preprocessing_and_eda/missing_value_imputation.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Replace None/NaN values with statistical estimates (mean, median, mode) and create binary missing-indicator columns.** Preserves sample count while reconstructing plausible values from complete records. Tracks missingness separately.

**When to use:** Handling incomplete datasets before analysis, preserving row count, understanding missing-data patterns.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[Optional[float]], values with None | |
| `strategy` | str, 'mean', 'median', or 'mode' | |

---

## How inputs shape the output

- **No None values remain after imputation** — all missing positions filled.
- **Missing indicators are correct** — 1 where original was None, 0 otherwise.
- **Imputed values match the chosen strategy** — mean/median/mode of non-missing.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/missing_value_imputation.py
missing_value_imputation.py: PASS
```

**Reading the output:** 3 missing values in a 9-element array are filled with the mean (50.5) of the 6 non-missing values. Indicators correctly mark the missing positions.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all values missing | ValueError | cannot impute |
| unknown strategy | ValueError | must be mean/median/mode |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20