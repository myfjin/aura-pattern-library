# config versioning

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(config_file: str, expected_version: str) → ?`

## What it does

Config versioning: track config version, detect drift (config changed without version bump).
Failure simulated: config content changed but version not bumped; version mismatch.
Asserts: exact version mismatch in error; version matches content hash; drift detected.

## Guarantee

When it runs, config versioning guarantees config['host'] == 'localhost'; version == '1.0'; hash_val == content_hash (weak-grade: directional, proven by run).

**Checkable constraints:**

- `config['host'] == 'localhost'`
- `version == '1.0'`
- `hash_val == content_hash`
- `version == '2.0'`
- `'version mismatch' in str(e).lower()`
- `'1.0' in str(e) and '2.0' in str(e)`
- `'drift' in str(e).lower()`
- `'hash' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def compute_config_hash(config_dict):`, `def validate_config_version(config_file, expected_version):`
**Valid input:** `config_file` contains a JSON wrapper with `version`, `content`, and `content_hash` fields; `expected_version` is a string.
**Core:** Hashes the `content` dict deterministically (sorted JSON + SHA-256) and compares it with the stored `content_hash`, catching content drift without a version bump.
**Assert:** Matching version and hash pass; version mismatch, content drift, and missing fields are rejected with explicit `ValueError` messages.
**⚠️ Defect:** The version string is arbitrary and not enforced to be monotonic; an attacker can bump the version to match any content. The hash is computed over JSON serialization, so semantically identical configs with different key ordering would hash the same, but any formatting difference in the source file is lost.

---
*△ AURA Pattern Library — © Reality Optimizer*
