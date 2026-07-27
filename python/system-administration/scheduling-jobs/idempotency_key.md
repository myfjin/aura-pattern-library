# idempotency key

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(idempotency_key: str, callback: Callable) → ?`

## What it does

Idempotency key: same key submitted twice → operation runs exactly once.
Failure simulated: submit same key twice concurrently; assert callback fires once.

## Guarantee

When it runs, idempotency key guarantees exec_count[0] == 2; exec_count[0] == 1; len(results) == 2 (proven by run).

**Checkable constraints:**

- `exec_count[0] == 1`
- `len(results) == 2`
- `sum(executed_flags) == 1`
- `result_values[0] == result_values[1]`
- `exec_count[0] == 2`
- `all((r[0] for r in results))`
- `was_exec1 is True`
- `result1 == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
