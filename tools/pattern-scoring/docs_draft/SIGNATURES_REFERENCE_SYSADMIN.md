# AUTHORITATIVE SIGNATURE REFERENCE — python/system-administration (COPY VERBATIM)

## access-control-audit
### append_only_audit.py
```python
def sha256(data):
class AppendOnlyAudit:
def __init__(self, log_path):
def append(self, event):
def _write(self):
def verify_chain(self):
```
### command_allowlist.py
```python
class CommandAllowlist:
def __init__(self, allowed_commands):
def check(self, cmd, args):
```
### immutable_audit.py
```python
def sha256(data):
class ImmutableAudit:
def __init__(self, log_path, secret_key):
def append(self, event):
def seal(self):
def _write(self):
def verify_seal(self):
```
### least_privilege_verify.py
```python
class PrivilegeChecker:
def __init__(self):
def grant(self, user, privilege):
def revoke(self, user, privilege):
def check(self, user, required_priv):
```
### permission_matrix.py
```python
class PermissionMatrix:
def __init__(self):
def grant(self, user, resource, action):
def check(self, user, resource, action):
def verify_integrity(self, expected):
```
### priv_escalation_detect.py
```python
class PrivilegeMonitor:
def __init__(self):
def snapshot(self, user_privileges):
def detect_escalation(self):
```
### rbac_check.py
```python
def rbac_enforce(user_role, resource, action, role_perms):
```
### session_record.py
```python
def sha256(data):
class SessionRecorder:
def __init__(self, session_file):
def record_event(self, event_type, details):
def seal(self):
def _write(self):
def verify_integrity(self):
def list_events(self):
```
### sudo_self_body_guard.py
```python
class SudoGuard:
def check_command(self, cmd):
```
### tamper_evident_chain.py
```python
def sha256(data):
class MerkleTree:
def __init__(self):
def add_leaf(self, data):
def build_tree(self):
def verify_leaf(self, leaf_index, expected_leaf_data):
def verify_root(self, tampered_leaves=None):
```

## backup-disaster-recovery
### backup_catalog.py
```python
def create_backup_entry(backup_id, metadata):
def build_backup_catalog(backup_dir, catalog_dir):
def search_catalog(catalog_dir, query):
def get_backup_stats(catalog_dir):
def test_backup_catalog():
```
### backup_dedup.py
```python
def chunk_file(path, chunk_size=4096):
def backup_with_dedup(src_dir, backup_dir, chunk_size=4096):
def restore_from_dedup(backup_dir, restore_dir):
def test_backup_dedup():
```
### backup_encryption.py
```python
def xor_encrypt(data, key):
def create_encrypted_backup(src_dir, backup_dir, passphrase):
def decrypt_backup(backup_dir, restore_dir, passphrase):
def test_backup_encryption():
```
### full_incremental_backup.py
```python
def compute_checksum(path):
def backup_full(src_dir, backup_dir):
def backup_incremental(src_dir, backup_dir, level_num, last_manifest):
def restore_from_backup(backup_dir, restore_dir):
def test_full_incremental_backup():
```
### offsite_integrity.py
```python
def create_offsite_backup(src_dir, offsite_dir):
def verify_offsite_integrity(offsite_dir):
def test_offsite_integrity():
```
### restore_drill.py
```python
def create_test_backup(src_dir, backup_dir, label):
def run_restore_drill(backup_dir, backup_label, drill_restore_dir):
def test_restore_drill():
```
### restore_verify.py
```python
def create_backup_with_manifest(src_dir, backup_dir):
def verify_backup(backup_dir):
def restore_verified(backup_dir, restore_dir):
def test_restore_verify():
```
### retention_policy.py
```python
class InjectedClock:
def __init__(self, start_time=0):
def advance(self, seconds):
def now(self):
def create_backup(backup_dir, backup_id, clock):
def apply_retention_policy(backup_dir, policy_config, clock):
def test_retention_policy():
```
### rpo_rto_measure.py
```python
class InjectedClock:
def __init__(self, start_time=0):
def advance(self, seconds):
def now(self):
def backup_with_timestamp(src_dir, backup_dir, clock):
def restore_with_timer(backup_dir, restore_dir, clock, seconds_per_file=2):
def measure_rpo_rto():
```
### snapshot_chain.py
```python
def create_snapshot(src_dir, snapshot_dir, snapshot_id, parent_id=None):
def restore_from_snapshot(snapshot_dir, snapshot_id, restore_dir):
def test_snapshot_chain():
```

## concurrency-locking
### advisory_lock_timeout.py
```python
def advisory_lock_with_timeout(filename, timeout_sec):
def holder(filename, results_dict, hold_time):
def waiter_with_timeout(filename, results_dict, timeout_val):
```
### atomic_append.py
```python
def atomic_append(filename, lockfile, line, results_dict, writer_id):
```
### cas_file_update.py
```python
def _read(path):
def cas_increment(path, lockfile, results_dict, updater_id, barrier):
```
### deadlock_timeout.py
```python
class TimeoutLock:
def __init__(self):
def acquire(self, timeout=None):
def release(self):
def acquirer(lock1, lock2, lock_order, results, thread_id, timeout, barrier):
```
### double_launch_block.py
```python
class ServiceLauncher:
def __init__(self, service_name, tmpdir):
def try_launch(self):
def launcher_process(service_name, tmpdir, results_dict, launcher_id):
```
### flock_singleton.py
```python
def holder_then_releaser(filename, results_dict):
def blocker(filename, results_dict):
```
### idempotent_once_guard.py
```python
def idempotent_action_once(marker_file, results_dict, caller_id):
```
### named_mutex.py
```python
class NamedMutex:
def __init__(self, name):
def acquire(self, timeout=None):
def release(self):
def __enter__(self):
def __exit__(self, *args):
def critical_section(mutex_name, results_dict, worker_id, hold_time):
```
### reader_writer_lock.py
```python
class ReaderWriterLock:
def __init__(self):
def acquire_read(self):
def release_read(self):
def acquire_write(self):
def release_write(self):
def reader(lock, res, rid, state):
def writer(lock, res, wid, state):
```
### stale_lock_break.py
```python
def acquire_and_hold_with_pidfile(lockfile, pidfile, results_dict, ready_marker):
def detector_and_breaker(lockfile, pidfile, results_dict, ready_marker):
```

