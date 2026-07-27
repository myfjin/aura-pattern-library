# backdoor vs collider adjustment

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x: List[float], y: List[float]) → Tuple[float, float]`

## What it does

Backdoor vs Collider adjustment: adjusting backdoor removes confounding bias;
adjusting a collider CREATES bias (collider bias, Berkson's paradox).

DAG: X ← U → Y (backdoor open; adjust U to close it).
DAG: X → V ← Y (collider; adjusting V opens a spurious path).
Core claim: backdoor adjustment recovers effect; collider adjustment makes bias WORSE.

## Guarantee

When it runs, backdoor vs collider adjustment guarantees abs(adjusted_backdoor - true_effect) < 0.3; abs(unadjusted_backdoor - true_effect) > 0.3; abs(adjusted_collider) > abs(unadjusted_collider) * 1.5 (proven by run).

**Checkable constraints:**

- `abs(unadjusted_backdoor - true_effect) > 0.3`
- `abs(adjusted_backdoor - true_effect) < 0.3`
- `abs(adjusted_collider) > abs(unadjusted_collider) * 1.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
