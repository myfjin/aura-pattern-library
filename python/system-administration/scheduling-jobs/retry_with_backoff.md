# retry with backoff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(callback: Callable, max_attempts: int, initial_delay: float, max_delay: int) → ?`

## What it does

Retry with backoff: exponential backoff for failed operations.
Failure simulated: callback fails N times; assert retry delays grow exponentially.

## Guarantee

When it runs, retry with backoff guarantees attempts == 2; attempts == 4; success (proven by run).

**Checkable constraints:**

- `success`
- `attempts == 2`
- `total_delay > 0.04`
- `elapsed >= total_delay * 0.8`
- `not success`
- `attempts == 4`
- `0.3 <= total_delay <= 0.5`
- `len(intervals) >= 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
