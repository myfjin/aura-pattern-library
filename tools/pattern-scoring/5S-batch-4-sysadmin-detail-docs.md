# Batch 4 — Sysadmin Pattern Detail Docs (20 patterns)

Categories: `filesystem-integrity` (10) + `log-management` (10). Fourth batch of the Python system-administration sphere.

---

## Category: filesystem-integrity

### 1. atomic_snapshot.py
**Entry fn:** `def atomic_snapshot(source_path, snapshot_path):`
**Valid input:** `source_path` points to an existing file; `snapshot_path` is a writable path in the same filesystem as the temp file used for staging.
**Core:** Reads the entire source file into memory, writes it to a temp file next to `snapshot_path`, then atomically renames the temp file over `snapshot_path` so the snapshot is never partial.
**Assert:** After `atomic_snapshot`, `snapshot_path` contains the exact original bytes; modifying the source afterward leaves the snapshot unchanged; sizes match.
**⚠️ Defect:** The snapshot requires enough memory to hold the entire source file and enough free space to temporarily store a second copy. It does not preserve file metadata (mtime, permissions); it only copies content. There is no incremental or CoW efficiency.

### 2. atomic_write_temp_rename.py
**Entry fn:** `def atomic_write(target_path, content):`, `def _wait_until(pred, timeout=3.0):`
**Valid input:** `target_path` is a writable file path; `content` is bytes; `_wait_until` takes a predicate and an optional timeout.
**Core:** Writes `content` to a temp file in the target directory and renames it over `target_path`. The bundled `_wait_until` helper polls a predicate until the timeout expires.
**Assert:** A simulated crash after the temp file is fully written but before the rename leaves the original target intact; a subsequent clean atomic replace succeeds with the new content; no leaked temp files remain.
**⚠️ Defect:** Atomicity depends on same-filesystem `os.rename`, which is POSIX-typical but not guaranteed everywhere. The function returns nothing, so callers cannot verify which path was actually written. `_wait_until` is a busy-poll with 5 ms sleeps, not event-driven.

### 3. checksum_corruption_detect.py
**Entry fn:** `def compute_checksum(path, algo="sha256"):`, `def verify_checksum(path, expected_checksum, algo="sha256"):`
**Valid input:** `path` points to an existing file; `algo` is a hashlib-supported algorithm name; `expected_checksum` is a hex string.
**Core:** Streams the file through `hashlib.new(algo)` in 64 KiB chunks and returns the hex digest; `verify_checksum` recomputes and raises `ValueError` on mismatch.
**Assert:** Original checksum verifies; flipping a single byte at offset 512 produces a different checksum and causes `verify_checksum` to raise; verifying against the corrupted checksum passes.
**⚠️ Defect:** No verification of the algorithm name — an unsupported `algo` will raise from `hashlib.new` rather than a controlled error. The function reads the whole file, so it is unsuitable for streaming or very large files without a more chunked strategy. It does not store checksums alongside files.

### 4. cow_backup.py
**Entry fn:** `def cow_backup(source_path, backup_path):`
**Valid input:** `source_path` points to an existing file; `backup_path` is a writable path.
**Core:** Performs an eager full copy (source → temp → atomic rename) to produce a backup that is independent of the source. Despite the name, this is not filesystem-level copy-on-write.
**Assert:** Backup matches source at backup time; corrupting the source afterward does not affect the backup; the backup differs from the corrupted source.
**⚠️ Defect:** The docstring honestly discloses this is an eager full copy, not real CoW, so it wastes space and time compared to filesystem CoW. It copies entire files into memory (`read_bytes`), so it cannot handle files larger than RAM. It does not preserve metadata or support incremental backups.

### 5. dir_tree_diff.py
**Entry fn:** `def tree_checksum_index(root_dir):`, `def tree_diff(tree1_index, tree2_index):`
**Valid input:** `root_dir` is a directory containing regular files; indexes are dicts returned by `tree_checksum_index`.
**Core:** Walks a directory, computes `{relative_path: (size, sha256)}` for every file, and compares two indexes to classify paths as added, removed, modified, or unchanged.
**Assert:** Identical trees show no diff; modifying a file, adding a file, and removing a file are each detected with the correct classification; unchanged files are reported as unchanged.
**⚠️ Defect:** Only regular files are indexed; directories, symlinks, and metadata are ignored. The index is recomputed from scratch for each diff, so large trees are expensive. Empty directories are not represented at all. File permissions and timestamps are not compared.

