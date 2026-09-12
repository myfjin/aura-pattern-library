"""
probes.py — executable adapters: import a pattern's entry function and run recipe fixtures
against it, capturing the real result for the oracle. This is where recipes meet real code.

Each probe returns a `result` dict for oracle.classify_signal:
  raised, error_text, output, clean_output, reached, names_bad_param, oracle_match,
  invariant_broken, mutation_unnoticed.

v1 wires the audited PYTHON patterns (richest attack surface). The pattern of each adapter
is identical -> generic manifest-driven execution is the v1.5 extension.
"""
import importlib.util, os, math, io, contextlib, subprocess, sys, tempfile

LIB = os.path.expanduser("~/aura-pattern-library")

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regression_fixtures")

def _load(relpath):
    p = os.path.join(LIB, relpath)
    spec = importlib.util.spec_from_file_location("pat", p)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)  # module-level demo runs; we then call its functions
    return m

def _load_fixture(name):
    """Load a BROKEN snapshot from regression_fixtures/ — the permanent kill-test corpus.
    A pattern fixed in the library keeps its detection test here forever (the tool must never
    LOSE the ability to catch the defect it once caught)."""
    p = os.path.join(FIXTURES, name)
    spec = importlib.util.spec_from_file_location("fix_" + str(abs(hash(name))), p)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        spec.loader.exec_module(m)
    return m

def _call(fn, *args, **kw):
    "run fn, capture raised/output; suppress its stdout."
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            out = fn(*args, **kw)
        return {"raised": False, "output": out}
    except Exception as e:
        return {"raised": True, "error_text": f"{type(e).__name__}: {e}", "output": None}


# ---- bayes_factor: R10 numeric-oracle. LIVE file is FIXED (match->PASS); the BROKEN
#      snapshot fixture must still mismatch (INVALID). Same oracle, two files. ----
def _brute_bf(data, tau2=1.0):
    n = len(data); lo, hi, steps = -50, 50, 200000; dt = (hi-lo)/steps
    logs = []
    for i in range(steps):
        th = lo+(i+0.5)*dt
        lp = -0.5*th*th/tau2 - 0.5*math.log(2*math.pi*tau2)
        ll = sum(-0.5*(y-th)**2 - 0.5*math.log(2*math.pi) for y in data)
        logs.append(lp+ll)
    M = max(logs); log_m1 = M + math.log(sum(math.exp(l-M) for l in logs)*dt)
    log_m0 = sum(-0.5*y*y - 0.5*math.log(2*math.pi) for y in data)
    return math.exp(log_m1-log_m0)

def _bf_oracle(m):
    fn = m.bayes_factor_normal
    data = [2.0]*30
    code = _call(fn, data, 1.0)["output"]
    truth = _brute_bf(data, 1.0)
    match = code is not None and abs(math.log10(max(code,1e-300)) - math.log10(max(truth,1e-300))) < 1.0
    return {"raised": False, "output": code, "oracle_match": match,
            "oracle_run": True, "oracle_truth": truth,
            "detail": f"code={code:.3g} truth={truth:.3g}"}

def probe_bayes_factor():   # LIVE (fixed) -> match=True -> PASS
    return _bf_oracle(_load("python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py"))

def probe_bayes_factor_BROKEN():   # FIXTURE (wrong-math snapshot) -> mismatch -> INVALID
    return _bf_oracle(_load_fixture("bayes_factor_normal_means.BROKEN.py"))

# ---- bayesian_ab_beta: LIVE FIXED (impossible-data guard + B-better oracle -> PASS);
#      BROKEN fixture keeps the confident-on-impossible-data defect (-> INVALID). ----
def _ab_impossible_silent(m):
    r = _call(m.bayesian_ab_test, 60, 100, 65, 10)   # 65 successes / 10 trials — impossible
    out = r.get("output")
    return (not r["raised"]) and isinstance(out, tuple) and out and _finite(out[0]), out

def probe_bayesian_ab():   # LIVE (fixed): impossible raises + B-clearly-better -> prob~1 -> PASS
    import random
    m = _load("python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py")
    guarded = _call(m.bayesian_ab_test, 60, 100, 65, 10)["raised"]   # impossible must raise
    random.seed(1)
    out = _call(m.bayesian_ab_test, 20, 100, 80, 100)["output"]      # B clearly better
    b_better = isinstance(out, tuple) and out[0] > 0.95
    ok = guarded and b_better
    return {"raised": False, "output": out, "reached": True,
            "oracle_run": True, "oracle_truth": "impossible rejected + P(B>A)>0.95 when B clearly wins",
            "oracle_match": ok, "invariant_checks": ["impossible_guarded", "b_better_detected"],
            "detail": f"impossible guarded={guarded}; P(B>A)={out[0]:.3f} when B wins"}

def probe_bayesian_ab_BROKEN():   # FIXTURE: confident output on impossible data -> INVALID
    m = _load_fixture("bayesian_ab_beta.BROKEN.py")
    silent_wrong, out = _ab_impossible_silent(m)
    return {"raised": False, "output": out, "reached": True,
            "confident_impossible": silent_wrong, "oracle_coverage": {"semantic": True},
            "invariant_broken": silent_wrong, "detail": f"65/10 -> {out}"}

# ---- stacking_ensemble: LIVE FIXED (NaN guard + ensemble-improvement oracle -> PASS);
#      BROKEN fixture keeps the silent NaN-absorb (-> INVALID). ----
def _stacking_nan_silent(m):
    b = m.BaseModel1()
    Xn = [(float("nan"), 2.0), (3.0, 4.0), (5.0, 6.0)]
    return not _call(b.fit, Xn, [0, 1, 0])["raised"]   # silent absorb = defect

def probe_stacking():   # LIVE (fixed): NaN raises + ensemble improves over base -> PASS
    m = _load("python/data-science/ensembles_and_robust_methods/stacking_ensemble.py")
    guarded = not _stacking_nan_silent(m)               # NaN must now raise
    # positive oracle: on separable clean data the base learner recovers the true threshold
    b = m.BaseModel1(); b.fit([(1.0, 0.0), (2.0, 0.0), (8.0, 0.0), (9.0, 0.0)], [0, 0, 1, 1])
    preds = b.predict([(1.0, 0.0), (9.0, 0.0)])
    separates = (preds == [0.0, 1.0])
    ok = guarded and separates
    return {"raised": False, "output": [guarded, separates], "reached": True,
            "oracle_run": True, "oracle_truth": "NaN rejected + threshold separates classes",
            "oracle_match": ok, "invariant_checks": ["nan_guarded", "threshold_separates"],
            "detail": f"NaN guarded={guarded}; clean threshold separates={separates}"}

def probe_stacking_BROKEN():   # FIXTURE: NaN trained silently, no raise -> INVALID
    m = _load_fixture("stacking_ensemble.BROKEN.py")
    silent = _stacking_nan_silent(m)
    return {"raised": False, "reached": True, "nan_absorbed_silently": silent,
            "oracle_coverage": {"semantic": True}, "invariant_broken": silent,
            "detail": f"NaN fit silent-absorb={silent}"}

# ---- power_analysis: recipes catch (accidental) -> PASS-with-flag ----
def probe_power_analysis():
    m = _load("python/data-science/statistical_modeling/power_analysis_sample_size.py")
    fn = m.sample_size_two_proportion
    r = _call(fn, 1.5, 0.5, 0.05, 0.80)   # p1=1.5 out of domain
    # it raises (accidentally) -> caught. no silent-wrong. PASS with flag.
    return {"raised": r["raised"], "error_text": r.get("error_text"), "output": r.get("output"),
            "names_bad_param": False, "reached": True, "oracle_coverage": {"mechanical": True},
            "detail": f"p1=1.5 -> raised={r['raised']}"}

def _finite(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)


# ---- robust_csv_parse: POSITIVE oracle #1 (Illia verdict: PASS — "first contract-quality catch").
#      Ground-truth battery: expected outputs are hand-fixed from the CSV contract (the audit's
#      judgment made executable), NOT re-read from the module's own self-test. ----
def probe_robust_csv():
    m = _load("python/system-administration/text-stream-ops/robust_csv_parse.py")
    fn = m.parse_csv_line
    RAISE = "<ValueError>"
    battery = [
        (("name,age,address",), {}, ["name", "age", "address"]),
        (('alice,30,"123 Main St, Apt 4"',), {}, ["alice", "30", "123 Main St, Apt 4"]),
        (("a,b,c,d",), {}, ["a", "b", "c", "d"]),
        (("field1 , field2 ",), {}, ["field1 ", " field2 "]),      # no trimming by contract
        (('name,"address\nline2"',), {"strict": True}, ["name", "address\nline2"]),
        (("",), {"strict": False}, []),
        (('a,"b"c,d',), {"strict": True}, RAISE),                   # data after closing quote
        (('a,"b"c,d',), {"strict": False}, None),                   # non-strict skips, not raises
        (('a,"b',), {"strict": True}, RAISE),                       # unterminated quote
    ]
    mismatches, results = [], []
    for args, kw, want in battery:
        r = _call(fn, *args, **kw)
        got = RAISE if (r["raised"] and "ValueError" in (r.get("error_text") or "")) else r.get("output")
        results.append(got)
        if got != want:
            mismatches.append(f"{args[0]!r}: want {want!r} got {got!r}")
    none_r = _call(fn, None)  # E006 disclosed flag: None silently coerced to empty input
    return {"raised": False, "output": results, "reached": True,
            "oracle_run": True, "oracle_truth": [w for _, _, w in battery],
            "oracle_match": not mismatches,
            "invariant_checks": [f"contract_battery:{len(battery)}"],
            "detail": ("; ".join(mismatches) if mismatches else
                       f"{len(battery)}/{len(battery)} contract cases exact; "
                       f"E006 None-coercion (disclosed flag): None -> {none_r.get('output')!r}")}


