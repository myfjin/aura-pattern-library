# mnar missingness bias

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Missing Not At Random (MNAR): bias in naive complete-case analysis.

Generates data with MNAR missingness (missing indicator depends on the value itself),
compares complete-case mean to true mean, and contrasts with MCAR which introduces
no bias. MNAR produces systematic bias.

## Guarantee

When it runs, mnar missingness bias guarantees mnar_mean < true_mean; mnar_bias > 5; mcar_bias < mnar_bias (proven by run).

**Checkable constraints:**

- `mnar_mean < true_mean`
- `mnar_bias > 5`
- `mcar_bias < mnar_bias`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
