# wal append replay

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(record: &[u8]) → ?`

## What it does

wal_append_replay — write-ahead log with CRC-32 framing, crash simulation, and recovery.

Core idea: each record is prefixed with length + followed by CRC32. A crash mid-write
leaves a torn tail. On replay, valid records are recovered exactly; a CRC mismatch
signals the torn record. THE LAW: write N records, truncate the file at a random point
mid-record, replay the corrupted file, and assert exactly the committed records come back
— proving the log survives the integrated disaster of an incomplete write.
When to use: durability guarantees, crash recovery, transactional logs.

## Guarantee

When it runs, wal append replay guarantees assert_eq!(recovered.len(), 3, "should recover exactly 3 intact records"); assert_eq!(recovered[0], b"rec0".to_vec()); assert_eq!(recovered[1], b"rec1".to_vec()) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(recovered.len(), 3, "should recover exactly 3 intact records")`
- `assert_eq!(recovered[0], b"rec0".to_vec())`
- `assert_eq!(recovered[1], b"rec1".to_vec())`
- `assert_eq!(recovered[2], b"rec2".to_vec())`
- `assert_eq!(torn.len(), 1, "should detect exactly one torn tail")`
- `assert_eq!(torn[0], 36, "torn tail at 4th record")`
- `assert_eq!(rec2.len(), 0, "empty log replays empty")`
- `assert_eq!(torn2.len(), 0, "no torn tail in empty log")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
