# discrete fourier transform

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float]) → List[Tuple[float, float]]`

## What it does

Discrete Fourier Transform (DFT) from Scratch.

Convert time-domain signal to frequency-domain via DFT.
DFT[k] = Σ x[n] * exp(-2πi*k*n/N).
We plant known frequencies in a signal and verify DFT recovers them.
Also verify Parseval's theorem: sum of squared signal = sum of squared DFT magnitudes / N.

## Guarantee

When it runs, discrete fourier transform guarantees mag_freq1 > 20; mag_freq2 > 10; parseval_error < 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mag_freq1 > 20`
- `mag_freq2 > 10`
- `parseval_error < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
