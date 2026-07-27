# exponential histogram count

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[int], window: int, eps: float) → int`

## Guarantee

When it runs, exponential histogram count guarantees rel <= eps + 1e-09; _bucket_count(stream, N, eps) < N // 10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rel <= eps + 1e-09`
- `_bucket_count(stream, N, eps) < N // 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
