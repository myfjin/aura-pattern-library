# crash log capture

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 5 · Log management

## What it does

crash_log_capture: recover from torn log writes (truncated JSON mid-write).

## Guarantee

When it runs, crash log capture guarantees malformed >= 1; malformed == 1; 'seq' in entry (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `len(entries) >= 3`
- `len(entries) <= 5`
- `malformed >= 1`
- `malformed == 1`
- `'seq' in entry`
- `entry['seq'] == i`
- `crash_idx not in seqs`
- `len(seqs) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
