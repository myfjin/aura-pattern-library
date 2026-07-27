# doubly robust aipw

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x: float) → float`

## What it does

Doubly Robust AIPW: consistent if EITHER the outcome model OR the propensity is correct.

AIPW = (1/n) Σ [ μ₁(Xᵢ) − μ₀(Xᵢ) + Tᵢ(Yᵢ−μ₁)/eᵢ − (1−Tᵢ)(Yᵢ−μ₀)/(1−eᵢ) ].
Core claim (double robustness): it recovers the true ATE in BOTH
  Case 1 — CORRECT outcome model, WRONG propensity, and
  Case 2 — WRONG outcome model, CORRECT propensity.

## Guarantee

When it runs, doubly robust aipw guarantees abs(aipw_c1 - 2.0) < 0.4; abs(aipw_c2 - 2.0) < 0.5 (proven by run).

**Checkable constraints:**

- `abs(aipw_c1 - 2.0) < 0.4`
- `abs(aipw_c2 - 2.0) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