### 6. disk_full_write_guard.py
**Entry fn:** `class QuotaGuard:`, `def __init__(self, quota_bytes):`, `def write_file(self, path, content):`, `def get_used(self):`, `def remaining(self):`
**Valid input:** `quota_bytes` is a non-negative int; `path` is a writable file path; `content` is bytes.
**Core:** Tracks cumulative bytes written; refuses any write that would exceed the quota by raising `ValueError`. Successful writes use temp+rename for atomicity.
**Assert:** Sequential writes within quota succeed and update `used`; a write that would exceed quota is refused; existing files remain intact; no temp files leak; `remaining()` reaches zero at the exact quota boundary.
**⚠️ Defect:** The guard tracks bytes by counting the requested content size, not the actual on-disk allocation, so holes, filesystem overhead, and concurrent writers are ignored. It has no concept of reclaiming space after deleting or truncating files. The quota is global to the instance, not per-directory or per-user.

### 7. fsync_durability.py
**Entry fn:** `def durable_write(path, data):`, `def _recording_fsync(fd):`
**Valid input:** `path` is a writable file path; `data` is bytes; `_recording_fsync` is a monkeypatch helper used only in tests.
**Core:** Opens the file in binary write mode, writes `data`, flushes the Python buffer, and calls `os.fsync` on the file descriptor before returning.
**Assert:** Tests monkeypatch `os.fsync` with `_recording_fsync` to prove exactly one fsync is invoked on a valid fd; after write+reopen the bytes match; a second overwrite replaces content exactly.
**⚠️ Defect:** True durability across power loss cannot be proven in-process; the pattern only demonstrates that `os.fsync` is called. The function opens with `"wb"`, so it truncates on every call rather than appending. There is no error path that retries or reports fsync failure separately from write failure.

### 8. restore_from_backup.py
**Entry fn:** `def create_backup(source_path, backup_path):`, `def restore_from_backup(backup_path, target_path):`
**Valid input:** `source_path` and `backup_path` are writable file paths; `target_path` is a writable file path.
**Core:** `create_backup` copies source → backup via temp+rename; `restore_from_backup` copies backup → target via temp+rename, overwriting the target atomically.
**Assert:** Backup equals source; after corrupting source, `restore_from_backup` restores it byte-for-byte to the original; restored size and header/tail match; restored data differs from corrupted data.
**⚠️ Defect:** Both functions read the entire file into memory, so they do not scale to large files. They do not preserve metadata. There is no versioning: restoring always overwrites the target and cannot roll back a bad restore.

### 9. safe_delete_trash.py
**Entry fn:** `def safe_delete_to_trash(file_path, trash_dir):`
**Valid input:** `file_path` points to an existing file; `trash_dir` is a writable directory (created if missing).
**Core:** Moves the file into `trash_dir` with a microsecond timestamp prefix on the basename to avoid collisions, preserving the original data for recovery.
**Assert:** The original path no longer exists; the file exists in trash with identical content; exactly one file appears in trash; the file can be moved back out and matches the original; trash is empty after recovery.
**⚠️ Defect:** Cross-filesystem moves are not handled; if `trash_dir` is on a different filesystem, `os.rename` will raise. Directory metadata and permissions are not preserved. There is no automatic expiration or quota on the trash directory.

### 10. symlink_escape_guard.py
**Entry fn:** `def safe_symlink(link_path, target_path, root_dir):`
**Valid input:** `link_path` is the path where the symlink will be created; `target_path` is the symlink target (relative or absolute); `root_dir` is the directory the resolved target must stay within.
**Core:** Resolves the target relative to the link's directory, takes the absolute path, and raises `ValueError` unless it starts with the absolute root directory path.
**Assert:** Symlinks pointing outside the root are blocked; traversal symlinks (`../../..`) are blocked; safe relative symlinks inside the root are created and resolve correctly; absolute outside paths are blocked.
**⚠️ Defect:** The containment check uses string prefix matching (`startswith(abs_root + os.sep)`), which can be bypassed by tricky paths that do not normalize correctly. It does not use `pathlib.Path.resolve()` or realpath, so symlinks inside the root that point outside are not followed for validation. The function creates the symlink even if the target file does not exist.

