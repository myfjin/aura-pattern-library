# 6E Additions — Post-Review Findings (2026-07-18)

These are items the MATCHES/ADJACENT-BUT-WRONG/UNCLEAR taxonomy does not capture.
Each is a genuine signal for Illia's manual gate or for a follow-up pass.

## 1. Four oracle-parity cpp files are style outliers

**Files:** `exponential_reliability_mtbf.cpp`, `fft_cooley_tukey.cpp`,
`exponential_histogram_count.cpp`, `feature_hashing_trick.cpp`

**Why:** These four have terse descriptions like "Oracle parity: uses Python-generated
data" instead of the 3-6 line what/when/guarantees format used everywhere else.
They are technically MATCHES (the code does what the description says), but they
do not explain the *pattern* — what it does, when to use it, what disaster it
survives. In Illia's manual gate these will stand out as under-documented.

**Recommendation:** Either expand them to match the full format, or flag them
explicitly for Illia's attention so he knows they're intentionally brief (e.g.
because the pattern is fully described by the name + oracle reference).

## 2. Ten compile-repair cpp files need compilation verification

**Files:** `one_hot_encoding.cpp`, `quantile_mapping_bias_correction.cpp`,
`quantile_binning.cpp`, `three_way_stratified_split.cpp`,
`pairwise_ranking_learn.cpp`, `query_expansion_prf.cpp`,
`pagerank_power_iteration.cpp`, `thompson_sampling_bandit.cpp`,
`stirling_approximation_error.cpp`, `position_bias_click_model.cpp`

**Why:** The fix session added missing `#include` directives to these 10 files
(they did not compile before). A description that says "Guarantee (proven in
main): ..." on a file that does not compile is a docstring-lie regardless of
how accurate the prose is. I reviewed the descriptions as MATCHES against the
code text, but I never compiled them.

**Recommendation:** Run `g++ -std=c++17 <file>` on each before presenting to
Illia. The fix session claimed they all compile now, but verify-don't-believe.

## 3. Determinism fix was never verified

**File:** `python/data-science/rankings_and_information_retrieval/inverted_index_search.py`

**Why:** The fix_request flagged this file as a NOTE (stdout varies across runs
with different PYTHONHASHSEED). The completion report says it was fixed by adding
`sorted()` around three printed sets. I never ran the determinism check to
confirm.

**Recommendation:** Run `python3 ~/ai-lab/tools/determinism_check.py <file>`
and confirm it returns OK before claiming done.

## 4. "Short" category expansions may be padded, not clarified

**Files (representative):** `group_by_aggregate.cpp`, `hash_join_merge.cpp`,
`data_profiling_summary.cpp`, `histogram_builder.cpp`,
`gradient_boosting_stumps.cpp`, `huber_robust_regression.cpp`,
`doubly_robust_aipw.cpp`, `e_value_sensitivity.cpp`,
`stratification_subclassification.cpp`, `gradient_descent_momentum.cpp`,
`hill_climbing_restarts.cpp`, `richardson_extrapolation.cpp`,
`rk4_ode_solver.cpp`, `soundex_phonetic.cpp`,
`stirling_approximation_error.cpp`, `drift_detection_psi.cpp`,
`space_saving_heavy_hitters.cpp`, `spatial_radius_join.cpp`,
`rolling_zscore_anomaly.cpp`

**Why:** These 19 files had title-only descriptions (under 40 chars) that were
expanded to full descriptions. I verified every expansion is factually accurate
against the code. But factual accuracy is not the same as *value* — a description
that says "does X with Y" is accurate but may be mechanically filling space
without adding insight. Illia's gate should spot-check 3-4 of these for prose
quality, not just truth.

**Recommendation:** Spot-check `gradient_descent_momentum.cpp`,
`doubly_robust_aipw.cpp`, `soundex_phonetic.cpp`, and
`space_saving_heavy_hitters.cpp` — these cover the range from simple to complex
patterns and will reveal whether the expansions are genuinely helpful or just
padding.

## 5. No cross-file consistency check was done

**Why:** I treated each file independently. But several patterns share concepts
across files — e.g., `ucb_bandit.cpp` and `epsilon_greedy_bandit.cpp` both
describe multi-armed bandits; `budget_allocator.go` and
`free_list_allocator.go` both describe allocation. If two descriptions use
different terminology for the same concept (e.g., one says "exploration bonus"
and another says "exploration term"), that is not a MATCHES/ADJACENT-BUT-WRONG
issue but it *is* something Illia would notice in a manual pass.

**Recommendation:** Before Illia's gate, do a quick terminology scan across
related files. The bandit files and the allocator files are the highest-signal
pairs.

## 6. Four "already-had-description" files are style outliers

**Files:** Same four as item 1 — `exponential_reliability_mtbf.cpp`,
`fft_cooley_tukey.cpp`, `exponential_histogram_count.cpp`,
`feature_hashing_trick.cpp`

**Why:** The completion report notes these were in the "missing" list but the
old ruler couldn't parse their descriptions (bare `/*` on its own line after
an inlined header). They were left as-is. Their descriptions are notably shorter
than the truly-missing files that got full rewrites. This creates a two-tier
style in the library that Illia may want to normalize.

**Recommendation:** Either rewrite them to match the full format, or explicitly
document them as "legacy descriptions, kept as-is" so Illia knows they're not
an oversight.
