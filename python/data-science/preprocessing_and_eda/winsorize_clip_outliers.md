# winsorize clip outliers

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(data: List[float], p: float) → float`

## What it does

Winsorization and Clipping Pattern.

Caps extreme values at percentile thresholds (winsorization) or hard bounds
(clipping). Core idea: reduce influence of outliers while preserving sample
count and general structure; interior values untouched.

When to use: outlier mitigation before analysis, handling measurement errors,
reducing leverage of extreme observations, robust preprocessing.

## Guarantee

When it runs, winsorize clip outliers guarantees min(clipped) == 10; max(clipped) == 90; len(winsorized) == n_original (proven by run).

**Checkable constraints:**

- `len(winsorized) == n_original`
- `len(winsorized) == n_original`
- `min(winsorized) <= val <= max(winsorized)`
- `winsorized_range < original_range * 0.7`
- `all((10 <= x <= 90 for x in clipped))`
- `len(clipped) == n_original`
- `min(clipped) == 10`
- `max(clipped) == 90`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
