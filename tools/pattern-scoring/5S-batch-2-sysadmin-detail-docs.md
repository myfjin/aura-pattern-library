# Batch 2 — Sysadmin Pattern Detail Docs (20 patterns)

Categories: `concurrency-locking` (10) + `config-management` (10). Second batch of the Python system-administration sphere.

---

## Category: concurrency-locking

### 1. advisory_lock_timeout.py
**Entry fn:** `def advisory_lock_with_timeout(filename, timeout_sec):`, `def holder(filename, results_dict, hold_time):`, `def waiter_with_timeout(filename, results_dict, timeout_val):`
**Valid input:** `filename` is a writable lockfile path; `timeout_sec` and `hold_time` are positive numbers; the waiter starts after a short delay.
**Core:** Non-blocking advisory lock via `fcntl.flock(LOCK_EX | LOCK_NB)`. If the lock is held, the caller polls every 10 ms until `timeout_sec` elapses, then returns `False`.
**Assert:** Holder acquires and releases; waiter eventually acquires after blocking for at least 0.25 s while the holder holds the lock for 0.5 s.
**⚠️ Defect:** The polling loop is a busy-wait (10 ms sleep) rather than an event-driven wakeup, so it wastes CPU under contention. It does not handle `EINTR` or unexpected `IOError` errno values; any non-EAGAIN error is re-raised.

### 2. atomic_append.py
**Entry fn:** `def atomic_append(filename, lockfile, line, results_dict, writer_id):`
**Valid input:** `filename` and `lockfile` exist and are writable; `line` is a string; multiple concurrent writers are launched from separate processes.
**Core:** File-based read-modify-write append serialized by `fcntl.flock(LOCK_EX)` on a separate lockfile. Reads the whole file, appends `line`, writes the whole file, then releases the lock.
**Assert:** All 20 distinct writer lines survive the concurrent RMW and are present in the final file; no duplicates or torn lines.
**⚠️ Defect:** The entire file is rewritten on every append, which is O(n) write amplification and does not scale. A crash between truncate-and-write can lose all prior content; it is not crash-safe even with the lock.

### 3. cas_file_update.py
**Entry fn:** `def _read(path):`, `def cas_increment(path, lockfile, results_dict, updater_id, barrier):`
**Valid input:** `path` points to a JSON file containing `{"value": int, "version": int}`; `lockfile` exists; multiple updaters start together via the barrier.
**Core:** Optimistic compare-and-swap counter. Reads value+version outside the lock, computes new value, then under a brief `fcntl.flock` re-reads and writes only if the version is unchanged; otherwise retries.
**Assert:** With two concurrent updaters the final value and version are both 2, and at least one real conflict-retry occurred (proving it is CAS, not pessimistic locking).
**⚠️ Defect:** The compare-and-swap serializes under a global file lock, so it is not lock-free; it is optimistic only in the read/compute phase. The lockfile is opened in append mode but the lock is per-process file descriptor, not per-file, so a stale lock from a crashed process could block all future updaters.

### 4. deadlock_timeout.py
**Entry fn:** `class TimeoutLock:`, `def __init__(self):`, `def acquire(self, timeout=None):`, `def release(self):`, `def acquirer(lock1, lock2, lock_order, results, thread_id, timeout, barrier):`
**Valid input:** `timeout` is a non-negative number or `None`; locks are `TimeoutLock` instances; two threads use opposite lock orders to create a cycle.
**Core:** Condition-variable-based lock with timed `acquire`. If the lock is not available within `timeout`, returns `False` instead of blocking forever, allowing the caller to back off and break deadlock.
**Assert:** Two threads acquiring two locks in opposite order produce at least one timeout, and neither thread hangs.
**⚠️ Defect:** `release` does not verify that the calling thread owns the lock, so a thread can release a lock it never acquired. There is no deadlock *detection* (cycle detection), only timeout-and-backoff, so the same cycle can recur.

