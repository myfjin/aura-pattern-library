# sliding rate window

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(.0: list_iterator) → ?`

## What it does

Rate limiting using sliding time window.

## Guarantee

When it runs, sliding rate window guarantees window.get_event_count() == 3; window.is_allowed() is True; window.is_allowed() is True (proven by run).

**Checkable constraints:**

- `window.is_allowed() is True`
- `window.is_allowed() is True`
- `window.is_allowed() is True`
- `window.get_event_count() == 3`
- `window.is_allowed() is True`
- `window.is_allowed() is True`
- `allowed is False`
- `window.is_allowed() is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
