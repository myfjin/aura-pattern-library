# AURA Error Catalog — empirical, built during Illia's manual audit
**Started 2026-07-19 · living document · grows one entry per error actually observed in testing.**

Companion to `ERROR_TAXONOMY.md` (statuses & gates) — that doc says what a VERDICT means;
this one catalogs the RUNTIME ERRORS a user of the library can actually hit, with stable IDs.
Purpose: (a) full definition-coverage of the lib ("defined in all meanings" — Illia, 07-19);
(b) the spec sheet for the future code-level retrofit (paid tier: patterns raise `AURA-E###`
directly). Retrofit stays a separate gated lane — THIS doc changes no code.

## Entry format
- **ID**: AURA-E### (sequential, never reused) · **Class**: B1 type · B2 shape · B3 numeric edge ·
  B4 null/NaN · B5 boundary/domain · B6 encoding/language · B7 number format · B8 empty
- **Quality**: CONTRACT (explicit check, names the input) / ACCIDENTAL (math or runtime crashed;
  message cryptic or misattributed). ACCIDENTAL = pattern PASSES the three-way rule but is a
  retrofit candidate.

---

### AURA-E001 · Class B5 (domain) · ACCIDENTAL
- **Pattern:** `python/data-science/statistical_modeling/power_analysis_sample_size.py`
- **Trigger:** `alpha = -0.05` (negative significance level; combined attack w/ `p1=1.5`)
- **Observed:** `ValueError: expected a positive input, got -0.02499…` at `normal_quantile`
  line 22 (`math.log(1.0 - p)` domain).
