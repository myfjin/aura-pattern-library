# gk quantile summary

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], epsilon: float, q: float) → float`

## What it does

Greenwald-Khanna ε-approximate quantile summary.
Core idea: maintain sorted list of (v, g, delta) tuples; compress on overflow to ε-error guarantees.
When: need approximate quantiles with bounded space and error guarantees on large streams.

## Guarantee

When it runs, gk quantile summary guarantees abs(measured_quantile - true_quantile) <= error_bound + 1e-06 (proven by run).

**Checkable constraints:**

- `abs(measured_quantile - true_quantile) <= error_bound + 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
