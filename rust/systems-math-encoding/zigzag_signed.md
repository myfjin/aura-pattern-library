# zigzag signed

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(n: i64) → u64`

## What it does

Zigzag encoding for signed integers (maps signed to unsigned for efficient varint).
Core idea: alternating sign to adjacent values: 0→0, -1→1, 1→2, -2→3, -3→5, 3→6.
When to use: protocol buffers for signed fields, compact variable-length signed int storage.

## Guarantee

When it runs, zigzag signed guarantees assert_eq!(encoded, *expected_encoded, "zigzag_encode({}) mismatch", input) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(encoded, *expected_encoded, "zigzag_encode({}) mismatch", input)`
- `assert_eq!(decoded, *input, "zigzag round-trip mismatch for {}", input)`
- `assert_eq!(decoded, n, "zigzag round-trip failed for {}", n)`
- `assert!(zigzag_encode(0) < zigzag_encode(100))`
- `assert!(zigzag_encode(-1) < zigzag_encode(-100))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
