# fourth!quarter validation-tool vision — 2026-07-19

## Chain of thought

What Fable described is already strong: an abuse fuzzer, a numeric oracle for closed-form math, combined-fault injection, and calibration against Illia's hand-verdicts. I read the ABUSE_CANDIDATES.md list (15 Python functions chosen for manual attack), the 6E additions (style outliers, unverified compile repairs, unverified determinism fix, padded descriptions, missing cross-file terminology, legacy brief cpp descriptions), and the 5S/6E second-pass reviews that found 230/230 MATCHES but only at description-vs-code fidelity. The three kills Illia found by hand are the real signal: they were invisible to every machine gate. So the question is not "what else can we check?" but "what failure classes are still invisible to the current spec, and how would a hostile reviewer at a university exploit them?"

First dead end: I thought about adding more input categories (unicode, very large structures, recursive types, etc.). That is just expanding the abuse fuzzer. It is useful but not a new *class* of detection. The real invisible class is **the test itself being gamed by the code under test** — the pattern's self-test is a tiny oracle that may pass for the wrong reason, as in `bayes_factor_normal_means` (planted test passed at 1.24>1 by luck) and `bayesian_ab_beta` (impossible data → confident PASS). A fuzzer alone would only flag silent acceptance of bad inputs; it would not notice that the *good* inputs in the self-test produce a misleading PASS.

Second dead end: I considered suggesting formal verification or symbolic execution. That is overkill for a 1,399-file polyglot library and would require language-specific engines we do not have. Discard.

Third thought: the current tool tests *the implementation*. It also needs to test *the oracle* — the assertions and evidence cards that claim correctness. Illia's kills were all cases where the code ran, the asserts ran, and the asserts declared victory on evidence that did not actually prove the name. So one new class is **oracle weakness detection**: given the description's claimed guarantee, can we generate a case where the code's own assertion would pass even if the implementation were wrong? This is different from a numeric oracle; it is structural analysis of the self-tests.

Fourth thought: combined-fault injection is good for compositionality, but it should be paired with **semantic inversion**: for every function that is supposed to reject an input, generate a sibling function call with *valid* input that the broken implementation would also reject (or conversely). This catches sign-flipped comparisons, reversed inequalities, and off-by-one guards. `bayes_factor_normal_means` had a sign-flipped formula; a guard that is supposed to reject negative prior variance but does not is one side, but a guard that rejects positive variance because the comparison is backwards is the other side. We currently only test the reject side.

Fifth thought: cross-pattern consistency. 6E already flagged terminology, but the deeper class is **cross-pattern mathematical coherence**. Many patterns share laws: UCB bandit and Thompson sampling bandit should agree on the same fixture (best arm is pulled most in expectation). Synthetic control and difference-in-differences should not contradict on the same synthetic data. If we build a small shared fixture bank and run sibling patterns against it, contradictions become visible. A hostile reviewer loves to point out that Pattern A and Pattern B disagree on the same textbook example.

Sixth thought: description-driven adversarial generation. The tool should read the description's "what it guarantees" and try to violate it *without* touching bad inputs. For example, if the description says "returns the k-armed bandit arm with the highest empirical reward", we should generate data where arm A is clearly best but a subtle bug (e.g., uninitialized counter) makes arm B look best, and then check that the function still returns A. This is **counterfactual guarantee testing**: the implementation must satisfy the guarantee in a world where the guarantee is non-trivial.

Seventh thought: statistical power and false-pass risk. Illia's kill on `bayesian_ab_beta` is impossible data yielding confident PASS. We should add **plausibility-aware sampling**: before running a test, reject synthetic fixtures that are physically or logically impossible for the claimed model. This is a pre-oracle gate. It prevents the "garbage in, oracle out" problem.

Eighth thought: hostile reviewers also attack reproducibility and reporting. The tool should produce **adversarial-style evidence cards**: for every verdict, list not just pass/fail but the exact counter-example, the claimed invariant, why the counter-example violates it, and a confidence. This makes the tool's reasoning inspectable by Illia in Part C. It also surfaces *near-misses* — cases where the function almost failed but the fixture was too easy.

Ninth thought: token budget. Fable explicitly tied heavy work to account-pair tanks. 4Q+6E share llibresnave. A validation tool that brute-forces every pattern is heavy. The vision must include **incremental, tiered execution**: quick tier (smoke + abuse), medium tier (numeric oracle + cross-pattern consistency), heavy tier (description-driven adversarial search + statistical plausibility gate). That way we do not drain the shared tank on low-signal runs.

Tenth thought: the tool should be self-doubting. Before trusting its own verdict, it should run a **self-consistency check**: run the same attack twice with different seeds/fixtures and confirm the verdict is stable. If a pattern only fails on one random draw, that is a flaky oracle, not a bug. Illia values honesty over smoothness; the tool should report "flaky oracle" as a first-class category.

## Proposals

1. **Oracle-weakness scanner** — analyze each self-test/assert to detect whether the evidence would also pass under an obviously-wrong alternative implementation (e.g., constant output, sign-flipped formula, no-op). WHY: Illia's three hand-kills all had green asserts that proved nothing; the tool must judge the test, not just the code.

2. **Semantic inversion fuzzing** — for every guard/rejection condition, also test the opposite boundary (e.g., if negative variance should be rejected, test that a tiny positive variance is accepted). WHY: catches backwards comparisons and off-by-one guards that ordinary abuse tests miss.

3. **Description-driven counterfactual generator** — parse the description's guarantee and synthesize minimal fixtures where the guarantee is non-trivially true, then check the code satisfies it. WHY: moves validation from "does not crash on garbage" to "does the documented contract hold on meaningful cases."

4. **Plausibility pre-gate** — reject impossible or degenerate fixtures before they reach the implementation (e.g., negative trials, zero variance, contradictory labels). WHY: prevents the `bayesian_ab_beta`-class bug where impossible data returns a confident but meaningless PASS.

5. **Cross-pattern coherence bank** — maintain a small set of shared reference fixtures and run sibling patterns (bandits, causal estimators, streaming sketches) against them; flag contradictions. WHY: a hostile reviewer will point out when two AURA patterns disagree on the same textbook problem.

6. **Flaky-oracle detector** — repeat each numeric/oracle attack with multiple seeds and report "stable fail / stable pass / flaky" before declaring a defect. WHY: distinguishes real bugs from brittle self-tests and avoids false alarms that waste Illia's time.

7. **Tiered execution by cost** — split the tool into quick (smoke+abuse), medium (numeric oracle+cross-pattern), and heavy (adversarial search+plausibility) tiers with explicit token/time budgets per pattern. WHY: 4Q+6E share one Ollama tank; we cannot afford to run the heavy tier on every file every time.

8. **Adversarial evidence-card format** — every reported defect includes: claimed invariant, counter-example input, actual output, why it violates the claim, confidence, and reproduction command. WHY: makes the machine's reasoning inspectable in Illia's Part C gate and surfaces near-misses.

9. **Compile-and-run enforcement for compiled languages with stub-injection** — for cpp/rust/go, compile a tiny harness that calls each public entry point with the abuse fixtures and checks both return values and side effects. WHY: 6E noted 10 cpp files were compile-repaired but never verified; compiled languages can silently fail at link time even when descriptions are accurate.

10. **Description drift watch** — after any fix session, diff the description against the code's exported symbol/type signatures and flag claims that no longer have a corresponding implementation anchor. WHY: prevents the "docstring lie" where a fix changes behavior but the description still promises the old guarantee.
