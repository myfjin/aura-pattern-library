# tail follow

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str) → ?`

## What it does

Tail-follow: read appended lines from a growing log without re-reading old lines.
Failure simulated: append to log, follow, verify no duplicates and all new lines captured.
Defended outcome: exact count of new lines read, no duplicates across follows.

## Guarantee

When it runs, tail follow guarantees line == expected; len(batch1) == 50; len(batch2) == 30 (proven by run).

**Checkable constraints:**

- `len(batch1) == 50`
- `len(batch2) == 30`
- `len(all_lines) == len(unique_lines)`
- `line == expected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
