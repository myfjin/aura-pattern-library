"""Env secret load: load secrets from env var without exposing them to logs/stdout.
Failure simulated: load secret from env, assert it's not printed to stdout/stderr,
and not stored in plaintext in any output file.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
from io import StringIO
from pathlib import Path

def env_secret_load(env_key, default=None):
    """Load secret from env var safely; return secret reference (not printed)."""
    secret = os.environ.get(env_key, default)
    if secret is None:
        raise KeyError(f"Env var {env_key} not set and no default")
    return secret

def load_secrets_safe(env_keys, output_file=None):
    """Load multiple secrets from env vars, optionally write a usage log (not secrets)."""
    secrets = {}
    for key in env_keys:
        secret = env_secret_load(key)
        secrets[key] = secret

    # Log usage (NOT the secrets themselves)
    if output_file:
        with open(output_file, 'a') as f:
            for key in env_keys:
                f.write(f"Loaded secret for {key}\n")

    return secrets

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        # Set up env vars with secrets
        secret_db = "password_db_hunter2_xyz"
        secret_api = "api_key_sk_live_12345678"
        secret_token = "oauth_ghp_secret_token"

        os.environ["DB_PASSWORD"] = secret_db
        os.environ["API_KEY"] = secret_api
        os.environ["OAUTH_TOKEN"] = secret_token

        # Capture stdout/stderr to verify no leakage
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        captured_stdout = StringIO()
        captured_stderr = StringIO()

        try:
            sys.stdout = captured_stdout
            sys.stderr = captured_stderr

            # Load secrets
            log_file = os.path.join(tmpdir, "usage.log")
            secrets = load_secrets_safe(["DB_PASSWORD", "API_KEY", "OAUTH_TOKEN"], log_file)

        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        # RECOVERY ASSERT 1: secrets NOT in stdout
        stdout_text = captured_stdout.getvalue()
        assert secret_db not in stdout_text, "DB password leaked to stdout"
        assert secret_api not in stdout_text, "API key leaked to stdout"
        assert secret_token not in stdout_text, "OAuth token leaked to stdout"

        # RECOVERY ASSERT 2: secrets NOT in stderr
        stderr_text = captured_stderr.getvalue()
        assert secret_db not in stderr_text, "DB password leaked to stderr"
        assert secret_api not in stderr_text, "API key leaked to stderr"
        assert secret_token not in stderr_text, "OAuth token leaked to stderr"

        # RECOVERY ASSERT 3: usage log exists but contains NO secrets
        log_content = Path(log_file).read_text()
        assert secret_db not in log_content, "DB password in usage log"
        assert secret_api not in log_content, "API key in usage log"
        assert secret_token not in log_content, "OAuth token in usage log"

        # RECOVERY ASSERT 4: usage log mentions key names, not values
        assert "DB_PASSWORD" in log_content, "Log should mention DB_PASSWORD"
        assert "API_KEY" in log_content, "Log should mention API_KEY"
        assert "OAUTH_TOKEN" in log_content, "Log should mention OAUTH_TOKEN"

        # RECOVERY ASSERT 5: returned secrets dict has correct values (in memory only)
        assert secrets["DB_PASSWORD"] == secret_db, "DB secret not loaded correctly"
        assert secrets["API_KEY"] == secret_api, "API secret not loaded correctly"
        assert secrets["OAUTH_TOKEN"] == secret_token, "OAuth secret not loaded correctly"

        print("env_secret_load PASS")
