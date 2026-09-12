#!/usr/bin/env python3
"""
nan_domain_probe.py — the PROBE PASS over the NaN/domain FLAG suspects (open-loop item 9, lane B).

WHY THIS EXISTS
The library-wide sweep collapses two very different behaviours into one `FLAG`:
  * NaN in -> NaN out            = VISIBLE poison. The pattern propagates honestly. Not a kill.
  * NaN in -> FINITE out, no raise = FABRICATED CERTAINTY. The pattern absorbed poison and
    returned a confident number. That is the tool's own conclusive-kill rule
    (`nan_absorbed_silently` / `confident_impossible` in probes.py).
An aggregate FLAG hides which one happened, so 151 patterns sat undifferentiated. This probe
re-fires ONLY the nan/domain fixtures and records, per fixture, the actual input -> output pair.

IT INVENTS NO RULER. Baseline construction, fixture generation and the call guard are imported
from executor.py — the same code the graded sweep uses (exam 69/69). This module only
*classifies what it observed* and shows its evidence.

CLASSES (per pattern, worst-wins)
  FABRICATED_CERTAINTY  NaN/Inf scalar in -> finite output, no raise.        conclusive-kill class
  DOMAIN_SILENT         unambiguous invalid domain value (p=1.5, var=-1,
                        k=0) in -> finite output, no raise.                  needs human ruling
  VISIBLE_POISON        NaN/Inf in -> NaN/Inf out.                           benign / honest
  GUARDED               every attack raised.                                 good
  NO_EVIDENCE           no nan/domain fixture was applicable/reached.

A class is NOT a verdict. FABRICATED_CERTAINTY is the only class this tool would escalate on its
own authority, and even that is emitted as an evidence card for Illia's gate — written-on-disk
is not validated (the 191-descriptions precedent).
"""
import json, math, os, sys, io, contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from executor import (LIB, load_module, entry_functions, build_baseline, _call,
                      attack_fixtures, _finite, _finite_or_full, _has_nan_out)

def deep_has_nan(x, _depth=0):
    """Deep NaN/Inf scan — the executor's `_has_nan_out` only recurses into list/tuple, so a
    NaN sitting in a DICT KEY, a set, or a numpy array reads as 'clean finite output' and a
    visibly-poisoned result gets misfiled as fabricated certainty. Measured on this very run:
    `target_encoding_smoothing` returns {nan: 0.0, ...} — visible poison, not a silent kill.
    Recurses into dict keys+values, sets, and anything array-like."""
    if _depth > 6:
        return False
    try:
        if isinstance(x, bool):
            return False
        if isinstance(x, float):
            return math.isnan(x) or math.isinf(x)
        if isinstance(x, (list, tuple, set, frozenset)):
            return any(deep_has_nan(v, _depth + 1) for v in x)
        if isinstance(x, dict):
            return any(deep_has_nan(k, _depth + 1) or deep_has_nan(v, _depth + 1)
                       for k, v in x.items())
        # numpy / array-like without importing numpy
        tol = getattr(x, "tolist", None)
        if callable(tol):
            return deep_has_nan(tol(), _depth + 1)
    except Exception:
        return False
    return False


NAN_RECIPES = ("R15_scalar_nan_inf", "R8_nan_inf_poison")
DOMAIN_RECIPES = ("R2_domain_aware", "R9_degenerate_param")

ORDER = {"FABRICATED_CERTAINTY": 6, "DOMAIN_SILENT": 5, "INF_ABSORBED": 4,
         "VISIBLE_POISON": 3, "NO_OP_ATTACK": 2, "GUARDED": 1, "NO_EVIDENCE": 0}


def _same(a, b):
    """Equality that survives un-comparable outputs (numpy arrays raise on ==)."""
    try:
        return bool(a == b)
    except Exception:
        try:
            return repr(a) == repr(b)
        except Exception:
            return False


def _poison_kind(margs):
    """Which poison the fixture actually carried: 'nan', 'inf', or None.

    The split is load-bearing, not cosmetic. NaN means UNKNOWN — returning a confident finite
    number is a lie by construction. Inf is a well-defined extended-real value, and a bounded
    function may map it to a finite answer entirely correctly: `tricube_weight` documents
    "(1-|u|^3)^3 for |u| <= 1, else 0", so tricube_weight(inf) == 0.0 is the CONTRACT, not a
    defect. Hand-check on this run caught that as a false kill. So only NaN absorption is
    conclusive; Inf absorption is reported separately for a human ruling."""
    has_nan = has_inf = False

    def walk(v, d=0):
        nonlocal has_nan, has_inf
        if d > 5:
            return
        if isinstance(v, bool):
            return
        if isinstance(v, float):
            if math.isnan(v):
                has_nan = True
            elif math.isinf(v):
                has_inf = True
        elif isinstance(v, (list, tuple, set, frozenset)):
            for x in v:
                walk(x, d + 1)

    for a in margs:
        walk(a)
    return "nan" if has_nan else ("inf" if has_inf else None)


