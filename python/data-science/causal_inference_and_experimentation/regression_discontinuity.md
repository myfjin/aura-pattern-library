# regression discontinuity

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(x_window: List[float], y_window: List[float]) → Tuple[float, float]`

## What it does

Regression Discontinuity (RD).

Treatment is assigned by a cutoff rule on a running variable: T=1 if X >= cutoff.
There is a discontinuity in the outcome at the cutoff: E[Y | X=c+] - E[Y | X=c-] = ATE.
We plant a cutoff effect and smooth underlying relationship; RD recovers the effect.

## Guarantee

When it runs, regression discontinuity guarantees bias < 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bias < 1.0`
- `len(left_indices) >= 20`
- `len(right_indices) >= 20`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
