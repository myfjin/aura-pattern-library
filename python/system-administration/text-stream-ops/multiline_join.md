# multiline join

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(lines: List[str], continuation_prefix: str) → ?`

## What it does

multiline_join: Join split multiline log entries (e.g., Python stacktraces).
THE ONE LAW: Parse real messy multiline data with proper continuation detection.

## Guarantee

When it runs, multiline join guarantees deep_joined[0].count('\n') == 5; newlines == 2; len(joined) == 2 (proven by run).

**Checkable constraints:**

- `len(joined) == 2`
- `joined[0].startswith('2024-07-10 ERROR')`
- `'Division by zero' in joined[0]`
- `'File "app.py"' in joined[0]`
- `'result = 10 / x' in joined[0]`
- `joined[1].startswith('2024-07-10 WARNING')`
- `'Memory low' in joined[1]`
- `'Available: 512MB' in joined[1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
