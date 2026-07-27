# debounce throttle

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(time: u32) → ?`

## What it does

debounce_throttle — event debounce/throttle over virtual clock; emitted set exact.

Core idea: debounce waits for a quiet period before emitting; throttle emits at
most once per time window. THE ONE LAW: plant an event sequence with timings,
apply debounce/throttle, and assert the emitted set is exactly correct — no missed
events, no extra emissions.
When to use: UI responsiveness (debounce search), rate limiting (throttle clicks).

## Guarantee

When it runs, debounce throttle guarantees assert_eq!(emitted[0], 7, "debouncer should first emit at time 7"); assert_eq!(gap, 10, "gap between emissions should be exactly throttle period") (proven by rustc-run).

**Checkable constraints:**

- `assert!(emitted.len() >= 1, "debouncer should emit after quiet period, got {}", emitted.len())`
- `assert_eq!(emitted[0], 7, "debouncer should first emit at time 7")`
- `assert_eq!(emitted, vec![0, 6, 12], "throttler should emit at times 0, 6, 12")`
- `assert_eq!(emitted, vec![0, 10, 20, 30, 40], "throttler should emit every 10 time units")`
- `assert_eq!(gap, 10, "gap between emissions should be exactly throttle period")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
