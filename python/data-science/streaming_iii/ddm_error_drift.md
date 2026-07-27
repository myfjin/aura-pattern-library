# ddm error drift

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(error_stream: List[int], min_samples: int) → Tuple[bool, int]`

## What it does

DDM -- Drift Detection Method (Gama, Medas, Castillo, Rodrigues 2004).
Core idea: as a classifier's binary error stream arrives, track p_i (running error rate)
and s_i = sqrt(p_i(1-p_i)/i). Keep the minimum of (p_i + s_i) ever seen (p_min, s_min):
that marks the best the model has been. Signal WARNING at p_i+s_i >= p_min+2*s_min and
DRIFT at p_i+s_i >= p_min+3*s_min -- a statistical control chart, not "later > earlier".
When: detect that a classifier's error rate has significantly worsened, online.

## Guarantee

When it runs, ddm error drift guarantees det_s is False; det_d is True and idx_d >= 400 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `det_s is False`
- `det_d is True and idx_d >= 400`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
