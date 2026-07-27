# immutable release

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(version: str, content: str) → ?`

## What it does

Immutable release artifacts (prevent re-deployment or modification).

## Guarantee

When it runs, immutable release guarantees immutable.release_exists('v1.0'); immutable.get_release('v1.0') == 'app code v1'; 'already exists' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `immutable.release_exists('v1.0')`
- `immutable.get_release('v1.0') == 'app code v1'`
- `'already exists' in str(e)`
- `'immutable' in str(e)`
- `immutable.get_release(ver) == content`
- `'not found' in str(e)`
- `os.path.exists(v1_dir)`
- `os.path.exists(v2_dir)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class ImmutableRelease:`, `def __init__(self, releases_dir):`, `def create_release(self, version, content):`, `def get_release(self, version):`, `def release_exists(self, version):`, `def prevent_modification(self, version):`
**Valid input:** `releases_dir` is a writable directory; `version` is a unique string; `content` is a string.
**Core:** Creates versioned subdirectories under `releases_dir`; rejects duplicate version creation; stores metadata in memory and writes an `artifact.txt`; `prevent_modification` sets the artifact read-only (`0o444`).
**Assert:** Creating a release makes it retrievable; duplicate creation raises `ValueError`; multiple versions coexist; the artifact file is read-only after `prevent_modification`; nonexistent release access raises `ValueError`.
**⚠️ Defect:** The in-memory `self.released` dict is not persisted, so process restart loses release metadata even though directories remain. `prevent_modification` only sets file permissions and does not protect the version directory itself. The artifact name is hardcoded to `artifact.txt`.

---
*△ AURA Pattern Library — © Reality Optimizer*
