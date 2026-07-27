# reliability series parallel

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(component_reliabilities: List[float]) → float`

## What it does

System reliability: series vs parallel from component reliabilities.

Series: all components must work → R_sys = R1 · R2 · ... · Rn.
Parallel: at least one must work → R_sys = 1 - (1-R1)·(1-R2)·...·(1-Rn).
Core claim: system reliability computed correctly; verified vs simulation.

## Guarantee

When it runs, reliability series parallel guarantees abs(r_series_analytic - r_series_sim) < 0.05; abs(r_parallel_analytic - r_parallel_sim) < 0.05; r_series_analytic < r_parallel_analytic (proven by run).

**Checkable constraints:**

- `abs(r_series_analytic - r_series_sim) < 0.05`
- `abs(r_parallel_analytic - r_parallel_sim) < 0.05`
- `r_series_analytic < r_parallel_analytic`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def reliability_series(component_reliabilities: List[float]) -> float:`, `def reliability_parallel(component_reliabilities: List[float]) -> float:`, `def simulate_series(component_reliabilities: List[float], num_sim: int) -> float:`, `def simulate_parallel(component_reliabilities: List[float], num_sim: int) -> float:`
**Valid input:** `component_reliabilities` is a non-empty list of probabilities in [0, 1]; `num_sim` > 0.
**Core:** Analytic and simulation-based system reliability. Series: all components must work → product of reliabilities. Parallel: at least one must work → `1 − Π(1 − r_i)`. Monte Carlo simulations verify the analytic formulas.
**Assert:** For four components with `r = 0.9`, simulated series and parallel reliabilities are within 0.05 of analytic values; series reliability is below parallel reliability.
**⚠️ Defect:** No validation that component reliabilities are in [0, 1]; values outside this range silently produce nonsensical probabilities. `simulate_series` and `simulate_parallel` import `random` locally, so they are not seeded and not reproducible unless the caller seeds the global random state.

---
*△ AURA Pattern Library — © Reality Optimizer*
