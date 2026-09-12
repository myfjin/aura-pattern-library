#!/usr/bin/env python3
"""
compiled_harness.py — the COMPILED-LANGUAGE ATTACK LANE (open-loop item 9, lane A).

`polyglot.py` says it plainly: "Deep attack-injection stays python-only (executor.py) until
compiled-language harness editing lands (v2)." This is that v2 for Go.

WHAT IT DOES
Python patterns get attacked by importing the module and calling functions with poisoned args.
A compiled language cannot be driven that way, so this harness attacks at SOURCE level:

  1. parse `func Name(...) ret {` and keep only signatures it can honestly construct
     (float64 / int / []float64 / []int / string / bool — everything else is SKIPPED and counted)
  2. copy the pattern into a temp package dir, renaming its own `main` so it does not run
  3. emit a SECOND file in that package holding the attack driver
     (a separate file because Go requires imports before declarations — appending is illegal)
  4. `go run` the package; each call is wrapped in its own recover() so a panic is DATA, not a
     lost run
  5. classify exactly as the python lane does — same words, same meaning

CLASSES  (identical semantics to nan_domain_probe.py)
  FABRICATED_CERTAINTY  NaN in -> finite output, no panic       conclusive-kill class
  VISIBLE_POISON        NaN in -> NaN/Inf out                   honest propagation
  OVERFLOW_WRAP         1<<62 in -> silently wrapped/zeroed      the typed-language class
                        (python/R cannot have this: LANG_PRIORS overflow=0.0 there, 1.3 for go)
  GUARDED               the call panicked / returned an error    good
  NO_OP_ATTACK          output identical to baseline            unreachable — never a kill

HONEST LIMITS
- Only functions whose full signature is constructible are attacked; every skip is counted and
  reported. Coverage is stated, never implied.
- A Go function returning `(value, error)` that sets error is GUARDED — that is the idiomatic
  guard and the harness must not read it as a defect.
- This proves behaviour of the FUNCTION under poison. It is not a proof of the pattern's claim.
"""
import json, os, re, shutil, signal, subprocess, sys, tempfile


def run_in_process_group(cmd, cwd, timeout):
    """Run a command and, on timeout, kill its ENTIRE process group.

    THIS IS NOT A STYLE CHOICE — it cost a cooked laptop on 2026-07-27.
    `go run` COMPILES to a temp binary and executes it as a CHILD process. plain
    subprocess.run(timeout=...) kills only its direct child (`go run`) and leaves that
    grandchild binary running. Several of the attacked patterns block forever (channel
    receives, barrier awaits), so each timeout leaked a spinning binary: six of them
    accumulated at ~100% CPU each, load average 11+, fans at maximum, and they survived
    even `pkill -f compiled_harness` because they were reparented to launchd.

    start_new_session=True puts the child in its own process group; killpg then takes the
    whole tree — `go run` and the binary it spawned."""
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, start_new_session=True)
    try:
        out, err = p.communicate(timeout=timeout)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            p.kill()
        try:
            out, err = p.communicate(timeout=10)
        except Exception:
            out, err = "", ""
        return 124, out, err

LIB = os.path.expanduser("~/aura-pattern-library")
HERE = os.path.dirname(os.path.abspath(__file__))

FUNC_RE = re.compile(r'^func\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*([^{]*?)\s*\{', re.M)

# types this harness can honestly build a value for
SIMPLE = {"float64", "int", "int64", "string", "bool", "[]float64", "[]int", "[]string"}


def parse_params(param_src):
    """Go allows grouped decls: `a, b float64, n int`. Return [(name, type)] or None if any
    parameter is of a type we cannot construct."""
    param_src = param_src.strip()
    if not param_src:
        return []
    parts = [p.strip() for p in param_src.split(",") if p.strip()]
    out, pending = [], []
    for p in parts:
        toks = p.split()
        if len(toks) == 1:              # bare name in a group: `a, b float64`
            pending.append(toks[0])
            continue
        if len(toks) != 2:
            return None
        name, typ = toks
        if typ not in SIMPLE:
            return None
        for q in pending:
            out.append((q, typ))
        pending = []
        out.append((name, typ))
    if pending:
        return None
    return out


def baseline_value(typ):
    return {"float64": "2.0", "int": "3", "int64": "3", "string": '"abc"', "bool": "true",
            "[]float64": "[]float64{1.0, 2.0, 3.0, 4.0}", "[]int": "[]int{1, 2, 3, 4}",
            "[]string": '[]string{"a", "b"}'}[typ]


