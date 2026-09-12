# Batch 1 — Sysadmin Pattern Detail Docs (20 patterns)

Categories: `access-control-audit` (10) + `backup-disaster-recovery` (10). First batch of the Python system-administration sphere.

---

## Category: access-control-audit

### 1. append_only_audit.py
**Entry fn:** `def sha256(data):`, `class AppendOnlyAudit:`, `def __init__(self, log_path):`, `def append(self, event):`, `def _write(self):`, `def verify_chain(self):`
**Valid input:** `event` is any JSON-serializable value; `log_path` is writable.
**Core:** Append-only audit log where each entry stores the SHA-256 hash of `{event, prev_hash}` and links to the previous entry's hash. `verify_chain` recomputes every hash from the genesis `0...0` and raises `ValueError` on any mismatch.
**Assert:** A three-event chain verifies cleanly; after flipping a byte in the first event on disk and reloading, `verify_chain` raises with "hash mismatch" or "chain broken".
**⚠️ Defect:** `append` rewrites the entire log to disk after every event, so write amplification is O(n²) for n entries. Reloading is left to the caller (the demo manually populates `entries` from disk); there is no `load` method, so the class is not self-contained.

### 2. command_allowlist.py
**Entry fn:** `class CommandAllowlist:`, `def __init__(self, allowed_commands):`, `def check(self, cmd, args):`
**Valid input:** `allowed_commands` is a dict mapping command names to lists of allowed argument strings (or `"*"` for any args); `cmd` is a string; `args` is a string.
**Core:** Whitelist guard. Returns `True` if `cmd` is present and `args` matches one of the allowed patterns; raises `ValueError` for unknown commands or disallowed arguments.
**Assert:** `ls /tmp`, `cat /etc/passwd`, `echo hello world`, and `grep -i` pass; `rm -rf`, `cat /etc/shadow`, and `grep -r` are rejected with `ValueError`.
**⚠️ Defect:** Argument matching is exact-string equality, so patterns like `/etc/passwd` are brittle (a path containing a trailing slash or `..` bypasses the allowlist). The wildcard `"*"` is all-or-nothing per command, offering no granular control.

### 3. immutable_audit.py
**Entry fn:** `def sha256(data):`, `class ImmutableAudit:`, `def __init__(self, log_path, secret_key):`, `def append(self, event):`, `def seal(self):`, `def _write(self):`, `def verify_seal(self):`
**Valid input:** `event` is any JSON-serializable object; `secret_key` is a string or bytes; sealing happens before verification.
**Core:** HMAC-SHA-256 sealed audit log. `seal` signs the sorted JSON serialization of all entries; `verify_seal` reloads the file and recomputes the HMAC, raising `ValueError` if tampering is detected.
**Assert:** Sealed log verifies; after changing an entry on disk, `verify_seal` raises with "tampering detected".
**⚠️ Defect:** Appending after sealing is correctly rejected, but the class never records that an append-was-attempted. There is no `load` method, so callers must manually assign `entries`, `sealed`, and `seal_signature` from the JSON record before verifying.

### 4. least_privilege_verify.py
**Entry fn:** `class PrivilegeChecker:`, `def __init__(self):`, `def grant(self, user, privilege):`, `def revoke(self, user, privilege):`, `def check(self, user, required_priv):`
**Valid input:** `user` and `privilege` are hashable identifiers; a user must exist and hold `required_priv` for `check` to succeed.
**Core:** Minimal-privilege enforcer. Maintains `user -> set(privilege)`; `check` raises `ValueError` for missing users, missing privileges, or attempts to use a revoked privilege.
**Assert:** Alice with only `read_files` passes `read_files` but is blocked from `write_files`, `delete_files`, and `admin`; after granting and then revoking `write_files`, the privilege is denied again.
**⚠️ Defect:** `check` leaks the user's full privilege set in the error message, which is a minor information-disclosure side channel. There is no concept of roles or inheritance, so real least-privilege policies must be flattened manually.

### 5. permission_matrix.py
**Entry fn:** `class PermissionMatrix:`, `def __init__(self):`, `def grant(self, user, resource, action):`, `def check(self, user, resource, action):`, `def verify_integrity(self, expected):`
**Valid input:** `user`, `resource`, `action` are hashable identifiers; `expected` has the same nested dict-of-sets shape as the internal matrix.
**Core:** User × resource × action matrix. `grant` adds an action; `check` raises `ValueError` on missing user, resource, or action; `verify_integrity` compares the entire matrix against an expected structure.
**Assert:** Granted permissions pass `check`; adding an unauthorized action or removing a legitimate one is caught by `verify_integrity` with "action mismatch".
**⚠️ Defect:** Direct mutation of `matrix.perms` (as the tests do) is required to simulate tampering, exposing the internal dict to callers. The integrity check compares only the current snapshot and does not protect the matrix between grant/check operations.

