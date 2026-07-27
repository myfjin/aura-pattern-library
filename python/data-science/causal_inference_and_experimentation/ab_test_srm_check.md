# ab test srm check

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(observed: list, expected: list) → Tuple[float, float]`

## What it does

Sample Ratio Mismatch (SRM) Check for A/B Tests.

In a valid A/B test, the allocation ratio should match the design (e.g., 50/50).
A chi-square test on the observed counts detects when sample ratio deviates significantly.
SRM flags data quality issues (e.g., bugs, bot filtering).
We plant an SRM (skewed split) and a clean split; SRM caught vs clean passes.

## Guarantee

When it runs, ab test srm check guarantees p_clean > 0.05; p_skewed < 0.05; chi_sq_clean < 3.84 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `p_clean > 0.05`
- `p_skewed < 0.05`
- `chi_sq_clean < 3.84`
- `chi_sq_skewed > 3.84`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
