# df capacity forecast

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(samples: &[DfSample], capacity: u64) → Option<u32>`

## What it does

df_capacity_forecast — linear time-to-full from synthetic df samples; matches trajectory.

Core idea: collect disk usage samples over time, fit a line, forecast when full.
THE ONE LAW: plant a known growth rate, collect samples, fit, forecast, and assert
the prediction matches the hand-computed time-to-full.
When to use: capacity planning, SLA monitoring, disk quota alerts.

## Guarantee

When it runs, df capacity forecast guarantees assert_eq!(forecast, 100, "forecast should match hand math"); assert_eq!(forecast2, 20, "forecast should be at 20 seconds") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(forecast, 100, "forecast should match hand math")`
- `assert_eq!(forecast2, 20, "forecast should be at 20 seconds")`
- `assert!((expected_ttf - 10.0).abs() < 1.0, "time-to-full should match")`
- `assert!(forecast3.is_none(), "single sample should not forecast")`
- `assert!(forecast4.is_none(), "negative growth should not forecast full")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
