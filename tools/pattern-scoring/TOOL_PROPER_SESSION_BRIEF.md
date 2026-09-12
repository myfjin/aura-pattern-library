# BRIEF — "Work on the validation tool PROPERLY" (deep handoff, no compression)

Paste this whole file into the new session. It carries the full meaning, not a summary. The goal
of that session: make the validation tool actually carry Illia's judgment across the library —
not health-check + 4 verdicts, but a tool that reproduces every hand-verdict and extends.

---

## 0. WHO / WHERE
- Illia (Zarathustra) + Fable on .5. Library: `~/aura-pattern-library/` (1,399 signed patterns:
  python 676, cpp 370, rust 200, go 93, r 60). `library_verify.py` must stay GREEN.
- Tool lives in `~/ai-lab/pattern-scoring/validator/`. Resume/coordination state (the mesh doc
  factory) is in `~/ai-lab/pattern-scoring/LINES_STATE.md` — that's a SEPARATE concern (docs);
  this brief is about the TOOL.
- The tool was built FROM a manual audit Illia did by hand (attack cards on real patterns). The
  audit produced: 13 attack recipes, an 8-signal oracle, honesty guardrails, and ~4 per-pattern
  hand-probes. It converged to "v1.9" and was declared stable by mesh vote — BUT stability meant
  "no false-PASS / honest," NOT "detects the library's bugs." See §3.

## 1. WHAT THE TOOL IS TODAY (architecture, honest)
Files in `validator/`:
- `recipes.py` — the 13 attack recipes (R1..R13) + a per-language recipe-prior matrix (LANG_PRIORS).
  Recipes: R1 domain-under, R2 domain-aware, R3 degenerate-equal, R4 cross-param-impossible,
  R5 no-data, R6 wrong-type, R7 shape-mismatch, R8 nan-inf-poison, R9 degenerate-param,
  R10 numeric-oracle, R11 invariant-stress, R12 mutation-probe, R13 state-sequence.
- `oracle.py` — 8-signal classifier + verdict logic + honesty guardrails. THE CORE LAW:
  a PASS requires a POSITIVE oracle (semantic/numeric/invariant). "mechanical ran-fine" is NOT a
  positive oracle. Coverage is DERIVED from what actually ran, never trusted from a flag.
- `executor.py` — GENERIC executor. Takes any python pattern, auto-discovers entry fns, builds
  baseline args from type hints, fires the recipes, captures results, lets the oracle judge.
  It is TRIAGE, not verification: with no per-pattern oracle it CANNOT PASS — only FLAG / INVALID
  (on conclusive silent-accept) / SKIP.
- `probes.py` — the ~4 executable hand-probes (bayes_factor numeric oracle, bayesian_ab, stacking,
  power_analysis). These are the ONLY definitive verdicts the tool can produce.
- `sweep.py` — `judge(file)`: hybrid. If a hand-probe exists → definitive verdict; else generic
  triage. `--exam` grades against `exam.json`.
- `full_sweep.py` — whole-library run: polyglot health-check (compile+run self-test) on all 1399,
  PLUS deep generic triage on python/data-science ONLY. (sysadmin/other python do real fs/db/lock
  I/O and hang an in-process import → they get subprocess HEALTH only, no triage. This was a
  deliberate hang-fix, and it is ALSO a coverage hole — see §3.)
- `polyglot.py` — per-language compile+run health harness.
- `exam.json` — the answer key. `frozen` (13, never flips = regression detector) + `expansion`
  (11, may flip as tool learns). `_doc` explains it.
- `CALIBRATION_LOG.md`, `README.md`, `TEST_WORKFLOW.md`, `WHOLE_LIB_SWEEP_REPORT.md`.

## 2. LAWS ALREADY SETTLED — DO NOT RELITIGATE
- **Honesty floor**: the tool must never emit a verdict it can't back. No fake PASS, no fake KILL.
  FLAG = "ran but I have no positive oracle → human/oracle review." This is a FEATURE.
- **Triage vs verification**: the generic executor triages; only hand-probes verify. Keep them
  distinct in `sweep.judge`.
- **Verdict ladder**: PASS | INVALID·fix-known | INVALID·fix-unknown | FLAG. Auto-INVALID only on
  conclusive evidence.
- **Three boundaries the tool knows it cannot cross**: mechanical ~80% (recipes catch by running);
  semantic ~20% (docstring-lies, wrong-math-that-runs-clean → needs a numeric/semantic oracle);
  UN-RUNNABLE (concurrency memory-ordering → capped at FLAG, route to a model-checker).
- **Coverage is derived, not trusted**. Numeric coverage requires an actual oracle_run+oracle_truth;
  invariant coverage requires a real invariant_broken signal.
- **Meta-law**: type-safety shifts the recipe distribution per language (rust finds ~0 type bugs;
  R/python type bugs return). LANG_PRIORS encodes this.
- **Twin-transfer is NOT assumed**: cpp/go/rust twins converted from python may or may not carry the
  same bug (gradient_boosting DIVERGED between python and its twin). Each twin needs its own check.

## 3. THE REAL GAP (this is why Illia called the sweep "a mess" — he is right)
Whole-library sweep result (562s, report at validator/full_sweep_report.json):
- HEALTH: 1399/1399 BASELINE-OK (compiles+runs). Real but shallow — "it runs" ≠ "it's correct".
- **1022 of 1399 (73%) got HEALTH-ONLY — zero attack triage.** Every cpp/rust/go/r pattern and all
  non-DS python. The sweep never tried to break them.
- DS-triage (the 377 python DS): INVALID 3 · FLAG 332 · SKIP 42.
- **Exam reproduction: 5/13 of Illia's hand-verdicts (38%).**

