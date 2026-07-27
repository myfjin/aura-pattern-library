# authenticated message channel

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8], key: &[u8]) → u32`

## What it does

composes: frame-construct + keyed-checksum-append + transmit + verify-strip-decode

## Guarantee

When it runs, authenticated message channel guarantees assert_eq!(computed_mac, stored_mac, "MAC verification passed"); assert_eq!(payload, message, "Payload matches original"); assert_ne!(corrupted_payload_mac, corrupted_mac, "Corrupted payload detected") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(computed_mac, stored_mac, "MAC verification passed")`
- `assert_eq!(payload, message, "Payload matches original")`
- `assert_ne!(corrupted_payload_mac, corrupted_mac, "Corrupted payload detected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
