# weighted reservoir ares

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[Tuple], k: int) → List`

## What it does

Weighted reservoir sampling -- Efraimidis-Spirakis A-Res.
Core idea: give each item a key u**(1/weight) with u ~ Uniform(0,1); keep the k items
with the largest keys in a min-heap. The resulting sample is a weighted sample without
replacement: P(item in sample) grows with its weight.
When: sample k items proportional to weight in one pass over a weighted stream.

## Guarantee

When it runs, weighted reservoir ares guarantees max_dev < 0.015; counts == sorted(counts) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `max_dev < 0.015`
- `counts == sorted(counts)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
