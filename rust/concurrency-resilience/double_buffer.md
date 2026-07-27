# double buffer

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `() → u64`

## What it does

double_buffer — atomic front/back buffer swap ensuring readers always see consistent state.

Core idea: two buffers (front and back). A writer updates the back buffer, then
swaps it to front (atomically). Readers always see a complete front buffer, never
catching a half-written update. THE ONE LAW: readers must never observe a torn
buffer (partial write). Concurrent writers/readers with an atomic swap ensure readers
always see a fully-consistent snapshot. When to use: publishing large updated state
(configs, metrics snapshots) without blocking readers.

## Guarantee

When it runs, double buffer guarantees assert_eq!(total_torn, 0, "double_buffer failed: {} inconsistencies detected", total_torn) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(total_torn, 0, "double_buffer failed: {} inconsistencies detected", total_torn)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
