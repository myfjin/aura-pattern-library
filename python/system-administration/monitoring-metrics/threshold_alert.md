# threshold alert

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(value: int) → ?`

## What it does

threshold_alert: fire alerts when metrics cross thresholds.

## Guarantee

When it runs, threshold alert guarantees alert_multi.alert_count == 2; not alert_gt.check(50); not alert_gt.check(75) (proven by run).

**Checkable constraints:**

- `not alert_gt.check(50)`
- `not alert_gt.check(75)`
- `not alert_gt.check(100)`
- `alert_gt.check(101)`
- `alert_gt.is_alerting()`
- `not alert_gt.check(101)`
- `not alert_gt.check(100)`
- `alert_gt.is_alerting()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
