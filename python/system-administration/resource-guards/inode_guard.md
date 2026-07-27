# inode guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(inode_cap: int) → ?`

## What it does

Inode guard: refuses file creation past inode limit.
Failure simulated: create 10000 files with cap=100; assert guard refuses
creation when inode count reaches cap, peak ≤ cap.

## Guarantee

When it runs, inode guard guarantees peak <= 100; num_refused >= 9900; num_created <= 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak <= 100`
- `num_refused >= 9900`
- `num_created <= 100`
- `num_refused > num_created * 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
