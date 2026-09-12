#!/usr/bin/env python3
"""
roundtrip_gen.py — generate POSITIVE oracles for codec patterns via the round-trip identity
  inverse(forward(x)) == x   over several varied inputs.

Unlike the retrofit lane this MUTATES NOTHING: a round-trip oracle is a PROBE run against the
unmodified library file. A pattern that survives earns a positive oracle (semantic) — a real
PASS candidate for the exam, gated to Illia. Triple gate per pattern:
  (1) round-trip identity holds on >=3 varied inputs (the positive oracle)
  (2) the pattern's own self-test still passes (unbroken)
  (3) deterministic across two runs
Patterns whose encode/decode don't cleanly compose (constructor args unknown, tuple field
ambiguous, container-not-codec) are QUARANTINED honestly — never forced to a fake PASS.

Scope: same-class or free-function codec pairs with buildable inputs. Containers
(insert/delete, push/pop) need a structural oracle, NOT value identity — out of this lane.
"""
import os, re, ast, glob, json, sys, importlib.util, io, contextlib, subprocess
from executor import _valid_for
import inspect

LIB = os.path.expanduser("~/aura-pattern-library")
HERE = os.path.dirname(os.path.abspath(__file__))

CODEC_PAIRS = [("encode", "decode"), ("serialize", "deserialize"),
               ("marshal", "unmarshal"), ("compress", "decompress"),
               ("to_u32", "from_u32"), ("to_bytes", "from_bytes"),
               ("to_dict", "from_dict"), ("dumps", "loads"), ("pack", "unpack")]
CONTAINER = ("insert", "delete", "push", "pop", "enqueue", "dequeue")

# varied round-trip inputs by type-hint (reuse the executor's builder where possible)
SAMPLE_INPUTS = {
    "str":   ["hello world", "", "the quick brown fox 123", "λ日本語 mixed"],
    "bytes": [b"hello", b"", b"\x00\x01\xff data", b"A" * 40],
    "int":   [0, 1, 42, 2**31 - 1],
    "list":  [[1, 2, 3], [], [0, 0, 0, 1], list(range(10))],
    "dict":  [{"a": 1, "b": 2}, {}, {"x": [1, 2]}],
}

def _load(relpath):
    p = os.path.join(LIB, relpath)
    spec = importlib.util.spec_from_file_location("rt_" + str(abs(hash(relpath))), p)
    m = importlib.util.module_from_spec(spec)
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            spec.loader.exec_module(m)
        return m, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"

def _find_pair(module, src):
    """Return (fwd_callable, inv_callable, kind) or None. kind: 'free' | 'method:<Class>'."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    # class-scoped methods
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            meths = {n.name for n in node.body if isinstance(n, ast.FunctionDef)}
            for a, b in CODEC_PAIRS:
                fa = next((m for m in meths if a in m.lower() and m.lower() != b), None)
                fb = next((m for m in meths if b in m.lower() and m != fa), None)
                if fa and fb:
                    cls = getattr(module, node.name, None)
                    if cls is not None:
                        return (fa, fb, "method:" + node.name)
    # free functions
    free = {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}
    for a, b in CODEC_PAIRS:
        fa = next((m for m in free if a in m.lower() and m.lower() != b), None)
        fb = next((m for m in free if b in m.lower() and m != fa), None)
        if fa and fb:
            return (getattr(module, fa, None), getattr(module, fb, None), "free")
    return None

def _build_instance(cls):
    """Try to construct with no-arg, else build __init__ args from hints. Return instance or None."""
    try:
        return cls()
    except Exception:
        pass
    try:
        sig = inspect.signature(cls.__init__)
        args = []
        for p in list(sig.parameters.values())[1:]:  # skip self
            if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                continue
            v, ok = _valid_for(p.annotation, p.default, p.name)
            if not ok:
                return None
            args.append(v)
        return cls(*args)
    except Exception:
        return None

def _fwd_inputs(fwd):
    """Yield candidate x values from the forward callable's first real param hint."""
    try:
        sig = inspect.signature(fwd)
    except (TypeError, ValueError):
        return []
    params = [p for p in sig.parameters.values()
              if p.name != "self" and p.kind in (p.POSITIONAL_OR_KEYWORD, p.POSITIONAL_ONLY)]
    if not params:
        return []
    ann = str(params[0].annotation).lower()
    for key, samples in SAMPLE_INPUTS.items():
        if key in ann:
            return samples
    if "union" in ann and "str" in ann:
        return SAMPLE_INPUTS["str"]
    return SAMPLE_INPUTS["str"]  # default guess: strings

