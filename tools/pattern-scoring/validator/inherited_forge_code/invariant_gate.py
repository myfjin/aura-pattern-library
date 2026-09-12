#!/usr/bin/env python3
"""Forge Gate — Wave 2 (#5): Daikon-style mined invariant contracts.

Mine likely invariants from a signed oracle (run it across many input
instances, observe outputs), propose ratifiable contracts, then check
candidates against the RATIFIED contract. Zero LLM in the verdict path.

Modes:
  mine   <pattern>                 -> write contracts/<pattern>.json (ratified=false)
  verify <user_file> --pattern <p> -> PASS/FAIL/UNSUPPORTED against ratified contract

A contract is only enforced once a human sets "ratified": true. This adds
RELATIONAL catching power (e.g. coefficient ratios/signs) that scalar
property thresholds miss — proven: weights individually in-tolerance but
whose ratio is wrong are caught here, not by property-primary.
"""
from __future__ import annotations
import argparse, importlib.util, json, random, statistics, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "tools" / "invariant_contracts"
CONTRACTS.mkdir(parents=True, exist_ok=True)
LIB = Path("/home/au/aura-pattern-library")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


# ---- per-pattern adapters: (oracle_relpath, fn_name, gen(seed)->args, metrics(out,args)->dict) ----
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
    true_weights = [2.0, 3.0, -1.0]
    y = [sum(true_weights[j] * X[i][j] for j in range(n_features)) + random.gauss(0, 0.5)
         for i in range(n_samples)]
    return {"X": X, "y": y, "lambda_reg": 0.01}


def _metrics_ridge(out, args):
    weights = out
    X, y = args["X"], args["y"]
    n_samples = len(X)
    pred = [sum(weights[j] * X[i][j] for j in range(len(weights))) for i in range(n_samples)]
    my = sum(y) / len(y)
    ssr = sum((pred[i] - y[i]) ** 2 for i in range(n_samples))
    sst = sum((y[i] - my) ** 2 for i in range(n_samples))
    r2 = 1 - ssr / sst if sst > 0 else 0.0
    w0, w1, w2 = weights[0], weights[1], weights[2]
    return {"r2": r2,
            "weight_0": w0, "weight_1": w1, "weight_2": w2,
            "ratio_w0_w1": w0 / w1 if abs(w1) > 1e-9 else float("nan"),
            "ratio_w1_w2": w1 / w2 if abs(w2) > 1e-9 else float("nan")}


def _gen_poly(seed, n=20):
    random.seed(seed)
    true_coeffs = [2.0, 3.0, 0.5]
    x_vals = [float(i) * 0.5 for i in range(n)]
    y_vals = []
    for x in x_vals:
        y = true_coeffs[0] + true_coeffs[1] * x + true_coeffs[2] * x * x + random.gauss(0, 0.1)
        y_vals.append(y)
    return {"x_vals": x_vals, "y_vals": y_vals, "degree": 2}


def _metrics_poly(out, args):
    coeffs = out
    x_vals, y_vals = args["x_vals"], args["y_vals"]
    pred = []
    for x in x_vals:
        p = 0.0
        power = 1.0
        for c in coeffs:
            p += c * power
            power *= x
        pred.append(p)
    mse = sum((pred[i] - y_vals[i]) ** 2 for i in range(len(y_vals))) / len(y_vals)
    c0, c1, c2 = coeffs[0], coeffs[1], coeffs[2]
    return {"mse": mse,
            "coeff_0": c0, "coeff_1": c1, "coeff_2": c2,
            "ratio_c0_c1": c0 / c1 if abs(c1) > 1e-9 else float("nan"),
            "ratio_c1_c2": c1 / c2 if abs(c2) > 1e-9 else float("nan")}


ADAPTERS = {
    "linear_regression_gd": {
        "oracle": "python/data-science/core_ml/linear_regression_gd.py",
        "fn": "linear_regression_gd", "gen": _gen_linreg, "metrics": _metrics_linreg,
    },
    "ridge_regression_normal_eq": {
        "oracle": "python/data-science/core_ml/ridge_regression_normal_eq.py",
        "fn": "ridge_regression_normal_eq", "gen": _gen_ridge, "metrics": _metrics_ridge,
    },
    "polynomial_regression": {
        "oracle": "python/data-science/statistical_modeling/polynomial_regression.py",
        "fn": "fit_polynomial", "gen": _gen_poly, "metrics": _metrics_poly,
    },
}


def mine(pattern, n=100):
    a = ADAPTERS[pattern]
    oracle = load(LIB / a["oracle"], "oracle")
    fn = getattr(oracle, a["fn"])
    samples = []
    for seed in range(n):
        args = a["gen"](seed)
        out = fn(**args)
        samples.append(a["metrics"](out, args))
    inv = {}
    for k in samples[0]:
        v = [s[k] for s in samples if s[k] == s[k]]  # drop NaN
        if not v:
            continue
        mean, sd = statistics.mean(v), statistics.pstdev(v)
        inv[k] = {"observed": [round(min(v), 5), round(max(v), 5)],
                  "mean": round(mean, 5), "sd": round(sd, 5),
                  "contract": [round(mean - 4 * sd - 0.02, 4), round(mean + 4 * sd + 0.02, 4)],
                  "sign": "positive" if min(v) > 0 else ("negative" if max(v) < 0 else "mixed")}
    doc = {"pattern": pattern, "n_samples": n, "ratified": False,
           "note": "human sets ratified=true after reviewing contracts", "invariants": inv}
    (CONTRACTS / f"{pattern}.json").write_text(json.dumps(doc, indent=2))
    return doc


def verify(user_file, pattern):
    cpath = CONTRACTS / f"{pattern}.json"
    if pattern not in ADAPTERS or not cpath.exists():
        return "UNSUPPORTED", "no adapter or contract for pattern"
    doc = json.loads(cpath.read_text())
    if not doc.get("ratified"):
        return "UNSUPPORTED", "contract not yet ratified by a human"
    a = ADAPTERS[pattern]
    user = load(Path(user_file), "user")
    fn = getattr(user, a["fn"], None)
    if fn is None:
        return "FAIL", f"user must define {a['fn']}"
    # deterministic seed 0 instance for the check
    args = a["gen"](0)
    try:
        m = a["metrics"](fn(**args), args)
    except Exception as e:
        return "FAIL", f"user raised {type(e).__name__}: {e}"
    violations = []
    for k, spec in doc["invariants"].items():
        val = m.get(k)
        if val is None or val != val:
            continue
        lo, hi = spec["contract"]
        if not (lo <= val <= hi):
            violations.append(f"{k}={val:.4f} outside [{lo},{hi}]")
    if violations:
        return "FAIL", "invariant violation: " + "; ".join(violations)
    return "PASS", "all ratified invariants hold"


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    m = sub.add_parser("mine"); m.add_argument("pattern")
    v = sub.add_parser("verify"); v.add_argument("user_file"); v.add_argument("--pattern", required=True)
    args = ap.parse_args()
    if args.mode == "mine":
        doc = mine(args.pattern)
        print(json.dumps(doc, indent=2))
    else:
        status, reason = verify(args.user_file, args.pattern)
        print(f"{status}: {args.pattern}\n  reason: {reason}")
        sys.exit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
