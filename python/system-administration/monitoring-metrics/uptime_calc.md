# uptime calc

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(start_time: int, end_time: int) → ?`

## What it does

uptime_calc: calculate uptime percentage from events.

## Guarantee

When it runs, uptime calc guarantees uptime_all_up == 100.0; uptime_2 == 80.0; uptime_3 == 80.0 (proven by run).

**Checkable constraints:**

- `uptime_all_up == 100.0`
- `uptime_2 == 80.0`
- `uptime_3 == 80.0`
- `uptime_partial == 60.0`
- `abs(uptime_partial2 - expected) < 0.1`
- `abs(uptime_nines - expected_nines) < 0.01`
- `uptime_starts_down == 50.0`
- `abs(uptime_frac - expected_frac) < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
