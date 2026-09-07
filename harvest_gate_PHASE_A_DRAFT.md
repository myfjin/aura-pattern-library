# Phase A wiring — DRAFT for Illia review

**Branch:** `harvest-remediation-2026-09` · **Base:** master@`f592df0` · **Date:** 2026-09-07

## ⚠️ First finding — the wiring plan needs re-framing

Draft 1 v2 said *"wire Phase A harvest tools into `ingest.py`"*. Reading the tools revealed:

- **`ingest.py` is intake-time only** — it reads `~/ai-lab/patterns_cpp/final_approved.jsonl`, runs gate B4 (approved + not-quarantined + sha256 match + compiles+runs), then copies twin + watermarks + signs. It's specific to the C++ ingestion pipeline for data-science twins (there are also `ingest_go.py`, `ingest_cpp_native.py`, `ingest_go_native.py`).
- **The harvest tools are OBSERVATION-ONLY oracles over the signed library.** Every one carries an explicit law: *"MUST NOT auto-flip a frozen exam verdict. Contradictions → calibration, not the ruler."* They read signed-oracle behavior and emit evidence cards.

**So Phase A is not an ingest-gate change.** It's a `library_harvest.py` runner that invokes the observation-mode tools over signed patterns and reports coverage + contradictions. Ingest.py stays untouched.

## Inventory — validator/ staging tools on .5

| tool | lines | role | Phase | current coverage |
|---|---|---|---|---|
| `metamorphic_scan.py` | 137 | scaling/permutation/duplication invariance | A | 9 patterns (regression/classification/clustering) |
| `chaos_scan.py` | 61649 B (~1500 lines) | fault injection + survival predicate + negative control | A | 3 patterns (atomic_write, WAL, checkpoint_resume) |
| `invariant_mine.py` | 225 | Daikon-style mining, `harvest`/`check` modes, ratify-by-hand | A | pattern-list configurable |
| `nan_domain_probe.py` | 205 | NaN/domain-boundary sweep | A | TBD (unread) |
| `twin_divergence.py` | 232 | parallel reference disagreement | **A → HELD** | needs Draft 2 for trusted reference |
| `full_sweep.py` | 72 | runner orchestrator | A | wraps the above |
| `probes.py` | 1219 | oracle target definitions | A | supplies patterns |
| `executor.py` | 17485 B | subprocess pattern runner | shared | — |
| `compiled_harness.py` | 17714 B | cpp/rust/go compile-run wrapper | shared | — |
| `oracle.py` / `oracle_sizer.py` | 158/146 | oracle load + size heuristics | shared | — |
| `recipes.py` | 216 | R13 state-lie recipes | Phase B | — |
| `xmt_scan.py` | 192 | cross-mutation test scan | Phase B? | unread |
| `polyglot.py` | 73 | multi-lang dispatch | shared | — |
| others (`retrofit_*`, `roundtrip_*`, `sweep.py`, `r_*`) | | Phase B or unused | | |

**Coverage gap up front:** T1 population from Step 1 = **122 patterns**. Harvest tools currently cover ~**12** of them by name. Phase A wiring exposes the gap; it does not close it. Closing means writing per-pattern probes (Phase B).

## Phase A wiring — the actual diff

Not a diff to `ingest.py`. A new file at repo root:

**NEW: `~/aura-pattern-library/harvest_gate.py`** — a runner that:

1. Loads T1 population from `.harvest/t1_manifest.json` (produced by v2 T1 detector; committed to branch).
2. For each T1 pattern, invokes the applicable Phase A tools:
   - `metamorphic_scan.py check <pid>` if pid is in metamorphic_scan.PATTERNS
   - `chaos_scan.py check <pid>` if pid is in chaos_scan targets
   - `invariant_mine.py check <pid>` if a ratified invariant file exists
   - `nan_domain_probe.py <pid>` if applicable
