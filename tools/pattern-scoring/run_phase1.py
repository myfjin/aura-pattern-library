#!/usr/bin/env python3
"""Phase 1 — validate the 674 canonical Python patterns in the signed grand library.
Deterministic. Produces JSON form + CSV summary + verdict distribution."""
import glob, json, subprocess, os, sys, csv, hashlib, collections

LIB = os.path.expanduser("~/aura-pattern-library/python")
OUT_JSON = os.path.expanduser("~/ai-lab/pattern-scoring/output/python_canonical_2026-07-16.json")
OUT_CSV  = os.path.expanduser("~/ai-lab/pattern-scoring/output/python_canonical_2026-07-16.csv")
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)

files = sorted(f for f in glob.glob(os.path.join(LIB, "**/*.py"), recursive=True) if "pycache" not in f)
print(f"Phase 1: {len(files)} canonical Python patterns")

rows = []
dist = collections.Counter()
for i, f in enumerate(files, 1):
    sha = hashlib.sha256(open(f, "rb").read()).hexdigest()[:12]
    try:
        r = subprocess.run(["python3", "utility_score.py", f, "--abuse", "--json"],
                           capture_output=True, text=True, timeout=120)
        rec = json.loads(r.stdout)
        status = rec.get("status", "?")
        rows.append({
            "file": os.path.relpath(f, LIB), "name": rec.get("name"), "sha": sha,
            "status": status, "U": rec.get("U"),
            "failing_column": rec.get("failing_column"),
            "sense_pass": rec.get("sense_pass"), "sense_reason": rec.get("sense_reason"),
            "description_pass": rec.get("description_pass"),
            "validity_pass": rec.get("validity_pass"),
            "flags": rec.get("flags"),
        })
    except Exception as e:
        status = "RUNERR"
        rows.append({"file": os.path.relpath(f, LIB), "name": None, "sha": sha,
                     "status": status, "failing_column": "runner_error",
                     "flags": [str(e)[:120], (r.stderr.strip().splitlines()[-1][:120] if 'r' in dir() and r.stderr else "")]})
    dist[status] += 1
    if i % 100 == 0:
        print(f"  {i}/{len(files)} ...")

json.dump({"phase": 1, "corpus": LIB, "count": len(files),
           "distribution": dict(dist), "rubric_version": "1.0.0", "patterns": rows},
          open(OUT_JSON, "w"), indent=2)

with open(OUT_CSV, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["file", "name", "sha", "status", "U", "failing_column", "sense_reason"])
    for r in rows:
        w.writerow([r["file"], r.get("name"), r["sha"], r["status"], r.get("U"),
                    r.get("failing_column"), r.get("sense_reason")])

print("\n=== PHASE 1 VERDICT DISTRIBUTION ===")
for k, v in dist.most_common():
    print(f"  {k:32s} {v}")
print(f"\nform: {OUT_JSON}")
print(f"csv : {OUT_CSV}")

# show the non-VERIFIED sample (the interesting ones for Illia's audit)
nonv = [r for r in rows if r["status"] != "VERIFIED"]
print(f"\n=== NON-VERIFIED: {len(nonv)} patterns (the ones needing eyes) ===")
for r in nonv[:40]:
    print(f"  {r['status']:28s} {r['file']:45s} {r.get('failing_column') or (r.get('sense_reason') or '')[:40]}")
