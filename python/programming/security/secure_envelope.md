# secure envelope

**Language:** Python · **Sphere:** programming · **Category:** Security

## What it does

Secure Envelope Module

This module provides a secure envelope implementation using HMAC-SHA256 for
message authentication and integrity verification. It includes key rotation
capabilities and tamper detection.

## Guarantee

When it runs, secure envelope guarantees sum((m[1]['n'] for m in opened)) == 3; message == messages[i]; metadata == {'sender': 'user1', 'n': i} (proven by run).

**Checkable constraints:**

- `message == messages[i]`
- `metadata == {'sender': 'user1', 'n': i}`
- `key_id == key_id1`
- `sum((m[1]['n'] for m in opened)) == 3`
- `opened[2][0] == b'\x00\xff binary \x7f'`
- `envelope.open(s1)[0] == envelope.open(s2)[0] == b'same'`
- `key_id2 != key_id1`
- `message == b'with new key' and key_id == key_id2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
