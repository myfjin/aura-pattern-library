# secret separation

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(config_file: str, secret_file: str) → ?`

## What it does

Secret separation: keep secrets separate from regular config; assert not leaked.
Failure simulated: secret ends up in regular config; secret missing from secret location.
Asserts: secret not in regular config; secret is in secret location; both have right keys.

## Guarantee

When it runs, secret separation guarantees 'api_key' not in config; 'host' in config; 'api_key' in secrets (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'api_key' not in config`
- `'host' in config`
- `'api_key' in secrets`
- `secrets['api_key'] == 'secret123'`
- `'api_key' in str(e)`
- `'secret.json' in str(e) or 'not found' in str(e)`
- `'db_password' in str(e) or 'token' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def load_config_with_secrets(config_file, secret_file):`
**Valid input:** `config_file` is a JSON file with only non-secret keys; `secret_file` is a JSON file containing `api_key`, `db_password`, and `token`.
**Core:** Loads regular config and secrets separately. Raises `ValueError` if any known secret key leaks into the regular config; raises `FileNotFoundError` if the secret file is missing; raises `KeyError` if required secrets are absent.
**Assert:** Proper separation returns both dicts; leaked secret in regular config, missing secret file, and missing required secret are all detected.
**⚠️ Defect:** The set of secret keys (`api_key`, `db_password`, `token`) is hardcoded, so adding a new secret type requires editing the function. There is no encryption of the secret file; it is plain JSON on disk.

---
*△ AURA Pattern Library — © Reality Optimizer*
