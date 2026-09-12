# 5S Final Vision — Validation Tool Design Review (2026-07-20)

Author: fifth_state  
Source read: `TOOL_ARCHITECTURE_ANALYSIS.md`, `VALIDATION_TOOL_SPEC.md`, `ERROR_CATALOG.md`, `manual_audit_2026-07-19.csv`, `6E_tool_vision_2026-07-19.md`, `6E_round2_2026-07-19.md`, `patterns_manifest.json`.

---

## Chain of thought

### 1. The design is much stronger than round-1

The consolidated spec fixes the three hard problems that broke every previous gate:
- **Three kills → three mechanisms** (abuse recipes + invariant grid + numeric oracle + output plausibility).
- **Disagreement protocol** turns Illia from oracle into a movable ruler tied to mechanism.
- **Four-verdict ladder** makes the tool honest about what it can fix vs what it can only flag.
- **Twin-transfer law** gives a 5× path across languages.
- **Third boundary** (UN-RUNNABLE concurrency) is the first honest statement about what execution *cannot* prove.

That last one is the most important architectural move. A tool that silently greenlights a wrong spinlock is worse than no tool. Admitting the boundary *raises* trust, not lowers it.

### 2. Dead end I almost followed: "the 13 recipes are complete"

Reading the architecture doc, the claim is: "13 recipes cover every finding of the 14-pattern audit. New patterns rarely need new recipes now (saturation)."

I think this is **80% true and dangerous if believed at 100%**. The recipes are complete for the *failure classes already seen*. But the audit also found two meta-signals that are not recipes:
- **R12 mutation-probe** is not a recipe against the pattern — it is a recipe against the *test harness* (corrupt epsilon, still pass = dead branch).
- **E012 validation-theater** is not an input transform — it is a *claim-falsification* verdict subclass of R11.
- **META-LAW** says recipe distribution shifts by language; the same recipe has different power in rust vs python.

So "13 recipes" is the right library, but the **oracle signal table** (8 rows) is where the real intelligence lives. A hostile reviewer will not break us by inventing recipe 14; they will break us by showing that one of the 8 signals misclassifies a plausible output.

### 3. What I think is still invisible

I looked for gaps in four directions: (a) things the tool will wrongly PASS, (b) things it will wrongly KILL, (c) things it cannot run at all, (d) things the disagreement protocol cannot resolve.

**Invisible gap 1 — the "oracle-collision" false negative.**  
Two different wrong formulas can produce the same plausible number. Example: bayes_factor bug gives 1.24 on the planted demo. A numeric oracle that only checks "is BF > 1?" would PASS. The spec’s numeric oracle is better (closed-form vs brute integration), but for patterns *without* a closed form the oracle dies. What replaces it? Currently: R11 invariant-stress. But many iterative/randomized patterns have no simple invariant. The honest fall-through is **FLAG**, not PASS. I don’t think the spec makes this fall-through loud enough.

**Invisible gap 2 — the "attack-succeeded but looks like no-op" false positive.**  
Illia discovered this in stacking_ensemble: setting `X=[]` before generation loops is a legitimate run, not fake-robustness. The tool’s noise-identity check (clean vs garbage output) will compare *different* inputs and may flag a PASS as fake-robust when the attack simply failed to reach the code. We need an **attack-reachability oracle**: did the poisoned value actually flow through the function? Without it, P2 output plausibility will false-KILL.

**Invisible gap 3 — harness defects are pattern verdicts in disguise.**  
The token_bucket_limiter audit found the harness prints NOTHING on success — you cannot tell if the pattern ran. The current tool runs the pattern *through* the harness (or calls `entry_fn`). If the harness swallows success, the tool sees neither PASS nor KILL. We need a **harness honesty gate**: the tool must observe the pattern output directly, or at least confirm the harness reports success/failure unambiguously. A pattern that is correct but untestable is a tool failure, not a pattern failure.

**Invisible gap 4 — the calibration loop has a memory problem.**  
The anti-overfit rule says "no resolution may flip a previously-correct exam verdict." But the exam itself is Illia’s ~50 hand-verdicts. As the tool learns new recipes, it will *retroactively* catch bugs in patterns Illia previously PASSed. The rule as written forbids the tool from correcting Illia. That conflicts with the TOOL-TAUGHT channel. We need a distinction between: (a) flipping an exam verdict because the rule is wrong, and (b) flipping because the rule found a genuinely new bug Illia hadn’t tested. The current protocol conflates them.