## config-management
### config_diff.py
```python
def config_diff(old_config, new_config):
```
### config_versioning.py
```python
def compute_config_hash(config_dict):
def validate_config_version(config_file, expected_version):
```
### dotenv_parse.py
```python
def parse_dotenv(filepath):
```
### env_load_defaults.py
```python
def env_load_defaults(required_vars, optional_defaults=None):
```
### hot_reload.py
```python
class HotConfig:
def __init__(self, filepath):
def reload(self):
def get(self, key):
```
### layered_merge.py
```python
def layered_merge(layers, required_keys=None):
```
### multiformat_load.py
```python
def load_config(filepath):
```
### refuse_start_on_invalid.py
```python
def validate_and_load_config(config_file, required_fields):
```
### schema_validate.py
```python
def schema_validate(config, schema):
```
### secret_separation.py
```python
def load_config_with_secrets(config_file, secret_file):
```

## data-pipeline-ops
### backfill_range.py
```python
def backfill_range(records, range_start, range_end, backfill_path):
def test_backfill_range():
def test_backfill_idempotent():
def test_failure_no_backfill_tracking():
def buggy_backfill(records, range_start, range_end):
```
### checkpoint_resume.py
```python
def process_batch_with_checkpoint(records, checkpoint_path):
def test_checkpoint_resume():
def test_failure_missing_checkpoint():
def buggy_process(records):
```
### exactly_once_dedup.py
```python
def deduplicate_stream(records, dedup_journal_path):
def test_exactly_once_dedup():
def test_crash_and_resume():
def test_failure_no_dedup_journal():
def buggy_process(stream):
```
### idempotent_etl_step.py
```python
def stable_checksum(value):
def idempotent_transform(records, checkpoint_path):
def test_idempotent_etl():
def norm(recs):
def test_failure_non_idempotent():
def buggy_transform(records, last_offset):
```
### lineage_track.py
```python
def transform_with_lineage(records, lineage_path):
def test_lineage_track():
def test_lineage_consistency():
def test_failure_no_lineage():
def buggy_transform(records):
```
### partition_manage.py
```python
def process_partitioned(records, partition_meta_path):
def test_partition_manage():
def test_partition_closed_immutable():
def test_failure_no_partition_tracking():
def buggy_process(records):
```
### pipeline_dead_letter.py
```python
class ProcessingError(Exception):
def process_with_dlq(records, dlq_path, retry_limit=3):
def test_pipeline_dlq():
def test_dlq_retry_exhaustion():
def test_failure_no_dlq():
def buggy_process(records):
```
### replay_safe.py
```python
def replay_safe_aggregate(records, state_path):
def test_replay_safe():
def test_replay_order_independence():
def test_failure_stateful_accumulation():
class StatefulBuggy:
def __init__(self):
def aggregate(self, records):
```
### schema_drift_detect.py
```python
class SchemaDriftError(Exception):
def infer_schema(records):
def detect_schema_drift(records, schema_path):
def test_schema_drift_detect():
def test_schema_removed_field():
def test_failure_no_schema_tracking():
def buggy_process(records):
```
### watermark_track.py
```python
def process_with_watermark(records, watermark_path):
def test_watermark_track():
def test_watermark_monotonic():
def test_failure_no_watermark():
def buggy_process(records):
```

