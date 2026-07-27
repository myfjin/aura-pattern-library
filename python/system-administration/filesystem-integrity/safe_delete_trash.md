# safe delete trash

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(file_path: str, trash_dir: str) → ?`

## What it does

safe_delete_trash: delete files to trash (not permanent deletion).
Failure simulated: delete a file via trash move; assert file is gone from original location
but recoverable from trash. Prevent permanent data loss via trash buffer.
Recovery asserted: file removed from source; file exists in trash; can be restored from trash.
Pattern's own delete-to-trash function is called.

## Guarantee

When it runs, safe delete trash guarantees result == expected_content; recovered_result == expected_content; Path(source_file).exists() (proven by run).

**Checkable constraints:**

- `Path(source_file).exists()`
- `not Path(source_file).exists()`
- `Path(trash_path).exists()`
- `result == expected_content`
- `len(trash_files) == 1`
- `trash_files[0] == os.path.basename(trash_path)`
- `recovered_result == expected_content`
- `len(os.listdir(trash_dir)) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
