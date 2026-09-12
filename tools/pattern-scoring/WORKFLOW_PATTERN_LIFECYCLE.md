# Pattern Lifecycle Workflow — harvest → verify → review → Illia signs
**v1.0 FINAL · 2026-07-18 · ratified by Illia · distilled from the first full run
(library sweep → fix → cross-model review), 6E's additions merged.**
This is the reusable playbook. Next harvest follows THIS document. Owner of the final word: Illia —
machines VERIFY, only he makes VALID.

---
## Stage 0 — Laws that govern every stage (violating one = the stage's output is void)
1. **Frozen ruler**: every measurement uses a versioned, deterministic, single-source standard.
   New measurement ≠ new ruler. If the ruler must change, version it and re-run from scratch.
2. **Pre-flight**: read board → show proof (real command output) → then claim. No claim without
   its output shown. Applies to humans, Fable, and every mesh agent equally.
3. **The name is a claim, the docstring is a claim** — descriptions must be true to code the
   writer actually read. When unsure, describe less. UNCLEAR is an honest verdict, never a failure.
4. **Validate-my-own-fix**: whoever fixes something re-runs the gate that caught it, plus spot-checks
   their own tooling (today's example: the sheet-extractor bug that manufactured 114 phantom defects).
5. **A rail scoped too wide breaks what it protects**: no mass edits outside the defect list
   (e.g. the 359 assert-WARNs stay untouched until each gets its own per-file oracle re-run).
6. **Signature law**: any edited pattern file → re-sign its language subtree → `library_verify` GREEN,
   or the edit didn't happen. (`~/aura-pattern-library/.venv/bin/python library_verify.py`;
   sign via `folder_nature.mark.signing.sign_directory(<lib>/<lang>, "AURA Pattern Library", key)`,
   key at `~/.config/folder-nature/aura-signing.key`. Watermarks survive comment edits — never re-stamp.)

---
## Stage 1 — HARVEST (existing doctrine, unchanged)
Source of truth: `HARVEST-PLAN-THEMES.md` + per-sphere ORACLE LAW (cause the disaster, prove survival).
Output: pattern files with watermark + signature, ingested into `~/aura-pattern-library/<lang>/`.
**New requirement from this run:** every harvested file MUST carry a top-level description
(what · when · guarantees) at birth — 191 files arrived without one and blocked the human gate later.
Harvest reviewers reject description-less patterns at ingest, not at audit.

## Stage 2 — MACHINE VERIFY (per sphere, at ingest and at any change)
- Oracle/testbed run for the sphere (e.g. `python3 pattern-scoring/testbed/driver.py` → 13/13 expected).
- `library_verify.py` → GREEN.
- Gate suite `~/ai-lab/tools/`: `assert_linter.py` (REJECT = gutted asserts, blocks),
  `determinism_check.py` (REJECT = varies across PYTHONHASHSEED, blocks; NOTE = inspect),
  dup check (normalized-source sha256 across the whole library).
- **Compile gate for compiled languages** (added after this run found 10 cpp files that never
  compiled): `g++ -std=c++17` AND clang-pedantic per portability law; go build; rustc. Run the binary,
  not just the compile — the real gate runs the disaster.

## Stage 3 — DEFECT SWEEP → FIX SESSION (when audit prep or any doubt arises)
1. **Sweep deterministically** (all checks re-runnable, results into a dated dir
   `pattern-scoring/fix_request_<date>/`):
   description layer (missing / <40-char title-only / decl-style; ruler: claim = first real
   comment/docstring block above code, watermark lines skipped, python via `ast.get_docstring`) ·
   watermark presence · dup hash · syntax/compile · assert_linter · determinism · TODO/FIXME.
2. **Write `FIX_REQUEST.md`** — self-contained work order for a FRESH session: exact counts,
   machine-readable `defect_lists.json`, what is CLEAN (marked do-not-improve), per-language fix
   format, the signature law closing sequence, and the completion contract:
   **`COMPLETION_REPORT.md` when done** (files touched · before/after counts · verify output tails).
