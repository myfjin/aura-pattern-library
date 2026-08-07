# backup catalog

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 13 · Backup & disaster recovery

## What it does

backup_catalog: maintain and search backup metadata.

## Guarantee

When it runs, backup catalog guarantees backup1_entry['file_count'] == 2; catalog['backup_1']['file_count'] == 2; catalog['backup_2']['file_count'] == 2 (proven by run on the SYS original).

**Checkable constraints:**

- `len(catalog) == 3`
- `'backup_1' in catalog`
- `'backup_2' in catalog`
- `'backup_3' in catalog`
- `backup1_entry['status'] == 'complete'`
- `backup1_entry['file_count'] == 2`
- `backup1_entry['size_bytes'] > 0`
- `catalog['backup_1']['file_count'] == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def create_backup_entry(backup_id, metadata):`, `def build_backup_catalog(backup_dir, catalog_dir):`, `def search_catalog(catalog_dir, query):`, `def get_backup_stats(catalog_dir):`, `def test_backup_catalog():`
**Valid input:** `backup_dir` contains directories matching `backup_*`; `catalog_dir` is writable; `query` is a lowercase substring or retention tag.
**Core:** Scans backup directories, builds `catalog.json` and `summary.json` with per-backup size/file-count metadata plus totals, and supports search by ID or retention tag.
**Assert:** Three synthetic backups produce a 3-entry catalog with proportional sizes; search finds exact and substring matches; summary total size matches the sum of entries.
**⚠️ Defect:** `search_catalog` only checks the literal query against the backup ID and the `retention_tag` field; there is no full-text metadata search. The catalog is rebuilt from scratch every call rather than incrementally updated, so large backup trees are rescanned repeatedly.

---
*△ AURA Pattern Library — © Reality Optimizer*
