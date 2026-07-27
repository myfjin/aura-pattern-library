# signed snapshot

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → [u8`

## What it does

signed_snapshot — serialize a state map + HMAC-sign; tampering fails verify; restore equals original.

Core idea: serialize a map into JSON-like format, compute HMAC-SHA256 over it,
store (data, HMAC). On restore, recompute HMAC and verify it matches; if any field
is tampered, HMAC fails. THE LAW: snapshot → tamper one field → restore → verify
fails, proving integrity protection.
When to use: integrity-checked state snapshots, signed configurations, state export/import.

## Guarantee

When it runs, signed snapshot guarantees assert_eq!(restored, original.to_vec(), "restore equals original"); assert_eq!(empty_snap.restore(), vec![], "empty restore is empty") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(snap.verify(key), "fresh snapshot verifies")`
- `assert_eq!(restored, original.to_vec(), "restore equals original")`
- `assert!(!snap_tampered.verify(key), "tampered snapshot fails verify")`
- `assert!(!snap2.verify(wrong_key), "wrong key fails verify")`
- `assert!(empty_snap.verify(key), "empty snapshot verifies")`
- `assert_eq!(empty_snap.restore(), vec![], "empty restore is empty")`
- `assert!(!snap3.verify(key), "multi-point tamper fails")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
