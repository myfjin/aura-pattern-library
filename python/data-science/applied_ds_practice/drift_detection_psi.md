# drift detection psi

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(ref_values: list[float], n_bins: int) → list[float]`

## What it does

Population Stability Index (PSI) and KS-statistic for feature drift detection.

PSI measures how a feature's distribution shifts between a reference period
(e.g., training data) and a current window (e.g., production data).
KS-statistic tests whether two distributions are significantly different.
Both detect dataset shift / concept drift.

Use: production monitoring, model retraining triggers, data quality checks.

## Guarantee

When it runs, drift detection psi guarantees psi_no_drift < 0.25; ks_no_drift < 0.1; ks_drift > 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `psi_no_drift < 0.25`
- `ks_no_drift < 0.1`
- `ks_drift > 0.1`
- `psi_drift > 0.25`
- `psi_drift > psi_no_drift`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def reference_bin_edges(ref_values: list[float], n_bins: int = 10) -> list[float]:`, `def bin_with_edges(values: list[float], edges: list[float]) -> list[int]:`, `def population_stability_index(ref_bins: list[int], curr_bins: list[int], n_bins: int = 10) -> float:`, `def kolmogorov_smirnov_statistic(ref_vals: list[float], curr_vals: list[float]) -> float:`
**Valid input:** `ref_values` and `curr_values` non-empty numeric lists; `n_bins >= 2`.
**Core:** Population Stability Index (PSI) and Kolmogorov-Smirnov statistic for distribution drift. Bins the reference window on its own quantile edges, then bins the current window on those same edges to avoid hiding drift. PSI uses Laplace-smoothed bin proportions; KS uses the maximum absolute CDF difference.
**Assert:** On 500 reference + 500 current samples from the same N(100, 15): PSI < 0.25 and KS < 0.1. On a shifted N(145, 25) current window: KS > 0.1 and PSI > 0.25, with drift PSI exceeding no-drift PSI.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
