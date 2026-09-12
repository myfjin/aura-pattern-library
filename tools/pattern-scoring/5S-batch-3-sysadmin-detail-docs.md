# Batch 3 — Sysadmin Pattern Detail Docs (20 patterns)

Categories: `data-pipeline-ops` (10) + `deployment-rollback` (10). Third batch of the Python system-administration sphere.

---

## Category: data-pipeline-ops

### 1. backfill_range.py
**Entry fn:** `def backfill_range(records, range_start, range_end, backfill_path):`
**Valid input:** `records` is a list of dicts each containing `'seq'`; `range_start` and `range_end` are ints defining the inclusive sequence range to fill; `backfill_path` is a writable JSON path that persists processed ranges.
**Core:** Computes gaps in the sequence range, skips the whole range if it was already backfilled (recorded in `backfill_path`), otherwise appends synthetic backfill records and persists the new range.
**Assert:** Sparse records `seq 1,3,5` backfilled to `[1,5]` produce 5 records with gaps 2 and 4 marked `source='backfill'`; re-running the same range yields zero new fills and no duplicates.
**⚠️ Defect:** The gap-filling logic mutates the input `records` list in place. The per-record processing order is not transactional: if the process crashes after writing some backfilled records but before persisting the range, a retry could duplicate those records. The synthetic backfill value is just `f'backfilled_{seq}'`, with no schema integration.

### 2. checkpoint_resume.py
**Entry fn:** `def process_batch_with_checkpoint(records, checkpoint_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `checkpoint_path` is a writable JSON path; batch size is fixed at 2.
**Core:** Processes records in batches of 2, writing a checkpoint (`batches_done` with batch id → processed records) after each batch commits; on resume, completed batches are replayed from the checkpoint.
**Assert:** Four records processed after a simulated crash after batch 0 yield all four records exactly once, in order, with `processed == value + 100`.
**⚠️ Defect:** The checkpoint stores full record outputs, so it grows linearly with input size. The batch size is hardcoded to 2. There is no cleanup of old checkpoints, and an interrupted checkpoint write leaves a partial JSON file that will crash the next run.

### 3. exactly_once_dedup.py
**Entry fn:** `def deduplicate_stream(records, dedup_journal_path):`
**Valid input:** `records` is a list of dicts with unique `'id'` values plus intentional duplicates; `dedup_journal_path` is a writable JSON path.
**Core:** Maintains a journal set of processed record IDs; writes the journal before processing each record (write-ahead); skips any record whose ID is already journalized.
**Assert:** A stream `[a,b,c,c,d]` produces 4 processed records and 1 skipped duplicate; after a crash/resume replay the same stream skips the already-seen IDs and processes only new ones.
**⚠️ Defect:** Deduplication is by ID only, so two different records with the same ID are treated as duplicates even if their payloads differ. The journal is rewritten in full after every record, which is O(n²) write amplification for large streams. There is no journaling of skipped records beyond their count.

### 4. idempotent_etl_step.py
**Entry fn:** `def idempotent_transform(records, checkpoint_path):`, `def stable_checksum(value):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `checkpoint_path` is a writable JSON path.
**Core:** Transforms each record (`value * 2` + SHA-256-derived checksum) and checkpoints the serialized output keyed by record ID before adding it to the output; on resume, already-checkpointed IDs are replayed from the checkpoint.
**Assert:** Full transform and crash/resume transform produce identical, duplicate-free outputs; checksums match the original value.
**⚠️ Defect:** The checkpoint is overwritten after every single record, so throughput is low for large inputs. The checksum uses only the first 8 hex chars of SHA-256, which is much weaker than a full hash. The function mutates/checkpoints based on `'id'` only, so a record whose value changes between runs would still be skipped.

