# peak detection

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Signal Processing & Sequences

## What it does

peak_detection.cpp
Peak detection via prominence.

## Guarantee

When it runs, peak detection guarantees 25 in detected_peaks; 75 in detected_peaks; noise_detections <= 1 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `25 in detected_peaks`
- `75 in detected_peaks`
- `noise_detections <= 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