- **Why cryptic:** reports the intermediate `1-alpha/2` value, names neither `alpha` nor `p1`.
  With multiple bad inputs, FIRST crash wins and misattributes the fault (Illia's find, 07-19).
- **Means (plain words):** significance level must be in (0, 1).
- **Ideal message:** `AURA-E001: alpha must be in (0,1), got -0.05`.

### AURA-E002 · Class B3 (numeric edge) · ACCIDENTAL
- **Pattern:** same file
- **Trigger:** `p1 = p2 = 0.5` (zero effect size)
- **Observed:** `ZeroDivisionError: division by zero` at `sample_size_two_proportion` line 96
  (`… / (effect ** 2)`).
- **Means:** identical proportions ⇒ no effect ⇒ required sample size is undefined (infinite).
- **Ideal message:** `AURA-E002: effect size is zero (p1 == p2); sample size undefined`.

### AURA-E003 · Class B5 (domain) · ACCIDENTAL
- **Pattern:** same file
- **Trigger:** `p1 = 1.5` alone (probability out of [0,1], everything else healthy)
- **Observed:** `ValueError: expected a nonnegative input, got -0.5` at `two_proportion_power`
  line 53 (`math.sqrt(p1*(1-p1)+…)` — 1.5·(−0.5) drives the radicand negative).
- **Why cryptic:** reports the radicand, not the offending probability; a DIFFERENT function
  crashes than in E001 — error location depends on which garbage enters first, not on the fault.
- **Means:** proportions must be in [0, 1].
- **Ideal message:** `AURA-E003: p1 must be in [0,1], got 1.5`.

### AURA-E004 · Class B5 (domain) · **was SILENT — the audit's first true INVALID**
- **Pattern:** `python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py`
- **Trigger:** `successes > trials` (Illia run 4: 65 successes / 10 trials → printed
  `PASS, P(B>A)=1.000, mean B=1.000`)
- **Observed:** NO error — confident wrong output. Root cause: `beta = prior + (trials − successes)`
  goes NEGATIVE (1 + 10 − 65 = −54); a negative Beta parameter is mathematically meaningless and
  the sampler saturates at 1.0.
- **Means:** more successes than trials is impossible data; the experiment described never happened.
- **Message (implemented in retrofit):** `AURA-E004: successes_b (65) exceed trials_b (10) — impossible data`.

### AURA-E005 · Class B3/B8 (no data) · **was SILENT — second true INVALID**
- **Pattern:** same file
- **Trigger:** `trials = 0` with successes > 0 (Illia run 11) → printed `PASS, mean B=1.000`.
- **Observed:** NO error — confident output from zero experiments.
- **Means:** zero trials = no experiment ran; any posterior claim is fiction.
- **Message (implemented):** `AURA-E005: trials_b must be > 0, got 0 (no experiment ran)`.

### AURA-E006 · Class B1 (type) · SILENT COERCION (flag, not fabrication)
- **Pattern:** `python/system-administration/text-stream-ops/robust_csv_parse.py`
- **Trigger:** `parse_csv_line(None, strict=False)` (not a string at all)
- **Observed:** returns `[]` silently — script's ✓ still prints. Root cause: **`io.StringIO(None)`
  is a stdlib quirk meaning "empty buffer"**, so None is coerced into empty-input semantics and
  takes the legitimate StopIteration path. No broad except involved.
- **Means:** absence of input (None) is not the same as empty input (""). Masking the type fault
  hides caller bugs (an unassigned variable parses "successfully" forever).
- **Ideal:** `AURA-E006: text must be str, got NoneType` — raise even in non-strict mode
  (non-strict tolerates broken ROWS, not broken TYPES).
- **Contrast (the good news):** the same file's strict-mode catch (`ValueError: Malformed CSV: …`)
  is the audit's FIRST CONTRACT-quality error — deliberate raise, named fault class. Proof that
  contract catches were always possible; the standard exists in our own library.

### AURA-E007 · Class B2/B5 (shape + label domain) · LATE-ACCIDENTAL (the worst catch class)
- **Pattern:** `python/data-science/ensembles_and_robust_methods/stacking_ensemble.py`
- **Trigger:** junk element prepended to `y` (Illia: `y = [10]` before generation) → 101 labels vs
  100 points, label `10` outside {0,1}, every label shifted off its point.
- **Observed:** `fit()` ingested it all silently and TRAINED; the crash came only downstream
  (IndexError in the accuracy loop) — by arithmetic luck, not by contract.
- **Means:** a model can be corrupted at training time with zero complaint; the error, when it
  comes, points at the wrong place entirely.
- **Ideal:** `AURA-E007: len(X)=100 != len(y)=101` + `labels must be in {0,1}, got 10` at fit() entry.

**Field note — the no-op attack (Illia's discovery, 07-19):** editing an initializer that later
code overwrites (`X = []` before generation loops that append) produces a PASS that LOOKS like
fake-robustness but is a legitimate run on rebuilt data. Before judging a PASS, confirm the attack
actually reached the target — attack AFTER generation, or attack the function call itself.

### AURA-E008 · Class B4 (NaN/non-finite) · **was PERFECTLY SILENT — the audit's purest fake-robust**
- **Pattern:** `python/data-science/ensembles_and_robust_methods/stacking_ensemble.py`
- **Trigger:** `X[0] = (float("nan"), 0.0)` in training data (Illia, 07-19).
- **Observed:** confident PASS with accuracies **identical to the clean baseline** — the poisoned
  run is indistinguishable from a healthy one. NaN compares as unordered without raising, so
  `sorted()` quietly mis-orders and the model trains on non-data with zero trace.
- **Means:** a broken upstream feed (NaN from a failed sensor/parse) corrupts the model forever
  and nothing ever complains — the most dangerous failure class in the library.
- **Message (implemented in retrofit):** `AURA-E008: X[0] contains non-finite/non-numeric value (nan, 0.0)`.

### AURA-E009 · Class B5/B8 (parameter domain + empty input) · SILENT DEGENERATE OUTPUT
- **Pattern:** `python/data-science/composed_tools/dedup_pipeline.py`
- **Trigger:** `shingles("abc", k=0)` (Illia, 07-19) — also any k <= 0, and empty-string docs.
- **Observed:** returns a set holding one empty string, silently. The `range(max(1, ...))`
  construction guarantees at least one window even when the window size is nonsense. Same root:
  `shingles("")` gives the same degenerate set, so two EMPTY docs verify as perfect duplicates.
- **Means:** meaningless shingle size (or contentless doc) yields a degenerate signature the
  rest of the pipeline treats as real.
- **Ideal:** `AURA-E009: k must be >= 1, got 0` - and an empty-doc policy declared in the contract.

### AURA-E010 · NEW CLASS: WRONG-MATH (code-vs-claim) · **the audit's deepest kill**
- **Pattern:** `python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py`
- **Found by:** Illia's free-play on the demo's own data (sigma/n changes), 07-19 batch 2.
- **Defect:** the marginal-likelihood evidence term uses `y_mean^2*n/denom`; correct conjugate
  form requires `tau^2*(sum y)^2/denom` — a missing factor of n*tau^2. Verified against
  brute-force numeric integration: 30 points at 2.0 -> code BF 1.24, TRUE BF 3e24. The planted
  demo passed only because 1.24 > 1 by a hair (planted-test-too-easy concealing wrong math).
- **Consequence:** SIGN-FLIPPED conclusions on valid data (Illia's 300 identical points at the
  H1 mean -> code said 0.42, evidence AGAINST the visible truth).
- **Why every machine gate missed it:** oracle ran the too-easy planted test; assert_linter checks
  assert shape; cross-model review checks description-vs-intent. Only re-derivation or a NUMERIC
  ORACLE (closed-form vs brute integration on probe points) catches wrong math -> new gate idea
  for the validation tool, recorded.
- **Fix:** corrected formula + contract, verified vs numeric ground truth:
  `playground/retrofit_demo/bayes_factor_normal_means_RETROFIT.py` (also prints PASS receipts).

### AURA-E011 · NEW CLASS: OVERCLAIMED-INVARIANT (claim true only in undeclared sub-domain)
- **Pattern:** `python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py`
- **Found by:** Illia free-play (alpha=100 with default truncation), 07-19 batch 2.
- **Defect:** docstring promises "probabilities that sum to (approximately) 1" — but with
  num_breaks=100 the expected UNBROKEN remainder is (alpha/(1+alpha))^100: for alpha=100 that is
  ~0.37, so weights sum ~0.6. The pattern's own demo assert (>0.9) FAILS on valid input.
  The claim silently assumes alpha << num_breaks/2.3 and never says so.
- **Distinction from E010:** the math here is CORRECT (truncation behaves as theory says);
  the CLAIM is broader than the math. Cure = qualify the claim + guard: require num_breaks
  large enough for the requested alpha, or return the remainder explicitly.
- **Also observed same file:** alpha<=0 caught by STDLIB (random.gammavariate) with a message
  about ITS internals ("alpha and beta must be > 0.0" = gamma params, not the user's alpha) —
  delegated-accidental catch, misattributed message. num_breaks=0 -> [] silently (E009 class;
  [] sums to 0, contradicting the pattern's own invariant).

### AURA-E012 · NEW CLASS: VALIDATION-THEATER (shallow proxy for a claimed guarantee)
- **Pattern:** `rust/parsing-protocols/http_request_line_parser.rs` (Illia, 07-20)
- **Trigger:** structurally-valid but semantically-malformed input — `"GET /path HTTP/BANANA"`,
  `"GET /path HTTP/"` (bare prefix, no version), `"BANANA /p HTTP/1.1"`, `"GET @@@ HTTP/1.1"`.
  ALL return `Ok(...)`.
- **Defect:** docstring claims "malformed requests return Err rather than being silently accepted",
  code comment says "missing HTTP version → Err" — but validation checks only STRUCTURE
  (exactly 3 whitespace parts + `version.starts_with("HTTP/")`), never CONTENT. `HTTP/` passes
  the version check though it contains no version.
- **Distinct from E011:** E011 = a REAL invariant, over-scoped (holds in a sub-domain). E012 =
  NO real validation, just a cheap proxy costumed as one. The guarantee was never implemented.
- **Caught by:** existing recipe R11 (claim-falsification) — feed input that violates the stated
  guarantee, check it's silently accepted. No new recipe; new verdict subclass.

### META-LAW (07-20, Illia's rust probe): TYPE-SAFETY SHIFTS THE RECIPE DISTRIBUTION
Strong type systems (rust, and partly go/cpp) make R6 (wrong-type), R8 (NaN-poison), R1/R2
(numeric-domain) UNCOMPILABLE — the compiler enforces them. Risk therefore MIGRATES to semantic
validation of well-typed inputs → **R11 claim-falsification dominates.** Tool consequence: a
LANGUAGE-AWARE PRIOR — in strongly-typed langs, down-weight type/NaN recipes, up-weight R11 +
semantic-content probes. TESTABLE PREDICTION: rust patterns show fewer type/value kills, more
validation-theater/claim-gaps than python. (Test in progress across the rust sphere.)

## Notes from the field (Illia's session, 07-19)
- **Pre-runtime attacks:** editing source to bare `шістдесят п'ять` or `06` triggers Python's
  PARSER (SyntaxError) before the pattern runs — that's an artifact of source-level attack, not a
  pattern property. The equivalent runtime attack is the quoted string → caught as AURA-E-B1.
- **Planted-demo-assert ≠ contract:** `__main__` blocks are proof harnesses with planted data.
  Impossible inputs sometimes crash the harness's EXPECTATIONS (luck), and *valid* inputs that
  contradict the planted story crash them too (Illia run 7: A genuinely better → assert fails).
  Only entry-function validation is real protection. Teach: use the function, don't repurpose
  the harness.
- **Delegated catches:** a stdlib error (gammavariate) firing on your parameter is still an
  ACCIDENTAL catch — and its message describes the stdlib's internals, not your input. Worse
  than the pattern's own cryptic errors: it names somebody else's variables.
- **Combined-fault injection (Illia's tool requirement, 07-19):** the validation tool must fire
  fault COMBINATIONS, not just singles — first-crash-wins means N-1 of N faults hide behind the
  first; a contract is only proven compositional when simultaneous bad inputs yield ALL
  violations in one report (accumulate-then-raise verified pairwise and full-stack).
- **Layered reporting:** when a parameter's TYPE is wrong, range checks on the same pair are
  skipped as uncomparable — fix the type fault and remaining range faults surface next call.

---
## THE DESIGN RULE for the retrofit (proven 2026-07-19, Illia's requirement)
**Accumulate-then-raise.** First-crash-wins cannot be fixed by better messages — Python stops at
the first illegal operation. The fix is structural: every pattern's entry function gets a
`_validate_*_inputs()` contract block that checks ALL declared inputs against the docstring
domain, collects ALL violations, and raises ONE `AuraInputError` listing every violation with
its AURA-E code, parameter name, and offending value. Multiple bad inputs → multiple lines, one
error. Working proof: `playground/retrofit_demo/power_analysis_sample_size_RETROFIT.py`
(Illia's combined attack p1=1.5 + alpha=-0.05 → both E003 and E001 reported together; healthy
baseline unchanged). This is the template for the paid-tier retrofit lane.

## Audit-observed pattern-level summary
| Pattern | Attacks run | Silent-wrong | Verdict | Retrofit candidates |
|---|---|---|---|---|
| power_analysis_sample_size.py | 3 (E001–E003) | 0 | **PASS-WITH-FLAG** (all catches accidental) | E001–E003 |
| bayesian_ab_beta.py | 12 runs by Illia | **2** (runs 4, 11) | **❌ INVALID (fake-robust)** — fix PROVEN in `playground/retrofit_demo/bayesian_ab_beta_RETROFIT.py`, queued for gated library ingest | E004, E005 + B1 |
| robust_csv_parse.py | 3 attacks | 0 (one silent coercion ⚠) | **PASS-WITH-FLAG** — first CONTRACT-quality catch; None→[] coercion flagged | E006 |
| stacking_ensemble.py | 10 runs by Illia | **1** (NaN poison — output identical to clean) | **❌ INVALID (fake-robust)** — fix PROVEN in `playground/retrofit_demo/stacking_ensemble_RETROFIT.py` | E007, E008 |
| dedup_pipeline.py | 8 runs by Illia | 1 silent-degenerate (k=0) | **PASS-WITH-FLAG** - Ukrainian dup detection genuine (unicode-clean); k/empty-doc guard missing | E009 |
| bayes_factor_normal_means.py | 9 runs by Illia (batch 2) | **1 wrong-math** (sign-flipped BF on valid data) | **XX INVALID (WRONG FORMULA)** - corrected + verified vs numeric integration | E010 (+B8/B5/B4 instances) |
| dirichlet_stick_breaking.py | 10 runs by Illia (batch 2) | 0 silent-wrong (1 silent-degenerate [], 1 overclaim) | **PASS-WITH-FLAG** - claim needs qualification (E011) + description fails comprehension gate (rewrite queued) | E011 (+E009, delegated-catch instances) |

---
## GO BATCH 1 — new error classes (Illia's hand-audit card session, 2026-07-21)
Five go natives audited live (deadline_ttl, exponential_backoff, csv_validator,
circuit_breaker, bloom_filter). Three ❌ INVALID, two STRONG-FLAG. New classes:

- **AURA-E013 — silent-overflow-wrap.** Typed-language arithmetic wraps without error:
  go `baseDelay * (1 << n)` through `time.Duration` lands on EXACTLY 0 → the backoff
  VANISHES (measured 37µs where the contract implies centuries) and the failing service
  is hammered at full speed. Python/R immune (arbitrary precision / double) — this class
  fires only in typed lanes (recipes.py R14, LANG_PRIORS "overflow").
- **AURA-E014 — magic-sentinel-collision.** csv_validator treats the literal string
  `"<nil>"` as missing → a legal value silently vanishes, dropping whole rows. Any
  in-band sentinel ("null", "None", "N/A", "-") is a data-loss trap.
- **AURA-E015 — non-monotonic-clock-trust.** deadline_ttl: an EXPIRED lease RESURRECTS
  when the clock steps backward (NTP correction, VM restore). TTL/lease logic that
  trusts a rewindable clock lies about liveness. Kin: token_bucket idle-burst.
- **AURA-E016 — cumulative-state-counting.** circuit_breaker never resets failureCount
  on success in CLOSED → the "3 failures" threshold is cumulative-forever, and a
  50%-healthy alternating service trips PERMANENTLY OPEN. The breaker manufactures the
  outage it exists to prevent. Contract-grade counting must be consecutive or windowed.
- **AURA-E017 — stdlib-parser-accepts-poison.** go `strconv.ParseFloat("NaN")` (and
  python `float("nan")`) SUCCEED → a schema validator that delegates to them validates
  NaN/±Inf as legal numbers with zero errors. Delegated validation inherits the
  delegate's tolerance for poison. (Executable now: recipes.py R15 + generic executor.)

Strengths on the record (the audit cuts both ways): go strconv.Atoi catches 20-digit
overflow cleanly; bloom's analytic FPR is honest even at 100k/cap-10 saturation;
bloom held no-false-negatives everywhere; NaN TTL immortality aside, deadline
arithmetic is exact at every sane boundary.

Cross-language law CONFIRMED for the third sphere: sysadmin/resilience patterns hide
STATE-LIES-OVER-TIME (python ttl_cache size(), go bloom itemCount, go breaker count,
go deadline resurrection) — and every kill in all three languages was invisible to
compile+run health checks. R13's sequence list now encodes all five observed sequences.
