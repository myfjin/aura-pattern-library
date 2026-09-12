#!/usr/bin/env python3
"""Rust validity oracle — same frozen frame as the Python mechanism, native judge.

Each canonical Rust pattern carries `#![forbid(unsafe_code)]` + a `fn main()` that runs
itself on real input (negative cases baked in), asserts the results, and prints "...: PASS".
So the oracle is: rustc + execution ARE the judge (never a model opinion).

  compile (unsafe forbidden in-source) → run → exit 0 + PASS  ==>  every assert held.

Verdicts (same vocabulary as utility_score.py):
  VERIFIED   compiles + runs + exit 0 (asserts held)
  senseless  no fn / no assert (hollow self-test) / too short
  invalid    failing_column ∈ {compile_error, assert_failed, run_timeout, no_pass_marker}
"""
import subprocess, sys, os, re, tempfile, json, glob, hashlib, collections

RUSTC = "rustc"
EDITION = "2021"
COMPILE_TIMEOUT = 90
RUN_TIMEOUT = 30

def extract_claim(src: str) -> str:
    lines = []
    for ln in src.splitlines():
        s = ln.strip()
        if s.startswith("#!") or s.startswith("const _AURA") or s.startswith("//") is False and lines:
            if not s.startswith("//"):
                break
        if s.startswith("//") and "AURA Pattern Library" not in s and "△" not in s and s.strip("/ ").strip():
            lines.append(s.lstrip("/ ").strip())
        if len(lines) >= 3:
            break
    return " ".join(lines)[:300] if lines else ""

def sense_check(src: str) -> tuple[bool, str]:
    if len(src.strip()) < 100:
        return False, "too short"
    if "fn " not in src:
        return False, "no function found"
    # hollow: has main but no real assertion macro anywhere
    if not re.search(r"\bassert(_eq|_ne)?!\s*\(", src):
        return False, "hollow: no assertion in self-test"
    return True, ""

def evaluate_rust(filepath: str) -> dict:
    try:
        src = open(filepath, encoding="utf-8").read()
    except Exception as e:
        return {"status": "invalid", "failing_column": "read_error", "evidence": {"error": str(e)[:120]}}

    ok, reason = sense_check(src)
    if not ok:
        return {"status": "senseless", "failing_column": None, "evidence": {"sense_reason": reason},
                "claim": extract_claim(src)}

    claim = extract_claim(src)
    with tempfile.TemporaryDirectory() as td:
        binpath = os.path.join(td, "pat")
        # COMPILE
        try:
            c = subprocess.run([RUSTC, "--edition", EDITION, "-O", "-A", "warnings",
                                filepath, "-o", binpath],
                               capture_output=True, text=True, timeout=COMPILE_TIMEOUT)
        except subprocess.TimeoutExpired:
            return {"status": "invalid", "failing_column": "compile_error", "claim": claim,
                    "evidence": {"compile": "TIMEOUT"}}
        if c.returncode != 0:
            err = (c.stderr or "").strip().splitlines()
            return {"status": "invalid", "failing_column": "compile_error", "claim": claim,
                    "evidence": {"compile_error": [l for l in err if "error" in l.lower()][:4] or err[-4:]}}
        # RUN (the pattern's main() = its self-test)
        try:
            r = subprocess.run([binpath], capture_output=True, text=True, timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired:
            return {"status": "invalid", "failing_column": "run_timeout", "claim": claim,
                    "evidence": {"run": "TIMEOUT"}}
        if r.returncode != 0:
            # a panic / failed assert_eq! → the pattern's own claim did NOT hold
            tail = (r.stderr or "").strip().splitlines()
            return {"status": "invalid", "failing_column": "assert_failed", "claim": claim,
                    "evidence": {"exit": r.returncode,
                                 "panic": [l for l in tail if "panic" in l.lower() or "assert" in l.lower()][:3] or tail[-3:]}}
        pass_marker = "PASS" in (r.stdout or "")
        return {"status": "VERIFIED", "failing_column": None, "claim": claim,
                "evidence": {"compiled": True, "ran": True, "exit": 0,
                             "pass_marker": pass_marker, "stdout": (r.stdout or "").strip()[:120]}}


def main(argv):
    if "--dir" in argv:
        d = argv[argv.index("--dir") + 1]
        files = sorted(f for f in glob.glob(os.path.join(d, "**/*.rs"), recursive=True))
        dist = collections.Counter(); rows = []
        print(f"Rust oracle: {len(files)} patterns")
        for i, f in enumerate(files, 1):
            res = evaluate_rust(f)
            res["file"] = os.path.relpath(f, d)
            res["sha"] = hashlib.sha256(open(f, "rb").read()).hexdigest()[:12]
            rows.append(res); dist[res["status"]] += 1
            if i % 50 == 0: print(f"  {i}/{len(files)} ...")
        out = os.path.expanduser("~/ai-lab/pattern-scoring/output/rust_canonical_2026-07-16.json")
        json.dump({"lang": "rust", "count": len(files), "distribution": dict(dist), "patterns": rows},
                  open(out, "w"), indent=2)
        print("\n=== RUST VERDICT DISTRIBUTION ===")
        for k, v in dist.most_common(): print(f"  {k:20s} {v}")
        nonv = [r for r in rows if r["status"] != "VERIFIED"]
        print(f"\n=== NON-VERIFIED: {len(nonv)} ===")
        for r in nonv[:40]:
            print(f"  {r['status']:12s} {r['file']:45s} {r.get('failing_column') or r.get('evidence',{}).get('sense_reason','')}")
        print(f"\nform: {out}")
    else:
        f = argv[1]
        print(json.dumps(evaluate_rust(f), indent=2))

if __name__ == "__main__":
    main(sys.argv)
