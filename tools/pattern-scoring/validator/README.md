# AURA Pattern Health-Check & Triage Tool — v1
Built 2026-07-20 from the manual audit. Encodes what Illia's hands discovered; invents nothing.

## What it is
HEALTH-CHECKS all 5 languages (compile+run each self-test) and TRIAGES the python data-science
sphere with generic attack recipes. Definitive verdicts (PASS/INVALID) come from hand-probes with
oracles; the generic path can only FLAG/SKIP (no oracle -> cannot PASS). This is triage-for-review,
NOT full verification. It reproduces Illia's hand-verdicts where a hand-probe exists. The bar: reproduce every kill he
found, false-alarm on none he passed.

## Architecture (spec v0.6)
- `recipes.py` — the 13 attack recipes (E001-E012) + per-language prior matrix (META-LAW).
- `oracle.py` — the 8-signal detection oracle + 5S's honesty guardrails:
  oracle_coverage (a PASS needs a positive oracle, else FLAG), attack-reachability
  (no false-KILL on no-op attacks), harness-honesty gate, concurrency verdict-cap.
- `probes.py` — executable adapters: import a pattern, run recipe fixtures against real code.
- `exam.json` — Illia's answer key. FROZEN set (never flips = regression detector) +
  EXPANSION set (may flip as tool learns = 5S proposal 4).
- `validate.py` — runner + exam grader.

## Verdict ladder (Illia)
PASS | INVALID·fix-known | INVALID·fix-unknown | FLAG. The tool auto-marks INVALID on its own
authority when evidence is conclusive; FLAGs when it cannot tell; never emits a fix it can't back.

## Run
```
cd validator && python3 validate.py
```

## Status (honest)
- v1 wires executable probes for 4 audited python patterns → **reproduces Illia's verdict 4/4**,
  including the bayes_factor WRONG-MATH kill (numeric oracle) that fooled every machine gate.
- 20 exam patterns are SKIP (no probe yet) — the tool says so rather than guessing.
- **v1.5:** generic manifest-driven execution (patterns_manifest.json) so all 24 run without
  hand-wired probes; then compiled-language probes (cpp UB, rust behavioral-twin-diff).

## Three boundaries the tool knows it cannot cross
- mechanical ~80% (recipes catch by running)
- semantic ~20% (docstring-lies, wrong-math-no-oracle → human Part C)
- UN-RUNNABLE: concurrency memory-ordering → capped at FLAG, routed to a model-checker.
