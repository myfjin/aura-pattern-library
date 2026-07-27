# cancellable task group

**Language:** Python · **Sphere:** programming · **Category:** Async

**Signature:** `(name: str, duration: float, token: CancellationToken) → str`

## What it does

Async task group implementation with cancellation support.

## Guarantee

When it runs, cancellable task group guarantees n_done == 3; len(results) == 3; t_quick.result == 'Task A finished instantly' (proven by run).

**Checkable constraints:**

- `len(results) == 3`
- `t_quick.result == 'Task A finished instantly'`
- `t_quick.completed and t_quick.exception is None`
- `isinstance(t_fail.exception, ValueError)`
- `t_fail.result is None`
- `t_short.result == 'Task C completed successfully'`
- `n_done == 3`
- `tg.token.is_cancelled`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
