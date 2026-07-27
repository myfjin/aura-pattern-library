# ntp offset check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(offset_seconds: float) → ?`

## What it does

Validate an NTP clock offset against a maximum bound.

NTPValidator checks a reported time offset against a configured maximum
magnitude: it accepts offsets within bounds (inclusive of the boundary),
raises ValueError with a descriptive message when the absolute offset exceeds
the limit, and remembers the last offset seen. Use it as a guard that refuses
to trust a clock that has drifted too far. Guarantees (self-test oracle):
in-bound and exact-boundary offsets are accepted, positive and negative
out-of-bound offsets raise, and the last offset is tracked accurately.

## Guarantee

When it runs, ntp offset check guarantees validator.get_offset() == 0.5; validator.validate(0.0) is True; validator.validate(0.5) is True (proven by run).

**Checkable constraints:**

- `validator.validate(0.0) is True`
- `validator.validate(0.5) is True`
- `validator.validate(-0.5) is True`
- `validator.validate(1.0) is True`
- `validator.validate(-1.0) is True`
- `'NTP offset' in str(e)`
- `'1.5' in str(e)`
- `'NTP offset' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