def _short(x, n=90):
    try:
        s = repr(x)
    except Exception:
        s = "<unreprable>"
    return s[:n]


def probe(relpath):
    module, load_err = load_module(relpath)
    if load_err:
        return {"file": relpath, "class": "NO_EVIDENCE", "reason": f"load error: {load_err}",
                "evidence": []}
    fns = entry_functions(module, relpath)
    if not fns:
        return {"file": relpath, "class": "NO_EVIDENCE", "reason": "no entry function",
                "evidence": []}

    worst, evidence = "NO_EVIDENCE", []
    for name, fn, sig, params in fns:
        baseline, buildable = build_baseline(params)
        if not buildable:
            continue
        # attack-reachability guardrail (oracle.py's rule, applied here too): if the mutated
        # arg never changes the result, the attack was a NO-OP — the param is unused or the
        # poison never reached the computation. Calling that "fabricated certainty" would be a
        # false KILL, so a no-op attack can never escalate.
        base_call = _call(fn, baseline)
        base_out = base_call.get("output") if not base_call.get("raised") else object()
        for recipe, margs, eclass, idx in attack_fixtures(params, baseline):
            if recipe not in NAN_RECIPES + DOMAIN_RECIPES:
                continue
            pname = params[idx].name if idx < len(params) else "?"
            r = _call(fn, margs)
            out = r.get("output")

            poison = _poison_kind(margs)
            no_op = (not r["raised"]) and _same(out, base_out)
            if r["raised"]:
                cls = "GUARDED"
            elif deep_has_nan(out):
                cls = "VISIBLE_POISON"
            elif no_op:
                cls = "NO_OP_ATTACK"          # unreachable/unused param — never a kill
            elif recipe in NAN_RECIPES and poison == "nan" and _finite_or_full(out):
                cls = "FABRICATED_CERTAINTY"
            elif recipe in NAN_RECIPES and poison == "inf" and _finite_or_full(out):
                cls = "INF_ABSORBED"
            elif recipe in DOMAIN_RECIPES and _finite_or_full(out):
                cls = "DOMAIN_SILENT"
            else:
                cls = "GUARDED"

            if ORDER[cls] > ORDER[worst]:
                worst = cls
            # keep evidence only for the actionable classes (and cap the card)
            if cls in ("FABRICATED_CERTAINTY", "DOMAIN_SILENT", "INF_ABSORBED") and len(evidence) < 8:
                evidence.append({
                    "fn": name, "recipe": recipe, "e_class": eclass, "param": pname,
                    "attack_value": _short(margs[idx] if idx < len(margs) else None, 60),
                    "output": _short(out),
                    "class": cls,
                })
    return {"file": relpath, "class": worst, "evidence": evidence}


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/nan_domain_suspects.json"
    files = json.load(open(src))
    print(f"PROBE PASS over {len(files)} NaN/domain suspects", flush=True)
    rows = []
    for i, f in enumerate(files):
        try:
            rows.append(probe(f))
        except Exception as e:
            rows.append({"file": f, "class": "NO_EVIDENCE",
                         "reason": f"probe error: {type(e).__name__}: {e}", "evidence": []})
        if (i + 1) % 25 == 0:
            print(f"  ...{i+1}/{len(files)}", file=sys.stderr, flush=True)

    from collections import Counter
    counts = Counter(r["class"] for r in rows)
    print("-" * 78)
    for k in ("FABRICATED_CERTAINTY", "DOMAIN_SILENT", "INF_ABSORBED", "VISIBLE_POISON", "NO_OP_ATTACK", "GUARDED", "NO_EVIDENCE"):
        print(f"  {k:22} {counts.get(k,0)}")
    out = os.path.join(HERE, "nan_domain_probe_report.json")
    json.dump({"counts": dict(counts), "rows": rows}, open(out, "w"), indent=1)
    print(f"report: {out}")


if __name__ == "__main__":
    main()
