# worker pool mpsc

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(n_workers: usize, jobs: Vec<u64>) → (u64, u64)`

## What it does

worker_pool_mpsc — a fixed thread pool draining jobs off an `mpsc` channel.

Core idea: a set of planted jobs is sent into an mpsc channel; W worker threads share
the receiver (behind `Arc<Mutex<..>>`) and pull until the channel drains and closes.
THE ONE LAW: submit jobs whose squared results have a known sum, then assert every job
ran EXACTLY once (exact count) and the order-agnostic result sum is exact — a pool that
dropped or double-ran jobs would miss the count or the sum. When to use: bounded
parallelism with a shared work queue.

## Guarantee

When it runs, worker pool mpsc guarantees assert_eq!(sum, expected_sum, "result sum wrong under parallel execution") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(done, n_jobs, "job count wrong: dropped or double-ran jobs")`
- `assert_eq!(sum, expected_sum, "result sum wrong under parallel execution")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
