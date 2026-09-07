# T1 auto-detection v2 — AURA Pattern Library at /Users/s_dio/aura-pattern-library

## Enumerated: 1074 unique pattern IDs across 1550 files.
  cpp           420 files
  go            103 files
  javascript     91 files
  python        676 files
  r              60 files
  rust          200 files

## H1 (named by probes.py, word-boundary): 28 patterns — scanned /Users/s_dio/ai-lab/pattern-scoring/validator/probes.py (68665 bytes) [word-boundary]
  atomic_spinlock
  bayes_factor_normal_means
  bayesian_ab_beta
  bloom_filter
  calibration_curve
  checkpoint_resume_crc
  circuit_breaker
  compressed_block_store
  csv_validator
  deadline_ttl
  dedup_pipeline
  dirichlet_stick_breaking
  edit_distance
  exponential_backoff
  gradient_boosting_stumps
  ... and 13 more

## H2 (per-pattern mentions ≥2): 11 patterns
## H2 (per-pattern mentions ≥3): 4 patterns [strict]
  sha256                                             mentioned by  31 distinct patterns ← T1@2 ← T1@3
  hmac_sha256                                        mentioned by   6 distinct patterns ← T1@2 ← T1@3
  integrity_check                                    mentioned by   3 distinct patterns ← T1@2 ← T1@3
  crc32                                              mentioned by   3 distinct patterns ← T1@2 ← T1@3
  label_propagation_communities                      mentioned by   2 distinct patterns ← T1@2
  query_expansion_prf                                mentioned by   2 distinct patterns ← T1@2
  broker_term_extraction                             mentioned by   2 distinct patterns ← T1@2
  edit_distance                                      mentioned by   2 distinct patterns ← T1@2
  pagerank_power_iteration                           mentioned by   2 distinct patterns ← T1@2
  restore_from_backup                                mentioned by   2 distinct patterns ← T1@2
  box_muller                                         mentioned by   2 distinct patterns ← T1@2
  betweenness_centrality                             mentioned by   1 distinct patterns
  pivot_table                                        mentioned by   1 distinct patterns
  bm25_ranking                                       mentioned by   1 distinct patterns
  ab_interleaving                                    mentioned by   1 distinct patterns
  bootstrap_model_comparison                         mentioned by   1 distinct patterns
  bias_variance_decomposition                        mentioned by   1 distinct patterns
  rank_correlation                                   mentioned by   1 distinct patterns
  pearson_correlation_matrix                         mentioned by   1 distinct patterns
  covariance_matrix                                  mentioned by   1 distinct patterns

## H3 (frontmatter self-declaration): 0 patterns

## H4b (twin-with-declared-oracle, widened): 14 patterns
  ab_test_srm_check  ← marker3: 'matches Python'
  apriori_frequent_itemsets  ← marker0: 'per Python oracle'
  atomic_snapshot  ← marker3: 'matches the original'
  authenticated_message_channel  ← marker3: 'matches original'
  circuit_breaker  ← marker8: 'mirrors the Python'
  content_addressed_blob_store  ← marker3: 'matches original'
  keyring_store  ← marker3: 'matches original'
  lru_cache  ← marker2: 'reference implementation'
  melt_unpivot  ← marker3: 'matches original'
  quantile_mapping_bias_correction  ← marker3: 'matches the reference'
  queue_capacity_planner  ← marker3: 'Matches the Python'
  restore_from_backup  ← marker3: 'matches original'
  singleflight_dedup  ← marker3: 'matches the original'
  spectral_clustering_lite  ← marker8: 'Mirrors the Python'
  apriori_frequent_itemsets in H4b: True

## H4 (L4 is_axiom + tier=hard): 97 patterns — read /Users/s_dio/lab-from-future/logic_registry.jsonl
## H4-informational (tier=consensus): 462 patterns

## T1 total (H2 threshold=2): 122 of 1074 (11.4%)
## T1 total (H2 threshold=3): 117 of 1074 (10.9%)

## 6E-G4 preview (NOT auto-promoted yet — Illia decision):
  consensus ∩ (H1 ∪ H2@2): 6 patterns
  consensus ∩ (H1 ∪ H2@3): 2 patterns
  consensus alone (would add if fully promoted): 448 new

## Heuristic overlap (v2 — subtracts h4_hard):
  only H1:  2
  only H2@2:9
  only H3:  0
  only H4b: 12
  only H4:  72
  H1 ∩ H4:  25
  H4b ∩ H4: 1

## T1 by language (H2@2, files not unique IDs):
  cpp            36
  go             10
  python         62
  r              27
  rust           39

## Cross-language twin population (informational):
  IDs in ≥2 files: 466
  IDs in ≥3 files: 8
  IDs in ≥4 files: 1
