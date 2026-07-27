# byte unit parse

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(s: &str) → Option<u64>`

## What it does

byte_unit_parse — "512Mi"/"1.5G" → bytes and back; round-trip + ordering.

Core idea: parse byte-unit strings (B, KiB, MiB, GiB, TiB) to u64 bytes and back to
string. THE ONE LAW: plant byte-unit strings with known values, parse them to bytes,
serialize back, and assert round-trip preserves order and magnitude — a missed unit
or misplaced decimal would fail the ordering or round-trip assert.
When to use: config parsing (cache size, buffer allocation), disk quotas, memory limits.

## Guarantee

When it runs, byte unit parse guarantees assert_eq!(parsed, *expected, "mismatch for {input}") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(parsed, *expected, "mismatch for {input}")`
- `assert!(bytes1.abs_diff(bytes2) <= 1, "round-trip failed for {input}")`
- `assert!(v1 < v2, "ordering violated")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
