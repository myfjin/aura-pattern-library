# caliper matching

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x1: float, x2: float) → float`

## What it does

Caliper matching: restrict nearest-neighbor matches to within a caliper (distance threshold).

Bias-variance tradeoff: uncalipered NN can match distant observations (high bias);
caliper trades some matches for lower bias. Core claim: bias vs uncalipered measured,
unmatched rate honestly reported.

## Guarantee

When it runs, caliper matching guarantees len(calipered) <= len(uncalipered); unmatch_cal >= unmatch_uncal; bias_cal <= bias_uncal * 1.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(calipered) <= len(uncalipered)`
- `unmatch_cal >= unmatch_uncal`
- `bias_cal <= bias_uncal * 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
