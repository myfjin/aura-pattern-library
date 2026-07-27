# barrier sync

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

barrier_sync — an N-thread barrier ensuring no thread proceeds until all N arrive.

Core idea: N threads call wait(); a counter increments on each arrival. No thread
returns from wait() until counter == N. THE ONE LAW: each thread increments a shared
"arrived" witness BEFORE calling wait(), then AFTER wait() asserts the witness equals
N — i.e. every thread had already arrived before this one was allowed to leave. A
no-op (broken) barrier lets a thread pass with the witness still below N, so the
post-wait assertion fails. When to use: synchronizing independent workers at a checkpoint.

## Guarantee

When it runs, barrier sync guarantees assert_eq!(seen, n_threads, "left barrier with only {seen}/{n_threads} arrived"); assert_eq!(arrived_witness.load(Ordering::SeqCst), n_threads, "not all threads reached the barrier") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(seen, n_threads, "left barrier with only {seen}/{n_threads} arrived")`
- `assert_eq!(arrived_witness.load(Ordering::SeqCst), n_threads, "not all threads reached the barrier")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
