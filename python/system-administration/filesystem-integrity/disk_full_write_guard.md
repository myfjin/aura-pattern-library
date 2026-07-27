# disk full write guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(path: str, content: bytes) → ?`

## What it does

disk_full_write_guard: refuse writes when disk space is exhausted or quota exceeded.
Failure simulated: attempt to write past disk quota; guard should refuse; existing
data remains intact. Guard trips BEFORE exhaustion, not after.
Recovery asserted: write is blocked when it would exceed quota; existing data untouched;
no partial/torn writes. Pattern's own guard function is called.

## Guarantee

When it runs, disk full write guard guarantees guard.get_used() == expected_file1_size; guard.get_used() == expected_quota; guard.get_used() == expected_quota (proven by run).

**Checkable constraints:**

- `Path(file1_path).exists()`
- `guard.get_used() == expected_file1_size`
- `guard.remaining() == expected_quota - expected_file1_size`
- `Path(file2_path).exists()`
- `guard.get_used() == expected_file1_size + expected_file2_size`
- `Path(file3_path).exists()`
- `guard.get_used() == expected_quota`
- `guard.remaining() == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
