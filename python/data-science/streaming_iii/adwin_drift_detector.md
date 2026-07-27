# adwin drift detector

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], delta: float) → Tuple[bool, int]`

## What it does

ADWIN0 adaptive-windowing drift detector (Bifet & Gavalda, 2007).
Core idea: keep a window of recent values; after each arrival, try EVERY split of the
window into an older part W0 and newer part W1. If |mean(W0) - mean(W1)| exceeds the
variance-aware Hoeffding cut bound e_cut(delta), a real change is declared and the older
part is dropped. delta bounds the false-positive rate; the bound is NOT an arbitrary
fraction of the std -- it is derived from delta and the window sizes.
When: detect distribution shift online with a provable false-alarm guarantee.
Values are assumed in [0,1] (e.g. a stream of classification errors) -- ADWIN's setting.

## Guarantee

When it runs, adwin drift detector guarantees det_s is False; det_d is True; 300 <= idx_d <= 400 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `det_s is False`
- `det_d is True`
- `300 <= idx_d <= 400`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