## deployment-rollback
### atomic_symlink_swap.py
```python
class AtomicSymlinkSwap:
def __init__(self, live_link_path):
def deploy(self, new_target_path):
def get_target(self):
def link_exists(self):
def test_atomic_swap_points_to_new_target():
def test_swap_maintains_link_validity():
def test_crash_between_temp_and_rename_leaves_live_intact():
def test_reject_nonexistent_target():
def test_rollback_to_previous():
def test_multiple_deployments():
```
### blue_green_deploy.py
```python
class BlueGreenDeploy:
def __init__(self, workspace_path):
def get_active_color(self):
def deploy_to_inactive(self, app_code):
def switch_active(self, new_color):
def get_active_dir(self):
def test_deploy_to_inactive():
def test_atomic_switch():
def test_switch_back_on_failure():
def test_get_active_directory():
def test_zero_downtime_deploy():
```
### canary_gate.py
```python
class CanaryGate:
def __init__(self, error_threshold=0.05):
def increase_canary_traffic(self, percent):
def record_canary_request(self, success):
def record_stable_request(self, success):
def get_canary_error_rate(self):
def is_healthy(self):
def should_rollback(self):
def test_canary_starts_at_zero():
def test_increase_canary_traffic():
def test_healthy_canary_continues():
def test_unhealthy_canary_triggers_rollback():
def test_error_rate_at_threshold():
def test_rollback_clears_canary():
def test_gradual_ramp_up():
```
### config_drift_detect.py
```python
class ConfigDriftDetect:
def __init__(self):
def set_expected(self, config_dict):
def scan_actual(self, config_dict):
def _compute_hash(self, config_dict):
def has_drift(self):
def get_drift_details(self):
def test_no_drift():
def test_detect_value_change():
def test_detect_missing_config():
def test_detect_extra_config():
def test_multiple_drift_issues():
def test_drift_allows_remediation():
def test_empty_configs():
def test_large_config_drift():
```
### deplock_verify.py
```python
class DeplockVerify:
def __init__(self):
def load_lock(self, lock_dict):
def _compute_lock_hash(self):
def verify_lock_integrity(self):
def add_dependency(self, pkg_name, version, dep_hash):
def verify_package(self, pkg_name, expected_version, expected_hash):
def test_load_lock_file():
def test_detect_lock_tampering():
def test_verify_package_success():
def test_verify_package_version_mismatch():
def test_verify_package_hash_mismatch():
def test_reject_missing_package():
def test_add_dependency_updates_hash():
def test_multiple_package_verification():
```
### deploy_idempotency.py
```python
class IdempotentDeploy:
def __init__(self):
def deploy(self, version, skip_if_current=True):
def get_current_version(self):
def get_deployment_count(self, version):
def is_deployed(self, version):
def test_idempotent_redeploy():
def test_redeploy_counts_attempts():
def test_redeploy_without_skip_counts_separately():
def test_switch_versions():
def test_idempotent_network_retry():
def test_multiple_idempotent_redeploys():
def test_deployment_order_matters():
```
### health_gated_promote.py
```python
class HealthGatedPromote:
def __init__(self):
def deploy(self, version):
def run_health_check(self, check_name, should_pass):
def promote(self):
def get_active_version(self):
def get_deployed_version(self):
def test_promote_after_passing_checks():
def test_reject_promote_if_check_fails():
def test_require_health_checks_before_promote():
def test_deployed_vs_active():
def test_all_checks_must_pass():
def test_promotion_chain():
```
### immutable_release.py
```python
class ImmutableRelease:
def __init__(self, releases_dir):
def create_release(self, version, content):
def get_release(self, version):
def release_exists(self, version):
def prevent_modification(self, version):
def test_create_release():
def test_reject_duplicate_release():
def test_release_immutable():
def test_multiple_releases():
def test_reject_nonexistent_release():
def test_release_directory_isolation():
def test_release_archival():
```
### rollback_on_failure.py
```python
class RollbackOnFailure:
def __init__(self):
def deploy(self, version):
def mark_unhealthy(self, reason):
def rollback(self):
def should_rollback(self):
def get_current_version(self):
def test_successful_deployment():
def test_detect_unhealthy_deployment():
def test_rollback_restores_previous():
def test_cannot_rollback_without_previous():
def test_rollback_clears_failure_flag():
def test_multi_version_rollback_chain():
def test_recovery_after_rollback():
```
### version_pin_verify.py
```python
class VersionPinVerify:
def __init__(self):
def pin_version(self, version, expected_hash):
def compute_hash(self, content):
def verify_deployment(self, version, actual_content):
def test_verify_matching_hash():
def test_reject_mismatched_hash():
def test_reject_unpinned_version():
def test_hash_deterministic():
def test_different_content_different_hash():
def test_single_byte_change_detected():
def test_pin_multiple_versions():
```

## filesystem-integrity
### atomic_snapshot.py
```python
def atomic_snapshot(source_path, snapshot_path):
```
### atomic_write_temp_rename.py
```python
def atomic_write(target_path, content):
def _wait_until(pred, timeout=3.0):
```
### checksum_corruption_detect.py
```python
def compute_checksum(path, algo="sha256"):
def verify_checksum(path, expected_checksum, algo="sha256"):
```
### cow_backup.py
```python
def cow_backup(source_path, backup_path):
```
### dir_tree_diff.py
```python
def tree_checksum_index(root_dir):
def tree_diff(tree1_index, tree2_index):
```
### disk_full_write_guard.py
```python
class QuotaGuard:
def __init__(self, quota_bytes):
def write_file(self, path, content):
def get_used(self):
def remaining(self):
```
### fsync_durability.py
```python
def durable_write(path, data):
def _recording_fsync(fd):
```
### restore_from_backup.py
```python
def create_backup(source_path, backup_path):
def restore_from_backup(backup_path, target_path):
```
### safe_delete_trash.py
```python
def safe_delete_to_trash(file_path, trash_dir):
```
### symlink_escape_guard.py
```python
def safe_symlink(link_path, target_path, root_dir):
```

## log-management
### crash_log_capture.py
```python
def crash_during_write_simulator(log_path, crash_after_n=5):
```
### log_compression.py
```python
def compress_log_file(log_path, compression_level=9):
```
### rate_limited_log.py
```python
def rate_limited_logger(limit_per_sec=100):
def log_entry(text):
```
### retention_prune.py
```python
def prune_by_count(log_dir, keep_count=5):
```
### ring_buffer_log.py
```python
def ring_buffer_log(max_size):
def log_entry(text):
def get_all():
```
### rotate_by_size.py
```python
def rotate_by_size(log_path, size_cap_bytes=1000, keep_rotations=2):
def append_line(text):
```
### rotate_by_time.py
```python
def rotate_by_time(log_path, rotation_interval_sec=5, keep_duration_sec=10):
def append_line(text, now):
```
### secret_redaction.py
```python
def redacting_logger(log_path, redact_patterns=None):
def log_entry(text):
```
### structured_json_log.py
```python
def structured_logger(log_path):
def log_event(event_dict):
def parse_json_log(log_path):
```
### tail_follow.py
```python
class TailFollower:
def __init__(self, log_path):
def read_new_lines(self):
```

