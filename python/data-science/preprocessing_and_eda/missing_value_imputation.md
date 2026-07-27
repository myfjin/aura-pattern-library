# missing value imputation

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

## What it does

Missing Value Imputation Pattern.

Replaces None/NaN values with statistical estimates (mean, median, mode) or
creates binary missing-indicator columns. Core idea: preserve sample count while
reconstructing plausible values from complete records; track missingness separately.

When to use: handling incomplete datasets before analysis, preserving row count,
understanding missing-data patterns, tree-based models that benefit from missingness signals.

## Guarantee

When it runs, missing value imputation guarantees abs(imputer_mean.fill_values['value'] - expected_mean) < 1e-06; imputed[i] == expected_mean; imputed_med[i] == expected_median (proven by run).

**Checkable constraints:**

- `len(imputed) == len(data_with_missing)`
- `len(indicators) == len(data_with_missing)`
- `all((x is not None for x in imputed))`
- `indicators == [0, 1, 0, 0, 1, 0, 0, 1, 0]`
- `abs(imputer_mean.fill_values['value'] - expected_mean) < 1e-06`
- `imputed[i] == expected_mean`
- `imputed_med[i] == expected_median`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