### 5. double_launch_block.py
**Entry fn:** `class ServiceLauncher:`, `def __init__(self, service_name, tmpdir):`, `def try_launch(self):`, `def launcher_process(service_name, tmpdir, results_dict, launcher_id):`
**Valid input:** `service_name` and `tmpdir` are strings; two launcher processes contend for the same service.
**Core:** PID-file-style singleton launcher. Uses atomic `os.open(O_CREAT | O_EXCL)` to create a lockfile; if held, checks whether the holder PID is alive via `os.kill(pid, 0)`; breaks stale locks if the holder is dead; writes output entries to prove only one instance ran.
**Assert:** Exactly one of two concurrent launches succeeds; the other gets reason `already_running`; the output file contains exactly one "started" and one "running" line.
**⚠️ Defect:** Reading the holder PID from the lockfile is racy (a loop of retries is used, but not atomic with lock creation). `os.kill(pid, 0)` can succeed for a recycled PID, so a stale lock may be treated as live. The lockfile is removed in `finally`, so the singleton guarantee expires the moment the first instance finishes.

### 6. flock_singleton.py
**Entry fn:** `def holder_then_releaser(filename, results_dict):`, `def blocker(filename, results_dict):`
**Valid input:** `filename` is a writable lockfile path; holder and blocker run in separate processes.
**Core:** Demonstrates that `fcntl.flock(LOCK_EX)` genuinely blocks: the holder acquires, sleeps 0.5 s, then releases; the blocker calls `flock` and records the acquisition time.
**Assert:** The blocker acquires only after the holder releases (event ordering); the blocker's relative wait is > 0.25 s, proving it blocked rather than acquiring immediately.
**⚠️ Defect:** This is a demo, not a reusable class. The lock is not tied to any resource or critical section beyond time measurement. `flock` locks are advisory, so any process that ignores them can access the guarded resource anyway.

### 7. idempotent_once_guard.py
**Entry fn:** `def idempotent_action_once(marker_file, results_dict, caller_id):`
**Valid input:** `marker_file` is a writable path; `caller_id` is an identifier; two callers start concurrently.
**Core:** Marker-file guard. Uses `fcntl.flock` to serialize a check-and-run: if the marker file exists, the action is already done; otherwise it increments a counter and writes the marker.
**Assert:** Exactly one caller runs the action (counter == 1); the other caller detects "already done".
**⚠️ Defect:** The marker file is written after the counter increment, so a crash between counter write and marker write would allow a second caller to re-run the action. The marker stores only the PID, not a completion timestamp or checksum.

### 8. named_mutex.py
**Entry fn:** `class NamedMutex:`, `def __init__(self, name):`, `def acquire(self, timeout=None):`, `def release(self):`, `def __enter__(self):`, `def __exit__(self, *args):`, `def critical_section(mutex_name, results_dict, worker_id, hold_time):`
**Valid input:** `name` is a string usable in a filename; `timeout` is `None` or a positive number; workers run in separate processes.
**Core:** Named mutex backed by a temp-directory lockfile. `acquire` uses `os.open(O_CREAT | O_EXCL)`; if the file exists it polls until timeout. Context-manager support is provided.
**Assert:** Two workers each hold a 0.3 s critical section; total wall time is at least ~0.6 s, proving serialization.
**⚠️ Defect:** The mutex is *not* robust: if a worker crashes while holding the lock, the lockfile remains and blocks all future acquirers forever (no heartbeat or stale-lock detection). `release` swallows all exceptions, hiding failures.

### 9. reader_writer_lock.py
**Entry fn:** `class ReaderWriterLock:`, `def __init__(self):`, `def acquire_read(self):`, `def release_read(self):`, `def acquire_write(self):`, `def release_write(self):`, `def reader(lock, res, rid, state):`, `def writer(lock, res, wid, state):`
**Valid input:** The lock is shared among threads; readers and writers use the corresponding acquire/release pairs.
**Core:** Condition-variable-based reader-writer lock. Multiple readers can hold simultaneously; writers wait for all readers to exit and then hold exclusively.
**Assert:** Three concurrent readers finish in roughly one hold time (not three); a writer blocked behind two readers waits > 0.05 s and never overlaps an active reader.
**⚠️ Defect:** The lock is writer-preferring only via `writer_waiting`, but new readers can still slip in before a waiting writer in some wakeups. There is no ownership tracking, so `release_read`/`release_write` can be called by the wrong thread and silently corrupt the counters.

