# FIX-CHANNEL PROTOCOL — repairing patterns without corrupting the ruler

**Goal (final mission):** fix every defect so the library ships ZERO known-broken patterns —
while the validation tool NEVER loses the ability to detect a defect it once caught.

## The trap
Fixing a frozen-INVALID pattern in the library makes the tool's probe find it *correct* →
its INVALID exam entry would fail → a silent flip of the ruler (the exact 29→28 regression).

## The channel (proven 2026-07-21 on bayes_factor + inverse_transform)
For each defective pattern:
1. **Snapshot** the broken file → `validator/regression_fixtures/<name>.BROKEN.py`
   (lives OUTSIDE the signed library, so library stays all-correct + library_verify GREEN).
2. **Fix** the live library file (real repair, not just a guard where the defect is logic/math).
3. **Two probes:**
   - `probe_<name>_BROKEN()` loads the FIXTURE via `_load_fixture()` → reproduces the defect →
     INVALID. This is the permanent kill-test.
   - `probe_<name>()` loads the LIVE file → must now carry a POSITIVE oracle proving the repair
     (numeric ground-truth / round-trip identity / invariant-holds) → PASS. A guard alone gives
     FLAG, not PASS — the fix must be *provably correct*, not merely *not-crashing*.
4. **Exam:** the old INVALID entry's `file` → `FIXTURE:<name>.BROKEN.py` (keeps INVALID);
   ADD a new entry for the live file → PASS. (`FIXTURE:` keys are dispatched by probes.PROBES;
   they end in .py so exam_files() includes them.)
5. **Re-sign** `python/data-science` (or the touched subtree) → `library_verify` GREEN →
   `sweep.py --exam` must hold + be deterministic.

## Positive-oracle recipe by kill-type
- **wrong-math** (bayes_factor): brute-force / closed-form truth; live output must match.
- **missing-guard on a math fn** (inverse_transform): guard + a round-trip/invariant that only
  holds when the math is right (e.g. F(F⁻¹(u))==u).
- **stateful defect** (token_bucket cap, ttl_cache purge): fix the state logic; positive oracle =
  the invariant that was violated now HOLDS across the attack sequence.
- **twin** (bayes_factor.cpp): apply the same formula fix in the twin language; its own probe
  already carries the oracle.

## Status (2026-07-21)
FIXED via channel: bayes_factor_normal_means.py · inverse_transform_sampling.py.
QUEUE (see audit_fix_queue_2026-07-19.md + exam INVALID/FLAG entries):
  stacking_ensemble (NaN-silent), bayesian_ab_beta (impossible-data), token_bucket (cap),
  ttl_cache (purge/leak), log_rank (contract+coverage), the 4 cpp twins, calibration_curve.cpp,
  compressed_block_store.rs (RLE empty-panic), + the go INVALIDs (backoff/csv/breaker).
Each is mechanical repetition of the channel above — batchable across sessions.
