# dynamic bitset

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(bit: usize) → ?`

## What it does

Dynamic bitset: set/clear/test bits with and/or/xor operations.
Core idea: Vec<u8> backing store, 8 bits per byte; operations match Vec<bool> exactly.
When to use: sparse bitmaps, large bit arrays, membership tests, permissions.

## Guarantee

When it runs, dynamic bitset guarantees assert_eq!(bs2.count_ones(), 0); assert_eq!(bs2.count_ones(), 3); assert_eq!(byte_aligned.bytes[0], 0xff) (proven by rustc-run).

**Checkable constraints:**

- `assert!(bit < self.len)`
- `assert!(bit < self.len)`
- `assert!(bit < self.len)`
- `assert_eq!(self.len, other.len)`
- `assert_eq!(self.len, other.len)`
- `assert_eq!(self.len, other.len)`
- `assert_eq!(bs.test(0), false)`
- `assert_eq!(bs.test(0), true)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