### 10. stale_lock_break.py
**Entry fn:** `def acquire_and_hold_with_pidfile(lockfile, pidfile, results_dict, ready_marker):`, `def detector_and_breaker(lockfile, pidfile, results_dict, ready_marker):`
**Valid input:** `lockfile`, `pidfile`, and `ready_marker` are writable paths in the same temp directory; the holder process is killed with SIGKILL.
**Core:** Detects a stale advisory lock. A holder acquires `flock`, writes its PID, and hangs; a breaker tries non-blocking acquire, reads the PID, waits for the holder to die (which auto-releases the OS lock), and then acquires.
**Assert:** Holder acquires; breaker reads the holder PID and eventually acquires the lock after the holder is killed; breaker does not acquire before the lock is held.
**⚠️ Defect:** The breaker never actually *breaks* the lock; it simply waits for the OS to release it when the holder dies. There is no proactive stale-lock breaker that works when the holder is stuck but alive (e.g., hung in an infinite loop, not dead).

---

## Category: config-management

### 11. config_diff.py
**Entry fn:** `def config_diff(old_config, new_config):`
**Valid input:** `old_config` and `new_config` are dicts with comparable values.
**Core:** Computes the difference between two flat configs: keys added, keys removed, and keys changed (with old and new values as a tuple).
**Assert:** Added key, removed key, changed value, complex add/remove/change, and identical configs all produce the expected diff structure.
**⚠️ Defect:** Only top-level keys are compared; nested dict values are compared by equality but not diffed recursively. Values must be equality-comparable, which breaks for unhashable or non-eq types like custom objects.

### 12. config_versioning.py
**Entry fn:** `def compute_config_hash(config_dict):`, `def validate_config_version(config_file, expected_version):`
**Valid input:** `config_file` contains a JSON wrapper with `version`, `content`, and `content_hash` fields; `expected_version` is a string.
**Core:** Hashes the `content` dict deterministically (sorted JSON + SHA-256) and compares it with the stored `content_hash`, catching content drift without a version bump.
**Assert:** Matching version and hash pass; version mismatch, content drift, and missing fields are rejected with explicit `ValueError` messages.
**⚠️ Defect:** The version string is arbitrary and not enforced to be monotonic; an attacker can bump the version to match any content. The hash is computed over JSON serialization, so semantically identical configs with different key ordering would hash the same, but any formatting difference in the source file is lost.

### 13. dotenv_parse.py
**Entry fn:** `def parse_dotenv(filepath):`
**Valid input:** `filepath` points to a `.env` file with `KEY=VALUE` lines, comments (`#`), and blank lines.
**Core:** Line-by-line dotenv parser. Strips lines, skips comments/blanks, splits on the first `=`, strips whitespace, and removes matching surrounding single/double quotes.
**Assert:** Simple key-values, quoted values, comments/blanks, missing `=`, empty key, and exact line-number reporting all behave as expected.
**⚠️ Defect:** Does not handle inline comments (`KEY=val # comment` would include the comment in the value), escaped quotes, variable expansion (`$OTHER`), or multiline values. Quote stripping is naive and can mangle values like `"say "hello""`.

### 14. env_load_defaults.py
**Entry fn:** `def env_load_defaults(required_vars, optional_defaults=None):`
**Valid input:** `required_vars` is a list of environment-variable names; `optional_defaults` is a dict of name → default value.
**Core:** Loads required environment variables, raising `KeyError` with the exact missing name if absent; fills optional variables from the environment or their defaults.
**Assert:** Required vars load, missing required raises with the var name, optional defaults apply, and present optional vars override defaults.
**⚠️ Defect:** Modifies the process-global `os.environ` in its own tests by popping keys, which is not isolated. There is no type conversion or validation beyond presence; every value is returned as a string.

