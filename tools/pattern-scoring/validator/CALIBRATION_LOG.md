# CALIBRATION LOG — tool verdict vs Illia's ruling (disagreement protocol)
Format: date | pattern | tool verdict + mechanism | Illia verdict + reason | category | who moved | rule changed?

---

## TICKET 001 — power_analysis: mechanical-coverage false-PASS (4Q, 2026-07-20) — TOOL-TAUGHT
- **Pattern:** python/data-science/statistical_modeling/power_analysis_sample_size.py
- **4Q's mechanism (reproducible):** `sample_size_two_proportion(1.5, 0.5, 0.05, 0.80)` returns
  `1` silently — no raise. p1=1.5 is outside [0,1] (E003 domain). A confident number from an
  impossible input = silent domain acceptance.
- **Tool's current behavior:** PASS — because the probe declares `oracle_coverage={"mechanical":True}`
  and no KILL signal fired. This MATCHES Illia's frozen exam verdict (PASS) — but for a fragile reason.
- **Illia's original verdict:** PASS-WITH-FLAG. Basis: the DEMO (`__main__`) raises downstream on
  p1=1.5 (in `two_proportion_power`). Illia tested via the demo; the demo does raise.
- **The disagreement:** Illia ruled on the DEMO's behavior (raises → caught). 4Q tested the ENTRY
  FUNCTION directly (`sample_size_two_proportion` returns silent 1). Both true; different surfaces.
- **Root design flaw (4Q, correct):** `oracle_coverage:{mechanical:True}` should NOT satisfy the
  PASS requirement. "mechanical" = recipes ran ≠ correctness verified. This is 5S's own principle,
  mis-implemented by Fable. Fix: PASS requires numeric/semantic/invariant coverage; add a
  `silent_domain_acceptance` KILL signal (domain recipe fires + finite output + no raise).
- **STATUS: AWAITING ILLIA'S RULING (TOOL-TAUGHT channel).** If Illia accepts 4Q's mechanism:
  power_analysis moves PASS → FLAG (function-level silent hole), the oracle fix applies, and the
  frozen exam verdict updates via the TOOL-TAUGHT channel (logged, not silent). If Illia holds PASS
  (the demo-level verdict stands), the oracle still gets the mechanical-demotion fix but
  power_analysis's probe must gain a positive oracle to legitimately PASS.
- **Category:** false-PASS / oracle-coverage floor. **Who moved:** pending. **Rule changed:** pending.

## v1.5 improvements from 4Q's test (not disagreements — extensions)
- F2: probe-honesty gate (5S harness-gate applied to the tool's OWN probes) — verify `reached`,
  `clean_output`, `invariant_broken` are justified, not just probe-asserted.
- F4: wire a real concurrency probe (atomic_spinlock.rs) so the third-boundary cap is exercised.
- F5: twin-divergence module (structural + behavioral diff) before any inherited verdict.
- F6: separate probe (raw data collection) from oracle (judgment) — probes report outputs, a
  generic oracle decides noise-identity. Removes probe-author-as-judge risk.

---
## TICKET 001 — RESOLVED 2026-07-20 (Illia ruled: 4Q right)
- **Ruling:** 4Q's mechanism accepted. power_analysis PASS → FLAG (function-level silent domain
  acceptance of p1=1.5). **Who moved:** Illia's verdict (TOOL-TAUGHT event).
