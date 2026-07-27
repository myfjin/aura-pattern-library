# wait group

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

wait_group — an add/done/wait pattern for coordinating task completion.

Core idea: call add(n) to register N tasks; call done() when a task finishes.
wait() blocks until all tasks have signaled done(). THE ONE LAW: add(k) tasks,
spawn k workers that each call done() upon completion. wait() must block until
all k done() calls have occurred. Count mismatches reveal lost or extra signals.
When to use: fan-out work and wait for all to finish without knowing tasks upfront.

## Guarantee

When it runs, wait group guarantees assert_eq!(completed, n_tasks, "not all tasks completed") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(completed, n_tasks, "not all tasks completed")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
