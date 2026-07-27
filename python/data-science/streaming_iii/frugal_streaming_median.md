# frugal streaming median

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], step: float) → float`

## What it does

Frugal streaming median (Ma, Muthukrishnan, Sandler) -- Frugal-1, one integer of state.
Core idea: keep a single estimate m; for each element, with a coin gated by the target
quantile q=0.5, step m up by 1 if the element is above it, down by 1 if below. At the
quantile the up-pressure and down-pressure balance, so m random-walks to the true median.
When: estimate a quantile in O(1) memory on an unbounded stream.

## Guarantee

When it runs, frugal streaming median guarantees err < 3.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `err < 3.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
