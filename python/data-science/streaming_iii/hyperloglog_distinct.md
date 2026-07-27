# hyperloglog distinct

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List, p: int) → int`

## What it does

HyperLogLog cardinality estimation (Flajolet et al.).
Core idea: hash each element to 64 bits; the first p bits pick a register, the rank
(position of the leftmost 1) in the remaining bits updates that register with its max;
estimate distinct count from the harmonic mean of 2^register across m = 2^p registers.
When: count distinct elements on massive streams in fixed tiny memory (m registers).
Standard error is 1.04/sqrt(m); with p=12 (m=4096) that is ~1.6%.

## Guarantee

When it runs, hyperloglog distinct guarantees rel_err < 0.05; rel_err < naive_rel / 10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rel_err < 0.05`
- `rel_err < naive_rel / 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