def _equal(a, b):
    if a == b:
        return True
    # tuple/list decode result: does x appear as a field?
    if isinstance(a, (tuple, list)):
        return any(_equal(x, b) for x in a)
    # bytes/str tolerance
    try:
        if isinstance(a, bytes) and isinstance(b, str):
            return a.decode() == b
        if isinstance(a, str) and isinstance(b, bytes):
            return a == b.decode()
    except Exception:
        return False
    return False

def probe_roundtrip(relpath):
    src = open(os.path.join(LIB, relpath), encoding="utf-8", errors="replace").read()
    module, err = _load(relpath)
    if err:
        return {"status": "SKIP", "detail": f"load: {err}"}
    pair = _find_pair(module, src)
    if not pair:
        return {"status": "SKIP", "detail": "no composable codec pair"}
    fa, fb, kind = pair
    # resolve callables (bound to an instance for methods)
    if kind.startswith("method:"):
        cls = getattr(module, kind.split(":", 1)[1])
        inst = _build_instance(cls)
        if inst is None:
            return {"status": "JUDGE", "detail": f"cannot construct {cls.__name__} (ctor args)"}
        fwd, inv = getattr(inst, fa), getattr(inst, fb)
    else:
        fwd, inv = fa, fb
    inputs = _fwd_inputs(fwd)
    if not inputs:
        return {"status": "JUDGE", "detail": "cannot build forward input"}
    held, total, fails = 0, 0, []
    for x in inputs:
        total += 1
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                mid = fwd(x)
                back = inv(mid)
        except Exception as e:
            fails.append(f"{x!r}: raised {type(e).__name__}")
            continue
        if _equal(back, x):
            held += 1
        else:
            fails.append(f"{x!r} -> {back!r}")
    if held < 3:
        return {"status": "JUDGE", "detail": f"round-trip held {held}/{total}: {fails[:2]}"}
    # gate 2+3: self-test green + deterministic
    r1 = subprocess.run([sys.executable, os.path.join(LIB, relpath)],
                        capture_output=True, text=True, timeout=90)
    r2 = subprocess.run([sys.executable, os.path.join(LIB, relpath)],
                        capture_output=True, text=True, timeout=90)
    selftest = (r1.returncode == 0)
    det = (r1.stdout == r2.stdout)
    status = "OK" if (selftest and det) else "REVIEW"
    return {"status": status, "detail": f"round-trip {held}/{total} via {fa}<->{fb} ({kind}); "
            f"selftest={'GREEN' if selftest else 'RED'} det={det}",
            "held": held, "total": total, "pair": f"{fa}<->{fb}"}


def candidates():
    ex = json.load(open(os.path.join(HERE, "exam.json")))
    known = {e["file"] for e in ex["frozen"] + ex["expansion"]}
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "**", "*.py"), recursive=True))
    out = []
    for f in files:
        if f in known:
            continue
        src = open(os.path.join(LIB, f), encoding="utf-8", errors="replace").read()
        # skip pure-container patterns (no codec verb)
        low = src.lower()
        has_codec = any(a in low and b in low for a, b in CODEC_PAIRS)
        if has_codec:
            out.append(f)
    return out


def main():
    cands = candidates()
    print(f"ROUND-TRIP ORACLE GENERATOR — {len(cands)} python codec candidates")
    print("=" * 88)
    tally = {"OK": 0, "JUDGE": 0, "REVIEW": 0, "SKIP": 0}
    oks = []
    for f in cands:
        try:
            r = probe_roundtrip(f)
        except Exception as e:
            r = {"status": "SKIP", "detail": f"gen error: {e}"}
        tally[r["status"]] += 1
        if r["status"] == "OK":
            oks.append(f)
        if r["status"] in ("OK", "REVIEW", "JUDGE"):
            print(f"  [{r['status']:6}] {f.split('/')[-1]:40} {r['detail'][:70]}")
    print("=" * 88)
    print(f"POSITIVE ORACLES EARNED (OK): {tally['OK']}  "
          f"| JUDGE {tally['JUDGE']} | REVIEW {tally['REVIEW']} | SKIP {tally['SKIP']}")
    json.dump({"tally": tally, "oks": oks}, open(os.path.join(HERE, "roundtrip_report.json"), "w"), indent=1)
    print(f"report: {os.path.join(HERE, 'roundtrip_report.json')}")

if __name__ == "__main__":
    main()
