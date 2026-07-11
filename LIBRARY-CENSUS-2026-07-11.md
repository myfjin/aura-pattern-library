# LIBRARY CENSUS & VALIDITY VERDICT — 2026-07-11

Every number below is produced by `tools/census.py` (committed; re-run:
`python3 tools/census.py --jobs 8 --quarantine-out QUARANTINE.jsonl`) or by the
named committed tool. Nothing is cited from memory. VALID = **L1 ∧ L2 ∧ L3**
(runs · real asserts · deterministic), per the settled terms of
`~/ai-lab/WEEK-REQUESTS/REQ-LIBRARY-VALIDITY-CENSUS.md`. On failure: quarantine
ledger + report — **nothing was fixed, moved, or edited toward passing.**

## 0 · Toolchain preconditions (measured via `shutil.which`)

python3 ✓ · g++ ✓ · clang++ ✓ · go ✓ · rustc ✓ · Rscript ✓ — **all present;
no language was skipped.** (`library_verify.py` was additionally patched so a
missing toolchain is now a LOUD per-language skip that turns the run RED —
the old code silently counted an ungated language as passing.)

## 1 · VALIDITY VERDICT

**Fully-valid patterns: 769 / 927.** (A pattern counts only if *every* one of
its language files passes all three layers, including the coupling law.)

| sphere | fully valid | failure cluster |
|---|---|---|
| data-science | **369 / 370** | 1 cpp twin coupling-drift (`peeking_alpha_inflation`) |
| rust-systems | **200 / 200** | — |
| system-administration | **142 / 200** | 58 go twins broken by the watermark stamp |
| r-statistics | **58 / 58** | — (2 further R files are twins inside DS rows, both valid) |
| programming | **0 / 99** | the demo-era public sphere has no self-verification (L2) |

By file: **1201 / 1392 pass L1∧L2∧L3** mechanically; 1200 / 1392 after the
coupling law (the drifted cpp twin runs, but its approval no longer describes
its source). By source file (python+R, the material universities would read
first): **631 / 729 valid** — every DS, sysadmin, R and rust source passes;
all 98 failures are in the programming-99.

**Quarantine ledger: `QUARANTINE.jsonl` (192 entries)**, `{id, sphere, lang,
layer_failed, reason, date}`. No files were moved; the ledger is the exclusion
record (contract A2 semantics), the signed trees are untouched. Breakdown:

- **93 × go — L1 (compile fail), all 93 go files in the library.** Root cause
  proven, not guessed: the master-0 watermark inserts `var _auraMark = …`
  *before* `package main`; Go requires the package clause to be the first
  non-comment token, so **the stamp broke every twin after it was gated**
  (`ingest_go.py` gates at copy time, stamps afterward, never re-gates; the
  pre-stamp twin `~/ai-lab/patterns_go/staging/sysadmin/dedup_stream.go`
  builds and runs exit 0 — the library copy does not compile). MANIFEST's
  `go … gate_ok` records the pre-stamp gate. Python/R/cpp/rust placements are
  legal in their grammars — only Go breaks. 10 of the 93 (twins of the
  demo-era programming files) would *also* fail L2.
- **98 × python (programming sphere) — L2 REJECT (`no-asserts`).** 98 of the
  public 99 contain zero asserts: they are library modules with print-demos
  (`lru_cache.py` prints "should be None (evicted)" and checks nothing;
  the go twin `distributed_lock_manager` prints "Tests passed"
  unconditionally). The 99th, `sat_solver`, is WARN (weak-only). This sphere
  predates the assert-linter regime and does not meet the library's own
  L2 standard. It is the **published free tier** — see finding F1.
- **1 × cpp — COUPLING (B3 source-hash drift).** `peeking_alpha_inflation`:
  the python source was fixed in the 07-11 DS seed-audit *after* the cpp twin
  was approved; per the ingest contract the twin is invalidated until
  re-converted + re-approved.

**Layer results elsewhere: zero failures.** L1: every python (669), R (60),
cpp (370), rust (200) file compiles/runs exit 0 — cpp additionally compiles
clean under **clang++** (portability law: 0 failures). L3: 3 runs per file
(python under PYTHONHASHSEED 0/1/2; compiled binaries re-run) — **0 flaky**;
31 files print non-identical-but-passing stdout (timing/thread-order in the
programming demos; recorded as NOTEs, per `determinism_check.py` semantics).
L2 across the sound spheres: DS 108 PASS / 262 WARN / 0 REJECT — matching the
logic-registry split (108 recovery · 262 weak) exactly; sysadmin 106/94/0;
rust, R, cpp all carry real failure paths (non-python languages get an
idiom-aware failure-path scan — a weaker instrument than the python AST
tiering; the read-pass below covers the semantic gap).

**Semantic read-pass (the check no linter does):** reproducible sample, seed
42, 2 files per sphere (12 files). All 12 pin real truths: manual ANOVA vs
R's `aov()` oracle at 1e-8 · concurrent atomic-max vs LCG-known max under 8
real threads · DBSCAN vs planted 2-cluster geometry · windowed OLS tracking a
planted drift · RBAC forced to attempt the forbidden action · go dedup with
10 hard exit-paths. **No semantic fakes found in the sample** (excepting the
programming sphere, whose gap is systemic and already counted above).

## 2 · INTEGRITY (what the library claims about itself)

- `library_verify.py` (patched, no --gate): **GREEN** — Ed25519 signatures
  authentic + unaltered on all 7 subtrees; watermarks valid on all files;
  catalog↔disk **916 = 916** IDs; no quarantined ID in any shippable tree.
