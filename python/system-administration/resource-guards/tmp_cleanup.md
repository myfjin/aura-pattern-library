# tmp cleanup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(quota_mb: int, cleanup_target_mb: int) → ?`

## What it does

Tmp cleanup: auto-cleans temp files when usage exceeds quota.
Failure simulated: create files until 200MB used, auto-cleanup kicks at 150MB;
assert final size stays ≤ 150MB after cleanup + new creates, refused > 0.

## Guarantee

When it runs, tmp cleanup guarantees final_usage_mb <= quota_mb; guard.cleanup_runs >= 1 and guard.refused >= 1; num_created > quota_mb // file_mb (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_usage_mb <= quota_mb`
- `guard.cleanup_runs >= 1 and guard.refused >= 1`
- `num_created > quota_mb // file_mb`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
