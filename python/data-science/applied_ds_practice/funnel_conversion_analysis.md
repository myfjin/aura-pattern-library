# funnel conversion analysis

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(successes: int, trials: int, confidence: float) → tuple[float, float]`

## What it does

Multi-step funnel conversion analysis with confidence intervals.

Track user progression through a conversion funnel (e.g., visit → signup →
purchase → retain). Compute step-wise conversion rates with Wilson confidence
intervals. Identify the weakest step.

Use: product analytics, sales/marketing funnels, conversion rate optimization.

## Guarantee

When it runs, funnel conversion analysis guarantees weakest_step == 'purchase'; trial_ci[0] > purchase_ci[1] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `weakest_step == 'purchase'`
- `trial_ci[0] > purchase_ci[1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def wilson_confidence_interval(successes: int, trials: int, confidence: float = 0.95) -> tuple[float, float]:`, `def build_funnel_events(events: list[dict]) -> dict[str, dict]:`, `def compute_conversion_rates(funnel: dict[str, dict], step_order: list[str]) -> dict[str, dict]:`
**Valid input:** `events` are dicts with `user_id` and `step`. `funnel` is the output of `build_funnel_events`. `step_order` lists steps in progression order.
**Core:** Multi-step funnel analysis. Aggregates unique users per step, computes step-to-step conversion rates, and adds Wilson score confidence intervals. Identifies the weakest step by minimum conversion rate.
**Assert:** On a planted funnel (visit→signup 80%, signup→trial 75%, trial→purchase 20%), the weakest step is "purchase" and the trial conversion CI lies entirely above the purchase conversion CI.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
