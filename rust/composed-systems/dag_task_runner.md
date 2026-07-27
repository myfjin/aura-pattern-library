# dag task runner

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(tasks: &[Task], workers: usize) → Result<(Vec<Option<usize>>, Vec<usize>), String>`

## What it does

dag_task_runner — topological readiness + a real thread worker-pool executing a DAG.

Core idea: composes W2's topological ordering with W1's shared-queue worker pool. Tasks with
satisfied dependencies land on a shared ready-queue; N worker threads pull and run them, and
on completion release dependents (decrement in-degree, enqueue newly-ready) under a Condvar.
Because a task is enqueued ONLY after every dependency has committed, deps always run first —
even under parallel scheduling. THE LAW: run a DAG on multiple threads and assert (1) every
task ran exactly once, (2) each task ran AFTER all its deps (checked against the real exec log),
(3) the aggregate is exact, and (4) a cycle is rejected. When to use: build systems, workflows.

## Guarantee

When it runs, dag task runner guarantees assert_eq!(exec_order.len(), 4, "all tasks ran once") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(exec_order.len(), 4, "all tasks ran once")`
- `assert!(results.iter().all(|r| r.is_some()), "every task produced a result")`
- `assert!(pos[&d] < pos[&i], "dep {d} must complete before task {i} (order {exec_order:?})")`
- `assert_eq!(total, (10 + 20 + 30 + 40) * 2, "aggregate exact")`
- `assert!(execute_parallel(&cycle, 2).is_err(), "cycle detected, not deadlocked")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
