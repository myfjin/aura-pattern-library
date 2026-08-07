#!/usr/bin/env python3
"""Probe robustness of python pattern entry functions on synthetic input classes.

Rules:
- Probe EVERY registry entry function where matrix_param is true.
- Select entry functions where registry matrix_param is true (never entry_fns[0] blindly).
- Seed everything; two runs at the same seed produce byte-identical output.
- Report only: FINITE / NaN-Inf / DIVERGED / THREW / INCONCLUSIVE.
- Append each row the moment it is produced.
- No PASS/FAIL verdicts; exit non-zero only if the prober itself breaks.

Pattern-level summary rule (written down):
  For each (pattern, class) pair, look at the outcomes of all probed matrix_param
  functions. The worst outcome wins, ordered:
      THREW > NaN-Inf > DIVERGED > INCONCLUSIVE > FINITE
  If no matrix_param function can be exercised, the summary is INCONCLUSIVE.
"""

import argparse
import hashlib
import importlib.util
import inspect
import json
import math
import os
import random
import signal
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

DIVERGE_THRESHOLD = 1e15  # absurd magnitude threshold, declared here per brief.
TIMEOUT_SECONDS = 30      # per-call hang guard.
WILDLY_SCALED_MAGNITUDES = [1e3, 1e6, 1e12, 1e30, 1e155]
CLASSES = [
    "uncentred",
    "wildly-scaled",
    "near-collinear",
    "rank-deficient",
    "single-row",
    "constant-column",
]

# Worst-outcome-wins ordering for pattern-level summary.
_OUTCOME_RANK = {
    "THREW": 4,
    "NaN-Inf": 3,
    "DIVERGED": 2,
    "INCONCLUSIVE": 1,
    "FINITE": 0,
}


def _classify_value(v: float) -> str:
    if math.isnan(v) or math.isinf(v):
        return "nan-inf"
    if abs(v) > DIVERGE_THRESHOLD:
        return "huge"
    return "ok"


def _scan_result(obj: Any) -> Tuple[str, str]:
    """Recursively scan returned object; return (outcome, note)."""
    worst = "ok"
    count = 0
    max_abs = 0.0

    def walk(o: Any) -> None:
        nonlocal worst, count, max_abs
        if isinstance(o, float):
            count += 1
            max_abs = max(max_abs, abs(o))
            if math.isnan(o) or math.isinf(o):
                if worst in ("ok", "huge"):
                    worst = "nan-inf"
            elif abs(o) > DIVERGE_THRESHOLD:
                if worst == "ok":
                    worst = "huge"
        elif isinstance(o, int):
            count += 1
            max_abs = max(max_abs, abs(o))
            if abs(o) > DIVERGE_THRESHOLD:
                if worst == "ok":
                    worst = "huge"
        elif isinstance(o, (list, tuple)):
            for item in o:
                walk(item)
        elif isinstance(o, dict):
            for item in o.values():
                walk(item)

    walk(obj)
    note = f"numbers={count},max_abs={max_abs:.3e}"
    if count == 0:
        return "INCONCLUSIVE", "no numbers returned; nothing was measured"
    if worst == "ok":
        return "FINITE", note
    if worst == "huge":
        return "DIVERGED", note
    return "NaN-Inf", note


class TimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("call exceeded TIMEOUT_SECONDS")


def _call_with_timeout(fn, args, kwargs):
    old = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(TIMEOUT_SECONDS)
    try:
        result = fn(*args, **kwargs)
        return result, None
    except TimeoutError as e:
        return None, ("INCONCLUSIVE", f"hang: {e}")
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def _is_2d_annotation(ann: Any) -> bool:
    if ann is None:
        return False
    s = str(ann).lower()
    return "list[list" in s or "[][]" in s or "sequence[sequence" in s


