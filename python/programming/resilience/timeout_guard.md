# timeout guard

**Language:** Python · **Sphere:** programming · **Category:** Resilience

**Signature:** `(duration: float, result: str) → str`

## What it does

Timeout guard that interrupts an operation past its deadline.

A context manager (TimeoutGuard) and wrapper (TimedOperation) that bound how
long an operation may run: it prefers signal-based interruption via setitimer
on Unix main threads and falls back to a threading.Timer elsewhere, raising
TimeoutError or invoking a fallback when the deadline passes. Use it to cap a
call that may hang. Guarantees (self-test oracle): a 2s task under a 0.3s
deadline is actually cut off near the deadline (not double it — a fixed
truncation bug), the fallback fires only on timeout, in-deadline tasks complete
normally, and the operation's own exceptions surface instead of being masked.

## Guarantee

When it runs, timeout guard guarantees abs(elapsed - 0.3) < 0.25; TimedOperation(fast_task, timeout=1.0).execute('Quick') == 'Quick'; result == 'Fallback: too slow' (proven by run).

**Checkable constraints:**

- `TimedOperation(fast_task, timeout=1.0).execute('Quick') == 'Quick'`
- `result == 'Fallback: too slow'`
- `elapsed < 1.5`
- `abs(elapsed - 0.3) < 0.25`
- `time.monotonic() - start < 1.5`
- `interrupted`
- `guard.fallback_value == 'guard-fb'`
- `TimedOperation(lambda: slow_task(0.05, 'in time'), timeout=1.0).execute() == 'in time'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
