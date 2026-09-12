#!/usr/bin/env python3
"""R validity oracle — same frozen frame, native judge. Canonical R patterns use set.seed +
stopifnot(...) as self-tests, run under Rscript. Judge = R runtime. stopifnot holds & exit 0 => VERIFIED.
Verdicts: VERIFIED / senseless / invalid(syntax_error|assert_failed|run_error|run_timeout) / needs_validity(missing_dependency)."""
import subprocess, sys, os, re, json, glob, hashlib, collections
RUN_TIMEOUT = 60
def extract_claim(src):
    for ln in src.splitlines():
        s = ln.strip()
        if s.startswith("#") and "AURA Pattern Library" not in s and "△" not in s and s.strip("# ").strip():
            return s.lstrip("# ").strip()[:300]
    return ""
def sense_check(src):
    if len(src.strip()) < 100: return False, "too short"
    if "stopifnot" not in src: return False, "hollow: no stopifnot self-test"
    return True, ""
def evaluate_r(filepath):
    try: src = open(filepath, encoding="utf-8", errors="replace").read()
    except Exception as e: return {"status":"invalid","failing_column":"read_error","evidence":{"error":str(e)[:120]}}
    ok, reason = sense_check(src)
    if not ok: return {"status":"senseless","failing_column":None,"claim":extract_claim(src),"evidence":{"sense_reason":reason}}
    claim = extract_claim(src)
    try:
        r = subprocess.run(["Rscript","--vanilla",filepath], capture_output=True, text=True, timeout=RUN_TIMEOUT)
    except subprocess.TimeoutExpired:
        return {"status":"invalid","failing_column":"run_timeout","claim":claim,"evidence":{"run":"TIMEOUT"}}
    err = r.stderr or ""
    if r.returncode == 0:
        return {"status":"VERIFIED","failing_column":None,"claim":claim,
                "evidence":{"ran":True,"exit":0,"stdout":(r.stdout or "").strip()[:140]}}
    el = err.lower()
    if "there is no package called" in el or ("could not find function" in el and "package" in el):
        return {"status":"needs_validity","failing_column":"missing_dependency","claim":claim,
                "evidence":{"note":"R package not installed — env gap, not pattern fault","stderr":err.strip().splitlines()[-2:]}}
    if "unexpected" in el or "unexpected symbol" in el or "parse" in el:
        return {"status":"invalid","failing_column":"syntax_error","claim":claim,"evidence":{"stderr":err.strip().splitlines()[-2:]}}
    if "is not true" in el or "stopifnot" in el:
        return {"status":"invalid","failing_column":"assert_failed","claim":claim,"evidence":{"stderr":[l for l in err.splitlines() if "not TRUE" in l or "Error" in l][:2]}}
    return {"status":"invalid","failing_column":"run_error","claim":claim,"evidence":{"stderr":err.strip().splitlines()[-3:]}}
def main(argv):
    if "--dir" in argv:
        d = argv[argv.index("--dir")+1]
        files = sorted(glob.glob(os.path.join(d,"**/*.R"),recursive=True)+glob.glob(os.path.join(d,"**/*.r"),recursive=True))
        dist=collections.Counter(); rows=[]
        print(f"R oracle: {len(files)} patterns")
        for i,f in enumerate(files,1):
            res=evaluate_r(f); res["file"]=os.path.relpath(f,d); res["sha"]=hashlib.sha256(open(f,"rb").read()).hexdigest()[:12]
            rows.append(res); dist[res["status"]]+=1
            if i%20==0: print(f"  {i}/{len(files)} ...")
        out=os.path.expanduser("~/ai-lab/pattern-scoring/output/r_canonical_2026-07-16.json")
        json.dump({"lang":"r","count":len(files),"distribution":dict(dist),"patterns":rows},open(out,"w"),indent=2)
        print("\n=== R VERDICT DISTRIBUTION ==="); [print(f"  {k:22s} {v}") for k,v in dist.most_common()]
        nonv=[r for r in rows if r["status"]!="VERIFIED"]; print(f"\n=== NON-VERIFIED: {len(nonv)} ===")
        for r in nonv[:40]: print(f"  {r['status']:14s} {r['file']:40s} {r.get('failing_column') or r.get('evidence',{}).get('sense_reason','')}")
        print(f"\nform: {out}")
    else: print(json.dumps(evaluate_r(argv[1]),indent=2))
if __name__=="__main__": main(sys.argv)
