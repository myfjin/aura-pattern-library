# cron expr next fire

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(cron_expr: str, from_time: float) → ?`

## What it does

Cron expression parser: calculate next fire time exactly.
Failure simulated: parse a cron expression and compute the EXACT next fire timestamp.
Assert: next_fire() produces the expected timestamp for known inputs.

## Guarantee

When it runs, cron expr next fire guarantees next_ts == expected_dt.timestamp(); next_ts == expected_dt.timestamp(); 'Invalid cron' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `next_ts == expected_dt.timestamp()`
- `next_ts == expected_dt.timestamp()`
- `'Invalid cron' in str(e)`
- `next_ts == expected_dt.timestamp()`
- `'Invalid field' in str(e) or 'out of range' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
