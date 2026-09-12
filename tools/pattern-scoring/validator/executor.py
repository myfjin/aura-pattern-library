"""
executor.py — v1.5 GENERIC executor for TRIAGE (not verification). TRIAGES any python pattern:
auto-discovers its entry functions, builds baseline valid args from type hints, fires the 13
recipes, captures real results, and lets the oracle FLAG/SKIP. It cannot PASS (no per-pattern
oracle). No hand-written probe per pattern.

Scale lever for TRIAGE (not verification): fires generic recipes at python patterns to flag
 which SILENTLY ACCEPT domain violations. Without per-pattern oracles it cannot PASS anything —
 it triages for human/oracle review. Definitive verdicts still need hand-probes (see sweep.judge).
Coverage is DERIVED from what actually ran (round-2 hardening) — no human writes coverage flags.
"""
import importlib.util, inspect, io, contextlib, math, os, signal, ast, re
from oracle import classify_signal, verdict_from_signals, derive_coverage

LIB = os.path.expanduser("~/aura-pattern-library")

_CONC_RE = re.compile(r"\b(Atomic\w*|compare_exchange|thread(ing)?\.|Thread\(|Lock\(|"
                      r"Mutex|RwLock|multiprocessing\.|std::thread|std::sync|tokio|rayon|sync\.)\b")
def _scan_concurrency(relpath):  # 4Q #4: apply the third boundary in the generic executor too
    try:
        return bool(_CONC_RE.search(open(os.path.join(LIB, relpath), encoding="utf-8", errors="replace").read()))
    except OSError:
        return False

# ---------- safe module load (module-level demo may run; suppress + time-guard) ----------
class _Timeout(Exception): pass
def _alarm(sec):
    def handler(signum, frame): raise _Timeout()
    signal.signal(signal.SIGALRM, handler); signal.alarm(sec)
def _cancel(): signal.alarm(0)

def load_module(relpath):
    p = os.path.join(LIB, relpath)
    spec = importlib.util.spec_from_file_location("pat_" + str(abs(hash(relpath))), p)
    m = importlib.util.module_from_spec(spec)
    try:
        _alarm(20)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            spec.loader.exec_module(m)
        _cancel()
        return m, None
    except Exception as e:
        _cancel()
        return None, f"{type(e).__name__}: {e}"

# ---------- entry-function discovery ----------
def entry_functions(module, relpath):
    """Public functions defined IN this module (not imports), with >=1 arg. Prefer annotated."""
    fns = []
    src_names = set()
    try:
        tree = ast.parse(open(os.path.join(LIB, relpath), encoding="utf-8", errors="replace").read())
        src_names = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    except Exception:
        pass
    for name, fn in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_") or name not in src_names:
            continue
        try:
            sig = inspect.signature(fn)
        except Exception:
            # py3.14 lazy annotations: a missing typing import (e.g. Tuple) passes
            # health but raises NameError only on introspection (pca_power_iteration find)
            continue
        params = [p for p in sig.parameters.values() if p.kind in
                  (p.POSITIONAL_OR_KEYWORD, p.POSITIONAL_ONLY)]
        if params:
            fns.append((name, fn, sig, params))
    return fns

# ---------- baseline valid-arg builder from type hints ----------
def _valid_for(ann, default, pname=""):
    if default is not inspect.Parameter.empty and default is not None:
        return default, True
    s = str(ann).lower()
    if "list[list" in s: return [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], True
    if "list[int]" in s: return [0, 1, 0, 1, 1, 0], True
    if "list" in s or "sequence" in s or "vector" in s: return [1.0, 2.0, 3.0, 4.0, 5.0], True
    if "tuple" in s: return (1.0, 2.0), True
    if "int" in s: return 5, True
    if "float" in s or "number" in s: return 0.5, True
    if "str" in s: return "the quick brown fox", True
    if "bool" in s: return True, True
    if "dict" in s: return {"a": 1.0, "b": 2.0}, True
    # 5S hole 3: unannotated params -> guess from the NAME (fewer SKIPs).
    n = pname.lower()
    if any(w in n for w in ("data", "samples", "values", "series", "arr", "xs", "ys", "points", "scores", "counts")):
        return [1.0, 2.0, 3.0, 4.0, 5.0], True
    if any(w in n for w in ("text", "name", "key", "line", "doc", "word")):
        return "the quick brown fox", True
    if n in ("x", "y", "z") or any(w in n for w in ("num", "count", "n_", "size", "k", "depth", "width", "seed")):
        return 5, True
    if any(w in n for w in ("prob", "rate", "alpha", "p1", "p2", "u", "var", "mean", "mu", "threshold", "eps", "value", "val")):
        return 0.5, True
    return None, False  # genuinely unknown -> honest SKIP (routed to manual/hand-probe)

