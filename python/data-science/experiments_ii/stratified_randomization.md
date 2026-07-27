# stratified randomization

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(x: List[float], seed: int) → List[int]`

## What it does

Stratified randomization: randomize treatment within strata of a covariate.

Better covariate balance + lower estimator variance vs simple randomization.
Core claim: over seeded replications, stratified shows better balance and lower variance.

## Guarantee

When it runs, stratified randomization guarantees avg_balance_strat < avg_balance_simple + 0.01; avg_var_strat < avg_var_simple * 1.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `avg_balance_strat < avg_balance_simple + 0.01`
- `avg_var_strat < avg_var_simple * 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
