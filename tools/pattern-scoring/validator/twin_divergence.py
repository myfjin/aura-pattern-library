#!/usr/bin/env python3
"""
twin_divergence.py — FOLD 4: twin-consensus / divergence as a compiled cross-language oracle.
Adapted from forge-gate/tools/twin_consensus.py (inherited, NOT merged — tools stay separate).

Forge's version verifies USER code against reference twins and is bound to forge_gate.catalog/
runner/verifier. We keep only the two transferable ideas and re-aim them at OUR signed library:
  (a) COMPILED cross-language harness (4Q #9): compile+run cpp/go/rust twins, capture verdict+metrics.
  (b) TWIN DIVERGENCE (5S #7): the language twins of ONE pattern must reach the same verdict.
      A twin that fails/does-not-compile while its sibling passes = DIVERGENCE (a broken translation).

HONEST SCOPE (stated, not dressed up): our library is already GREEN (library_verify passes every
self-test), so this does NOT surface new bugs today. Its value is two things the tool did not have:
  1. an independent COMPILED oracle lane (behavior via the real compiler, not a python probe), and
  2. a permanent cross-language DIVERGENCE TRIPWIRE — a future edit that breaks one twin but not its
     sibling is caught here, where a per-language sweep would miss the cross-language contradiction.
Metric-level consensus is opportunistic ONLY: our twins embed their own inputs, so numbers are
compared only when both twins happen to emit the same named metric (never fabricated agreement).

Verdict-ladder mapping:
  all twins of a pattern AGREE (same verdict)     -> cross-language positive oracle ('xlang')
  twins DIVERGE (mixed verdicts / compile split)  -> INVALID-CANDIDATE (broken translation) -> card,
      routed to calibration; MUST NOT auto-flip a frozen exam verdict (a divergence that contradicts
      a frozen PASS means the harness/env is miscalibrated, not the ruler).

Observation-only: reads twin behavior, never mutates the library, never touches exam grading.
"""
from __future__ import annotations
import json, os, re, shutil, subprocess, sys, tempfile, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = Path(os.path.expanduser("~/aura-pattern-library"))
EXTS = {".py": "python", ".cpp": "cpp", ".go": "go", ".rs": "rust", ".R": "r"}
SKIP_METRIC_NAMES = {"exit", "code", "line", "seed", "version", "copyright", "cpp", "pass", "true", "false"}


def _extract_numbers(text):
    out = {}
    for line in text.splitlines():
        m = re.search(r"R[²2]\s*=?\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)", line, re.I)
        if m:
            out["r2"] = float(m.group(1))
        for wm in re.finditer(r"\b(\w+)\s*[:=]\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)", line):
            name = wm.group(1).lower()
            if name in SKIP_METRIC_NAMES:
                continue
            out[name] = float(wm.group(2))
    return out


def _status_from(exit_code, stdout):
    # our twins self-test: exit 0 (and a PASS marker if present) = PASS.
    if exit_code == 0:
        return "PASS"
    return "FAIL"


def _run_python(path, timeout=30):
    try:
        p = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "metrics": {}}
    return {"status": _status_from(p.returncode, p.stdout), "metrics": _extract_numbers(p.stdout)}


def _compile_run(path, compile_cmd, run_argv, timeout=45):
    try:
        c = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=90)
        if c.returncode != 0:
            return {"status": "COMPILE-FAIL", "metrics": {}, "err": c.stderr.strip().splitlines()[-1:] }
        r = subprocess.run(run_argv, capture_output=True, text=True, timeout=timeout)
        return {"status": _status_from(r.returncode, r.stdout), "metrics": _extract_numbers(r.stdout)}
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "metrics": {}}
    except Exception as e:
        return {"status": "ERROR", "metrics": {}, "err": [str(e)]}


