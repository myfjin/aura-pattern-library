# novelty effect decay

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(n_users: int, true_long_run_effect: float, novelty_boost: float, decay_rate: float) → List[List[float]]`

## What it does

Novelty effect: early treatment boost that fades over time.

First measurement of a treatment shows inflated effect; long-run effect is lower.
Core claim: day-1 estimate overstates long-run effect; time-sliced estimates reveal decay.

## Guarantee

When it runs, novelty effect decay guarantees abs(ate_day10 - true_long_run_effect) < 0.8; ate_day1 > ate_day10 + 1.0 (proven by run).

**Checkable constraints:**

- `ate_day1 > ate_day10 + 1.0`
- `abs(ate_day10 - true_long_run_effect) < 0.8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
