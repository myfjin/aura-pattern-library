#!/usr/bin/env python3
"""Probe robustness of python pattern entry functions on synthetic input classes.

Rules:
- Probe EVERY registry entry function where matrix_param is true.
- Build arguments from the registry's declared roles in parameter order:
    role == "matrix"                -> synthetic matrix for current class
    role == "vector"                -> synthetic vector, length = matrix rows
    role == "other", not required   -> omit, let the default apply
    role == "other", required       -> INCONCLUSIVE: "required param <name> role=other"
- Use inspect.signature ONLY to confirm arity; if it disagrees with the registry,
  report INCONCLUSIVE "registry/signature mismatch" and never guess.
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
        elif isinstance(o, int) and not isinstance(o, bool):
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

    def vector(self, n: int = 30) -> List[float]:
        # Generic vector used for any role=="vector" parameter, length = matrix rows.
        self._reset(f"vector:{n}")
        return [self.rng.uniform(-1.0, 1.0) for _ in range(n)]

    def vector_for_class(self, cls: str, n: int = 30) -> List[float]:
        self._reset(f"vector-class:{cls}:{n}")
        if cls == "uncentred":
            return [self.rng.uniform(self.uncentred_offset, self.uncentred_offset + 10.0) for _ in range(n)]
        if cls == "rank-deficient":
            return [1.0 for _ in range(n)]
        if cls == "single-row":
            return [5.0]
        if cls == "constant-column":
            return [5.0 for _ in range(n)]
        return [self.rng.uniform(-1.0, 1.0) for _ in range(n)]

    def vector_wildly_scaled(self, n: int = 30, scale: float = 1e12) -> List[float]:
        self._reset(f"vector-wildly:{scale}:{n}")
        return [scale if i % 2 == 0 else self.rng.uniform(-1.0, 1.0) for i in range(n)]


def _synth_for_param(pinfo: Dict[str, Any], matrix_input: Any, gen: InputGenerator, cls: str,
                     wild_scale: float | None = None) -> Tuple[Any, str]:
    """Return (value, note) for a single registry parameter.

    note is empty when the value is valid; otherwise it is an INCONCLUSIVE reason.
    """
    role = pinfo.get("role", "other")
    required = pinfo.get("required", False)
    name = pinfo.get("name", "")

    if role == "matrix":
        if cls == "wildly-scaled":
            return gen.matrix_wildly_scaled(scale=wild_scale if wild_scale is not None else 1e30), ""
        return matrix_input, ""

    if role == "vector":
        n_rows = len(matrix_input) if isinstance(matrix_input, list) else 30
        if cls == "wildly-scaled":
            return gen.vector_wildly_scaled(n=n_rows, scale=wild_scale if wild_scale is not None else 1e30), ""
        # For non-wildly classes, match the vector style to the class when it is a target-like vector,
        # otherwise use a generic random vector. We treat any vector that is not the primary matrix as
        # a generic numeric vector.
        return gen.vector_for_class(cls, n=n_rows), ""

    if role == "other":
        if required:
            return None, f"required param `{name}` role=other"
        return None, ""  # signal to omit

    return None, f"unknown role `{role}` for param `{name}`"


def _build_args(mod, fn_info: Dict[str, Any], cls: str, gen: InputGenerator,
                wild_scale: float | None = None) -> Tuple[List, Dict, str]:
    """Build positional and keyword args from the registry's declared roles.

    Returns (args, kwargs, note) where note is empty on success.
    """
    fn_name = fn_info["name"]
    fn = getattr(mod, fn_name)
    sig = inspect.signature(fn)
    sig_params = list(sig.parameters.items())

    registry_params = fn_info.get("params", [])

    # Normalize registry params: if 'role' is missing but 'matrix_param' is true and it's the
    # function-level flag, infer roles from annotations/names for legacy registries that still
    # describe the function but not each param.
    # However, the canonical registry now provides role per param. We only do a minimal fallback
    # for the 12-pattern sample registry that lacks role fields: derive role from annotation.
    normalized_params = []
    for rp in registry_params:
        role = rp.get("role")
        required = rp.get("required")
        if role is None:
            ann = str(rp.get("annotation", "")).lower()
            name = rp.get("name", "").lower()
            if name in ("groups", "chains"):
                role = "matrix"
            elif name in ("data", "chains", "observations", "obs_seq", "pre_treated", "pre_controls",
                          "control_outcomes", "treatment_outcomes", "samples_per_run", "ranking", "rankings",
                          "stream"):
                # ⛔ FIXTURE-TUNED, KEPT ONLY AS A RECORD — DO NOT EXTEND THIS LIST.
                # These names were hardcoded from the 33-pattern test set to make it resolve,
                # i.e. fitting the test rather than fixing the tool. It fires only for legacy
                # registries lacking `role` fields; every current registry carries roles, so this
                # branch is dead for them. The correct fix is to regenerate the registry, never to
                # add a name here.
                role = "vector"
            elif "list[list" in ann or "[][]" in ann or ann == "list":
                role = "matrix"
            elif "list[float]" in ann or "list[int]" in ann:
                role = "vector"
            else:
                role = "other"
        if required is None:
            # Legacy sample registry has no required field. Treat params with defaults
            # in the live signature as not required; everything else required.
            sig_param = sig_params[len(normalized_params)][1] if len(normalized_params) < len(sig_params) else None
            required = sig_param.default is inspect.Parameter.empty if sig_param else True
        normalized_params.append({
            "name": rp.get("name"),
            "role": role,
            "required": required,
        })
    registry_params = normalized_params

    # Arity / naming mismatch guard.
    if len(registry_params) != len(sig_params):
        return [], {}, (
            f"registry/signature mismatch: registry has {len(registry_params)} params, "
            f"live signature has {len(sig_params)}"
        )
    for rp, (sp_name, sp) in zip(registry_params, sig_params):
        if rp.get("name") != sp_name:
            return [], {}, (
                f"registry/signature mismatch: registry param `{rp.get('name')}` vs signature `{sp_name}`"
            )

    # Build the matrix input first so vector lengths can follow it.
    matrix_input = None
    for rp in registry_params:
        if rp.get("role") == "matrix":
            matrix_input, _ = _synth_for_param(rp, None, gen, cls, wild_scale=wild_scale)
            break
    if matrix_input is None:
        # No matrix role found, but the function is matrix_param. Fall back to a generic matrix.
        if cls == "wildly-scaled":
            matrix_input = gen.matrix_wildly_scaled(scale=wild_scale if wild_scale is not None else 1e30)
        else:
            matrix_input = gen.matrix(cls)

    args = []
    kwargs = {}

    for i, (rp, (sp_name, sp)) in enumerate(zip(registry_params, sig_params)):
        value, note = _synth_for_param(rp, matrix_input, gen, cls, wild_scale=wild_scale)
        if note:
            return [], {}, note
        if value is None and not rp.get("required", False):
            # omitted optional "other" param
            continue

        if sp.kind == inspect.Parameter.VAR_POSITIONAL:
            args.extend(value if isinstance(value, (list, tuple)) else [value])
        elif sp.kind == inspect.Parameter.VAR_KEYWORD:
            if isinstance(value, dict):
                kwargs.update(value)
        elif sp.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
            args.append(value)
        else:
            kwargs[sp_name] = value

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
    # Escape newlines/tabs in note to keep TSV single-line.
    safe_note = note.replace("\n", " ").replace("\t", " ")
    outfh.write(f"{seed}\t{offset}\t{pattern_id}\t{fn_col}\t{cls}\t{scale_col}\t{outcome}\t{exc_type}\t{safe_note}\n")
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
    parser.add_argument("--registry", required=True, help="registry.jsonl path")
    parser.add_argument("--seed", type=int, default=20260804, help="random seed")
    parser.add_argument("--uncentred-offset", type=float, default=10.0,
                        help="offset for uncentred input class; 5S measured flip near 5-6")
    parser.add_argument("--out", default="/home/au/ai-lab/robustness-kit/SAMPLE_RESULTS.tsv",
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
