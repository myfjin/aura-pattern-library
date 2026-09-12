"""
recipes.py — the 13 attack recipes (Layer 1 of the validation tool).
Each recipe transforms a pattern's declared inputs into an attack fixture.
Derived from Illia's hand-audit error classes E001-E012. See TOOL_ARCHITECTURE_ANALYSIS.md.

A recipe = f(arg_spec) -> list of {name, args, kind, e_class} attack fixtures.
The tool fires EVERY applicable recipe at EVERY pattern (library mode, not artisan mode).
"""
import math

NAN = float("nan")
INF = float("inf")

# Per-language recipe-prior matrix (5S proposal 5): META-LAW as a measured dial.
# weight ~0 means "compiler already enforces this; don't waste the probe".
# GO batch 1 (2026-07-21) recalibration: "overflow" added — python/R are arbitrary-precision/
# double (class can't exist); typed langs wrap SILENTLY (go Duration -> exactly 0, proven).
# go "nan" RAISED 0.5 -> 1.0: ParseFloat accepts NaN/Inf, csv_validator killed by it.
LANG_PRIORS = {
    "python": {"domain": 1.0, "wrong_type": 1.0, "nan": 1.0, "shape": 1.0, "claim": 1.0, "overflow": 0.0, "stateful": 1.0},
    "r":      {"domain": 1.0, "wrong_type": 1.0, "nan": 1.0, "shape": 1.0, "claim": 1.0, "na_probe": 1.0, "overflow": 0.0, "stateful": 1.0},
    "cpp":    {"domain": 0.5, "wrong_type": 0.3, "nan": 0.7, "shape": 1.0, "claim": 1.2, "ub_probe": 1.0, "overflow": 1.3, "stateful": 1.0},
    "go":     {"domain": 0.3, "wrong_type": 0.2, "nan": 1.0, "shape": 0.8, "claim": 1.3, "nil_probe": 1.0, "overflow": 1.3, "stateful": 1.3},
    "rust":   {"domain": 0.1, "wrong_type": 0.0, "nan": 0.0, "shape": 0.4, "claim": 1.5, "overflow": 1.0, "stateful": 1.0},
}


def _numeric_params(arg_spec):
    return [a for a in arg_spec if a.get("type") in ("float", "int", "number")]

def _collection_params(arg_spec):
    return [a for a in arg_spec if a.get("type", "").lower() in
            ("list", "list[float]", "list[int]", "list[list[float]]", "array", "vector")]


# ---- the 13 recipes. each yields attack fixtures given the manifest arg_spec ----

def R1_domain_under(spec):
    "E001/E003 — push a bounded numeric param below its low bound."
    out = []
    for p in _numeric_params(spec):
        lo = p.get("domain_lo")
        val = (lo - 1) if isinstance(lo, (int, float)) else -1
        out.append({"recipe": "R1_domain_under", "e_class": "E001/E003", "target": p["name"],
                    "value": val, "kind": "domain"})
    return out

def R2_domain_over(spec):
    "E003 — push above high bound (probabilities>1, u>=1)."
    out = []
    for p in _numeric_params(spec):
        hi = p.get("domain_hi")
        if isinstance(hi, (int, float)):
            out.append({"recipe": "R2_domain_over", "e_class": "E003", "target": p["name"],
                        "value": hi + 0.5, "kind": "domain"})
    return out

def R3_degenerate_equal(spec):
    "E002 — make a difference/effect zero (two params equal)."
    nums = _numeric_params(spec)
    if len(nums) >= 2:
        return [{"recipe": "R3_degenerate_equal", "e_class": "E002",
                 "target": [nums[0]["name"], nums[1]["name"]], "value": "equal", "kind": "numeric"}]
    return []

def R4_cross_param_impossible(spec):
    "E004 — violate a joint constraint (successes>trials)."
    # heuristic: any param named successes/count/k vs trials/n/total
    names = [p["name"] for p in spec]
    pairs = [("successes", "trials"), ("successes_a", "trials_a"), ("k", "n"), ("count", "total")]
    out = []
    for a, b in pairs:
        if a in names and b in names:
            out.append({"recipe": "R4_cross_param_impossible", "e_class": "E004",
                        "target": (a, b), "value": "a_exceeds_b", "kind": "domain"})
    return out

def R5_no_data(spec):
    "E005/E008-empty — zero count / empty collection / trials=0."
    out = []
    for p in _collection_params(spec):
        out.append({"recipe": "R5_no_data", "e_class": "E005", "target": p["name"],
                    "value": [], "kind": "empty"})
    for p in _numeric_params(spec):
        if any(w in p["name"] for w in ("trials", "n", "count", "size")):
            out.append({"recipe": "R5_no_data", "e_class": "E005", "target": p["name"],
                        "value": 0, "kind": "empty"})
    return out

def R6_wrong_type(spec):
    "E006 — None / str-for-number / bool. (down-weighted in typed langs by LANG_PRIORS)."
    out = []
    for p in spec:
        out.append({"recipe": "R6_wrong_type", "e_class": "E006", "target": p["name"],
                    "value": None, "kind": "wrong_type"})
        if p.get("type") in ("float", "int", "number"):
            out.append({"recipe": "R6_wrong_type", "e_class": "E006", "target": p["name"],
                        "value": "сорок два", "kind": "wrong_type"})  # wrong-language string
    return out

def R7_shape_mismatch(spec):
    "E007 — unequal-length parallel arrays, BOTH directions."
    cols = _collection_params(spec)
    if len(cols) >= 2:
        return [{"recipe": "R7_shape_mismatch", "e_class": "E007",
                 "target": [cols[0]["name"], cols[1]["name"]], "value": "unequal_len", "kind": "shape"},
                {"recipe": "R7_shape_mismatch", "e_class": "E007",
                 "target": [cols[0]["name"], cols[1]["name"]], "value": "unequal_len_rev", "kind": "shape"}]
    return []

