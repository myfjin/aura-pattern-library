# atomic refcount

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `() → u64`

## What it does

atomic_refcount — a hand-rolled atomic reference count with concurrent clone/drop.

Core idea: an AtomicU64 holds the refcount. Each clone() increments; each drop()
decrements. When count hits 0, the resource is freed. THE ONE LAW: spawn N threads,
each performing K balanced clone/drop pairs concurrently. Because fetch_add/fetch_sub
are atomic, every increment and decrement is accounted for: after all threads finish,
the count must equal the baseline EXACTLY (not merely "> 0"), and the final drop of
the baseline reference must return exactly 0. A non-atomic counter loses updates under
contention and lands off the exact baseline. When to use: learning how reference
counting works at the atomic level (Arc is safer; this is educational).

## Guarantee

When it runs, atomic refcount guarantees assert_eq!(baseline, 1, "atomic refcount drifted off baseline: {baseline} (lost updates)"); assert_eq!(last, 0, "final drop of baseline must reach 0, saw {last}") (proven by rustc-run).

**Checkable constraints:**

- `assert!(after_clone >= 2, "clone must lift count to >= 2, saw {after_clone}")`
- `assert_eq!(baseline, 1, "atomic refcount drifted off baseline: {baseline} (lost updates)")`
- `assert_eq!(last, 0, "final drop of baseline must reach 0, saw {last}")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