class InputGenerator:
    """Produce deterministic synthetic inputs for the six classes."""

    def __init__(self, seed: int, uncentred_offset: float):
        self.seed = seed
        self.uncentred_offset = uncentred_offset
        self.rng = random.Random(seed)

    def _stable_int(self, salt: str) -> int:
        # Stable, process-independent 31-bit integer from salt.
        digest = hashlib.md5(salt.encode("utf-8")).digest()
        return int.from_bytes(digest[:4], "little") & 0x7FFFFFFF

    def _reset(self, salt: str):
        self.rng = random.Random(self.seed + self._stable_int(salt))

    def matrix(self, cls: str, n: int = 30, p: int = 2) -> List[List[float]]:
        self._reset(f"matrix:{cls}:{n}:{p}")
        if cls == "uncentred":
            return [[self.rng.uniform(self.uncentred_offset, self.uncentred_offset + 10.0)
                     for _ in range(p)] for _ in range(n)]
        if cls == "wildly-scaled":
            raise ValueError("matrix() does not support wildly-scaled; use matrix_wildly_scaled(scale)")
        if cls == "near-collinear":
            eps = 1e-12
            scale = 30.0
            base = [self.rng.uniform(-scale, scale) for _ in range(n)]
            return [[base[i] * (1.0 + eps * self.rng.uniform(-1.0, 1.0)) for _ in range(p)] for i in range(n)]
        if cls == "rank-deficient":
            # p columns but one is a linear combination; keep n >= p to avoid trivial shape issues.
            rows = []
            for _ in range(n):
                a = self.rng.uniform(-1.0, 1.0)
                b = self.rng.uniform(-1.0, 1.0)
                rows.append([a, b, a + b])
            return rows
        if cls == "single-row":
            return [[self.rng.uniform(-1.0, 1.0) for _ in range(p)]]
        if cls == "constant-column":
            rows = []
            for _ in range(n):
                a = self.rng.uniform(-1.0, 1.0)
                rows.append([a, 5.0])
            return rows
        raise ValueError(f"unknown class {cls}")

    def matrix_wildly_scaled(self, n: int = 30, p: int = 2, scale: float = 1e12) -> List[List[float]]:
        self._reset(f"matrix-wildly:{scale}:{n}:{p}")
        rows = []
        for _ in range(n):
            row = [self.rng.uniform(-scale, scale)]
            for _ in range(1, p):
                row.append(self.rng.uniform(-1.0, 1.0))
            rows.append(row)
        return rows

    def vector(self, cls: str, n: int = 30) -> List[float]:
        self._reset(f"vector:{cls}:{n}")
        if cls == "uncentred":
            return [self.rng.uniform(self.uncentred_offset, self.uncentred_offset + 10.0) for _ in range(n)]
        if cls == "wildly-scaled":
            raise ValueError("vector() does not support wildly-scaled; use vector_wildly_scaled(scale)")
        if cls == "near-collinear":
            eps = 1e-12
            scale = 30.0
            base = [self.rng.uniform(-scale, scale) for _ in range(n)]
            return [base[i] * (1.0 + eps * self.rng.uniform(-1.0, 1.0)) for i in range(n)]
        if cls == "rank-deficient":
            return [1.0 for _ in range(n)]
        if cls == "single-row":
            return [5.0]
        if cls == "constant-column":
            return [5.0 for _ in range(n)]
        raise ValueError(f"unknown class {cls}")

    def vector_wildly_scaled(self, n: int = 30, scale: float = 1e12) -> List[float]:
        self._reset(f"vector-wildly:{scale}:{n}")
        return [scale if i % 2 == 0 else self.rng.uniform(-1.0, 1.0) for i in range(n)]

    def groups(self, cls: str, m: int = 3, n_obs: int = 10) -> List[List[float]]:
        self._reset(f"groups:{cls}:{m}:{n_obs}")
        if cls == "uncentred":
            return [[self.rng.uniform(self.uncentred_offset, self.uncentred_offset + 10.0)
                     for _ in range(n_obs)] for _ in range(m)]
        if cls == "wildly-scaled":
            raise ValueError("groups() does not support wildly-scaled")
        if cls == "near-collinear":
            eps = 1e-12
            scale = 30.0
            base = [self.rng.uniform(-scale, scale) for _ in range(n_obs)]
            return [[base[i] * (1.0 + eps * self.rng.uniform(-1.0, 1.0)) for i in range(n_obs)] for _ in range(m)]
        if cls == "rank-deficient":
            return [[float(i + 1) for _ in range(n_obs)] for i in range(m)]
        if cls == "single-row":
            return [[5.0] for _ in range(m)]
        if cls == "constant-column":
            return [[5.0 for _ in range(n_obs)] for _ in range(m)]
        raise ValueError(f"unknown class {cls}")

    def chains(self, cls: str, m: int = 4, n: int = 30) -> List[List[float]]:
        # Treat chains like a matrix of samples x chains, then transpose.
        mat = self.matrix(cls, n=n, p=m)
        return [[mat[j][i] for j in range(n)] for i in range(m)]

    def train_test_split(self, cls: str, n_train: int = 24, n_test: int = 6, p: int = 2):
        self._reset(f"train_test:{cls}:{n_train}:{n_test}:{p}")
        if cls == "wildly-scaled":
            raise ValueError("train_test_split does not support wildly-scaled")
        X_train = self.matrix(cls, n=n_train, p=p)
        X_test = self.matrix(cls, n=n_test, p=p)
        y_train = [self.rng.randint(0, 1) for _ in range(n_train)]
        return X_train, y_train, X_test


