# sliding window quantile

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], window_size: int, q: float) → float`

## What it does

Sliding window quantile via sorted window maintenance.
Core idea: keep the last k elements in order, sort when needed, compute exact quantile.
When: need exact quantile over fixed-size sliding window on a stream.

## Guarantee

When it runs, sliding window quantile guarantees abs(measured_quantile - true_quantile) < 1e-09 (proven by run).

**Checkable constraints:**

- `abs(measured_quantile - true_quantile) < 1e-09`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