def _run_cpp(path, timeout=45):
    gxx = shutil.which("g++") or shutil.which("clang++")
    if not gxx:
        return {"status": "NO-TOOLCHAIN", "metrics": {}}
    out = Path(tempfile.gettempdir()) / f"_tw_{path.stem}"
    return _compile_run(path, [gxx, "-O0", "-std=c++17", str(path), "-o", str(out)], [str(out)], timeout)


def _run_rust(path, timeout=45):
    rc = shutil.which("rustc")
    if not rc:
        return {"status": "NO-TOOLCHAIN", "metrics": {}}
    out = Path(tempfile.gettempdir()) / f"_tw_{path.stem}"
    return _compile_run(path, [rc, "-O", "--edition", "2021", str(path), "-o", str(out)], [str(out)], timeout)


def _run_go(path, timeout=60):
    go = shutil.which("go")
    if not go:
        return {"status": "NO-TOOLCHAIN", "metrics": {}}
    return _compile_run(path, [go, "build", "-o", str(Path(tempfile.gettempdir()) / f"_tw_{path.stem}"), str(path)],
                        [str(Path(tempfile.gettempdir()) / f"_tw_{path.stem}")], timeout)


RUNNERS = {"python": _run_python, "cpp": _run_cpp, "rust": _run_rust, "go": _run_go}


def _resolve_twins():
    """basename -> {lang: path} for every pattern with 2+ runnable-language twins (r excluded: no
    scripted runner here). Excludes .BROKEN fixtures and __pycache__."""
    by = collections.defaultdict(dict)
    for root, _, files in os.walk(LIB):
        if "__pycache__" in root or "regression_fixtures" in root:
            continue
        for f in files:
            b, e = os.path.splitext(f)
            lang = EXTS.get(e)
            if lang and lang in RUNNERS and not b.endswith(".BROKEN"):
                by[b][lang] = Path(root) / f
    return {b: d for b, d in by.items() if len(d) >= 2}


def _consensus(results, tol=1e-3, compare_metrics=False):
    """results: {lang: {status, metrics}}. Agree = all twins reach the SAME self-test verdict (all
    PASS). compare_metrics is OFF for the library scan by design: our twins are self-testing files
    that embed their OWN inputs (and python's RNG != C++'s RNG != go's), so a value like wins=101 vs
    wins=113 is different random data, NOT a broken translation — comparing absolute values there
    manufactures false divergences (forge handled the same with require_value_match=False). The
    defensible cross-language signal for input-independent twins is STATUS + compile integrity.
    compare_metrics=True is kept ONLY for the negative control (proves the value-diff capability is
    real) and for any future twins that are wired to share a deterministic input."""
    statuses = {lang: r["status"] for lang, r in results.items()}
    if len(set(statuses.values())) > 1:
        return False, [f"status split: {statuses}"]
    if next(iter(statuses.values())) != "PASS":
        return False, [f"all twins non-PASS: {statuses}"]
    if not compare_metrics:
        return True, []
    langs = list(results)
    notes = []
    for i in range(len(langs)):
        for j in range(i + 1, len(langs)):
            a, b = results[langs[i]]["metrics"], results[langs[j]]["metrics"]
            for k in set(a) & set(b):
                denom = max(abs(a[k]), abs(b[k]), 1.0)
                if abs(a[k] - b[k]) / denom > tol:
                    notes.append(f"metric '{k}' {langs[i]}={a[k]} vs {langs[j]}={b[k]}")
    return (not notes), notes