**Invisible gap 5 — twin-transfer needs a divergence detector, not just structural diff.**  
gradient_boosting_stumps.cpp DIVERGED from python (it had guards python lacked). Structural diff alone would have wrongly flagged the C++ guard as a difference to investigate. We need a **semantic diff**: same mathematical intent, not same code shape. The spec says "verify not assume" but doesn’t specify how. A simple heuristic: if the twin passes the same abuse recipes as the source, inherit the source verdict; if it survives recipes the source failed, it diverged upward and needs independent audit.

**Invisible gap 6 — the META-LAW is stated but not instrumented.**  
The tool should weight recipes by language. But the spec only says "down-weight type/NaN recipes in rust." How much? What about Go (strong-ish static types but nil-able references)? What about R (weak types, NA semantics)? Without a measured prior per language, the tool will either over-fire in rust or under-fire in R. We need a small calibration matrix (language × recipe class weight) derived from the audit CSV.

**Invisible gap 7 — no mechanism for E011 vs E012 distinction.**  
Both are "claim/code mismatch." E011 = claim true only in undeclared sub-domain (real invariant, over-scoped). E012 = no real validation, proxy costumed as validation. The spec says E012 is caught by R11, but the oracle signal table does not distinguish them. The *verdict authority* differs: E011 might be FLAG (qualify claim) while E012 is INVALID-fix-known (implement validation). The tool needs a **claim-strength oracle**: does the code contain any logic that *could* enforce the claim, or is the claim entirely unimplemented?

### 4. What a hostile university reviewer would actually break

A reviewer will not say "your 13 recipes are incomplete." They will say:

1. **"Your tool greenlit a wrong formula because the numeric oracle had no closed-form reference."**  
   → Fix: explicit no-oracle fall-through to FLAG, not PASS; maintain an `oracle_coverage` field per pattern.

2. **"Your tool called a pattern INVALID because garbage output equaled clean output, but the attack never reached the code."**  
   → Fix: attack-reachability oracle (instrumentation or taint check).

3. **"Your tool reported PASS on a pattern whose harness prints nothing."**  
   → Fix: harness honesty gate, separate from pattern verdict.

4. **"Your tool inherited a python verdict into C++ without checking C++-specific UB."**  
   → Fix: per-language poison probes (UB/out-of-bounds/overflow/NaN-with-ffast-math).

5. **"Your calibration loop can never improve because flipping any exam verdict is forbidden."**  
   → Fix: split exam into "frozen ground-truth set" (Illia’s original 50) and "expansion set" for newly found kills.

6. **"Your tool cannot distinguish an over-scoped claim from an unimplemented guarantee."**  
   → Fix: claim-strength oracle (E011 vs E012).

---

## Proposals

### 1. Add an `oracle_coverage` field to every verdict

**Why:** Gaps 1 and 6. The tool should report not just PASS/KILL but *how* it knows. If the numeric oracle has no reference, if invariant grid has no invariants, if language prior has no calibration — the verdict becomes FLAG (tool admits uncertainty) instead of PASS.

**How:** Each evidence card gets `oracle_coverage: {mechanical: bool, semantic: bool, numeric: bool, un_runnable: bool}`. A PASS requires at least one of mechanical/semantic/numeric to be true. A pattern with all false is FLAG. Concurrency-ordering automatically sets `un_runnable: true` and caps the verdict at FLAG.

**Cost:** Low — metadata-only, no new mechanism.

### 2. Attack-reachability check for output plausibility

**Why:** Gap 2. Prevents P2 from false-KILLing legitimate no-op attacks.

**How:** For each abuse recipe, after running, check whether any poisoned value appears in the function’s observable state (return value, raised exception, side-effect logs). If not, mark the fixture `attack_did_not_reach` and exclude it from noise-identity judgment. Use taint-style tracking for simple cases; for complex cases, require the recipe to target a return-visible parameter.

**Cost:** Medium — requires per-recipe reachability rule, but mostly automatable.

### 3. Harness honesty gate

**Why:** Gap 3. The tool must know whether the pattern ran.

**How:** The manifest already has `entry_fn`. The tool should prefer direct `entry_fn` invocation over file-level harness execution. If a harness is required, the tool first runs a calibration fixture with a known outcome and verifies the harness reports it. If the harness is silent or ambiguous, the verdict is `FLAG — harness untrustworthy`, not PASS.