3. **Fix session executes** (parallel sub-agents fine; each writer READS the code it describes;
   descriptions are DRAFTS for the human gate — "UNCLEAR: …" beats invented confidence).
4. **Audit session re-verifies the report against disk** — never trusts it: re-run library_verify,
   testbed, re-count the defect lists, read at least one fixed file raw.

## Stage 4 — CROSS-MODEL SECOND-PASS (two models, two visions)
Purpose: same-model self-review inherits the writer's blind spots. A different model reviews
all fresh/changed descriptions AGAINST THE CODE before Illia spends his eyes.
- **Commission template** (send in the cockpit group, VIA MENTION — agents filter on @handle;
  an unmentioned message is invisible): scope (exact file count + skip-list), local paths,
  the one law (code-not-prose; the prey is the docstring-lie), verdict format
  `MATCHES / ADJACENT-BUT-WRONG (say what the code actually does) / UNCLEAR` one line per file
  **with the convincing code element cited**, write INCREMENTALLY batch-by-batch (a timeout costs
  one batch, not the run), @mention back when done or blocked.
- **Before commissioning, check the ACCOUNT PAIR's token tank, not the agent**:
  Ver+5S = ihladkyi2@gmail.com · 4Q+6E = llibresnave@gmail.com (budgets pool per account).
- **Ops: bring the material to the reviewer's node.** Remote reads hang on silent auth prompts and
  eat the run's timeout (5S lost a 600s run to this). rsync the library + fix_request dir to the
  reviewer's machine; verify the reviewer's UNIX user can READ the paths **and WRITE the verdict
  file** (6E = `bu` on .8: /home/au is ACL r-x for him → verdicts must go to an open dir like
  /tmp/aura-review; /tmp dies on reboot → pull verdicts to .5 promptly and continuously).
- **Watch the file, not the promise**: monitor verdict-file growth from .5; pull incrementally.
  Check the FIRST batch early for format drift before hundreds accumulate.
- **Close with coverage math, not vibes**: parse both verdict files, set-compare against the
  worklist — unique reviewed / missed / extra / dupes — and verify the tally line by line.
- **All-green is a finding to test, not to celebrate**: an all-MATCHES sweep means clean material
  OR shared blind spot. Counterweight: an independent spot-check by a third mind (this run: 3 files
  from the fuzziest corners, checking that descriptions disclose their own quirks), and over-sample
  the reviewed files in Stage 5's Part C.
- Artifacts: `<AGENT>_review_<date>.md` per reviewer, pulled to .5, referenced in the memory record.

## Stage 5 — ILLIA'S MANUAL GATE (the only VALID-maker; brief: `MANUAL_TESTING_BRIEF.md`)
- **Part A — description gate**: sampled batches from `manual_audit_prep/DESCRIPTIONS_SHEET.csv`
  (rebuilt under the frozen claim-ruler). Per pattern: ① what it does ② when to use ③ what it
  guarantees ④ plain-words understandable ⑤ next-person understandable. Any no → GONE
  (archived, reversible — never hard-deleted). Checklist replaces vibes; good-day = bad-day verdicts.
- **Part B — his abuse session**: ~10–15 runnable patterns, HIS garbage (wrong numbers/letters/
  languages). Three-way rule: errors ✅ · handled-per-contract ✅ · silent wrong output ❌ INVALID.
  Fable runs commands, shows raw output, never softens a silently-wrong into "edge case".
- **Part C — code-vs-claim sample**: ~5% random (seeded, reproducible) weighted toward fuzzy
  data-science + freshly-touched files (restructured 8, the 230 fresh descriptions) + anything
  A/B made suspicious. Hunt where machines are blind: circular asserts · docstring lies ·
  planted-easy test data.
- Every verdict → dated form `output/manual_audit_<date>.csv` (file · part · verdict · evidence) —
  the audit itself is re-runnable evidence.
