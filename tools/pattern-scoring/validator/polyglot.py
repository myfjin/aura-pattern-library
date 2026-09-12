"""
polyglot.py — language-agnostic self-test runner for the whole library (5 languages).
For cpp/rust/go/r the tool can't import+inject like python; instead it COMPILES AND RUNS each
pattern's own self-test (the ORACLE LAW: cause the disaster, prove survival) and observes.

Universal signal per pattern:
  BASELINE-OK   — compiles (if needed) AND runs clean (exit 0): its self-test holds
  COMPILE-FAIL  — does not compile (compiled langs)
  RUNTIME-FAIL  — compiles but self-test fails / crashes / nonzero exit
  TIMEOUT       — hung

This is baseline HEALTH across all languages. Deep attack-injection stays python-only (executor.py)
until compiled-language harness editing lands (v2). Together: whole-library health + python triage.
"""
import subprocess, os, tempfile, hashlib

LIB = os.path.expanduser("~/aura-pattern-library")

def _run(cmd, timeout=30, cwd=None):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd)
        return p.returncode, (p.stdout or "")[-400:], (p.stderr or "")[-400:]
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"
    except Exception as e:
        return 125, "", str(e)[:200]

def selftest(relpath):
    """Compile (if needed) + run the pattern's self-test. Returns a health card."""
    path = os.path.join(LIB, relpath)
    ext = relpath.rsplit(".", 1)[-1]
    tag = hashlib.md5(relpath.encode()).hexdigest()[:8]
    binout = os.path.join(tempfile.gettempdir(), f"aura_{tag}")

    if ext == "py":
        rc, out, err = _run(["python3", path])
    elif ext == "R":
        rc, out, err = _run(["Rscript", path])
    elif ext == "go":
        rc, out, err = _run(["go", "run", path], timeout=60)
    elif ext == "cpp":
        crc, _, cerr = _run(["g++", "-std=c++17", "-O0", "-o", binout, path], timeout=45)
        if crc != 0:
            return {"file": relpath, "health": "COMPILE-FAIL", "detail": cerr[-160:]}
        rc, out, err = _run([binout])
    elif ext == "rs":
        crc, _, cerr = _run(["rustc", "--edition", "2021", "-O", "-o", binout, path], timeout=60)
        if crc != 0:
            return {"file": relpath, "health": "COMPILE-FAIL", "detail": cerr[-160:]}
        rc, out, err = _run([binout])
    elif ext == "js":
        rc, out, err = _run(["node", path])
    else:
        return {"file": relpath, "health": "SKIP", "detail": f"unknown ext {ext}"}

    if rc == 124:
        return {"file": relpath, "health": "TIMEOUT", "detail": "self-test hung"}
    if rc == 0:
        return {"file": relpath, "health": "BASELINE-OK", "detail": (out or "").strip()[-80:]}
    return {"file": relpath, "health": "RUNTIME-FAIL", "detail": (err or out)[-160:]}


def all_patterns(lang=None):
    exts = {"python": "py", "cpp": "cpp", "rust": "rs", "go": "go", "r": "R", "javascript": "js"}
    langs = [lang] if lang else list(exts)
    files = []
    for lg in langs:
        d = os.path.join(LIB, lg)
        for root, _, names in os.walk(d):
            for n in names:
                if n.endswith("." + exts[lg]):
                    files.append(os.path.relpath(os.path.join(root, n), LIB))
    return sorted(files)