### 5. lineage_track.py
**Entry fn:** `def transform_with_lineage(records, lineage_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `lineage_path` is a writable JSON path.
**Core:** Maps each input record to exactly one output record, persisting the lineage (`source_id`, `output_id`, `output_value`) before adding the output; on resume, already-tracked IDs are replayed from lineage.
**Assert:** Every output record has a matching lineage entry and every lineage entry points to an output record; after a simulated crash/resume the lineage stays consistent with no dangling references.
**⚠️ Defect:** Lineage is 1-to-1 only; patterns that fan out or fan in are not represented. The lineage file stores the full output payload, so it grows with output size. Like the other checkpoint patterns, it rewrites the entire lineage file after every record.

### 6. partition_manage.py
**Entry fn:** `def process_partitioned(records, partition_meta_path):`
**Valid input:** `records` is a list of dicts with `'id'`, `'partition'`, and `'value'`; `partition_meta_path` is a writable JSON path.
**Core:** Tracks per-partition processed counts and a closed-partition list; records belonging to a closed partition are skipped; a partition is closed once it reaches `max_per_partition=2` records.
**Assert:** Processing 2 records for partition `p1` plus 1 for `p2` closes `p1`; a second batch with more `p1` records skips them while accepting additional `p2` records.
**⚠️ Defect:** The closure threshold is hardcoded to 2, which is arbitrary and unsuitable for real partitions. Partition closure is irreversible in the current run, so late-arriving records for a closed partition are silently dropped rather than quarantined or logged.

### 7. pipeline_dead_letter.py
**Entry fn:** `def process_with_dlq(records, dlq_path, retry_limit=3):`, `class ProcessingError(Exception):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; failing records are marked with `'bad_record': True`; `dlq_path` is a writable JSON path.
**Core:** Retries each record up to `retry_limit` times; records that still fail are appended to a dead-letter queue (DLQ) JSON file together with the original record, error message, and retry count.
**Assert:** Out of 4 records with 2 bad ones and `retry_limit=1`, exactly 2 are processed and 2 land in the DLQ with no overlap and no lost IDs; a single bad record retried 3 times records `retry_count == 3`.
**⚠️ Defect:** The DLQ is appended to memory but the file is only flushed when a record finally fails; a crash mid-retry could lose DLQ entries. There is no backoff between retries. Successfully processed records are not persisted, so an overall pipeline retry could reprocess them.

