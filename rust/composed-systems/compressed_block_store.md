# compressed block store

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → Vec<u8>`

## What it does

composes: rle-encode + checksum-compute + store + read-back-decode-verify

## Guarantee

When it runs, compressed block store guarantees assert_eq!(checksum, stored_checksum, "Checksum preserved"); assert_eq!(decoded, original, "Roundtrip successful"); assert_ne!(checksum, corrupted_checksum, "Corrupted data detected by checksum") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(checksum, stored_checksum, "Checksum preserved")`
- `assert_eq!(decoded, original, "Roundtrip successful")`
- `assert_ne!(checksum, corrupted_checksum, "Corrupted data detected by checksum")`
- `assert_eq!(decoded_restored, original, "Restored data decodes correctly")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
