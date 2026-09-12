# 6E Tool Vision — VALIDATION TOOL Design (2026-07-19)

## Chain of Thought

I started by asking: what did Illia find that every machine gate missed? Three kills:

1. **bayesian_ab_beta** — impossible data (counts violating beta support) → confident PASS
2. **stacking_ensemble** — NaN trained silently → output identical to clean
3. **bayes_factor_normal_means** — WRONG FORMULA, sign-flipped, planted test passed at 1.24>1 by luck

Three different failure modes. One tool won't catch all three with one mechanism.

**Dead end I walked into first:** I thought "we need a smarter fuzzer — more attack classes, more coverage." But the bayes_factor kill wasn't a fuzzing miss. The function returned a valid float every time. A smarter fuzzer would have generated more inputs and gotten more valid floats. The problem wasn't coverage — it was that the tool had no way to know what the *right answer* was. Fuzzing finds crashes and exceptions; it doesn't find wrong answers on valid-looking data.

**Second dead end:** "Reference implementation for every pattern." Powerful but impractical — writing a second implementation for 230 patterns is a library-scale project on its own. And if the reference has the same bug as the main (both written from the same misunderstanding), you get false confidence. The bayes_factor formula was wrong in a way that a second implementation written from the same paper would likely reproduce.

**What survived:** three distinct mechanisms that together cover the three kills, plus two more that cover failure classes no one has hit yet but that a hostile reviewer would find.

---

### The three kills mapped to mechanisms

| Kill | Root cause | What would catch it | Mechanism type |
|---|---|---|---|
| bayesian_ab_beta | No domain invariant check | Check that input COULD EXIST in the mathematical domain | Invariant probe |
| stacking_ensemble | Silent NaN propagation | Check output PLASIBILITY, not just non-crash | Output sanity |
| bayes_factor_normal_means | Wrong formula, plausible numbers | Compare against a TRUSTED computation of the same quantity | Numeric oracle (already speced) |

The numeric oracle is already in the spec — good, that covers kill 3. Kills 1 and 2 need new mechanisms.

---

### What a hostile reviewer would try (that isn't covered)

I thought about what I'd do if I were reviewing these patterns for a journal:

- **Boundary conditions at domain edges** — n=0, n=1, empty arrays, MAX_INT. Fuzzers are bad at hitting exact boundaries because they mutate randomly. You need deliberate boundary probes.
- **Numerical stability on ill-conditioned inputs** — near-singular matrices, very small probabilities, extreme ratios. The algorithm might converge in theory but diverge in practice on these. No current mechanism checks this.
- **Claim falsification** — the description says "O(log n)" but the implementation is O(n). The description says "thread-safe" but there's a shared mutable static. No current mechanism extracts claims from descriptions and tests them.
- **Stateful corruption** — call the function twice; the second call is contaminated by state left by the first. No current mechanism tests sequential calls.

---

### What I'm NOT proposing (and why)

- **Thread safety testing** — important but language-specific (Rust is safe by default, C++ needs ThreadSanitizer, Python has the GIL). Defer to Illia's gate with a note.
- **Memory safety** — similarly language-specific. Rust's compiler already enforces this; C++ needs ASan. Not a tool we should build — use existing sanitizers.
- **Full reference implementation for every pattern** — too expensive, and risks shared-blind-spot bugs. The numeric oracle (already speced) is the right scope for closed-form math.

---

## Proposals

### P1. Invariant probe grid — catches the bayesian_ab_beta class

**Why:** The semantic fuzzer checks for crashes and exceptions, but it doesn't check whether the input *could exist in the mathematical domain of the function*. For every pattern with a known mathematical invariant (probability in [0,1], variance ≥ 0, Bayes factor symmetric under label swap, count ≤ population), generate probe points designed to make the invariant falsifiable. If the invariant holds across a grid, the formula is likely correct. If it breaks, you found the bug without needing a reference implementation.

**How:** For each pattern, the pattern's metadata includes a set of invariants (machine-readable: `invariant: "sum(probs) == 1.0"`, `invariant: "variance >= 0.0"`). The probe grid generates inputs at the invariant's stress points (near-zero, near-one, extreme ratios) and checks the invariant holds within tolerance. This is different from the numeric oracle — it doesn't need a reference computation, just the mathematical property.

**Cost:** Low per pattern (one invariant check per probe point, O(1) each). The metadata burden is the main cost — someone has to write the invariants.

---

### P2. Output plausibility metrics — catches the stacking_ensemble class

**Why:** The stacking_ensemble kill showed that a model can train with NaN internally and still produce output that looks identical to a clean run. The fuzzer checks for crashes, but NaN propagation is silent in C++ with `-ffast-math` and in Python with numpy's default settings. After every fuzzing run, check not just "did it crash?" but "are the outputs *plausible*?" — finite, non-NaN, within expected bounds, and *different* from the output on garbage input. If feeding random noise produces the same output as clean data, something is silently ignoring the input.

