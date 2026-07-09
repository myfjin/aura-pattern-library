#!/usr/bin/env python3
"""Secret redaction: redact sensitive data from logs before writing.
Failure simulated: log contains API key/password, verify redaction removed it.
Defended outcome: secret string never appears in the written log file.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re, tempfile, pathlib, os

def redacting_logger(log_path, redact_patterns=None):
    """Logger that redacts sensitive data before writing."""
    if redact_patterns is None:
        redact_patterns = [
            (r'api[_-]?key[=:]\s*[^\s,]+', '[REDACTED_APIKEY]'),
            (r'password[=:]\s*[^\s,]+', '[REDACTED_PASSWORD]'),
            (r'token[=:]\s*[^\s,]+', '[REDACTED_TOKEN]'),
        ]

    log_file = pathlib.Path(log_path)

    def log_entry(text):
        redacted = text
        for pattern, replacement in redact_patterns:
            redacted = re.sub(pattern, replacement, redacted, flags=re.IGNORECASE)
        log_file.write_text(log_file.read_text() + redacted + "\n")

    return log_entry

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        log_path = os.path.join(tmpdir, "app.log")
        pathlib.Path(log_path).touch()

        log_entry = redacting_logger(log_path)

        # Log entries containing secrets
        secret_api_key = "super-secret-api-key-12345"
        secret_password = "password@MyP@ssw0rd123"
        secret_token = "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

        log_entry(f"User login attempt with api_key={secret_api_key}")
        log_entry(f"Database connection: password={secret_password}")
        log_entry(f"OAuth token={secret_token}")
        log_entry("Normal log line with no secrets")

        # Read the log file
        with open(log_path, 'r') as f:
            log_content = f.read()

        # Assert: no secrets appear (unconditional, all three must fail to appear)
        secret_count = 0
        secret_count += secret_api_key.count(secret_api_key) if secret_api_key in log_content else 0
        secret_count += secret_password.count(secret_password) if secret_password in log_content else 0
        secret_count += secret_token.count(secret_token) if secret_token in log_content else 0
        assert secret_count == 0, f"{secret_count} secrets leaked in log"

        # Assert: secrets do NOT appear in the log file (unconditional)
        assert secret_api_key not in log_content, f"API key leaked in log"
        assert secret_password not in log_content, f"Password leaked in log"
        assert secret_token not in log_content, f"Token leaked in log"

        # Assert: redaction markers ARE present (unconditional, all three)
        redacted_count = 0
        redacted_count += log_content.count("[REDACTED_APIKEY]")
        redacted_count += log_content.count("[REDACTED_PASSWORD]")
        redacted_count += log_content.count("[REDACTED_TOKEN]")
        assert redacted_count == 3, f"Expected 3 redacted markers, found {redacted_count}"

        assert "[REDACTED_APIKEY]" in log_content, "API key not redacted"
        assert "[REDACTED_PASSWORD]" in log_content, "Password not redacted"
        assert "[REDACTED_TOKEN]" in log_content, "Token not redacted"

        # Assert: normal log line preserved
        assert "Normal log line" in log_content, "Normal log corrupted"

        print("PASS")