## mesh-distributed
### consistent_hashing.py
```python
def stable_hash(s):
class ConsistentHash:
def __init__(self, nodes=None, ring_size=100):
def _build_ring(self):
def get_node(self, key):
def add_node(self, node):
def remove_node(self, node):
def test_consistent_hashing_basic():
def test_consistent_hashing_minimal_remapping():
def test_consistent_hashing_remove_node():
def test_consistent_hashing_stability():
def test_failure_naive_modulo():
def naive_hash(key, num_nodes):
```
### gossip_membership.py
```python
class GossipNode:
def __init__(self, node_id):
def gossip(self, other_node):
def test_gossip_membership_join():
def test_gossip_membership_multi_hop():
def test_gossip_membership_leave():
def test_gossip_membership_version_numbers():
class VersionedGossipNode:
def __init__(self, node_id):
def gossip(self, other):
def leave(self):
def test_failure_no_gossip():
class StaticNode:
def __init__(self, node_id, initial_membership):
```
### heartbeat_lease.py
```python
class HeartbeatLease:
def __init__(self, lease_ttl=10):
def tick(self):
def send_heartbeat(self):
def is_alive(self):
def leader_think_follower_alive(self):
def test_heartbeat_lease_alive():
def test_heartbeat_lease_expiry():
def test_heartbeat_lease_renew():
def test_heartbeat_lease_multi_followers():
def test_failure_no_heartbeat_monitoring():
class BuggyFollower:
def __init__(self):
```
### idempotent_replication.py
```python
class ReplicatedStore:
def __init__(self, replica_id):
def apply_write(self, write_id, key, value):
def get_applied(self):
def test_idempotent_replication():
def test_idempotent_replication_batch():
def test_idempotent_replication_concurrent():
def test_idempotent_replication_ordering():
def test_idempotent_replication_duplicate_write():
def test_failure_no_write_id_tracking():
class BuggyReplica:
def __init__(self):
def apply_write(self, key, value):
```
### lamport_clock.py
```python
class LamportClock:
def increment(self):
def see(self, other_ts):
def read(self):
def test_lamport_clock():
def test_lamport_monotonic():
def test_lamport_causality():
def test_lamport_concurrent_events():
def test_failure_wall_clock():
```
### leader_election_lite.py
```python
class Node:
def __init__(self, node_id, term=0, leader_id=None):
def request_vote(self, candidate_id, candidate_term):
def become_leader(self):
def test_leader_election_lite():
def test_leader_election_node_crash():
def test_leader_election_term_monotonic():
def test_leader_election_split_brain():
def test_failure_no_term_tracking():
class BuggyNode:
def __init__(self, node_id):
def claim_leadership(self):
```
### lease_distributed_lock.py
```python
class Lease:
def __init__(self, holder_id, grant_time, lease_ttl):
def is_expired(self, current_time):
class DistributedLock:
def __init__(self, lease_ttl=10):
def tick(self):
def acquire(self, holder_id):
def renew(self, holder_id):
def holder(self):
def test_lease_acquire():
def test_lease_expiry():
def test_lease_renew():
def test_lease_renew_as_non_holder():
def test_lease_multiple_holders_sequence():
def test_failure_no_lease_expiry():
class BuggyLock:
def __init__(self):
def acquire(self, holder_id):
```
### lww_conflict_resolve.py
```python
class VersionedValue:
def __init__(self, value, timestamp):
def __repr__(self):
class LWWStore:
def __init__(self, node_id):
def tick(self):
def write(self, key, value):
def merge(self, other_store):
def see_write(self, key, value, timestamp):
def test_lww_conflict_resolution():
def test_lww_partition_heal():
def test_lww_causality_preserved():
def test_lww_multiple_keys():
def test_lww_tie_breaking():
def test_failure_no_timestamp_tracking():
class BuggyStore:
def __init__(self):
def write(self, key, value):
def merge(self, other):
```
### partition_tolerance_demo.py
```python
class PartitionTolerantNode:
def __init__(self, node_id, total_nodes):
def can_write(self):
def write(self, key, value):
def partition(self, other_nodes):
def test_partition_tolerance_majority_wins():
def test_partition_tolerance_data_divergence():
def test_partition_tolerance_rejoin():
def test_partition_split_brain_avoidance():
def test_failure_no_quorum_check():
class BuggyNode:
def __init__(self):
def write(self, key, value):
```
### quorum_check.py
```python
def quorum_size(total_nodes):
def can_write(alive_nodes, total_nodes):
def test_quorum_check():
def test_quorum_lost_on_partition():
def test_quorum_check_even_nodes():
def test_quorum_minimal():
def test_quorum_three_nodes():
def test_failure_majority_requirement():
def buggy_can_write(alive_nodes):
```

