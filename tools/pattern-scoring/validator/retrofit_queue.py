#!/usr/bin/env python3
"""
retrofit_queue.py — generate the RETROFIT QUEUE with receipts (2026-07-21).

For every triage-safe python pattern, record EVERY attack fixture that was SILENTLY
ACCEPTED (finite/confident output, no raise): file, function, recipe, parameter, value,
e_class. The queue is machine-generated evidence — the retrofit maps each receipt to an
accumulate-then-raise guard (ERROR_CATALOG design rule, proven in playground/retrofit_demo).

Output: retrofit_queue.json + RETROFIT_QUEUE.md (grouped by defect class -> template).
"""
import os, json, math, glob
from collections import defaultdict
from executor import (load_module, entry_functions, build_baseline, attack_fixtures,
                      _call, _finite_or_full, _has_nan_out, LIB)
import probes

HERE = os.path.dirname(os.path.abspath(__file__))
ACCEPT_RECIPES = ("R1_domain_under", "R2_domain_aware", "R9_degenerate_param", "R15_scalar_nan_inf")


def safe_set():
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "python/data-science", "**", "*.py"), recursive=True))
    return files


def receipts_for(relpath):
    module, err = load_module(relpath)
    if err:
        return []
    out = []
    for name, fn, sig, params in entry_functions(module, relpath):
        baseline, buildable = build_baseline(params)
        if not buildable:
            continue
        for recipe, margs, eclass, idx in attack_fixtures(params, baseline):
            if recipe not in ACCEPT_RECIPES:
                continue
            r = _call(fn, margs)
            o = r.get("output")
            if (not r["raised"]) and (not _has_nan_out(o)) and _finite_or_full(o):
                val = margs[idx]
                out.append({"function": name, "recipe": recipe, "e_class": eclass,
                            "param": params[idx].name,
                            "value": repr(val), "output": repr(o)[:60]})
    return out


def main():
    queue = {}
    for f in safe_set():
        if f in probes.PROBES and f != "python/data-science/statistical_modeling/power_analysis_sample_size.py":
            pass  # probe-backed verdicts already ruled; still record receipts (fix queue is orthogonal)
        rs = receipts_for(f)
        if rs:
            queue[f] = rs
    n_receipts = sum(len(v) for v in queue.values())
    json.dump(queue, open(os.path.join(HERE, "retrofit_queue.json"), "w"), indent=1)

    # class clustering: e_class+recipe -> guard template
    by_class = defaultdict(list)
    for f, rs in queue.items():
        for r in rs:
            by_class[(r["recipe"], r["e_class"])].append((f, r))

    TEMPLATES = {
        "R2_domain_aware": "T1 domain-bounds guard: param must lie in its declared domain (prob in [0,1], alpha in (0,1), rate>0, u in [0,1)); violation -> collect AURA-E001/E003.",
        "R1_domain_under": "T1 domain-bounds guard (blunt underflow -1e9 accepted -> same bounds check).",
        "R9_degenerate_param": "T2 degenerate-count guard: k/window/bins/n >= 1; violation -> collect AURA-E009.",
        "R15_scalar_nan_inf": "T3 finite-scalar guard: math.isfinite(x) required on every float param; violation -> collect AURA-E008/E017.",
    }

    lines = ["# RETROFIT QUEUE — machine-generated 2026-07-21 (receipts, not opinions)",
             f"\n{len(queue)} patterns · {n_receipts} silently-accepted attacks · source: retrofit_queue.json",
             "\nDESIGN RULE (frozen 07-19): accumulate-then-raise — one `_validate_inputs()` block",
             "per entry fn, collects ALL violations, raises ONE AuraInputError listing each with",
             "its AURA-E code. Proven template: playground/retrofit_demo/*_RETROFIT.py",
             "\n## Guard templates -> receipts per class"]
    for (recipe, eclass), items in sorted(by_class.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"\n### {recipe} ({eclass}) — {len(items)} receipts -> {TEMPLATES.get(recipe, '?')}")
        per