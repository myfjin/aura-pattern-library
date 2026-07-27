# nelson aalen cumhazard

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(times: List[float], events: List[int]) → Tuple[List[float], List[float]]`

## What it does

Nelson-Aalen cumulative hazard: nonparametric estimate from event times.

H(t) = Σ d_i / y_i where d_i = events at time i, y_i = at-risk count.
Core claim: cumulative hazard monotone increasing; verified vs Kaplan-Meier.

## Guarantee

When it runs, nelson aalen cumhazard guarantees cumhazard[i] >= cumhazard[i - 1] - 1e-10; cumhazard[-1] > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `cumhazard[i] >= cumhazard[i - 1] - 1e-10`
- `cumhazard[-1] > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def nelson_aalen_cumhazard(times: List[float], events: List[int]) -> Tuple[List[float], List[float]]:`
**Valid input:** `times` and `events` are equal-length lists; `events[i]` ∈ {0,1}; `times` ≥ 0.
**Core:** Nelson-Aalen estimator of the cumulative hazard function: `H(t) = Σ_{s ≤ t} d_s / y_s`, where `d_s` is the number of events at time `s` and `y_s` is the number at risk just before `s`.
**Assert:** The estimated cumulative hazard is monotone non-decreasing; the final value is positive for the planted exponential example with 50 uncensored observations.
**⚠️ Defect:** Censored observations are included in the risk set but do not contribute to the hazard increment, which is correct, but the function does not return the number at risk or event counts for diagnostics. Time points where no events occur are omitted from the output, so the step function is not directly plottable without interpolation. No input validation.

---
*△ AURA Pattern Library — © Reality Optimizer*