## monitoring-metrics
### counter_gauge_histogram.py
```python
class Counter:
def __init__(self, name, initial=0):
def increment(self, delta=1):
def get(self):
class Gauge:
def __init__(self, name, initial=0):
def set(self, value):
def increment(self, delta=1):
def decrement(self, delta=1):
def get(self):
class Histogram:
def __init__(self, name, buckets=None):
def observe(self, value):
def get_percentile(self, percentile):
def get_average(self):
def test_counter_gauge_histogram():
```
### heartbeat_miss_alert.py
```python
class HeartbeatMissAlert:
def __init__(self, timeout_seconds=60):
def heartbeat(self, timestamp):
def check(self, current_timestamp):
def is_alerting(self):
def test_heartbeat_miss_alert():
```
### metric_export.py
```python
class MetricRegistry:
def __init__(self):
def register_counter(self, name, value):
def register_gauge(self, name, value):
def register_histogram(self, name, buckets):
def export_json(self):
def export_prometheus_text(self):
def export_csv(self):
def test_metric_export():
```
### p2_percentile.py
```python
class P2Percentile:
def __init__(self, percentile=50):
def observe(self, value):
def _parabolic(self, i, d):
def get_percentile(self):
def brute_force_percentile(data, percentile):
def test_p2_percentile():
def p2_of(data, p):
```
### rate_calc.py
```python
class RateCalculator:
def __init__(self, window_size_seconds=60):
def observe(self, timestamp, counter_value):
def calculate_rate(self, current_timestamp):
def test_rate_calc():
```
### sliding_aggregate.py
```python
class SlidingWindow:
def __init__(self, window_size):
def add(self, value):
def sum(self):
def average(self):
def min(self):
def max(self):
def count(self):
def test_sliding_aggregate():
```
### slo_error_budget.py
```python
class SLOErrorBudget:
def __init__(self, slo_percent=99.9, period_seconds=2592000):
def request_success(self, count=1):
def request_failure(self, count=1):
def success_rate_percent(self):
def error_budget_consumed_percent(self):
def remaining_budget_requests(self):
def over_budget(self):
def test_slo_error_budget():
```
### threshold_alert.py
```python
class ThresholdAlert:
def __init__(self, threshold, comparison="greater_than", hysteresis=0):
def check(self, value):
def is_alerting(self):
def test_threshold_alert():
```
### uptime_calc.py
```python
class UptimeCalculator:
def __init__(self):
def add_event(self, timestamp, state):
def calculate_uptime(self, start_time, end_time):
def test_uptime_calc():
```
### zscore_anomaly.py
```python
class ZScoreAnomaly:
def __init__(self, threshold=3.0, window_size=30):
def add(self, value):
def get_anomalies(self):
def test_zscore_anomaly():
```

## network-health
### dns_resolve_check.py
```python
def dns_resolve_check(hostname, timeout_sec=1.0):
```
### exponential_backoff.py
```python
def exponential_backoff(operation, max_attempts=5, base_delay_ms=10):
def flaky_op():
```
### failover_switch.py
```python
def is_reachable(host, port, timeout_sec=0.3):
class FailoverSwitch:
def __init__(self, primary, secondary):
def check_and_switch(self, timeout_sec=0.3):
def accept_conns(server):
```
### heartbeat_gossip.py
```python
class GossipMember:
def __init__(self, node_id, heartbeat_interval_sec=0.05, failure_threshold=0.2):
def send_heartbeat(self):
def receive_heartbeat(self):
def check_alive(self, current_time=None):
class GossipCluster:
def __init__(self, heartbeat_interval_sec=0.05, failure_threshold=0.2):
def add_member(self, node_id):
def receive_heartbeat(self, node_id):
def detect_failures(self):
def alive_count(self):
```
### http_health_probe.py
```python
class HealthHandler(http.server.BaseHTTPRequestHandler):
def do_GET(self):
def log_message(self, format, *args):
def probe_health(url, timeout_sec=0.5):
```
### latency_measure.py
```python
def latency_measure(host, port, timeout_sec=0.5):
def accept_connections():
```
### reachability_matrix.py
```python
def probe_endpoint(node_id, endpoint_host, endpoint_port, timeout_sec=0.3):
def build_reachability_matrix(nodes, endpoints, timeout_sec=0.3):
def accept_conns(s):
```
### retry_timeout.py
```python
def retry_with_timeout(operation, max_attempts=5, timeout_sec=2.0):
def flaky_op():
def never_succeeds():
```
### split_brain_detect.py
```python
def can_reach(from_node, to_node, node_addresses):
def detect_split_brain(node_id, all_nodes, node_addresses, quorum_size):
def accept_conns(s):
```
### tcp_port_check.py
```python
def tcp_port_check(host, port, timeout_sec=1.0):
```

## packaging-environment
### binary_presence_check.py
```python
def check_binaries_exist(binary_paths):
```
### capability_probe.py
```python
def probe_capabilities(test_dir):
```
### depgraph_resolve.py
```python
def detect_cycle_dfs(graph):
def dfs(node, path):
```
### deps_verify.py
```python
def verify_dependencies(manifest_path, actual_versions):
```
### dryrun_installer.py
```python
def install(install_dir, packages, dry_run=False):
def verify_installation(install_dir, expected_packages):
```
### env_diff.py
```python
def diff_environments(env1, env2):
```
### lockfile_hash_integrity.py
```python
def compute_sha256(data):
def verify_lockfile(lockfile_path, dep_contents):
```
### path_sanity.py
```python
def find_binary(name, path_str):
def verify_binary_locations(path_str, required):
```
### reproducible_build_check.py
```python
def build_artifact(sources):
def build_and_hash(sources):
```
### version_constraint_solve.py
```python
def parse_constraint(constraint_str):
def version_satisfies(version_tuple, constraint):
def resolve_versions(constraints, available_versions):
```

## process-supervision
### crash_loop_detector.py
```python
class CrashLoopDetector:
def __init__(self, restart_threshold=5, window_seconds=60.0):
def record_restart(self):
def should_restart(self):
```
### graceful_shutdown_sigterm.py
```python
def handle_sigterm(signum, frame):
def install_graceful_shutdown_handler(state_file_path: str) -> str:
def spawn_shutdown_child(state_file: str) -> subprocess.Popen:
def send_sigterm_and_wait(child: subprocess.Popen, settle: float = 0.1,
                          timeout: float = 2.0) -> None:
def assert_state_saved(state_file: str, expected_content: str) -> None:
def main() -> None:
```
### heartbeat_liveness.py
```python
def liveness_detector(heartbeat_timeout=0.2):
def heartbeat():
def detector():
```
### keepalive_daemon.py
```python
class KeepAliveDaemon:
def __init__(self, poke_interval=0.05, timeout_threshold=0.3):
def poke(self):
def keepalive_loop(self):
def check_keepalive(self):
def stop(self):
def cleanup(self):
```
### pidfile_singleton.py
```python
def pidfile_lock(pidfile):
```
### readiness_vs_liveness.py
```python
class Instance:
def __init__(self, name):
def check_liveness(self):
def check_readiness(self):
class Router:
def __init__(self, instances):
def dispatch(self, n):
```
### restart_backoff.py
```python
def restart_with_backoff(max_backoff=2.0, backoff_factor=2.0):
```
### supervised_child.py
```python
class Supervisor:
def __init__(self):
def spawn_child(self):
def supervise(self):
def kill_child(self):
def stop_supervise(self):
```
### watchdog_restart.py
```python
class Watchdog:
def __init__(self, cap):
def _spawn(self):
def run(self):
def kill_current(self):
def stop(self):
def _wait_until(pred, timeout=3.0):
```
### zombie_reaper.py
```python
def sigchld_handler(signum, frame):
```

