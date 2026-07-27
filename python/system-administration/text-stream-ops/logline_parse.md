# logline parse

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(line: str) → ?`

## What it does

logline_parse: Parse syslog-style log lines (timestamp priority host process message).
THE ONE LAW: Parse messy real-world log data, assert exact extraction.

## Guarantee

When it runs, logline parse guarantees parsed_lines[0]['pid'] == 1234; parsed_lines[1]['pid'] == 5678; parsed_lines[0] is not None (proven by run).

**Checkable constraints:**

- `parsed_lines[0] is not None`
- `parsed_lines[0]['host'] == 'myhost'`
- `parsed_lines[0]['process'] == 'kernel'`
- `parsed_lines[0]['pid'] == 1234`
- `'memory' in parsed_lines[0]['message'].lower()`
- `parsed_lines[1]['process'] == 'sshd'`
- `parsed_lines[1]['pid'] == 5678`
- `'publickey' in parsed_lines[1]['message']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
