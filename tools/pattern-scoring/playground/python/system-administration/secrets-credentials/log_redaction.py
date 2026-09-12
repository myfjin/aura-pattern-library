"""Log redaction: redact secrets from log output, never write plaintext to disk.
Failure simulated: log message containing secret string; guard redacts it;
assert secret NEVER appears in log file, only [REDACTED] marker appears.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re
import tempfile
import os
from pathlib import Path

def log_redaction(log_path, secrets_to_redact=None):
    """Logger that redacts secrets before writing to disk."""
    if secrets_to_redact is None:
        secrets_to_redact = []

    class RedactingLogger:
        def __init__(self, fpath, secrets):
            self.fpath = fpath
            self.secrets = secrets

        def redact_message(self, message):
            """Replace all secrets in message with [REDACTED]."""
            result = message
            for secret in self.secrets:
                if secret and len(secret) > 0:
                    result = result.replace(secret, "[REDACTED]")
            return result

        def log(self, message):
            """Write redacted message to log file."""
            redacted = self.redact_message(message)
            with open(self.fpath, 'a') as f:
                f.write(redacted + "\n")

        def read_log(self):
            """Read log file."""
            if not Path(self.fpath).exists():
                return ""
            return Path(self.fpath).read_text()

    return RedactingLogger(log_path, secrets_to_redact)

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        log_path = os.path.join(tmpdir, "app.log")

        # Secrets to protect
        api_key = "sk_live_abcdefg1234567890"
        db_pass = "postgres_pwd_secret_xyz"
        oauth_token = "ghp_XXXXXXXXXX"

        logger = log_redaction(log_path, secrets_to_redact=[api_key, db_pass, oauth_token])

        # Log messages containing secrets (insecure input)
        logger.log(f"Initializing with API_KEY={api_key}")
        logger.log(f"Connecting to database with password={db_pass}")
        logger.log(f"OAuth token validated: {oauth_token}")
        logger.log("Normal message with no secrets")
        logger.log(f"Multiple secrets: api={api_key} and pass={db_pass}")

        # Read the on-disk log
        log_content = logger.read_log()

        # RECOVERY ASSERT 1: plaintext secrets NEVER appear in file
        assert api_key not in log_content, \
            f"API key leaked in log: {api_key}"
        assert db_pass not in log_content, \
            f"DB password leaked in log: {db_pass}"
        assert oauth_token not in log_content, \
            f"OAuth token leaked in log: {oauth_token}"

        # RECOVERY ASSERT 2: redaction marker appears for each secret
        redaction_count = log_content.count("[REDACTED]")
        assert redaction_count == 5, \
            f"Expected 5 [REDACTED] markers, found {redaction_count}"

        # RECOVERY ASSERT 3: normal message is preserved
        assert "Normal message with no secrets" in log_content, \
            "Normal message was not preserved"

        # RECOVERY ASSERT 4: partial secrets don't leak (e.g., "sk_live" prefix)
        assert "sk_live" not in log_content, "API key prefix leaked"
        assert "postgres_pwd" not in log_content, "DB password prefix leaked"

        # RECOVERY ASSERT 5: verify exact line count (one per log call)
        lines = [l for l in log_content.strip().split("\n") if l]
        assert len(lines) == 5, f"Expected 5 log lines, got {len(lines)}"

        print("log_redaction PASS")
