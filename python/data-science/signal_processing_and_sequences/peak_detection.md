# peak detection

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float], prominence_threshold: float) → List[int]`

## What it does

Peak Detection via Prominence.

Find local maxima in a signal using prominence: height above the baseline
(minimum of the valleys to the left and right).
Detect planted peaks; reject noise bumps that don't meet prominence threshold.

## Guarantee

When it runs, peak detection guarantees 25 in detected_peaks; 75 in detected_peaks; noise_detections <= 1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `25 in detected_peaks`
- `75 in detected_peaks`
- `noise_detections <= 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
