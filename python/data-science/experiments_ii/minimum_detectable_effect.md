# minimum detectable effect

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(n_per_arm: int, alpha: float, power: float, sigma: float) → float`

## What it does

Minimum Detectable Effect (MDE): smallest effect size detectable with given n, α, power.

Computed from normal approximation. Verified by simulation at multiple points.
Core claim: MDE formula matches simulated power curve.

## Guarantee

When it runs, minimum detectable effect guarantees 0.65 < power_at_mde < 0.95; power_at_1_5x > power_at_mde; power_at_0_7x < power_at_mde (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.65 < power_at_mde < 0.95`
- `power_at_1_5x > power_at_mde`
- `power_at_0_7x < power_at_mde`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