- The twin-integrity check was **vacuous before this session** (it tested
  twin stems against a set that already contained the twins themselves — it
  could never fire). Patched to test against python/R source stems only;
  result after the fix: still green — every cpp/go twin traces to a live source.
- `folder-nature verify --root .`: **GREEN** — 1392/1392 files signed +
  watermark-verified, 7 signed subtrees.
- Twin ledgers (`final_approved.jsonl`): cpp 370 rows = 370 twins, go 93 rows
  = 93 twins, no orphans either direction; source-hash pinning: **1 drift**
  (above), 0 missing sources.

## 3 · CENSUS (disk-counted, index-cross-checked)

**Definitions.** A *pattern* = one CATALOG.md row (id + languages +
category); the same stem in two spheres is two patterns. A *file* = one
source file in a shippable tree. Twins fold into their source sphere.

1. **TOTALS — 927 patterns · 916 unique stems · 1392 files.**
   Catalog rows (927) = disk pattern set (927): **zero orphans, zero ghost
   rows, zero language mismatches, zero duplicate rows.** The 916 unique
   stems < 927 patterns because 10 stems recur across spheres
   (`circuit_breaker` ×3; `bloom_filter`, `consistent_hash_ring`,
   `count_min_sketch`, `dead_letter_queue`, `exponential_backoff`,
   `lru_cache`, `merkle_tree`, `skip_list`, `token_bucket` ×2) — same name,
   different patterns. Any headline quoting "916 verified patterns" is
   conflating stems with patterns; the honest headline number is **927
   patterns, 769 currently fully valid**.

2. **PER LANGUAGE (files / unique ids carrying the language):**
   python **669**/667 · cpp **370**/370 · rust **200**/200 · go **93**/92 ·
   R **60**/60. (python 667 < 669 and go 92 < 93 are the `circuit_breaker` /
   `dead_letter_queue` cross-sphere stem shares, not missing files.)

3. **PER SPHERE / TYPE (patterns · categories):**
   data-science **370** · 37 cats — sysadmin **200** · 20 cats —
   rust-systems **200** · 10 cats — programming **99** · 13 cats —
   r-statistics **58** · 9 cats (+2 R files as twin-languages of DS rows =
   the historical "529 vs 527" delta, now explicit).
   Per-category tables: `tools/census_results.json → census.per_category`.

4. **BASE vs COMPOSED:** base **873** · composed **44** (DS "Composed Tools
   (bridge-born)" 10 + rust "Composed Systems (bridge)" 34) · plus rust
   "Cross-Sphere Twins (bridge)" **10**, listed separately (bridge-born but
   twin-natured — decide their tier explicitly rather than let them drift
   between counts; they are the historical miscount trap).

5. **TIER:** free = the public programming 99 — **verified against the
   published repo**: `github.com/myfjin/awesome-python-patterns` contains
   exactly those 99 stems + `run_gate.py` (a tool, not a pattern). Paid /
   private: the remaining **828** patterns. ⚠ The free tier is the sphere
   that fails L2 (F1).

6. **LANGUAGE-COVERAGE MATRIX (patterns):** python-only **206** ·
   python+cpp **368** · python+go **93** · python+cpp+r **2** · r-only **58**
   · rust-only **200**. That is the real state of twin-conversion on disk:
   DS→cpp complete (370/370 incl. the 2 tri-lingual), go at 93 of the planned
   299, cpp/go conversions of programming-64-python-only and the rest of
   sysadmin not started.

## 4 · INDEX FINDINGS (mismatches reported, not papered over)

- **F1 — the free tier fails the library's own floor.** The public 99 (and
  10 of their go twins) have no self-verification. We must not quote "N
  verified patterns" with these inside N. Proposal: harvest-regime upgrade of
  the 99 (add recovery asserts; ~the wave-rebuild playbook), or re-tier the
  public set until then.
- **F2 — all 93 go twins are stamp-broken** (details above). Proposal: fix
  `folder_nature` watermark placement for `.go` (mark after the package
  clause), re-stamp, re-sign, and add a **post-stamp re-gate** to
  `ingest_go.py` (verify the SYSTEM, not the component — the gate must run on
  what actually ships).
- **F3 — MANIFEST.json is stale/self-contradictory:** `cpp/data-science: 369`
  vs 370 on disk (not regenerated after the 370th ingest); a leftover
  `"cpp": {files: 0, empty-ready}` stanza contradicting the populated tree;
  `total_shippable: 529 / unique_ids: 527` predating sysadmin/rust/cpp/go
  entirely. CATALOG.md's `## Counts` block is the same 529-era snapshot and
  sits mid-file with 400+ rows after it.
- **F4 — the go ingest was never committed:** `go/` (93 files) and
  `ingest_go.py` are untracked; CATALOG.md/MANIFEST.json/library_verify.py
  carry uncommitted modifications from that session. The signed, GREEN state
  on disk is ahead of git history.
- **F5 — `library_verify.py` had two silent-pass defects** (missing-toolchain
  = pass; vacuous twin check), both patched this session; docstring updated.
  rustc/go *were* gated by the code despite the stale docstring — but only
  pre-stamp (F2) — and `.go` gating via the twin loop double-ran; removed.

## 5 · What was NOT done (by design)

No pattern was edited, no file moved, no MANIFEST/CATALOG "corrected", no
re-stamp attempted, nothing published. The census reports; the fixes above
are proposals awaiting Illia's yes. Artifacts of this session: this report ·
`tools/census.py` · `tools/census_results.json` (full per-file evidence) ·
`QUARANTINE.jsonl` (192) · the `library_verify.py` patch.
