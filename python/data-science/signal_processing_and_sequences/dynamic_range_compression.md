# dynamic range compression

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(values: List[float], offset: float) → List[float]`

## What it does

Dynamic Range Compression via Logarithm and μ-Law.

Compress large dynamic range (e.g., audio amplitudes or intensity values)
into a narrower range while preserving relative differences at small scales.
Both log compression and μ-law compression should be invertible
and reduce the dynamic range.

## Guarantee

When it runs, dynamic range compression guarantees dr_log < dr_original; dr_mu < dr_original; log_reconstruction_error < 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `dr_log < dr_original`
- `dr_mu < dr_original`
- `log_reconstruction_error < 0.05`
- `mu_reconstruction_error < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
