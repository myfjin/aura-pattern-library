# crash loop detector

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 1 · Process Supervision & Immortality

## What it does

crash_loop_detector: count restarts in a sliding window; if threshold exceeded, flag crash-loop + stop restarting.

## Guarantee

When it runs, crash loop detector guarantees actual_restarts == expected_restarts; detector.crash_loop_detected is True and detector.should_restart() is False; window_span < 1.0 (proven by run on the SYS original).

**Checkable constraints:**

- `actual_restarts == expected_restarts`
- `detector.crash_loop_detected is True and detector.should_restart() is False`
- `window_span < 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
