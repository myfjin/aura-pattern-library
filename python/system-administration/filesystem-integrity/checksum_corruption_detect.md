# checksum corruption detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(path: str, expected_checksum: str, algo: str) → ?`

## What it does

checksum_corruption_detect: detect corruption via checksum mismatch.
Failure simulated: write file + compute checksum; corrupt a byte in the file;
recompute checksum and assert it differs (corruption detected).
Recovery asserted: honest checksum detects single-byte flip; a no-op check (len, first byte)
would miss it. Pattern's own checksum function must be called.

## Guarantee

When it runs, checksum corruption detect guarantees actual_corrupted != expected_checksum; result != expected_data; 'checksum mismatch' in str(e) (proven by run).

**Checkable constraints:**

- `actual_corrupted != expected_checksum`
- `'checksum mismatch' in str(e)`
- `result != expected_data`
- `result[512] != expected_data[512]`
- `result[:512] == expected_data[:512]`
- `result[513:] == expected_data[513:]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
