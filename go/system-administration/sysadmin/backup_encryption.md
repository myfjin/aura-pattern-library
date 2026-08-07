# backup encryption

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 13 · Backup & disaster recovery

## What it does

backup_encryption: encrypt backups at rest, verify decryption.

## Guarantee

When it runs, backup encryption guarantees len(encrypted_content) == len(original_content); encrypted_content != original_content; len(decrypted_wrong) == len(original) (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `len(encrypted_content) == len(original_content)`
- `encrypted_content != original_content`
- `len(decrypted_wrong) == len(original)`
- `decrypted_wrong != original`
- `num_differences > 5`
- `decrypted_correct == b'top_secret_payload_123'`
- `config_restored == '{"api_key": "secret_key_here"}'`
- `encrypted_size == original_size`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def xor_encrypt(data, key):`, `def create_encrypted_backup(src_dir, backup_dir, passphrase):`, `def decrypt_backup(backup_dir, restore_dir, passphrase):`, `def test_backup_encryption():`
**Valid input:** Passphrase is a string; source directory contains files.
**Core:** XOR-based symmetric encryption of backup files. Each file is XORed with a SHA-256-derived key stream; the same function decrypts because XOR is self-inverse.
**Assert:** Encrypted files differ from plaintext and have the same length; decryption with the wrong passphrase yields content that differs in many bytes; decryption with the correct passphrase restores the originals exactly.
**⚠️ Defect:** XOR with a SHA-256-derived repeated key stream is not semantically secure and is vulnerable to known-plaintext attacks. Identical files produce identical ciphertexts, leaking file equality. The implementation explicitly labels itself demo-only.

---
*△ AURA Pattern Library — © Reality Optimizer*
