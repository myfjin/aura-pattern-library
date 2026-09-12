# How to Build the Tool — deep analysis of the manual audit (Fable, 2026-07-20)
*Illia's teaching: I audited calibration by improvising fresh attacks instead of replaying the
error classes we already found. That gap IS the tool's architecture. This doc extracts it.*

## The core realization
A human auditor (me, yesterday and this morning) works in ARTISAN mode: read each pattern fresh,
re-invent attacks from scratch, use intuition. A TOOL works in LIBRARY mode: hold a fixed set of
attack RECIPES — one per discovered failure class — and fire EVERY recipe at EVERY pattern,
mechanically, then judge the outputs. **The tool is the error catalog turned executable.**

Proof I was in the wrong mode: attacking calibration_curve.cpp I re-derived "mismatch", "empty",
"garbage labels" by hand — those are just E007, E009, E-B5 from yesterday. I should have RUN the
catalog as a checklist. I even MISSED recipes I'd already discovered (never fired NaN/E008 or
None/E006 at calibration). A tool never forgets a recipe. That is its whole advantage over me.

## LAYER 1 — the ATTACK RECIPE LIBRARY (mechanical; derived from E001–E011)
Each recipe = a transformation applied to a pattern's declared inputs. The tool fires all of them.

| Recipe | From | The probe (input transform) | Fires on any pattern with… |
|---|---|---|---|
| R1 domain-under | E001,E003 | push a param below its low bound (prob<0, alpha≤0, rate≤0) | a bounded numeric param |
| R2 domain-over | E003 | push above high bound (prob>1, u≥1) | a bounded numeric param |
| R3 degenerate-equal | E002 | make a difference zero (p1==p2, all-same) | a param measuring a gap/effect |
| R4 cross-param-impossible | E004 | violate a relationship (successes>trials) | ≥2 params with a joint constraint |
| R5 no-data | E005,E008-empty | zero count / empty list / trials=0 | any count or collection input |
| R6 wrong-type | E006 | None, str-for-number, bool-for-int | any typed input |
| R7 shape-mismatch | E007 | unequal-length parallel arrays (both directions) | ≥2 arrays that must align |
| R8 nan-inf-poison | E008 | inject float('nan')/inf into a data array | any float collection |
| R9 degenerate-param | E009 | k=0, window=0, num_breaks=0 | any size/count tuning param |
| R10 numeric-oracle | E010 | brute-compute the claimed quantity, compare | any closed-form math claim |
| R11 invariant-stress | E011 | push a claimed invariant to its edge (sum≈1 at large α) | any docstring "guarantees X" |
| R12 mutation-probe | log_rank find | corrupt a constant/branch, see if any assert notices | any pattern (tests the TEST) |
| R13 state-sequence | ttl/token find | call twice; idle then burst; rewind clock | any stateful/temporal pattern |

13 recipes cover every finding of the 14-pattern audit. New patterns rarely need new recipes now
(saturation) — they need the existing 13 fired systematically. THAT is what I failed to do.

## LAYER 2 — the DETECTION ORACLE (the hard half: judging each recipe's OUTPUT)
Firing the recipe is trivial. Knowing whether the result is a KILL is the real problem — and it's
exactly where yesterday's verdict-types become machine rules:

| Output signal | Verdict | Mechanism (from spec) |
|---|---|---|
| raised a NAMED error citing the bad param | ✅ CONTRACT (best) | parse the error text |
| raised a cryptic/foreign error (stdlib deep) | ✅ but flag ACCIDENTAL | error raised, message doesn't name input |
| **no error + output ≈ clean-run output** | ❌ KILL (fake-robust) | 6E-P2 noise-identity: feed garbage, diff output |
| no error + output is nan/inf | ⚠ visible poison | 6E-P2 finiteness check |
| no error + confident plausible number | ❌ KILL (silent-wrong) | **hardest** — needs R10 oracle or R11 invariant |
| numeric-oracle mismatch | ❌ WRONG-MATH | R10: brute vs code |
| invariant broke on valid input | ⚠/❌ | R11: check the guarantee |
| no assert reacted to mutation | ⚠ coverage-gap | R12 |

The 3rd and 5th rows are the whole game: **a confident plausible number with no error is the kill
that fooled every machine gate.** It's caught two ways only — noise-identity (does garbage change
the output?) and the oracle/invariant (is the number actually RIGHT?). Everything else is cheap.

## What this means for the BUILD (v1 concretely)
1. Encode the 13 recipes as pure functions: `recipe(manifest_entry) -> list[fixture]`.
2. Encode the oracle as the 8-row signal table above → a verdict per (pattern, recipe).
3. Run all 13 × every pattern in the manifest → evidence cards.
4. EXAM: the tool's verdicts must match Illia's 14 hand-verdicts. Where they differ → calibration
   ticket (Opus's protocol). Yesterday's 14 patterns are the answer key.
5. calibration_curve.cpp is now item 15 of the answer key — and note: firing R7+R8+R10 on it
   mechanically would have found everything I found by hand, plus the E008 NaN I forgot.

## The honest gap (what the library does NOT yet catch)
- **wrong-math without a closed form** (R10 needs a computable reference; iterative/random patterns
  have none) → falls to R11 invariant or stays human-only (Illia's Part C).
- **semantic docstring-lies** (ttl_cache size() "counts non-expired" but counts all) → R11-ish but
  needs the claim parsed; largely human until v3 claim-extraction.
- **cross-pattern disagreement** (two patterns, same textbook, different answer) → 4Q-P5, v2.
These 3 are exactly why Illia's gate never fully retires — the tool carries the mechanical 80%,
the human keeps the semantic 20%. That division, measured, is the honest university claim.



## THIRD BOUNDARY (Illia's spinlock probe, 2026-07-20): the UN-runnable
The mechanical/semantic split had two rows. Concurrency memory-ordering is a THIRD:
- Mechanical ~80%: the 13 recipes catch it by running.
- Semantic ~20%: docstring-lies, wrong-math-no-oracle — human/Part-C.
- **UN-RUNNABLE (new): memory-ordering correctness.** PROVEN: atomic_spinlock with orderings
  weakened Acquire/Release->Relaxed STILL passes 8000/8000 on Apple Silicon (hardware > model).
  A wrong lock is indistinguishable from a correct one BY RUNNING. Neither recipes nor eyeballs
  catch it — only a model-checker (loom) exploring interleavings does.
- **Tool consequence:** the tool must DETECT concurrency primitives (Atomic*, compare_exchange,
  thread::spawn) and REFUSE to certify their ordering — route to formal-methods / label
  "ordering unverified by execution". Honest incapacity beats false PASS. A run-based tool that
  greenlights a spinlock is lying by omission.

## One-line summary
The tool = {13 attack recipes} × {8-signal oracle} × {Illia's 14 verdicts as the exam}.
I build it by encoding what Illia's hands already discovered — not by inventing anything new.
