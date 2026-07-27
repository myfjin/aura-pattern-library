# gray code

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(n: u32) → u32`

## What it does

Gray code (reflected binary): binary↔Gray conversion where consecutive values differ in exactly 1 bit.
Core idea: Gray(n) = n ^ (n >> 1); inverse via iterative XOR shifting.
When to use: rotary encoders, error-resistant counting, digital circuit state transitions.

## Guarantee

When it runs, gray code guarantees assert_eq!(gray, expected_gray[i as usize], "binary_to_gray({}) = {}, expected {}", i, gray, expected_gray[i as usize]); assert_eq!(dist, 1, "Hamming distance between gray({}) and gray({}) = {}, expected 1", i, i + 1, dist); assert_eq!(dist, 1, "Hamming distance at {} = {}", i, dist) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(gray, expected_gray[i as usize], "binary_to_gray({}) = {}, expected {}", i, gray, expected_gray[i as usize])`
- `assert_eq!(dist, 1, "Hamming distance between gray({}) and gray({}) = {}, expected 1", i, i + 1, dist)`
- `assert_eq!(back, i, "gray round-trip failed for {}: got {}", i, back)`
- `assert_eq!(dist, 1, "Hamming distance at {} = {}", i, dist)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
