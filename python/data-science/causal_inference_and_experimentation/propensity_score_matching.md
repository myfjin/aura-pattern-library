# propensity score matching

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(x: float) → float`

## What it does

Propensity Score Matching (PSM).

Observational data is confounded: treatment assignment depends on observed traits.
We estimate the propensity score P(treatment | confounders), then match treated and
control units on their propensity score, creating pseudo-random assignment within strata.
Naive OLS on the raw data will miss the true causal effect (or estimate it wrong).
PSM recovers the true effect by eliminating the confounder's association with treatment.

## Guarantee

When it runs, propensity score matching guarantees bias_matched < bias_naive (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bias_matched < bias_naive`
- `len(matched_t) > 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