- **Every pattern that completes the gate → a PATTERN SHEET** (`sheets/<name>.sheet.md`, template
  in `sheets/PATTERN_SHEET_TEMPLATE.md`): what it solves · input contract · how inputs shape the
  output · worked example with REAL audited output · failure modes from the catalog · provenance.
  Added 07-19 (Illia): the teaching layer — target audience universities/students; the audit
  generates the material for free; mass production for untested patterns = re-run of Stages 3–5.
- **Every error observed in Part B → an `ERROR_CATALOG.md` entry** (AURA-E### · B-class ·
  CONTRACT/ACCIDENTAL quality · plain-words meaning · ideal message). Added 07-19, Illia's ruling:
  the catalog is built DURING testing (costs nothing, testing generates it) and becomes the spec
  for the later code-level retrofit — which stays a separate gated lane (paid tier, per-file re-gate).
  New verdict shade this created: **PASS-WITH-FLAG** = survives the three-way rule but all catches
  are accidental/cryptic → retrofit candidate, not GONE.
- Library-level: clean sample → VERIFIED set earns trust, university claim stands. Rubber-stamping
  found → fix the ruler, not the number.

---
## Roles (as proven in this run)
| Who | Lane |
|---|---|
| Illia | Definition-work, the gate, the signature. The only VALID. |
| Fable (.5) | Orchestration, sweeps, verification-of-verifiers, docs, memory, cockpit relay. |
| Fix session (fresh Fable) | Executes FIX_REQUEST, writes COMPLETION_REPORT. |
| 5S / 6E / Ver / 4Q | Cross-model review + commissioned builds; chosen by account-pair budget + field fit. |

## 6E's additions (restated 07-18, discussed Fable↔6E via mentions; source:
## `fix_request_2026-07-18/6E_additions_2026-07-18.md`)
1. **[AGREED — now law] Fixer ≠ verifier, per artifact class.** Compile repairs get an independent
   compile+RUN by a second party before the gate (6E's demand; Fable ran all 10: OK). Determinism
   fixes get an independent determinism_check re-run (done: OK). Generalization: every fix class
   names its verifying gate, and someone other than the fixer runs it.
2. **[AGREED] Accuracy ≠ value.** Expanded descriptions can be factually true yet mechanical
   padding. Part A over-samples 6E's prose-quality picks: `gradient_descent_momentum.cpp`,
   `doubly_robust_aipw.cpp`, `soundex_phonetic.cpp`, `space_saving_heavy_hitters.cpp`.
3. **[AGREED, scoped] Cross-file terminology scan** — optional Stage-3 sweep extension (related
   patterns should share vocabulary). Checked 6E's top pair: allocator files have no clash
   (different concepts); residue = `budget_allocator.go`'s misleading FILENAME → gate watch-list.
   Not a gate blocker.
4. **[OPEN — Illia rules] The 4 oracle-parity legacy descriptions** (`exponential_reliability_mtbf`,
   `fft_cooley_tukey`, `exponential_histogram_count`, `feature_hashing_trick` — all cpp):
   intentionally brief, two-tier style vs the full format. 6E: expand or explicitly label.
   Fable: label "legacy, kept as-is" + Part A MUST-REVIEW; rewrite only if Illia GONEs them
   (avoids an edit+re-sign cycle the gate may prove unnecessary). Awaiting 6E counter / Illia.
5. **Part A MUST-REVIEW list (from this discussion):** the 4 legacy files (item 4) + the 4
   prose-quality picks (item 2) + the 6 self-flagged honesty caveats from COMPLETION_REPORT
   §Honesty caveats + `budget_allocator.go` filename question.

## Change log
- v1.0 (2026-07-18): first distillation, from the sweep→fix→review run of 07-18. Author: Fable,
  with Illia's rulings inline (comprehension gate, drafts-not-final, wait-then-mention protocol).
