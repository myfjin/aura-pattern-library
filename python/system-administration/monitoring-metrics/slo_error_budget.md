# slo error budget

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(count: int) → ?`

## What it does

slo_error_budget: track error budget against SLO.

## Guarantee

When it runs, slo error budget guarantees success_rate == 99.9; success == 99.0; budget_consumed == 100.0 (proven by run).

**Checkable constraints:**

- `success_rate == 99.9`
- `not slo.over_budget()`
- `slo.over_budget()`
- `success == 99.0`
- `budget_consumed == 100.0`
- `remaining == 0`
- `not slo999.over_budget()`
- `remaining_999 == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
