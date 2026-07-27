# retry timeout

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(operation: Callable, max_attempts: int, timeout_sec: float) → ?`

## What it does

retry_timeout: retry an operation with a timeout; fail if it doesn't succeed within deadline.
Failure simulated: operation fails 3 times in succession, then succeeds on 4th try.
Recovery asserted: retry succeeds on eventual attempt; max_attempts enforced to prevent infinite retry.

## Guarantee

When it runs, retry timeout guarantees attempts == 4; success is True; success is False (proven by run).

**Checkable constraints:**

- `success is True`
- `attempts == 4`
- `success is False`
- `attempts < 1000`
- `attempts > 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