## resource-guards
### backpressure_queue.py
```python
def backpressure_queue(max_size=64, timeout_sec=0.1):
class BackpressureQ:
def __init__(self, size, timeout):
def put_item(self, item):
def get_item(self):
```
### circuit_breaker.py
```python
def circuit_breaker_guard(failure_threshold=10, recovery_timeout=1.0):
class CircuitBreaker:
def __init__(self, threshold, timeout):
def call(self, fn):
def failing_fn():
```
### cpu_throttle.py
```python
def cpu_throttle_guard(max_concurrent=4):
class CpuThrottle:
def __init__(self, max_concurrent):
def spawn_worker(self, work_fn):
def worker_wrapper():
def cpu_work():
```
### disk_space_watchdog.py
```python
def disk_space_watchdog(threshold_mb=100):
class DiskGuard:
def __init__(self, threshold):
def available_space(self):
def can_write(self, size_bytes):
def write_file(self, size_bytes):
def cleanup(self):
```
### fd_leak_detector.py
```python
def fd_leak_detector(soft_cap=64):
class FdCapGuard:
def __init__(self, cap):
def can_open(self):
def opened(self):
def closed(self):
```
### inode_guard.py
```python
def inode_guard(inode_cap=100):
class InodeGuard:
def __init__(self, cap):
def can_create_file(self):
def create_file(self):
def cleanup(self):
```
### load_shedding.py
```python
def load_shedding_guard(capacity=64):
class LoadShedder:
def __init__(self, cap):
def submit_request(self, request_id):
def process_requests(self):
def start_worker(self):
def stop_worker(self):
```
### memory_cap_guard.py
```python
def memory_cap_guard(cap_mb=256):
class MemCapGuard:
def __init__(self, cap):
def can_allocate(self, size_bytes):
def allocate(self, size_bytes):
def free(self, size_bytes):
```
### tmp_cleanup.py
```python
def tmp_cleanup_guard(quota_mb=150, cleanup_target_mb=100):
class TmpCleanup:
def __init__(self, quota, cleanup_target):
def create_file(self, size_bytes):
def cleanup(self):
def cleanup_all(self):
```
### token_bucket_limiter.py
```python
def token_bucket_limiter(tokens_per_sec=10):
class TokenBucket:
def __init__(self, rate):
def allow_op(self):
```

## scheduling-jobs
### cron_expr_next_fire.py
```python
def next_fire(cron_expr, from_time=None):
def parse_field(field_str, min_val, max_val):
def test_cron_next_fire():
```
### dead_letter_queue.py
```python
class DeadLetterQueue:
def __init__(self, max_retries=3):
def execute_with_dlq(self, job_id, callback):
def get_dlq(self):
def get_dlq_count(self):
def get_job_state(self, job_id):
def test_dead_letter_queue():
def failing_job():
def fail_then_succeed():
def always_fail(msg):
def fail_first():
def persistent_failure():
```
### idempotency_key.py
```python
class IdempotencyStore:
def __init__(self):
def execute_idempotent(self, idempotency_key, callback):
def get_log(self):
def get_result(self, key):
def test_idempotency_key():
def increment_callback():
def submit_job(key):
def thread_work(key):
def sync_submit(key):
def failing_callback():
```
### interval_scheduler.py
```python
class IntervalScheduler:
def __init__(self, interval_seconds):
def start(self, callback):
def periodic_loop():
def stop(self):
def get_execution_times(self):
def test_interval_scheduler():
def callback():
```
### jitter_backoff.py
```python
def compute_backoff_with_jitter(attempt, base_delay=0.1, max_jitter_factor=0.5, max_delay=10):
class JitterBackoffRetry:
def __init__(self, seed=None):
def retry_with_jitter(self, callback, max_attempts=3, base_delay=0.05):
def get_retry_times(self):
def test_jitter_backoff():
def failing_callback():
def multi_fail_callback():
def parallel_job(job_id):
def fail_twice():
```
### job_dedup.py
```python
class JobDedup:
def __init__(self):
def run_job(self, job_id, callback, timeout=5):
def get_count(self, job_id):
def test_job_dedup():
def long_running_job():
def launch_job(job_name):
def job_b_work():
def job_c_work():
def run_job_b():
def run_job_c():
def slow_job():
def try_launch():
def simple_callback():
```
### missed_run_catchup.py
```python
class MissedRunCatchup:
def __init__(self, interval=1.0):
def run_with_catchup(self, callback, current_time=None):
def get_log(self):
def reset(self):
def test_missed_run_catchup():
def callback():
```
### oneshot_at_time.py
```python
class OneShotScheduler:
def __init__(self):
def schedule(self, job_key, target_time, callback):
def wait_and_execute():
def wait_all(self, timeout=10):
def get_count(self, job_key):
def test_oneshot_at_time():
def callback():
```
### retry_with_backoff.py
```python
def retry_with_exponential_backoff(callback, max_attempts=3, initial_delay=0.1, max_delay=10):
def test_retry_with_backoff():
def fail_once():
def fail_three_times():
def always_fail():
def fail_immediately():
def succeeds_immediately():
```
### timeout_kill.py
```python
def run_with_timeout(cmd, timeout_seconds, stdin_data=None):
def test_timeout_kill():
```

