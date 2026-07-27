# duration parse

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(s: &str) → Option<u64>`

## What it does

duration_parse — "1h30m"/"250ms" → total; round-trip + arithmetic.

Core idea: parse duration strings (1h, 30m, 250ms, etc.) to total milliseconds,
serialize back, and verify arithmetic. THE ONE LAW: plant duration strings with
known totals, parse them, serialize back, then assert round-trip and arithmetic are
exact — a missed unit or decimal error would fail the total or arithmetic asserts.
When to use: timeout config, sleep durations, rate-limiting intervals.

## Guarantee

When it runs, duration parse guarantees assert_eq!(parsed, *expected_ms, "mismatch for {input}"); assert_eq!(sum, expected, "arithmetic failed") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(parsed, *expected_ms, "mismatch for {input}")`
- `assert_eq!(ms1, ms2, "round-trip failed for {input}")`
- `assert_eq!(sum, expected, "arithmetic failed")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
