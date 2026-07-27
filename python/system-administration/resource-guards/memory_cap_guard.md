# memory cap guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(cap_mb: int) → ?`

## What it does

Memory cap guard: refuses allocations past limit, keeps peak ≤ cap.
Failure simulated: allocate 100 chunks × 10MB each (1GB total) with cap=256MB;
assert guard raises MemoryError before peak reaches 1GB, and peak ≤ cap.

## Guarantee

When it runs, memory cap guard guarantees peak_mb <= 256; num_refused >= 70; num_succeeded <= 30 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak_mb <= 256`
- `num_refused >= 70`
- `num_succeeded <= 30`
- `num_refused > num_succeeded`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