3. Writes results to `.harvest/results/<date>/<pid>.json` — verdict + evidence card + timestamps.
4. Content-hash-cached: if the pattern's sha256 matches last run's hash AND all tool sha256s match, skip and reuse cached result. (v2 draft requirement — cache invalidates on ANY tool change.)
5. **Never mutates the signed tree. Never touches `library_verify.py`. Never edits `AUDIT-RESULTS.jsonl`.**
6. Reports coverage gap at end: `T1 total: N · covered by ≥1 Phase A tool: M · gap: N-M`.

**Config:** tool paths pinned in `harvest_gate.py` to `~/ai-lab/pattern-scoring/validator/`. Not copied into the library — imported by path. Keeps the staging separation Illia set up (the tools are a WIP, the library is signed).

**Sub-move — bring T1 population INTO the branch:**
- Copy `t1_detect_v2_output.txt` → `.harvest/t1_manifest.md` in the branch (evidence).
- Add `.harvest/t1_manifest.json` — machine-readable list of 122 pattern IDs + Q1 consensus-flag tags.
- Add `.harvest/README.md` — one-page explaining what harvest is vs library_verify.
- Add `.gitignore` entry for `.harvest/results/` (per-run outputs, not part of the signed library).

## Kill criterion for Phase A landing

`python3 harvest_gate.py --dry-run` prints:
```
T1 population: 122 patterns
Applicable Phase A tools: metamorphic_scan(9) chaos_scan(3) invariant_mine(0 ratified) nan_domain_probe(TBD)
Would run: X pattern-tool pairs
Cache hits: 0 (first run)
```
Exit 0. No files written to signed tree. Coverage gap surfaced.

Then `--run` mode: writes `.harvest/results/` only, exit 0, per-pattern verdicts printed.

## What is EXPLICITLY OUT of Phase A

- Twin_divergence — held for Draft 2 (needs trusted reference).
- Any Phase B recipe build (resource_leak, concurrency, complexity, environment, side-effect).
- Any change to `ingest.py`, `library_verify.py`, `library_audit.py`, or `library_audit_verify.py`.
- Any per-pattern probe authoring — this cycle wires the runner; probe authoring is subsequent work.
- Any auto-flipping of frozen exam verdicts. Contradictions log to `.harvest/contradictions/` for calibration review.

## Two decisions before I write `harvest_gate.py`

**D1 — tool location.** Import from `~/ai-lab/pattern-scoring/validator/` (staging separation) OR copy into `aura-pattern-library/harvest/tools/` (vendored, versioned with library)?
- **My rec:** IMPORT from staging. Keeps Illia's tool separation, matches the observation-only stance, lets the tools evolve without a library commit.
- **Cost:** the library repo can't be run standalone; anyone cloning it needs the staging repo too. Acceptable at this stage.

**D2 — T1 manifest format.** Static JSON committed to branch, or regenerated on every `harvest_gate.py` run by calling `t1_detect_v2.py`?
- **My rec:** STATIC JSON committed. T1 population is a snapshot decision (Step 1 close). Re-running the detector on every harvest run couples them and hides the T1 decision inside runtime output.
- **Cost:** T1 stays frozen until someone regenerates the manifest. Explicit is a feature here.

## What lands in the first commit on `harvest-remediation-2026-09` (if you approve)

```
new file:    .harvest/README.md
new file:    .harvest/t1_manifest.md        (from t1_detect_v2_output.txt)
new file:    .harvest/t1_manifest.json      (machine-readable, 122 IDs)
new file:    .gitignore                     (adds .harvest/results/ if .gitignore exists; new file otherwise)
new file:    harvest_gate.py                (dry-run capable, no --run yet)
```

Zero changes to signed tree, `ingest.py`, `library_verify.py`, `library_audit.py`. First commit is scaffolding + read-only runner.

## Waiting on

Your D1 + D2 calls, and any pushback on the "not-a-diff-to-ingest.py" reframing. If the reframing is wrong, tell me — I read what I read but I might be missing the intent Draft 1 v2 encoded.