### 15. hot_reload.py
**Entry fn:** `class HotConfig:`, `def __init__(self, filepath):`, `def reload(self):`, `def get(self, key):`
**Valid input:** `filepath` is a JSON config file; keys requested via `get` exist in the current config.
**Core:** Loads a JSON config at init and on explicit `reload`; caches values in memory; `get` reads from the cache.
**Assert:** Initial values load; after modifying the file and calling `reload`, new values are visible; a third reload also works.
**⚠️ Defect:** `reload` is manual, not automatic or file-watch-driven, so stale config is used until someone calls it. There is no error handling for a malformed JSON file during reload; a bad reload would crash the caller.

### 16. layered_merge.py
**Entry fn:** `def layered_merge(layers, required_keys=None):`
**Valid input:** `layers` is a list of dicts; `required_keys` is a list of keys that must exist in the merged result.
**Core:** Merges config layers in order, with later layers overriding earlier ones. Raises `KeyError` if any required key is missing from the final merged dict.
**Assert:** Later layers override earlier values; required keys present pass; missing required keys are reported by name.
**⚠️ Defect:** Merging is shallow; nested dicts are replaced rather than recursively merged. There is no type checking or conflict reporting for keys that appear in multiple layers.

### 17. multiformat_load.py
**Entry fn:** `def load_config(filepath):`
**Valid input:** `filepath` has a `.json`, `.ini`, or `.env` suffix and contains valid syntax for that format.
**Core:** Dispatches to `json.load`, `configparser.ConfigParser`, or a simple dotenv parser based on file extension.
**Assert:** Valid JSON, INI, and dotenv files load; invalid syntax for each format and unsupported extensions are rejected with format-specific error messages.
**⚠️ Defect:** INI values are returned as strings (configparser default), so type information is lost. The dotenv parser is duplicated from `dotenv_parse.py` and inherits its limitations. YAML/TOML are unsupported.

### 18. refuse_start_on_invalid.py
**Entry fn:** `def validate_and_load_config(config_file, required_fields):`
**Valid input:** `config_file` is a JSON file; `required_fields` is a list of top-level keys; when present, `port` must be an int in 1–65535 and `timeout` must be a positive number.
**Core:** Loads JSON config and validates required fields plus hardcoded semantic checks for `port` and `timeout`. Raises precise `ValueError` messages prefixed with "REFUSE START".
**Assert:** Valid config loads; missing required field, wrong port type, out-of-range port, negative timeout, missing file, and invalid JSON are all rejected with descriptive errors.
**⚠️ Defect:** Validation rules for `port` and `timeout` are hardcoded, so the function cannot validate arbitrary config schemas. It does not return the loaded config in a structured way; callers must parse the returned dict themselves.

### 19. schema_validate.py
**Entry fn:** `def schema_validate(config, schema):`
**Valid input:** `config` is a dict; `schema` is a dict mapping required keys to expected type names as strings (e.g., `"str"`, `"int"`).
**Core:** Checks that every key in `schema` exists in `config` and that its value's `type().__name__` matches the expected type name.
**Assert:** Valid config passes; missing required key and wrong type are rejected with the field name in the error; extra keys are allowed.
**⚠️ Defect:** Type checking is string-name based, so legitimate subclasses or numeric compatibility (e.g., `bool` is a subclass of `int`) are not handled. Nested schemas, optional keys, and value-range constraints are unsupported.

### 20. secret_separation.py
**Entry fn:** `def load_config_with_secrets(config_file, secret_file):`
**Valid input:** `config_file` is a JSON file with only non-secret keys; `secret_file` is a JSON file containing `api_key`, `db_password`, and `token`.
**Core:** Loads regular config and secrets separately. Raises `ValueError` if any known secret key leaks into the regular config; raises `FileNotFoundError` if the secret file is missing; raises `KeyError` if required secrets are absent.
**Assert:** Proper separation returns both dicts; leaked secret in regular config, missing secret file, and missing required secret are all detected.
**⚠️ Defect:** The set of secret keys (`api_key`, `db_password`, `token`) is hardcoded, so adding a new secret type requires editing the function. There is no encryption of the secret file; it is plain JSON on disk.
