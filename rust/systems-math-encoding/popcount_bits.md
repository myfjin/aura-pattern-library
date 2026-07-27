# popcount bits

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(mut n: u64) → u32`

## What it does

Bit population count (Hamming weight) and bit operations from scratch.
Core idea: count set bits in an integer; also provide ctz (trailing zeros) and clz (leading zeros).
When to use: bit manipulation in protocols, sparse set operations, instruction simulation.

## Guarantee

When it runs, popcount bits guarantees assert_eq!(count, expected_count, "popcount({:#x}) = {}, expected {}", value, count, expected_count); assert_eq!(result, expected_ctz, "ctz({:#x}) = {}, expected {}", value, result, expected_ctz); assert_eq!(result, expected_clz, "clz({:#x}) = {}, expected {}", value, result, expected_clz) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(count, expected_count, "popcount({:#x}) = {}, expected {}", value, count, expected_count)`
- `assert_eq!(count, builtin, "popcount({:#x}) {} != builtin {}", value, count, builtin)`
- `assert_eq!(result, expected_ctz, "ctz({:#x}) = {}, expected {}", value, result, expected_ctz)`
- `assert_eq!(result, builtin, "ctz({:#x}) {} != builtin {}", value, result, builtin)`
- `assert_eq!(result, expected_clz, "clz({:#x}) = {}, expected {}", value, result, expected_clz)`
- `assert_eq!(result, builtin, "clz({:#x}) {} != builtin {}", value, result, builtin)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
