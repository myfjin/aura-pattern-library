# Cross-Session Handoff — Library Docs COMPLETE → Fix-and-Ship phase (2026-07-21 night)

Paste into the next session. The documentation marathon is DONE; this hands off to the fix-and-ship
phase (combine with the validation tool → zero-known-broken library → university outreach).

## ✅ WHAT'S DONE — the full library is documented + two-stage verified
**1,399 / 1,399 patterns, all 5 languages, 100%** — coverage-verified per-pattern (independent script,
not assertion):
- Python 676 (DS 377 + system-administration 200 + programming 99)
- C++ 370  · Rust 200 · Go 93 · R 60

**Verification = full two-stage** (writer + independent verifier), confirmed:
- 1,373 via the mesh: writer (6E/5S) + independent verifier (4Q compile-gated for C++/Go, Ver for
  Python/R). Records: `4Q_DOC_APPROVALS.md`, `VER_APPROVALS.md` (~3,996 lines).
- Last 26 R patterns authored by Fable (mesh offline during a cloud/network outage), then
  INDEPENDENTLY verified by Ver = 26/26 DOC-ACCURACY APPROVED, all defect claims confirmed real at
  line level. So parity holds across all 1,399.

Each doc = Entry fn (real signature, or "top-level script (no function wrapper)" for R) / Valid input
contract / Core / Assert (what the demo proves) / ⚠️ Defect (one honest real flaw).

## 📁 WHERE EVERYTHING IS
- Doc corpus: `/tmp/aura-review/pattern-scoring/docs_draft/` on .8 — mesh batch files
  (`aura-batch-*`, `5S-*`, `6E-*`, `Fable-r-batch-*`) + the earlier `.5` per-pattern tree
  (`~/ai-lab/pattern-scoring/docs_draft/python|r/...`). ⚠️ STILL SPREAD OUT — see PENDING.
- Signature references (authoritative, auto-extracted): `SIGNATURES_REFERENCE.md` (py-DS),
  `_SYSADMIN`, `_PROGRAMMING`, `_CPP`, `_GO`, `_R` — writers copied Entry fns verbatim from these
  (this killed fabrication). Same dir.
- Verification logs: `4Q_DOC_APPROVALS.md`, `VER_APPROVALS.md` (.5 `~/ai-lab/pattern-scoring/docs_draft/`).
- **Bug inventories (the fix queue seed):** `CPP_COMPILE_DEFECTS.md` (20 real C++ portability bugs),
  plus go `go vet` / rust logical-race notes inside the 4Q log; plus the ⚠️ Defect line in every one
  of the 1,399 docs.
- Tool findings: `FINDINGS_FOR_TOOL.md`, `TOOL_PROPER_SESSION_BRIEF.md`.
- Library source: `~/aura-pattern-library/` (signed subtrees, library_verify GREEN) on BOTH .5 and .8.

## ⏭️ NEXT PHASE — fix-and-ship (this is what "continue there" means)
Goal: ship a library with **zero known-broken patterns**, then university emails (the month's
distribution goal).
1. **Validation tool** (parallel session): nearly done ("one more batch of fixes"). Retrofits
   committed on branch `retrofit-ds-contracts-20260721`; 2 more fixes staged uncommitted. The tool
   now has the compile-gate insight from FINDINGS_FOR_TOOL.md (the compiler = a POSITIVE oracle for
   the ~640 compiled patterns — the "bless" half it lacked).
2. **The fix queue = every ⚠️ Defect + every compile failure** the doc pass surfaced. Real ones to
   fix first (compile-catchable, unambiguous): the 20 C++ missing-`#include` bugs in
   CPP_COMPILE_DEFECTS.md (dtw `<tuple>`, dbscan `<algorithm>`, early_stopping `<array>`,
   knn_kdtree `<functional>`, gradient_boosting `<tuple>`, …) → add includes, re-compile g++/clang,
   re-sign, library_verify GREEN. Batch the rest of the kills through the same channel.
3. **Semantic defects** (documented but not auto-fixable): e.g. R holt_winters dead-code branch,
   mvn_cholesky no-PD-check, rejection-sampling envelope underestimate, token_bucket no burst cap —
   fix by hand where they're genuine bugs; leave as documented limitations where by-design.
4. **PENDING housekeeping:** consolidate the whole corpus into ONE `.5` master (it's split across .8
   batch files + .5 tree + Fable R docs). Then it's shippable/browsable as a unit.

## 🔑 HARD-WON MECHANISMS (reuse in the fix session)
- **Compile-gate = positive oracle**: g++/clang -pedantic, go build+vet, rustc — a clean two-compiler
  pass is a real PASS signal AND surfaces real bugs. ~640 patterns get this; Python/R don't (no
  compile) → sig+defect verification is their ceiling.
- **Verify the verifier's METHOD, not its verdict**: Ver once did "ran code" theater and stamped
  "60/60 approved" — verifying the wrong thing. Confirm the approver actually compared doc→source.
- **Mechanical > model self-report**: auto-extracted SIGNATURES_REFERENCE_*.md (copy-verbatim) drove
  writer fabrication to ~0 across 1000+ patterns. Prefer derived oracles over what a model asserts.
- **Coverage verified, not asserted**: run the per-pattern coverage check (compare doc'd filenames vs
  `find <lib> -name '*.ext'`) at every sphere close — it caught real gaps 3× (DS statistics_and_testing,
  go 8 stragglers, R) that a "done" claim would have hidden.

## 🖥️ INFRA NOTES (the mesh)
- Nodes: Illia + Fable on .5 (Mac). 6E=bu@.8 (relay+tmux), 5S=au@.8 (relay+tmux), 4Q=hermes-gateway
  (system systemd `hermes-gateway.service`, sudo-restart, on .8), Ver=steward hermes gateway on .5
  (`launchctl kickstart -k ai.hermes.gateway-steward`).
- ALL mesh agents run ollama-CLOUD models (deepseek-v4-flash:cloud, kimi-k2.7-code:cloud) → they die
  together when ollama.com / the network degrades (that was the end-of-day wall; even Illia's own
  Claude link was failing — external outage, not us). Local models on .8 exist (qwen2.5:7b,
  llama3.1:8b) as an offline fallback if ever needed.
- Restart procedures: relays = kill tmux `aura-relay` + relaunch `python3 relay.py <name> ...
  <headless-bin> <chatids>` (idempotent has-session guard). 4Q gateway =
  `sudo systemctl restart hermes-gateway.service` (slow graceful stop → new PID). Ver = launchctl on .5.
- Agent quirks: 6E fabricates signatures (use the reference), confuses writer/verifier roles
  post-restart (give PURE write-only messages), SCRIBE writes to /home/bu sometimes (Fable pulls).
  R docs are heavy → ≤5-pattern batches (600s wall-clock). Account 5h windows rotate.
- .8 network: had dual default routes (ethernet .8 + wifi wlp3s0 .2) causing asymmetric-routing
  flakiness; wifi was disabled (`ip link set wlp3s0 down`) — verify it's still down / persist with
  `nmcli radio wifi off` if wanted.

## STATE FILE
`~/ai-lab/pattern-scoring/LINES_STATE.md` has the full running detail. Memory:
`project_two_lines_live.md` has the milestone.