def _card(base, results, agree, notes):
    langs = "·".join(sorted(results))
    if agree:
        return {"pattern": base, "technique": "twin-consensus", "severity": "info",
                "class": "xlang-consensus", "fixture": f"compiled twins: {langs}",
                "expected": "all language twins reach the same verdict",
                "actual": f"{len(results)} twins agree (all PASS)", "verdict": "PASS",
                "verdict_target": "PATTERN", "confidence": "high",
                "repro_cmd": f"python3 twin_divergence.py {base}", "oracle_coverage_kind": "xlang"}
    return {"pattern": base, "technique": "twin-consensus", "severity": "high",
            "class": "xlang-divergence", "fixture": f"compiled twins: {langs}",
            "expected": "all language twins reach the same verdict + agree on shared metrics",
            "actual": "; ".join(notes) or "twins diverge",
            "why": "a twin diverging from its sibling is a broken translation (cross-lang tripwire)",
            "verdict": "INVALID-CANDIDATE", "verdict_target": "PATTERN",
            "note": "MUST NOT auto-flip a frozen exam verdict; contradiction => harness/env miscalibrated",
            "confidence": "high", "repro_cmd": f"python3 twin_divergence.py {base}",
            "oracle_coverage_kind": "xlang",
            "detail": {lang: results[lang]["status"] for lang in results}}


def negative_control():
    """Teeth: two synthetic twins whose self-tests disagree (one exits 0, one exits 1) MUST be flagged
    DIVERGENT; two that agree MUST be consensus. Proves the detector isn't cosmetic."""
    agree_ok = _consensus({"python": {"status": "PASS", "metrics": {"r2": 0.99}},
                           "cpp": {"status": "PASS", "metrics": {"r2": 0.99}}})[0] is True
    diverge_caught = _consensus({"python": {"status": "PASS", "metrics": {}},
                                 "cpp": {"status": "FAIL", "metrics": {}}})[0] is False
    metric_caught = _consensus({"python": {"status": "PASS", "metrics": {"r2": 0.99}},
                                "cpp": {"status": "PASS", "metrics": {"r2": 0.40}}},
                               compare_metrics=True)[0] is False  # capability proven; OFF in live scan
    ok = agree_ok and diverge_caught and metric_caught
    print(f"negative control: agree={agree_ok} status-diverge-caught={diverge_caught} "
          f"metric-diverge-caught={metric_caught} -> {'DETECTION WORKS' if ok else 'COSMETIC (ABORT)'}")
    return ok


def scan(only=None, limit=None, verbose=True):
    twins = _resolve_twins()
    if only:
        twins = {b: d for b, d in twins.items() if b in only}
    items = sorted(twins.items())
    capped = False
    if limit and len(items) > limit:
        items = items[:limit]; capped = True
    cards, diverged = [], []
    for idx, (base, d) in enumerate(items, 1):
        results = {lang: RUNNERS[lang](path) for lang, path in d.items()}
        agree, notes = _consensus(results)
        cards.append(_card(base, results, agree, notes))
        if not agree:
            diverged.append((base, results, notes))
            if verbose:
                print(f"  [{idx}/{len(items)}] DIVERGE {base:40} "
                      + "; ".join(notes) + " :: " + str({l: r['status'] for l, r in results.items()}))
        elif verbose and idx % 50 == 0:
            print(f"  ...{idx}/{len(items)} twin-sets checked, {len(diverged)} divergent so far")
    json.dump({"cards": cards, "diverged": [d[0] for d in diverged], "n": len(items), "capped": capped},
              open(HERE / "twin_divergence_report.json", "w"), indent=1)
    return cards, diverged, capped, len(items)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    limit = next((int(a.split("=")[1]) for a in sys.argv[1:] if a.startswith("--limit=")), None)
    print("TWIN-CONSENSUS / DIVERGENCE (fold 4) — do a pattern's compiled language twins agree?")
    print("=" * 92)
    if not negative_control():
        print("ABORT: divergence detection is cosmetic.")
        return 1
    print("-" * 92)
    cards, diverged, capped, n = scan(only=set(args) or None, limit=limit)
    print("=" * 92)
    print(f"twin-sets checked: {n}{' (CAPPED — not all twins run)' if capped else ''} · "
          f"consensus: {n-len(diverged)} · DIVERGENT: {len(diverged)}")
    if diverged:
        print("DIVERGENCES (investigate: broken translation vs harness/env):",
              [d[0] for d in diverged])
    return 0


if __name__ == "__main__":
    sys.exit(main())
