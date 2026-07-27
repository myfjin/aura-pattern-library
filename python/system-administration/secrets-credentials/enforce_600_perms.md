# enforce 600 perms

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(filepath: str) → ?`

## What it does

Enforce 0o600 perms on secrets: reject world-readable files.
Failure simulated: create secret file with 0o644 (world-readable);
guard detects and rejects read, or forces chmod to 0o600.
Defended outcome: assert final perms are 0o600 via os.stat, not a flag.

## Guarantee

When it runs, enforce 600 perms guarantees mode_before == 420; mode_after == 384; user_bits == 6 (proven by run).

**Checkable constraints:**

- `mode_before == 420`
- `result`
- `mode_after == 384`
- `world_bits == 0`
- `user_bits == 6`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
