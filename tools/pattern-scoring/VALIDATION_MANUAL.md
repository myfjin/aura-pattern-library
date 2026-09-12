# How to Validate the Pattern Library — Operator's Manual

**For:** Illia · **Scope:** the whole AURA Pattern Library (934 patterns / 1,399 files, 5 languages)
**Mechanism version:** frozen ruler v1.0.0 · **Status:** ALL 5 LANGUAGES DONE (1,399 files, 1,391 VERIFIED). Python 676 · Rust 200 · C++ 370 · R 60 · Go 93 — each testbed-gated + deterministic. See `UNIFIED_VALIDATION_REPORT.md`.

This is the manual you asked for: *what* to test, *how*, *when*, *every error you can face*, and *the exact output that lets you call a pattern VALID*. It is grounded in the mechanism as it actually runs today — not in intention.

---

## 0. What "valid" MEANS (the definition that does not move)

A pattern is **VALID** when it is **correct-and-holds**, not when it is "best." Concretely, valid = all four:

1. **It runs** reproducibly on representative input (no crash, no import rot).
2. **It has a real, testable shape** — a reusable function or class, not a bare script.
3. **Its self-checks are honest** — real assertions, not `assert True` theatre.
4. **It survives abuse** — fed deliberately wrong input, it either errors cleanly or handles it correctly; it never produces a silently-wrong answer.

What valid does **NOT** mean: elegant, optimal, or fastest. Those are personal/taste judgments — the ruler refuses to measure them, because that is exactly where the number used to swing. Valid is the *social* floor: it holds, independent of how anyone feels about it.

**The ruler never says a flat 0 or 100.** Every verdict carries its evidence and its reason. A verdict without evidence is not trusted — not from a script, not from a model, not from a vibe.

---

## 1. WHAT you are testing (the corpus)

The canonical, signed library lives on **.5** at `~/aura-pattern-library/`:

| Language | Files | Where |
|---|---|---|
| Python — programming | 99 | `python/programming/` |
| Python — data-science | 377 | `python/data-science/` |
| Python — system-administration | 200 | `python/system-administration/` |
| R | 60 | `r/` |
| C++ | 370 | `cpp/data-science/` |
| Rust | 200 | `rust/` |
| Go | 93 | `go/` |
| **Total files** | **1,399** | (= 934 unique patterns; many have cross-language twins) |

**All five languages are validated** — the staircase completed 2026-07-16, one language at a time, each under its own native oracle in the same frozen frame: Python (`utility_score.py` + `evidence_runner.py`, 676 files), Rust (`rust_oracle.py`, rustc + forbid-unsafe, 200), C++ (`cpp_oracle.py`, g++ AND clang++ pedantic, 370), R (`r_oracle.py`, Rscript + stopifnot, 60), Go (`go_oracle.py`, go run + exit code, 93). Each oracle passed its own planted testbed before it touched canonical patterns. Re-run any of them: `python3 <lang>_oracle.py --dir ~/aura-pattern-library/<lang>` (Python: `python3 utility_score.py --dir … --abuse`). Failure vocabulary per oracle: see `ERROR_TAXONOMY.md` §4.

---

## 2. HOW — two layers, in order

```
pattern file
   │
   ├─ LAYER 1: THE MACHINE FLOOR (deterministic, no opinions)
   │     SENSE      → real pattern, or trivial/script-shaped?
   │     DESCRIPTION→ does it declare what it does + its input domain?
   │     VALIDITY   → compiles · runs · meets its own claim · survives fuzz
   │     EVIDENCE   → success-run AND abuse-run both checked
   │        └─→ produces a STATUS + an EVIDENCE CARD per pattern
   │
   └─ LAYER 2: YOUR EYES (only where the machine hands off)
         4-question gate on anything flagged
         ≤5% deep audit of the VERIFIED set (spot-check, not all 900)
```

The machine does the 95%. You do the irreducible 5% — the descriptions it can't comprehend and the silent-outputs it won't guess on. **You are the auditor, not the assembly line.**

---

## 3. The commands (copy-paste)

Everything runs from `~/ai-lab/pattern-scoring/` on **.5**.

```bash
cd ~/ai-lab/pattern-scoring

# (A) Validate ONE pattern, full evidence card + abuse fuzz:
python3 utility_score.py ~/aura-pattern-library/python/programming/lru_cache.py --abuse --json

# (B) Validate the WHOLE Python library (Phase 1 — ~1.2 min):
python3 run_phase1.py
#   → writes output/python_canonical_2026-07-16.json  (full form)
#          output/python_canonical_2026-07-16.csv     (summary you can open in a sheet)
#   → prints the verdict distribution + every non-VERIFIED pattern with its reason

# (C) Manual description gate on one pattern (your 4 questions, guided):
python3 utility_score.py <pattern.py> --description-review

# (D) Prove the ruler doesn't swing (run B twice, compare):
python3 run_phase1.py && cp output/python_canonical_2026-07-16.csv /tmp/a.csv
python3 run_phase1.py && diff /tmp/a.csv output/python_canonical_2026-07-16.csv && echo "IDENTICAL — no swing"
```

---

## 4. Reading the output — what VALID actually looks like

Every pattern returns a JSON record. The fields that decide validity:

| Field | VALID looks like | Meaning |
|---|---|---|
| `status` | `"VERIFIED"` | the verdict — the only status that means "keep, proven" |
| `sense_pass` | `true` | it's a real, shaped pattern (not trivial/script) |
| `description_pass` | `true` | it declares what it does + its input domain |
| `validity_pass` | `true` | compiles, runs, meets its claim, survives fuzz |
| `failing_column` | `null` | nothing failed |
| `evidence_card.abuse` | `errored:true` OR correct output | bad input was rejected or correctly handled — never silently wrong |
| `U` | a number **or** `null` | ranking score; `null` is fine — it means "utility not measured," NOT "invalid" |

