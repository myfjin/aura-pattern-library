# lsm tree

**Language:** Python · **Sphere:** programming · **Category:** Persistence

**Signature:** `() → None`

## What it does

LSM-Tree Engine Implementation

A complete implementation of an LSM-Tree (Log-Structured Merge-Tree) storage engine
with MemTable, SSTable, and compaction functionality.

## Guarantee

When it runs, lsm tree guarantees lsm.get('k03') == 30; lsm.get('k12') == 120; len(lsm.sstables) >= 2 (proven by run).

**Checkable constraints:**

- `len(lsm.sstables) >= 2`
- `lsm.get(f'k{i:02d}') == i * 10`
- `lsm.get('ghost') is None`
- `lsm.get('k03') == 30`
- `lsm.get('k12') == 120`
- `lsm.get('k01') == 'fresh'`
- `lsm.get('k02') is None`
- `lsm.get('k02') is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