# ---- token_bucket_limiter: LIVE FIXED (burst_cap depth -> idle burst bounded -> PASS);
#      BROKEN fixture keeps the unbounded-accumulation-after-idle kill (-> INVALID). ----
def _tb_idle_burst(m):
    bucket = m.token_bucket_limiter(tokens_per_sec=10)
    bucket.last_refill -= 100.0   # R13: simulate 100s idle by rewinding the refill clock
    return sum(1 for _ in range(500) if bucket.allow_op())

def probe_token_bucket():   # LIVE (fixed): idle burst == cap (two-sided) + rate guard -> PASS
    m = _load("python/system-administration/resource-guards/token_bucket_limiter.py")
    burst = _tb_idle_burst(m)
    # cap defaults to rate (10). A CORRECT bucket grants ~cap on an idle burst: not 500
    # (unbounded accumulation, the BROKEN kill) and not 0 (a limiter that grants nothing —
    # XMT fold-1 caught the old one-sided `burst<=11` blessing a wiped allow_op at burst=0).
    granted = burst >= 8           # actually admits work after idle (lower bound closes the hollow)
    bounded = burst <= 11          # doesn't accumulate unboundedly (upper bound = the BROKEN kill)
    guarded = _call(m.token_bucket_limiter, -5)["raised"]   # rate<=0 must raise
    ok = granted and bounded and guarded
    return {"raised": False, "output": burst, "reached": True,
            "oracle_run": True, "oracle_truth": "8 <= idle burst <= cap+1 (grants ~cap, not 0, not 500)",
            "oracle_match": ok,
            "invariant_checks": ["idle_burst_grants_cap", "idle_burst_bounded_by_cap", "rate_guarded"],
            "detail": f"idle 100s @ rate=10,cap=10 -> burst={burst} (granted={granted},bounded={bounded}); rate<0 guarded={guarded}"}

def probe_token_bucket_BROKEN():   # FIXTURE: unbounded burst after idle -> INVALID
    m = _load_fixture("token_bucket_limiter.BROKEN.py")
    burst = _tb_idle_burst(m)
    broken = burst > 50
    return {"raised": False, "output": burst, "reached": True,
            "invariant_broken": broken, "invariant_checks": ["idle100s_burst_le_cap"],
            "conclusive_kill": broken, "kill_reason": "unbounded_burst_after_idle",
            "detail": f"idle 100s @ rate=10 -> {burst}/500 burst ops granted instantly"}


# ---- dedup_pipeline: POSITIVE oracle (Illia: PASS). Exact edit-distance ground truth +
#      planted-pair detection with a named diff; unrelated docs must NOT pair. ----
def probe_dedup_pipeline():
    m = _load("python/data-science/composed_tools/dedup_pipeline.py")
    checks, truths, gots = [], [], []
    def chk(name, got, want):
        truths.append(want); gots.append(got); checks.append((name, got == want))
    # stage-2 exact verifier: textbook edit distances (independent hand truth)
    chk("ed_kitten", m.edit_distance("kitten", "sitting"), 3)
    chk("ed_flaw", m.edit_distance("flaw", "lawn"), 2)
    chk("ed_empty", m.edit_distance("", "abc"), 3)
    chk("ed_same", m.edit_distance("abcd", "abcd"), 0)
    chk("jaccard_self", m.estimated_jaccard((1, 2, 3), (1, 2, 3)), 1.0)
    # end-to-end: one planted near-dup among unrelated docs
    A = "the quick brown fox jumps over the lazy dog"
    A2 = "the quick brown fox leaps over the lazy dog"
    B = "raft quorum shard vector matrix entropy gradient kernel tensor"
    C = "seasonal retail sales peak sharply before winter holidays arrive"
    cands, verified, expl = m.dedup_pipeline([A, A2, B, C], cand_thresh=0.3)
    chk("planted_pair_verified", verified, [(0, 1)])
    chk("diff_names_the_edit", expl.get((0, 1)), ["-jumps", "+leaps"])
    mismatches = [n for n, ok in checks if not ok]
    return {"raised": False, "output": gots, "reached": True,
            "oracle_run": True, "oracle_truth": truths, "oracle_match": not mismatches,
            "invariant_checks": ["verified_subset_of_candidates", "no_false_pairs"],
            "detail": (f"FAILED: {mismatches}" if mismatches else
                       f"{len(checks)}/{len(checks)} exact (edit-distance truth + planted pair + diff)")}


# ---- dirichlet_stick_breaking: POSITIVE oracle (Illia: PASS). Closed-form theory:
#      E[w1] = 1/(1+alpha); weights in [0,1], partial sums <= 1, sum -> 1. Seeded. ----
def probe_dirichlet():
    import random as _r
    m = _load("python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py")
    fn = m.stick_breaking_process
    _r.seed(7)
    mismatches, details = [], []
    inv_ok = True
    for alpha in (0.5, 5.0):
        first, sums = [], []
        for _ in range(1500):
            w = fn(alpha)
            first.append(w[0]); s = sum(w); sums.append(s)
            if not all(0.0 <= x <= 1.0 for x in w) or s > 1.0 + 1e-9:
                inv_ok = False
        mean_w1, want = sum(first) / len(first), 1.0 / (1.0 + alpha)
        if abs(mean_w1 - want) > 0.03:
            mismatches.append(f"E[w1] alpha={alpha}: want {want:.4f} got {mean_w1:.4f}")
        if min(sums) < 0.999:
            mismatches.append(f"sum drifted from 1: min {min(sums):.6f} @ alpha={alpha}")
        details.append(f"a={alpha}: E[w1] {mean_w1:.4f}~{want:.4f}")
    if not inv_ok:
        mismatches.append("weight/partial-sum invariant broken")
    return {"raised": False, "output": details, "reached": True,
            "oracle_run": True, "oracle_truth": "E[w1]=1/(1+alpha); sum<=1; w in [0,1]",
            "oracle_match": not mismatches,
            "invariant_checks": ["weights_in_unit", "sum_le_1", "sum_to_1"],
            "detail": ("; ".join(mismatches) if mismatches else "; ".join(details))}


# ---- gradient_boosting_stumps: POSITIVE oracle (Illia: PASS). Noiseless separable data:
#      the stump MUST recover the exact split; boosting MUST drive train MSE to ~0. ----
def probe_gradient_boosting():
    m = _load("python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py")
    X = [(1.0, 0.0), (2.0, 0.0), (8.0, 0.0), (9.0, 0.0)]
    y = [1.0, 1.0, 2.0, 2.0]
    feat, thr, lv, rv = m.fit_stump(X, y)
    mismatches = []
    if feat != 0: mismatches.append(f"feature: want 0 got {feat}")
    if abs(thr - 5.0) > 1e-12: mismatches.append(f"threshold: want 5.0 got {thr}")
    if abs(lv - 1.0) > 1e-12 or abs(rv - 2.0) > 1e-12:
        mismatches.append(f"leaf means: want (1.0, 2.0) got ({lv}, {rv})")
    if abs(m.predict_stump((3.0, 0.0), feat, thr, lv, rv) - 1.0) > 1e-12:
        mismatches.append("predict_stump left side wrong")
    if abs(m.predict_stump((7.0, 0.0), feat, thr, lv, rv) - 2.0) > 1e-12:
        mismatches.append("predict_stump right side wrong")
    _, gb_mse = m.gradient_boost(X, y, n_rounds=60, learning_rate=0.3)
    if not (gb_mse < 1e-9):
        mismatches.append(f"boosted MSE on separable noiseless data: want ~0 got {gb_mse}")
    return {"raised": False, "output": [feat, thr, lv, rv, gb_mse], "reached": True,
            "oracle_run": True, "oracle_truth": [0, 5.0, 1.0, 2.0, "mse->0"],
            "oracle_match": not mismatches,
            "invariant_checks": ["exact_split_recovery", "boosting_converges"],
            "detail": ("; ".join(mismatches) if mismatches else
                       f"exact split (f0 @ 5.0, leaves 1.0/2.0); boosted mse={gb_mse:.2e}")}