### 6. priv_escalation_detect.py
**Entry fn:** `class PrivilegeMonitor:`, `def __init__(self):`, `def snapshot(self, user_privileges):`, `def detect_escalation(self):`
**Valid input:** `user_privileges` is a dict mapping users to sets of privileges; at least two snapshots are needed for detection.
**Core:** State-change detector. Records privilege snapshots and compares the latest with the previous one, returning `(True, {user: new_privs})` if any user gained privileges.
**Assert:** Identical snapshots produce no escalation; adding `write` to alice, `admin` to bob, and simultaneous escalations across multiple users are all detected.
**⚠️ Defect:** Only privilege *additions* are flagged; privilege *removals* (de-escalation) are silently ignored. The snapshot is stored as a shallow copy, so if the caller mutates a nested privilege set in place, the stored history may change.

### 7. rbac_check.py
**Entry fn:** `def rbac_enforce(user_role, resource, action, role_perms):`
**Valid input:** `user_role` exists in `role_perms`; `role_perms` maps roles to resources to lists of permitted actions.
**Core:** Role-based access-control enforcer. Raises `ValueError` for unknown roles, unknown resources for a role, or actions not listed for the role-resource pair.
**Assert:** Admin `delete files`, user `write files`, and guest `read files` pass; user `delete files`, guest `write files`, and user `delete users` are denied.
**⚠️ Defect:** Role permissions are passed in on every call rather than being encapsulated, so policy drift between calls is possible. There is no support for dynamic role hierarchy or deny-rules; every permission must be explicitly listed.

### 8. session_record.py
**Entry fn:** `def sha256(data):`, `class SessionRecorder:`, `def __init__(self, session_file):`, `def record_event(self, event_type, details):`, `def seal(self):`, `def _write(self):`, `def verify_integrity(self):`, `def list_events(self):`
**Valid input:** `event_type` and `details` are JSON-serializable; `session_file` is writable.
**Core:** Session recorder with hash integrity. Records login/command/logout events, seals by hashing the sorted JSON of all events, and detects on-disk tampering by recomputing the hash.
**Assert:** Four recorded events list correctly and verify after sealing; modifying a command to `rm -rf /` on disk triggers "tampering" / "hash mismatch" on reload.
**⚠️ Defect:** Timestamps are simulated by event index (`len(self.events)`), not real time, so event ordering is just insertion order. Like the other audit classes, there is no `load` method; callers must manually populate fields from the JSON record before calling `verify_integrity`.

### 9. sudo_self_body_guard.py
**Entry fn:** `class SudoGuard:`, `def check_command(self, cmd):`
**Valid input:** `cmd` is a string representing a command that may be run under sudo.
**Core:** Regex-based guard against self-destructive sudo commands. Raises `ValueError` when `cmd` matches dangerous patterns (`rm -rf /`, `dd if=/dev/zero of=/`, `mkfs`, etc.).
**Assert:** Safe commands (`apt-get install`, `systemctl restart`, `usermod`) pass; `rm -rf /etc/important`, `dd if=/dev/zero of=/dev/sda`, `chmod -r /`, and `mkfs.ext4 /dev/sda1` are blocked.
**⚠️ Defect:** Pattern `rm\s+-rf\s+/` only matches literal `/` at the end, missing variants like `rm -rf --no-preserve-root /` or `rm -rf /*`. The check is purely syntactic and can be bypassed by aliases, encoded spaces, or shell expansion.

### 10. tamper_evident_chain.py
**Entry fn:** `def sha256(data):`, `class MerkleTree:`, `def __init__(self):`, `def add_leaf(self, data):`, `def build_tree(self):`, `def verify_leaf(self, leaf_index, expected_leaf_data):`, `def verify_root(self, tampered_leaves=None):`
**Valid input:** Leaves are bytes-like or string data; `leaf_index` is in range; `tampered_leaves` is a dict of index → replacement data.
**Core:** Simple Merkle tree. Pairwise SHA-256 hashes are combined level by level to produce a root; `verify_root` rebuilds the tree with optional tampered leaves and compares the resulting root.
**Assert:** Clean tree verifies; replacing leaf 0 with `b"event: user alice HACKED"` or leaf 1 with tampered data raises "root mismatch".
**⚠️ Defect:** `verify_leaf` compares hashes rather than raw data (`sha256(expected) != sha256(original)`), so it never validates the caller's expected data against the stored leaf content. The tree does not store internal node hashes, so it cannot produce or verify a real Merkle proof path.

---

## Category: backup-disaster-recovery

