#!/usr/bin/env python3
"""
validate.py — the validation tool, v1. Ties recipes + oracle + probes together, produces
evidence cards, and GRADES the tool's verdicts against Illia's frozen answer key (the exam).

The bar (6E/5S): the tool is trusted only when it reproduces Illia's hand-verdicts.
Run: python3 validate.py [--exam]
"""
import json, os, sys, math, re
from oracle import classify_signal, verdict_from_signals, derive_coverage
import probes

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.expanduser("~/aura-pattern-library")

CONCURRENCY_RE = re.compile(r"\b(Atomic\w*|compare_exchange|thread::spawn|Mutex|RwLock|"
                            r"threading\.|multiprocessing\.|goroutine|go func|sync\.)\b")

def _scan_concurrency(relpath):
    "5S #3: derive concurrency_ordering from the file, don't hardcode False."
    try:
        return bool(CONCURRENCY_RE.search(open(os.path.join(LIB, relpath),
                                               encoding="utf-8", errors="replace").read()))
    except OSError:
        return False

def load_exam():
    return json.load(open(os.path.join(HERE, "exam.json")))

def run_probe_to_card(relpath):
    """Execute the pattern's probe, run its result through the oracle, emit an evidence card."""
    probe = probes.PROBES.get(relpath)
    if not probe:
        return {"file": relpath, "verdict": "SKIP", "reason": "no executable probe yet (v1.5)"}
    r = probe()
    # collect signals from the probe result
    signals = [classify_signal(r)]
    # extra semantic signals surfaced by the probe
    if r.get("confident_impossible") or r.get("nan_absorbed_silently"):
        signals.append(("silent_wrong_on_invalid", "KILL_signal"))
    if r.get("oracle_match") is False:
        signals.append(("numeric_oracle_mismatch", "KILL_signal"))
    # 5S #1: DERIVE coverage from actual signals — do NOT trust the probe's claim.
    oracle_coverage = derive_coverage(signals, r)
    # 5S #3: wire guardrails from real detection, not hardcoded OFF.
    harness_ok = r.get("harness_ok", True)
    concurrency_ordering = _scan_concurrency(relpath)
    card = verdict_from_signals(signals, oracle_coverage, harness_ok=harness_ok,
                                concurrency_ordering=concurrency_ordering)
    card["file"] = relpath
    card["detail"] = r.get("detail", "")
    return card

def grade(exam):
    frozen = exam["frozen"] + exam["expansion"]
    results, correct, graded = [], 0, 0
    for entry in frozen:
        card = run_probe_to_card(entry["file"])
        expected = entry["verdict"]
        got = card.get("verdict")
        if got == "SKIP":
            results.append((entry["file"], expected, "SKIP", "—")); continue
        graded += 1
        # PASS-family: exam PASS == tool PASS; INVALID==INVALID; FLAG==FLAG
        ok = (got == expected)
        correct += ok
        results.append((entry["file"], expected, got, "✓" if ok else "✗ MISMATCH"))
    return results, correct, graded

def main():
    exam = load_exam()
    print("=" * 78)
    print("AURA VALIDATION TOOL v1 — exam against Illia's frozen answer key")
    print("=" * 78)
    results, correct, graded = grade(exam)
    for f, exp, got, mark in results:
        name = f.split("/")[-1]
        print(f"  {mark:12} exam={exp:8} tool={got:8}  {name}")
    print("-" * 78)
    executable = [r for r in results if r[2] != "SKIP"]
    print(f"EXECUTABLE PROBES: {graded} | REPRODUCED ILLIA'S VERDICT: {correct}/{graded}"
          + (f" ({100*correct//graded}%)" if graded else ""))
    print(f"SKIPPED (no probe yet, v1.5 extension): {len(results)-graded}")
    print("=" * 78)
    print("Note: v1 wires executable probes for the audited python patterns to prove the")
    print("exam loop closes. Generic manifest-driven execution across 5 langs = v1.5.")

if __name__ == "__main__":
    main()
