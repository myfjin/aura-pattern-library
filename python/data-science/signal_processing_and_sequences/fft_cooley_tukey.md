# fft cooley tukey

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float]) → List[Tuple[float, float]]`

## What it does

FFT via Cooley-Tukey Algorithm.

Recursive divide-and-conquer FFT: O(N log N) vs naive DFT O(N²).
Works on power-of-2 lengths. FFT should produce same result as naive DFT,
and operation count should be measurably lower (on fixed input).

## Guarantee

When it runs, fft cooley tukey guarantees max_error < 1e-06; ops_fft < ops_naive (weak-grade: directional, proven by run).

**Checkable constraints:**

- `max_error < 1e-06`
- `ops_fft < ops_naive`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
