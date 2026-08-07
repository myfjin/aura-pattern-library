# tdigest lite

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], compression: float) → Tuple[float, float]`

## What it does

t-digest (merging variant) -- accurate tail quantiles in small space.
Core idea: merge sorted points into centroids under a q-dependent SIZE BOUND
limit(q) = 4*N*delta*q*(1-q). Near the tails (q->0 or 1) the bound shrinks to ~0, so tail
centroids stay tiny (near-exact), while mid-distribution centroids may grow large. This
tail-scaling is the DEFINING move of a t-digest -- it is why p99/p01 are far more accurate
than a fixed-width sketch would give.
When: estimate extreme quantiles (p99, p01, ...) from a large stream in bounded memory.

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