def _shape_kind_for_first_param(fn_info: Dict[str, Any]) -> str:
    ann = (fn_info.get("params") or [{}])[0].get("annotation")
    if _is_2d_annotation(ann):
        return "matrix"
    name = (fn_info.get("params") or [{}])[0].get("name", "")
    if name in ("groups", "chains"):
        return name
    return "vector"


def _build_args(mod, fn_info: Dict[str, Any], cls: str, gen: InputGenerator,
                wild_scale: float | None = None) -> Tuple[List, Dict, str]:
    """Build positional and keyword args for the selected entry function.

    Returns (args, kwargs, note) where note is empty on success.
    """
    fn_name = fn_info["name"]
    fn = getattr(mod, fn_name)
    sig = inspect.signature(fn)

    params = list(sig.parameters.items())
    if not params:
        return [], {}, "no parameters"

    shape = _shape_kind_for_first_param(fn_info)

    # Generate the synthetic primary input.
    if shape == "matrix":
        if cls == "wildly-scaled":
            primary = gen.matrix_wildly_scaled(scale=wild_scale) if wild_scale is not None else gen.matrix_wildly_scaled()
        else:
            primary = gen.matrix(cls)
    elif shape == "groups":
        if cls == "wildly-scaled":
            # groups do not have a scale ladder; fall back to a single representative 1e30.
            primary = gen.groups("uncentred")
            for i in range(len(primary)):
                for j in range(len(primary[i])):
                    primary[i][j] *= 1e30
        else:
            primary = gen.groups(cls)
    elif shape == "chains":
        if cls == "wildly-scaled":
            primary = gen.matrix_wildly_scaled(scale=1e30, p=4)
            primary = [[primary[j][i] for j in range(len(primary))] for i in range(4)]
        else:
            primary = gen.chains(cls)
    else:
        if cls == "wildly-scaled":
            primary = gen.vector_wildly_scaled(scale=wild_scale) if wild_scale is not None else gen.vector_wildly_scaled()
        else:
            primary = gen.vector(cls)

    args = []
    kwargs = {}

    for i, (pname, param) in enumerate(params):
        if i == 0:
            value = primary
        elif pname in ("y", "y_train"):
            # Generate a target compatible with the primary input.
            if shape == "matrix" and isinstance(primary, list) and primary:
                if cls == "wildly-scaled":
                    # Make target large enough to overflow naive GD, keep X within the chosen scale.
                    scale = wild_scale if wild_scale is not None else 1e30
                    value = [row[0] * scale + (row[1] if len(row) > 1 else 0.0) + gen.rng.gauss(0.0, 0.1)
                             for row in primary]
                elif cls == "near-collinear":
                    # Natural-ish target; ill-conditioning still drives divergence in vanilla GD.
                    value = [sum(row) + gen.rng.gauss(0.0, 0.01) for row in primary]
                else:
                    value = [sum(row) + gen.rng.gauss(0.0, 0.1) for row in primary]
            elif shape == "vector" and isinstance(primary, list):
                value = [gen.rng.randint(0, 1) for _ in primary]
            else:
                value = [gen.rng.randint(0, 1) for _ in range(len(primary) if isinstance(primary, list) else 0)]
        elif pname == "X_test":
            # Small test set derived from the same class.
            if shape == "matrix":
                if cls == "wildly-scaled":
                    value = gen.matrix_wildly_scaled(scale=wild_scale if wild_scale is not None else 1e30, n=6)
                else:
                    value = gen.matrix(cls, n=6)
            else:
                if cls == "wildly-scaled":
                    value = gen.vector_wildly_scaled(scale=wild_scale if wild_scale is not None else 1e30, n=6)
                else:
                    value = gen.vector(cls, n=6)
        elif pname == "k":
            value = 3
        elif pname in ("iterations", "max_iter", "cycles"):
            value = 100
        elif pname == "learning_rate":
            value = 0.01
        elif pname == "prior_var_h1":
            value = 1.0
        elif pname == "prior_sigma":
            value = 1.0
        elif pname == "prior_sigma_sq":
            value = 10.0
        elif pname == "mu0":
            value = 0.0
        elif pname == "s0":
            value = 10.0
        elif pname == "lam0":
            value = 0.01
        elif pname == "a0":
            value = 0.01
        elif pname == "b0":
            value = 0.01
        elif pname == "n_dims":
            value = 16
        elif pname == "texts":
            value = ["alpha beta gamma"] * 3
        else:
            if param.default is inspect.Parameter.empty:
                return [], {}, f"unresolved required parameter `{pname}`"
            value = param.default

        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            args.extend(value)
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            kwargs.update(value)
        elif param.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
            args.append(value)
        else:
            kwargs[pname] = value

    return args, kwargs, ""


