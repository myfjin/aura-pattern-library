# atomic append

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(filename: ?, lockfile: ?, line: ?, results_dict: ?, writer_id: ?) → ?`

## What it does

atomic_append: serialize a read-modify-write "append" so concurrent writers never lose data.
Failure simulated: MANY processes each do read-the-whole-file → add their line → write it back
(a read-modify-write, the classic lost-update race). WITHOUT the lock, two writers that read the
same content each overwrite the other → lines are lost. WITH fcntl.flock serializing the whole
RMW, every writer's line survives.
Recovery asserted: all N distinct writer lines are present and the count == N. This assert FAILS
on a no-op lock — the RMW race drops lines (which is why we use N=20, not 2: pure O_APPEND would
hide the race, so the demo makes the lock genuinely necessary).

## Guarantee

When it runs, atomic append guarantees results.get(f'writer_{i}_done'); len(data_lines) == num_writers; len(set(data_lines)) == num_writers (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get(f'writer_{i}_done')`
- `len(data_lines) == num_writers`
- `len(set(data_lines)) == num_writers`
- `f'writer_{i}_line' in content`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def atomic_append(filename, lockfile, line, results_dict, writer_id):`
**Valid input:** `filename` and `lockfile` exist and are writable; `line` is a string; multiple concurrent writers are launched from separate processes.
**Core:** File-based read-modify-write append serialized by `fcntl.flock(LOCK_EX)` on a separate lockfile. Reads the whole file, appends `line`, writes the whole file, then releases the lock.
**Assert:** All 20 distinct writer lines survive the concurrent RMW and are present in the final file; no duplicates or torn lines.
**⚠️ Defect:** The entire file is rewritten on every append, which is O(n) write amplification and does not scale. A crash between truncate-and-write can lose all prior content; it is not crash-safe even with the lock.

---
*△ AURA Pattern Library — © Reality Optimizer*