def attacks_for(typ):
    """(label, go-literal) attack values per type."""
    if typ == "float64":
        return [("nan", "math.NaN()"), ("inf", "math.Inf(1)"), ("neg", "-1.0")]
    if typ in ("int", "int64"):
        return [("overflow", "int(1) << 62"), ("zero", "0"), ("neg", "-1")]
    if typ == "[]float64":
        return [("nan", "[]float64{math.NaN(), 2.0, 3.0, 4.0}"),
                ("inf", "[]float64{math.Inf(1), 2.0, 3.0, 4.0}"),
                ("empty", "[]float64{}")]
    if typ == "[]int":
        return [("empty", "[]int{}"), ("overflow", "[]int{1 << 62, 2, 3}")]
    if typ == "[]string":
        return [("empty", "[]string{}")]
    if typ == "string":
        return [("empty", '""')]
    return []


def build_driver(fname, params, cases):
    """Emit the driver file. Every call is isolated behind its own recover() so one panic
    cannot abort the remaining fixtures."""
    lines = ["package main", "", 'import (', '\t"fmt"', '\t"math"', ')', "",
             "var _ = math.NaN", "",
             "func auraCall(tag string, f func()) {",
             "\tdefer func() {",
             "\t\tif r := recover(); r != nil {",
             '\t\t\tfmt.Printf("AURA|%s|PANIC|%v\\n", tag, r)',
             "\t\t}",
             "\t}()",
             "\tf()",
             "}", "",
             "func main() {"]
    for tag, argexprs in cases:
        call = f"{fname}({', '.join(argexprs)})"
        lines.append(f'\tauraCall("{tag}", func() {{')
        lines.append(f'\t\tres := fmt.Sprintf("%v", {call})')
        lines.append(f'\t\tfmt.Printf("AURA|%s|OK|%s\\n", "{tag}", res)')
        lines.append("\t})")
    lines.append("}")
    return "\n".join(lines) + "\n"


