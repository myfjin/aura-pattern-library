# Findings from the doc-verification marathon → for the tool-building session (2026-07-21)

Context: while the tool session builds positive oracles, the documentation session verified 1,276/1,399
library patterns with a writer(6E/5S)→approver(4Q/Ver) loop. 4Q's key move was a COMPILE-GATE on the
compiled languages. These findings are the reusable output.

## 🎯 THE BIG ONE — the compiler IS a positive oracle for ~640 patterns
The tool's core gap (from TOOL_PROPER_SESSION_BRIEF): it can KILL but can't BLESS — no positive oracle,
so healthy patterns FLAG instead of PASS. For COMPILED languages this is already solved:
- **C++ (370): `g++ -std=c++17 -pedantic -Wall -Wextra` AND `clang++ -pedantic`** — two-compiler agreement.
- **Go (93): `go build` AND `go vet`** — vet catches real races/goroutine-leaks/nil-derefs, not just syntax.
- **Rust (200): `rustc`/`cargo`** — strongest of all (borrow checker), BUT rustc must be installed
  (it's at /home/bu/.rustup/.../bin/rustc on .8, not in au's PATH — au needs it or route to bu).
A clean two-compiler pass under -pedantic is a genuine POSITIVE oracle — not proof of correctness, but a
real, mechanical, PASS-worthy signal. Wiring compile-check as an oracle gives the tool real PASSes on
~640 of the 1,399 patterns immediately. This is the compiled-language analogue of the "assisted codec /
round-trip PASS" — the compiler is the assist.
LIMIT (matches the tool's UN-RUNNABLE boundary): concurrency memory-ordering / logical races are NOT
compile-catchable (rust/go). Those stay FLAG → model-checker, exactly as the tool already scopes.

## 🐛 REAL BUGS the compile-gate surfaced (a verified INVALID inventory for the tool)
- **C++: 20 portability defects** → `CPP_COMPILE_DEFECTS.md`. Dominant class: missing `#include`
  (<tuple>/<algorithm>/<array>/<functional>) that g++ swallows via transitive includes but clang -pedantic
  rejects. e.g. dtw_dynamic_time_warping, dbscan_clustering, early_stopping, gradient_boosting_stumps,
  iqr_outlier_detection, knn_kdtree_accelerated. These are real: the pattern does NOT compile strict.
- **Total compile failures logged across langs: 14** (in 4Q_DOC_APPROVALS.md).
- These are ground-truth INVALIDs the tool should reproduce — a free regression set beyond the manual audit.

## 🎭 VERIFICATION THEATER is the enemy (validates the tool's honesty floor)
Ver (one approver) drifted to RUNNING the code (exec) instead of checking docs, and emitted a confident
"60/60 CODE-VERIFIED APPROVED" that measured the WRONG thing (does it run ≠ is it correct/accurate). The
tell: 0 mismatches where the real verifier (4Q) found doc-errors in nearly every batch. LESSON FOR THE
TOOL: "ran clean" must NEVER count as a positive oracle — a PASS needs a semantic/numeric/invariant/compile
oracle, and coverage must be DERIVED from what actually ran, not trusted from a self-report. The tool
already encodes this (mechanical-coverage removed) — this is field confirmation it's the right law.

## 🔧 Mechanical > model self-report (the signature-reference win)
6E (small model) fabricated plausible-but-wrong signatures even when told to copy. FIX that held across
1,000+ patterns: auto-extract the REAL signatures into SIGNATURES_REFERENCE_*.md and have the writer copy
verbatim → fabrication → 0. TOOL PRINCIPLE: prefer mechanically-derived oracles/fixtures over anything the
model asserts about itself. (Same reason the tool derives coverage instead of trusting the probe.)

## 📦 What the doc pass HANDS the tool
- **1,276 verified per-pattern docs**: each = real signature + input contract + one honest ⚠️ defect,
  cross-checked against source (and compiled, for C++/Go). This is a per-pattern EXPECTED-BEHAVIOR /
  EXPECTED-DEFECT reference the tool can consume to build per-pattern oracles or an expanded answer-key.
- Location: /tmp/aura-review/pattern-scoring/docs_draft/ (6E-*/5S-* batch files + SIGNATURES_REFERENCE_*.md).
- The ⚠️ defect notes are candidate INVALID/FLAG expectations; the "no defect, compiles clean" ones are
  candidate PASSes (with the compile oracle backing them).

## RECOMMENDATION for the tool session
1. Wire compile-check (g++/clang, go build+vet, rustc) as a POSITIVE oracle for the compiled sphere →
   ~640 real PASSes, the "bless" half the tool lacked.
2. Ingest CPP_COMPILE_DEFECTS.md + the 14 compile failures as ground-truth INVALIDs (free regression set).
3. Keep the honesty floor: ran-clean ≠ PASS; only an oracle PASSes. (Confirmed by the Ver-theater incident.)
4. Use the 1,276 verified docs as the expected-behavior source for per-pattern oracles / answer-key expansion.
