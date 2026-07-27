# structured json log

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str) → ?`

## What it does

Structured JSON logging: emit logs as JSON, parse and validate structure.
Failure simulated: write mixed JSON/plaintext, parser must skip invalid, count valid.
Defended outcome: exact count of valid JSON lines, malformed skipped without crash.

## Guarantee

When it runs, structured json log guarantees skipped == 50; valid == valid_written (proven by run).

**Checkable constraints:**

- `valid == valid_written`
- `skipped == 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
