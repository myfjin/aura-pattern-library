# birthday paradox exact vs sim

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(n: int, days: int) → float`

## What it does

Birthday paradox: analytical vs simulated collision probability.

P(≥2 same birthday in n people) ≈ 1 - n!/((365)^n · (365-n)!). Planted n values;
analytic and simulated agree.

## Guarantee

When it runs, birthday paradox exact vs sim guarantees 0.4 < p_exact < 0.6; abs(p_sim - p_exact) < 0.1 (proven by run).

**Checkable constraints:**

- `0.4 < p_exact < 0.6`
- `abs(p_sim - p_exact) < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
