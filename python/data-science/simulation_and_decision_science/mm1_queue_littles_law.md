# mm1 queue littles law

**Language:** Python · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

M/M/1 Queue: verify Little's Law and analytic formulas.

Simulates an M/M/1 queue (Poisson arrivals, exponential service).
Verifies Little's Law: L ≈ λW. Also compares to analytic M/M/1 formulas.

## Guarantee

When it runs, mm1 queue littles law guarantees littles_law_check < 0.3; 0.5 * expected_w < W < 2.0 * expected_w; 0.5 * expected_l < L < 2.0 * expected_l (weak-grade: directional, proven by run).

**Checkable constraints:**

- `littles_law_check < 0.3`
- `0.5 * expected_w < W < 2.0 * expected_w`
- `0.5 * expected_l < L < 2.0 * expected_l`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def mm1_queue_littles_law() -> None:`
**Valid input:** None (self-contained with hardcoded rates).
**Core:** Simulates an M/M/1 queue for 1,000 arrivals, measuring average time in system `L` and average number in system `W`. Verifies Little's Law (`L = λ·W`) and compares empirical results to analytic M/M/1 formulas.
**Assert:** With `λ = 0.8`, `μ = 1.0`, empirical `W` and `L` are within 0.5×–2.0× of analytic values (`E[W] = 1/(μ−λ)`, `E[L] = ρ/(1−ρ)`), and Little's Law holds within 30%.
**⚠️ Defect:** The code labels `L` as "average time in system" and `W` as "average number in system", which is the opposite of the standard Little's Law convention (`L` = average number in system, `W` = average time in system). This is a documentation/naming bug that could confuse readers. Also, the simulation uses the time of the last arrival as the denominator, not total elapsed time, biasing utilization estimates.

---
*△ AURA Pattern Library — © Reality Optimizer*
