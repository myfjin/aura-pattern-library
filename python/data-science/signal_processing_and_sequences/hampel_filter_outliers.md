# hampel filter outliers

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float], window_size: int, k: float) → List[float]`

## Guarantee

When it runs, hampel filter outliers guarantees mse_filtered < mse_noisy; spike_removals >= 3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mse_filtered < mse_noisy`
- `spike_removals >= 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
