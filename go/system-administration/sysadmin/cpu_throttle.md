# cpu throttle

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 6 · Resource guards & quotas

## What it does

cpu_throttle: caps concurrent CPU-bound workers, refuses spawning past limit.

## Guarantee

When it runs, cpu throttle guarantees peak <= 4; num_refused > 900; num_spawned <= 50 (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `peak <= 4`
- `num_refused > 900`
- `num_spawned <= 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
