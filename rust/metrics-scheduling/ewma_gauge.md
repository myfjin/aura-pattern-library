# ewma gauge

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(sample: f64) → bool`

## What it does

ewma_gauge — exponentially weighted moving average with hysteresis alert.

Core idea: EWMA smooths noisy samples; hysteresis prevents alert flapping when
the signal hovers near the threshold. THE ONE LAW: plant a known sequence with
drift, compute EWMA by hand, verify it matches, inject a drifting event sequence,
and assert alerts fire only when crossing the threshold with hysteresis deadband —
a broken EWMA or missing hysteresis would trigger spurious alerts or miss real ones.
When to use: anomaly detection, threshold alerts, smoothing noisy metrics.

## Guarantee

When it runs, ewma gauge guarantees assert_eq!(alert_count, 1, "exactly one alert should fire when drifting above threshold with hysteresis") (proven by rustc-run).

**Checkable constraints:**

- `assert!((gauge.current() - manual[i]).abs() < 1e-9, "EWMA mismatch at step {}: gauge={}, manual={}", i, gauge.current(), manual[i])`
- `assert_eq!(alert_count, 1, "exactly one alert should fire when drifting above threshold with hysteresis")`
- `assert!(spike_alert, "spike should trigger alert")`
- `assert!(still_alert, "alert should remain active when above threshold")`
- `assert!(!de_alert, "alert should clear when dropping below threshold-hysteresis")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