def _probe_function(pattern_id: str, mod: Any, fn_info: Dict[str, Any], cls: str, gen: InputGenerator,
                    outfh, wild_scale: float | None = None) -> Tuple[str, str, str]:
    """Probe one function on one class. Return (outcome, exception, note)."""
    fn_name = fn_info["name"]
    outcome = "INCONCLUSIVE"
    exc_type = ""
    note = ""
    try:
        args, kwargs, build_note = _build_args(mod, fn_info, cls, gen, wild_scale=wild_scale)
        if build_note:
            outcome = "INCONCLUSIVE"
            note = build_note
        else:
            fn = getattr(mod, fn_name)
            result, timeout_info = _call_with_timeout(fn, args, kwargs)
            if timeout_info:
                outcome, note = timeout_info
            else:
                outcome, note = _scan_result(result)
    except Exception as e:
        outcome = "THREW"
        exc_type = type(e).__name__
        note = str(e)[:120]
    return outcome, exc_type, note


def _write_row(outfh, seed: int, offset: float, pattern_id: str, fn_name: str | None,
               cls: str, outcome: str, exc_type: str, note: str,
               wild_scale: float | None = None):
    scale_col = "" if wild_scale is None else f"{wild_scale:.0e}"
    fn_col = fn_name if fn_name is not None else ""
    outfh.write(f"{seed}\t{offset}\t{pattern_id}\t{fn_col}\t{cls}\t{scale_col}\t{outcome}\t{exc_type}\t{note}\n")
    outfh.flush()


