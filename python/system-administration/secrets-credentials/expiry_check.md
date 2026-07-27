# expiry check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(token: str, expiry_time: int, clock: LogicalClock) → ?`

## What it does

Expiry check: reject tokens based on logical clock, not wall-clock.
Failure simulated: token expires at clock=100; check at clock=50 (accept),
then at clock=150 (reject). Assert accept/reject based on logical time only.

## Guarantee

When it runs, expiry check guarantees result1 is True; result2 is True; result3 is False (weak-grade: directional, proven by run).

**Checkable constraints:**

- `result1 is True`
- `result2 is True`
- `result3 is False`
- `result4 is False`
- `result_replay is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