## secrets-credentials
### enforce_600_perms.py
```python
def enforce_600_perms(filepath):
```
### env_secret_load.py
```python
def env_secret_load(env_key, default=None):
def load_secrets_safe(env_keys, output_file=None):
```
### expiry_check.py
```python
class LogicalClock:
def __init__(self):
def advance(self, delta):
def current(self):
def expiry_check(token, expiry_time, clock):
```
### keyring_store.py
```python
def keyring_store(keyring_path):
class Keyring:
def __init__(self, fpath):
def store_secret(self, key, secret):
def retrieve_secret(self, key):
def verify_protected(self):
```
### leaked_secret_scan.py
```python
def leaked_secret_scan(blob, patterns=None):
def connect_database():
def get_api_client():
def oauth_flow():
```
### least_privilege_check.py
```python
def least_privilege_check(filepath):
def enforce_least_privilege(filepath):
```
### log_redaction.py
```python
def log_redaction(log_path, secrets_to_redact=None):
class RedactingLogger:
def __init__(self, fpath, secrets):
def redact_message(self, message):
def log(self, message):
def read_log(self):
```
### secret_audit_trail.py
```python
class AuditTrail:
def __init__(self, audit_path):
def log_access(self, action, secret_name, user="system"):
def read_trail(self):
def verify_trail(self, expected_count):
```
### token_rotation.py
```python
def token_rotation(token_file, max_tokens=5):
class TokenRing:
def __init__(self, fpath, cap):
def add_token(self, token_id, secret):
def get_tokens(self):
def size(self):
```
### ttl_cache.py
```python
class LogicalClock:
def __init__(self):
def advance(self, delta):
def current(self):
def ttl_cache(ttl_seconds=100, clock=None):
class TTLCache:
def __init__(self, ttl, clk):
def set(self, key, value):
def get(self, key):
def size(self):
```

## state-db-durability
### backup_rotation.py
```python
def p(v): return os.path.join(d, "backup.v%d.txt" % v)
for i in (1, 2, 3):
def surviving_backups(d):
```
### corruption_repair.py
```python
def create_good_database(db_path: str) -> None:
def backup_database(source: str, backup: str) -> None:
def corrupt_by_truncation(db_path: str, factor: float = 0.5) -> None:
def detect_corruption(db_path: str) -> bool:
def attempt_repair(db_path: str) -> bool:
def restore_from_backup(backup: str, target: str) -> bool:
def assert_repair_consistency(db_path: str, expected_rows: int = 3) -> None:
def main() -> None:
```
### crash_consistent_snapshot.py
```python
def atomic_snapshot(db_path, snap_path):
def _valid_db(path):
```
### hot_copy.py
```python
def hot_copy_sqlite(source_path: str, dest_path: str, pages: int = 1, sleep: float = 0.005) -> None:
def seed_database(db_path: str) -> None:
def start_writer(db_path: str) -> subprocess.Popen:
def read_copy_indexes(copy_path: str) -> List[int]:
def count_live_rows(live_path: str) -> int:
def assert_copy_consistency(copy_path: str, live_path: str) -> None:
def main() -> None:
```
### integrity_check.py
```python
def check(path):
```
### journaled_write.py
```python
def recover_from_journal(data_path, journal_path):
```
### migration_with_rollback.py
```python
def create_old_schema(db_path: str) -> None:
def get_schema_version(db_path: str) -> Tuple[str, List[str]]:
def start_migration_child(db_path: str) -> subprocess.Popen:
def kill_child(child: subprocess.Popen, settle: float = 0.2, wait_timeout: float = 1.0) -> None:
def assert_valid_schema_state(version: str, columns: List[str]) -> None:
def assert_data_preserved(db_path: str, expected_rows: int = 2) -> None:
def main() -> None:
```
### point_in_time_restore.py
```python
def restore_to(base_path, log_path, target_ts, db_path):
def vals(db_path):
```
### transaction_rollback.py
```python
def start_transaction_child(db_path: str, marker_file: str) -> subprocess.Popen:
def wait_for_marker(marker_file: str, timeout: float = 2.0) -> None:
def kill_child(child: subprocess.Popen) -> None:
def read_rows(db_path: str) -> List[str]:
def assert_rolled_back(db_path: str, expected_count: int = 1) -> None:
def main() -> None:
```
### wal_checkpoint.py
```python
def verify_wal_recovery(db_path):
```

## system-introspection
### load_avg_read.py
```python
def parse_loadavg(loadavg_text):
def read_loadavg_real():
def main():
```
### memory_pressure.py
```python
def parse_psi_memory(psi_text):
def read_psi_memory():
def main():
```
### mount_disk_usage.py
```python
def parse_df_output(df_text):
def main():
```
### open_fd_count.py
```python
def count_open_fds_from_dir(fd_dir_listing):
def count_open_fds_real(pid):
def main():
```
### orphan_detect.py
```python
def detect_orphans(process_lines):
def main():
def detect_orphans_broken(process_lines):
```
### proc_parse_portable.py
```python
def parse_proc_info(proc_text):
def read_proc_status(pid):
def main():
```
### process_tree.py
```python
def build_process_tree(proc_lines):
def main():
def build_process_tree_broken(proc_lines):
```
### resource_usage.py
```python
def parse_resource_metrics(status_text):
def main():
```
### top_n_by_resource.py
```python
def rank_by_memory(process_lines, n):
def main():
```
### uptime_read.py
```python
def parse_uptime(uptime_text):
def read_uptime_real():
def main():
```

