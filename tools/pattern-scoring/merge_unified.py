#!/usr/bin/env python3
"""Phase 3 — merge all per-language forms into ONE unified library validation form."""
import json, os, glob, csv, collections
OUT = os.path.expanduser("~/ai-lab/pattern-scoring/output")
SOURCES = {
    "python": "python_canonical_2026-07-16.json",
    "rust":   "rust_canonical_2026-07-16.json",
    "cpp":    "cpp_canonical_2026-07-16.json",
    "r":      "r_canonical_2026-07-16.json",
    "go":     "go_canonical_2026-07-16.json",
}
rows = []; per_lang = {}
for lang, fn in SOURCES.items():
    p = os.path.join(OUT, fn)
    if not os.path.exists(p):
        per_lang[lang] = {"status": "PENDING", "count": 0}; continue
    d = json.load(open(p))
    dist = collections.Counter()
    for r in d["patterns"]:
        st = r.get("status", "?")
        rows.append({"lang": lang, "file": r.get("file"), "status": st,
                     "failing_column": r.get("failing_column"), "sha": r.get("sha")})
        dist[st] += 1
    per_lang[lang] = {"count": len(d["patterns"]), "distribution": dict(dist)}

overall = collections.Counter(r["status"] for r in rows)
unified = {"library": "AURA Pattern Library", "rubric_version": "1.0.0",
           "generated": "2026-07-16", "total_files_validated": len(rows),
           "per_language": per_lang, "overall_distribution": dict(overall), "patterns": rows}
json.dump(unified, open(os.path.join(OUT, "UNIFIED_library_form_2026-07-16.json"), "w"), indent=2)
with open(os.path.join(OUT, "UNIFIED_library_form_2026-07-16.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["lang", "file", "status", "failing_column", "sha"])
    for r in rows: w.writerow([r["lang"], r["file"], r["status"], r["failing_column"], r["sha"]])

print("=== UNIFIED LIBRARY VALIDATION FORM ===")
for lang, info in per_lang.items():
    if info.get("status") == "PENDING":
        print(f"  {lang:8s} PENDING"); continue
    d = info["distribution"]; v = d.get("VERIFIED", 0)
    print(f"  {lang:8s} {info['count']:4d} files → {v} VERIFIED" + (f" · {dict((k,x) for k,x in d.items() if k!='VERIFIED')}" if len(d) > 1 else ""))
print(f"\n  TOTAL validated: {len(rows)} files")
print(f"  OVERALL: {dict(overall)}")
verified = overall.get("VERIFIED", 0)
print(f"  VERIFIED: {verified}/{len(rows)} = {100*verified/len(rows):.1f}%")
print(f"  flagged for human audit: {len(rows)-verified}")
