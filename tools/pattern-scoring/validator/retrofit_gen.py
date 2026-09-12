#!/usr/bin/env python3
"""
retrofit_gen.py — generate accumulate-then-raise input contracts for the silent-acceptance
queue, poured ONLY where the tool's own attacks proved a guard is missing. NEVER touches the
library: writes retrofitted copies to a sandbox, then makes the validator VERIFY its own fix
(re-attack must now raise · self-test must stay green · determinism must hold).

Guard classes emitted (the AUTO-SAFE ones — R1 blunt-underflow is DELIBERATELY excluded:
a -1e9 mean-shift can be legitimate, so it routes to the model-assisted docstring lane):
  R15 scalar NaN/Inf  -> AURA-E008: value must be finite
  R9  degenerate      -> AURA-E009: count/window param must be > 0
  R2  domain-aware    -> AURA-E001/E003: name-implied domain (prob[0,1], alpha(0,1), rate>0, u[0,1))

Usage:
  python3 retrofit_gen.py --batch 10           # first 10 queue patterns -> sandbox + verify
  python3 retrofit_gen.py --file <relpath>     # single pattern
"""
import os, sys, ast, math, shutil, subprocess, glob
from executor import (load_module, entry_functions, build_baseline, attack_fixtures,
                      _call, _has_nan_out, _finite_or_full, LIB)

SANDBOX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "retrofit_gen_out")

# param-name -> (domain family) for R2 guards. NARROWER than executor.DOMAIN_ATTACKS:
# bare "alpha"/"beta" are EXCLUDED from auto (batch-1 finding: alpha = smoothing strength
# in target_encoding [0 legit], Beta shape in beta_binomial [1.73 legit] — the most
# overloaded names in DS; they route to the model-assisted docstring lane).
DOMAIN_FAMILIES = [
    (("p1","p2","prob","probability","rate_a","rate_b"), "prob"),      # [0,1]  E003
    (("significance","level"),                            "alpha"),     # (0,1)  E001
    (("rate","lambda","lam"),                             "posrate"),   # >0     E001
    (("u","quantile","q","percentile"),                   "u"),         # [0,1)  E003
    (("var","variance","sigma","std","sd"),               "nonneg"),    # >=0    E-B5
]
COUNT_STEMS = ("k","window","breaks","bins","num","order","n","size","trials","count")

GUARD = {  # family -> (predicate-of-P-that-is-BAD, message)
    "prob":    ("not (0.0 <= {P} <= 1.0)",  'AURA-E003: {n} must be in [0,1], got {{{P}}}'),
    "alpha":   ("not (0.0 < {P} < 1.0)",    'AURA-E001: {n} must be in (0,1), got {{{P}}}'),
    "posrate": ("{P} <= 0",                 'AURA-E001: {n} must be > 0, got {{{P}}}'),
    "u":       ("not (0.0 <= {P} < 1.0)",   'AURA-E003: {n} must be in [0,1), got {{{P}}}'),
    "nonneg":  ("{P} < 0",                  'AURA-E-B5: {n} must be >= 0, got {{{P}}}'),
}

def _domain_family(pname):
    pl = pname.lower()
    for names, fam in DOMAIN_FAMILIES:
        if pl in names or any(pl == n or pl.endswith("_" + n) for n in names):
            return fam
    return None

def _is_count(pname):
    pl = pname.lower()
    return any(w in pl for w in COUNT_STEMS)


def accepted_guards(relpath):
    """Return {fnname: {argname: set(of guard-kinds)}} for attacks the pattern SILENTLY accepts.
    guard-kinds: 'finite' (R15), 'positive_count' (R9), 'domain:<family>' (R2)."""
    module, err = load_module(relpath)
    if err:
        return None, f"load error: {err}"
    spec = {}
    for name, fn, sig, params in entry_functions(module, relpath):
        base, ok = build_baseline(params)
        if not ok:
            continue
        pnames = [p.name for p in params]
        per_arg = {}
        for recipe, margs, ec, idx in attack_fixtures(params, base):
            r = _call(fn, margs)
            out = r.get("output")
            if r["raised"] or _has_nan_out(out):
                continue  # loud rejection or visible poison -> not a silent-accept
            if not _finite_or_full(out):
                continue
            arg = pnames[idx] if idx < len(pnames) else None
            if arg is None:
                continue
            if recipe == "R15_scalar_nan_inf":
                per_arg.setdefault(arg, set()).add("finite")
            elif recipe == "R9_degenerate_param" and _is_count(arg):
                per_arg.setdefault(arg, set()).add("positive_count")
            elif recipe == "R2_domain_aware":
                fam = _domain_family(arg)
                if fam:
                    per_arg.setdefault(arg, set()).add("domain:" + fam)
            # R1_domain_under DELIBERATELY not guarded (may be legitimate) -> model lane
        if per_arg:
            spec[name] = per_arg
    return spec, None


