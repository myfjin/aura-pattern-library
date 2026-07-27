# cron expr next fire

**Language:** Go · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(cron_expr: str, from_time: float) → ?`

## What it does

cron_expr_next_fire: parse a cron expression and compute the exact next fire timestamp.

## Guarantee

When it runs, cron expr next fire guarantees next_ts == expected_dt.timestamp(); next_ts == expected_dt.timestamp(); 'Invalid cron' in str(e) (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `next_ts == expected_dt.timestamp()`
- `next_ts == expected_dt.timestamp()`
- `'Invalid cron' in str(e)`
- `next_ts == expected_dt.timestamp()`
- `'Invalid field' in str(e) or 'out of range' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
