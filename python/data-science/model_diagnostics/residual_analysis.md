# residual analysis

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(n: int, seed: int) → List[Tuple[float, float]]`

## What it does

Residual Analysis

Fits a linear model to data with a planted quadratic term.
Inspects residuals for structure (correlation with x^2 or runs test).

Use this to detect model misspecification: if residuals correlate with the omitted feature,
you've found a missing term in your specification.

## Guarantee

When it runs, residual analysis guarantees len(u) == len(v); abs(corr_lin) > 0.5; abs(corr_quad) < abs(corr_lin) * 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(u) == len(v)`
- `abs(corr_lin) > 0.5`
- `abs(corr_quad) < abs(corr_lin) * 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `residual_analysis_test()` — no return, prints PASS.
**Valid input:** Uses internal `generate_quadratic_data(100, seed=42)`.
**Core:** Fit linear model to quadratic data (y = 1 + 0.5x + 0.3x² + N(0,0.3)). Compute residuals and check correlation with omitted x² term. Then fit quadratic model and verify residuals no longer show structure. Demonstrates residual analysis for detecting model misspecification.
**Assert:** On 100 samples: linear residuals correlate with x² (|corr| > 0.5). Quadratic residuals have correlation with x² reduced to < 30% of linear correlation.
**⚠️ Defect:** The test asserts `abs(corr_quad) < abs(corr_lin) * 0.3`, which is a relative threshold. If the linear correlation is very high (e.g., 0.99), the quadratic residual correlation must be < 0.3, which is reasonable. But if the linear correlation is barely above 0.5, the quadratic residual correlation must be < 0.15, which may fail if the quadratic fit is imperfect due to noise.

---
*△ AURA Pattern Library — © Reality Optimizer*
