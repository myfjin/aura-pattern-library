# checkpoint resume crc

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → u32`

## What it does

checkpoint_resume_crc — checkpoint + CRC; crash after N records, resume without dups.

Core idea: records are logged with a checkpoint marker every K records. On crash,
resume from the last checkpoint, replaying only the records between checkpoints.
CRC detects partial writes. THE LAW: log N records, truncate mid-record after
checkpoint M, resume, and assert each record is processed exactly once.
When to use: crash recovery with duplication avoidance, resumable operations.

## Guarantee

When it runs, checkpoint resume crc guarantees assert_eq!(log.recover().len(), 10, "clean recover returns all 10"); assert_eq!(recovered.len(), 7, "exactly the 7 committed records (0..=6) recover; torn 7th dropped"); assert_eq!(rec_corrupt.len(), 0, "CRC mismatch on record 0 stops recovery immediately") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(log.recover().len(), 10, "clean recover returns all 10")`
- `assert!(crashed.len() < buf.len(), "truncation actually shortened the image")`
- `assert_eq!(recovered.len(), 7, "exactly the 7 committed records (0..=6) recover; torn 7th dropped")`
- `assert_eq!(recovered[i], format!("record_{}", i).as_bytes().to_vec(), "record {i} exact, once")`
- `assert_eq!(rec_corrupt.len(), 0, "CRC mismatch on record 0 stops recovery immediately")`
- `assert_eq!(CheckpointLog::recover_from(&[]).len(), 0, "empty image recovers nothing")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
