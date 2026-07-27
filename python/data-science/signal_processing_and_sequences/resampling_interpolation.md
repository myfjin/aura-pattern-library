# resampling interpolation

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float], factor: int) → List[float]`

## What it does

Resampling and Interpolation.

Upsample or downsample a time series via interpolation.
Demonstrate linear interpolation and nearest-neighbor.
On smooth signals, linear should outperform nearest-neighbor (lower RMSE).

## Guarantee

When it runs, resampling interpolation guarantees len(downsampled) == expected_length; rmse_linear < rmse_nearest (proven by run).

**Checkable constraints:**

- `rmse_linear < rmse_nearest`
- `len(downsampled) == expected_length`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
