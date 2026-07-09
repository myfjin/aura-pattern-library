"""Keyring store: persist secrets in protected file (0o600), prevent world access.
Failure simulated: store secret in file, verify file perms are 0o600,
retrieve secret, assert it matches original and file remains protected.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import os
import tempfile
from pathlib import Path

def keyring_store(keyring_path):
    """Context for storing/retrieving secrets in a protected keyring file."""
    class Keyring:
        def __init__(self, fpath):
            self.fpath = fpath
            if Path(self.fpath).exists():
                os.chmod(self.fpath, 0o600)
            else:
                Path(self.fpath).touch()
                os.chmod(self.fpath, 0o600)

        def store_secret(self, key, secret):
            """Store secret in keyring with 0o600 protection."""
            if Path(self.fpath).exists():
                content = Path(self.fpath).read_text()
                data = json.loads(content) if content else {}
            else:
                data = {}
            data[key] = secret
            Path(self.fpath).write_text(json.dumps(data))
            # Ensure perms are 0o600 after write
            os.chmod(self.fpath, 0o600)

        def retrieve_secret(self, key):
            """Retrieve secret from keyring, or None if not found."""
            if not Path(self.fpath).exists():
                return None
            content = Path(self.fpath).read_text()
            if not content:
                return None
            data = json.loads(content)
            return data.get(key)

        def verify_protected(self):
            """Verify file perms are 0o600."""
            if not Path(self.fpath).exists():
                return False
            mode = os.stat(self.fpath).st_mode & 0o777
            return mode == 0o600

    return Keyring(keyring_path)

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        keyring_path = os.path.join(tmpdir, "keyring.json")
        keyring = keyring_store(keyring_path)

        # Store multiple secrets
        secrets_to_store = {
            "db_password": "hunter2_secret",
            "api_key": "sk_test_abcdef123456",
            "oauth_token": "oauth_xyz_token_789",
        }

        for key, secret in secrets_to_store.items():
            keyring.store_secret(key, secret)

        # RECOVERY ASSERT 1: file is protected (0o600)
        assert keyring.verify_protected(), "Keyring file is not 0o600"

        # RECOVERY ASSERT 2: os.stat confirms 0o600
        mode = os.stat(keyring_path).st_mode & 0o777
        assert mode == 0o600, f"Keyring mode is {oct(mode)}, not 0o600"

        # RECOVERY ASSERT 3: all secrets are retrievable
        for key, original_secret in secrets_to_store.items():
            retrieved = keyring.retrieve_secret(key)
            assert retrieved == original_secret, \
                f"Secret for {key} mismatch: {retrieved} != {original_secret}"

        # RECOVERY ASSERT 4: non-existent key returns None
        result = keyring.retrieve_secret("nonexistent")
        assert result is None, f"Nonexistent key returned {result}, not None"

        # RECOVERY ASSERT 5: perms stay 0o600 after multiple operations
        keyring.store_secret("another_key", "another_secret")
        mode_after = os.stat(keyring_path).st_mode & 0o777
        assert mode_after == 0o600, f"Perms changed to {oct(mode_after)} after store"

        print("keyring_store PASS")