### 8. replay_safe.py
**Entry fn:** `def replay_safe_aggregate(records, state_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `state_path` is a writable JSON path.
**Core:** Recomputes aggregate statistics (sum, count, max, min) from the full input set every call and overwrites the state file, making the aggregate commutative and replay-safe.
**Assert:** First run and replay with identical input produce identical aggregates; reordering the same records also produces identical aggregates.
**⚠️ Defect:** The function ignores any previously persisted state and recomputes from scratch, which is correct for commutativity but wastes work for incremental streams. It does not handle missing/None values or non-numeric inputs. The initial `state` dict loaded from disk is immediately discarded, so partial crash recovery of incremental state is impossible.

### 9. schema_drift_detect.py
**Entry fn:** `def detect_schema_drift(records, schema_path):`, `def infer_schema(records):`, `class SchemaDriftError(Exception):`
**Valid input:** `records` is a non-empty list of dicts; `schema_path` is a writable JSON path.
**Core:** Infers a schema `{field: type_name}` from the records and stores it on first run; on subsequent runs, compares the current schema to the stored schema and reports new fields, removed fields, and type changes.
**Assert:** First run stores schema with no drift; adding `'email'` and changing `'age'` from int to float reports both a new-field and a type-change drift; removing `'ssn'` reports a removed-field drift.
**⚠️ Defect:** `SchemaDriftError` is defined but never raised; drift is returned as a plain list of strings. Schema inference marks a field as `'mixed'` if type conflicts occur within the same batch, but this mixed type is not explicitly reported as drift. The stored schema is always updated after each run, so drift is ephemeral unless captured by the caller.

### 10. watermark_track.py
**Entry fn:** `def process_with_watermark(records, watermark_path):`
**Valid input:** `records` is a list of dicts with `'id'`, `'timestamp'`, and `'value'`; `watermark_path` is a writable JSON path.
**Core:** Tracks the highest timestamp processed in `watermark_path`; on each run, skips records with `timestamp <=` current watermark and updates the watermark after each processed record.
**Assert:** First batch `10,20,30` yields watermark 30 and 3 processed; second batch containing the same old records plus `40,50` skips 3 old records and processes 2 new ones with watermark 50.
**⚠️ Defect:** Out-of-order records with timestamps below the watermark are silently skipped, so late-arriving data is lost. The watermark is rewritten after every record, which is fine for small streams but inefficient for high-throughput pipelines. The initial watermark defaults to 0, which would skip any records with non-positive timestamps.

---

## Category: deployment-rollback

### 11. atomic_symlink_swap.py
**Entry fn:** `class AtomicSymlinkSwap:`, `def __init__(self, live_link_path):`, `def deploy(self, new_target_path):`, `def get_target(self):`, `def link_exists(self):`
**Valid input:** `live_link_path` is an absolute or relative path for the live symlink; `new_target_path` points to an existing directory.
**Core:** Creates a temporary symlink `live_link.tmp` pointing to the new target, then atomically renames it over `live_link` so the live pointer is never dangling during the swap.
**Assert:** After deployment the symlink resolves to the new target; if the process crashes after staging the temp link but before the rename, the original live link remains valid; rolling back re-points to the previous target.
**⚠️ Defect:** Atomicity relies on `os.rename` being atomic for symlinks on the same filesystem, which is true on POSIX but not universally guaranteed. The temp link is removed at the start of each deploy, so a concurrent deploy could race. There is no verification that the *contents* of the target are healthy before switching.

### 12. blue_green_deploy.py
**Entry fn:** `class BlueGreenDeploy:`, `def __init__(self, workspace_path):`, `def get_active_color(self):`, `def deploy_to_inactive(self, app_code):`, `def switch_active(self, new_color):`, `def get_active_dir(self):`
**Valid input:** `workspace_path` is a writable directory; `app_code` is a string; `new_color` is `'blue'` or `'green'`.
**Core:** Maintains two directories (`blue/` and `green/`); deploys new code to whichever directory is currently inactive, then atomically flips the active color via a JSON state file.
**Assert:** Initial active color is `'blue'`; deploying writes to the inactive (`green`) directory without affecting active traffic; switching makes green active and subsequent deploys go to blue; zero-downtime sequence works.
**⚠️ Defect:** `switch_active` writes the state file directly (not via temp+rename), so a crash during the write can leave the active color corrupted. `deploy_to_inactive` clears files but does not remove stale subdirectories, and it never validates `app_code` syntax or health.

### 13. canary_gate.py
**Entry fn:** `class CanaryGate:`, `def __init__(self, error_threshold=0.05):`, `def increase_canary_traffic(self, percent):`, `def record_canary_request(self, success):`, `def record_stable_request(self, success):`, `def get_canary_error_rate(self):`, `def is_healthy(self):`, `def should_rollback(self):`
**Valid input:** `error_threshold` is a float between 0 and 1; `percent` is a non-negative traffic percentage; `success` is a boolean.
**Core:** Tracks canary and stable request/error counts; compares canary error rate against the threshold; provides `is_healthy()` and `should_rollback()` decisions.
**Assert:** Canary starts at 0 traffic; traffic increases are capped at 100%; 1% error rate passes the default 5% threshold; 10% error rate triggers rollback; error rate exactly at threshold is considered healthy.
**⚠️ Defect:** The class does not actually shift traffic; it only records statistics and returns decisions. Stable errors are tracked but never used in the health decision. There is no minimum sample size, so one early failure could trigger rollback with a tiny denominator.

### 14. config_drift_detect.py
**Entry fn:** `class ConfigDriftDetect:`, `def __init__(self):`, `def set_expected(self, config_dict):`, `def scan_actual(self, config_dict):`, `def has_drift(self):`, `def get_drift_details(self):`
**Valid input:** `config_dict` is a flat dict of comparable values.
**Core:** Stores an expected config hash, computes a hash of the actual config, and reports drift details: missing keys, extra keys, and changed values with old/new tuples.
**Assert:** Matching configs report no drift; value change, missing key, and extra key are each detected; multiple drift issues are reported simultaneously; rescanning after remediation clears drift.
**⚠️ Defect:** Only flat dictionaries are supported; nested configs are compared by overall hash, so inner key-level drift is opaque. `_compute_hash` imports `json` inside the method, which is unnecessary. The detector does not suggest or apply remediation.

### 15. deplock_verify.py
**Entry fn:** `class DeplockVerify:`, `def __init__(self):`, `def load_lock(self, lock_dict):`, `def verify_lock_integrity(self):`, `def add_dependency(self, pkg_name, version, dep_hash):`, `def verify_package(self, pkg_name, expected_version, expected_hash):`
**Valid input:** `lock_dict` maps package names to `(version, hash)` tuples; `expected_version` and `expected_hash` are strings.
**Core:** Loads a dependency lock dictionary, computes its SHA-256 hash, and verifies that later modifications change the hash; also verifies individual package version/hash against the lock.
**Assert:** Lock hash is unchanged immediately after load; tampering with a package entry makes `verify_lock_integrity()` return `False`; matching package version/hash pass, mismatches raise `ValueError`, and missing packages raise `ValueError`.
**⚠️ Defect:** The hash is computed from an in-memory dict, so the lock file itself is not validated against an independent source hash. `add_dependency` silently overwrites existing entries. Hashes in the example are fake short strings (`"abc123"`), so the demonstration does not prove real cryptographic verification.

### 16. deploy_idempotency.py
**Entry fn:** `class IdempotentDeploy:`, `def __init__(self):`, `def deploy(self, version, skip_if_current=True):`, `def get_current_version(self):`, `def get_deployment_count(self, version):`, `def is_deployed(self, version):`
**Valid input:** `version` is a string; `skip_if_current` is a boolean.
**Core:** Tracks the currently deployed version and a per-version deployment counter; when `skip_if_current=True`, redeploying the current version succeeds without incrementing the counter.
**Assert:** Redeploying the same version with skip is a no-op (count stays 1); redeploying with `skip_if_current=False` counts each attempt; switching versions updates current version; network retry scenarios leave count at 1.
**⚠️ Defect:** There is no notion of rollback or previous version. The counter is only incremented when `skip_if_current=False`, but the current version is set on every call, so a skipped redeploy still counts as a deployment event semantically. No actual deployment artifact is produced.

### 17. health_gated_promote.py
**Entry fn:** `class HealthGatedPromote:`, `def __init__(self):`, `def deploy(self, version):`, `def run_health_check(self, check_name, should_pass):`, `def promote(self):`, `def get_active_version(self):`, `def get_deployed_version(self):`
**Valid input:** `version` is a string; `check_name` is a string; `should_pass` is a boolean.
**Core:** Separates `deployed_version` (staged) from `active_version` (promoted); `promote()` succeeds only if at least one health check was run and all recorded checks passed.
**Assert:** Passing all checks promotes the staged version to active; a failing check blocks promotion and keeps active unchanged; promoting without running any checks raises `RuntimeError`; deployed and active versions can differ.
**⚠️ Defect:** Health checks are simulated booleans, not real probes. There is no timeout or retry on checks. Once promoted, there is no rollback path; a bad promotion must be handled externally. The gate does not ensure the deployed version is still the one that was health-checked.

### 18. immutable_release.py
**Entry fn:** `class ImmutableRelease:`, `def __init__(self, releases_dir):`, `def create_release(self, version, content):`, `def get_release(self, version):`, `def release_exists(self, version):`, `def prevent_modification(self, version):`
**Valid input:** `releases_dir` is a writable directory; `version` is a unique string; `content` is a string.
**Core:** Creates versioned subdirectories under `releases_dir`; rejects duplicate version creation; stores metadata in memory and writes an `artifact.txt`; `prevent_modification` sets the artifact read-only (`0o444`).
**Assert:** Creating a release makes it retrievable; duplicate creation raises `ValueError`; multiple versions coexist; the artifact file is read-only after `prevent_modification`; nonexistent release access raises `ValueError`.
**⚠️ Defect:** The in-memory `self.released` dict is not persisted, so process restart loses release metadata even though directories remain. `prevent_modification` only sets file permissions and does not protect the version directory itself. The artifact name is hardcoded to `artifact.txt`.

### 19. rollback_on_failure.py
**Entry fn:** `class RollbackOnFailure:`, `def __init__(self):`, `def deploy(self, version):`, `def mark_unhealthy(self, reason):`, `def rollback(self):`, `def should_rollback(self):`, `def get_current_version(self):`
**Valid input:** `version` is a string; `reason` is a string describing the failure.
**Core:** Tracks `current_version` and `previous_version`; when the current version is marked unhealthy, `should_rollback()` returns `True`; `rollback()` restores `current_version` to `previous_version` and clears the unhealthy flag.
**Assert:** Healthy deployment does not rollback; marking unhealthy triggers rollback recommendation; rollback restores previous version; rollback without previous version raises `RuntimeError`; multi-version chain rolls back one step at a time.
**⚠️ Defect:** There is no automatic rollback trigger; the caller must poll `should_rollback()` and call `rollback()`. Only one previous version is remembered, so rolling back twice in a row just toggles between the last two versions. Health state is a single boolean with no time-based decay.

### 20. version_pin_verify.py
**Entry fn:** `class VersionPinVerify:`, `def __init__(self):`, `def pin_version(self, version, expected_hash):`, `def compute_hash(self, content):`, `def verify_deployment(self, version, actual_content):`
**Valid input:** `version` is a string; `expected_hash` is a 64-char hex SHA-256 string; `actual_content` is the deployed string.
**Core:** Registers a SHA-256 hash pin per version and verifies that the actual deployed content hashes to the pinned value.
**Assert:** Matching content passes; mismatched content raises `ValueError`; unpinned version raises `ValueError`; same content yields same hash, different content yields different hash, and a single-byte change is detected.
**⚠️ Defect:** There is no mechanism to discover or fetch the actual deployed content; the caller must supply it. The hash is computed over UTF-8 string content, so binary artifacts must be decoded first. Pin registry is in-memory only and is lost on process restart.
