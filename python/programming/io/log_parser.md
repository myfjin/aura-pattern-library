# log parser

**Language:** Python · **Sphere:** programming · **Category:** Io

## What it does

JSON Schema Validator Module

This module provides a lightweight JSON schema validator that supports:
- Type checking
- Required fields
- Nested object validation
- Custom validation errors

## Guarantee

When it runs, log parser guarantees caught == 4; False; field in str(e) (proven by run).

**Checkable constraints:**

- `field in str(e)`
- `caught == 4`
- `'[1]' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
