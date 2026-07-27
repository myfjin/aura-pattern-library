# bayesian two segment changepoint

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(data: List[float], mean: float, var: float) → float`

## What it does

Bayesian two-segment changepoint: marginal-likelihood comparison over split points.

Core idea: compare model evidence for no-change vs change-at-t; find planted change location;
no-change data prefers single-segment model.

When to use: quality control, structural break detection, time-series anomalies.

## Guarantee

When it runs, bayesian two segment changepoint guarantees 20 <= split_detected <= 30; bf > 0; abs(bf_no_change) < 3.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `20 <= split_detected <= 30`
- `bf > 0`
- `abs(bf_no_change) < 3.0`
- `bf > abs(bf_no_change)`
- `0 < split_no_change < len(no_change_data)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
