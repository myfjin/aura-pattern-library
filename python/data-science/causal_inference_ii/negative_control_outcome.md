# negative control outcome

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x: List[float], y: List[float]) → float`

## What it does

Negative control outcome: a known-null outcome should remain null under clean analysis
but light up under planted residual confounding. Detector for unobserved confounding.

Core claim: null outcome stays null under correct analysis; null outcome becomes non-null
when unmeasured confounder is present — both directions demonstrated.

## Guarantee

When it runs, negative control outcome guarantees abs(effect_real_clean) > 1.0; abs(effect_null_clean) < 0.5; abs(effect_null_conf) > 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(effect_real_clean) > 1.0`
- `abs(effect_null_clean) < 0.5`
- `abs(effect_null_conf) > 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
