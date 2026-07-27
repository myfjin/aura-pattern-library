# enforce 600 perms

**Language:** Go · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(filepath: str) → ?`

## What it does

enforce_600_perms: check and enforce 0o600 permissions on secret files.

## Guarantee

When it runs, enforce 600 perms guarantees mode_before == 420; mode_after == 384; user_bits == 6 (proven by run on the SYS original).

**Checkable constraints:**

- `mode_before == 420`
- `result`
- `mode_after == 384`
- `world_bits == 0`
- `user_bits == 6`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
