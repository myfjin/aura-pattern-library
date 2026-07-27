# heartbeat miss alert

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(timestamp: int) → ?`

## What it does

heartbeat_miss_alert: detect heartbeat/watchdog timeouts.

## Guarantee

When it runs, heartbeat miss alert guarantees alert4.alert_count == 2; not alert.check(10); not alert.is_alerting() (proven by run).

**Checkable constraints:**

- `not alert.check(10)`
- `not alert.is_alerting()`
- `not alert.check(20)`
- `not alert.is_alerting()`
- `not alert2.check(30)`
- `not alert2.check(59)`
- `alert2.check(61)`
- `alert2.is_alerting()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
