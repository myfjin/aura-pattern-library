# adversarial perturbation lite

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Adversarial Perturbation: gradient-sign attack on logistic classifier.

Builds a simple logistic classifier from scratch, computes adversarial perturbation
via gradient direction, and shows that adversarial perturbations flip predictions more
reliably than random noise of equivalent norm.

## Guarantee

When it runs, adversarial perturbation lite guarantees 0.5 < pred_orig < 0.8; pred_adv < 0.5; random_flips <= 5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.5 < pred_orig < 0.8`
- `pred_adv < 0.5`
- `random_flips <= 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