def _probe_pattern(pattern_file: Path, registry: Dict[str, Any], gen: InputGenerator,
                   seed: int, offset: float, outfh) -> int:
    pattern_id = registry["id"]
    spec = importlib.util.spec_from_file_location(pattern_id, pattern_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    matrix_fns = [fn for fn in registry["entry_fns"] if fn["matrix_param"]]

    if not matrix_fns:
        for cls in CLASSES:
            _write_row(outfh, seed, offset, pattern_id, None, cls, "INCONCLUSIVE", "", "no matrix_param entry")
        return 0

    rows_written = 0
    summary: Dict[str, List[Tuple[str, str, str]]] = {cls: [] for cls in CLASSES}

    for fn_info in matrix_fns:
        fn_name = fn_info["name"]
        for cls in CLASSES:
            if cls == "wildly-scaled":
                for scale in WILDLY_SCALED_MAGNITUDES:
                    outcome, exc_type, note = _probe_function(pattern_id, mod, fn_info, cls, gen, outfh, wild_scale=scale)
                    _write_row(outfh, seed, offset, pattern_id, fn_name, cls, outcome, exc_type, note, wild_scale=scale)
                    rows_written += 1
                    summary[cls].append((outcome, exc_type, note))
            else:
                outcome, exc_type, note = _probe_function(pattern_id, mod, fn_info, cls, gen, outfh)
                _write_row(outfh, seed, offset, pattern_id, fn_name, cls, outcome, exc_type, note)
                rows_written += 1
                summary[cls].append((outcome, exc_type, note))

    # Emit pattern-level summary row per class.
    # Worst-outcome-wins, ordered: THREW > NaN-Inf > DIVERGED > INCONCLUSIVE > FINITE.
    for cls in CLASSES:
        results = summary[cls]
        if not results:
            _write_row(outfh, seed, offset, pattern_id, "_summary", cls, "INCONCLUSIVE", "", "no functions probed")
            continue
        best = max(results, key=lambda t: _OUTCOME_RANK.get(t[0], -1))
        summary_note = f"summary over {len(results)} function(s); worst={best[0]}"
        _write_row(outfh, seed, offset, pattern_id, "_summary", cls, best[0], best[1], summary_note)
        rows_written += 1

    return rows_written


def main():
    parser = argparse.ArgumentParser(description="Probe python pattern robustness on synthetic input classes.")
    parser.add_argument("--patterns", required=True, help="directory containing pattern .py files")
    parser.add_argument("--registry", required=True, help="entry_points_sample.jsonl path")
    parser.add_argument("--seed", type=int, default=20260804, help="random seed")
    parser.add_argument("--uncentred-offset", type=float, default=10.0,
                        help="offset for uncentred input class; 5S measured flip near 5-6")
    parser.add_argument("--out", default="/home/au/ai-lab/robustness-kit/SAMPLE_RESULTS_R2.tsv",
                        help="output TSV path")
    args = parser.parse_args()

    random.seed(args.seed)
    gen = InputGenerator(args.seed, uncentred_offset=args.uncentred_offset)

    patterns_dir = Path(args.patterns)
    with open(args.registry) as f:
        registries = [json.loads(line) for line in f if line.strip()]

    # Write header.
    with open(args.out, "w") as outfh:
        outfh.write("seed\tuncentred_offset\tpattern\tfunction\tclass\twild_scale\toutcome\texception\tnote\n")
        outfh.flush()

        for reg in registries:
            pattern_file = patterns_dir / f"{reg['id']}.py"
            if not pattern_file.exists():
                for cls in CLASSES:
                    _write_row(outfh, args.seed, args.uncentred_offset, reg["id"], None,
                               cls, "INCONCLUSIVE", "", f"missing file: {pattern_file}")
                continue
            _probe_pattern(pattern_file, reg, gen, args.seed, args.uncentred_offset, outfh)

    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