# ---- walk_forward_early_stopping: POSITIVE oracle (Illia: PASS — "exemplary harness").
#      Walk-forward logic is script-only -> exact helper truths + the demonstration run
#      live in a subprocess (its own hard U-curve asserts are the semantic check). ----
def probe_walk_forward():
    m = _load("python/data-science/composed_tools/walk_forward_early_stopping.py")
    mismatches = []
    if abs(m.mae([1.0, 2.0], [2.0, 4.0]) - 1.5) > 1e-12:
        mismatches.append("mae([1,2],[2,4]) != 1.5")
    f, thr, lm, rm = m.fit_stump_to_residuals([[1.0], [2.0], [8.0], [9.0]], [1.0, 1.0, 2.0, 2.0])
    if (f, thr, lm, rm) != (0, 5.0, 1.0, 2.0):
        mismatches.append(f"stump recovery: want (0, 5.0, 1.0, 2.0) got {(f, thr, lm, rm)}")
    if abs(m.predict_ensemble([3.0], [(0, 5.0, 1.0, 2.0)] * 3, 0.5) - 1.5) > 1e-12:
        mismatches.append("predict_ensemble: 3 stumps x lr 0.5 x left 1.0 != 1.5")
    # the composed claim, demonstrated live: script must survive its own U-curve asserts
    r = subprocess.run([sys.executable, os.path.join(
        LIB, "python/data-science/composed_tools/walk_forward_early_stopping.py")],
        capture_output=True, text=True, timeout=120)
    if r.returncode != 0 or "PASS" not in r.stdout:
        mismatches.append(f"script asserts failed (rc={r.returncode}): {r.stderr[-200:]}")
    return {"raised": False, "output": [r.returncode, r.stdout.strip()[-60:]], "reached": True,
            "oracle_run": True, "oracle_truth": ["mae=1.5", "(0,5.0,1.0,2.0)", "rc=0+PASS"],
            "oracle_match": not mismatches,
            "invariant_checks": ["helper_exact_truth", "u_curve_asserts_live"],
            "detail": ("; ".join(mismatches) if mismatches else
                       "helpers exact; U-curve demonstration ran with asserts live")}


# ---- log_rank_test: POSITIVE oracle (Illia: PASS). Hand-computed tiny case
#      (z = 0.5/sqrt(7/12)) + two mathematical invariants: identical groups -> (0, 1);
#      swapping groups exactly negates z. ----
def probe_log_rank():
    m = _load("python/data-science/survival_and_reliability/log_rank_test.py")
    fn = m.log_rank_test
    mismatches = []
    # hand computation: g1 t=[1,2] e=[1,1]; g2 t=[1,3] e=[1,1]
    # t=1: y1=2 y2=2 d=2 -> o1=1, e1=1.0, var+=16/48;  t=2: y1=1 y2=1 d=1 -> o1=2, e1=1.5, var+=1/4
    z, p = fn([1.0, 2.0], [1, 1], [1.0, 3.0], [1, 1])
    z_want = 0.5 / math.sqrt(7.0 / 12.0)
    p_want = math.erfc(z_want / math.sqrt(2.0))   # two-tailed, independent identity
    if abs(z - z_want) > 1e-9: mismatches.append(f"z: want {z_want:.6f} got {z:.6f}")
    if abs(p - p_want) > 1e-6: mismatches.append(f"p: want {p_want:.6f} got {p:.6f}")
    z0, p0 = fn([1.0, 2.0, 3.0], [1, 1, 1], [1.0, 2.0, 3.0], [1, 1, 1])
    if abs(z0) > 1e-12 or abs(p0 - 1.0) > 1e-12:
        mismatches.append(f"identical groups: want (0, 1.0) got ({z0}, {p0})")
    za, _ = fn([1.0, 2.0], [1, 1], [1.0, 3.0], [1, 1])
    zb, _ = fn([1.0, 3.0], [1, 1], [1.0, 2.0], [1, 1])
    if abs(za + zb) > 1e-9:
        mismatches.append(f"group-swap must negate z: {za:.6f} vs {zb:.6f}")
    return {"raised": False, "output": [z, p, z0, p0], "reached": True,
            "oracle_run": True, "oracle_truth": [z_want, p_want, 0.0, 1.0],
            "oracle_match": not mismatches,
            "invariant_checks": ["hand_computed_z", "null_identity", "antisymmetry"],
            "detail": ("; ".join(mismatches) if mismatches else
                       f"hand z={z_want:.4f} exact; null (0,1) exact; antisymmetry holds")}


# ---- inverse_transform_sampling: LIVE is FIXED (rate>0 guard + round-trip oracle -> PASS);
#      BROKEN fixture keeps the silent-negative-waiting-time defect (-> INVALID). ----
def _inv_transform_defect(m):
    r = _call(m.exponential_inverse_cdf, 0.5, -2.0)   # valid u, impossible rate
    out = r.get("output")
    return (not r["raised"]) and isinstance(out, float) and math.isfinite(out) and out < 0, out

def probe_inverse_transform():   # LIVE (fixed): rate<0 raises + F(Finv(u))==u positive oracle -> PASS
    m = _load("python/data-science/information_theory_and_probability/inverse_transform_sampling.py")
    guarded = _call(m.exponential_inverse_cdf, 0.5, -2.0)["raised"]   # bad rate must now raise
    # positive oracle: the exponential inverse-CDF must invert its CDF F(x)=1-exp(-rate*x)
    rt = all(abs((1 - math.exp(-2.0 * m.exponential_inverse_cdf(u, 2.0))) - u) < 1e-9
             for u in (0.1, 0.3, 0.5, 0.7, 0.9))
    ok = guarded and rt
    return {"raised": False, "output": [guarded, rt], "reached": True,
            "oracle_run": True, "oracle_truth": "F(Finv(u))==u for exponential",
            "oracle_match": ok, "invariant_checks": ["rate_guarded", "cdf_inverse_roundtrip"],
            "detail": f"rate<0 guarded={guarded}; F(Finv(u))==u round-trip={rt}"}

def probe_inverse_transform_BROKEN():   # FIXTURE: silent negative waiting-time -> INVALID
    m = _load_fixture("inverse_transform_sampling.BROKEN.py")
    silent_negative, out = _inv_transform_defect(m)
    return {"raised": False, "output": out, "reached": True,
            "invariant_broken": silent_negative,
            "invariant_checks": ["exp_sample_nonneg_for_any_accepted_rate"],
            "conclusive_kill": silent_negative, "kill_reason": "silent_negative_waiting_time_on_rate_lt_0",
            "detail": f"u=0.5, rate=-2.0 -> {out!r} (silent negative, no raise)"}


# ---- ttl_cache: LIVE FIXED (size() truthful + purge() + ttl guard -> PASS);
#      BROKEN fixture keeps the size()-docstring-lie (-> FLAG, STRONG-FLAG). ----
def _ttl_size_after_expiry(m):
    clock = m.LogicalClock()
    cache = m.ttl_cache(ttl_seconds=100, clock=clock)
    for k in ("a", "b", "c"):
        cache.set(k, k)
    clock.advance(200)                  # all 3 now expired; deliberately no get() calls
    return cache.size(), len(cache.cache)   # (claimed non-expired, resident)

def probe_ttl_cache():   # LIVE (fixed): size()==live count (0) + ttl guard -> PASS
    m = _load("python/system-administration/secrets-credentials/ttl_cache.py")
    claimed, _ = _ttl_size_after_expiry(m)
    truthful = (claimed == 0)          # positive oracle: size() equals the true live count
    guarded = _call(m.ttl_cache, -5)["raised"]   # ttl<=0 must raise
    ok = truthful and guarded
    return {"raised": False, "output": claimed, "reached": True,
            "oracle_run": True, "oracle_truth": "size() == count of non-expired items (0 after expiry)",
            "oracle_match": ok, "invariant_checks": ["size_equals_live_count", "ttl_guarded"],
            "detail": f"3 keys ttl=100 clock+200: size()={claimed} (truth 0, truthful={truthful}); ttl<0 guarded={guarded}"}

def probe_ttl_cache_BROKEN():   # FIXTURE: size() lies (returns 3 for 0 live) -> FLAG
    m = _load_fixture("ttl_cache.BROKEN.py")
    claimed, leaked = _ttl_size_after_expiry(m)
    lie = (claimed != 0)
    return {"raised": False, "output": claimed, "reached": True,
            "invariant_broken": lie,    # KILL_or_FLAG -> FLAG (STRONG-FLAG, not INVALID)
            "invariant_checks": ["size_equals_live_count"],
            "detail": f"size() claims {claimed} non-expired (truth 0); {leaked} expired resident"}


# ============ NON-PYTHON PROBES (subprocess-based; compile/run with probe-owned harness) ============

def _rust_harness(relpath, extra_main, fixture=False):
    """Compile pattern source with its main renamed to pattern_main + a probe-authored
    main appended, run it. fixture=True loads from regression_fixtures/ (broken snapshots)."""
    path = os.path.join(FIXTURES, relpath) if fixture else os.path.join(LIB, relpath)
    src = open(path, encoding="utf-8").read()
    src = src.replace("fn main()", "fn pattern_main()") + "\n" + extra_main
    d = tempfile.mkdtemp(prefix="aura_probe_")
    p = os.path.join(d, "probe.rs")
    open(p, "w", encoding="utf-8").write(src)
    exe = os.path.join(d, "probe")
    c = subprocess.run(["rustc", "-O", "--edition", "2021", "-A", "warnings", "-o", exe, p],
                       capture_output=True, text=True, timeout=180)
    if c.returncode != 0:
        return {"compile_err": c.stderr[-400:]}
    r = subprocess.run([exe], capture_output=True, text=True, timeout=60)
    return {"rc": r.returncode, "out": r.stdout, "err": r.stderr[-400:]}


