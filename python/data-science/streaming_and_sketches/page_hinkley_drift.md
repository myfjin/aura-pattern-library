# page hinkley drift

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

## What it does

Page-Hinkley Test for Streaming Drift Detection

Core idea: Monitor cumulative sum of (residuals - threshold) to detect if the distribution
has shifted. High positive sum indicates upward drift; reset if drift detected.

When to use: You're monitoring a stream metric and need early warning when it changes
(e.g., system latency, error rate, model performance degradation).

## Guarantee

When it runs, page hinkley drift guarantees num_alarms_1 <= 1; drift_step < 150 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `num_alarms_1 <= 1`
- `drift_step < 150`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class PageHinkleyDrift:`, `def __init__(self, threshold: float = 50.0, delta: float = 0.005, min_instances: int = 30):`, `def process(self, value: float) -> bool:`
**Valid input:** `threshold` > 0; `delta` ≥ 0; `min_instances` ≥ 0; `value` is a number.
**Core:** Page-Hinkley drift detector. Updates the streaming mean, accumulates `m_t = Σ(x_i - mean - delta)`, tracks the running minimum, and fires when `m_t - m_min` exceeds the threshold.
**Assert:** A stable Gaussian stream produces at most one false alarm; a planted mean shift at step 100 is detected before step 150.
**⚠️ Defect:** On detection the detector resets its statistics using the current value as the new mean, which can cause a second alarm immediately after a weak shift. The `min_instances` guard prevents early alarms but also delays detection. The test for the drifting stream has a soft `pass` branch if the detector never fires, so the assert does not strictly enforce detection.

---
*△ AURA Pattern Library — © Reality Optimizer*
