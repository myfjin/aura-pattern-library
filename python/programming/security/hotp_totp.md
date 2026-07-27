# hotp totp

**Language:** Python · **Sphere:** programming · **Category:** Security

## What it does

Time-Based One-Time Password (TOTP) generator and validator.

This module implements RFC 6238 TOTP and RFC 4226 HOTP algorithms for generating
and validating time-based one-time passwords. It includes functionality for
generating secrets, creating QR code URIs, and validating tokens with drift tolerance.

## Guarantee

When it runs, hotp totp guarantees got == expected; got == expected; hotp.validate('755224', 0) is True (proven by run).

**Checkable constraints:**

- `got == expected`
- `hotp.validate('755224', 0) is True`
- `hotp.validate('755224', 1) is False`
- `hotp.validate('000000', 0) is False`
- `got == expected`
- `ok and offset == -1`
- `ok is False`
- `totp.generate(990) == totp.generate(1019)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
