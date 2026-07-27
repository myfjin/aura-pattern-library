# switchback experiment lite

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(n_users: int, true_effect: float, spillover: float) → float`

## What it does

Switchback experiment: time-block randomization for marketplace interference.

Under interference (treating some users spills over to controls), a user-split A/B is
BIASED: the control arm is partially "treated" through the marketplace, so the measured
treatment−control gap shrinks toward zero. A switchback flips the WHOLE market between
all-treatment and all-control time blocks, so within a block there is no cross-
contamination and the effect is recovered.
Core claim: user-split A/B is biased toward zero; switchback recovers the true effect.

## Guarantee

When it runs, switchback experiment lite guarantees ab < true_effect; abs(sb - true_effect) < 0.3; abs(sb - true_effect) < abs(ab - true_effect) (proven by run).

**Checkable constraints:**

- `abs(ab - true_effect) > 0.3`
- `ab < true_effect`
- `abs(sb - true_effect) < 0.3`
- `abs(sb - true_effect) < abs(ab - true_effect)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
