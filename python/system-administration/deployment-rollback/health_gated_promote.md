# health gated promote

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(check_name: str, should_pass: bool) → ?`

## What it does

Promote deployment only after health checks pass.

## Guarantee

When it runs, health gated promote guarantees gate.get_active_version() == 'v2.0'; 'db_connect' in str(e); 'failed' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `gate.get_active_version() == 'v2.0'`
- `'db_connect' in str(e)`
- `'failed' in str(e)`
- `gate.get_active_version() is None`
- `'no health checks' in str(e)`
- `gate.get_deployed_version() == 'v2.0'`
- `gate.get_active_version() is None`
- `gate.get_deployed_version() == 'v2.0'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class HealthGatedPromote:`, `def __init__(self):`, `def deploy(self, version):`, `def run_health_check(self, check_name, should_pass):`, `def promote(self):`, `def get_active_version(self):`, `def get_deployed_version(self):`
**Valid input:** `version` is a string; `check_name` is a string; `should_pass` is a boolean.
**Core:** Separates `deployed_version` (staged) from `active_version` (promoted); `promote()` succeeds only if at least one health check was run and all recorded checks passed.
**Assert:** Passing all checks promotes the staged version to active; a failing check blocks promotion and keeps active unchanged; promoting without running any checks raises `RuntimeError`; deployed and active versions can differ.
**⚠️ Defect:** Health checks are simulated booleans, not real probes. There is no timeout or retry on checks. Once promoted, there is no rollback path; a bad promotion must be handled externally. The gate does not ensure the deployed version is still the one that was health-checked.

---
*△ AURA Pattern Library — © Reality Optimizer*
