# crp table growth

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(n: int, alpha: float) → int`

## What it does

Chinese Restaurant Process (CRP): expected number of tables ≈ α·ln(n).

Core claim: E[#tables] ≈ α·ln(n) within tolerance (planted α).

## Guarantee

When it runs, crp table growth guarantees abs(mean_tables - expected) < alpha * 2 (proven by run).

**Checkable constraints:**

- `abs(mean_tables - expected) < alpha * 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