**A pattern is VALID when `status == "VERIFIED"`.** That single field already bundles the four checks above. `U = null` does not block valid — utility is a *ranking* number, separate from correctness. Missing utility evidence is honestly reported as `null`, never faked to 0.5.

---

## 5. Every verdict you can get (the 6 statuses) + what to DO

| status | what it means | your action |
|---|---|---|
| **VERIFIED** | correct and holds; evidence clean | keep. (Spot-audit ≤5% of these.) |
| **senseless** | trivial wrapper / script-shaped / no real logic — nothing to catalogue | read it once. If it's genuinely a stdlib one-liner → drop. If it has real logic but no function/class → **restructure** (wrap it), then re-run. |
| **invalid** | a hard gate failed — doesn't compile/run/meet-claim, OR fuzz caught it silently wrong | read the `failing_column`. If a real bug → fix or drop. This is the ruler catching a fake-robust pattern. |
| **needs_validity** | couldn't be positively proven (e.g. no runnable entry-point found) | **not rejected, not proven.** Give it a runnable example/entry-point, re-run. If still unprovable → your call. |
| **quarantine_no_description** | no description at all — no contract to check | one rewrite attempt to add a description → re-run. If still none → gone. |
| **quarantine_undefined_domain** | has a description but declares no valid-input domain → can't be fuzzed | add an explicit `Valid input:` / `Args:` line → re-run. |

**"gone" always means ARCHIVED, never hard-deleted.** A tired-day verdict is reversible.

---

## 6. Every error (`failing_column`) you can face + meaning + action

**Structural**
- `read_error` — file couldn't be read → check the file exists / encoding.
- `syntax_error` / `parse_error` — file won't parse → real syntax bug, fix or drop.

**Sense**
- `"No top-level function or class found."` — script-shaped, no reusable entry-point → wrap the logic in a function, re-run. *(This is 7 of the 8 Phase-1 flags.)*
- `"Trivial wrapper..."` — the body is just a call to a stdlib function → probably drop.
- `hollow_assert: all assertions are tautologies` — self-tests are `assert True`/`1==1` → add a real check, re-run.

**Fuzz / abuse**
- `abuse_silent_output` — bad input produced output **without erroring**. ⚠️ **This is the one the machine WON'T decide** — see §9. Your verdict.
- `abuse_wrong` — bad input gave a clearly wrong result → real bug, fix or drop.
- `abuse_unclear` — bad input gave no output and no error → investigate.

**Integrity**
- `evidence_runner_error` — the runner itself failed to execute the pattern → environment/harness issue, not the pattern's fault; re-run or check deps.
- `validity_report_missing` — appears as a *flag* on VERIFIED patterns; benign — it just means the optional external validity report wasn't supplied. Does not block valid.

---

## 7. WHEN to re-run (the frozen-ruler discipline)

- **After ANY mutation to a pattern** — a rename, a fix, a conversion, a signature change — re-run the gate. A pass only stays a pass until the code or the standard changes.
- **The standard is FROZEN + VERSIONED (v1.0.0).** "Valid under v1" is a permanent, re-checkable fact. Re-running never changes a verdict unless *you* deliberately bump the standard. That is what kills the overnight swing: the ruler doesn't move, so the number doesn't either.
- **Same pattern → same verdict, every run, every machine.** Proven: Phase 1 ran twice byte-identical, and .5 matches .8 exactly.

---

## 8. Your 4-question human gate (for flagged patterns)

Run these on anything the machine hands you (flagged / needs_validity / quarantine). Answer fast:

| # | Question | if "no" |
|---|---|---|
| ① | **What** does it do — do you understand the purpose? | gone |
| ② | **When** to use it — do you know the right situation? | gone |
| ③ | **What** does it guarantee — do you know the output/promise? | gone |
| ④ | **Plain words** — jargon-free enough to be useful? | gone |

Same four questions on a good day and a bad day → the verdict doesn't depend on your mood.

---

## 9. The one honest boundary — `abuse_silent_output`

This is the deliberate hand-off, and the reason your ≤5% pass exists.

The fuzzer confirms a pattern accepted **bad input without erroring**. A machine cannot always tell whether that no-error output is *correct-by-design* (the pattern legitimately handles the edge) or *silently wrong* (the fake-robust disease). So the mechanism **flags it and refuses to guess.** You open it, read what it did with the bad input, and decide. The honesty is the whole point: the ruler tells you what it proved, what it rejected and why, and precisely what still needs your eyes.

---

## 10. What makes YOU stamp a pattern VALID — the checklist

A pattern earns the VALID stamp when, together:

- [ ] `status == "VERIFIED"` from the frozen mechanism, **and**
- [ ] you (on a ≤5% sample of VERIFIED) confirmed the code actually does what its description claims — you can point at the lines, in seconds, **and**
- [ ] any `abuse_silent_output` it had was resolved by your eyes as correct-by-design, **and**
- [ ] it passed the 4 questions (understandable, jargon-free, known use, known guarantee).

That is the full chain: **machine proves the floor with evidence → you audit a sample → the stamp is earned, not claimed.**

---

### Phase 1 result (Python, 2026-07-16), as an example of reading this manual

676 patterns → **668 VERIFIED · 7 senseless · 1 needs_validity.** The 7 senseless all carry `"No top-level function or class found"` (script-shaped, §6) — your call: restructure or drop. The library's own run-gate had passed all 676; this mechanism is stricter (it demands a testable shape), so it surfaced 8 the gate missed. That disagreement is the mechanism working, and those 8 are exactly your audit list.