def R8_nan_inf_poison(spec):
    "E008 — inject NaN/inf into a float collection (the purest silent kill)."
    out = []
    for p in _collection_params(spec):
        out.append({"recipe": "R8_nan_inf_poison", "e_class": "E008", "target": p["name"],
                    "value": "inject_nan", "kind": "nan"})
        out.append({"recipe": "R8_nan_inf_poison", "e_class": "E008", "target": p["name"],
                    "value": "inject_inf", "kind": "nan"})
    return out

def R9_degenerate_param(spec):
    "E009 — k=0, window=0, num_breaks=0."
    out = []
    for p in _numeric_params(spec):
        if any(w in p["name"] for w in ("k", "window", "breaks", "bins", "num_", "poly_order")):
            out.append({"recipe": "R9_degenerate_param", "e_class": "E009", "target": p["name"],
                        "value": 0, "kind": "domain"})
    return out

def R10_numeric_oracle(spec, oracle=None):
    "E010 — brute-compute the claimed quantity, compare. Only if a closed-form oracle exists."
    if oracle:
        return [{"recipe": "R10_numeric_oracle", "e_class": "E010", "target": "output",
                 "value": "compare_brute", "kind": "numeric", "oracle": oracle}]
    return []  # no oracle -> honest fall-through to FLAG (5S proposal 1)

def R11_invariant_stress(spec, invariants=None):
    "E011/E012 — push a claimed invariant/guarantee to its edge; claim-falsification."
    out = []
    for inv in (invariants or []):
        out.append({"recipe": "R11_invariant_stress", "e_class": "E011/E012", "target": "invariant",
                    "value": inv, "kind": "claim"})
    return out

def R12_mutation_probe(spec):
    "log_rank find — corrupt a constant/branch, see if any assert notices (tests the TEST)."
    return [{"recipe": "R12_mutation_probe", "e_class": "coverage-gap", "target": "harness",
             "value": "corrupt_guard_constant", "kind": "mutation"}]

def R13_state_sequence(spec, stateful=False):
    """ttl/token/breaker/bloom finds — state-lies-over-time, the sysadmin/resilience kill class.
    Sequences (each one killed or strong-flagged a real pattern):
      idle_then_burst      (token_bucket: unbounded accumulation)
      expire_without_touch (ttl_cache: size() counts the dead)
      clock_rewind         (deadline_ttl: expired lease RESURRECTS on backward clock step)
      alternating_fail_ok  (circuit_breaker: cumulative count trips on non-consecutive fails)
      clear_then_report    (bloom_filter: Resize clears bits, itemCount/FPR describe the ghost)
    Only stateful patterns."""
    if stateful:
        return [{"recipe": "R13_state_sequence", "e_class": "stateful", "target": "sequence",
                 "value": seq, "kind": "stateful"}
                for seq in ("idle_then_burst", "expire_without_touch", "clock_rewind",
                            "alternating_fail_ok", "clear_then_report")]
    return []


def R14_int_overflow(spec):
    """E013 (GO batch 1) — huge int (1<<62) into numeric params: typed langs WRAP SILENTLY
    (go: Duration math -> exactly 0, backoff vanished). Python/R are arbitrary-precision/
    double — LANG_PRIORS weight 0 there (and huge ints hang in-process loops), so this
    recipe fires only through the typed-language harness lanes."""
    out = []
    for p in _numeric_params(spec):
        out.append({"recipe": "R14_int_overflow", "e_class": "E013", "target": p["name"],
                    "value": 1 << 62, "kind": "overflow"})
    return out


def R15_scalar_nan_inf(spec):
    """E008-scalar (GO batch 1) — NaN/Inf into SCALAR float params. csv_validator find:
    stdlib parsers (go ParseFloat, python float()) accept 'NaN'/'Inf' as valid — a
    validator that trusts them validates poison. Finite output from NaN input with no
    raise = fabricated certainty."""
    out = []
    for p in _numeric_params(spec):
        out.append({"recipe": "R15_scalar_nan_inf", "e_class": "E008", "target": p["name"],
                    "value": NAN, "kind": "nan"})
        out.append({"recipe": "R15_scalar_nan_inf", "e_class": "E008", "target": p["name"],
                    "value": INF, "kind": "nan"})
    return out


ALL_RECIPES = [R1_domain_under, R2_domain_over, R3_degenerate_equal, R4_cross_param_impossible,
               R5_no_data, R6_wrong_type, R7_shape_mismatch, R8_nan_inf_poison,
               R9_degenerate_param, R12_mutation_probe,
               R14_int_overflow, R15_scalar_nan_inf]  # R10/R11/R13 need extra args


def fire_all(arg_spec, lang="python", oracle=None, invariants=None, stateful=False, weight_floor=0.15):
    """Fire every applicable recipe, weighted by the per-language prior (META-LAW).
    Recipes whose language-weight is below weight_floor are skipped and RECORDED as
    blocked_by_type_system (5S/4Q: positive coverage, not a silent skip)."""
    priors = LANG_PRIORS.get(lang, LANG_PRIORS["python"])
    fixtures, skipped = [], []
    for fn in ALL_RECIPES:
        batch = fn(arg_spec)
        for fx in batch:
            w = priors.get(fx["kind"], 1.0)
            if w < weight_floor:
                skipped.append({**fx, "weight": w, "blocked_by_type_system": True})
            else:
                fixtures.append({**fx, "weight": w})
    fixtures += R10_numeric_oracle(arg_spec, oracle)
    fixtures += R11_invariant_stress(arg_spec, invariants)
    fixtures += R13_state_sequence(arg_spec, stateful)
    return fixtures, skipped