def _rust_result(relpath, extra_main, truth_note, invariants):
    h = _rust_harness(relpath, extra_main)
    if "compile_err" in h:
        return {"raised": True, "error_text": f"harness compile failed: {h['compile_err']}",
                "output": None, "reached": False, "detail": h["compile_err"]}
    ok = (h["rc"] == 0 and "ORACLE_OK" in h["out"])
    return {"raised": False, "output": h["out"].strip()[-120:], "reached": True,
            "oracle_run": True, "oracle_truth": truth_note, "oracle_match": ok,
            "invariant_checks": invariants,
            "detail": (h["out"].strip()[-160:] if ok else
                       f"rc={h['rc']} out={h['out'].strip()[-100:]} err={h['err'][-160:]}")}


# ---- rendezvous_hash_hrw.rs: POSITIVE oracle (Illia: PASS). The pattern's own test only
#      checks removed-node keys go ELSEWHERE; the HRW LAW's strong half is that every
#      OTHER key must not move at all. Probe checks both directions over 1000 keys. ----
def probe_rendezvous_hash():
    return _rust_result("rust/networking-resilience/rendezvous_hash_hrw.rs", '''
fn main() {
    let full = RendezvousHashHRW::new(vec![0,1,2], 42);
    let mut reduced = RendezvousHashHRW::new(vec![0,1,2], 42);
    reduced.remove(0);
    let (mut on0, mut moved_non0) = (0u32, 0u32);
    for key in 0..1000u64 {
        let b = full.get(key).unwrap();
        let a = reduced.get(key).unwrap();
        if b == 0 { on0 += 1; assert!(a != 0, "key still on removed node"); }
        else if a != b { moved_non0 += 1; }
    }
    assert!(on0 > 0, "some keys must live on node 0");
    assert_eq!(moved_non0, 0, "HRW LAW: only removed-node keys may remap");
    let base = RendezvousHashHRW::new(vec![0,1], 42);
    let mut grown = RendezvousHashHRW::new(vec![0,1], 42);
    grown.add(2);
    let (mut to_new, mut illegal) = (0u32, 0u32);
    for key in 0..1000u64 {
        let b = base.get(key).unwrap();
        let a = grown.get(key).unwrap();
        if a != b { if a == 2 { to_new += 1; } else { illegal += 1; } }
    }
    assert_eq!(illegal, 0, "HRW LAW: add may only pull keys to the NEW node");
    assert!(to_new > 0, "new node must receive some keys");
    pattern_main();
    println!("ORACLE_OK minimal-disruption both directions (1000 keys), to_new={}", to_new);
}''', "HRW minimal-disruption law: remove moves ONLY that node's keys; add pulls ONLY to new node",
        ["remove_minimal_disruption", "add_only_to_new_node"])


# ---- checkpoint_resume_crc.rs: POSITIVE oracle (Illia: PASS). Probe-owned layout with
#      DIFFERENT parameters than the demo (12 recs, ckpt-4, torn rec 9) so the oracle
#      is independent arithmetic, not an echo of the self-test. ----
def probe_checkpoint_crc():
    return _rust_result("rust/composed-systems/checkpoint_resume_crc.rs", '''
fn main() {
    let mut log = CheckpointLog::new();
    for i in 0..12 { log.append_and_checkpoint(format!("r{:02}", i).as_bytes(), 4); }
    let buf = log.serialize();
    assert_eq!(buf.len(), 144, "layout: 12 frames x 11 + 3 checkpoint markers x 4");
    let mut crashed = buf.clone();
    crashed.truncate(112);            // 5 bytes into record 9 frame (starts at 107)
    let rec = CheckpointLog::recover_from(&crashed);
    assert_eq!(rec.len(), 9, "exactly r00..r08 recover; torn r09 dropped");
    for i in 0..9 { assert_eq!(rec[i], format!("r{:02}", i).as_bytes().to_vec(), "exact, once"); }
    let mut corrupted = buf.clone();
    corrupted[2*11 + 4] ^= 0x01;      // flip a data byte inside record 2
    assert_eq!(CheckpointLog::recover_from(&corrupted).len(), 2, "CRC halts at r02");
    assert_eq!(CheckpointLog::recover_from(&[]).len(), 0, "empty image");
    pattern_main();
    println!("ORACLE_OK independent layout: 9-exact-once after torn r09; CRC halt at 2");
}''', "exactly-once recovery on probe-owned layout (12 recs/ckpt-4/torn r09) + CRC halt",
        ["exactly_once_after_truncation", "crc_halts_recovery"])


# ---- http_request_line_parser.rs: FLAW oracle (Illia: INVALID, E012 validation-theater).
#      Claims "strict shape validation" yet accepts: empty version number 'HTTP/',
#      non-numeric version, empty header name. Any accept = the encoded kill. ----
_HTTP_RS_MAIN = '''
fn main() {
    pattern_main();
    let mut accepted: Vec<String> = Vec::new();
    if HttpParser::parse_request_line("GET /path HTTP/").is_ok() {
        accepted.push("version 'HTTP/' with EMPTY number".into());
    }
    if HttpParser::parse_request_line("GET /path HTTP/one.two").is_ok() {
        accepted.push("non-numeric version 'HTTP/one.two'".into());
    }
    if HttpParser::parse_headers(": no-name").map(|h| !h.is_empty() && h[0].0.is_empty()).unwrap_or(false) {
        accepted.push("EMPTY header name ': no-name'".into());
    }
    // the fixed parser must STILL accept a well-formed request line (no over-rejection)
    let good = HttpParser::parse_request_line("GET /index.html HTTP/1.1").is_ok();
    if accepted.is_empty() && good { println!("ORACLE_OK strict + well-formed accepted"); }
    else { println!("THEATER: {} good={}", accepted.join(" | "), good); }
}'''

def probe_http_parser():   # LIVE (fixed): malformed rejected + well-formed accepted -> PASS
    h = _rust_harness("rust/parsing-protocols/http_request_line_parser.rs", _HTTP_RS_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-160:], "reached": True,
            "oracle_run": True, "oracle_truth": "malformed rejected + well-formed accepted",
            "oracle_match": ok, "invariant_checks": ["strict_validation_claim_vs_accepts"],
            "detail": h["out"].strip()[-200:]}

def probe_rle_broken():   # FIXTURE: rle_decode panics on empty input -> FLAG (roundtrip defect)
    h = _rust_harness("compressed_block_store.BROKEN.rs", '''
fn main() {
    let e = rle_encode(&[]);
    let _ = rle_decode(&e);   // empty input: encoded.len()-1 underflows -> OOB panic
    println!("NO_PANIC");
}''', fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    panicked = h["rc"] != 0
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": panicked, "invariant_checks": ["rle_decode_empty_safe"],
            "detail": (f"rle_decode(rle_encode([])) PANICS rc={h['rc']}: {h['err'][-100:]}" if panicked
                       else "no panic")}

# ---- ini_config_parser.rs: ORDER-NONDETERMINISM (found 2026-07-23 by the round-trip oracle;
# the pattern's own `contains`-only asserts could not see it). Fix-channel: HashMap -> BTreeMap.
# Probe main drives MANY sections so two independent instances colliding on the same HashMap
# iteration order is vanishingly unlikely (1/N!) — the kill-test is reliable, not flaky.
_INI_RS_MAIN = '''
fn main() {
    let cfg = "[alpha]\\na=1\\n[bravo]\\nb=2\\n[charlie]\\nc=3\\n[delta]\\nd=4\\n\
[echo]\\ne=5\\n[foxtrot]\\nf=6\\n[golf]\\ng=7\\n[hotel]\\nh=8\\n[india]\\ni=9\\n[juliet]\\nj=10\\n";
    let mut diverged = 0;
    let mut trials = 0;
    let mut first = String::new();
    for t in 0..20 {
        let mut p = IniConfig::new(); p.parse(cfg);
        let s = p.serialize();
        if t == 0 { first = s.clone(); }
        trials += 1;
        if s != first { diverged += 1; }
    }
    // fixed point: re-parsing our own output must reproduce it byte-for-byte
    let mut p0 = IniConfig::new(); p0.parse(cfg);
    let s0 = p0.serialize();
    let mut p1 = IniConfig::new(); p1.parse(&s0);
    let fixed_point = p1.serialize() == s0;
    // values survive the round-trip
    let vals_ok = p1.get("alpha","a")==Some("1") && p1.get("juliet","j")==Some("10")
               && p1.sections.len()==10;
    println!("INI diverged={} trials={} fixed_point={} vals_ok={}",
             diverged, trials, fixed_point, vals_ok);
}'''


