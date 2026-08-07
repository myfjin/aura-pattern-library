# competing risks naive bias

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(times: List[float], events: List[int], event_type: int) → Tuple[List[float], List[float]]`

## What it does

Competing risks: the naive 1−KM overestimates incidence; Aalen-Johansen is correct.

With competing events, a common MISTAKE is to estimate the cumulative incidence of
cause 1 as 1 − KM, where the cause-specific Kaplan-Meier treats every competing event
(and censoring) as if it were independent right-censoring. That double-counts the people
removed by the competing risk and OVERSTATES the incidence. The correct Aalen-Johansen
CIF weights each cause-1 hazard increment by the overall survival S(t⁻):
    F₁(t) = Σ_{s≤t} [d₁(s)/Y(s)] · S(s⁻),  S(s) = ∏ (1 − d_any(s)/Y(s)).
Core claim: with censoring present, naive (1−KM) > correct (Aalen-Johansen); bias shown.

## Guarantee

When it runs, competing risks naive bias guarantees final_naive > final_correct + 0.1; 0.0 < final_correct < 1.0; final_naive <= 1.0 + 1e-09 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_naive > final_correct + 0.1`
- `0.0 < final_correct < 1.0`
- `final_naive <= 1.0 + 1e-09`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def naive_km_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:`, `def aalen_johansen_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:`
**Valid input:** `times` and `events` are equal-length lists; `events` ∈ {0,1,2} where 0 = censored, 1/2 = competing events; `event_type` is 1 or 2.
**Core:** Shows the bias in competing-risks analysis. The naive `1 − KM` cumulative incidence treats competing events as independent censoring and overstates incidence. The correct Aalen-Johansen estimator weights each cause-specific hazard increment by the overall survival probability just before the event time.
**Assert:** Final naive CIF exceeds final Aalen-Johansen CIF by at least 0.1; Aalen-Johansen CIF is a valid probability in (0, 1); naive CIF does not exceed 1.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
