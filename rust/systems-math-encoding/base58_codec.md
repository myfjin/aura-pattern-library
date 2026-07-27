# base58 codec

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → String`

## What it does

Base58 codec (Bitcoin alphabet): encode/decode arbitrary-length bytes.
Core idea: treat the byte string as a big-endian base-256 number and re-base it to 58 by
processing each input byte with carry propagation — so it works for ANY length (a real
25-byte address), unlike a fixed u128 which overflows past 16 bytes. Leading zero bytes map
to leading '1's (and '1' is itself the digit 0 — decoded normally, not skipped). THE ONE LAW:
assert against published base58 vectors (including a 20-byte input that a u128 impl fails).
When to use: Bitcoin addresses, human-readable binary without 0/O/I/l ambiguity.

## Guarantee

When it runs, base58 codec guarantees assert_eq!(base58_encode(b"a"), "2g", "0x61 → 2g"); assert_eq!(base58_encode(&[0x62, 0x62, 0x62]), "a3gV"); assert_eq!(base58_encode(&[0x63, 0x63, 0x63]), "aPEr") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(base58_encode(b"a"), "2g", "0x61 → 2g")`
- `assert_eq!(base58_encode(&[0x62, 0x62, 0x62]), "a3gV")`
- `assert_eq!(base58_encode(&[0x63, 0x63, 0x63]), "aPEr")`
- `assert_eq!(base58_encode(b"simply a long string"), "2cFupjhnEsSn59qHXstmK2ffpLv2", "20-byte input must encode correctly (u128 would overflow)")`
- `assert_eq!(base58_encode(b""), "")`
- `assert_eq!(base58_encode(&[0x00]), "1")`
- `assert_eq!(base58_encode(&[0x00, 0x00]), "11")`
- `assert_eq!(base58_encode(&[0x00, 0x00, 0x61]), "112g")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
