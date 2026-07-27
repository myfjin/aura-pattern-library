# log redaction

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(log_path: str, secrets_to_redact: List[str]) → ?`

## What it does

Log redaction: redact secrets from log output, never write plaintext to disk.
Failure simulated: log message containing secret string; guard redacts it;
assert secret NEVER appears in log file, only [REDACTED] marker appears.

## Guarantee

When it runs, log redaction guarantees redaction_count == 5; api_key not in log_content; db_pass not in log_content (proven by run).

**Checkable constraints:**

- `api_key not in log_content`
- `db_pass not in log_content`
- `oauth_token not in log_content`
- `redaction_count == 5`
- `'Normal message with no secrets' in log_content`
- `'sk_live' not in log_content`
- `'postgres_pwd' not in log_content`
- `len(lines) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