def harness_file(relpath, timeout=30):
    """Attack every drivable function in one Go pattern. Returns a card."""
    src_path = os.path.join(LIB, relpath)
    src = open(src_path, encoding="utf-8", errors="replace").read()

    targets, skipped = [], []
    for m in FUNC_RE.finditer(src):
        name, psrc, ret = m.group(1), m.group(2), m.group(3).strip()
        if name in ("main", "init"):
            continue
        params = parse_params(psrc)
        if params is None:
            skipped.append({"fn": name, "why": f"unconstructible signature: ({psrc.strip()[:60]})"})
            continue
        if not params or not any(t in ("float64", "[]float64", "int", "int64", "[]int")
                                 for _, t in params):
            skipped.append({"fn": name, "why": "no numeric parameter to poison"})
            continue
        # Void functions have nothing to observe but a panic; everything else IS drivable,
        # including the idiomatic `(value, error)` pair — Go lets a multi-value call be passed
        # as the sole argument to a variadic function, so `auraWrap(f(x))` captures both.
        # Excluding those would have dropped most of the Go corpus (measured: 27 of 31 skipped).
        if ret == "":
            skipped.append({"fn": name, "why": "void return — nothing to observe but a panic"})
            continue
        targets.append((name, params, ret))

    if not targets:
        return {"file": relpath, "class": "NO_EVIDENCE", "drivable": 0,
                "skipped": skipped, "results": []}

    tmp = tempfile.mkdtemp(prefix="aura_go_")
    try:
        # 1. copy pattern with its own main neutralised
        patched = re.sub(r'^func\s+main\s*\(\s*\)\s*\{', 'func auraOrigMain() {', src, count=1, flags=re.M)
        open(os.path.join(tmp, "pattern.go"), "w").write(patched)
        # `go run .` needs a module context; the patterns are standalone files with no go.mod
        open(os.path.join(tmp, "go.mod"), "w").write("module auraharness\n\ngo 1.21\n")

        cases, meta = [], []
        rets = {f: r for f, _p, r in targets}
        for fname, params, _ret in targets:
            base = [baseline_value(t) for _, t in params]
            cases.append((f"{fname}#baseline", list(base)))
            meta.append((f"{fname}#baseline", fname, "baseline", "-"))
            for i, (pname, ptyp) in enumerate(params):
                for label, expr in attacks_for(ptyp):
                    args = list(base)
                    args[i] = expr
                    tag = f"{fname}#{pname}#{label}"
                    cases.append((tag, args))
                    meta.append((tag, fname, label, pname))

        open(os.path.join(tmp, "aura_driver.go"), "w").write(
            build_driver_multi(targets, cases))

        rc, stdout, stderr = run_in_process_group(["go", "run", "."], tmp, timeout)
        if rc == 124 and "AURA|" not in stdout:
            return {"file": relpath, "class": "NO_EVIDENCE", "drivable": len(targets),
                    "skipped": skipped, "results": [],
                    "reason": "timeout — blocking call; process group killed"}
        class _P:  # keep the downstream reads unchanged
            pass
        p = _P(); p.returncode, p.stdout, p.stderr = rc, stdout, stderr
        if p.returncode != 0 and "AURA|" not in p.stdout:
            return {"file": relpath, "class": "NO_EVIDENCE", "drivable": len(targets),
                    "skipped": skipped, "results": [],
                    "reason": "driver did not build: " + (p.stderr or "")[-200:]}

        observed = {}
        for line in p.stdout.splitlines():
            if not line.startswith("AURA|"):
                continue
            bits = line.split("|", 3)
            if len(bits) < 4:
                continue
            observed[bits[1]] = (bits[2], bits[3])
        return classify(relpath, meta, observed, skipped, len(targets), rets)
    except subprocess.TimeoutExpired:
        return {"file": relpath, "class": "NO_EVIDENCE", "drivable": len(targets),
                "skipped": skipped, "results": [], "reason": "timeout"}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def build_driver_multi(targets, cases):
    lines = ["package main", "", "import (", '\t"fmt"', '\t"math"', ")", "",
             "var _ = math.NaN", "",
             "func auraWrap(vs ...interface{}) string {",
             "\treturn fmt.Sprint(vs...)",
             "}", "",
             "func auraCall(tag string, f func()) {",
             "\tdefer func() {",
             "\t\tif r := recover(); r != nil {",
             '\t\t\tfmt.Printf("AURA|%s|PANIC|%v\\n", tag, r)',
             "\t\t}",
             "\t}()",
             "\tf()",
             "}", "",
             "func main() {"]
    for tag, argexprs in cases:
        fname = tag.split("#")[0]
        lines.append(f'\tauraCall("{tag}", func() {{')
        lines.append(f'\t\tres := auraWrap({fname}({", ".join(argexprs)}))')
        lines.append(f'\t\tfmt.Printf("AURA|%s|OK|%s\\n", "{tag}", res)')
        lines.append("\t})")
    lines.append("}")
    return "\n".join(lines) + "\n"


def _is_poisoned_out(text):
    t = text.lower()
    return "nan" in t or "+inf" in t or "-inf" in t


BIG = str(1 << 62)          # 4611686018427387904
_NOISE = [
    re.compile(r"0x[0-9a-f]+"),                     # pointer addresses
    re.compile(r"\d{4}-\d{2}-\d{2}[ T][\d:.+\-]+"),  # timestamps
    re.compile(r"m=\+[\d.]+"),                       # go monotonic clock reading
    re.compile(r"evt-\d+"),                          # monotonically increasing demo ids
]


def _normalize(text):
    """Strip nondeterministic fields before any baseline comparison.

    Measured, not theoretical: `event_sourcing_store` outputs differ run-to-run by event id,
    wall-clock timestamp and pointer address. Comparing raw strings made every attack look
    like it 'changed the result' and produced two false OVERFLOW_WRAP kills on the first run."""
    for rx in _NOISE:
        text = rx.sub("~", text)
    return text


def _overflow_class(payload, baseline):
    """Distinguish a REAL silent wrap from a faithfully-stored large value.

    recipes.py records the true class from GO batch 1: a Duration computation that receives a
    huge int comes out as *exactly 0* and the backoff silently vanishes. If the huge value
    appears verbatim in the output it was stored correctly — that is NOT a wrap, and calling it
    one is a false kill (caught by hand on this harness's first run)."""
    if BIG in payload:
        return "VALUE_PRESERVED"
    if re.search(r"(^|[^\w.])-\d", payload):        # a negative appeared
        return "OVERFLOW_WRAP"
    if re.fullmatch(r"[{\[(]?\s*0(\s|[}\])]|$)", payload.strip()[:12]):
        return "OVERFLOW_WRAP"                       # collapsed to exactly zero
    return "VALUE_PRESERVED"


