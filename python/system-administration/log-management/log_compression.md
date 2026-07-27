# log compression

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str, compression_level: int) → ?`

## What it does

Compress rotated logs: archive to .gz, assert compressed size < original.
Failure simulated: write large logs, compress them, measure shrinkage.
Defended outcome: compressed size is significantly smaller than raw.

## Guarantee

When it runs, log compression guarantees comp_size > 0; comp_size < orig_size; orig_size > comp_size (weak-grade: directional, proven by run).

**Checkable constraints:**

- `comp_size > 0`
- `comp_size < orig_size`
- `orig_size > comp_size`
- `ratio < 0.6`
- `ratio > 0.0`
- `not os.path.exists(log_path)`
- `gz_exists`
- `os.path.getsize(f'{log_path}.gz') == comp_size`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
