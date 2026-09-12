#!/usr/bin/env python3
"""
invariant_mine.py — FOLD 2: Daikon-style invariant mining as the invariant-probe grid's
AUTO-harvester. Adapted from forge-gate/tools/invariant_gate.py (inherited, NOT merged — the
two tools stay separate; forge's `verify` half checks USER code, we keep only the `mine` half
and re-aim it at OUR signed library to auto-propose the invariants we were hand-writing).

WHAT IT DOES for the validation tool:
  Run a signed-library oracle across N deterministic seeds, observe outputs, and MINE likely
  invariants — scalar ranges (mean +/- 4sd) AND the relational ones scalar thresholds miss
  (coefficient ratios, signs). Emit them as ratifiable contracts + evidence cards.

TWO HARD LAWS (Illia's):
  1. RATIFY BY HAND. Every mined contract is written ratified=false and is NEVER enforced until
     a human flips it. `harvest()` proposes; it does not grade. An un-ratified invariant carries
     ZERO verdict weight — it cannot PASS or INVALID anything.
  2. MINING IS OBSERVATION-ONLY. It reads the signed oracle's outputs; it never mutates the
     library and never touches exam grading. The frozen exam cannot flip by construction.

Verdict-ladder mapping: a mined invariant is a PROPOSAL, not a verdict. Once RATIFIED it becomes
a positive oracle of kind 'invariant' in oracle_coverage: a pattern that satisfies its ratified
invariants has that much more verified positive coverage; a ratified invariant a pattern VIOLATES
is an INVALID candidate (routed to calibration, never auto-enforced). Relational invariants are
the catch scalar thresholds miss (weights each in-tolerance but whose RATIO is wrong).

Modes:
  harvest [pattern...]   -> mine + write mined_invariants/<pattern>.json (ratified=false) + cards
  check   <pattern>      -> report which RATIFIED invariants the live library pattern satisfies
                            (skips unratified; observation report, not an exam verdict)
"""
from __future__ import annotations
import argparse, importlib.util, json, os, random, statistics, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = Path(os.path.expanduser("~/aura-pattern-library"))
MINED = HERE / "mined_invariants"
MINED.mkdir(parents=True, exist_ok=True)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


# ---- per-pattern adapters (ported from the forge miner: gen(seed)->args, metrics(out,args)->dict).
#      metrics MUST include the relational quantities (ratios/signs) — that's the mining edge. ----
def _gen_linreg(seed, n=30):
    random.seed(seed)
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n)]
    return {"X": X, "y": y, "learning_rate": 0.01, "iterations": 200}


def _metrics_linreg(out, args):
    w, b = out
    X, y = args["X"], args["y"]
    pred = [b + sum(w[j] * X[i][j] for j in range(2)) for i in range(len(X))]
    my = sum(y) / len(y)
    ssr = sum((pred[i] - y[i]) ** 2 for i in range(len(X)))
    sst = sum((y[i] - my) ** 2 for i in range(len(X)))
    r2 = 1 - ssr / sst if sst > 0 else 0.0
    return {"r2": r2, "weight_0": w[0], "weight_1": w[1], "bias": b,
            "ratio_w0_w1": w[0] / w[1] if abs(w[1]) > 1e-9 else float("nan")}


def _gen_ridge(seed, n_samples=30, n_features=3):
    random.seed(seed)
    X = [[random.uniform(-5, 5) for _ in range(n_features)] for _ in range(n_samples)]
    tw = [2.0, 3.0, -1.0]
    y = [sum(tw[j] * X[i][j] for j in range(n_features)) + random.gauss(0, 0.5)
         for i in range(n_samples)]
    return {"X": X, "y": y, "lambda_reg": 0.01}


def _metrics_ridge(out, args):
    w = out
    X, y = args["X"], args["y"]
    pred = [sum(w[j] * X[i][j] for j in range(len(w))) for i in range(len(X))]
    my = sum(y) / len(y)
    ssr = sum((pred[i] - y[i]) ** 2 for i in range(len(X)))
    sst = sum((y[i] - my) ** 2 for i in range(len(X)))
    r2 = 1 - ssr / sst if sst > 0 else 0.0
    return {"r2": r2, "weight_0": w[0], "weight_1": w[1], "weight_2": w[2],
            "ratio_w0_w1": w[0] / w[1] if abs(w[1]) > 1e-9 else float("nan"),
            "ratio_w1_w2": w[1] / w[2] if abs(w[2]) > 1e-9 else float("nan")}


def _gen_poly(seed, n=20):
    random.seed(seed)
    tc = [2.0, 3.0, 0.5]
    xs = [float(i) * 0.5 for i in range(n)]
    ys = [tc[0] + tc[1] * x + tc[2] * x * x + random.gauss(0, 0.1) for x in xs]
    return {"x_vals": xs, "y_vals": ys, "degree": 2}


def _metrics_poly(out, args):
    coeffs = out
    xs, ys = args["x_vals"], args["y_vals"]
    pred = []
    for x in xs:
        p, power = 0.0, 1.0
        for c in coeffs:
            p += c * power; power *= x
        pred.append(p)
    mse = sum((pred[i] - ys[i]) ** 2 for i in range(len(ys))) / len(ys)
    return {"mse": mse, "coeff_0": coeffs[0], "coeff_1": coeffs[1], "coeff_2": coeffs[2],
            "ratio_c0_c1": coeffs[0] / coeffs[1] if abs(coeffs[1]) > 1e-9 else float("nan"),
            "ratio_c1_c2": coeffs[1] / coeffs[2] if abs(coeffs[2]) > 1e-9 else float("nan")}


