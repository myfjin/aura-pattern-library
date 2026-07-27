# atomic snapshot

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(source_path: str, snapshot_path: str) → ?`

## What it does

atomic_snapshot: take an atomic snapshot of a file at a point in time.
Failure simulated: snapshot a live file, modify the original, verify snapshot is unchanged.
The snapshot is taken via temp-write + rename, ensuring atomicity.
Recovery asserted: snapshot holds the original bytes exactly; subsequent modifications
to the source don't affect the snapshot. Pattern's own snapshot function is called.

## Guarantee

When it runs, atomic snapshot guarantees result == expected_original; result == expected_original; result != modified_data (proven by run).

**Checkable constraints:**

- `result == expected_original`
- `result == expected_original`
- `result != modified_data`
- `len(result) == len(expected_original)`
- `len(result) != len(modified_data)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
