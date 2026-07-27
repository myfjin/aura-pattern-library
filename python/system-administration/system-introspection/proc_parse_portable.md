# proc parse portable

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(proc_text: str) → ?`

## What it does

proc_parse_portable: Parse /proc-style process info, portable across platforms.
Handles missing /proc gracefully; tests against synthetic data regardless.
THE ONE LAW: Simulate parse failure on malformed data, assert it's caught.

## Guarantee

When it runs, proc parse portable guarantees 'Name' not in broken_parsed; 'VmPeak' in broken_parsed; parsed['Name'] == 'bash' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'Name' not in broken_parsed`
- `'VmPeak' in broken_parsed`
- `parsed['Name'] == 'bash'`
- `parsed['Pid'] == '1234'`
- `parsed['PPid'] == '1000'`
- `parsed['State'] == 'S (sleeping)'`
- `len(parsed) == 8`
- `'Pid' in result`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
