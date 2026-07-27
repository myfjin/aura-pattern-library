# rate counter

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(count: u64, time: u32) → f64`

## What it does

rate_counter — reset-safe counter rate; planted resets not read as spikes.

Core idea: track event count and compute rate per time unit. When the counter
resets, the rate should remain stable (not spike). THE ONE LAW: plant a reset,
assert that the rate across the reset boundary is computed correctly and doesn't
produce a spurious spike. A naive delta (current - prev) would see the reset as a
negative spike; a correct impl handles it.
When to use: traffic rate, request counters, monotonic metric rates.

## Guarantee

When it runs, rate counter guarantees assert_eq!(rate_zero, 0.0, "rate should initialize to 0"); assert_eq!(rate_same, 0.0, "rate at zero time-delta should not change") (proven by rustc-run).

**Checkable constraints:**

- `assert!((rate1 - 10.0).abs() < 1e-6, "rate should be 10 events/time")`
- `assert!(rate_after_reset >= 0.0, "rate after reset must be non-negative")`
- `assert!(rate_after_reset < 1.5, "rate after reset (100 in 100 units) should be around 1.0, not a spike")`
- `assert!((rate1 - 10.0).abs() < 1e-6)`
- `assert!((rate2 - 10.0).abs() < 1e-6)`
- `assert!((rate3 - 10.0).abs() < 1e-6)`
- `assert_eq!(rate_zero, 0.0, "rate should initialize to 0")`
- `assert_eq!(rate_same, 0.0, "rate at zero time-delta should not change")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