def probe_ini_config():   # LIVE: BTreeMap -> serialize deterministic + fixed point -> PASS
    h = _rust_harness("rust/parsing-protocols/ini_config_parser.rs", _INI_RS_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None,
                "reached": False, "detail": h["compile_err"]}
    out = h["out"]
    stable = "diverged=0 " in out
    fixed_point = "fixed_point=true" in out
    vals_ok = "vals_ok=true" in out
    ok = stable and fixed_point and vals_ok and h["rc"] == 0
    return {"raised": False, "output": out.strip()[-160:], "reached": True,
            "oracle_run": True,
            "oracle_truth": "serialize() byte-identical across 20 independent parses "
                            "(canonical order) + re-parse fixed point + values preserved",
            "oracle_match": ok,
            "invariant_checks": ["serialize_deterministic", "serialize_fixed_point",
                                 "roundtrip_values_preserved"],
            "detail": out.strip()[-200:]}


def probe_ini_config_BROKEN():   # FIXTURE: HashMap order -> serialize nondeterministic -> INVALID
    h = _rust_harness("ini_config_parser.BROKEN.rs", _INI_RS_MAIN, fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None,
                "reached": False, "detail": h["compile_err"]}
    out = h["out"]
    nondet = ("diverged=0 " not in out) or ("fixed_point=false" in out)
    return {"raised": False, "output": out.strip()[-160:], "reached": True,
            "invariant_broken": nondet,
            "invariant_checks": ["serialize_deterministic"],
            "conclusive_kill": nondet,
            "kill_reason": "serialize_order_nondeterministic_hashmap",
            "detail": out.strip()[-200:]}


def probe_http_parser_BROKEN():   # FIXTURE: validation theater, malformed accepted -> INVALID
    h = _rust_harness("http_request_line_parser.BROKEN.rs", _HTTP_RS_MAIN, fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    theater = "THEATER:" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-160:], "reached": True,
            "invariant_broken": theater, "invariant_checks": ["strict_validation_claim_vs_accepts"],
            "conclusive_kill": theater, "kill_reason": "validation_theater_malformed_accepted",
            "detail": h["out"].strip()[-200:]}


# ---- atomic_spinlock.rs: THIRD-BOUNDARY probe (Illia: FLAG). Run the real 8-thread
#      contention test: lost updates -> KILL; success is still capped at FLAG because
#      memory-ordering is UN-RUNNABLE (needs a model-checker, not execution). ----
def probe_atomic_spinlock():
    h = _rust_harness("rust/concurrency-resilience/atomic_spinlock.rs", '''
fn main() { pattern_main(); println!("ORACLE_OK execution-half held"); }''')
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None,
                "reached": False, "detail": h["compile_err"]}
    lost = h["rc"] != 0
    return {"raised": False, "output": h["out"].strip()[-120:], "reached": True,
            "conclusive_kill": lost, "kill_reason": "lost_updates_under_contention",
            "concurrency_ordering": True,   # third boundary: caps at FLAG even on success
            "invariant_checks": ["contention_exactness_8x1000"],
            "detail": (f"LOST UPDATES rc={h['rc']}: {h['err'][-140:]}" if lost else
                       f"8x1000 exact under contention; ordering un-runnable -> capped FLAG")}


# ---- R patterns: self-oracle scripts (stopifnot vs lm()/t.test() = R's reference
#      implementations). Probe = run live twice (determinism) + guard the R-wave-3
#      evasion (incident #13: comment-out-the-assert). ----
def _r_script_probe(relpath, expect, truth_note):
    src = open(os.path.join(LIB, relpath), encoding="utf-8").read()
    live_asserts = [ln for ln in src.splitlines() if ln.strip().startswith("stopifnot")]
    r1 = subprocess.run(["Rscript", os.path.join(LIB, relpath)], capture_output=True, text=True, timeout=120)
    r2 = subprocess.run(["Rscript", os.path.join(LIB, relpath)], capture_output=True, text=True, timeout=120)
    ok = (r1.returncode == 0 and expect in r1.stdout
          and r1.stdout == r2.stdout and len(live_asserts) >= 1)
    why = [] if ok else [f"rc={r1.returncode}", f"expect '{expect}' in out: {expect in r1.stdout}",
                         f"deterministic: {r1.stdout == r2.stdout}",
                         f"live stopifnot: {len(live_asserts)}", r1.stderr.strip()[-120:]]
    return {"raised": False, "output": r1.stdout.strip()[-120:], "reached": True,
            "oracle_run": True, "oracle_truth": truth_note, "oracle_match": ok,
            "invariant_checks": [f"live_stopifnot:{len(live_asserts)}", "deterministic_double_run"],
            "detail": ("; ".join(why) if not ok else
                       f"{len(live_asserts)} live stopifnot vs reference; deterministic x2; {r1.stdout.strip()}")}

def probe_linreg_r():
    return _r_script_probe("r/regression_and_glm/linear_regression_normal_eq.R",
                           "linear_regression_normal_eq.R PASS",
                           "normal-equation betas == lm() reference @1e-8 (stopifnot live)")

def probe_welch_r():
    return _r_script_probe("r/hypothesis_testing_parametric/welch_t_test.R",
                           "welch_t_test.R PASS",
                           "manual t/df/p == t.test() reference @1e-8 (stopifnot live)")


# ============ CPP TWIN PROBES (twin-transfer law: VERIFY, never assume) ============

def _cpp_harness(relpath, extra_main, fixture=False):
    """Compile pattern .cpp with its main renamed to pattern_main + probe-authored main.
    fixture=True loads from regression_fixtures/ instead of the library (broken snapshots)."""
    path = os.path.join(FIXTURES, relpath) if fixture else os.path.join(LIB, relpath)
    src = open(path, encoding="utf-8").read()
    src = src.replace("int main(", "int pattern_main(") + "\n" + extra_main
    d = tempfile.mkdtemp(prefix="aura_probe_cpp_")
    p = os.path.join(d, "probe.cpp")
    open(p, "w", encoding="utf-8").write(src)
    exe = os.path.join(d, "probe")
    c = subprocess.run(["g++", "-std=c++17", "-O2", "-w", "-o", exe, p],
                       capture_output=True, text=True, timeout=180)
    if c.returncode != 0:
        return {"compile_err": c.stderr[-400:]}
    r = subprocess.run([exe], capture_output=True, text=True, timeout=60)
    return {"rc": r.returncode, "out": r.stdout, "err": r.stderr[-400:]}


# ---- bayes_factor.cpp: INVALID twin (wrong-math inherited; behavioral-diff confirmed).
#      Same brute-force integration truth as the python probe, computed IN the harness:
#      code uses y_mean^2*n/denom where the conjugate form needs (sum y)^2*tau2/denom. ----
_BF_CPP_MAIN = '''
#include <cstdio>
int main() {
    pattern_main();
    std::vector<double> data(30, 2.0);
    double code = bayes_factor_normal(data, 1.0);
    // brute-force ground truth by numeric integration (log-space)
    int steps = 200000; double lo = -50, hi = 50, dt = (hi-lo)/steps;
    std::vector<double> logs(steps);
    for (int i = 0; i < steps; ++i) {
        double th = lo + (i + 0.5) * dt;
        double lp = -0.5*th*th - 0.5*std::log(2*M_PI);
        double ll = 0.0;
        for (double y : data) ll += -0.5*(y-th)*(y-th) - 0.5*std::log(2*M_PI);
        logs[i] = lp + ll;
    }
    double M = *std::max_element(logs.begin(), logs.end());
    double s = 0.0; for (double l : logs) s += std::exp(l - M);
    double log_m1 = M + std::log(s * dt);
    double log_m0 = 0.0;
    for (double y : data) log_m0 += -0.5*y*y - 0.5*std::log(2*M_PI);
    double log10_diff = std::abs((std::log(std::max(code,1e-300)) - (log_m1 - log_m0)) / std::log(10.0));
    if (log10_diff < 1.0) std::printf("ORACLE_OK code=%g\\n", code);
    else std::printf("WRONG_MATH code=%g truth_logBF=%g off_by_10^%.0f\\n", code, log_m1-log_m0, log10_diff);
    return 0;
}'''

def probe_bayes_factor_cpp():   # LIVE (fixed): brute-force match -> PASS
    h = _cpp_harness("cpp/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.cpp", _BF_CPP_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "brute_force_integration", "oracle_match": ok,
            "invariant_checks": ["brute_force_integration_truth"], "detail": h["out"].strip()[-180:]}

def probe_bayes_factor_cpp_BROKEN():   # FIXTURE (wrong-math snapshot) -> INVALID
    h = _cpp_harness("bayes_factor_normal_means.BROKEN.cpp", _BF_CPP_MAIN, fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    wrong = "WRONG_MATH" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": wrong, "invariant_checks": ["brute_force_integration_truth"],
            "conclusive_kill": wrong, "kill_reason": "wrong_math_inherited_from_python_twin",
            "detail": h["out"].strip()[-180:]}


