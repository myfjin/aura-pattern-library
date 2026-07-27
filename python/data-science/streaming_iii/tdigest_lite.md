# tdigest lite

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], compression: float) → Tuple[float, float]`

## Guarantee

When it runs, tdigest lite guarantees e99 < 1.0 and e01 < 1.0; len(centroids) < 0.1 * len(stream); centroids[-1][1] < centroids[len(centroids) // 2][1] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `e99 < 1.0 and e01 < 1.0`
- `len(centroids) < 0.1 * len(stream)`
- `centroids[-1][1] < centroids[len(centroids) // 2][1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
