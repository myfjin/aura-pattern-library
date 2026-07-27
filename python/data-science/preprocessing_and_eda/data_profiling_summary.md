# data profiling summary

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(value: Any) → str`

## What it does

Data Profiling Summary Pattern.

Per-column profile of a mixed dataset (numeric/categorical): type inference,
missing count, cardinality, min/max/mean for numeric, top values for categorical.
Core idea: one-pass summary to understand data structure, missingness, range,
and uniqueness without external libraries.

When to use: exploratory data analysis, data quality checks, understanding
dataset structure before modeling, missing-data patterns, feature planning.

## Guarantee

When it runs, data profiling summary guarantees age_prof['missing_count'] == 2; age_prof['cardinality'] == 8; age_prof['min'] == 25 (proven by run).

**Checkable constraints:**

- `age_prof['type'] == 'numeric'`
- `age_prof['missing_count'] == 2`
- `age_prof['cardinality'] == 8`
- `'min' in age_prof and 'max' in age_prof and ('mean' in age_prof)`
- `age_prof['min'] == 25`
- `age_prof['max'] == 42`
- `city_prof['type'] == 'categorical'`
- `city_prof['missing_count'] == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
