#!/usr/bin/env python3
"""Go validity oracle — same frozen frame, native judge. Canonical Go patterns are package main
whose func main() self-tests (os.Exit(1)/panic on failure, prints 'passed' on success).
Judge = go build + run. compile ok + exit 0 => VERIFIED.
Verdicts: VERIFIED / senseless / invalid(compile_error|check_failed|run_timeout)."""
import subprocess, sys, os, re, tempfile, json, glob, hashlib, collections
COMPILE_TIMEOUT = 120; RUN_TIMEOUT = 30
ENV = dict(os.environ, GO111MODULE="off", GOFLAGS="")
def extract_claim(src):
    for ln in src.splitlines():
        s = ln.strip()
        if s.startswith("//") and "AURA Pattern Library" not in s and "△" not in s and s.strip("/ ").strip():
            return s.lstrip("/ ").strip()[:300]
    return ""
def _strip_comments(src):
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)          # block comments
    src = re.sub(r"//[^\n]*", "", src)                         # line comments
    return src
def sense_check(src):
    if len(src.strip()) < 100: return False, "too short"
    if "func main" not in src: return False, "no func main"
    code = _strip_comments(src)                                # don't let a comment fake a check
    if not re.search(r"os\.Exit|panic\(|log\.Fatal", code): return False, "hollow: no failure check (os.Exit/panic/log.Fatal)"
    return True, ""
def evaluate_go(filepath):
    try: src = open(filepath, encoding="utf-8", errors="replace").read()
    except Exception as e: return {"status":"invalid","failing_column":"read_error","evidence":{"error":str(e)[:120]}}
    ok, reason = sense_check(src)
    if not ok: return {"status":"senseless","failing_column":None,"claim":extract_claim(src),"evidence":{"sense_reason":reason}}
    claim = extract_claim(src)
    with tempfile.TemporaryDirectory() as td:
        binp = os.path.join(td, "pat")
        try:
            c = subprocess.run(["go","build","-o",binp,filepath], capture_output=True, text=True, timeout=COMPILE_TIMEOUT, env=ENV)
        except subprocess.TimeoutExpired:
            return {"status":"invalid","failing_column":"compile_error","claim":claim,"evidence":{"compile":"TIMEOUT"}}
        if c.returncode != 0:
            err=(c.stderr or "").strip().splitlines()
            return {"status":"invalid","failing_column":"compile_error","claim":claim,"evidence":{"build_error":[l for l in err if ".go:" in l or "error" in l.lower()][:4] or err[-4:]}}
        try: r = subprocess.run([binp], capture_output=True, text=True, timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired:
            return {"status":"invalid","failing_column":"run_timeout","claim":claim,"evidence":{"run":"TIMEOUT"}}
        if r.returncode != 0:
            tail=(r.stderr or "").strip().splitlines()
            return {"status":"invalid","failing_column":"check_failed","claim":claim,"evidence":{"exit":r.returncode,"stderr":tail[-3:]}}
        return {"status":"VERIFIED","failing_column":None,"claim":claim,"evidence":{"built":True,"ran":True,"exit":0,"pass_marker":("pass" in (r.stdout or "").lower()),"stdout":(r.stdout or "").strip()[:120]}}
def main(argv):
    if "--dir" in argv:
        d=argv[argv.index("--dir")+1]; files=sorted(glob.glob(os.path.join(d,"**/*.go"),recursive=True))
        dist=collections.Counter(); rows=[]; print(f"Go oracle: {len(files)} patterns")
        for i,f in enumerate(files,1):
            res=evaluate_go(f); res["file"]=os.path.relpath(f,d); res["sha"]=hashlib.sha256(open(f,"rb").read()).hexdigest()[:12]
            rows.append(res); dist[res["status"]]+=1
            if i%20==0: print(f"  {i}/{len(files)} ...")
        out=os.path.expanduser("~/ai-lab/pattern-scoring/output/go_canonical_2026-07-16.json")
        json.dump({"lang":"go","count":len(files),"distribution":dict(dist),"patterns":rows},open(out,"w"),indent=2)
        print("\n=== GO VERDICT DISTRIBUTION ==="); [print(f"  {k:20s} {v}") for k,v in dist.most_common()]
        nonv=[r for r in rows if r["status"]!="VERIFIED"]; print(f"\n=== NON-VERIFIED: {len(nonv)} ===")
        for r in nonv[:40]: print(f"  {r['status']:12s} {r['file']:42s} {r.get('failing_column') or r.get('evidence',{}).get('sense_reason','')}")
        print(f"\nform: {out}")
    else: print(json.dumps(evaluate_go(argv[1]),indent=2))
if __name__=="__main__": main(sys.argv)
