# bayesian changepoint offline

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(data: List[float]) → int`

## What it does

Bayesian changepoint detection: find the point where mean shifts.

Core claim: detected changepoint ≈ true location within tolerance.

## Guarantee

When it runs, bayesian changepoint offline guarantees abs(detected - changepoint_true) < 5 (proven by run).

**Checkable constraints:**

- `abs(detected - changepoint_true) < 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
