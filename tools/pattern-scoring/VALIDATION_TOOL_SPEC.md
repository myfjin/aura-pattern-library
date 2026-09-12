# VALIDATION TOOL — merged specification v0.6 (honesty guardrails from 5S+4Q final review)

## v0.3 resolutions (from round-2, Fable adjudicating; sources: {4Q,6E}_round2_2026-07-19.md)
- **v1 FINAL SCOPE (6 modules):** ① abuse-fuzzer w/ boundary recipes folded in (4Q; P3 dissolves
  into recipe corpus) ② numeric oracle NARROWED to hand-verified math patterns + template (6E's
  keep × 4Q's narrowing) ③ output plausibility P2 (6E) ④ invariant probe grid P1, manual
  invariants for exam set (6E; auto-harvester → v1.5) ⑤ flaky-oracle detector, 3 seeds (4Q)
  ⑥ evidence-card emitter, full JSON schema (4Q). Combined-fault: v1 = PAIRWISE on individually-
  failing fixtures only (Illia's requirement kept alive cheaply); full-stack → v1.5.
- **GOVERNANCE (adopted verbatim from both):** Illia = ground truth, always. Every mismatch →
  calibration ticket in CALIBRATION_LOG.md (date | pattern | tool verdict+reason | Illia
  verdict+reason | resolution | rule rewritten?). False alarms: 3 same-class strikes before a
  rule rewrite. **Missed kill: immediate rewrite, no waiting** (6E's asymmetry). Anti-overfit:
  a change may not flip previously-correct verdicts; every change bumps tool version and re-runs
  the full exam (4Q).
- **ENTRY-POINT CONVENTION (6E's A3, resolved):** manifest-driven, not wrappers —
  `patterns_manifest.json`: {file, entry_fn, args:[{name,type,domain}], returns}. Seeded from
  ABUSE_CANDIDATES signatures for the exam set; auto-derivation later.
- **EVIDENCE-CARD JSON (4Q's schema, adopted + combo answer):** fields = pattern, severity
  (INVALID/FLAG/FLAKY/PASS), class, function, fixture, expected, actual, why, confidence,
  repro_cmd, seeds[], combo_id. One card PER violation; shared combo_id groups simultaneous
  faults (4Q's lean, confirmed).
- **Build split confirmed:** 4Q = ①⑤⑥ · 6E = ③④ (+ helps integration; P3's recipes handed to
  4Q's corpus) · Fable = manifest, integration, pairwise wiring, exam runner, CALIBRATION_LOG.


**2026-07-19 · sources: Illia's manual audit (batches 1–2, ground truth) + Fable spec v0.1 +
4Q vision (10 proposals) + 6E vision (5 proposals) — full files in
`fix_request_2026-07-18/{4Q,6E}_tool_vision_2026-07-19.md`. Status: awaiting Illia's ruling on
v1 scope, then ONE more agent loop (Illia's protocol), then build.**

## The bar (6E's formulation, adopted)
> "Not catching everything — catching everything he's already found."
The tool is trusted only after it reproduces Illia's ~50 hand-verdicts: every kill caught,
no false alarms on his passes. His judgment is the exam; the tool carries it at machine speed.

## Kill-to-mechanism map (6E's analysis, adopted as the spec's spine)
| Illia's kill | Root cause | Mechanism | Origin |
|---|---|---|---|
| bayesian_ab_beta | impossible data blessed | Invariant probe grid | **6E P1** |
| stacking_ensemble | NaN → output identical to clean | Output plausibility + noise-identity check | **6E P2** |
| bayes_factor_normal_means | wrong formula, plausible numbers | Numeric oracle | Fable v0.1 (from Illia's find) |

## v1 (build first)
- Semantic abuse-fuzzer (B-class recipes from Illia's attack corpus) — Fable v0.1
- **Numeric oracle** (closed-form vs brute computation at probe points) — Fable v0.1
- **Combined-fault injection** (all violations in ONE report; pairwise + full-stack) — Illia 07-19
- **Output plausibility** incl. noise-identity + sequential-call state check — **6E P2** (cheapest, zero metadata)
- **Invariant probe grid** (machine-readable invariants stressed at edges; harvest invariants
  from existing asserts + audit sheets, don't hand-write — Fable's cost correction) — **6E P1**
- **Boundary value analysis** (deliberate n=0/1/MAX probes; fuzzers don't aim) — **6E P3**
- Flaky-oracle detector (multi-seed verdict stability; "flaky" is a first-class verdict) — 4Q #6
- Adversarial evidence cards (invariant · counter-example · why · confidence · repro cmd) — 4Q #8
- Exam against Illia's hand-verdicts — Fable v0.1

## v1.5
- Oracle-weakness scanner / mutation testing (would the asserts pass a no-op? a flipped sign?) — 4Q #1
- Semantic inversion (test the ACCEPT side of every guard: tiny-valid must pass) — 4Q #2
- Description drift watch (post-fix-session diff of claims vs exported symbols) — 4Q #10

## v2
- Cross-pattern coherence bank (sibling patterns must agree on shared textbook fixtures) — 4Q #5
- Numerical stability sweep (ill-conditioned inputs; output ≠ initial guess; perturbation-stable) — **6E P4**
- Compiled-language harness (cpp/rust/go entry-point stubs, compile AND run) — 4Q #9

## v3
- Claim extraction + automated verification (metadata `claims:` field → generated tests;
  unautomatable claims routed to Illia's Part C) — merged design: 4Q #3 ⊕ **6E P5**

## Standing principles
- Tiered execution by token cost (quick/medium/heavy; the account-pair tank is finite) — 4Q #7
- Scoping correction (Fable): plausibility PRE-gate (4Q #4) applies ONLY to the tool's own
  guarantee-testing fixtures — never to abuse inputs, where impossible data IS the test.
- ~~OPEN: disagreement protocol~~ **RESOLVED by Opus 4.8, 2026-07-19 — adopted in full:**

## Disagreement protocol (tool verdict ≠ Illia verdict) — design by Opus 4.8
**Principle: Illia is ground truth by default, but disagreements resolve by MECHANISM, not
authority.** Neither "Illia always wins" (tool = parrot, can never catch what he missed) nor
"tool always wins" (the moving ruler with extra steps). The ruler changes only via a dated,
reproducible mechanism — never fatigue or mood.
- Every disagreement is a first-class event: halts auto-verdict on that pattern, opens a
  CALIBRATION_LOG.md ticket — `date | pattern | tool verdict + mechanism reason | Illia verdict
  + reason | category | who moved | rule changed?`. Never averaged, dropped, or settled by seniority.
- **Tie-breaker = demonstration, not vote.** Tool's burden: reproducible fixture (repro_cmd +
  seed) + the invariant/counter-example justifying its verdict. Illia's burden: why it's correct
  behavior (contract permits it / abuse-input-IS-the-test exemption / textbook).
- **Case 1 — tool PASS, Illia KILL (missed kill):** Illia wins immediately, tool rewritten NOW
  (6E's asymmetry, extended). The one error you cannot ship.
- **Case 2 — tool KILL, Illia PASS (false alarm):** tool's verdict SUSPENDED, not discarded —
  Illia must actually look at the fixture. Spurious mechanism → tool moves (after 3-same-class
  strikes). Mechanism exposes a real untested edge → **Illia moves: PASS becomes KILL, logged as
  a "TOOL TAUGHT" event** — the only channel by which the tool corrects the human, gated on a
  mechanism he accepts; counted separately (the tool earning its keep).
- **Anti-un-freeze rule:** a ground-truth verdict changes only through a logged ticket with a
  mechanism attached. That constraint IS the difference between a frozen ruler and a drifting one.
- **Overfit guard on the loop itself (4Q's rule):** no resolution may flip a previously-correct
  exam verdict; if it does, the rule is wrong — escalate to design change, don't patch. Every
  resolution bumps tool version + re-runs the full exam.
- *Refinement note:* round-2's "the tool never overrules a human ruling" stands — in the
  TOOL-TAUGHT channel the tool doesn't overrule Illia; Illia moves himself on accepted evidence.

## Attribution ledger
6E: P1, P2, P3 in v1 · P4 in v2 · P5 in v3 — **all five proposals adopted.**
4Q: #6, #8 in v1 · #1, #2, #10 in v1.5 · #5, #9 in v2 · #3 in v3 · #7 standing · #4 adopted-with-narrowing.
Illia: the ground truth, the combined-fault requirement, the receipts-harness idea, and the bar itself.
Opus 4.8: the disagreement protocol (mechanism-over-authority, TOOL-TAUGHT channel, anti-un-freeze rule).

## TOOL LESSON — cross-language efficiency (Illia's insight, 2026-07-20, PROVEN)
**Logical bugs transfer through faithful conversion; language-specific failures do not.**
Proof: bayes_factor's wrong formula (missing n·τ² factor) is byte-identical in python AND its
cpp twin (`y_mean*y_mean*n/denom` both). So:
- The tool audits ONE language deeply (python — richest attack surface, easiest to drive).
- For each CONVERTED twin (cpp/go-from-python), it does NOT re-audit the logic. It runs a cheap
  STRUCTURAL DIFF confirming the flagged expression transferred (→ inherit the verdict), PLUS a
  per-language probe for modes the source can't have: C++ UB (out-of-bounds read on mismatched
  containers = silent garbage, not IndexError), integer overflow, -ffast-math NaN, silent
  truncation; rust debug-panic vs release-wrap.
- NATIVE patterns (all rust; go sysadmin; r) have NO twin → full audit, genuinely new logic.
This is a ~5× multiplier: 1 deep audit + N cheap twin-confirmations, not N deep audits.
Maps to 4Q proposal #5 (cross-pattern coherence) extended across LANGUAGES. → v1.5 tool feature.

## VERDICT AUTHORITY + FIX CATEGORIES (Illia, 2026-07-20; from the mnemos session)
Extends the disagreement protocol. Resolves "auto-mark or flag?".
**Principle:** the tool OWNS the verdict — it auto-marks INVALID on its own authority when evidence
is conclusive (mechanism + repro); it does not merely flag and wait. But it is honest about whether
it owns the FIX. Invalidation is a judgment it can stand behind; repair is split by real confidence.
The tool never emits a fix it can't back.

### The four-verdict ladder
1. **PASS** — survived every attack (the disaster happened, it held). Tool-authoritative.
2. **INVALID · fix known (Category A)** — conclusively broken AND the tool has a concrete,
   mechanism-backed repair. Emits: `verdict: INVALID`, `fix_available: true`, `fix: <specific
   edit/mechanism>`, `fix_confidence`, + failing fixture + why. INVALID stands on the tool's
   authority; the fix is a recommendation (human applies; or auto-apply + re-run exam if later enabled).
3. **INVALID · fix unknown (Category B)** — conclusively broken, but NO fix the tool is confident
   in (ambiguous, or needs human intent). Emits: `verdict: INVALID`, `fix_available: false`, routed
   to Illia's queue with full evidence, NO fabricated fix. **A wrong fix is worse than an honest
   "I don't know how to fix this."**
4. **FLAG** — suspicious but NOT conclusive on validity. Not auto-INVALID. Routed to Illia to decide
   validity (the honest floor — the tool admitting it can't tell yet, not a guess dressed as a verdict).

### Composition with the disagreement protocol
An auto-INVALID is authoritative UNTIL Illia contests it. If Illia thinks an INVALID pattern is
actually valid → calibration ticket, resolves by MECHANISM not authority (whoever shows a mechanism
the other accepts wins; logged; ruler moves only on evidence). The tool's power to auto-invalidate
is real but never unchecked — bounded by the calibration loop.

**Why honest:** the tool ACTS (invalidates) where sure, DEFERS (FLAG / Category B) where not, never
emits a fix it can't back. Agency + a conscience about the edge of its own competence — the same
two-layer honesty as aura-mnemos (act when healthy, say "down" when not).

## FINAL-REVIEW ADDITIONS (5S + 4Q, 2026-07-20) — HONESTY GUARDRAILS, not new recipes
Both independently concluded the 13 recipes are complete; the risk is FALSE VERDICTS. Convergent
findings adopted. 5S's thesis: "the biggest risk is silently PASSing when it should say I cannot tell."

### ADOPTED into v1 (low-cost, make the tool honest before powerful — 5S's build order)
1. **oracle_coverage field** (5S#1, ⊇4Q#3/#9) — every card carries
   `oracle_coverage:{mechanical,semantic,numeric,un_runnable}`. **A PASS REQUIRES ≥1 positive
   oracle; all-false → FLAG.** This operationalizes the honest floor — no silent PASS.
2. **Attack-reachability check** (5S#2) — before P2 noise-identity judges "garbage output ==
   clean output = fake-robust", confirm the poisoned value ACTUALLY REACHED the function
   (return-visible or side-effect). If not → `attack_did_not_reach`, exclude from judgment.
   PREVENTS FALSE-KILL on no-op attacks (exactly Illia's X=[]-before-generation discovery).
3. **Harness honesty gate** (5S#3) — prefer direct `entry_fn` call over file-harness. If a
   harness is silent/ambiguous on success (token_bucket printed nothing) → `FLAG: harness
   untrustworthy`, never PASS. A correct-but-untestable pattern is a TOOL failure, not a pass.
4. **Frozen + expansion exam split** (5S#4) — resolves a real spec contradiction: anti-overfit
   forbids flipping exam verdicts, but TOOL-TAUGHT requires it. FIX: Illia's original ~50 =
   FROZEN (flip = regression); newly-found kills/twins = EXPANSION (flip = learning event).
5. **Twin DIVERGENCE detector** (5S#7 ⊇ 4Q#8) — replace structural-diff with BEHAVIORAL diff:
   run the source's FAILING recipes on the twin. Same failure → inherit. Twin survives a recipe
   source failed → divergence alert, independent audit (this is what gradient_boosting.cpp needed).
   Twin fails a NEW way → language-specific card (C++ UB etc).
6. **Concurrency verdict cap + liveness split** (5S#8 ⊇ 4Q#4) — AST-detect Atomic/compare_exchange/
   thread::spawn/Mutex → mandatory `ordering: unverified_by_execution`, verdict capped at FLAG for
   ordering. BUT still stress-test LIVENESS/lock-load-bearing (Illia's remove-lock→panic). The
   boundary caps only the ordering claim, not all lock testing.
7. **Per-language recipe-prior matrix** (5S#5) — META-LAW as a measured dial, not prose. Starting
   matrix (language × recipe-class weight) in 5S_final_vision; rust R6/R8→0.0, R11→1.5; python/R
   baseline 1.0. Versioned artifact, tuned as audit data grows.

### ADOPTED into v1.5 / v2 (semantic depth — after honesty guardrails prove out)
- **Claim-strength oracle E011-vs-E012** (5S#6 ⊇ 4Q#6) — existence probe (does code contain ANY
  branch that could enforce the claim?) + falsification. exists+fails=E011 over-scoped(FLAG);
  absent+fails=E012 theater(INVALID-fix-known). v1.5.
- **Validation-depth probe** (4Q#6) — malformed input at syntactic/semantic/domain levels; count
  guarded levels. Concrete method for E012. v1.5.
- **Statistical rare-mode detector** (4Q#5) — many seeds, flag bimodal/rare-catastrophic modes
  (flaky detector catches non-determinism, NOT 5%-catastrophic). For bandits/MCMC/forests. v2.
- **Unit/dimension-scaling oracle** (4Q#2) — scale input by k, check output scales predictably;
  catches misinterpreted-unit bugs that pass numeric oracles. v2, human-assisted.
- **Composition/pipeline probe** (4Q#1) — chain compatible patterns, check end-output not silently
  degraded. v2. · **Name-claim mismatch flag** (4Q#7) — human-review only, no auto-verdict. v2.
- **Empirical tiering log** (4Q#10) — measure per-recipe runtime/language for evidence-based tiers. v2.

Attribution: 5S — 7 adopted (5 in v1); the honest-floor guardrails are his. 4Q — 10 proposals,
~4 unique adopted (rare-mode, unit-scaling, validation-depth, composition), rest converged w/ 5S.
