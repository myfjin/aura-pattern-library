# deploy idempotency

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(version: str, skip_if_current: bool) → ?`

## What it does

Idempotent deployments (safe to run multiple times).

## Guarantee

When it runs, deploy idempotency guarantees deployer.get_deployment_count('v1.0') == 2; deployer.get_deployment_count('v1.0') == 3; deployer.get_deployment_count('v1.0') == 2 (proven by run).

**Checkable constraints:**

- `deployer.get_current_version() == 'v1.0'`
- `deployer.get_deployment_count('v1.0') == 1`
- `deployer.get_current_version() == 'v1.0'`
- `deployer.get_deployment_count('v1.0') == 1`
- `deployer.get_deployment_count('v1.0') == 1`
- `deployer.get_deployment_count('v1.0') == 2`
- `deployer.get_deployment_count('v1.0') == 3`
- `deployer.is_deployed('v1.0')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class IdempotentDeploy:`, `def __init__(self):`, `def deploy(self, version, skip_if_current=True):`, `def get_current_version(self):`, `def get_deployment_count(self, version):`, `def is_deployed(self, version):`
**Valid input:** `version` is a string; `skip_if_current` is a boolean.
**Core:** Tracks the currently deployed version and a per-version deployment counter; when `skip_if_current=True`, redeploying the current version succeeds without incrementing the counter.
**Assert:** Redeploying the same version with skip is a no-op (count stays 1); redeploying with `skip_if_current=False` counts each attempt; switching versions updates current version; network retry scenarios leave count at 1.
**⚠️ Defect:** There is no notion of rollback or previous version. The counter is only incremented when `skip_if_current=False`, but the current version is set on every call, so a skipped redeploy still counts as a deployment event semantically. No actual deployment artifact is produced.

---
*△ AURA Pattern Library — © Reality Optimizer*
