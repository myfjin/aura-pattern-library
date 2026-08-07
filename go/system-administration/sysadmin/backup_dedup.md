# backup dedup

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 13 · Backup & disaster recovery

## What it does

backup_dedup: detect and skip duplicate content in backups.

## Guarantee

When it runs, backup dedup guarantees max_refs == 3; chunk_count[shared_hash] == 3; len(stored_chunks_list) >= 1 (proven by run on the SYS original).

**Checkable constraints:**

- `len(stored_chunks_list) >= 1`
- `max_refs == 3`
- `(restore_base / 'file1.txt').read_bytes() == chunk_data + b'_file1'`
- `(restore_base / 'file2.txt').read_bytes() == chunk_data + b'_file2'`
- `(restore_base / 'file3.txt').read_bytes() == chunk_data + b'_file3'`
- `chunk_count[shared_hash] == 3`
- `rehash != shared_hash`
- `restored != (src / fname).read_bytes()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def chunk_file(path, chunk_size=4096):`, `def backup_with_dedup(src_dir, backup_dir, chunk_size=4096):`, `def restore_from_dedup(backup_dir, restore_dir):`, `def test_backup_dedup():`
**Valid input:** Source directory contains readable files; `chunk_size` is positive.
**Core:** Content-defined deduplicating backup. Files are split into fixed-size chunks, chunks are stored content-addressed by SHA-256, and a manifest records per-file chunk lists. Restore reassembles files from chunks.
**Assert:** Three files sharing a 4 KB chunk store only one physical chunk with three references; restore reproduces originals; corrupting the shared chunk breaks the content-address invariant and propagates to every referencing file.
**⚠️ Defect:** Fixed-size chunking means small boundary shifts duplicate all subsequent chunks. The store does not verify chunk hashes on read, so silent corruption is only detectable if a caller re-hashes; the restore fails only if the chunk is outright missing.

---
*△ AURA Pattern Library — © Reality Optimizer*
