# reusable phaser

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

reusable_phaser — a reusable multi-phase barrier for N threads across P phases.

Core idea: N threads synchronize at each of P phases. Each phase requires all N to
arrive before any advance. THE ONE LAW: at every phase each thread increments a shared
per-phase witness BEFORE arriving, then AFTER the phaser returns asserts the witness
equals N — no thread advances past phase k until all N have reached phase k. A no-op
(broken) phaser lets a thread advance while the witness is still below N, failing the
assertion. When to use: iterative algorithms with per-iteration synchronization points.

## Guarantee

When it runs, reusable phaser guarantees assert_eq!(seen, n_threads, "advanced past phase {phase} with only {seen}/{n_threads} arrived"); assert_eq!(count, n_threads, "phase {phase} had {count} arrivals, expected {n_threads}") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(seen, n_threads, "advanced past phase {phase} with only {seen}/{n_threads} arrived")`
- `assert_eq!(count, n_threads, "phase {phase} had {count} arrivals, expected {n_threads}")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
