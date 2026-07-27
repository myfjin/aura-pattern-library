# config drift detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(config_dict: dict) → ?`

## What it does

Detect configuration drift between expected and actual state.

## Guarantee

When it runs, config drift detect guarantees detector.has_drift() is False; detector.has_drift() is True; 'timeout' in drift (weak-grade: directional, proven by run).

**Checkable constraints:**

- `detector.has_drift() is False`
- `detector.has_drift() is True`
- `'timeout' in drift`
- `drift['timeout'] == ('changed', 30, 60)`
- `detector.has_drift() is True`
- `'db_port' in drift`
- `drift['db_port'][0] == 'missing'`
- `detector.has_drift() is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class ConfigDriftDetect:`, `def __init__(self):`, `def set_expected(self, config_dict):`, `def scan_actual(self, config_dict):`, `def has_drift(self):`, `def get_drift_details(self):`
**Valid input:** `config_dict` is a flat dict of comparable values.
**Core:** Stores an expected config hash, computes a hash of the actual config, and reports drift details: missing keys, extra keys, and changed values with old/new tuples.
**Assert:** Matching configs report no drift; value change, missing key, and extra key are each detected; multiple drift issues are reported simultaneously; rescanning after remediation clears drift.
**⚠️ Defect:** Only flat dictionaries are supported; nested configs are compared by overall hash, so inner key-level drift is opaque. `_compute_hash` imports `json` inside the method, which is unnecessary. The detector does not suggest or apply remediation.

---
*△ AURA Pattern Library — © Reality Optimizer*