### 11. backup_catalog.py
**Entry fn:** `def create_backup_entry(backup_id, metadata):`, `def build_backup_catalog(backup_dir, catalog_dir):`, `def search_catalog(catalog_dir, query):`, `def get_backup_stats(catalog_dir):`, `def test_backup_catalog():`
**Valid input:** `backup_dir` contains directories matching `backup_*`; `catalog_dir` is writable; `query` is a lowercase substring or retention tag.
**Core:** Scans backup directories, builds `catalog.json` and `summary.json` with per-backup size/file-count metadata plus totals, and supports search by ID or retention tag.
**Assert:** Three synthetic backups produce a 3-entry catalog with proportional sizes; search finds exact and substring matches; summary total size matches the sum of entries.
**⚠️ Defect:** `search_catalog` only checks the literal query against the backup ID and the `retention_tag` field; there is no full-text metadata search. The catalog is rebuilt from scratch every call rather than incrementally updated, so large backup trees are rescanned repeatedly.

### 12. backup_dedup.py
**Entry fn:** `def chunk_file(path, chunk_size=4096):`, `def backup_with_dedup(src_dir, backup_dir, chunk_size=4096):`, `def restore_from_dedup(backup_dir, restore_dir):`, `def test_backup_dedup():`
**Valid input:** Source directory contains readable files; `chunk_size` is positive.
**Core:** Content-defined deduplicating backup. Files are split into fixed-size chunks, chunks are stored content-addressed by SHA-256, and a manifest records per-file chunk lists. Restore reassembles files from chunks.
**Assert:** Three files sharing a 4 KB chunk store only one physical chunk with three references; restore reproduces originals; corrupting the shared chunk breaks the content-address invariant and propagates to every referencing file.
**⚠️ Defect:** Fixed-size chunking means small boundary shifts duplicate all subsequent chunks. The store does not verify chunk hashes on read, so silent corruption is only detectable if a caller re-hashes; the restore fails only if the chunk is outright missing.

### 13. backup_encryption.py
**Entry fn:** `def xor_encrypt(data, key):`, `def create_encrypted_backup(src_dir, backup_dir, passphrase):`, `def decrypt_backup(backup_dir, restore_dir, passphrase):`, `def test_backup_encryption():`
**Valid input:** Passphrase is a string; source directory contains files.
**Core:** XOR-based symmetric encryption of backup files. Each file is XORed with a SHA-256-derived key stream; the same function decrypts because XOR is self-inverse.
**Assert:** Encrypted files differ from plaintext and have the same length; decryption with the wrong passphrase yields content that differs in many bytes; decryption with the correct passphrase restores the originals exactly.
**⚠️ Defect:** XOR with a SHA-256-derived repeated key stream is not semantically secure and is vulnerable to known-plaintext attacks. Identical files produce identical ciphertexts, leaking file equality. The implementation explicitly labels itself demo-only.

### 14. full_incremental_backup.py
**Entry fn:** `def compute_checksum(path):`, `def backup_full(src_dir, backup_dir):`, `def backup_incremental(src_dir, backup_dir, level_num, last_manifest):`, `def restore_from_backup(backup_dir, restore_dir):`, `def test_full_incremental_backup():`
**Valid input:** Source directory exists; `level_num` is a positive integer; `last_manifest` maps relative paths to SHA-256 hashes.
**Core:** Full backup writes all files to `level0` with a manifest; incremental backups write only changed files to `levelN` using checksum comparison. Restore overlays levels in order so later incremental changes win.
**Assert:** Full backup contains two files; incremental captures a modified file and a new file; restore after deleting the source yields the latest version of every file and matching checksums.
**⚠️ Defect:** There is no compaction or expiration of old incremental levels, so a long chain slows restores and consumes space. Deleted files in the source are not explicitly tracked; a deleted file from an early level can reappear if a later level does not overwrite it.

### 15. offsite_integrity.py
**Entry fn:** `def create_offsite_backup(src_dir, offsite_dir):`, `def verify_offsite_integrity(offsite_dir):`, `def test_offsite_integrity():`
**Valid input:** Source directory contains files; `offsite_dir` is writable; `offsite_dir/checksums.json` exists after backup creation.
**Core:** Creates a local copy simulating an offsite backup and stores per-file SHA-256 checksums. Verification compares the offsite copy against the stored checksums and raises `ValueError` on missing files or hash mismatches.
**Assert:** Fresh offsite copy verifies; replacing a file with `CORRUPTED_BY_ATTACKER`, flipping a byte, or deleting a file are all detected with "hash mismatch" or "missing".
**⚠️ Defect:** Checksums are stored alongside the offsite copy in the same directory tree, so an attacker with access to the offsite store can recompute and replace checksums after tampering. There is no separation of checksums to a truly remote/trusted location.