# ---- stacking_ensemble.cpp: LIVE FIXED (NaN throws -> PASS); BROKEN fixture keeps
#      the silent NaN-into-std::sort UB (-> INVALID). ----
_STACKING_CPP_MAIN = '''
#include <cstdio>
#include <stdexcept>
int main() {
    pattern_main();
    BaseModel1 poisoned_m;
    std::vector<std::pair<double,double>> Xn = {{std::nan(""),2.0},{3.0,4.0},{5.0,6.0}};
    std::vector<int> y = {0,1,0};
    bool threw = false;
    try { poisoned_m.fit(Xn, y); } catch (const std::exception&) { threw = true; }
    if (threw) { std::printf("NAN_GUARDED\\n"); return 0; }
    auto preds = poisoned_m.predict(Xn);
    bool finite = true;
    for (double p : preds) if (!std::isfinite(p)) finite = false;
    if (finite) std::printf("NAN_SILENT poisoned_threshold=%g\\n", poisoned_m.threshold);
    else std::printf("NAN_SURFACED\\n");
    return 0;
}'''

def probe_stacking_cpp():   # LIVE (fixed): NaN throws -> PASS
    h = _cpp_harness("cpp/data-science/ensembles_robust_methods/stacking_ensemble.cpp", _STACKING_CPP_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    guarded = "NAN_GUARDED" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "NaN feature rejected (guarded)", "oracle_match": guarded,
            "invariant_checks": ["nan_poison_must_surface"], "detail": h["out"].strip()[-180:]}

def probe_stacking_cpp_BROKEN():   # FIXTURE: NaN trained silently -> INVALID
    h = _cpp_harness("stacking_ensemble.BROKEN.cpp", _STACKING_CPP_MAIN, fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    silent = "NAN_SILENT" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": silent, "invariant_checks": ["nan_poison_must_surface"],
            "conclusive_kill": silent, "kill_reason": "nan_trained_silently_inherited",
            "detail": h["out"].strip()[-180:]}


# ---- log_rank_test.cpp: FLAG twin. Math half VERIFIED (hand z = 0.5/sqrt(7/12), same
#      truth as the python probe); mismatch half is the inherited hole — python threw
#      IndexError, cpp has NO length guard so mismatch = UB (garbage OR crash, both
#      undefined). invariant_broken either way; kill only if the MATH is wrong. ----
_LR_CPP_MAIN = '''
#include <cstdio>
#include <stdexcept>
int main() {
    pattern_main();
    auto [z, p] = log_rank_test({1.0,2.0}, {1,1}, {1.0,3.0}, {1,1});
    double z_want = 0.5 / std::sqrt(7.0/12.0);
    bool math_ok = std::abs(z - z_want) < 1e-9;
    // mismatch (events shorter than times) must now be a DEFINED error, not OOB UB
    bool mismatch_guarded = false;
    try { log_rank_test({1.0,2.0,3.0,4.0,5.0}, {1,1}, {1.5,2.5}, {1,1}); }
    catch (const std::exception&) { mismatch_guarded = true; }
    if (math_ok && mismatch_guarded) std::printf("ORACLE_OK z=%g mismatch_guarded\\n", z);
    else std::printf("HOLE math_ok=%d mismatch_guarded=%d\\n", math_ok, mismatch_guarded);
    return 0;
}'''

def probe_log_rank_cpp():   # LIVE (fixed): hand-z exact + mismatch guarded -> PASS
    h = _cpp_harness("cpp/data-science/survival_reliability/log_rank_test.cpp", _LR_CPP_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "hand-computed z exact + length mismatch rejected",
            "oracle_match": ok, "invariant_checks": ["hand_computed_z", "mismatch_needs_defined_error"],
            "detail": h["out"].strip()[-180:]}

def probe_log_rank_cpp_BROKEN():   # FIXTURE: math exact but mismatch = silent OOB-UB -> FLAG
    h = _cpp_harness("log_rank_test.BROKEN.cpp", '''
#include <cstdio>
int main() {
    pattern_main();
    auto [z, p] = log_rank_test({1.0,2.0}, {1,1}, {1.0,3.0}, {1,1});
    double z_want = 0.5 / std::sqrt(7.0/12.0);
    if (std::abs(z - z_want) > 1e-9) { std::printf("MATH_MISMATCH z=%g want=%g\\n", z, z_want); return 0; }
    std::printf("MATH_OK z=%g\\n", z);
    auto [z2, p2] = log_rank_test({1.0,2.0,3.0,4.0,5.0}, {1,1}, {1.5,2.5}, {1,1});
    std::printf("UB_SILENT z=%g p=%g (mismatch accepted, no defined error)\\n", z2, p2);
    return 0;
}''', fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    math_ok = "MATH_OK" in h["out"]
    hole = ("UB_SILENT" in h["out"]) or (math_ok and h["rc"] != 0)
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": hole, "invariant_checks": ["hand_computed_z", "mismatch_needs_defined_error"],
            "conclusive_kill": not math_ok, "kill_reason": "log_rank_math_mismatch",
            "detail": h["out"].strip()[-180:] + (f" [rc={h['rc']}]" if h["rc"] else "")}


# ---- gradient_boosting_stumps.cpp: PASS twin (Illia ruling 2026-07-21: evidence=audit).
#      DIVERGED twin (guards python lacked); exact-split recovery + mse->0 convergence
#      ruled sufficient as the independent audit -> positive oracle, earned PASS. ----
def probe_gradient_boosting_cpp():
    h = _cpp_harness("cpp/data-science/ensembles_robust_methods/gradient_boosting_stumps.cpp", '''
#include <cstdio>
int main() {
    pattern_main();
    std::vector<std::pair<double,double>> X = {{1.0,0.0},{2.0,0.0},{8.0,0.0},{9.0,0.0}};
    std::vector<double> y = {1.0,1.0,2.0,2.0};
    auto [f, thr, lv, rv] = fit_stump(X, y);
    bool exact = (f == 0 && std::abs(thr-5.0) < 1e-12 && std::abs(lv-1.0) < 1e-12 && std::abs(rv-2.0) < 1e-12);
    auto [stumps, mse] = gradient_boost(X, y, 60, 0.3);
    if (exact && mse < 1e-9) std::printf("EVIDENCE_OK exact split, mse=%g\\n", mse);
    else std::printf("MECHANISM_BROKEN f=%d thr=%g lv=%g rv=%g mse=%g\\n", f, thr, lv, rv, mse);
    return 0;
}''')
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None,
                "reached": False, "detail": h["compile_err"]}
    broken = "MECHANISM_BROKEN" in h["out"] or h["rc"] != 0
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": [0, 5.0, 1.0, 2.0, "mse->0"],
            "oracle_match": not broken,
            "invariant_checks": ["exact_split_recovery", "boosting_converges"],
            "conclusive_kill": broken, "kill_reason": "diverged_twin_mechanism_broken",
            "detail": h["out"].strip()[-160:] +
                      " | DIVERGED twin: ruled PASS 2026-07-21 (evidence=audit)"}


# ---- calibration_curve.cpp: FLAW oracle (Illia lean INVALID, ruling PENDING —
#      stays in exam expansion until ruled). Two encoded defects: brier_score OOB on
#      scores/labels mismatch (UB), and garbage labels (7, -3) accepted as
#      "observed frequency" 3.5 — nonsense emitted with full confidence. ----
_CAL_CPP_MAIN = '''
#include <cstdio>
#include <stdexcept>
int main() {
    pattern_main();
    // garbage labels {7,-3} must be REJECTED now
    bool garbage_guarded = false;
    try { std::vector<double> s2 = {0.1, 0.9}; std::vector<int> g = {7, -3}; brier_score(s2, g); }
    catch (const std::exception&) { garbage_guarded = true; }
    // labels shorter than scores must be REJECTED now (was OOB UB)
    bool mismatch_guarded = false;
    try { std::vector<double> s5 = {0.1,0.2,0.3,0.4,0.5}; std::vector<int> l2 = {1,0}; brier_score(s5, l2); }
    catch (const std::exception&) { mismatch_guarded = true; }
    if (garbage_guarded && mismatch_guarded) std::printf("ORACLE_OK both guarded\\n");
    else std::printf("HOLE garbage_guarded=%d mismatch_guarded=%d\\n", garbage_guarded, mismatch_guarded);
    return 0;
}'''

def probe_calibration_curve_cpp():   # LIVE (fixed): garbage + mismatch both throw -> PASS
    h = _cpp_harness("cpp/data-science/model_diagnostics/calibration_curve.cpp", _CAL_CPP_MAIN)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "garbage labels + length mismatch both rejected",
            "oracle_match": ok, "invariant_checks": ["labels_must_be_binary", "mismatch_needs_defined_error"],
            "detail": h["out"].strip()[-200:]}

