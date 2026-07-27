# disk space watchdog

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(threshold_mb: int) → ?`

## What it does

Disk space watchdog: refuses writes when available space < threshold.
Failure simulated: "fill" disk by tracking usage, attempt 1000 writes with cap=100MB;
assert guard refuses writes when available < cap, peak usage ≤ cap.

## Guarantee

When it runs, disk space watchdog guarantees peak_mb <= 100; num_refused >= 900; num_wrote <= 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak_mb <= 100`
- `num_refused >= 900`
- `num_wrote <= 100`
- `num_refused > num_wrote * 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
