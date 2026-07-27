# kaplan meier survival

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(times: List[float], events: List[int]) → List[Tuple[float, float]]`

## What it does

Kaplan-Meier Survival Curve with Censored Observations.

Estimates a survival function from time-to-event data with right censoring.
Computes the product of (1 - events/at_risk) at each event time.
Use when analyzing time-to-event data with censoring (medical, reliability, churn).

## Guarantee

When it runs, kaplan meier survival guarantees abs(surv_at_3 - expected_surv_at_3) < 1e-06; n == len(events); check_kaplan_meier_properties(km_curve) (proven by run).

**Checkable constraints:**

- `n == len(events)`
- `check_kaplan_meier_properties(km_curve)`
- `surv_at_3 is not None`
- `abs(surv_at_3 - expected_surv_at_3) < 1e-06`
- `check_kaplan_meier_properties(km_synthetic)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `kaplan_meier(times, events) → List[Tuple[float, float]]`
**Valid input:** `times: List[float]` — event/censoring times. `events: List[int]` — 1=event, 0=censored. Same length.
**Core:** Kaplan-Meier survival curve estimator. Sorted by time, at each unique event time: S(t) = S(t⁻) × (1 - events_at_time / at_risk). At-risk count decreases by events + censored at each time. Returns list of (time, survival_prob) pairs.
**Assert:** On hand-computed example (5 subjects: times [1,2,2,3,4], events [1,1,0,1,0]), survival at t=3 is 0.3. Curve is non-increasing. Synthetic test (50 samples) also non-increasing.
**⚠️ Defect:** The function uses `set(t for t in times_sorted if t is not None)` to get unique event times, but the `if t is not None` filter is unnecessary since times are floats. More importantly, the function processes ALL unique times including those where only censoring occurs (no events), which is correct but the survival probability doesn't change at pure-censoring times. The at-risk count is reduced correctly.

---
*△ AURA Pattern Library — © Reality Optimizer*