def _guard_lines(per_arg):
    """Emit accumulate-then-raise guard lines for one function's arg->kinds map."""
    lines = []
    for arg, kinds in per_arg.items():
        num_guarded = False
        if "finite" in kinds:
            lines.append(f'    if isinstance({arg}, (int, float)) and not math.isfinite({arg}):')
            lines.append(f'        v.append(f"AURA-E008: {arg} must be finite, got {{{arg}}}")')
            num_guarded = True
        if "positive_count" in kinds:
            lines.append(f'    if isinstance({arg}, (int, float)) and {arg} <= 0:')
            lines.append(f'        v.append(f"AURA-E009: {arg} must be > 0, got {{{arg}}}")')
            num_guarded = True
        for k in kinds:
            if k.startswith("domain:"):
                fam = k.split(":", 1)[1]
                pred, msg = GUARD[fam]
                pred = pred.format(P=arg)
                msg = msg.format(n=arg, P=arg)
                lines.append(f'    if isinstance({arg}, (int, float)) and {pred}:')
                lines.append(f'        v.append(f"{msg}")')
                num_guarded = True
    return lines


def retrofit_source(relpath, spec):
    """Return retrofitted source text: AuraInputError + per-fn validators + injected calls."""
    src = open(os.path.join(LIB, relpath), encoding="utf-8").read()
    tree = ast.parse(src)
    lines = src.splitlines(keepends=True)

    # ensure MODULE-LEVEL `import math` (guards use math.isfinite at module scope).
    # a function-LOCAL `import math` does not satisfy the module-level validators — the
    # generator must add its own top-level import (stratification_subclassification find).
    has_math = any(isinstance(n, ast.Import) and any(a.name == "math" for a in n.names)
                   for n in tree.body)

    # build the injected block: AuraInputError once + one validator per guarded fn
    err_class = (
        "\n\nclass AuraInputError(ValueError):\n"
        '    """All input-contract violations, reported together (accumulate-then-raise)."""\n'
        "    def __init__(self, violations):\n"
        "        self.violations = violations\n"
        '        super().__init__("input contract violated:\\n  " + "\\n  ".join(violations))\n'
    )
    validators = [err_class]
    for fnname, per_arg in spec.items():
        args = ", ".join(per_arg.keys())
        body = _guard_lines(per_arg)
        validators.append(
            f"\ndef _aura_validate_{fnname}({args}):\n"
            f"    v = []\n" + "\n".join(body) + "\n"
            f"    if v:\n        raise AuraInputError(v)\n"
        )
    inject_block = "".join(validators) + "\n"

    # collect all insertions as (line_idx0, text); apply bottom-up so indices stay valid.
    edits = []  # (insert_lineno_0based, text)
    guarded_def_lines = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in spec:
            guarded_def_lines.append(node.lineno)
            first = node.body[0]
            after = first if isinstance(first, ast.Expr) and isinstance(
                getattr(first, "value", None), ast.Constant) and isinstance(
                first.value.value, str) else None
            insert_line = (after.end_lineno if after else node.body[0].lineno - 1)
            body_indent = " " * (node.body[0].col_offset)
            args = ", ".join(spec[node.name].keys())
            call = f"{body_indent}_aura_validate_{node.name}({args})\n"
            edits.append((insert_line, call))

    # the validator block must be DEFINED before any code that runs it (the __main__ demo
    # calls the entry fns). Insert it just above the EARLIEST guarded function definition.
    block_line0 = min(guarded_def_lines) - 1
    # walk back over any decorator/blank lines directly above the def
    while block_line0 > 0 and lines[block_line0 - 1].lstrip().startswith("@"):
        block_line0 -= 1
    edits.append((block_line0, inject_block))

    for insert_line, text in sorted(edits, key=lambda e: -e[0]):
        lines.insert(insert_line, text)

    out = "".join(lines)
    if not has_math:
        out = "import math\n" + out
    return out


def verify(relpath, sandbox_path, spec):
    """The tool verifies its OWN fix: (1) each accepted attack now RAISES,
    (2) self-test (__main__) still green, (3) deterministic."""
    result = {"attacks_closed": 0, "attacks_total": 0, "selftest": None, "deterministic": None}
    # 1. re-attack the sandbox copy: every guarded arg's attack must now raise
    m, err = load_module(os.path.relpath(sandbox_path, LIB)) if sandbox_path.startswith(LIB) \
        else _load_abs(sandbox_path)
    if err:
        result["selftest"] = f"sandbox load error: {err}"
        return result
    for name, fn, sig, params in entry_functions(m, os.path.relpath(sandbox_path, LIB)
                                                 if sandbox_path.startswith(LIB) else relpath):
        if name not in spec:
            continue
        base, ok = build_baseline(params)
        if not ok:
            continue
        pnames = [p.name for p in params]
        for recipe, margs, ec, idx in attack_fixtures(params, base):
            arg = pnames[idx] if idx < len(pnames) else None
            if arg not in spec[name]:
                continue
            kinds = spec[name][arg]
            relevant = ((recipe == "R15_scalar_nan_inf" and "finite" in kinds) or
                        (recipe == "R9_degenerate_param" and "positive_count" in kinds) or
                        (recipe == "R2_domain_aware" and any(k.startswith("domain:") for k in kinds)))
            if not relevant:
                continue
            result["attacks_total"] += 1
            r = _call(fn, margs)
            if r["raised"] and "AuraInputError" in (r.get("error_text") or ""):
                result["attacks_closed"] += 1
    # 2 + 3. self-test twice (determinism) via subprocess
    r1 = subprocess.run([sys.executable, sandbox_path], capture_output=True, text=True, timeout=90)
    r2 = subprocess.run([sys.executable, sandbox_path], capture_output=True, text=True, timeout=90)
    result["selftest"] = "GREEN" if r1.returncode == 0 else f"RED rc={r1.returncode}: {r1.stderr[-200:]}"
    result["deterministic"] = (r1.stdout == r2.stdout)
    return result


