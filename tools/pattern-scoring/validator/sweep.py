#!/usr/bin/env python3
"""
sweep.py — v1.9 library-wide sweep. Runs the generic executor over every python pattern,
produces verdicts + an evidence report. This is the "validate the whole library" capability.

Usage:
  python3 sweep.py --exam           # sweep only the audited patterns, grade vs answer key
  python3 sweep.py --lang python    # sweep the whole python sphere
  python3 sweep.py --sample 40      # random reproducible sample
"""
import os, sys, json, glob, time
from executor import evaluate, LIB
import probes  # hand-probes give DEFINITIVE verdicts; generic executor gives TRIAGE

HERE = os.path.dirname(os.path.abspath(__file__))

_RT_LOST = {}   # relpath -> why a wired round-trip oracle failed to return a verdict this run


def judge(relpath):
    """Hybrid: definitive hand-probe verdict if we have one, else generic triage."""
    # assisted round-trip positive oracle: inverse(forward(x))==x is a SEMANTIC oracle -> PASS.
    import roundtrip_probes as rtp
    rt_name = os.path.basename(relpath)
    if rt_name in rtp.REGISTRY:
        res = rtp.verify(rt_name, rtp.REGISTRY[rt_name])
        if res.get("status") == "PASS":
            return {"file": relpath, "verdict": "PASS", "source": "roundtrip-oracle",
                    "reason": f"round-trip identity oracle {res['held']}/{res['total']}"}
        if res.get("status") == "FLAG":   # the lane found a real defect (crash/incomplete identity)
            return {"file": relpath, "verdict": "FLAG", "source": "roundtrip-oracle",
                    "reason": res.get("reason", "roundtrip_defect")}
        # oracle inconclusive (can't construct) -> fall through to normal triage (never fake)
        #
        # BUT RECORD WHY (2026-07-27). A REVIEW/ERROR/SKIP here used to vanish silently: the
        # row fell through to generic triage and reported the generic reason ("no discoverable
        # entry function"), so the fact that a positive oracle was LOST — and its cause — left
        # no trace. That is how 5 patterns silently dropped hard->consensus and the exam went
        # 69/69 -> 64/69 with nobody touching the registry, and why it could not be diagnosed
        # afterwards. An intermittent that does not record its own cause cannot be fixed.
        _RT_LOST[relpath] = {"status": res.get("status"), "detail": res.get("detail", "")[:160]}
    if relpath in probes.PROBES:
        from oracle import classify_signal, verdict_from_signals, derive_coverage
        r = probes.PROBES[relpath]()
        signals = [classify_signal(r)]
        if r.get("confident_impossible") or r.get("nan_absorbed_silently"):
            signals.append(("silent_wrong_on_invalid", "KILL_signal"))
        # generic conclusive-kill seam: a hand-probe that PROVED its defect (ruling-backed)
        # escalates on its own authority. Only probes set this — the generic path never can.
        if r.get("conclusive_kill"):
            signals.append((r.get("kill_reason", "defect_oracle_confirmed"), "KILL_signal"))
        if r.get("oracle_match") is False:
            signals.append(("numeric_oracle_mismatch", "KILL_signal"))
        cov = derive_coverage(signals, r)
        card = verdict_from_signals(signals, cov, harness_ok=True,
                                    concurrency_ordering=bool(r.get("concurrency_ordering")))
        card["file"] = relpath; card["source"] = "oracle-probe"
        return card
    card = evaluate(relpath); card["source"] = "generic-triage"
    return card

def exam_files():
    ex = json.load(open(os.path.join(HERE, "exam.json")))
    # all five probe-covered languages graded (go batch 1 hand-audited 2026-07-21)
    return [(e["file"], e["verdict"]) for e in ex["frozen"] + ex["expansion"]
            if e["file"].endswith((".py", ".rs", ".R", ".cpp", ".go"))]

def all_python():
    """Triage-SAFE python set: data-science + probe-backed files only. Sysadmin/other python
    do real fs/db/lock I/O that can hang an in-process import (the lane full_sweep gives
    subprocess HEALTH only) — burned 2026-07-21, now excluded here by default."""
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "python", "**", "*.py"), recursive=True))
    return [f for f in files if "/data-science/" in f or f in probes.PROBES]

def run(files, answer=None):
    counts = {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": 0}
    correct = graded = 0
    rows = []
    t0 = time.time()
    for i, f in enumerate(files):
        try:
            card = judge(f)
        except Exception as e:
            card = {"file": f, "verdict": "SKIP", "reason": f"executor error: {e}"}
        # a wired positive oracle that failed to deliver a verdict is RECORDED, not silent
        if f in _RT_LOST:
            card["rt_lost"] = _RT_LOST.pop(f)
        v = card["verdict"]; counts[v] = counts.get(v, 0) + 1
        mark = ""
        if answer and f in answer:
            graded += 1
            exp = answer[f]
            ok = (v == exp)
            correct += ok
            mark = "✓" if ok else f"✗ (exam={exp})"
        rows.append((f, v, mark, card.get("reason", ""), card.get("rt_lost")))
        if (i + 1) % 50 == 0:
            print(f"  ...{i+1}/{len(files)}  ({counts})", file=sys.stderr)
    return counts, correct, graded, rows, time.time() - t0

def main():
    args = sys.argv[1:]
    if "--exam" in args:
        pairs = exam_files(); files = [f for f, _ in pairs]; answer = dict(pairs)
        title = "EXAM sweep (audited patterns vs answer key — all 5 languages)"
    elif "--sample" in args:
        n = int(args[args.index("--sample") + 1]); files = all_python()
        # reproducible sample: every len/n-th file
        step = max(1, len(files) // n); files = files[::step][:n]; answer = None
        title = f"SAMPLE sweep ({len(files)} python patterns)"
    else:
        files = all_python(); answer = None
        title = f"FULL python sweep ({len(files)} patterns)"

    print("=" * 82); print(f"AURA VALIDATION TOOL v1.9 — {title}"); print("=" * 82)
    counts, correct, graded, rows, dt = run(files, answer)
    for f, v, mark, reason, _lost in rows:
        if answer or v in ("INVALID", "FLAG"):  # in full sweep, show only findings
            print(f"  {v:8} {mark:14} {f.split('/')[-1]:40} {reason[:40]}")
    print("-" * 82)
    print(f"verdicts: {counts}  | swept {len(files)} in {dt:.1f}s")
    if graded:
        print(f"EXAM: reproduced {correct}/{graded} answer-key verdicts ({100*correct//graded}%)")
    # write full report
    out = os.path.join(HERE, "sweep_report.json")
    # rt_lost is carried into the report so a LOST positive oracle leaves a trace.
    json.dump({"counts": counts,
               "rows": [dict({"file": f, "verdict": v, "reason": r},
                             **({"rt_lost": lost} if lost else {}))
                        for f, v, m, r, lost in rows]}, open(out, "w"), indent=1)
    print(f"full report: {out}")

if __name__ == "__main__":
    main()
