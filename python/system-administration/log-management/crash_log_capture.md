# crash log capture

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str, crash_after_n: int) → ?`

## What it does

Crash log capture: recover from a torn log write (the artifact a crash mid-write leaves).
Failure simulated: write N complete JSON lines then a TRUNCATED line (exactly what a process
killed mid-write leaves on disk). Defended outcome: the incomplete line is skipped on parse,
the N complete entries are recovered intact — no gaps, crash entry absent.

## Guarantee

When it runs, crash log capture guarantees malformed >= 1; malformed == 1; 'seq' in entry (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(entries) >= 3`
- `len(entries) <= 5`
- `malformed >= 1`
- `malformed == 1`
- `'seq' in entry`
- `entry['seq'] == i`
- `crash_idx not in seqs`
- `len(seqs) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
