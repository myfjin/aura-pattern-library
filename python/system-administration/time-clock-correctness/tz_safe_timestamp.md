# tz safe timestamp

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(dt: datetime, target_tz: timezone) → ?`

## What it does

Safe timezone-aware timestamp handling without DST confusion.

## Guarantee

When it runs, tz safe timestamp guarantees TZSafeConverter.round_trip(original_dt, tz_plus5) is True; 'timezone-aware' in str(e); epoch1 == original_epoch (weak-grade: directional, proven by run).

**Checkable constraints:**

- `TZSafeConverter.round_trip(original_dt, tz_plus5) is True`
- `'timezone-aware' in str(e)`
- `epoch1 == original_epoch`
- `epoch2 == original_epoch`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