**Cost:** Low — leverages existing manifest entry-point convention.

### 4. Split the exam into frozen + expansion sets

**Why:** Gap 4. Allows the tool to learn without rewriting history.

**How:**
- **Frozen set:** Illia’s original ~50 hand-verdicts. These never flip. They measure regression.
- **Expansion set:** New patterns / new recipes / twin inheritances. These can flip as the tool improves. They measure progress.
- A flip in the frozen set is a tool regression. A flip in the expansion set is a learning event.

**Cost:** Near-zero — renames the existing exam file into two sections.

### 5. Per-language recipe-prior matrix

**Why:** Gap 6. Turns META-LAW from prose into a measured dial.

**How:** Build a small table from the audit CSV:

| lang_family | R1-R2 domain | R6 wrong-type | R8 NaN | R11 claim | weight rule |
|---|---|---|---|---|---|
| python | 1.0 | 1.0 | 1.0 | 1.0 | baseline |
| R | 1.0 | 1.0 | 1.0 (NA) | 1.0 | same baseline, separate NA probe |
| cpp | 0.5 | 0.3 | 0.7 | 1.2 | type-ish compiler, UB probe added |
| go | 0.3 | 0.2 | 0.5 | 1.3 | strong static, nil probe added |
| rust | 0.1 | 0.0 | 0.0 | 1.5 | compiler kills type/NaN; R11 dominates |

The tool multiplies recipe confidence by this prior. The matrix is itself a calibration artifact — versioned and adjusted when audit data grows.

**Cost:** Low to add; medium to validate.

### 6. Claim-strength oracle for E011 vs E012

**Why:** Gap 7. Distinguishes over-scoped real invariant from validation-theater.

**How:** For each claimed guarantee, do two probes:
- **Existence probe:** does the code contain any branch/condition that *could* enforce the claim? (AST search, regex, or simple heuristic.)
- **Falsification probe:** R11 — feed input that violates the claim. If it passes:
  - existence=true → E011 (over-scoped real validation). Verdict: FLAG or INVALID-fix-known (qualify claim).
  - existence=false → E012 (validation-theater). Verdict: INVALID-fix-known (implement validation).

**Cost:** Medium — needs AST/symbolic parsing per language, but only for claims listed in metadata.

### 7. Twin divergence detector

**Why:** Gap 5. Prevents structural-diff false positives and false negatives when twins diverge.

**How:** For each twin pair, run the source’s failing recipes on the twin.
- If twin fails the same way → inherit verdict.
- If twin passes a recipe the source failed → **divergence alert**, do independent full audit.
- If twin fails a new way (e.g., C++ UB) → add language-specific evidence card.

Do not rely on code diff alone.

**Cost:** Low — reuses existing recipes; just adds a comparison pass.

### 8. Concurrency-ordering explicit un-runnable verdict

**Why:** The third boundary must be visible in every verdict.

**How:** Any pattern whose AST contains `Atomic`, `compare_exchange`, `thread::spawn`, `Mutex`, `Arc<Atomic>`, etc. gets a mandatory `ordering: unverified_by_execution` field in its evidence card. The tool may PASS execution-based checks, but it cannot PASS the ordering property. Final verdict is capped at **FLAG** for ordering correctness.

**Cost:** Low — simple static detection + verdict cap.

---

## What I would build first

If Fable is about to start building the validation tool, the order is:

1. **Core 13 recipes + 8-signal oracle** (already speced).
2. **Proposal 8** (concurrency cap) and **Proposal 1** (`oracle_coverage`) — they make the tool honest before it makes it powerful.
3. **Proposal 3** (harness honesty gate) — without this, the exam is unreliable.
4. **Proposal 2** (attack-reachability) — without this, P2 output plausibility will false-KILL.
5. **Proposal 5** (language prior matrix) — turns META-LAW into code.
6. **Proposals 4 + 6 + 7** — governance and semantic depth, ship in v1.5.

The spec is strong. These eight proposals are not new mechanisms — they are *guardrails on the mechanisms already chosen*. The tool’s biggest risk is not missing a recipe; it is silently PASSing when it should say "I cannot tell."

---

*5S · 2026-07-20*  
*Ready for Fable to build.*
