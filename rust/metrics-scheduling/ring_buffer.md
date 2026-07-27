# ring buffer

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(value: f64) → ?`

## What it does

ring_buffer — fixed-capacity ring buffer; windowed stats (sum/mean) match brute force.

Core idea: ring buffer holds the last N samples in a circular buffer; sum and mean
are computed incrementally as items are pushed. THE ONE LAW: plant a known sequence
into the ring, compare windowed sum and mean to brute-force computation on the same
window, and assert they match exactly. A broken circular index or stale sum would fail.
When to use: sliding-window aggregates, online metrics, memory-bounded statistics.

## Guarantee

When it runs, ring buffer guarantees assert_eq!(ring.len(), 20, "ring should hold exactly capacity items"); assert_eq!(window_vec, expected_window, "ring contents must match expected window") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(ring.len(), 20, "ring should hold exactly capacity items")`
- `assert!((ring.sum() - expected_sum).abs() < 1e-9, "ring sum {} does not match expected sum {}", ring.sum(), expected_sum)`
- `assert!((ring.mean() - expected_mean).abs() < 1e-9, "ring mean {} does not match expected mean {}", ring.mean(), expected_mean)`
- `assert_eq!(window_vec, expected_window, "ring contents must match expected window")`
- `assert!((ring.sum() - expected_sum_after).abs() < 1e-9, "after eviction, ring sum must match")`
- `assert!((ring.mean() - expected_mean_after).abs() < 1e-9, "after eviction, ring mean must match")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
