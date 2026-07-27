# rate limited log

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(limit_per_sec: int) → ?`

## What it does

Rate-limited logger: cap log emissions per time window (token bucket).
Failure simulated: fire 1000 logs, assert <= limit actually written.
Defended outcome: emitted count stays at or below configured rate.

## Guarantee

When it runs, rate limited log guarantees emitted <= max_expected; emitted < 1000 (proven by run).

**Checkable constraints:**

- `emitted <= max_expected`
- `emitted < 1000`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
