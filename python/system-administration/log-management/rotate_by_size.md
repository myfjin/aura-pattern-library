# rotate by size

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str, size_cap_bytes: int, keep_rotations: int) → ?`

## What it does

Rotate logs by size: exceed cap, assert on-disk bytes <= cap×(retain+1).
Failure simulated: write 100× the cap, forcing multiple rotations.
Defended outcome: total bytes on disk stays bounded despite flood.

## Guarantee

When it runs, rotate by size guarantees total_bytes <= expected_max; len(rotated) <= keep (proven by run).

**Checkable constraints:**

- `total_bytes <= expected_max`
- `len(rotated) <= keep`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
