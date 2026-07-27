# cpu throttle

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(max_concurrent: int) → ?`

## What it does

CPU throttle: caps concurrent CPU-bound workers, refuses spawning past limit.
Failure simulated: spawn 1000 CPU-bound workers with cap=4 concurrent;
assert peak concurrent ≤ 4, >900 refused, workers stayed bounded.

## Guarantee

When it runs, cpu throttle guarantees peak <= 4; num_refused > 900; num_spawned <= 50 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak <= 4`
- `num_refused > 900`
- `num_spawned <= 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
