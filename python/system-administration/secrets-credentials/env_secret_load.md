# env secret load

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(env_key: str, default: None) → ?`

## What it does

Env secret load: load secrets from env var without exposing them to logs/stdout.
Failure simulated: load secret from env, assert it's not printed to stdout/stderr,
and not stored in plaintext in any output file.

## Guarantee

When it runs, env secret load guarantees secret_db not in stdout_text; secret_api not in stdout_text; secret_token not in stdout_text (weak-grade: directional, proven by run).

**Checkable constraints:**

- `secret_db not in stdout_text`
- `secret_api not in stdout_text`
- `secret_token not in stdout_text`
- `secret_db not in stderr_text`
- `secret_api not in stderr_text`
- `secret_token not in stderr_text`
- `secret_db not in log_content`
- `secret_api not in log_content`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
