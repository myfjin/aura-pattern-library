# atomic write temp rename

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

## What it does

atomic_write_temp_rename: write atomically by writing to a temp file, then atomic rename.
Failure simulated (the REAL one): a writer is killed AFTER the temp is fully written but
BEFORE the rename. Recovery asserted: the target is left completely untouched — still the
intact OLD content, never torn/partial/new.

## Guarantee

When it runs, atomic write temp rename guarantees Path(target).read_bytes() == expected_old; after_crash == expected_old; result == expected_new and result != expected_old (proven by run on the SYS original).

**Checkable constraints:**

- `Path(target).read_bytes() == expected_old`
- `got`
- `after_crash == expected_old`
- `result == expected_new and result != expected_old`
- `not [f for f in os.listdir(tmpdir) if f.startswith('tmp')]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: hard, chaos, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