## text-stream-ops
### ansi_strip.py
```python
def strip_ansi(text):
def strip_ansi_from_file(file_path):
def main():
def strip_ansi_broken(text):
```
### dedup_stream.py
```python
def dedup_lines(lines, keep_first=True):
def dedup_from_file(file_path, keep_first=True):
def main():
def dedup_lines_broken(lines):
```
### field_extract.py
```python
def extract_fields(line, field_indices, delimiter=None):
def extract_from_file(file_path, field_indices, delimiter=None):
def main():
```
### logline_parse.py
```python
def parse_syslog_line(line):
def parse_log_file(file_path):
def main():
```
### merge_sorted_streams.py
```python
def merge_sorted_streams(streams, key=None):
def verify_sorted(items, key=None):
def main():
def merge_sorted_streams_broken(streams):
```
### multiline_join.py
```python
def join_multiline_logs(lines, continuation_prefix='    '):
def main():
def join_multiline_logs_broken(lines, continuation_prefix='    '):
```
### robust_csv_parse.py
```python
def parse_csv_line(text, strict=True):
def parse_csv_file(file_path, strict=False):
def main():
```
### structured_diff.py
```python
def diff_lines(before, after):
def diff_structured_output(before_text, after_text, key_field=None):
def main():
def diff_structured_output_broken(before_text, after_text):
```
### tail_follow_stream.py
```python
class TailFollower:
def __init__(self, file_path):
def read_new_lines(self):
def main():
```
### throughput_meter.py
```python
class ThroughputMeter:
def __init__(self, window_size=60):
def record(self, item_count=1, byte_count=0):
def get_throughput(self):
def reset(self):
def main():
```

## time-clock-correctness
### clock_skew_detect.py
```python
class SkewDetector:
def __init__(self):
def sample(self, wall_time):
def get_skew_count(self):
def get_total_skew(self):
def test_detect_backward_jump():
def test_multiple_skews():
def test_no_false_positive():
```
### deadline_ttl.py
```python
class DeadlineChecker:
def __init__(self, clock_fn):
def is_expired(self, deadline_time):
def remaining(self, deadline_time):
def set_deadline(self, ttl_seconds):
def test_not_expired_before_deadline():
def mock_clock():
def test_expired_after_deadline():
def mock_clock():
def test_expired_exactly_at_deadline():
def mock_clock():
def test_multiple_deadlines():
def mock_clock():
```
### drift_compensation.py
```python
class DriftCompensator:
def __init__(self, drift_rate):
def calibrate(self, real_time, clock_time):
def correct(self, clock_time):
def error_at(self, clock_time):
def test_fast_clock_compensation():
def test_slow_clock_compensation():
def test_error_calculation():
def test_simulation_fast_clock_causes_wrong_measure():
```
### leap_safe_interval.py
```python
class LeapSafeInterval:
def __init__(self):
def record_leap_second(self, leap_time):
def interval_between(self, time_a, time_b):
def test_interval_without_leap_second():
def test_interval_with_one_leap_second():
def test_interval_with_multiple_leap_seconds():
def test_leap_second_at_boundary_excluded():
def test_reverse_interval():
def test_simulation_wrong_if_leap_not_excluded():
```
### monotonic_vs_wall.py
```python
class ClockMock:
def __init__(self):
def step_wall_backward(self, amount):
def step_mono(self, amount):
def get_wall(self):
def get_mono(self):
def elapsed_time_safe(clock, start_wall, start_mono):
def test_monotonic_survives_backward_jump():
def test_no_false_positive_on_forward_jump():
```
### ntp_offset_check.py
```python
class NTPValidator:
def __init__(self, max_offset_seconds=1.0):
def validate(self, offset_seconds):
def get_offset(self):
def test_accept_valid_offset():
def test_reject_out_of_bounds():
def test_offset_tracking():
```
### sliding_rate_window.py
```python
class SlidingRateWindow:
def __init__(self, clock_fn, window_seconds, max_events):
def is_allowed(self):
def get_event_count(self):
def test_allow_within_limit():
def mock_clock():
def test_reject_over_limit():
def mock_clock():
def test_sliding_window_expires_old_events():
def mock_clock():
def test_multiple_event_bursts():
def mock_clock():
```
### timeout_budget.py
```python
class TimeoutBudget:
def __init__(self, clock_fn, total_seconds):
def start(self):
def remaining(self):
def consume(self, operation_duration):
def test_operations_within_budget():
def mock_clock():
def test_operation_exceeds_remaining_budget():
def mock_clock():
def test_total_budget_exhausted():
def mock_clock():
def test_not_started_raises():
def mock_clock():
def test_multiple_operations():
def mock_clock():
```
### two_clocks_reconcile.py
```python
class DualClockReconciler:
def __init__(self, max_skew_allowed=1.0):
def reconcile(self, clock1_time, clock2_time):
def test_clocks_agree():
def test_clocks_within_tolerance():
def test_one_clock_jumps_backward():
def test_both_clocks_jump_backward():
def test_large_disagreement_no_history():
```
### tz_safe_timestamp.py
```python
class TZSafeConverter:
def to_utc_seconds(dt):
def from_utc_seconds(epoch_seconds, target_tz=None):
def round_trip(dt, target_tz):
def test_round_trip_preserves_epoch():
def test_reject_naive_datetime():
def test_multiple_tz_conversions():
```

