# least privilege check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(filepath: str) → ?`

## What it does

Least privilege check: verify secret file has no world/group read bits.
Failure simulated: create secret with mode 0o666 (world+group readable);
guard checks and rejects or strips world/group bits. Assert world/group bits are 0.

## Guarantee

When it runs, least privilege check guarantees mode_before == 438; mode_after == 384; result is False (proven by run).

**Checkable constraints:**

- `mode_before == 438`
- `result is False`
- `world_bits_before > 0`
- `group_bits_before > 0`
- `result_after is True`
- `world_bits_after == 0`
- `group_bits_after == 0`
- `mode_after == 384`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
