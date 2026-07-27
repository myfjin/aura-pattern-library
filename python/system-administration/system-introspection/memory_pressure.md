# memory pressure

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(psi_text: str) → ?`

## What it does

memory_pressure: Parse /proc/pressure/memory for PSI (Pressure Stall Info) metrics.
THE ONE LAW: Parse exact pressure values, fail on incomplete data.

## Guarantee

When it runs, memory pressure guarantees abs(metrics['some_avg10'] - 1.23) < 0.001; abs(metrics['some_avg60'] - 2.34) < 0.001; abs(metrics['some_avg300'] - 3.45) < 0.001 (proven by run).

**Checkable constraints:**

- `abs(metrics['some_avg10'] - 1.23) < 0.001`
- `abs(metrics['some_avg60'] - 2.34) < 0.001`
- `abs(metrics['some_avg300'] - 3.45) < 0.001`
- `abs(metrics['full_avg10'] - 0.45) < 0.001`
- `abs(metrics['full_avg60'] - 0.56) < 0.001`
- `abs(metrics['full_avg300'] - 0.67) < 0.001`
- `'full_avg' in str(e)`
- `zero['some_avg10'] == 0.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
