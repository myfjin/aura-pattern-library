# rotating log checksum

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → u32`

## What it does

rotating_log_checksum — size-triggered rotation + per-segment CRC32; corruption isolated.

Core idea: logs rotate every N bytes; when a segment is sealed its CRC32 is STORED. Verify
recomputes each segment's CRC and compares to the stored value — so a bit-flip in one segment
fails ONLY that segment, others still verify. THE LAW: seal a multi-segment log, corrupt one
segment's bytes, and assert exactly that segment fails verification while the rest pass. (A
verify that only checks "crc != 0" would miss the corruption entirely.)
When to use: rotated log files with integrity, corruption isolation, archival.

## Guarantee

When it runs, rotating log checksum guarantees assert!(log.segments.len() >= 3, "data rotated across ≥3 segments") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(log.segments.len() >= 3, "data rotated across ≥3 segments")`
- `assert!(log.verify_segment(i), "sealed segment {i} verifies")`
- `assert!(!log.verify_segment(1), "corrupted segment 1 must FAIL verification")`
- `assert!(log.verify_segment(i), "uncorrupted segment {i} still verifies")`
- `assert!(empty.verify_segment(0), "empty sealed segment verifies")`
- `assert!(!empty.verify_segment(5), "out-of-range segment does not verify")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
