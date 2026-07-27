# tamper evident log

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → [u8`

## What it does

tamper_evident_log — HMAC-SHA256 hash-chained log; tampering detected at exact point.

Core idea: each log entry includes the HMAC of (previous_hash || current_record).
If any past entry is tampered, the chain breaks at that exact index. THE LAW: write
N entries, tamper one in the middle, verify, and assert the chain breaks exactly
at the tampered entry — proving the log detects and pinpoints corruption.
When to use: audit logs, blockchain-lite, integrity chains, tamper detection.

## Guarantee

When it runs, tamper evident log guarantees assert_eq!(idx, 2, "tamper at 2 breaks chain at 2"); assert_eq!(idx, 0, "tamper at 0 breaks chain at 0"); assert_eq!(idx, 4, "tamper at 4 breaks chain at 4") (proven by rustc-run).

**Checkable constraints:**

- `assert!(log.verify(key).is_ok(), "clean log verifies")`
- `assert_eq!(idx, 2, "tamper at 2 breaks chain at 2")`
- `assert_eq!(idx, 0, "tamper at 0 breaks chain at 0")`
- `assert_eq!(idx, 4, "tamper at 4 breaks chain at 4")`
- `assert!(empty_log.verify(key).is_ok(), "empty log verifies")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
