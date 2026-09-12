# FOLD PLAN — inherit 5 verification techniques into the validation tool
*Resume anchor (written 2026-07-23, pre-compression). READ THIS FIRST on wake for the fold work.*

## STATE (the mission that's DONE — don't redo)
Validation tool complete + MERGED TO MASTER (`~/aura-pattern-library` commit bd39f63):
exam **67/67 deterministic** (5 langs), library_verify GREEN, whole-lib 1399/1399 zero-invalid.
All fixable defects healed (fix-channel: broken→regression_fixtures/, live→PASS+positive-oracle),
17 cpp portability fixed, all 16 alpha/beta domains written+enforced (ALPHA_BETA_DOMAINS.md).
Key files: validator/{recipes.py=attack corpus, executor.py, oracle.py, probes.py, exam.json,
sweep.py, CALIBRATION_LOG.md, FIX_CHANNEL_PROTOCOL.md}.

## THE NEW TASK — fold 5 techniques, ONE AT A TIME (order 1→2→3→4→5, never two at once)
Source: ~/ai-lab/research/TESTING_TECHNIQUES_RESEARCH_2026-07-22.md +
TESTING_ARCHITECTURE_2026-07-23.md (sound but omits #5 chaos).
Working code for 1-4 on .8: `au@172.20.10.8:/home/au/forge-gate/tools/`
(xmt_harness.py, invariant_gate.py, metamorphic/, twin_consensus.py). #5 = new build.
LAW: ADAPT the code, don't reinvent. Keep validation tool SEPARATE from Forge Gate (inherit code,
NEVER merge the tools). Ratify mined artifacts BY HAND; never enforce an un-ratified one.

PER-FOLD PROTOCOL (every technique):
1. Emit the existing evidence-card JSON (pattern, severity, class, fixture, expected/actual, why,
   confidence, repro_cmd, seeds[], combo_id) — NOT ad-hoc output.
2. Map to the 4-verdict ladder: PASS · INVALID·A (fix-known) · INVALID·B (fix-unknown) · FLAG.
3. Count in oracle_coverage as a new positive-oracle KIND (mutation/invariant/metamorphic/xlang/chaos).
4. Run against the FROZEN exam — MUST NOT flip a verdict (if it does, the MODULE is miscalibrated,
   not the ruler). Version bump. CALIBRATION_LOG entry. Report exam result on mesh bus.

THE 5 (order):
1. XMT (mutation) → v1.5 oracle-weakness scanner. DO FIRST: it checks the tool's OWN fixtures for
   hollowness (would asserts pass a no-op / flipped sign?). Code: xmt_harness.py (17/17 proven).
2. Daikon invariant-mining → invariant-probe grid AUTO-harvester (was hand-writing invariants).
   Code: invariant_gate.py (mine mode). Human ratifies each mined invariant.
3. Metamorphic relations → unit/dimension-scaling oracle generalized (scale input→output scales).
   Code: forge-gate/tools/metamorphic/.
4. Twin-consensus/divergence → compiled-language harness + behavioral twin-divergence (run the
   source's failing recipes on the twin). Code: twin_consensus.py. ~5x audit multiplier.
5. Chaos/fault-injection → strengthens R13 state-lies-over-time. AWS game-day: inject a realistic
   fault + declare a survival predicate; a "crash-safe" pattern that dies to its OWN fault = INVALID.
   NO code — new build, design against R13.

## PROGRESS
- [x] Fold 1 XMT (v1.5, 2026-07-23 — 12/12 SOLID; caught+fixed probe_token_bucket hollow; exam 67/67)   [x] Fold 2 Daikon (v1.6, 2026-07-23 — 3 oracles, 17 invariants/5 relational mined ratified=false; exam 67/67; PENDING Illia ratification)   [x] Fold 3 Metamorphic (v1.7, 2026-07-23 — 9 oracles/31 relations all hold; teeth proven by baked negative control; exam 67/67)   [x] Fold 4 Twin (v1.8, 2026-07-23 — 466/466 twin-sets consensus, 0 divergent; metric-FP trap caught+disabled; exam 67/67)   [x] Fold 5 Chaos (v1.9, 2026-07-23 — 3 game-days all SURVIVED, negative controls prove teeth, WAL pickle-harness bug caught+fixed; exam 67/67)
ALL 5 FOLDS COMPLETE (v1.5→v1.9). New oracle kinds: mutation·invariant·metamorphic·xlang·chaos. Two real findings (hollow token_bucket probe; chaos pickle bug) caught+fixed. Ruler intact.
(update this line as folds land; each fold = its own commit + CALIBRATION_LOG entry + exam-held proof)

## BUSINESS FRAME (from Illia, the thread)
Money now = be testers who tell the truth (that's who we are). This tool is ONE improvised session,
NOT the defining work (Brain, whypass, the pattern library, time-travel are the deeper range —
held for when there's money to live AND create). Test, earn, hold the bigger vision.