ADAPTERS = {
    "linear_regression_gd": {
        "oracle": "python/data-science/core_ml/linear_regression_gd.py",
        "fn": "linear_regression_gd", "gen": _gen_linreg, "metrics": _metrics_linreg},
    "ridge_regression_normal_eq": {
        "oracle": "python/data-science/core_ml/ridge_regression_normal_eq.py",
        "fn": "ridge_regression_normal_eq", "gen": _gen_ridge, "metrics": _metrics_ridge},
    "polynomial_regression": {
        "oracle": "python/data-science/statistical_modeling/polynomial_regression.py",
        "fn": "fit_polynomial", "gen": _gen_poly, "metrics": _metrics_poly},
}


def _mine_one(pattern, n=100):
    a = ADAPTERS[pattern]
    oracle = load(LIB / a["oracle"], f"oracle_{pattern}")
    fn = getattr(oracle, a["fn"])
    samples = []
    for seed in range(n):
        args = a["gen"](seed)
        samples.append(a["metrics"](fn(**args), args))
    inv = {}
    for k in samples[0]:
        v = [s[k] for s in samples if s[k] == s[k]]  # drop NaN
        if not v:
            continue
        mean, sd = statistics.mean(v), statistics.pstdev(v)
        inv[k] = {"observed": [round(min(v), 5), round(max(v), 5)],
                  "mean": round(mean, 5), "sd": round(sd, 5),
                  # 4-sigma envelope + a small pad — a candidate range, NOT a law until ratified
                  "contract": [round(mean - 4 * sd - 0.02, 4), round(mean + 4 * sd + 0.02, 4)],
                  "sign": "positive" if min(v) > 0 else ("negative" if max(v) < 0 else "mixed"),
                  "kind": "relational" if k.startswith("ratio_") else "scalar"}
    doc = {"pattern": pattern, "oracle": a["oracle"], "n_samples": n, "ratified": False,
           "note": "MINED CANDIDATE — a human sets ratified=true after review; unratified = zero verdict weight",
           "invariants": inv}
    (MINED / f"{pattern}.json").write_text(json.dumps(doc, indent=2))
    return doc


def _card(pattern, doc):
    rel = [k for k, s in doc["invariants"].items() if s["kind"] == "relational"]
    return {"pattern": doc["oracle"], "technique": "daikon-invariant-mining", "severity": "info",
            "class": "mined-invariant-proposal",
            "fixture": f"{doc['n_samples']} deterministic seeds over signed oracle",
            "expected": "ratifiable invariant candidates (scalar ranges + relational ratios/signs)",
            "actual": f"mined {len(doc['invariants'])} candidates ({len(rel)} relational: {rel})",
            "why": "relational invariants (ratios/signs) catch what scalar thresholds miss; feeds the invariant-probe grid",
            "verdict": "PROPOSAL", "verdict_target": "HUMAN-RATIFICATION",
            "ratified": False, "confidence": "candidate",
            "repro_cmd": f"python3 invariant_mine.py harvest {pattern}",
            "oracle_coverage_kind": "invariant"}


def harvest(patterns, verbose=True):
    cards = []
    for pattern in patterns:
        if pattern not in ADAPTERS:
            if verbose: print(f"  {pattern:34} SKIP (no adapter)")
            continue
        doc = _mine_one(pattern)
        rel = [k for k, s in doc["invariants"].items() if s["kind"] == "relational"]
        if verbose:
            print(f"  {pattern:34} mined {len(doc['invariants'])} invariants "
                  f"({len(rel)} relational)  -> ratified=FALSE (awaits hand-ratification)")
        cards.append(_card(pattern, doc))
    json.dump({"cards": cards}, open(HERE / "invariant_mine_report.json", "w"), indent=1)
    return cards


def check(pattern):
    """Report which RATIFIED invariants the live library pattern satisfies. Unratified -> skipped.
    Observation report only — NOT an exam verdict (the exam ruler is untouched by this module)."""
    cpath = MINED / f"{pattern}.json"
    if pattern not in ADAPTERS or not cpath.exists():
        print(f"{pattern}: UNSUPPORTED (no adapter/contract)"); return
    doc = json.loads(cpath.read_text())
    if not doc.get("ratified"):
        print(f"{pattern}: {len(doc['invariants'])} invariants MINED but ratified=false "
              f"-> NOT enforced (zero verdict weight until a human ratifies)"); return
    a = ADAPTERS[pattern]
    oracle = load(LIB / a["oracle"], f"chk_{pattern}")
    m = a["metrics"](getattr(oracle, a["fn"])(**a["gen"](0)), a["gen"](0))
    held, viol = [], []
    for k, spec in doc["invariants"].items():
        val = m.get(k)
        if val is None or val != val:
            continue
        lo, hi = spec["contract"]
        (held if lo <= val <= hi else viol).append(k)
    print(f"{pattern}: RATIFIED invariants — {len(held)} hold, {len(viol)} violated"
          + (f" (VIOLATIONS: {viol})" if viol else ""))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    h = sub.add_parser("harvest"); h.add_argument("patterns", nargs="*")
    c = sub.add_parser("check"); c.add_argument("pattern")
    args = ap.parse_args()
    if args.mode == "harvest":
        pats = args.patterns or list(ADAPTERS)
        print("DAIKON INVARIANT MINER (fold 2) — auto-harvest ratifiable invariants from the signed library")
        print("=" * 92)
        cards = harvest(pats)
        print("=" * 92)
        print(f"harvested {len(cards)} pattern contracts -> mined_invariants/  (ALL ratified=false)")
        print("NEXT (human): review mined_invariants/*.json, flip ratified=true on the ones that are real.")
    else:
        check(args.pattern)


if __name__ == "__main__":
    main()
