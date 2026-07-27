# uptime read

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(uptime_text: str) → ?`

## What it does

uptime_read: Parse /proc/uptime to extract uptime in seconds and idle time.
THE ONE LAW: Parse exact values, assert single clock (no time() calls during parse).

## Guarantee

When it runs, uptime read guarantees uptime == 12345.67; idle == 98765.43; abs(p_up - 0.01) < 1e-09 (proven by run).

**Checkable constraints:**

- `uptime == 12345.67`
- `idle == 98765.43`
- `'2 fields' in str(e)`
- `abs(p_up - 0.01) < 1e-09`
- `abs(p_idle - 0.02) < 1e-09`
- `l_up == 999999999.99`
- `z_up == 0.0`
- `isinstance(uptime, float)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
