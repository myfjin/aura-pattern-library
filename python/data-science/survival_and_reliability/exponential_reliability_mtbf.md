# exponential reliability mtbf

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(failure_times: List[float]) → float`

## What it does

Exponential reliability: MTBF and survival function from failure times.

For constant hazard h(t) = λ, survival S(t) = exp(-λt) and MTBF = 1/λ.
Core claim: MTBF estimated from sample, compared to true and to analytic.

## Guarantee

When it runs, exponential reliability mtbf guarantees abs(mtbf_est - mtbf_true) < 30; abs(s_at_mtbf - math.exp(-1.0)) < 0.05 (proven by run).

**Checkable constraints:**

- `abs(mtbf_est - mtbf_true) < 30`
- `abs(s_at_mtbf - math.exp(-1.0)) < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def exponential_mtbf(failure_times: List[float]) -> float:`, `def exponential_survival(t: float, mtbf: float) -> float:`
**Valid input:** `failure_times` is a non-empty list of positive numbers; `t` ≥ 0; `mtbf` > 0.
**Core:** For a constant-hazard exponential model, MTBF = `1/λ` is estimated as the sample mean failure time, and survival probability is `S(t) = exp(−t/MTBF)`.
**Assert:** Estimated MTBF from 50 exponential samples is within 30 of the true MTBF=100; `S(MTBF)` ≈ `e^(−1)` ≈ 0.368 within 0.05.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