def build_baseline(params):
    args, buildable = [], True
    for p in params:
        v, ok = _valid_for(p.annotation, p.default, p.name)
        if not ok: buildable = False
        args.append(v)
    return args, buildable

# ---------- fire one call under guard ----------
def _call(fn, args):
    try:
        _alarm(10)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            out = fn(*args)
        _cancel()
        return {"raised": False, "output": out}
    except _Timeout:
        _cancel(); return {"raised": True, "error_text": "Timeout", "output": None}
    except Exception as e:
        _cancel(); return {"raised": True, "error_text": f"{type(e).__name__}: {e}", "output": None}

# ---------- recipe fixtures over baseline args (generic) ----------
def _finite(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def _finite_or_full(x):  # 5S hole 4: include set/frozenset so degenerate collections count
    return _finite(x) or (isinstance(x,(list,tuple,dict,str,set,frozenset)) and len(x) > 0)
def _has_nan_out(x):
    try:
        if isinstance(x,float): return math.isnan(x) or math.isinf(x)
        if isinstance(x,(list,tuple)): return any(_has_nan_out(v) for v in x)
    except TypeError: return False
    return False

# 4Q finding 2/3: DOMAIN-AWARE attack values — the E001-E009 catalog turned executable.
# map parameter NAME -> semantically-invalid values (the subtle finds -1e9 can't reproduce).
DOMAIN_ATTACKS = [
    (("p1", "p2", "prob", "probability", "p_", "rate_a", "rate_b"), [1.5, -0.5], "E003 prob out of [0,1]"),
    (("alpha", "significance", "level"), [-0.05, 1.5], "E001 alpha out of (0,1)"),
    (("rate", "lambda", "lam", "beta"), [-2.0, 0.0], "E001 rate <= 0"),
    (("u", "quantile", "q", "percentile"), [1.5, 1.0], "E003 u out of [0,1)"),
    (("var", "variance", "sigma", "std", "sd"), [-1.0], "E-B5 variance < 0"),
]
# 5S hole 5: positive-parameter families — any numeric param whose name contains one of these
# stems must be > 0; attack with negative + zero.
POSITIVE_STEMS = ("rate", "size", "capacity", "limit", "timeout", "ttl", "threshold", "window",
                  "step", "decay", "throughput", "tokens_per", "duration", "expiry", "epsilon",
                  "learning", "momentum", "bound", "cutoff", "n_", "num_",
                  # GO batch 1: negative recoveryTimeout made the breaker's fail-fast theater;
                  # negative baseDelay made the backoff vanish. Config-poison params:
                  "recovery", "delay", "backoff", "interval", "attempts", "retries")

# Illia ruling 2026-07-21: params that LEGITIMATELY accept 0 / negative — attacking these
# is a tool false-positive, not a pattern defect. Longitude (0 = prime meridian) + signed
# rates (risk-free / decay / growth / interest / return can be 0 or negative in real markets).
_SIGNED_OK_EXACT = {"lon", "lng", "longitude", "lon1", "lon2", "long"}
_SIGNED_OK_SUFFIX = ("_rate",)   # risk_free_rate, decay_rate, growth_rate, interest_rate
_SIGNED_OK_STEMS = ("longitude", "risk_free", "decay_rate", "growth_rate", "interest_rate",
                    "return", "drift", "log_return")

def _signed_ok(pname):
    pl = pname.lower()
    if pl in _SIGNED_OK_EXACT:
        return True
    if pl.endswith(_SIGNED_OK_SUFFIX) and pl not in ("rate",):
        # a bare "rate"/"lambda" is an exponential rate (>0); "*_rate" compounds are signed-ok
        return True
    return any(s in pl for s in _SIGNED_OK_STEMS)

def _domain_values(pname):
    if _signed_ok(pname):
        return []
    pl = pname.lower()
    vals = []
    for names, vs, _ in DOMAIN_ATTACKS:
        if pl in names or any(pl == n or pl.endswith("_" + n) for n in names):
            vals += vs
    if not vals and any(stem in pl for stem in POSITIVE_STEMS):
        vals += [-1.0]   # positive-param fallback: negative is clearly invalid (0 is often a valid
                          # boundary — timeout=0, epsilon=0 — so 4Q v18 N5: dropped 0.0 to cut false-FLAGs)
    return vals

def attack_fixtures(params, baseline):
    """Generate (recipe, mutated_args, e_class) by replacing ONE arg with an attack value.
    Domain-aware where the param name implies a domain (4Q finding 2/3)."""
    out = []
    numeric_idx = []
    for i, (p, base) in enumerate(zip(params, baseline)):
        s = str(p.annotation).lower()
        def sub(v, _i=i):
            a = list(baseline); a[_i] = v; return a
        if "int" in s or "float" in s or "number" in s:
            numeric_idx.append(i)
            # R2 domain-aware (the subtle finds): probability->1.5, alpha->-0.05, rate->-1, u->1.5
            for dv in _domain_values(p.name):
                out.append(("R2_domain_aware", sub(dv), "E001/E003", i))
            # R1 blunt underflow (still useful for unnamed numerics)
            out.append(("R1_domain_under", sub(-1e9), "E001/E003", i))
            out.append(("R6_wrong_type", sub(None), "E006", i))
            out.append(("R6_wrong_type", sub("сорок два"), "E006", i))
            # R15 scalar NaN/Inf (GO batch 1, csv_validator find): poison into scalar floats.
            # Finite output + no raise = fabricated certainty; NaN output = visible poison.
            if "float" in s or "number" in s:
                out.append(("R15_scalar_nan_inf", sub(float("nan")), "E008", i))
                out.append(("R15_scalar_nan_inf", sub(float("inf")), "E008", i))
            # NOTE R14_int_overflow (E013) deliberately NOT fired here: python ints are
            # arbitrary-precision (class can't exist) and 1<<62 loop-params hang in-process.
            # It lives in recipes.py for the typed-language harness lanes (LANG_PRIORS).
            # R9 degenerate (count param == 0). Single-letter stems k/n must match at a WORD
            # boundary — bare "n" as a substring wrongly hit lon1/mean/min (Illia ruling
            # 2026-07-21: longitude=0 is valid). Multi-char stems keep substring matching.
            _pl = p.name.lower()
            _is_count = (any(w in _pl for w in ("window","breaks","bins","num","order","size","trials","count"))
                         or _pl in ("k", "n") or _pl.startswith(("k_", "n_", "num_"))
                         or _pl.endswith(("_k", "_n")))
            if _is_count and not _signed_ok(_pl):
                out.append(("R9_degenerate_param", sub(0), "E009", i))
        if "list" in s or "vector" in s or "sequence" in s:
            out.append(("R5_no_data", sub([]), "E005", i))
            out.append(("R8_nan_inf_poison", sub([float("nan")]+list(base)[1:] if isinstance(base,list) and base else [float("nan")]), "E008", i))
            out.append(("R6_wrong_type", sub(None), "E006", i))
    # R3 degenerate-equal: make two numeric params equal (zero effect/difference) — E002.
    # 5S/4Q v17: SKIP if the baseline already equalizes them (mutation == baseline, a no-op false-FLAG).
    if len(numeric_idx) >= 2 and baseline[numeric_idx[0]] != baseline[numeric_idx[1]]:
        a = list(baseline); a[numeric_idx[1]] = a[numeric_idx[0]]
        out.append(("R3_degenerate_equal", a, "E002", numeric_idx[0]))
    # R4 cross-param impossible (4Q/5S): part > whole (successes>trials) — E004.
    # 5S/4Q v17: only CLEAR part-whole containment pairs; the generic ("k","n") pair removed (too broad).
    names = [p.name.lower() for p in params]
    for part_stem, whole_stem in (("success", "trial"), ("count", "total"), ("hit", "total")):
        pi = next((i for i, n in enumerate(names) if part_stem in n), None)
        wi = next((i for i, n in enumerate(names) if whole_stem == n or n.startswith(whole_stem)), None)
        if pi is not None and wi is not None and pi != wi \
                and isinstance(baseline[pi], (int, float)) and isinstance(baseline[wi], (int, float)):
            a = list(baseline); a[wi] = 10; a[pi] = 999   # part hugely exceeds whole
            out.append(("R4_cross_param_impossible", a, "E004", pi))
    # R7 shape-mismatch (4Q/5S): two parallel collections of unequal length — E007
    coll_idx = [i for i, (p, b) in enumerate(zip(params, baseline))
                if isinstance(b, list) and "list[list" not in str(p.annotation).lower()]
    if len(coll_idx) >= 2:
        a = list(baseline)
        a[coll_idx[0]] = list(baseline[coll_idx[0]]) + [1.0]   # one longer
        out.append(("R7_shape_mismatch", a, "E007", coll_idx[0]))
        b = list(baseline)
        b[coll_idx[1]] = list(baseline[coll_idx[1]])[:-1] if len(baseline[coll_idx[1]]) > 1 else []
        out.append(("R7_shape_mismatch", b, "E007", coll_idx[1]))
    return out

# ---------- judge one pattern ----------
def evaluate(relpath, verbose=False):
    module, load_err = load_module(relpath)
    if load_err:
        return {"file": relpath, "verdict": "FLAG", "reason": f"load/exec error: {load_err}",
                "oracle_coverage": {}, "detail": "module did not import/run"}
    fns = entry_functions(module, relpath)
    if not fns:
        return {"file": relpath, "verdict": "SKIP", "reason": "no discoverable entry function",
                "detail": "script-only or no annotated public fn"}
    worst = None  # aggregate to the most severe verdict across functions
    detail = []
    order = {"INVALID": 3, "FLAG": 2, "PASS": 1, "SKIP": 0}
    for name, fn, sig, params in fns:
        baseline, buildable = build_baseline(params)
        if not buildable:
            v = {"verdict": "SKIP", "reason": "cannot build valid baseline args"}
            detail.append(f"{name}: SKIP (unbuildable args)")
        else:
            base_result = _call(fn, baseline)
            signals = []
            n_accept = n_reject = n_nan = 0
            # NOTE: no clean_output passed -> the noise-identity KILL (which needs a proper
            # noise-vs-clean probe) does NOT fire in the generic path (round-2 false-KILL fix).
            for recipe, margs, eclass, idx in attack_fixtures(params, baseline):
                r = _call(fn, margs); r["reached"] = True
                out = r.get("output")
                if r["raised"]:
                    n_reject += 1                                   # rejected garbage (loud)
                elif _has_nan_out(out):
                    n_nan += 1                                      # visible poison
                # UNAMBIGUOUS domain violations (prob=1.5 is not a probability, k=0 is nonsense):
                # finite output + no raise = genuine silent acceptance.
                elif recipe in ("R1_domain_under", "R2_domain_aware", "R9_degenerate_param",
                                "R15_scalar_nan_inf") \
                        and _finite_or_full(out):
                    n_accept += 1
                # AMBIGUOUS recipes (5S/4Q v17): equal-params / part>whole / unequal-lists can ALL be
                # VALID input (clamp, non-parallel lists, symmetric fns). Only count when the output is
                # IDENTICAL to baseline -> the input change was truly IGNORED. Never on mere finite output.
                elif recipe in ("R3_degenerate_equal", "R4_cross_param_impossible", "R7_shape_mismatch") \
                        and not r["raised"] and out is not None and out == base_result.get("output") \
                        and _finite_or_full(out) and out not in (0, 0.0, -0.0):
                    # 5S v18: exclude TRIVIAL outputs (0/empty) — a symmetric fn like add(1,-1)==add(0,0)==0
                    # matches by coincidence, not by ignoring input. Require a distinctive matched output.
                    n_accept += 1
                signals.append(classify_signal(r))
            # triage verdict: silent domain acceptance is the actionable risk (Illia ticket001).
            if n_accept > 0:
                signals.append(("silent_domain_acceptance", "FLAG_signal"))
            if n_nan > 0:
                signals.append(("nan_output", "FLAG_signal"))
            cov = derive_coverage(signals, {})   # generic path has no positive oracle -> FLAG floor
            v = verdict_from_signals(signals, cov, harness_ok=True,
                                     concurrency_ordering=_scan_concurrency(relpath))  # 4Q #4
            v["triage"] = {"silently_accepted": n_accept, "rejected": n_reject, "nan": n_nan}
            detail.append(f"{name}: {v['verdict']} [accept={n_accept} reject={n_reject}]")
        if worst is None or order[v["verdict"]] > order[worst["verdict"]]:
            worst = v
    worst = worst or {"verdict": "SKIP", "reason": "all functions skipped"}
    return {"file": relpath, "verdict": worst["verdict"], "reason": worst.get("reason",""),
            "functions": len(fns), "detail": " | ".join(detail[:6])}
