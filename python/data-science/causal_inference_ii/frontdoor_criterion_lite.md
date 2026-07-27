# frontdoor criterion lite

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x: List[float], y: List[float]) → float`

## What it does

Frontdoor criterion: identify a causal effect when the backdoor is unblockable.

DAG: U → X → M → Y and U → Y (hidden confounder U on X and Y; the backdoor through U
cannot be closed because U is unobserved). The frontdoor path X→M→Y still identifies the
effect:  effect = β(X→M) × β(M→Y adjusting for X). The M→Y coefficient MUST adjust for X
(conditioning on X blocks the M↔Y backdoor through U) — the unadjusted M→Y slope leaves
the confounding in.
Core claim: frontdoor recovers the true causal effect; the naive X→Y slope is biased by U.

## Guarantee

When it runs, frontdoor criterion lite guarantees abs(frontdoor - true_effect) < 0.6; abs(frontdoor - true_effect) < abs(naive - true_effect); abs(naive - true_effect) > 0.3 (proven by run).

**Checkable constraints:**

- `abs(frontdoor - true_effect) < 0.6`
- `abs(naive - true_effect) > 0.3`
- `abs(frontdoor - true_effect) < abs(naive - true_effect)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