def probe_calibration_curve_cpp_BROKEN():   # FIXTURE: garbage accepted / OOB UB -> INVALID
    h = _cpp_harness("calibration_curve.BROKEN.cpp", '''
#include <cstdio>
int main() {
    pattern_main();
    std::vector<double> s2 = {0.1, 0.9};
    std::vector<int> g = {7, -3};
    auto cal = calibration_curve(s2, g, 2);
    bool nonsense = false;
    for (double f : cal.observed_freqs) if (f > 1.0 || f < 0.0) nonsense = true;
    double bs = brier_score(s2, g);
    if (nonsense || bs > 1.0) std::printf("GARBAGE_ACCEPTED freq0=%g brier=%g\\n",
        cal.observed_freqs.empty() ? -1.0 : cal.observed_freqs[0], bs);
    std::vector<double> s5 = {0.1,0.2,0.3,0.4,0.5};
    std::vector<int> l2 = {1,0};
    double bs2 = brier_score(s5, l2);
    std::printf("UB_SILENT mismatch brier=%g (no defined error)\\n", bs2);
    return 0;
}''', fixture=True)
    if "compile_err" in h:
        return {"raised": True, "error_text": h["compile_err"], "output": None, "reached": False, "detail": h["compile_err"]}
    garbage = "GARBAGE_ACCEPTED" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": garbage or "UB_SILENT" in h["out"] or h["rc"] != 0,
            "invariant_checks": ["labels_must_be_binary", "mismatch_needs_defined_error"],
            "conclusive_kill": garbage, "kill_reason": "garbage_label_accepted_silent_ub_on_mismatch",
            "detail": h["out"].strip()[-200:] + (f" [rc={h['rc']}]" if h["rc"] else "")}


# ============ GO NATIVE PROBES (Illia's hand-audit 2026-07-21, card session batch 1) ============

def _go_harness(relpath, extra_main, fixture=False):
    """Patch pattern main -> patternMain, append probe-authored main, go run in temp dir.
    fixture=True loads from regression_fixtures/ (broken snapshots)."""
    path = os.path.join(FIXTURES, relpath) if fixture else os.path.join(LIB, relpath)
    src = open(path, encoding="utf-8").read()
    src = src.replace("func main()", "func patternMain()", 1) + "\n" + extra_main
    d = tempfile.mkdtemp(prefix="aura_probe_go_")
    p = os.path.join(d, "probe.go")
    open(p, "w", encoding="utf-8").write(src)
    r = subprocess.run(["go", "run", p], capture_output=True, text=True, timeout=120)
    return {"rc": r.returncode, "out": r.stdout, "err": r.stderr[-400:]}


# ---- deadline_ttl.go: STRONG-FLAG (Illia ruling 2026-07-21). NaN TTL = immortal lease
#      (IsExpired always false); clock rewind RESURRECTS an expired lease. Core
#      arithmetic exact on sane inputs -> FLAG for the real reason, not a kill. ----
_DEADLINE_GO_MAIN = '''
func main() {
	defer func(){ if r := recover(); r != nil { fmt.Println("NAN_GUARDED_and_recheck") } }()
	var clockValue float64 = 2000.0
	mock := func() float64 { return clockValue }
	c := NewDeadlineChecker(mock)
	rez := c.SetDeadline(10.0)
	clockValue = 2011.0
	diedOnce := c.IsExpired(rez)
	clockValue = 1990.0
	resurrected := diedOnce && !c.IsExpired(rez)
	if resurrected { fmt.Println("HOLE rewind_resurrection"); return }
	// NaN TTL must now panic (guarded), not create an immortal lease
	z := 0.0
	_ = c.SetDeadline(z / z)
	fmt.Println("HOLE nan_immortal_no_panic")
}'''

def probe_deadline_ttl_go():   # LIVE (fixed): monotonic (no resurrection) + NaN panics -> PASS
    h = _go_harness("go/system-administration/sysadmin/deadline_ttl.go", _DEADLINE_GO_MAIN)
    ok = "NAN_GUARDED" in h["out"]   # reached the NaN check without resurrection, then panicked
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "expiry monotonic on rewind + NaN TTL rejected",
            "oracle_match": ok,
            "invariant_checks": ["nan_ttl_must_not_be_immortal", "expired_stays_expired_on_rewind"],
            "detail": h["out"].strip()[-180:]}

def probe_deadline_ttl_go_BROKEN():   # FIXTURE: NaN immortal + rewind resurrection -> FLAG
    h = _go_harness("deadline_ttl.BROKEN.go", '''
func main() {
	var clockValue float64 = 1000.0
	mock := func() float64 { return clockValue }
	c := NewDeadlineChecker(mock)
	z := 0.0
	nanD := c.SetDeadline(z / z)
	nanImmortal := !c.IsExpired(nanD)
	clockValue = 2000.0
	rez := c.SetDeadline(10.0)
	clockValue = 2011.0
	diedOnce := c.IsExpired(rez)
	clockValue = 1990.0
	resurrected := diedOnce && !c.IsExpired(rez)
	if nanImmortal || resurrected {
		fmt.Println("HOLE nan_immortal:", nanImmortal, "rewind_resurrection:", resurrected)
	} else {
		fmt.Println("ORACLE_OK holes closed")
	}
}''', fixture=True)
    if h["rc"] != 0 and "HOLE" not in h["out"]:
        return {"raised": True, "error_text": h["err"], "output": None, "reached": False, "detail": h["err"]}
    hole = "HOLE" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": hole,
            "invariant_checks": ["nan_ttl_must_not_be_immortal", "expired_stays_expired_on_rewind"],
            "detail": h["out"].strip()[-180:]}


# ---- exponential_backoff.go: INVALID (Illia ruling 2026-07-21). base*2^n Duration
#      math silently wraps to 0 -> backoff VANISHES, failing op hammered at full speed. ----
_BACKOFF_GO_MAIN = '''
func main() {
	defer func(){ if r := recover(); r != nil { fmt.Println("GUARDED", r) } }()
	t0 := time.Now()
	ok, delays, n := exponentialBackoff(func() bool { return false }, 3, 1<<62)
	elapsed := time.Since(t0)
	allZero := true
	for _, d := range delays { if d > 1.0 { allZero = false } }
	if !ok && n == 3 && elapsed < time.Second && allZero {
		fmt.Println("VANISHED backoff on 1<<62 base: delays", delays, "elapsed", elapsed)
	} else {
		fmt.Println("ORACLE_OK")
	}
}'''

def probe_exponential_backoff_go():   # LIVE (fixed): absurd base panics/guarded -> PASS
    h = _go_harness("go/system-administration/sysadmin/exponential_backoff.go", _BACKOFF_GO_MAIN)
    guarded = "GUARDED" in h["out"] or "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "absurd base rejected, backoff cannot vanish",
            "oracle_match": guarded, "invariant_checks": ["overflow_base_must_not_zero_backoff"],
            "detail": h["out"].strip()[-180:]}

def probe_exponential_backoff_go_BROKEN():   # FIXTURE: backoff vanishes on overflow -> INVALID
    h = _go_harness("exponential_backoff.BROKEN.go", _BACKOFF_GO_MAIN, fixture=True)
    if h["rc"] != 0:
        return {"raised": True, "error_text": h["err"], "output": None, "reached": False, "detail": h["err"]}
    gone = "VANISHED" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": gone, "invariant_checks": ["overflow_base_must_not_zero_backoff"],
            "conclusive_kill": gone, "kill_reason": "backoff_vanishes_on_duration_overflow",
            "detail": h["out"].strip()[-180:]}


# ---- csv_validator.go: INVALID (Illia ruling 2026-07-21). NaN/Inf pass float
#      validation with ZERO errors; failed optional coercion leaves a raw STRING in an
#      integer-typed column ("coercions are exact" falsified). ----
_CSV_GO_MAIN = '''
func main() {
	strict := []*FieldSchema{
		{Name: "id", DataType: TypeInteger, Required: true},
		{Name: "name", DataType: TypeString, Required: true},
		{Name: "salary", DataType: TypeFloat, Required: true}}
	res, err := ValidateAndTransformCSV("id,name,salary\\n9,NaNGuy,NaN\\n", strict, ',')
	if err != nil { fmt.Println("HARNESS_ERR", err); return }
	nanPassed := len(res["errors"].([]ValidationError)) == 0 &&
		len(res["rows"].([]map[string]interface{})) == 1
	wide := []*FieldSchema{strict[0], strict[1],
		{Name: "age", DataType: TypeInteger, Required: false}, strict[2]}
	res2, _ := ValidateAndTransformCSV("id,name,age,salary\\n6,Mix,abc,1.0\\n", wide, ',')
	rows2 := res2["rows"].([]map[string]interface{})
	mixed := false
	if len(rows2) == 1 {
		_, mixed = rows2[0]["age"].(string)
	}
	if nanPassed || mixed {
		fmt.Println("THEATER nan_validated:", nanPassed, "string_in_int_column:", mixed)
	} else {
		fmt.Println("ORACLE_OK")
	}
}'''

def probe_csv_validator_go():   # LIVE (fixed): NaN rejected + no mixed-type column -> PASS
    h = _go_harness("go/programming/io/csv_validator.go", _CSV_GO_MAIN)
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "NaN fails float validation + typed columns stay typed",
            "oracle_match": ok, "invariant_checks": ["nan_inf_must_fail_float_validation", "typed_columns_stay_typed"],
            "detail": h["out"].strip()[-180:]}

def probe_csv_validator_go_BROKEN():   # FIXTURE: NaN validated + mixed-type column -> INVALID
    h = _go_harness("csv_validator.BROKEN.go", _CSV_GO_MAIN, fixture=True)
    if h["rc"] != 0 and "THEATER" not in h["out"]:
        return {"raised": True, "error_text": h["err"], "output": None, "reached": False, "detail": h["err"]}
    theater = "THEATER" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": theater,
            "invariant_checks": ["nan_inf_must_fail_float_validation", "typed_columns_stay_typed"],
            "conclusive_kill": theater, "kill_reason": "nan_passes_validation_and_mixed_type_columns",
            "detail": h["out"].strip()[-180:]}


