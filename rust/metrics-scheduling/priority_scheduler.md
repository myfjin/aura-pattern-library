# priority scheduler

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(other: &Self) → Ordering`

## What it does

priority_scheduler — BinaryHeap job scheduler with fairness.

Core idea: jobs with priority are scheduled; higher priority jobs run first.
Fairness is maintained by aging: priority increases over time. THE ONE LAW: plant
a job mix, run them, and assert that jobs execute in priority order respecting
aging — a stale job eventually runs despite lower initial priority.
When to use: task scheduling, priority queues, fair resource allocation.

## Guarantee

When it runs, priority scheduler guarantees assert_eq!(order1, 2, "job 2 (priority 10) should run first"); assert_eq!(order2, 3, "job 3 (priority 8) should run second"); assert_eq!(order3, 1, "job 1 (priority 5) should run third") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(order1, 2, "job 2 (priority 10) should run first")`
- `assert_eq!(order2, 3, "job 3 (priority 8) should run second")`
- `assert_eq!(order3, 1, "job 1 (priority 5) should run third")`
- `assert_eq!(order, 12, "job 12 (high priority) runs first")`
- `assert_eq!(order, 10, "after aging, older job 10 (same priority) runs next")`
- `assert_eq!(order, 11, "younger job 11 runs last")`
- `assert_eq!(sched.run_order, vec![2, 3, 1], "run order must match priority then creation")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