---

## Category: log-management

### 11. crash_log_capture.py
**Entry fn:** `def crash_during_write_simulator(log_path, crash_after_n=5):`
**Valid input:** `log_path` is a writable JSON-lines file path; `crash_after_n` is a non-negative int.
**Core:** Simulates a crash mid-write by writing `crash_after_n` complete JSON entries followed by a truncated JSON line, then reads the file back, skipping malformed lines and counting complete entries.
**Assert:** At least 3 and at most `crash_after_n` complete entries are recovered; exactly one malformed line is detected; recovered entries are sequential with no gaps; the crash index itself is not present.
**⚠️ Defect:** The recovery loop swallows all exceptions with bare `except:` and bare `except json.JSONDecodeError`, so unrelated I/O errors are silently ignored. The function both writes and parses the log, so it is a simulator, not a reusable crash-recovery utility. It does not truncate or repair the corrupted file.

### 12. log_compression.py
**Entry fn:** `def compress_log_file(log_path, compression_level=9):`
**Valid input:** `log_path` points to an existing file; `compression_level` is an int in the gzip range 0–9.
**Core:** Reads the original log, writes it to `log_path.gz` at the given compression level, deletes the original, and returns `(original_size, compressed_size)`.
**Assert:** Compressed size is non-zero and smaller than the original; compression ratio is below 0.6 for the repetitive test data; the original file is removed and the `.gz` file exists with the reported size.
**⚠️ Defect:** The function reads the entire log into memory before compressing, so it does not stream large logs. It deletes the original unconditionally; there is no option to keep it. The compression ratio assertion depends on highly repetitive input and will fail on already-compressed or random data.

### 13. rate_limited_log.py
**Entry fn:** `def rate_limited_logger(limit_per_sec=100):`, `def log_entry(text):`
**Valid input:** `limit_per_sec` is a positive number; `text` is a string.
**Core:** Returns a closure implementing a token-bucket rate limiter; tokens refill continuously based on elapsed time, and a log is emitted only when at least one token is available.
**Assert:** Firing 1000 logs in a burst emits at most `2 * limit_per_sec` and strictly fewer than 1000, proving that some logs are dropped/throttled.
**⚠️ Defect:** The function returns only a boolean, so the actual log text is discarded — it is a rate-limit gate, not a real logger. Token state is stored in mutable single-element lists (`[limit_per_sec]`, `[time.time()]`) unnecessarily. There is no log of dropped messages, so operators cannot know what was lost.

### 14. retention_prune.py
**Entry fn:** `def prune_by_count(log_dir, keep_count=5):`
**Valid input:** `log_dir` is a directory containing `*.log` files; `keep_count` is a non-negative int.
**Core:** Sorts `*.log` files by modification time and deletes all but the `keep_count` newest, returning the number deleted.
**Assert:** Creating 100 `.log` files with staggered mtimes and pruning with `keep_count=5` leaves exactly 5 files; deleted count is 95; the remaining files are the newest by index.
**⚠️ Defect:** Only files matching `*.log` are considered; other extensions or subdirectories are ignored. Sorting by mtime is fragile — touching a file changes its retention rank. There is no protection against deleting the currently active log if it happens to be old.

### 15. ring_buffer_log.py
**Entry fn:** `def ring_buffer_log(max_size):`, `def log_entry(text):`, `def get_all():`
**Valid input:** `max_size` is a positive int; `text` is a string.
**Core:** Uses a `collections.deque(maxlen=max_size)` as an in-memory FIFO ring buffer; appending beyond the capacity evicts the oldest entry.
**Assert:** Pushing `max_size` entries then `max_size` more leaves exactly `max_size` entries; the oldest entries from the first batch are gone; the newest entries are present; no first-batch indices remain.
**⚠️ Defect:** The buffer is purely in-memory and is lost when the process exits. There is no persistence, no timestamps, and no log levels. The returned functions are closures, so the buffer cannot be inspected or queried from outside the pair.

