# cox partial likelihood lite

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(times: List[float], events: List[int], x1: List[float], x2: List[float], max_iter: int, tol: float) → Tuple[float, float]`

## What it does

Cox partial likelihood: semiparametric survival model for 2-covariate hazard.

Estimates hazard ratios via Newton-Raphson on partial likelihood. Core claim:
planted hazard ratios recovered from censored data; Newton steps converge.
Planted survival times with true HR, censoring, and covariate structure.

## Guarantee

When it runs, cox partial likelihood lite guarantees abs(beta1 - 0.5) < 0.5; abs(beta2 - -0.3) < 0.5 (proven by run).

**Checkable constraints:**

- `abs(beta1 - 0.5) < 0.5`
- `abs(beta2 - -0.3) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def cox_partial_likelihood_2cov(times: List[float], events: List[int], x1: List[float], x2: List[float], max_iter: int = 20, tol: float = 1e-6) -> Tuple[float, float]:`
**Valid input:** All input lists are equal-length; `events[i]` ∈ {0,1}; `max_iter` > 0; `tol` > 0.
**Core:** Fits a Cox proportional hazards model with two covariates by Newton-Raphson on the partial likelihood. Returns estimated log hazard ratios `β1` and `β2` where `h(t|x) = h₀(t)·exp(β1·x1 + β2·x2)`.
**Assert:** On planted data with true `β1 = 0.5`, `β2 = -0.3`, the estimates are within ±0.5 of the true values.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
