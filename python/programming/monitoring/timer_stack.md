# timer stack

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `() → None`

## What it does

Stack-based hierarchical timers for nested-section profiling.

Use to time nested code sections: start pushes a named timer, stop pops the
innermost one (LIFO), elapsed time accumulates across repeated start/stop of the
same name, and call counts are tracked. Usable as a context manager that
force-stops anything still running on exit; report() renders a sorted summary.
Guarantees (proven by self-test on a fake clock): elapsed arithmetic is exact
and accumulates across restarts; a running timer reads live time; stop() pops the
innermost timer; __exit__ closes abandoned timers; and double-start, stop on a
stopped timer, or stop on an empty stack raise RuntimeError.

## Guarantee

When it runs, timer stack guarantees t.elapsed() == 2.5; t.elapsed() == 4.0; t.elapsed() == 4.5 and t.running (proven by run).

**Checkable constraints:**

- `t.elapsed() == 2.5`
- `t.elapsed() == 4.0`
- `t.elapsed() == 4.5 and t.running`
- `t.elapsed() == 0.0 and (not t.running)`
- `stack.stop() == 'inner'`
- `stack.stop() == 'outer'`
- `stack.get_elapsed('inner') == 2.0`
- `stack.get_elapsed('outer') == 4.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
