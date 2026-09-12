#!/usr/bin/env python3
"""C++ validity oracle — same frozen frame as Rust/Python, native judge.
Canonical C++ patterns carry a watermark + `int main()` that runs the pattern, asserts its
documented "Oracle asserts", and prints "...PASS". Judge = compiler + execution, no model opinion.
Portability law: must compile under g++ AND clang++ (pedantic). Then run g++ binary; asserts hold => VERIFIED.
Verdicts match utility_score.py: VERIFIED / senseless / invalid(compile_error_gcc|compile_error_clang|assert_failed|run_timeout)."""
import subprocess, sys, os, re, tempfile, json, glob, hashlib, collections

STD = "c++17"; COMPILE_TIMEOUT = 90; RUN_TIMEOUT = 30

def extract_claim(src):
    m = re.search(r"/\*(.*?)\*/", src, re.S)
    if m:
        for ln in m.group(1).splitlines():
            s = ln.strip(" *")
            if s and "Oracle asserts" not in s: return s[:300]
    return ""

def sense_check(src):
    if len(src.strip()) < 100: return False, "too short"
    if "int main" not in src: return False, "no main entry"
    if not re.search(r"\bassert\s*\(", src): return False, "hollow: no assertion in self-test"
    return True, ""

def _compile(compiler, filepath, binpath):
    try:
        c = subprocess.run([compiler, f"-std={STD}", "-O2", "-pedantic", filepath, "-o", binpath],
                           capture_output=True, text=True, timeout=COMPILE_TIMEOUT)
        return c.returncode == 0, [l for l in (c.stderr or "").splitlines() if "error" in l.lower()][:4]
    except subprocess.TimeoutExpired:
        return False, ["TIMEOUT"]

def evaluate_cpp(filepath):
    try: src = open(filepath, encoding="utf-8", errors="replace").read()
    except Exception as e: return {"status": "invalid", "failing_column": "read_error", "evidence": {"error": str(e)[:120]}}
    ok, reason = sense_check(src)
    if not ok: return {"status": "senseless", "failing_column": None, "claim": extract_claim(src), "evidence": {"sense_reason": reason}}
    claim = extract_claim(src)
    with tempfile.TemporaryDirectory() as td:
        gbin, cbin = os.path.join(td, "g"), os.path.join(td, "c")
        g_ok, g_err = _compile("g++", filepath, gbin)
        if not g_ok: return {"status": "invalid", "failing_column": "compile_error_gcc", "claim": claim, "evidence": {"gcc_error": g_err}}
        c_ok, c_err = _compile("clang++", filepath, cbin)
        if not c_ok: return {"status": "invalid", "failing_column": "compile_error_clang", "claim": claim, "evidence": {"clang_error": c_err, "note": "compiles on g++ but not clang (portability)"}}
        try: r = subprocess.run([gbin], capture_output=True, text=True, timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired: return {"status": "invalid", "failing_column": "run_timeout", "claim": claim, "evidence": {"run": "TIMEOUT"}}
        if r.returncode != 0:
            tail = (r.stderr or "").strip().splitlines()
            return {"status": "invalid", "failing_column": "assert_failed", "claim": claim,
                    "evidence": {"exit": r.returncode, "abort": [l for l in tail if "assert" in l.lower() or "abort" in l.lower()][:3] or tail[-3:]}}
        return {"status": "VERIFIED", "failing_column": None, "claim": claim,
                "evidence": {"gcc": True, "clang": True, "ran": True, "exit": 0, "pass_marker": "PASS" in (r.stdout or ""), "stdout": (r.stdout or "").strip()[:120]}}

def main(argv):
    if "--dir" in argv:
        d = argv[argv.index("--dir")+1]
        files = sorted(glob.glob(os.path.join(d, "**/*.cpp"), recursive=True))
        dist = collections.Counter(); rows = []
        print(f"C++ oracle: {len(files)} patterns")
        for i, f in enumerate(files, 1):
            res = evaluate_cpp(f); res["file"] = os.path.relpath(f, d); res["sha"] = hashlib.sha256(open(f,"rb").read()).hexdigest()[:12]
            rows.append(res); dist[res["status"]] += 1
            if i % 50 == 0: print(f"  {i}/{len(files)} ...")
        out = os.path.expanduser("~/ai-lab/pattern-scoring/output/cpp_canonical_2026-07-16.json")
        json.dump({"lang":"cpp","count":len(files),"distribution":dict(dist),"patterns":rows}, open(out,"w"), indent=2)
        print("\n=== C++ VERDICT DISTRIBUTION ==="); [print(f"  {k:24s} {v}") for k,v in dist.most_common()]
        nonv=[r for r in rows if r["status"]!="VERIFIED"]; print(f"\n=== NON-VERIFIED: {len(nonv)} ===")
        for r in nonv[:40]: print(f"  {r['status']:10s} {r['file']:42s} {r.get('failing_column') or r.get('evidence',{}).get('sense_reason','')}")
        print(f"\nform: {out}")
    else:
        print(json.dumps(evaluate_cpp(argv[1]), indent=2))

if __name__ == "__main__": main(sys.argv)
