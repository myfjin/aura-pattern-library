# reproducible build check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(sources: dict) → ?`

## What it does

reproducible_build_check: build twice with identical inputs, verify byte-for-byte output
matches. Then mutate one input and verify the build differs. This detects non-determinism
and ensures builds are truly deterministic.

## Guarantee

When it runs, reproducible build check guarantees artifact1 == artifact2; hash1 == hash2; artifact3 != artifact1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `artifact1 == artifact2`
- `hash1 == hash2`
- `artifact3 != artifact1`
- `hash3 != hash1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
