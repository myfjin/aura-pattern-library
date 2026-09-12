#!/usr/bin/env python3
"""
full_sweep.py — HEALTH-CHECK all 5 languages (compile+run self-test) + TRIAGE the python
data-science sphere (generic recipes). This is NOT full verification: the generic path cannot
PASS a pattern (no oracle), only FLAG/INVALID/SKIP. Definitive verdicts come from hand-probes.
- Every pattern: polyglot self-test HEALTH (compile+run / interpret).
- Python patterns: PLUS the deep generic attack-injection triage (executor).
Writes full_sweep_report.json + a live progress line.

Illia's test: `python3 full_sweep.py`
"""
import os, sys, json, time
from collections import defaultdict
import polyglot
import probes
from executor import evaluate
from sweep import judge  # 4Q finding 1: use the hybrid (hand-probe verdict where proven, else triage)

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    files = polyglot.all_patterns()
    print(f"HEALTH-CHECK + DS-TRIAGE (not full verification) — {len(files)} patterns across 5 languages", flush=True)
    by_lang_health = defaultdict(lambda: defaultdict(int))
    py_triage = defaultdict(int)
    rows = []
    t0 = time.time()
    for i, f in enumerate(files):
        lang = f.split("/")[0]
        h = polyglot.selftest(f)
        by_lang_health[lang][h["health"]] += 1
        row = {"file": f, "lang": lang, "health": h["health"]}
        # python DATA-SCIENCE: add deep attack triage on top of health.
        # (sysadmin/other python patterns do real filesystem/DB/lock I/O in their demos, which
        # can hang an in-process import; they get subprocess-safe HEALTH only — no deep triage.)
        # probe-backed patterns (ANY language) get their definitive verdict; python DS
        # additionally gets generic triage. Probes are curated-safe (no wild fs/db I/O).
        if h["health"] == "BASELINE-OK" and (f in probes.PROBES
                or (lang == "python" and "/data-science/" in f)):
            try:
                t = judge(f)   # hand-probe INVALID/PASS where proven, else generic triage (4Q #1)
                row["triage"] = t["verdict"]; row["source"] = t.get("source", "generic-triage")
                py_triage[t["verdict"]] += 1
            except Exception as e:
                row["triage"] = "SKIP"; py_triage["SKIP"] += 1
        rows.append(row)
        if (i + 1) % 25 == 0:
            el = time.time() - t0
            print(f"  {i+1}/{len(files)}  ({el:.0f}s)  " +
                  " ".join(f"{k}:{sum(v.values())}" for k, v in [("done", by_lang_health)][:0]) +
                  f"  last={lang}:{h['health']}", flush=True)
    dt = time.time() - t0
    print("=" * 70)
    print(f"SWEPT {len(files)} patterns in {dt:.0f}s")
    print("\nHEALTH by language (self-test compiles + runs clean?):")
    for lang in ("python", "cpp", "rust", "go", "r"):
        hs = by_lang_health.get(lang, {})
        tot = sum(hs.values())
        ok = hs.get("BASELINE-OK", 0)
        print(f"  {lang:7} {ok:4}/{tot:<4} BASELINE-OK  |  " +
              " ".join(f"{k}:{v}" for k, v in sorted(hs.items()) if k != "BASELINE-OK"))
    print("\nPYTHON deep attack-triage (on the healthy ones):")
    print(f"  {dict(py_triage)}")
    print("  (FLAG = ran but no positive oracle / silently accepted a domain attack -> human review)")
    json.dump({"n": len(files), "seconds": dt,
               "health": {k: dict(v) for k, v in by_lang_health.items()},
               "py_triage": dict(py_triage), "rows": rows},
              open(os.path.join(HERE, "full_sweep_report.json"), "w"), indent=1)
    print(f"\nreport: {os.path.join(HERE, 'full_sweep_report.json')}")

if __name__ == "__main__":
    main()
