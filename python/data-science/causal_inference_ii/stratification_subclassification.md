# stratification subclassification

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x: float) → float`

## What it does

Stratification/Subclassification: divide sample into propensity score strata.

Divide into quintiles (or fewer) on propensity. Within each stratum, treatment is
more balanced. ATE = weighted average of within-stratum estimates.
Core claim: 5 strata remove bulk of planted confounding; exact bias reduction measured.

## Guarantee

When it runs, stratification subclassification guarantees abs(stratified_ate - 2.0) < 0.7; abs(stratified_ate - 2.0) < abs(naive_ate - 2.0) + 0.1; abs(naive_ate - 2.0) > 0.3 (proven by run).

**Checkable constraints:**

- `abs(stratified_ate - 2.0) < 0.7`
- `abs(naive_ate - 2.0) > 0.3`
- `abs(stratified_ate - 2.0) < abs(naive_ate - 2.0) + 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
