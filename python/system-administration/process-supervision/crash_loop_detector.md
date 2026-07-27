# crash loop detector

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(restart_threshold: int, window_seconds: float) → ?`

## What it does

crash_loop_detector: count restarts in a sliding window; if threshold exceeded, flag crash-loop + stop restarting.
Failure simulated: 6 restarts in 60 seconds (exceeds threshold of 5).
Recovery asserted: crash_loop_flag is True; assert flag prevents further restarts.

## Guarantee

When it runs, crash loop detector guarantees actual_restarts == expected_restarts; detector.crash_loop_detected is True and detector.should_restart() is False; window_span < 1.0 (proven by run).

**Checkable constraints:**

- `actual_restarts == expected_restarts`
- `detector.crash_loop_detected is True and detector.should_restart() is False`
- `window_span < 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