### 16. rotate_by_size.py
**Entry fn:** `def rotate_by_size(log_path, size_cap_bytes=1000, keep_rotations=2):`, `def append_line(text):`
**Valid input:** `log_path` is a writable file path; `size_cap_bytes` and `keep_rotations` are positive ints; `text` is a string.
**Core:** Appends lines to the current log; when the next line would exceed `size_cap_bytes`, it shifts existing rotations `.1` → `.2` (up to `keep_rotations`), moves the current log to `.1`, and starts a fresh current log.
**Assert:** Flooding 1100 lines of ~91 bytes each with cap 1000 and 2 rotations keeps total on-disk bytes ≤ `cap * (keep_rotations + 1)`; at most `keep_rotations` rotated files exist.
**⚠️ Defect:** Rotation is triggered by the next append exceeding the cap, so the current log can grow slightly beyond `size_cap_bytes`. The loop that deletes old rotations only removes the highest index, not any file older than `keep_rotations`. It reads file stats but does not use temp+rename, so a crash during rotation can leave torn or missing logs.

### 17. rotate_by_time.py
**Entry fn:** `def rotate_by_time(log_path, rotation_interval_sec=5, keep_duration_sec=10):`, `def append_line(text, now):`
**Valid input:** `log_path` is a writable file path; `rotation_interval_sec` and `keep_duration_sec` are positive numbers; `now` is a timestamp (logical clock); `text` is a string.
**Core:** Uses a mutable `last_rotation` timestamp and an explicit `now` parameter to rotate logs at intervals; rotated files are stamped with the fake clock via `os.utime`, and files older than `keep_duration_sec` relative to `now` are pruned.
**Assert:** Writing at times `0,5,...,25` with interval 5 and window 30 accumulates rotations; jumping to `now=100` and writing once prunes every surviving file older than the window; the current log remains.
**⚠️ Defect:** The entire age mechanism depends on the caller supplying a consistent logical clock; mixing real mtimes with fake timestamps breaks the pruning logic. Rotation renames the current log without fsync, so a crash can lose the most recent entries. The function returns only the append closure, so rotation state is not externally observable.

### 18. secret_redaction.py
**Entry fn:** `def redacting_logger(log_path, redact_patterns=None):`, `def log_entry(text):`
**Valid input:** `log_path` is a writable file path; `redact_patterns` is a list of `(regex, replacement)` tuples or `None` for defaults.
**Core:** Applies regex substitutions (default patterns for `api_key`, `password`, `token`) before appending the line to the log file.
**Assert:** Logging lines containing an API key, password, and token results in none of the raw secrets appearing in the file; all three redaction markers are present; a normal line without secrets is preserved unchanged.
**⚠️ Defect:** The default secret patterns are hardcoded and may miss other secret formats (e.g., `Authorization: Bearer <token>`). The function reads the entire log before every append, which is O(n²). Regex redaction can be bypassed by encoding or spacing variations. The `log_file.read_text()` call is not safe if the log is large or contains non-UTF-8 bytes.

### 19. structured_json_log.py
**Entry fn:** `def structured_logger(log_path):`, `def log_event(event_dict):`, `def parse_json_log(log_path):`
**Valid input:** `log_path` is a writable file path; `event_dict` is JSON-serializable.
**Core:** `structured_logger` returns a closure that appends JSON-serialized dicts as lines; `parse_json_log` reads the file line by line, counts valid JSON lines, and skips malformed ones.
**Assert:** Writing 100 valid events and manually injecting 50 malformed lines yields `valid_count == 100` and `skip_count == 50`; parsing does not crash.
**⚠️ Defect:** `log_event` reads the whole file before appending, which is inefficient and racy under concurrency. There is no timestamp or severity field added automatically. `parse_json_log` swallows all exceptions with bare `except`, so real I/O errors are silently ignored and the counts may be wrong.

### 20. tail_follow.py
**Entry fn:** `class TailFollower:`, `def __init__(self, log_path):`, `def read_new_lines(self):`
**Valid input:** `log_path` is a readable file path.
**Core:** Maintains a file-position cursor; each call to `read_new_lines` seeks to the saved position, reads all new lines, updates the cursor, and returns the new lines with trailing newlines stripped.
**Assert:** First follow reads all 50 initial lines; after appending 30 more lines, the same follower returns exactly those 30 new lines with no duplicates; returned lines match the expected content.
**⚠️ Defect:** The follower does not handle log truncation or rotation; if the file shrinks, the seek may land past EOF and silently return nothing. It opens the file on every call, so rapidly growing logs may see inconsistent reads. It swallows all exceptions and returns `[]`, hiding permission errors or missing files.
