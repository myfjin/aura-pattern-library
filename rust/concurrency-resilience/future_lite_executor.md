# future lite executor

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(id: usize, depends_on: Option<usize>) → ?`

## What it does

future_lite_executor — a tiny single-threaded executor for state-machine tasks.

Core idea: a set of tasks, each with a simple state machine (pending/ready/done).
The executor polls all tasks to completion in a loop. THE ONE LAW: create N tasks
with dependencies (task B waits on task A). Run the executor; all tasks must
complete, and task B must never run before task A finishes.
When to use: cooperative multitasking and executor patterns.

## Guarantee

When it runs, future lite executor guarantees assert_eq!(order.len(), 4, "not all tasks executed") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(order.len(), 4, "not all tasks executed")`
- `assert!(pos(0) < pos(1), "task 0 should run before 1")`
- `assert!(pos(0) < pos(3), "task 0 should run before 3")`
- `assert!(pos(1) < pos(2), "task 1 should run before 2")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
