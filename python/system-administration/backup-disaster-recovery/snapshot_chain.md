# snapshot chain

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(src_dir: Path, snapshot_dir: Path, snapshot_id: str, parent_id: None) → ?`

## What it does

snapshot_chain: maintain chain of snapshots with parent references.

## Guarantee

When it runs, snapshot chain guarantees snap1['id'] == 'snap1'; snap1['parent'] is None; 'file1.txt' in snap1['files'] and 'file2.txt' in snap1['files'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `snap1['id'] == 'snap1'`
- `snap1['parent'] is None`
- `len(snap1['files']) == 2`
- `'file1.txt' in snap1['files'] and 'file2.txt' in snap1['files']`
- `snap2['parent'] == 'snap1'`
- `snap3['parent'] == 'snap2'`
- `len(snap3['files']) == 3`
- `(restore1 / 'file1.txt').read_text() == 'content_v1'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def create_snapshot(src_dir, snapshot_dir, snapshot_id, parent_id=None):`, `def restore_from_snapshot(snapshot_dir, snapshot_id, restore_dir):`, `def test_snapshot_chain():`
**Valid input:** Source directory exists; snapshot IDs are unique; `parent_id` is either `None` or an existing snapshot ID.
**Core:** Copy-on-write-style snapshot chain. Each snapshot stores a manifest with its parent and content-addressed files; restore walks the parent chain from newest to oldest, applying older snapshots first so newer ones override.
**Assert:** Snapshots link `snap1 <- snap2 <- snap3`; restoring from each snapshot yields the correct point-in-time content, including inherited files from parents.
**⚠️ Defect:** True deduplication against the parent is not implemented—the comment says it would check the parent's manifest but the code stores every file in every snapshot. The restore chain stops if a snapshot directory is missing, even if enough data exists in descendants. Cycle detection only breaks on revisiting an ID and does not report an error.

---
*△ AURA Pattern Library — © Reality Optimizer*
