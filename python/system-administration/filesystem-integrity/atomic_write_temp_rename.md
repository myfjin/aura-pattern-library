# atomic write temp rename

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(target_path: str, content: bytes) → ?`

## What it does

atomic_write_temp_rename: write atomically by writing to a temp file, then atomic rename.
Failure simulated (the REAL one): a writer is SIGKILL'd AFTER the temp is fully written but
BEFORE the rename. Recovery asserted: the target is left completely untouched — still the
intact OLD content, never torn/partial/new. That is the all-or-nothing guarantee of
temp+rename, and the assert FAILS on a non-atomic direct-overwrite (which, killed mid-write,
would leave the target truncated). A second run does a clean atomic replace (old→new).

## Guarantee

When it runs, atomic write temp rename guarantees Path(target).read_bytes() == expected_old; after_crash == expected_old; result == expected_new and result != expected_old (proven by run).

**Checkable constraints:**

- `Path(target).read_bytes() == expected_old`
- `got`
- `after_crash == expected_old`
- `result == expected_new and result != expected_old`
- `not [f for f in os.listdir(tmpdir) if f.startswith('tmp')]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
