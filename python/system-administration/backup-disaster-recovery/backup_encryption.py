#!/usr/bin/env python3
"""backup_encryption: encrypt backups at rest, verify decryption."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import hmac
from pathlib import Path

def xor_encrypt(data, key):
    """Simple XOR encryption (for demo; in production use AES)."""
    key_hash = hashlib.sha256(key).digest()
    key_expanded = key_hash * (len(data) // len(key_hash) + 1)
    return bytes(a ^ b for a, b in zip(data, key_expanded[:len(data)]))

def create_encrypted_backup(src_dir, backup_dir, passphrase):
    """Create backup with encrypted files."""
    backup_path = Path(backup_dir) / "encrypted"
    backup_path.mkdir(parents=True, exist_ok=True)

    key = passphrase.encode()

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = backup_path / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            content = src_path.read_bytes()
            encrypted = xor_encrypt(content, key)
            dst_path.write_bytes(encrypted)

    return True

def decrypt_backup(backup_dir, restore_dir, passphrase):
    """Restore backup by decrypting files."""
    Path(restore_dir).mkdir(parents=True, exist_ok=True)

    key = passphrase.encode()
    backup_path = Path(backup_dir) / "encrypted"

    for root, dirs, files in os.walk(backup_path):
        for fname in files:
            enc_path = Path(root) / fname
            rel = enc_path.relative_to(backup_path)
            dst_path = Path(restore_dir) / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            encrypted_content = enc_path.read_bytes()
            decrypted = xor_encrypt(encrypted_content, key)  # XOR is symmetric
            dst_path.write_bytes(decrypted)

    return True

def test_backup_encryption():
    """Test: create encrypted backup, fail to decrypt with wrong passphrase, succeed with correct."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backup"

        # Create source files
        (src / "secret.txt").write_text("top_secret_payload_123")
        (src / "config.json").write_text('{"api_key": "secret_key_here"}')

        # Encrypt with passphrase "correct_pass"
        create_encrypted_backup(src, backup_base, "correct_pass")

        # Verify encrypted files are not plaintext
        encrypted_file = (Path(backup_base) / "encrypted" / "secret.txt")
        encrypted_content = encrypted_file.read_bytes()
        original_content = b"top_secret_payload_123"
        assert len(encrypted_content) == len(original_content), "Encrypted size should match original"
        assert encrypted_content != original_content, "File must be encrypted (not plaintext)"

        # Try to decrypt with WRONG passphrase
        restore_wrong = Path(tmpdir) / "restore_wrong"
        decrypt_backup(backup_base, restore_wrong, "wrong_pass")

        # Decrypted content should NOT match original
        decrypted_wrong = (restore_wrong / "secret.txt").read_bytes()
        original = b"top_secret_payload_123"
        assert len(decrypted_wrong) == len(original), "Decrypted file size must match original"
        assert decrypted_wrong != original, "Wrong passphrase must produce wrong output"
        # Verify it's not a coincidence
        num_differences = sum(1 for a, b in zip(decrypted_wrong, original) if a != b)
        assert num_differences > 5, f"Wrong passphrase should differ significantly ({num_differences} bytes)"

        # Decrypt with CORRECT passphrase
        restore_correct = Path(tmpdir) / "restore_correct"
        decrypt_backup(backup_base, restore_correct, "correct_pass")

        # Decrypted content should match original
        decrypted_correct = (restore_correct / "secret.txt").read_bytes()
        assert decrypted_correct == b"top_secret_payload_123", "Correct passphrase should produce original content"

        config_restored = (restore_correct / "config.json").read_text()
        assert config_restored == '{"api_key": "secret_key_here"}', "Config should be fully restored"

        # Verify encrypted file size (should be same as plaintext due to XOR)
        original_size = len("top_secret_payload_123".encode())
        encrypted_size = len(encrypted_content)
        assert encrypted_size == original_size, f"Encrypted size should match original: {encrypted_size} vs {original_size}"

if __name__ == "__main__":
    test_backup_encryption()
    print("✓ backup_encryption passed")
