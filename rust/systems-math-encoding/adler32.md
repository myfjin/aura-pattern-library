# adler32

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → u32`

## What it does

Adler-32 checksum: sum of all bytes (mod 65521) + sum of running sum (mod 65521).
Core idea: two 16-bit checksums interleaved; fast for small data.
When to use: zlib compression, quick integrity checks, not security-critical.

## Guarantee

When it runs, adler32 guarantees assert_eq!(result, 0x11e60398, "Adler-32('Wikipedia') = {:#010x}, expected 0x11e60398", result); assert_eq!(empty, 0x00000001, "Adler-32('') = {:#010x}, expected 0x00000001", empty) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, 0x11e60398, "Adler-32('Wikipedia') = {:#010x}, expected 0x11e60398", result)`
- `assert_eq!(empty, 0x00000001, "Adler-32('') = {:#010x}, expected 0x00000001", empty)`
- `assert_ne!(single_a, single_b, "Adler-32 should differ for different single characters")`
- `assert_eq!(adler, adler2, "Adler-32 not deterministic for {:?}", std::str::from_utf8(data).ok())`
- `assert_ne!(adler1, adler2)`
- `assert_ne!(adler_short, adler_long)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
