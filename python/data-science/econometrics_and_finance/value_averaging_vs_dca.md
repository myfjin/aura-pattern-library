# value averaging vs dca

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(prices: list, invest_per_period: float) → float`

## What it does

Value Averaging vs Dollar Cost Averaging: compare final wealth.

Dollar Cost Averaging (DCA): invest fixed $ each period.
Value Averaging (VA): invest to reach a target portfolio value.
Core claim: final wealth compared; honest (may favor either).

## Guarantee

When it runs, value averaging vs dca guarantees final_dca > 0 and final_va > 0; 0.5 < ratio < 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_dca > 0 and final_va > 0`
- `0.5 < ratio < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