# ---- circuit_breaker.go: INVALID (Illia ruling 2026-07-21). failureCount never resets
#      on success in CLOSED -> cumulative-forever threshold: a 50%-healthy service trips
#      permanently OPEN. The breaker manufactures the outage it should prevent. ----
_BREAKER_GO_MAIN = '''
func main() {
	clk := func() float64 { return 0.0 }
	mix := &circuitBreaker{failureThreshold: 3, recoveryTimeout: 5.0,
		expectedError: func(err error) bool { return err != nil },
		name: "probe", state: closed, now: clk}
	fail := func() (string, error) { return "", &connectionError{msg: "x"} }
	okf := func() (string, error) { return "ok", nil }
	mix.call(fail); mix.call(okf); mix.call(fail); mix.call(okf); mix.call(fail)
	if mix.state == open {
		fmt.Println("CUMULATIVE_TRIP open after fail,ok,fail,ok,fail (success never resets count)")
	} else {
		fmt.Println("ORACLE_OK consecutive counting")
	}
}'''

def probe_circuit_breaker_go():   # LIVE (fixed): 50%-healthy stays CLOSED -> PASS
    h = _go_harness("go/programming/resilience/circuit_breaker.go", _BREAKER_GO_MAIN)
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "success resets failure run (consecutive counting)",
            "oracle_match": ok, "invariant_checks": ["success_must_reset_or_window_failure_count"],
            "detail": h["out"].strip()[-180:]}

def probe_circuit_breaker_go_BROKEN():   # FIXTURE: cumulative count trips 50%-healthy -> INVALID
    h = _go_harness("circuit_breaker.BROKEN.go", _BREAKER_GO_MAIN, fixture=True)
    if h["rc"] != 0 and "CUMULATIVE_TRIP" not in h["out"]:
        return {"raised": True, "error_text": h["err"], "output": None, "reached": False, "detail": h["err"]}
    trip = "CUMULATIVE_TRIP" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": trip,
            "invariant_checks": ["success_must_reset_or_window_failure_count"],
            "conclusive_kill": trip, "kill_reason": "cumulative_count_trips_on_nonconsecutive_failures",
            "detail": h["out"].strip()[-180:]}


# ---- bloom_filter.go: STRONG-FLAG (Illia ruling 2026-07-21). Resize clears bits but
#      keeps itemCount -> analytic FPR describes a filter that no longer exists
#      (ttl_cache size()-lie kin). Core contract (no false negatives, honest
#      saturation FPR) genuinely holds -> FLAG not kill. ----
_BLOOM_GO_MAIN = '''
func main() {
	bf := NewBloomFilter(1000, 0.01)
	for i := 0; i < 1000; i++ { bf.Add(fmt.Sprintf("x_%d", i)) }
	bf.Resize(2000)
	if bf.itemCount != 0 && bf.FalsePositiveRate() > 0 {
		fmt.Println("STATE_LIE cleared filter reports itemCount", bf.itemCount, "fpr", bf.FalsePositiveRate())
	} else {
		fmt.Println("ORACLE_OK accounting resets with the bits")
	}
}'''

def probe_bloom_filter_go():   # LIVE (fixed): Resize resets itemCount -> PASS
    h = _go_harness("go/programming/data_structures/bloom_filter.go", _BLOOM_GO_MAIN)
    ok = "ORACLE_OK" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "oracle_run": True, "oracle_truth": "itemCount matches cleared state after Resize",
            "oracle_match": ok, "invariant_checks": ["itemCount_matches_cleared_state"],
            "detail": h["out"].strip()[-180:]}

def probe_bloom_filter_go_BROKEN():   # FIXTURE: itemCount lies after Resize -> FLAG
    h = _go_harness("bloom_filter.BROKEN.go", _BLOOM_GO_MAIN, fixture=True)
    if h["rc"] != 0 and "STATE_LIE" not in h["out"]:
        return {"raised": True, "error_text": h["err"], "output": None, "reached": False, "detail": h["err"]}
    lie = "STATE_LIE" in h["out"]
    return {"raised": False, "output": h["out"].strip()[-140:], "reached": True,
            "invariant_broken": lie, "invariant_checks": ["itemCount_matches_cleared_state"],
            "detail": h["out"].strip()[-180:]}


# registry: file -> probe. expandable.
PROBES = {
    "python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py": probe_bayes_factor,
    "FIXTURE:bayes_factor_normal_means.BROKEN.py": probe_bayes_factor_BROKEN,
    "python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py": probe_bayesian_ab,
    "FIXTURE:bayesian_ab_beta.BROKEN.py": probe_bayesian_ab_BROKEN,
    "python/data-science/ensembles_and_robust_methods/stacking_ensemble.py": probe_stacking,
    "FIXTURE:stacking_ensemble.BROKEN.py": probe_stacking_BROKEN,
    "python/data-science/statistical_modeling/power_analysis_sample_size.py": probe_power_analysis,
    "python/system-administration/text-stream-ops/robust_csv_parse.py": probe_robust_csv,
    "python/system-administration/resource-guards/token_bucket_limiter.py": probe_token_bucket,
    "FIXTURE:token_bucket_limiter.BROKEN.py": probe_token_bucket_BROKEN,
    "python/data-science/composed_tools/dedup_pipeline.py": probe_dedup_pipeline,
    "python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py": probe_dirichlet,
    "python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py": probe_gradient_boosting,
    "python/data-science/composed_tools/walk_forward_early_stopping.py": probe_walk_forward,
    "python/data-science/survival_and_reliability/log_rank_test.py": probe_log_rank,
    "python/data-science/information_theory_and_probability/inverse_transform_sampling.py": probe_inverse_transform,
    "FIXTURE:inverse_transform_sampling.BROKEN.py": probe_inverse_transform_BROKEN,
    "python/system-administration/secrets-credentials/ttl_cache.py": probe_ttl_cache,
    "FIXTURE:ttl_cache.BROKEN.py": probe_ttl_cache_BROKEN,
    "rust/networking-resilience/rendezvous_hash_hrw.rs": probe_rendezvous_hash,
    "rust/composed-systems/checkpoint_resume_crc.rs": probe_checkpoint_crc,
    "rust/parsing-protocols/http_request_line_parser.rs": probe_http_parser,
    "FIXTURE:http_request_line_parser.BROKEN.rs": probe_http_parser_BROKEN,
    "FIXTURE:compressed_block_store.BROKEN.rs": probe_rle_broken,
    "rust/parsing-protocols/ini_config_parser.rs": probe_ini_config,
    "FIXTURE:ini_config_parser.BROKEN.rs": probe_ini_config_BROKEN,
    "rust/concurrency-resilience/atomic_spinlock.rs": probe_atomic_spinlock,
    "r/regression_and_glm/linear_regression_normal_eq.R": probe_linreg_r,
    "r/hypothesis_testing_parametric/welch_t_test.R": probe_welch_r,
    "cpp/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.cpp": probe_bayes_factor_cpp,
    "FIXTURE:bayes_factor_normal_means.BROKEN.cpp": probe_bayes_factor_cpp_BROKEN,
    "cpp/data-science/ensembles_robust_methods/stacking_ensemble.cpp": probe_stacking_cpp,
    "FIXTURE:stacking_ensemble.BROKEN.cpp": probe_stacking_cpp_BROKEN,
    "cpp/data-science/survival_reliability/log_rank_test.cpp": probe_log_rank_cpp,
    "FIXTURE:log_rank_test.BROKEN.cpp": probe_log_rank_cpp_BROKEN,
    "cpp/data-science/ensembles_robust_methods/gradient_boosting_stumps.cpp": probe_gradient_boosting_cpp,
    "cpp/data-science/model_diagnostics/calibration_curve.cpp": probe_calibration_curve_cpp,
    "FIXTURE:calibration_curve.BROKEN.cpp": probe_calibration_curve_cpp_BROKEN,
    "go/system-administration/sysadmin/deadline_ttl.go": probe_deadline_ttl_go,
    "FIXTURE:deadline_ttl.BROKEN.go": probe_deadline_ttl_go_BROKEN,
    "go/system-administration/sysadmin/exponential_backoff.go": probe_exponential_backoff_go,
    "FIXTURE:exponential_backoff.BROKEN.go": probe_exponential_backoff_go_BROKEN,
    "go/programming/io/csv_validator.go": probe_csv_validator_go,
    "FIXTURE:csv_validator.BROKEN.go": probe_csv_validator_go_BROKEN,
    "go/programming/resilience/circuit_breaker.go": probe_circuit_breaker_go,
    "FIXTURE:circuit_breaker.BROKEN.go": probe_circuit_breaker_go_BROKEN,
    "go/programming/data_structures/bloom_filter.go": probe_bloom_filter_go,
    "FIXTURE:bloom_filter.BROKEN.go": probe_bloom_filter_go_BROKEN,
}