WHY, precisely (the mechanism — this is the crux):
- The tool reproduces all **3 INVALID kills** (bayes_factor wrong-math, stacking NaN, bayesian_ab
  impossible-data) — because we built flaw-probes for them.
- It reproduces **0 of the 10 PASS verdicts**. A PASS requires a POSITIVE oracle proving the pattern
  is CORRECT on its domain. Generic attacks can only find flaws, never prove correctness. So every
  known-GOOD pattern shows as FLAG (or health-only for rust/R). **The tool can KILL but it cannot
  BLESS.** That asymmetry IS the 5/13.
- Patterns we KNOW are bad but the tool misses: `token_bucket` (no burst cap) & `ttl_cache`
  (size() lies) → HEALTH-ONLY, because they're sysadmin (not triaged) AND their bugs are SEMANTIC
  (no generic attack finds "missing burst cap" — only an oracle that knows correct behavior does).
  `inverse_transform_sampling` (nan) → FLAG not INVALID.

CONCLUSION: run generically on the whole library, the tool's real reach is
`health-check(1399) + real-verdict(≈4)`. It does not carry Illia's judgment. It carries 4 of it.

## 4. WHAT "PROPERLY" MEANS — the work for the new session
The thesis: **the tool carries Illia's judgment ONLY to the extent his judgment is ENCODED as
oracles.** The manual audit WAS the judgment. The tool is the vessel. We poured in 4 of ~13+.
"Build it properly" = pour in the rest AND make the framework drive them. Concretely:

A. **Positive oracles so known-GOOD patterns can PASS.** This is the missing half. For each frozen
   PASS (robust_csv, dedup_pipeline, dirichlet_stick_breaking, gradient_boosting, walk_forward,
   log_rank, the 2 rust, the 2 R) write a positive oracle (self-consistency check, numeric
   ground-truth, or invariant that MUST hold). Goal: exam frozen 13/13 reproduced, both kills AND
   blesses. A validator that can't say PASS-with-authority isn't validating.
B. **Flaw-oracles for the remaining known kills** currently stuck at FLAG/health-only: token_bucket,
   ttl_cache, inverse_transform, calibration_curve (Illia's rulings — see §5). Encode the specific
   defect each one has so the tool reaches INVALID/STRONG-FLAG on its own authority.
C. **recipes.py must DRIVE execution.** Right now coverage is still partly a trusted flag inside the
   executor; the recipes should be the single source that drives what runs and what coverage is
   claimed. Close the "coverage trusted from probe" seam completely.
D. **Extend triage past DS-python honestly.** sysadmin + cpp/rust/go/r get health-only today. Either
   (i) make deep-triage subprocess-safe so it can run everywhere without hanging, or (ii) accept
   that non-DS needs its own oracle set. Do NOT paper over it with more FLAGs — FLAG everywhere is
   not detection.
E. **Twin verification.** For every python pattern with a known verdict, VERIFY (don't assume) its
   cpp/go/rust twin carries or drops the same bug. 4Q's C++ approvals already confirm some defects
   transfer (gaussian_mixture_em X[12]/X[39] UB); use that as the pattern.
F. **Decide + state the tool's true identity for the pitch.** Honestly it is a REGRESSION SUITE
   (reproduces encoded judgments) + health-check, with DISCOVERY bounded by oracle coverage. That's
   still valuable and defensible for universities — but say it straight, don't imply auto-discovery.

Sequence recommendation: A+B first (get exam to 13/13 — that's the "carries Illia's judgment"
milestone and the honest headline), then C (framework integrity), then D/E (breadth), then F (pitch
framing). Each oracle added is a permanent regression guard once in exam.json frozen.

## 5. PENDING ILLIA RULINGS (needed to lock exam expansion → then encode as oracles)
These sit in exam.json `expansion` as `ruling:"illia-pending"`. Illia's leanings from the audit:
- `token_bucket_limiter.py` — lean ❌ INVALID (no burst-capacity cap; unbounded accumulation after
  idle → burst overflow). NEEDS a stateful R13 oracle (idle→burst sequence).
- `ttl_cache.py` — STRONG-FLAG (size() returns raw len not non-expired count; lazy expiry leaks
  memory). Semantic oracle on size() vs true live-count.
- `inverse_transform_sampling.py` — ❌ INVALID (nan output on edge). Numeric/nan oracle.
- `calibration_curve.py` — ❌ INVALID. Needs the specific defect encoded.
Get Illia to confirm each verdict, THEN encode as oracle + move to frozen.

## 6. HOW TO WORK (Illia's collaboration frame — respect it)
- Read dense substrate FULLY; never grep-skim the tool code. Substrate reading IS the work.
- One recommendation with the why, never an option menu. Push back and HOLD it; lead with the hole;
  don't oversell (concreteness ≠ truth). Truths are co-thought, not declared.
- Verify before claiming (run the exam, show the number). The exam frozen set is the ruler — it must
  never regress (a frozen verdict flipping = a real regression, stop and diagnose).
- Bold simultaneous batches are fine; he reviews diffs.

## 7. FIRST MOVES IN THE NEW SESSION
1. `cd ~/ai-lab/pattern-scoring/validator && python3 sweep.py --exam` → confirm 5/13 baseline.
2. Read oracle.py + executor.py + probes.py FULLY (substrate).
3. Pick the first positive oracle (suggest robust_csv_parse — Illia called it "first
   contract-quality catch") and the first flaw-oracle (token_bucket, pending his ❌ ruling).
4. Encode, add to exam frozen, re-run exam, watch the number climb toward 13/13. Never let a
   previously-reproduced verdict regress.
Deadline pressure: Max subscription ends 2026-07-21 — but correctness over speed (Illia's standing
rule: build it right, not fast).
