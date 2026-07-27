# retention prune

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_dir: Path, keep_count: int) → ?`

## What it does

Prune logs by retention policy: keep N newest, delete rest.
Failure simulated: create 100 log files, prune, assert only N remain.
Defended outcome: exactly N files kept, older ones deleted.

## Guarantee

When it runs, retention prune guarantees remaining_nums == expected; len(remaining) == keep; deleted == 100 - keep (proven by run).

**Checkable constraints:**

- `len(remaining) == keep`
- `deleted == 100 - keep`
- `remaining_nums == expected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
