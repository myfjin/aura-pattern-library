# convolution filtering

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float], kernel: List[float]) → List[float]`

## What it does

Convolution and Filtering.

Convolve a signal with a kernel via discrete convolution: y[n] = Σ x[k] * h[n-k].
Demonstrate smoothing (moving average kernel) and edge detection (difference kernel).
Verify that smoothing reduces noise and difference kernel detects transitions.

## Guarantee

When it runs, convolution filtering guarantees mse_smoothed < mse_noisy (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mse_smoothed < mse_noisy`
- `edge_is_near_transition`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