### 16. restore_drill.py
**Entry fn:** `def create_test_backup(src_dir, backup_dir, label):`, `def run_restore_drill(backup_dir, backup_label, drill_restore_dir):`, `def test_restore_drill():`
**Valid input:** Source directory exists; backup label is unique; backup contains a `manifest.json` with per-file checksums.
**Core:** Creates labeled backups with checksum manifests and runs a restore drill: restores the backup to a fresh directory and verifies every restored file matches its original checksum.
**Assert:** Drills for three backups restore the correct point-in-time content; corrupting a file in a backup before the drill causes checksum mismatch and a failed drill.
**⚠️ Defect:** `run_restore_drill` copies dotfiles by skipping only `fname.startswith(".")`, but the manifest itself (`manifest.json`) is also a regular file and gets restored into the drill directory, polluting the restore. Restored file paths are reconstructed by `relative_to(backup_path)`, which fails if the backup contains absolute-symlink-like structures.

### 17. restore_verify.py
**Entry fn:** `def create_backup_with_manifest(src_dir, backup_dir):`, `def verify_backup(backup_dir):`, `def restore_verified(backup_dir, restore_dir):`, `def test_restore_verify():`
**Valid input:** Source directory exists; backup directory is writable.
**Core:** Creates a backup with a per-file SHA-256 manifest. `verify_backup` checks every file's presence and hash; `restore_verified` only restores after verification succeeds.
**Assert:** Fresh backup verifies and restores correctly; corrupting `file1.txt` in the backup makes `verify_backup` raise with "hash mismatch", and `restore_verified` fails rather than restore corrupted data.
**⚠️ Defect:** `verify_backup` and `restore_verified` both walk `backup_dir/data` independently; a race between verification and restore could allow a file to be corrupted after verification but before copy. There is no checksum verification of the restored copy itself.

### 18. retention_policy.py
**Entry fn:** `class InjectedClock:`, `def __init__(self, start_time=0):`, `def advance(self, seconds):`, `def now(self):`, `def create_backup(backup_dir, backup_id, clock):`, `def apply_retention_policy(backup_dir, policy_config, clock):`, `def test_retention_policy():`
**Valid input:** `policy_config` contains `max_age_seconds` (int or `inf`) and `min_count` (int); backups are directories named `backup_*` containing `timestamp.txt`.
**Core:** Age- and count-based backup retention. Sorts backups newest-first, keeps the newest `min_count`, and additionally keeps any backup whose age is within `max_age_seconds`.
**Assert:** With five hourly backups, a 2-hour age policy plus `min_count=2` keeps the three newest backups and deletes the oldest; a count-only policy keeps exactly the newest three.
**⚠️ Defect:** The policy does not handle ties or equal timestamps; when `max_age` is infinite, only `min_count` matters, but the code still computes ages unnecessarily. There is no guard against `min_count=0`, which would delete every backup.

### 19. rpo_rto_measure.py
**Entry fn:** `class InjectedClock:`, `def __init__(self, start_time=0):`, `def advance(self, seconds):`, `def now(self):`, `def backup_with_timestamp(src_dir, backup_dir, clock):`, `def restore_with_timer(backup_dir, restore_dir, clock, seconds_per_file=2):`, `def measure_rpo_rto():`
**Valid input:** Source directory exists; `seconds_per_file` is non-negative; separate clock instances are used for backup and restore timelines.
**Core:** Measures recovery-point objective (time between backups) and recovery-time objective (restore duration) using injected clocks. Each restored file advances the restore clock by `seconds_per_file`, making RTO a measured function of work rather than a constant.
**Assert:** Backups at time 0 and 3600 give RPO = 3600; restoring one file with `seconds_per_file=2` yields RTO = 2; restored content matches the latest backup.
**⚠️ Defect:** `backup_with_timestamp` names the backup directory with the current clock value, but if two backups occur at the same clock tick they collide. The restore-time model is linear per file and ignores directory traversal, metadata operations, or parallelism.

### 20. snapshot_chain.py
**Entry fn:** `def create_snapshot(src_dir, snapshot_dir, snapshot_id, parent_id=None):`, `def restore_from_snapshot(snapshot_dir, snapshot_id, restore_dir):`, `def test_snapshot_chain():`
**Valid input:** Source directory exists; snapshot IDs are unique; `parent_id` is either `None` or an existing snapshot ID.
**Core:** Copy-on-write-style snapshot chain. Each snapshot stores a manifest with its parent and content-addressed files; restore walks the parent chain from newest to oldest, applying older snapshots first so newer ones override.
**Assert:** Snapshots link `snap1 <- snap2 <- snap3`; restoring from each snapshot yields the correct point-in-time content, including inherited files from parents.
**⚠️ Defect:** True deduplication against the parent is not implemented—the comment says it would check the parent's manifest but the code stores every file in every snapshot. The restore chain stops if a snapshot directory is missing, even if enough data exists in descendants. Cycle detection only breaks on revisiting an ID and does not report an error.