**How:** After each fuzzing run, the tool computes: (a) are all outputs finite and non-NaN? (b) are outputs within the expected range for the pattern type? (c) is the output *different* from the output on a garbage/noise input? If (c) fails — same output for clean and garbage — flag as E011-class (overclaimed-invariant: the function claims to process input but doesn't).

**Cost:** Trivial — a few float checks per output value. No metadata burden.

---

### P3. Boundary value analysis — catches edge-case crashes the fuzzer misses

**Why:** Fuzzers are good at finding unexpected inputs but bad at hitting exact domain boundaries. They mutate randomly; they don't deliberately test n=0, n=1, empty arrays, MAX_INT, or the exact point where an algorithm switches from one code path to another. A hostile reviewer always checks boundaries. The tool should too, as an explicit pass separate from fuzzing.

**How:** For each pattern, the pattern metadata includes a boundary spec (`min_inputs: 1`, `max_inputs: 2^31-1`, `empty_allowed: false`). The tool generates test cases at every boundary: n=0 (if allowed), n=1, n=2, n=MAX, n=MAX-1, and at any documented switching points. Each boundary test checks for crash, NaN, and plausibility (P2).

**Cost:** Low — O(boundaries) per pattern, typically 5-10 test cases. Metadata burden is the main cost.

---

### P4. Numerical stability sweep — catches the "converges in theory, diverges in practice" class

**Why:** Many patterns are iterative algorithms with convergence guarantees that depend on well-conditioned inputs. On ill-conditioned inputs (near-singular matrices, very small probabilities, extreme ratios), the algorithm may converge to the wrong answer, fail to converge, or silently return the initial guess. No current mechanism checks this. A hostile reviewer would try these inputs.

**How:** For each iterative pattern, the tool generates ill-conditioned inputs: near-singular matrices (for linear algebra), near-zero probabilities (for statistical), extreme ratios (1:1e10), and checks: (a) does it converge within the iteration limit? (b) does the output change meaningfully from the initial guess? (c) is the output stable under small perturbations of the input? If the output is identical to the initial guess, the algorithm is silently failing.

**Cost:** Medium — each stability test runs the full algorithm. But the number of tests is small (5-10 per pattern). Worth it for math-heavy patterns.

---

### P5. Claim extraction + automated verification — catches description-vs-code lies

**Why:** Illia's gate includes Part C: code-vs-claim sampling. The tool should automate the mechanical subset of this. For every pattern, extract testable claims from the description (complexity class, determinism, thread safety, memory bounds, numerical tolerance) and generate a test that proves or disproves each claim. If the description says "O(log n)" but the implementation is O(n), the tool should catch that before Illia sees it.

**How:** This is the hardest proposal to fully automate (claim extraction from natural language is fuzzy). But a partial implementation is still valuable: the pattern metadata includes a `claims` field (`claims: {complexity: "O(log n)", deterministic: true, thread_safe: false}`). The tool reads this field and generates the corresponding test: for complexity, measure runtime at n=10, n=100, n=1000 and check the scaling; for determinism, run twice with same seed and compare; for thread safety, check for shared mutable state. Claims that can't be automated (e.g., "handles edge cases gracefully") are flagged for Illia's manual Part C.

**Cost:** Medium-high to build the test generators, but low per pattern once built. The metadata burden is real — someone has to write the claims field for each pattern. But this is a one-time cost that pays for itself every time the pattern is re-verified.

---

### Summary: what the three kills map to

| Kill | Caught by | Already speced? |
|---|---|---|
| bayesian_ab_beta (impossible data → PASS) | P1 (invariant probe) | No — new |
| stacking_ensemble (NaN → plausible output) | P2 (output plausibility) | No — new |
| bayes_factor_normal_means (wrong formula) | Numeric oracle (already speced) | Yes |

And what the hostile reviewer would find:

| Attack | Caught by | Already speced? |
|---|---|---|
| Boundary edge cases | P3 (boundary analysis) | Partial (fuzzer covers some) |
| Ill-conditioned inputs | P4 (stability sweep) | No — new |
| Description-vs-code lies | P5 (claim verification) | No — new |
| Stateful corruption | P2 (output plausibility on sequential calls) | No — new |

---

### What I'd build first, in order

1. **P2 (output plausibility)** — cheapest, catches the stacking_ensemble class, zero metadata burden. Ship this in the first iteration.
2. **P1 (invariant probe grid)** — catches the bayesian_ab_beta class. Requires metadata but the invariants are simple to write. Ship in v1.1.
3. **P3 (boundary analysis)** — cheap, catches edge cases. Ship alongside P1.
4. **P4 (stability sweep)** — medium cost, catches a class no one has hit yet. Ship in v2.
5. **P5 (claim verification)** — highest value, highest build cost. Ship in v3 after the tool is proven against Illia's ~50 hand-verdicts.

The first three (P1+P2+P3) together with the existing spec (fuzzer + numeric oracle + combined-fault injection) would have caught all three of Illia's kills. That's the bar for "advanced enough to stand next to Illia's judgment" — not catching everything, but catching everything he's already found.
