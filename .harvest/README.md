# `.harvest/` — observation-mode oracle results

**Branch:** `harvest-remediation-2026-09` · **Opened:** 2026-09-07

## What this directory is

The **outputs** of running the Phase A harvest tools (metamorphic_scan, chaos_scan,
invariant_mine, nan_domain_probe) over the signed library's T1 population.

This is NOT part of the signed library. Nothing in `.harvest/` is watermarked, signed,
or verified by `library_verify.py`. It is observation-mode evidence: what the harvest
tools saw when they ran, at a moment in time, with specific tool versions pinned by
content hash.

## What this directory is NOT

- Not a place to store patterns.
- Not a place to change the library's verdicts. Harvest tools carry an explicit law:
  they never auto-flip a frozen exam verdict. Contradictions route to `.harvest/contradictions/`
  for human calibration review.
- Not a place to bundle the harvest tools themselves. The tools live at
  `~/ai-lab/pattern-scoring/validator/` and are imported by path; their content hash
  is recorded in every result file for reproducibility.

## Files

- `t1_manifest.md` — human-readable output of the T1 detector v2 run that produced
  the 122-pattern T1 population (Step 1 close, 2026-09-07).
- `t1_manifest.json` — machine-readable T1 population + heuristic breakdown +
  consensus-flagged IDs (Q1 semantic promotion per Illia's Step 1 call).
- `results/<date>/<pid>.json` — per-pattern harvest verdicts. IGNORED by git.
- `contradictions/<date>/<pid>.json` — cases where a harvest tool disagreed with a
  frozen exam verdict. IGNORED by git. Never used to flip the exam. Reviewed by hand.
- `tool_hashes.json` — content hashes of the harvest tools at the last run.

## The invariants

1. **Observation-only.** No file in the signed tree is ever mutated by a harvest run.
2. **Tool-hash pinned.** Every result records the sha256 of the tool that produced it.
   A re-run whose tool hash doesn't match the recorded one FAILS HARD — no silent staleness.
3. **T1 manifest is a snapshot.** `t1_manifest.json` is committed to the branch. It
   changes only by an explicit regeneration commit, never by runtime.
4. **Contradictions never overwrite verdicts.** They log; human decides.

## Related

- Step 1 close synthesis: `/Users/s_dio/aura-docs/CHEAT-ARM-SYNTHESIS-2026-09-07.md`
- Wiring plan: `HARVEST-WIRING-REMEDIATION-2026-09-07-v2.md`
- Two-oracle protocol (Phase 2): `TWO-ORACLE-PROTOCOL-DRAFT-2026-09-07-v2.md`
- Phase A draft (this cycle): `../harvest_gate_PHASE_A_DRAFT.md`