- **Rule changed:** YES. oracle.py — 'mechanical' coverage REMOVED from positive-oracle set;
  coverage now DERIVED from actual signals (derive_coverage), not trusted from probe (5S #1).
  validate.py — harness_ok/concurrency_ordering wired from detection, not hardcoded (5S #3).
- **Verified:** 5S's executable phony-pattern (const 42.0 + fake mechanical) now → FLAG. 4/4 exam holds.
- **Convergence:** 4Q #1 and 5S #1/#6 were the SAME root (coverage trusted not derived). Both credited.

## 5S findings → status
- F1 (probe spoofs coverage): FIXED (derive_coverage).
- F6 (executable false-PASS): FIXED (verified above).
- F2 (invariant_broken severity split E004-INVALID vs E011-FLAG): v1.5 queued.
- F3 (guardrails dead in runner): FIXED (wired concurrency + harness).
- F4 (recipes.py unused — hand-tuned probes): HONEST v1.5 gap — wire recipes.fire_all into a real probe.
- F5 (reachability unvalidated by real probe): v1.5 — add no-op regression case to exam.

---
## ROUND-2 HARDENING APPLIED 2026-07-20 (Illia: apply now)
- 4Q+5S convergent: coverage derived from field PRESENCE, not verifiable ACTION. Two spoofs left.
- FIX: numeric coverage now requires `oracle_run:True` + `oracle_truth` (not bare `oracle_match`);
  invariant coverage requires a REAL `invariant_broken` signal or structured `invariant_checks`
  (not the `invariant_checked` boolean); noise-identity guarded against vacuous equality.
- VERIFIED: A1 spoof → FLAG, A4 spoof → FLAG, legit numeric → PASS, 4/4 exam holds.
- HONEST LIMIT (both agents): while probes are HAND-WRITTEN, spoofing is mitigated not eliminated —
  the structural fix is v1.5 recipe-wiring (coverage from real recipe execution, no human flags).

---
## SESSION 2026-07-21 — THE BLESSING HALF: exam 5/13 → 13/13 (100%), deterministic ×3
The gap was structural: the tool reproduced all 3 kills but 0 of the PASSes — it could KILL
but not BLESS, because a PASS needs a positive oracle and only ~4 probes existed. This session
poured the missing judgment in as oracles:

**6 positive oracles** (known-GOOD patterns now PASS on evidence, not default):
- robust_csv_parse — 9-case hand-fixed contract battery; E006 None-coercion recorded as disclosed flag
- dedup_pipeline — textbook edit-distance truths + planted near-dup pair + exact diff (-jumps/+leaps)
- dirichlet_stick_breaking — closed-form E[w1]=1/(1+α) Monte-Carlo (seeded) + unit/sum invariants
- gradient_boosting_stumps — exact split recovery on noiseless separable data; boosted MSE→6e-19
- walk_forward_early_stopping — exact helper truths + U-curve demonstration live in subprocess
- log_rank_test — hand-computed z=0.5/√(7/12) + null-identity (0,1) + group-swap antisymmetry

**3 flaw-oracles** (Illia rulings encoded; all moved expansion→frozen):
- token_bucket_limiter → INVALID (ruled 07-20): R13 idle→burst; 100s idle @ rate 10 grants 500/500
- inverse_transform_sampling → INVALID (ruled 07-21): rate unguarded; u=0.5,rate=-2 → silent -0.347
- ttl_cache → FLAG-for-the-real-reason (ruled 07-21 STRONG-FLAG): size() claims 3 live, truth 0;
  3 expired entries resident (lazy-expiry leak). invariant_broken WITHOUT conclusive_kill.

**Rule changed:** sweep.judge gained a generic `conclusive_kill`/`kill_reason` seam — a hand-probe
that PROVED its defect (ruling-backed) escalates to KILL on its own authority. Only probes can set
it; the generic path never can. Additive; prior probes untouched.

**Honest boundaries (unchanged):** exam grades python only — the 2 rust + 2 R frozen PASSes sit
OUTSIDE the exam loop (breadth work D). The tool remains a REGRESSION SUITE of encoded judgments
+ health-check; discovery is bounded by oracle coverage. 13/13 = "carries Illia's audited judgment",
not "auto-discovers bugs".

## SESSION 2026-07-21 (later) — EXAM EXTENDED TO RUST + R: 19/19 (100%), deterministic ×3
The graded set was python-only (13); the 2 rust + 2 R frozen PASSes + 2 rust expansion entries
sat outside the loop. Extended exam filter to .py/.rs/.R (cpp stays out until the twin lane, work E).
Now graded: 19 = 12 frozen py + 2 frozen rs + 2 frozen R + 3 expansion (py power_analysis,
rs http_parser, rs atomic_spinlock). **All 19 reproduce.**

**6 new subprocess probes** (compile/run with probe-owned harness; pattern main renamed,
oracle main appended):
- rendezvous_hash_hrw.rs PASS — HRW law's STRONG half (the self-test never checked it): over
  1000 keys, remove moves ONLY removed-node keys (0 illegal), add pulls ONLY to the new node.
  to_new=500/1000 = the disclosed demo-LCG skew, consistent with the audit flag.
- checkpoint_resume_crc.rs PASS — independent layout arithmetic (12 recs, ckpt-4, torn r09 →
  exactly r00..r08 once; CRC flip at r02 halts at 2; empty→0). Not an echo of the demo.
- http_request_line_parser.rs INVALID — E012 encoded: "strict shape validation" ACCEPTS
  'HTTP/' empty version + 'HTTP/one.two' non-numeric (+ empty header name check).
  conclusive_kill = validation_theater_malformed_accepted.
- atomic_spinlock.rs FLAG — real 8×1000 contention run exact (lost updates would KILL), but
  concurrency_ordering=True caps at FLAG: ordering is un-runnable, third boundary honored.
  Rule changed: sweep.judge now passes probe's concurrency_ordering through (was hardcoded False).
- linear_regression_normal_eq.R / welch_t_test.R PASS — self-oracle scripts run LIVE vs
  lm()/t.test() references; deterministic double-run; live-stopifnot guard against the
  R-wave-3 comment-out-the-assert evasion (incident #13).

**full_sweep.py extended:** probe-backed patterns of ANY language now get their definitive
verdict in the whole-library run (was python-DS only).

## SESSION 2026-07-21 (later still) — CPP TWIN LANE OPEN: exam 24/24 (100%), deterministic ×3
Full-library run first (554s): 1399/1399 BASELINE-OK; 19 probe-backed definitive verdicts
surfaced in-sweep (was ~4); python-DS triage FLAG 328 / SKIP 42. The signed library ships
6 known-INVALID patterns — the sweep now says so on every run.

**GO FINDING (honest boundary):** zero go twins of the 13 audited patterns exist — the go 93
are a different population (sysadmin/programming natives; deadline_ttl.go & dns_cache.go are
kin, not twins). Twin-verification needs a parent with a known verdict; go has none. Go stays
health-only until 4Q converts audited patterns or Illia hand-audits go natives. NOT papered over.

**CPP TWIN LANE (5 probes, harness = rename main -> pattern_main + probe main, g++ -O2):**
Every one of the five prints its own self-test "PASS" immediately before the probe exposes it —
compiles≠correct and self-report≠verdict, demonstrated in one screen:
- bayes_factor.cpp INVALID — in-harness brute-force integration: code BF=1.24, truth logBF=56.3,
  off by 10^24 (uses y_mean^2*n/denom, needs (sum y)^2*tau2/denom). Wrong-math inherited.
- stacking_ensemble.cpp INVALID — NaN into std::sort (UB), threshold=nan, predictions finite,
  no throw. NaN-silent inherited.
- log_rank_test.cpp FLAG — math half VERIFIED (hand z=0.6547 exact, same truth as python probe);
  mismatch half = OOB read, z=-1.06 garbage accepted with NO defined error (python threw
  IndexError). The hole is the UB itself, not its runtime costume.
- gradient_boosting_stumps.cpp FLAG — exact-split evidence GREEN (mse 6e-19) but verdict HELD
  at FLAG: DIVERGED twin (has guards python lacked), PASS gated on Illia's independent cpp audit.
  Deliberately returns no positive-oracle keys.
- calibration_curve.cpp INVALID (⚠ Illia lean encoded; ruling PENDING — stays in expansion,
  frozen-move awaits his word): labels {7,-3} accepted -> "observed frequency" 7, brier 31.4;
  mismatched lengths -> OOB UB, no defined error.

Exam filter now .py/.rs/.R/.cpp -> 24 graded, 24/24, zero regressions, 8.1s.
Probe census: 24 total (13 py + 4 rs + 2 R + 5 cpp). full_sweep surfaces all of them.

---
## CALIBRATION SESSION 2026-07-21 — four Illia rulings + GO batch 1 prepared
**Rulings (all encoded, exam 24/24 HOLDS after freeze):**
1. calibration_curve.cpp — ❌ INVALID CONFIRMED → expansion→frozen. Probe evidence decisive.
2. gradient_boosting_stumps.cpp — evidence=audit → FLAG→**PASS** (logged verdict change; probe
   gained positive-oracle keys: exact-split truth + mse->0). expansion→frozen.
3. bayes_factor.cpp + stacking.cpp + log_rank.cpp — all three confirmed twins → frozen.
   FROZEN now 21 · expansion 3 (power_analysis, http_parser.rs, atomic_spinlock.rs).
4. GO lane — Illia audits go NATIVES himself (rejected auto-conversion path for now).

**GO batch 1 — 5 cards written to playground/cards/*_go.card.md** (deadline_ttl,
exponential_backoff, csv_validator, circuit_breaker, bloom_filter — 5 distinct failure
dimensions: float-poison, int-overflow, contract-theater, state-sequence, state-accounting).
All baselines verified green; ALL 12 paste-attacks compile-verified in scratch and land:
- deadline_ttl: NaN TTL = IMMORTAL LEASE (IsExpired always false); neg TTL born-expired silent.
- backoff: 1<<62 base → Duration math wraps to EXACTLY 0 → backoff vanishes, instant [0 0];
  negative base same; maxAttempts=0 → (false,[],0).
- csv_validator: "NaN" passes float validation (ParseFloat accepts) → NaN salary, 0 errors;
  failed optional coercion keeps row with RAW STRING in integer column; literal "<nil>"
  string = magic missing-sentinel → row silently excluded (data loss).
- circuit_breaker: failureCount NEVER resets on success in CLOSED → OPEN on 3 non-consecutive
  fails (consecutive-vs-cumulative = Illia's ruling); recoveryTimeout<0 → "OPEN" invokes the
  dead service 5/5 (fail-fast theater); unexpected-err in HALF_OPEN parks there forever.
- bloom_filter: Resize never resets itemCount → analytic FPR lies about an EMPTY filter
  (ttl_cache size()-lie kin); dup Adds inflate n; cap=1/rate=0.99 accepted → contains(everything).
Verdicts are ILLIA'S to rule in the card session — cards carry predictions + evidence, not verdicts.

---
## GO BATCH 1 CARD SESSION 2026-07-21 (live, in-chat) — exam 29/29 (100%), ALL 5 LANGUAGES
Format evolution that WORKED: cards played in dialogue — Fable pre-verified each combined
paste-block in scratch, Illia pasted into playground, ran, output ruled line-by-line together.
Improv attacks in Illia's style landed the deepest finds. Illia caught the os.Exit(0)
paste-trap in backoff himself (block must sit ABOVE the final print).

**Illia's five rulings (all encoded as probes + frozen exam entries):**
- deadline_ttl.go → STRONG-FLAG. NaN TTL = immortal lease (IsExpired always false);
  IMPROV G1: clock rewind RESURRECTS an expired lease (remaining:20 after death).
  Core arithmetic exact on sane inputs.
- exponential_backoff.go → ❌ INVALID. 1<<62 base wraps Duration math to EXACTLY 0 →
  backoff vanishes (probe measures 37µs where contract implies centuries); dead op
  hammered 5/5; neg base same; maxAttempts=0 → failure-in-0-attempts.
- csv_validator.go → ❌ INVALID. NaN/+Inf/−Inf pass float validation with ZERO errors;
  failed optional coercion keeps row with raw STRING in integer column ("coercions are
  exact" falsified); literal "<nil>" = magic missing-sentinel drops rows. STRENGTH on
  record: 20-digit int caught cleanly by strconv.
- circuit_breaker.go → ❌ INVALID. failureCount never resets on success in CLOSED →
  cumulative-forever threshold; IMPROV G1: 50%-healthy alternating service trips
  PERMANENTLY OPEN — the breaker manufactures the outage it exists to prevent.
  Neg recoveryTimeout → "OPEN" invokes dead service 5/5 (fail-fast theater);
  unexpected err type parks HALF_OPEN forever.
- bloom_filter.go → STRONG-FLAG. Resize clears bits, keeps itemCount=1000 → analytic
  FPR describes a nonexistent filter (ttl_cache size()-lie kin). STRENGTHS on record:
  FPR formula HONEST at 100k/cap-10 saturation (claims 1.0, truth 1.0); no false
  negatives anywhere; real guards on shrink + invalid construction.

**GO-NATIVE ERROR CLASSES observed:** Duration/int overflow-to-zero (silent wraparound),
ParseFloat accepting NaN/Inf as valid, magic string sentinels ("<nil>"), non-monotonic
clock trust. THE PATTERN ACROSS LANGUAGES holds: sysadmin/resilience patterns hide
state-lies-over-time; every kill invisible to compile+run health checks.

Exam: 29 graded across .py/.rs/.R/.cpp/.go → 29/29, deterministic ×3, 12.3s.
Probe census: 29 (13 py + 4 rs + 2 R + 5 cpp + 5 go). FROZEN 21 · expansion 8 (5 go
entries land in expansion→frozen candidates after regression-observation window — or
freeze immediately at Illia's word).

---
## REBUILD 2026-07-21 (post-go-batch) — rules harvest poured into the GENERIC layer
GO entries FROZEN at Illia's word → frozen 26 · expansion 3 · exam 29/29 HOLDS ×2 with
all changes live. (Ops note: the freeze edit briefly created a DUPLICATE "expansion" key
in exam.json — JSON silently keeps the last, go entries would have vanished from grading;
caught by structure-assert before running. exam.json edits now verified with key-count
+ dup-entry asserts.)

**What the rebuild added (today's finds → tomorrow's generic detection):**
- recipes.py R14_int_overflow (E013): 1<<62 into numerics — typed langs wrap silently;
  python/R immune (arbitrary precision) → LANG_PRIORS "overflow" weight 0 py/R, 1.3 cpp/go,
  1.0 rust. NOT fired in the python in-process executor (hang-safe by design).
- recipes.py R15_scalar_nan_inf (E008-scalar): NaN/Inf into scalar floats — LIVE in the
  generic executor; finite-output-from-NaN-input counts as silent acceptance.
- R13 state-sequence catalog now encodes all five observed kill sequences: idle_then_burst,
  expire_without_touch, clock_rewind, alternating_fail_ok, clear_then_report.
- LANG_PRIORS go "nan" 0.5 → 1.0 (ParseFloat accepts NaN — proven kill) + "stateful" 1.3.
- POSITIVE_STEMS += recovery/delay/backoff/interval/attempts/retries (config-poison params).
- ERROR_CATALOG.md += AURA-E013..E017 (silent-overflow-wrap · magic-sentinel-collision ·
  non-monotonic-clock-trust · cumulative-state-counting · stdlib-parser-accepts-poison)
  + strengths on the record + third-sphere confirmation of the state-lies-over-time law.

Sample-60 under new rules: FLAG 35 · INVALID 1 (bayes_factor via hand-probe — correct) ·
SKIP 24 · zero generic false-kills. Full-library sweep running as final validation.

---
## FULL-LIBRARY RUN UNDER THE REBUILT TOOL 2026-07-21 (final validation) + reporting fix
Sweep: 1399/1399 BASELINE-OK in 569s · 29 probe-backed definitive verdicts surface in-sweep
(12 INVALID · 11 PASS · 6 FLAG across all 5 languages).

**Reporting defect found & fixed during analysis:** verdict_from_signals checked `unproven`
BEFORE `flags`, so "confident_output_no_oracle" SHADOWED "silent_domain_acceptance" in every
generic reason string — the most actionable triage signal was invisible in reports. Fix:
flags branch now names itself first (verdict unchanged — FLAG either way). Exam 29/29 ×2 after.

**True triage visibility (DS python 377, first honest measurement):**
- **105 patterns SILENTLY ACCEPT ≥1 domain/poison attack** (incl. new R15 scalar NaN/Inf)
- **133 emit NaN** on poisoned input (visible, not silent)
- 4 INVALID + 5 PASS (probe-backed) · 42 SKIP
The 105 = the semantic-abuse gate queue (Illia's scale plan: sample-measured rate → class-level
retrofit, not 676 by hand). Ops note: bare `sweep.py` (no filter) triages sysadmin python
in-process = the known hang lane full_sweep excludes — a chained verification run wedged there
and was killed; measurement redone DS-only. TODO: sweep.py should refuse or subprocess-guard
non-DS python by default.

---
## RETROFIT GENERATOR BUILT + AUTO-LANE CLOSED IN SANDBOX 2026-07-21
The 105/152 silent-acceptance queue does NOT need 152 hand-fixes — it clusters into 4 recipe
classes, 3 of them mechanically closable. Built `retrofit_gen.py`: derives guards ONLY where
the tool's own attacks proved one missing, emits Illia's accumulate-then-raise contract
(AuraInputError + _aura_validate_<fn>), writes to sandbox `retrofit_gen_out/` (LIBRARY NEVER
TOUCHED), then the validator VERIFIES ITS OWN FIX via triple gate:
  (1) every accepted attack must now RAISE AuraInputError
  (2) the pattern's __main__ self-test must stay GREEN
  (3) output deterministic across two runs.

**AUTO lane = 127 patterns, 283 guards.** Classes emitted: R15 finite (E008), R9 positive-count
(E009), R2 domain (E001/E003 — prob/significance/rate/u/var families). R1 blunt-underflow
DELIBERATELY excluded (a -1e9 shift can be legitimate) -> model-assisted docstring lane.

**The gate caught real generator bugs — proof the self-verify is not theater:**
- alpha/beta name-collision: `alpha`=smoothing strength (target_encoding, 0 legit) and Beta
  shape (beta_binomial, 1.73 legit) tripped the patterns' OWN demos. Auto now EXCLUDES bare
  alpha/beta + a general demo-disproof retry (drop guards the demo disproves, regenerate).
- function-local `import math`: has_math check saw a nested import, skipped the module-level
  one -> validator NameError (stratification). Fixed: module-level detection only.
- callable params (`f` = integrand in richardson): finite-guard on a callable never fires ->
  correctly routed to JUDGE, not shipped.

Final: 122/127 CLEAN CLOSURE (attacks raise · self-test green · deterministic). 5 quarantined
to JUDGE (all demo-disproved domains: caliper_matching, dtw_shape_drift, sharpe_sortino,
novelty_effect_decay, distance_metrics_toolkit). APPLY-LIST = the 122 OK rows in
retrofit_batch_full.log, NOT ls of the sandbox (JUDGE files also leave partial writes) — need docstring judgment,
never auto-guessed. **All in SANDBOX. Application to library is Illia's gate:** apply OK files
-> folder_nature re-sign -> library_verify GREEN -> exam 29/29 must hold -> fresh sweep for the
silent-acceptance BURN-DOWN (queue 152 -> ~30, the residue being the judgment lane by design).

---
## RETROFIT APPLIED TO LIBRARY 2026-07-21 (Illia's gate: apply · re-sign · verify · burn-down)
**116 retrofits LIVE in the library** (data-science subtree re-signed, library_verify GREEN,
exam 29/29 HELD). Every applied file carries AuraInputError; folder_nature Ed25519 re-signed.

**⚠ REGRESSION CAUGHT & CONTAINED (the law worked):** first apply of all 122 flipped exam
29→28 — `inverse_transform_sampling.py` (FROZEN INVALID) went PASS. Root cause: the auto-lane
retrofitted a GRADED pattern, and its rate>0 guard FIXED the exact rate<0 defect its probe
kills for → verdict flipped. The ruler must never be silently changed. Diagnosis + fix:
  1. Found all 6 exam patterns caught by the auto-lane (dirichlet, dedup, gradient_boosting,
     inverse_transform, bayesian_ab, power_analysis).
  2. Reverted all 6 to pristine (git checkout HEAD) — only inverse_transform had flipped, but
     ALL graded patterns are the measurement instrument and must stay untouched.
  3. Re-signed, exam RESTORED to 29/29, library GREEN.
  4. GENERATOR HARDENED: retrofit_gen.queue_files() now excludes exam.json files by design
     (_exam_files()). The ruler is off-limits to the auto lane, permanently.

**BURN-DOWN (honest, by the frozen ruler):** auto-lane residual 127 patterns/283 guards →
18 patterns/30 guards. ~109 patterns fully hardened, ~253 guards poured & proven. Second pass
on the 18 = 0 clean closures: all are JUDGE (demo-disproved domains) or REVIEW (guard trips
own demo, e.g. gaussian_mixture_em X[12]/X[39]) — the honest auto-lane floor.

**Remaining (judgment lane, by design, NOT auto-fixable):** ~77 R1-blunt-only patterns
(unbounded-by-design candidates) + 18 second-order/demo-disproved + bare alpha/beta domains.
These need docstring judgment (model-assisted or Illia's card session), never templates.

Note: 5 other DS py files show git-modified without AuraInputError — PRE-EXISTING prior-session
work (count_min_sketch keyless-API fix, inverted_index determinism, 3 recommenders), part of
the GREEN baseline before this apply, NOT from the retrofit. Verified absent from apply manifest.

NOT COMMITTED — working tree changes staged for Illia's review/commit at his chosen time.

---
## POSITIVE-ORACLE GAP SIZED + ROUND-TRIP LANE TESTED 2026-07-21
Illia pushed back on "green" — correctly. Green = compiles + self-test passes = SHALLOWEST rung,
NOT correctness (bayes_factor was green, off by 10^24). Honest tiering of the 1399:
  29  proven judgment (exam, hand+probe)
  116 input-hardened (guards reject poison; core math UNVERIFIED)
  1254 health-only (compiles + self-test; ZERO correctness knowledge)

**oracle_sizer.py** — static affordance classifier. FIRST estimate inflated 5x by the library's
own word "oracle" + error-msg "expected" (regex noise). TIGHTENED (strong reference tokens only):
  AUTO(round-trip+ref) 90 (7%) · SEMI(invariant) 128 (10%) · HAND(numeric/opaque) 1041 (82%)

**roundtrip_gen.py** — attempted to CASH the 90 AUTO into real positive oracles (probes, no
mutation; triple gate: identity holds >=3 inputs + self-test green + deterministic).
RESULT: **0/32 clean** on the generic lane. WHY (the real lesson): every codec needs per-pattern
setup a generic builder can't guess —
  - geohash: encode(lat,lon,precision), decode returns (lat,lon,err,err) -> APPROXIMATE round-trip
    within error bounds, not identity, 2-float input
  - bpe: must learn_merges(corpus) FIRST, then round-trip only on in-vocab text
  - WAL/model/event: forward input is a structured object (construct first)
  - autoencoder/range-compression: LOSSY -> identity is the WRONG oracle
PROOF the lane works WHEN wired: geohash 4/4 (within error bounds) + bpe 4/4 (trained, in-vocab),
hand-wired.

**HONEST REVISED SIZING:** zero-touch auto ~= 0%. Round-trip is FAST-ASSISTED (human writes a
3-5 line input+setup harness, tool verifies identity + gate) — ~10-15 patterns/hr vs numeric-truth
~1-2/hr. ~30 genuine codecs reachable this way (excl. lossy + container false-pairs). The 82%
HAND lane is real labor, not automatable. This is the FUNDED ROADMAP, measured — not a green lie.

---
## COMPILE-GATE FINDINGS INTEGRATED (from docs-chat FINDINGS_FOR_TOOL.md) 2026-07-21
Docs chat proposed "compile = positive oracle → ~640 PASSes." VERDICT: REJECTED AS PASS,
adopted as coverage axis. Proof compile≠PASS: bayes_factor.cpp (exam INVALID, off by 10^24)
compiles CLEAN under clang -pedantic -Wall -Wextra. Compile is necessary-not-sufficient —
same class as 'mechanical' which was removed from POSITIVE_ORACLES on 4Q ticket 001.

SELF-CAUGHT THEATER: my own strict-gate run flagged "13 fail-both" — on inspection all 13 are
-Werror-promoted unused-var/func warnings, NOT errors. AND macOS g++ IS clang (Apple clang 21),
so "two-compiler agreement" is unreproducible here — the 20 portability defects are a real-gcc
(.8) phenomenon (gcc transitive-include swallow vs clang -pedantic reject). Retracted the 13
before reporting. The honesty floor caught the tool-builder's own run — the exact Ver lesson.

HONEST INTEGRATION:
1. compiles_strict = NAMED coverage axis (type/mem/portability), recorded, NEVER a standalone
   PASS. A compiled pattern PASSes only with compiles_strict AND a semantic/numeric/invariant
   oracle. Closes the mechanical ~80% boundary for compiled langs (LANG_PRIORS already knew this).
2. CPP_COMPILE_DEFECTS.md (20) + 14 compile failures = CANDIDATE INVALIDs, verify on real-gcc
   host (.8) then freeze. Free regression set — VERIFIED not trusted.
3. 1,276 verified docs = candidate expected-behavior/expected-defect source for answer-key
   expansion; each ⚠️ = candidate INVALID/FLAG, each "clean" = candidate PASS — but every one
   PROBE-VERIFIED before it enters frozen (derive, don't trust — the doc is a lead, not a verdict).
4. Ver-theater + signature-reference wins = field confirmation of laws already encoded. No change.

---
## ASSISTED ROUND-TRIP LANE — 6 REAL SEMANTIC PASSES BANKED 2026-07-21
The bless-half, done right. roundtrip_probes.py: per-pattern assisted oracle (human supplies the
3-5 line setup a generic builder can't guess), harness verifies inverse(forward(x))==x + triple
gate (identity holds all inputs · self-test green · deterministic). NOTHING mutated — probes run
against unmodified library files.

EARNED (6/6, wired into exam expansion as PASS, sweep.judge consults roundtrip_probes):
  geohash_encode_decode.py   decode(encode(lat,lon)) within error bounds 6/6 (approx round-trip)
  bpe_tokenizer_lite.py      decode(encode(text))==text, trained + in-vocab 6/6
  message_encoder.py         Decoder.decode(Encoder.encode(data))==data 6/6
  model_persistence_*.py     from_dict(to_dict).predict == model.predict 6/6
  backslash_escape_codec.rs  decode(encode(bytes))==bytes over full byte range 6/6
  cobs_framing.rs            Cobs::decode(Cobs::encode(bytes))==bytes 6/6

Generic zero-touch = 0/32 (each needs setup); assisted = 6/6 wired in one sitting. Confirms the
sizing: round-trip is FAST-ASSISTED not automatic. EXAM now 35/35 deterministic (26 frozen +
9 expansion). The 6 are PASS candidates for frozen at Illia's word. Ops bugs self-caught during
build: rust rel-path (fixed via _rel), .rs-as-python import (lang-routed). ~24 more codecs remain
wireable (serialize/deslize WAL, cidr, slip/rle) — same lane, more sittings.

---
## ROUND-TRIP LANE EXPANDED — exam 40/40 2026-07-21 (same session)
Wired 5 more codecs. Now 11 in roundtrip_probes.REGISTRY: 10 PASS + 1 FLAG.
NEW PASSes (all triple-gated, unmutated): slip_escape_framer.rs · cidr_ip_math.rs (from_u32<->to_u32)
· crc_framed_packet.rs (serialize-stability) · backup_snapshot_restore.rs (data-identity).
The BLESS-LANE ALSO CAUGHT A KILL: compressed_block_store.rs (RLE) — rle_decode PANICS
'index out of bounds' on empty input (rle_decode(rle_encode([])) crashes; encode handles empty,
decode doesn't). Round-trip lane now emits FLAG-with-evidence (RoundtripDefect) so the tool
reports the REAL reason, not "can't read rust". Illia's ruling pending (candidate FLAG/INVALID).

TWO oracle-design self-corrections during wiring (honest, not bugs in the patterns):
  - backup State is HashMap-backed → byte-stability oracle wrong (non-det iteration); switched to
    DATA-identity (deserialize(serialize).data==data) → 3/3.
  - RLE 0/0 was a PANIC not a wiring miss → surfaced as a real defect, not silenced.

EXAM: 40/40 deterministic (26 frozen + 14 expansion). Session tally: 29→40 graded (10 new PASS +
1 new FLAG). The 10 round-trip PASSes are frozen candidates at Illia's word. ~13 more codecs
remain wireable (WAL serialize, event_sourcing, etc.).

---
## ROUND-TRIP LANE — EXAM 50/50 2026-07-21 (codec lane essentially exhausted)
Wired 10 more clean rust codecs. roundtrip_probes.REGISTRY now 21 entries: 20 PASS + 1 FLAG.
NEW PASSes: base32/base64/hex/base58/base64url(jwt) codecs · run_length_encode (Option-safe,
CONTRAST the panicking compressed_block_store rle) · varint_leb128 (incl u64::MAX) ·
zigzag_signed (incl i64::MIN/MAX) · delta_zigzag (i64 seq) · length_prefixed_framing (multi-frame).
Nice data point: TWO rle impls — run_length_encode.rs PASSes (returns Option, empty-safe),
compressed_block_store.rs FLAGs (returns bare Vec, panics on empty). The lane distinguishes them.

EXAM: 50/50 deterministic — 26 frozen + 24 expansion — {INVALID 12, PASS 31, FLAG 7}.
Session arc: 5/13 (yesterday) → 50/50 (5 langs). 20 round-trip PASSes are frozen candidates.

CODEC LANE EXHAUSTED for clean value-identity round-trips. Remaining name-pairs are NOT value
codecs: csv_to_json (format-convert), tiny_autoencoder (LOSSY), event_sourcing/dead_letter_queue
to_dict (structured-construct), rw_lock/reader_writer_lock/hot_copy/double_buffer/seqlock/
quorum_write (concurrency write/read = locks, not encode/decode). Those need different oracles
(structural/invariant) or are false pairs — NOT round-trippable. Next oracle lanes: invariant-
encode (128 SEMI candidates) or the 82% numeric hand-lane.

---
## PAUSE + COMMIT 2026-07-21 (resume in several hours)
COMMITTED: branch `retrofit-ds-contracts-20260721`, commit 7497d40 — python/data-science
subtree ONLY (123 files: 116 retrofits + 5 prior-session DS fixes + re-signed manifest).
library_verify GREEN. Explicit staging (git add python/data-science/, NO add -A).
NOT committed (left for the parallel line): ~231 mesh docs/compile-marathon files
(cpp/go/rust/non-DS python) + their manifests + stray bare-python/MANIFEST (wrong-level).
Validator tooling (~/ai-lab/pattern-scoring/) is NOT a git repo — saved on disk only.

RESUME STATE (read this first on wake):
- EXAM 50/50 deterministic (26 frozen + 24 expansion · INVALID 12/PASS 31/FLAG 7).
- Round-trip codec lane EXHAUSTED (20 PASS + 1 FLAG in roundtrip_probes.py). 20 round-trip
  PASSes are FROZEN CANDIDATES awaiting Illia's word.
- NEXT LANE OPTIONS: (a) invariant-encode ~128 SEMI candidates (human names property, tool
  checks) · (b) 82% numeric hand-lane · (c) verify CPP_COMPILE_DEFECTS on real-gcc host (.8).
- OPEN GATES for Illia: promote 20 round-trip PASSes to frozen · rule RLE compressed_block_store
  (candidate FLAG/INVALID: empty-input panic) · commit/merge the branch · commit the mesh line.
- Tools built today: retrofit_gen.py · roundtrip_probes.py · oracle_sizer.py (all in validator/).

---
## FIX-CHANNEL OPENED — repairing patterns without corrupting the ruler 2026-07-21
Final mission: fix EVERY defect so the library ships zero known-broken patterns, while the tool
never loses a kill it once had. Protocol in FIX_CHANNEL_PROTOCOL.md. Mechanism: broken snapshot
-> regression_fixtures/ (outside signed lib, keeps INVALID kill-test); live file FIXED + given a
POSITIVE oracle proving the repair -> PASS. A guard alone = FLAG; the fix must be provably correct.

FIXED (2/N):
- bayes_factor_normal_means.py — WRONG-MATH repaired: evidence term now full tau2*S^2/denom
  (was missing n*tau2 factor -> sign-flipped conclusions). Live output 2.96e24 == brute-force
  integration EXACT. Fixture BROKEN.py still mismatches -> INVALID preserved.
- inverse_transform_sampling.py — rate>0 guard added (mirrors exemplary u-guard); positive
  oracle F(Finv(u))==u round-trip holds. Fixture keeps silent-negative-waiting-time -> INVALID.

Both: library re-signed, library_verify GREEN, exam 52/52 deterministic (28 frozen + 24 exp).
New probes.py machinery: _load_fixture() + FIXTURE: exam keys dispatched via probes.PROBES.
QUEUE (batchable, same channel): stacking, bayesian_ab, token_bucket, ttl_cache, log_rank,
4 cpp twins, calibration_curve.cpp, RLE empty-panic, go INVALIDs (backoff/csv/breaker).
NOT COMMITTED (branch retrofit-ds-contracts-20260721 has the retrofits; these fixes staged on top).

---
## FIX-CHANNEL BATCH — 5 python kills healed 2026-07-21 (docs line done, fix-and-ship phase)
Each: broken snapshot -> regression_fixtures/ (keeps INVALID kill-test), live FIXED + POSITIVE
oracle proving the repair -> PASS. Library re-signed per subtree, GREEN, exam deterministic.

FIXED (5):
1. bayes_factor_normal_means.py — wrong-math (evidence term full tau2*S^2/denom); matches brute-force.
2. inverse_transform_sampling.py — rate>0 guard; oracle F(Finv(u))==u.
3. stacking_ensemble.py — _validate_fit rejects NaN/Inf+shape at both fit(); oracle threshold-separates.
4. bayesian_ab_beta.py — _validate_ab rejects successes>trials/negative; oracle P(B>A)>0.95 when B wins.
5. token_bucket_limiter.py — added burst_cap (bucket depth); idle-100s burst 500->10 bounded; rate guard.

EXAM 55/55 deterministic (31 frozen + 24 expansion, {INVALID 12, PASS 36, FLAG 7}). Each fixed
pattern's PASS is exam-frozen-eligible; its BROKEN twin is a permanent INVALID fixture.
QUEUE: ttl_cache (STRONG-FLAG, size() purge + leak), log_rank (contract+coverage), cpp twins
(bayes_factor.cpp/stacking.cpp/calibration_curve.cpp — same fixes in cpp), go INVALIDs
(backoff/csv/breaker), RLE compressed_block_store (empty-panic). NOT COMMITTED (staged on
branch retrofit-ds-contracts-20260721).

---
## FIX-CHANNEL BATCH 2 — ttl_cache + first 2 cpp twins 2026-07-21 (exam 58/58)
7. ttl_cache.py — STRONG-FLAG healed: size() now counts only non-expired (truthful) + purge()
   frees the lazy-expiry leak + ttl>0 guard. Fixture keeps size()-lie -> FLAG; live -> PASS
   (oracle: size()==live count after expiry). [FLAG->PASS, fixture stays FLAG]
8. bayes_factor_normal_means.cpp — wrong-math twin: same formula repair as python
   (full tau2*S^2/denom); in-harness brute-force matches 2.96e24. Fixture -> INVALID.
9. stacking_ensemble.cpp — NaN-silent twin: _validate_fit throws on NaN/Inf/empty before
   std::sort (was UB). Fixture -> INVALID (silent); live -> PASS (NaN guarded).

cpp fix-channel additions: _cpp_harness(fixture=True) compiles broken .cpp snapshots from
regression_fixtures/. Library re-signed (cpp + sysadmin subtrees), GREEN.
EXAM 58/58 deterministic (34 frozen + 24 expansion, {INVALID 12, PASS 39, FLAG 7}).

FIXED TOTAL 9 patterns (fix-channel): bayes_factor(py+cpp), stacking(py+cpp), bayesian_ab,
inverse_transform, token_bucket, ttl_cache. Note log_rank.py was already PASS (no fix needed).
REMAINING: calibration_curve.cpp, log_rank_test.cpp (FLAG UB-hole), go INVALIDs
(backoff/csv/breaker), compressed_block_store.rs (RLE empty-panic), http_parser.rs, + the 20
cpp missing-#include bugs (CPP_COMPILE_DEFECTS.md, on .8). NOT COMMITTED (branch retrofit-ds...).

---
## FIX-CHANNEL BATCH 3 — all 3 go INVALIDs healed 2026-07-21 (exam 61/61)
_go_harness(fixture=True) added for go broken snapshots. Each: snapshot->fixture(INVALID),
live FIXED + positive oracle -> PASS.
10. exponential_backoff.go — guard baseDelayMs in (0,60000] + maxAttempts>0 + shift/product cap;
    absurd base (1<<62) now PANICS instead of silently vanishing to 0. Oracle: absurd base rejected.
11. csv_validator.go — float validation rejects NaN/Inf (ParseFloat accepted them); failed
    coercion emits nil not a raw string in a typed column. Oracle: NaN fails + typed columns stay typed.
12. circuit_breaker.go — success in CLOSED now resets failureCount (consecutive, not cumulative);
    a 50%-healthy service stays CLOSED. Oracle: alternating fail/ok does not trip.

Library re-signed (go subtree), GREEN. EXAM 61/61 deterministic (37 frozen + 24 expansion,
{INVALID 12, PASS 42, FLAG 7}). FIXED TOTAL 11 patterns (6 py + 2 cpp + 3 go).
REMAINING exam kills: calibration_curve.cpp (INVALID), log_rank_test.cpp (FLAG UB-hole),
http_request_line_parser.rs (INVALID), compressed_block_store.rs (RLE FLAG). By-design FLAGs
(NOT defects): atomic_spinlock.rs (ordering un-runnable), power_analysis.py (accidental catches).
Plus 20 cpp #includes on .8. NOT COMMITTED (branch retrofit-ds-contracts-20260721).

---
## FIX-CHANNEL BATCH 4 — remaining exam kills 2026-07-21 autonomous (exam 66/66)
_rust_harness(fixture=True) added. Continued autonomously (Illia walking).
13. calibration_curve.cpp — _validate_cal: equal length + binary labels at both entries
    (was OOB-UB + garbage labels accepted). Oracle: garbage + mismatch both rejected.
14. log_rank_test.cpp — length-mismatch now throws (was OOB-UB silent garbage z). Oracle:
    hand-z exact + mismatch rejected. [FLAG->PASS]
15. http_request_line_parser.rs — validates version NUMBER (digits.digits) not just HTTP/
    prefix + rejects empty header name (E012 theater). Oracle: malformed rejected, well-formed OK.
16. compressed_block_store.rs — rle_decode uses i+1<len (empty-safe; was len-1 underflow panic).
    round-trip 6/6 incl empty. [FLAG->PASS]
17. bloom_filter.go — Resize resets itemCount (state-lie kin of ttl_cache). Oracle: itemCount==0
    + FPR==0 after resize. [STRONG-FLAG->PASS]

EXAM 66/66 deterministic (40 frozen + 26 expansion, {INVALID 12, PASS 47, FLAG 7}).
FIXED TOTAL 16 patterns via fix-channel. All FIXABLE exam kills now healed.
REMAINING exam FLAGs (7): 4 are FIXTURES (preserved kills, correct) + atomic_spinlock.rs
(by-design un-runnable) + power_analysis.py (Illia ruled FLAG) + deadline_ttl.go (STRONG-FLAG:
NaN-immortal-lease guardable BUT clock-rewind-resurrection is a monotonic-clock PRECONDITION
question = NEEDS ILLIA'S RULING, not auto-overridden). NOT COMMITTED (branch retrofit-ds...).

---
## CPP PORTABILITY BATCH + FULL-LIB RUN 2026-07-21 autonomous (fetched CPP_COMPILE_DEFECTS from .8)
Whole-lib run over the FIXED library: 1399/1399 BASELINE-OK; python DS triage PASS 29 · FLAG 327
· SKIP 40 · **ZERO INVALID** (all probe-detectable DS kills now fixed). Silent-acceptance residual:
45 DS patterns (auto-lane 0/18 clean = all judgment-lane: bare alpha/beta demos use legit,
callable params — need Illia per-pattern ruling, NOT auto-guardable).

CPP PORTABILITY: reached .8 (au@172.20.10.8), fetched CPP_COMPILE_DEFECTS.md. Applied 17 fixes
(16 missing-#include + 1 structured-binding-capture in naive_bayes_complement). Report was
INCOMPLETE — pagerank also needed <cstdio> (std::printf), pairwise also <algorithm> (std::find);
caught by verifying on .8's REAL clang++ -pedantic (mac g++ IS clang, includes transitively —
can't reproduce locally). FINAL: 0/17 fail clang++ -pedantic on .8, all compile locally.
Fixes: dtw/gk_quantile/gradient_boosting/iqr/lift_gain/accel_failure/permutation/walk_forward/
weighted_reservoir/dbscan(algo)/early_stopping(array)/knn(functional)/pagerank(cmath+cstdio)/
pairwise(cmath+algorithm)/query_expansion(algo)/quantile_binning(algo)/naive_bayes(tuple+bindfix).
cpp re-signed, library_verify GREEN, exam 66/66 HELD.

=== AUTONOMOUS SESSION COMPLETE — honest end-state ===
FIXED this mission: 16 exam kills (fix-channel) + 17 cpp portability = 33 patterns.
The library now ships ZERO known-broken patterns that the tool can detect + zero cpp portability
failures. NEEDS ILLIA (did not auto-override): (1) deadline_ttl.go STRONG-FLAG ruling
(clock-rewind = monotonic-clock precondition?); (2) 45 DS judgment-lane silent-acceptors
(per-pattern domain rulings); (3) commit the branch retrofit-ds-contracts-20260721 + the 33 fixes.
NOT COMMITTED. All on disk, GREEN, exam 66/66 deterministic.

---
## ILLIA'S 3 CATEGORY RULINGS EXECUTED 2026-07-21 (deadline_ttl->PASS + tool fix + guards)
deadline_ttl.go: Illia ruled fix-both->PASS. Monotonic high-water-mark clock (rewind can't
resurrect an expired lease) + NaN/Inf TTL guard. Demo's one same-checker-rewind sub-test moved
to a fresh checker. Fixture keeps NaN-immortal+resurrection FLAG. exam 67/67. [STRONG-FLAG->PASS]

45 judgment-lane analyzed = 133 attack-instances, NOT 45 bugs: domain 84 (alpha 31 + beta 18
polymorphic) · zero 27 · NaN 22. Illia rulings:
- CAT-1 (tool false-positives): FIXED the tool, not patterns. executor.py _signed_ok() excludes
  longitude (0=prime meridian) + signed rates (risk_free/decay/*_rate can be 0/neg). R9 "n"
  substring bug fixed (bare "n" matched lon1/mean/min) -> word-boundary for k/n. 45->41 silent
  (4 false-positives removed), exam 67/67 held.
- CAT-2 (alpha/beta polymorphic, 49): docstring-domain lane, DEFERRED (mesh/next session) — most
  aren't defects (smoothing alpha=0 legit, Beta shape beta=1.7 legit, significance alpha in (0,1)).
- CAT-3 (clear guards): tool fix unlocked 4 clean retrofit closures (was 0/18). Applied 3
  non-exam (sharpe_sortino, fft_cooley_tukey, gibbs_sampling); geohash EXCLUDED (it's the exam
  round-trip PASS under a now-corrected path). re-signed, GREEN, exam 67/67.

LATENT BUG FIXED: 2 exam entries had WRONG paths (geohash->information_theory should be
geospatial; model_persistence->architecture should be model_understanding). Graded correctly by
BASENAME dispatch (luck) but the wrong path made retrofit-exclusion miss geohash. Both corrected;
all 67 exam paths now valid on disk.

---
## ALPHA/BETA DOMAINS WRITTEN DOWN + ENFORCED 2026-07-21 (Cat-2 lane, Illia)
Registry: validator/ALPHA_BETA_DOMAINS.md — authoritative per-pattern alpha/beta domains
(the polymorphism is ACROSS patterns, not within: each has ONE clear domain).
CLASSES: significance alpha in (0,1) · shape/concentration alpha,beta > 0 · smoothing alpha >= 0
· unbounded (regression coef / output) = documented NOT guarded.
ENFORCED (6 non-exam patterns, domain guard added to existing validator, self-tests + exam held):
  (0,1): benjamini_hochberg, minimum_detectable_effect, sequential_probability_ratio
  > 0  : crp_table_growth, thompson_sampling_bandit (alpha+beta)
  >= 0 : target_encoding_smoothing
Guard verified rejecting out-of-domain (benjamini alpha=1.5 raises). library_verify GREEN, exam 67/67.
DEFERRED to registry+mesh (no validator anchor / need new validator): beta_binomial_overdispersion,
dirichlet_multinomial_posterior, conjugate_priors, gamma_poisson_conjugate. UNBOUNDED (doc-only,
correct): logit_marginal_effects (beta coef), householder_reflection (beta output). EXAM (skip):
dirichlet_stick_breaking, bayesian_ab_beta, power_analysis.

---
## MESH ORCHESTRATION — 4 alpha/beta validators dispatched 2026-07-21
Sent task to Telegram group -5598143227 (msg id 2930). Spec: ALPHA_BETA_DOMAINS.md; all 4 =
shape/concentration >0. Files: beta_binomial_overdispersion, dirichlet_multinomial_posterior,
conjugate_priors, gamma_poisson_conjugate. Writers build accumulate-then-raise validators
(copy benjamini/thompson shape), self-test must PASS + guard must reject alpha=-2. They do NOT
re-sign — Fable re-signs + runs exam gate on review. Asked them to MENTION @claude_aura_bot per
update so the tool line can track. INCOMING mesh mentions arrive as channel messages to whichever
session hosts the telegram bot — may need Illia to confirm relays (5S/6E on .8) are live + reading.
PENDING: their 4 diffs -> Fable verifies (self-test+reject) -> re-sign python/data-science + others
-> library_verify GREEN -> exam still 67/67 -> commit.

---
## ALPHA/BETA ENFORCEMENT COMPLETE 2026-07-21 (mesh-assisted)
The 4 deferred patterns closed. Mesh: 5S (fifth_state) delivered correct diffs for beta_binomial +
gamma_poisson on .8 (verified textbook-correct); 6E's relay stayed silent so Fable built its 2
(dirichlet_multinomial, conjugate_priors) directly. All applied to .5 canonical:
- beta_binomial_overdispersion: was ACCIDENTAL lgamma-catch on alpha=-2 -> now clean named >0 guard.
- gamma_poisson_conjugate: 4 entry fns guarded (alpha/beta + alpha_prior/beta_prior).
- dirichlet_multinomial_posterior: prior_alpha > 0 (was fully unguarded).
- conjugate_priors: alpha_prior/beta_prior + alpha/beta > 0.
Each self-test PASS + rejects alpha=-2 w/ AuraInputError. re-signed GREEN, exam 67/67. Commit e606d7e.
ALL 16 alpha/beta domains WRITTEN DOWN (ALPHA_BETA_DOMAINS.md) AND ENFORCED. Cat-2 lane closed.
Mesh coordination worked (tag writers directly + they tag @claude_aura_bot back = hub routing);
6E relay flakiness handled by Fable finishing rather than blocking.

---
## HONEST REMAINDER COVERED 2026-07-21 (the last 5 alpha/beta patterns)
All 16 now enforced (correcting the earlier "doc-only" call):
- logit_marginal_effects: beta coefficient — already FINITE-guarded (NaN beta -> raises). Any real OK.
- householder_reflection: beta = reflection scalar (apply_householder just multiplies, no division) —
  FINITE-guarded (was unguarded). Any finite real OK; earlier ">0"/"output" reads both wrong.
- bayesian_ab_beta: prior_alpha/prior_beta > 0 — already guarded (fix-channel).
- dirichlet_stick_breaking (EXAM PASS): alpha > 0 guard ADDED, verified exam verdict PRESERVED (PASS).
- power_analysis (EXAM FLAG): alpha in (0,1) guard ADDED, verified verdict PRESERVED (FLAG).
KEY: frozen exam patterns CAN be hardened safely IF the verdict is verified unchanged (exam 67/67 held).
The ruler is about verdict-stability, not file-immutability. All guards reject bad input; library GREEN.

---
## FOLD 1 — XMT ORACLE-WEAKNESS SCANNER 2026-07-23 (v1.5, technique 1 of 5)
Inherited from forge-gate/tools/xmt_harness.py (ADAPTED, tools stay SEPARATE — never merged).
NEW MODULE: `xmt_scan.py`. Question it answers about OUR tool (not user code): are our PASS
probes HOLLOW? For each PASS probe it body-wipes ONLY the target functions the probe's oracle
exercises (TARGET_FNS map — mutating unused helpers = false hollow, mirrors forge's get_fn filter),
runs the probe against the mutant in a TEMP mirror (P.LIB redirected then restored — the real
signed library is NEVER mutated). Probe still PASSes on a gutted oracle -> HOLLOW (verdict FLAG on
the PROBE, oracle-weakness; NEVER touches library exam verdicts). Negative control (test-of-the-test)
proves detection isn't cosmetic: hollow synthetic oracle survives, solid one is killed.

REAL FINDING (this is the fold's value — XMT earned its place first try):
- probe_token_bucket was HOLLOW. Its oracle was one-sided: `burst <= 11`. A wiped allow_op that
  grants ZERO tokens (burst=0) sails through — a limiter that never admits work was being blessed PASS.
- FIX: two-sided oracle. A correct bucket grants ~cap on an idle burst (real burst == cap == 10):
  granted = burst >= 8 (closes the hollow) AND bounded = burst <= 11 (the BROKEN unbounded kill).
  Now kills both burst=0 (wiped) and burst=500 (unbounded). Re-run: 12/12 SOLID, 0 HOLLOW.

PROTOCOL: evidence card emitted (xmt_report.json + resolved card in xmt_findings/). oracle_coverage
gains kind 'mutation' — a SOLID probe has verified mutation-coverage (its positive oracle actually
exercises its target). FROZEN EXAM HELD 67/67 (XMT is a META-check on probes, never grades the
library — cannot flip a verdict by construction; verified anyway). Version v1.5. 11 probes were
already solid; 1 caught + hardened. Foundation hardened before folds 2-5 build on it.

---
## FOLD 2 — DAIKON INVARIANT MINING (auto-harvester) 2026-07-23 (v1.6, technique 2 of 5)
Inherited from forge-gate/tools/invariant_gate.py (ADAPTED, tools stay SEPARATE). Kept only the
`mine` half (forge's `verify` half checks USER code — not our job) and re-aimed it at OUR signed
library. NEW MODULE: `invariant_mine.py`. Replaces hand-written invariants with auto-mined ones:
run a signed oracle across 100 deterministic seeds, observe outputs, mine scalar ranges (mean+/-4sd)
AND relational invariants (coefficient ratios/signs) — the catch scalar thresholds miss.

HARVEST (3 regression oracles that exist in our lib, ported forge adapters):
- linear_regression_gd: 5 invariants (1 relational). ratio_w0_w1 mined 0.668 (true weights 2.0/3.0). ✓
- ridge_regression_normal_eq: 6 (2 relational). ratio_w0_w1=0.667, ratio_w1_w2=-3.0 (true 2/3/-1). ✓
- polynomial_regression: 6 (2 relational). ratio_c0_c1=0.669, ratio_c1_c2=5.99 (true 2/3/0.5). ✓
All textbook-correct — the fitters recover the generating coefficients AND their ratios.

TWO LAWS HELD:
1. RATIFY BY HAND — every contract written ratified=false; zero verdict weight until Illia flips it.
   `harvest` proposes, `check` skips unratified. I do NOT self-ratify (Illia's explicit law).
2. OBSERVATION-ONLY — reads oracle outputs, never mutates library, never grades the exam.

PROTOCOL: evidence cards emitted (invariant_mine_report.json, verdict=PROPOSAL -> HUMAN-RATIFICATION,
NOT enforced). oracle_coverage gains kind 'invariant' (counts ONLY once ratified). FROZEN EXAM HELD
67/67 (mining is observation-only — cannot flip by construction; verified). Version v1.6.
PENDING ILLIA: review mined_invariants/*.json, ratify the real ones -> they become invariant-kind
positive oracles + regression tripwires (a future edit that breaks a ratified ratio is caught).

---
## FOLD 3 — METAMORPHIC RELATIONS (behavioral oracle) 2026-07-23 (v1.7, technique 3 of 5)
Inherited from forge-gate/tools/metamorphic/ (ADAPTED, tools stay SEPARATE). Forge runs these
(transform, comparator) relations against USER code; we re-aim the SAME relations at OUR signed
oracles. NEW MODULE: `metamorphic_scan.py` (imports the inherited relations UNMODIFIED). A
metamorphic relation needs no ground-truth output — only that a KNOWN input transform yields a
KNOWN output relation. Catches what a single fixed input misses: an oracle right on one case yet
violating the scaling/permutation LAW (memorized-case theater).

SCAN — 9 signed oracles, 31 relations, all function names verified present in our library:
- regression (linreg/ridge/poly): scale-target, shift-target, feature-permutation, ols-approx.
- classification (logreg/knn/tree/nb/perceptron): label-permutation, duplicate-invariance,
  feature/word-order/noise invariance, clean-separable, deep-class-region.
- clustering (kmeans): shift/scale/duplicate invariance.
RESULT: 9/9 patterns hold ALL their laws. 0 violations.

TEETH PROVEN (baked negative_control, runs every invocation): a broken linreg that IGNORES y fails
2/3 laws (scale_target + shift_target); feature-permutation correctly still holds (constant weights
ARE permutation-invariant). Detection is not cosmetic.

PROTOCOL: evidence cards emitted (metamorphic_report.json; PASS -> metamorphic coverage, FAIL ->
INVALID-CANDIDATE with an explicit anti-overfit note: a metamorphic FAIL that contradicts a frozen
PASS means the RELATION is miscalibrated, NOT the ruler). oracle_coverage gains kind 'metamorphic'.
FROZEN EXAM HELD 67/67 (additive/observation-only). Version v1.7. 9 patterns now carry behavioral
positive-oracle coverage on top of their numeric/semantic oracles.

---
## FOLD 4 — TWIN-CONSENSUS / DIVERGENCE (compiled cross-lang) 2026-07-23 (v1.8, technique 4 of 5)
Inherited from forge-gate/tools/twin_consensus.py (ADAPTED, tools stay SEPARATE). Forge's version
verifies USER code and is bound to forge_gate.catalog/runner/verifier; we kept only the two
transferable ideas and re-aimed them at OUR signed library. NEW MODULE: `twin_divergence.py`.
  (a) COMPILED cross-language harness (4Q#9): compile+run cpp (g++/clang++ -std=c++17), rust
      (rustc --edition 2021), go (go build), plus python — capture verdict + stdout metrics.
  (b) TWIN DIVERGENCE (5S#7): a pattern's language twins must reach the SAME self-test verdict.

FULL SWEEP: 466 twin-sets (367 py+cpp, 88 py+go, 11 with rust/R triples), UNCAPPED.
RESULT: 466/466 CONSENSUS, 0 divergent. Every compiled twin agrees with its siblings.

HONEST SCOPE (stated in the module header, not dressed up): the library is already GREEN, so this
surfaced NO new bugs today. Its real value is two things the tool lacked: an independent COMPILED
oracle lane (behavior via the real compiler, not a python probe) and a permanent cross-language
DIVERGENCE TRIPWIRE — a future edit that breaks one twin but not its sibling is caught here.

CALIBRATION CATCH (the fold's honest turn): the first cut compared twin METRIC VALUES and fired 3
FALSE divergences (ab_interleaving, ab_test_srm_check, adaboost) — twins that both PASS but run
DIFFERENT RNG streams (python's RNG != C++'s), so wins=101 vs wins=113 is different random data, NOT
a broken translation. Same wall forge hit; same fix: value-comparison OFF for input-independent
twins (compare_metrics=False). Consensus = STATUS + compile-integrity. The value-diff CAPABILITY is
retained + proven by the baked negative control (agree / status-diverge / metric-diverge all caught),
ready for any future twins wired to a shared deterministic input.

PROTOCOL: evidence cards emitted (twin_divergence_report.json, 466 PASS; DIVERGENCE -> INVALID-
CANDIDATE with anti-overfit note). oracle_coverage gains kind 'xlang'. FROZEN EXAM HELD 67/67
(separate module, observation-only). Version v1.8.

---
## FOLD 5 — CHAOS / FAULT-INJECTION 2026-07-23 (v1.9, technique 5 of 5) — NEW BUILD, no inherited code
Designed against R13 (state-lies-over-time). R13 attacks stateful patterns with adversarial INPUT
SEQUENCES; chaos goes deeper — inject a REALISTIC FAULT into the middle of an operation the pattern
CLAIMS to survive, then check a SURVIVAL PREDICATE (AWS game-day). LAW: a pattern advertised crash-
safe that DIES to its OWN injected fault is INVALID (the safety claim is theater). NEW MODULE:
`chaos_scan.py`. Every probe is paired with a NEGATIVE CONTROL — a crash-UNSAFE variant of the same
operation that MUST die to the identical fault (proves the predicate discriminates safe from unsafe).

THREE GAME-DAYS (fault -> survival predicate), 3/3 SURVIVED, 0 safety-theater:
- atomic_write_temp_rename: crash os.rename before commit -> destination stays intact OLD content
  (never truncated) + no temp litter. NC (direct-to-destination write) DIES: destination truncated.
- write_ahead_log: torn tail (truncate the log mid-last-record) -> replay recovers the 2 COMPLETE
  records, drops the torn one via its checksum/size guard, does NOT crash. NC (blind pickle.loads,
  no incomplete-read guard) DIES: uncaught crash on the torn tail.
- checkpoint_resume: crash json.dump after batch 0 commits -> resume processes every record EXACTLY
  once (correct values). NC (resumer with no checkpoint memory) DIES: batch-0 records duplicated.

HARNESS BUG CAUGHT + FIXED mid-fold: WAL pickles its LogEntry; an importlib module not registered in
sys.modules made pickle fail ("No module named 'chaos_wal'") — which had also made the WAL negative
control "die" for the WRONG reason (pickle artifact, not the torn tail). Registered the module in
sys.modules; both probe and NC now exercise the real fault. (Fold-1 discipline: a green result that
comes from the wrong mechanism is not green.)

PROTOCOL: evidence cards emitted (chaos_report.json; SURVIVED -> chaos oracle, DIED -> INVALID-
CANDIDATE 'safety-theater' with anti-overfit note). oracle_coverage gains kind 'chaos'. FROZEN EXAM
HELD 67/67 (separate module, throwaway temp dirs + restored monkeypatches — library never mutated).
Version v1.9. ALL 5 FOLDS COMPLETE.

## FIVE-FOLD SUMMARY (v1.5 -> v1.9, all exam 67/67)
The validation tool now carries 5 mechanically-independent oracle kinds beyond its v1 semantic/numeric
checks: mutation (XMT), invariant (Daikon, ratify-gated), metamorphic, xlang (twin-consensus), chaos.
Each inherited-or-built ADAPTED (forge code inherited, never merged; tools stay separate). Each proven
with a negative control / test-of-the-test. Two REAL findings surfaced by the folds themselves:
XMT caught a hollow probe (token_bucket) and the chaos harness caught its own pickle-mechanism bug —
both fixed. Nothing in the signed library flipped; nothing was auto-ratified. Frozen ruler intact.

---
## FOLD 2 RATIFICATION 2026-07-23 (Illia / human_agent_project — hand-ratified)
Illia reviewed the mined contracts and hand-ratified all 3 (flipped ratified=true): linear_regression_gd
(5), ridge_regression_normal_eq (6), polynomial_regression (6) = 17 invariants ARMED. Each contract
stamped ratified_by + ratification_note. The invariant oracles are now live (kind 'invariant' counts
in oracle_coverage). check-mode confirmed all 17 hold on the current signed oracles (0 violated).
TEETH: a broken fit that swaps weights (ratio 1.5 vs armed band [0.596,0.740]) is CAUGHT — the
relational tripwire fires on a wrong-ratio regression that scalar per-weight tolerances would miss.
FROZEN EXAM HELD 67/67 (ratification touches only the separate invariant module). Law honored: mined
by the tool, ARMED only by the human. Fold 2 fully closed.
