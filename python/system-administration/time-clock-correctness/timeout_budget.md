# timeout budget

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(operation_duration: float) → ?`

## What it does

Budget timeouts across multiple sequential operations.

## Guarantee

When it runs, timeout budget guarantees remaining == 7.0; remaining == 2.0; remaining == 0.0 (proven by run).

**Checkable constraints:**

- `remaining == 7.0`
- `remaining == 2.0`
- `remaining == 0.0`
- `'exceeds remaining' in str(e)`
- `'Budget exhausted' in str(e)`
- `'12' in str(e)`
- `'not started' in str(e)`
- `budget.remaining() == 0.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
