# reactive signals

**Language:** Python · **Sphere:** programming · **Category:** Async

## What it does

Fine-grained reactive primitives — Signal, Computed, Effect — with automatic
dependency tracking through a context stack.

Use when values should recompute (Computed) or side effects re-run (Effect) only
when the specific Signals they actually read change. Reading a signal inside a
reactive context records the edge; setting a signal lazily invalidates dependent
computeds and eagerly re-runs effects; dispose() detaches an observer.

Guarantees (self-test): computed values track exactly the signals they read, an
unrelated signal never re-fires an effect, computed-of-computed chains recompute,
and a disposed effect stops firing while surviving effects keep updating.

## Guarantee

When it runs, reactive signals guarantees doubled.value == 10; multiplied.value == 10; multiplied.value == 15 (proven by run).

**Checkable constraints:**

- `doubled.value == 0 and multiplied.value == 0`
- `log == [('doubled', 0), ('multiplied', 0)]`
- `doubled.value == 10`
- `multiplied.value == 10`
- `('doubled', 10) in log and ('multiplied', 10) in log`
- `multiplied.value == 15`
- `doubled.value == 10`
- `n_doubled_after == n_doubled_before`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
