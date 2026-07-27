# load avg read

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(loadavg_text: str) → ?`

## What it does

load_avg_read: Parse /proc/loadavg (1min, 5min, 15min load averages).
THE ONE LAW: Parse exact values, fail on missing fields.

## Guarantee

When it runs, load avg read guarantees load_1 == 2.5; load_5 == 1.8; load_15 == 0.95 (proven by run).

**Checkable constraints:**

- `load_1 == 2.5`
- `load_5 == 1.8`
- `load_15 == 0.95`
- `'3 load fields' in str(e)`
- `i1 == 0.0`
- `i5 == 0.0`
- `i15 == 0.0`
- `h1 == 16.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
