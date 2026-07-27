# clock skew detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(wall_time: float) → ?`

## What it does

Detect backward wall-clock jumps from a stream of time samples.

SkewDetector records successive wall-clock readings and flags any sample that
is earlier than the previous one (a backward jump), accumulating the count and
total magnitude of skew seen. Use it to catch NTP step-backs or manual clock
resets that would break time-based logic. Guarantees (self-test oracle): a
backward step is detected with its exact magnitude, multiple skews accumulate
correctly, and purely forward progression never raises a false positive.

## Guarantee

When it runs, clock skew detect guarantees detector.get_total_skew() == 7.0; detector.get_total_skew() == 5.0; detector.get_skew_count() == 2 (proven by run).

**Checkable constraints:**

- `detector.sample(1000.0) is False`
- `detector.sample(1001.0) is False`
- `detector.sample(1002.0) is False`
- `skew_detected is False`
- `skew_detected is True`
- `detector.get_skew_count() == 1`
- `detector.get_total_skew() == 7.0`
- `detector.get_skew_count() == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
