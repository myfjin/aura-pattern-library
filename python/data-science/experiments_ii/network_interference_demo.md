# network interference demo

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(n: int, treatment: List[int], effect_direct: float, effect_spillover: float) → List[float]`

## What it does

Network interference: SUTVA violation where spillover through a graph biases ATE.

Treatment on one user affects neighbors (e.g., social network). Naive ATE (individual
randomization) is biased due to spillover. Core claim: spillover biases naive ATE by
measured amount; the classic trap, quantified.

## Guarantee

When it runs, network interference demo guarantees ate_high < ate_low; abs(ate_high - ate_low) > 0.2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ate_high < ate_low`
- `abs(ate_high - ate_low) > 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
