# atomic counter sharded

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(which: usize) → ?`

## What it does

atomic_counter_sharded — a sharded atomic counter that stays exact under concurrency.

Core idea: N worker threads each hit one of S shards (an `AtomicU64`) to cut contention;
the total is the sum of shards. THE ONE LAW: run a genuine concurrent increment race,
then assert the total equals the planted number of increments — a non-atomic `+= 1`
would lose updates under the race and the count assert would catch it.
When to use: high-throughput metrics counters where one hot atomic would contend.

## Guarantee

When it runs, atomic counter sharded guarantees assert_eq!(got, expected, "sharded counter lost updates under concurrency") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got, expected, "sharded counter lost updates under concurrency")`
- `assert!(used >= 2, "expected work across shards, only {used} used")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
