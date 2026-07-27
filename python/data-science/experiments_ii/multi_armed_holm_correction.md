# multi armed holm correction

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(alpha: float, num_tests: int) → float`

## What it does

Holm correction (step-down Bonferroni) for multiple comparisons.

Many variants of a treatment tested; uncorrected testing breaks FWER over replications.
Holm correction controls FWER; trades power for false-positive control.
Core claim: uncorrected breaks FWER; Holm holds it.

## Guarantee

When it runs, multi armed holm correction guarantees fwer_unc_rate > fwer_bonf_rate; fwer_unc_rate > fwer_holm_rate; fwer_bonf_rate < 0.2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `fwer_unc_rate > fwer_bonf_rate`
- `fwer_unc_rate > fwer_holm_rate`
- `fwer_bonf_rate < 0.2`
- `fwer_holm_rate < 0.2`
- `fwer_holm_rate >= fwer_bonf_rate - 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