def _load_abs(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("sbx_" + str(abs(hash(path))), path)
    m = importlib.util.module_from_spec(spec)
    try:
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
        return m, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def _exam_files():
    """The graded patterns ARE the ruler — never retrofit them. Hardening a frozen
    INVALID silently destroys its regression signal (inverse_transform find 2026-07-21:
    a rate>0 guard fixed the exact defect its probe kills for -> verdict flipped)."""
    import json as _j
    ex = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "exam.json")))
    return {e["file"] for e in ex["frozen"] + ex["expansion"]}

def queue_files():
    exam = _exam_files()
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "python/data-science", "**", "*.py"), recursive=True))
    out = []
    for f in files:
        if f in exam:            # the ruler is off-limits to the auto lane
            continue
        spec, err = accepted_guards(f)
        if spec:
            out.append((f, spec))
    return out


def main():
    args = sys.argv[1:]
    os.makedirs(SANDBOX, exist_ok=True)
    if "--file" in args:
        rel = args[args.index("--file") + 1]
        spec, err = accepted_guards(rel)
        targets = [(rel, spec)] if spec else []
    else:
        n = int(args[args.index("--batch") + 1]) if "--batch" in args else 10
        targets = queue_files()[:n]

    print(f"RETROFIT GENERATOR — {len(targets)} patterns (sandbox: {SANDBOX})")
    print("=" * 90)
    rows = []
    for rel, spec in targets:
        base = os.path.basename(rel)
        sbx = os.path.join(SANDBOX, base)
        try:
            src = retrofit_source(rel, spec)
            open(sbx, "w", encoding="utf-8").write(src)
            v = verify(rel, sbx, spec)
            # SELF-CALIBRATION (batch-1 lesson): if the pattern's OWN demo trips a guard,
            # the demo disproves that domain — drop every guard on that arg, regenerate.
            # (Demo-green wins in the AUTO lane; disputed domains go to the judgment lane.)
            for _ in range(3):
                st = v.get("selftest") or ""
                if not (st.startswith("RED") and "AuraInputError" in st):
                    break
                import re as _re
                mo = _re.search(r"AURA-E[\w-]*: (\w+) must", st)
                if not mo:
                    break
                bad_arg = mo.group(1)
                for fname in list(spec):
                    spec[fname].pop(bad_arg, None)
                    if not spec[fname]:
                        del spec[fname]
                if not spec:
                    break
                src = retrofit_source(rel, spec)
                open(sbx, "w", encoding="utf-8").write(src)
                v = verify(rel, sbx, spec)
                v["note"] = f"self-calibrated: dropped guards on '{bad_arg}' (demo disproved domain)"
            if not spec:
                rows.append(("JUDGE", base, "0/0", "all guards demo-disproved", None, 0))
                print(f"  [JUDGE ] {base:44} all auto-guards disproved by demo -> judgment lane")
                continue
            closed = f"{v['attacks_closed']}/{v['attacks_total']}"
            status = ("OK" if v["attacks_closed"] == v["attacks_total"] and v["selftest"] == "GREEN"
                      and v["deterministic"] else "REVIEW")
            guards = sum(len(a) for a in spec.values())
            rows.append((status, base, closed, v["selftest"], v["deterministic"], guards))
            print(f"  [{status:6}] {base:44} attacks_closed={closed:6} "
                  f"selftest={v['selftest']:6} det={v['deterministic']!s:5} guards={guards}")
        except Exception as e:
            rows.append(("ERROR", base, "-", str(e)[:40], None, 0))
            print(f"  [ERROR ] {base:44} {e}")
    ok = sum(1 for r in rows if r[0] == "OK")
    print("=" * 90)
    print(f"CLEAN CLOSURE: {ok}/{len(rows)} patterns — attacks now raise, self-test green, deterministic")
    print(f"diffs: diff <(sed -n /dev/null) ; compare {SANDBOX}/<file> vs library original")

if __name__ == "__main__":
    main()
