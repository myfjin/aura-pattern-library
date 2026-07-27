# fsync durability

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(path: str, data: bytes) → ?`

## What it does

fsync_durability: write data then fsync to flush it to stable storage before returning.
Failure defended against: process/power death after write() but before the OS flushes the
page cache — the data would be lost on a crash without fsync.
HONEST SCOPE: true durability-across-power-loss cannot be demonstrated in-process (it needs an
actual crash/power cut). What IS proven here: (1) durable_write ACTUALLY INVOKES os.fsync on
the file's fd (a no-fsync no-op is caught — os.fsync is monkeypatched to record the call), in
the correct order (flush before fsync), and (2) the bytes are exactly correct across write
cycles. Recovery asserted: fsync was called on the written fd; without it the assert fails.

## Guarantee

When it runs, fsync durability guarantees result == expected_v1 and len(result) == len(expected_v1); result == expected_v2; result != expected_v1 and result[:11] == b'durable_v2_' (proven by run).

**Checkable constraints:**

- `len(fsync_calls) == 1`
- `isinstance(fsync_calls[0], int) and fsync_calls[0] >= 0`
- `result == expected_v1 and len(result) == len(expected_v1)`
- `result == expected_v2`
- `result != expected_v1 and result[:11] == b'durable_v2_'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
