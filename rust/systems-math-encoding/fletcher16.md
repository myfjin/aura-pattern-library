# fletcher16

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → u16`

## What it does

Fletcher-16 checksum: two running sums reduced modulo 255 (NOT 256).
Core idea: s1 = Σ bytes mod 255; s2 = Σ s1 mod 255; result = (s2 << 8) | s1. The mod-255
(ones-complement) reduction is the DEFINING detail — a mod-256 (`wrapping u8`) version is a
different, weaker checksum and does NOT match published Fletcher-16 vectors. THE ONE LAW:
assert against an independently-verified vector (fletcher16("abcde") == 0xC8F0), not a value
self-computed from the implementation. When to use: RAID/data validation, TCP-like checks.

## Guarantee

When it runs, fletcher16 guarantees assert_eq!(fletcher16(b""), 0x0000); assert_eq!(fletcher16(b"abcde"), 0xC8F0, "Fletcher-16(\"abcde\") must be 0xC8F0 (mod 255)"); assert_eq!(fletcher16(b"abc"), 0x4C27, "Fletcher-16(\"abc\") must be 0x4C27") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(fletcher16(b""), 0x0000)`
- `assert_eq!(fletcher16(b"abcde"), 0xC8F0, "Fletcher-16(\"abcde\") must be 0xC8F0 (mod 255)")`
- `assert_eq!(fletcher16(b"abc"), 0x4C27, "Fletcher-16(\"abc\") must be 0x4C27")`
- `assert_ne!(fletcher16(&[0xaa]), fletcher16(&[0xab]), "single-bit change detected")`
- `assert_ne!(fletcher16(b"hello"), fletcher16(b"helloworld"), "append changes checksum")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
