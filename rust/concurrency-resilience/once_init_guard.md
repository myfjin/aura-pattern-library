# once init guard

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(f: F) → ?`

## What it does

once_init_guard — a one-time initializer that runs exactly once across racing threads.

Core idea: use a CAS loop (or std::sync::Once) to ensure a closure runs exactly once,
even if N threads call init() simultaneously. THE ONE LAW: N threads race to init();
a counter inside the closure increments exactly once. If the guard fails, multiple threads
run the closure and the counter > 1. When to use: lazy initialization of shared state
without full locks; think singletons, lazy statics, connection pools.

## Guarantee

When it runs, once init guard guarantees assert_eq!(count, 1, "init closure ran {} times, expected exactly 1", count) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(count, 1, "init closure ran {} times, expected exactly 1", count)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