ORDER = {"FABRICATED_CERTAINTY": 5, "OVERFLOW_WRAP": 4, "VISIBLE_POISON": 3,
         "NO_OP_ATTACK": 2, "VALUE_PRESERVED": 1, "GUARDED": 1, "NO_EVIDENCE": 0}


def classify(relpath, meta, observed, skipped, drivable, rets=None):
    worst, results = "NO_EVIDENCE", []
    baselines = {tag.split("#")[0]: observed.get(tag, ("", ""))[1]
                 for tag, fn, lab, p in meta if lab == "baseline"}
    # BASELINE-VALIDITY GUARD (same law as the R lane): a function whose CLEAN call already
    # panicked or already produced NaN/Inf was never validly exercised, so nothing measured
    # against it can be called a defect.
    invalid_base = set()
    for tag, fn, lab, p in meta:
        if lab != "baseline":
            continue
        st, pay = observed.get(tag, ("MISSING", ""))
        if st != "OK" or _is_poisoned_out(pay):
            invalid_base.add(fn)

    for tag, fname, label, pname in meta:
        if label == "baseline" or tag not in observed or fname in invalid_base:
            continue
        status, payload = observed[tag]
        returns_err = "error" in (rets or {}).get(fname, "")
        errored = returns_err and "<nil>" not in payload
        if status == "PANIC":
            cls = "GUARDED"
        elif errored:
            cls = "GUARDED"        # returned a non-nil error — the idiomatic Go guard
        elif _is_poisoned_out(payload):
            cls = "VISIBLE_POISON"
        elif _normalize(payload) == _normalize(baselines.get(fname) or ""):
            cls = "NO_OP_ATTACK"
        elif label == "nan" and (rets or {}).get(fname, "").strip() == "bool":
            # A PREDICATE returning false for NaN is the mathematically correct answer, not a
            # fabricated one: NaN is not approximately-equal / less-than / inside-range for any
            # value. Caught by hand — `approxEqual(NaN, b, tol) -> false` is right, and calling
            # it a kill would demote a correct pattern.
            cls = "GUARDED"
        elif label == "nan":
            cls = "FABRICATED_CERTAINTY"
        elif label == "overflow":
            cls = _overflow_class(payload, baselines.get(fname) or "")
        else:
            cls = "GUARDED"
        if ORDER[cls] > ORDER[worst]:
            worst = cls
        if cls in ("FABRICATED_CERTAINTY", "OVERFLOW_WRAP") and len(results) < 8:
            results.append({"fn": fname, "param": pname, "attack": label,
                            "output": payload[:80], "class": cls,
                            "baseline": (baselines.get(fname) or "")[:40]})
    return {"file": relpath, "class": worst, "drivable": drivable,
            "skipped": skipped, "results": results}


def main():
    import glob
    from collections import Counter
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "go", "**", "*.go"), recursive=True))
    if "--limit" in sys.argv:
        files = files[:int(sys.argv[sys.argv.index("--limit") + 1])]
    print(f"COMPILED ATTACK LANE (go) — {len(files)} patterns", flush=True)
    rows = []
    for i, f in enumerate(files):
        try:
            rows.append(harness_file(f))
        except Exception as e:
            rows.append({"file": f, "class": "NO_EVIDENCE",
                         "reason": f"{type(e).__name__}: {e}", "skipped": [], "results": []})
        if (i + 1) % 10 == 0:
            print(f"  ...{i+1}/{len(files)}", file=sys.stderr, flush=True)
    counts = Counter(r["class"] for r in rows)
    drivable = sum(r.get("drivable", 0) for r in rows)
    skipped = sum(len(r.get("skipped", [])) for r in rows)
    print("-" * 78)
    for k in ("FABRICATED_CERTAINTY", "OVERFLOW_WRAP", "VISIBLE_POISON",
              "NO_OP_ATTACK", "VALUE_PRESERVED", "GUARDED", "NO_EVIDENCE"):
        print(f"  {k:22} {counts.get(k,0)}")
    print(f"  coverage: {drivable} functions driven · {skipped} skipped (unconstructible)")
    out = os.path.join(HERE, "compiled_harness_report.json")
    json.dump({"counts": dict(counts), "driven": drivable, "skipped_fns": skipped,
               "rows": rows}, open(out, "w"), indent=1)
    print(f"report: {out}")


if __name__ == "__main__":
    main()
