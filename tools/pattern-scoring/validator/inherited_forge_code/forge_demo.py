#!/usr/bin/env python3
"""Forge Gate — end-to-end demo.

Runs a candidate file through every verification lens and prints the layered
verdict. Zero LLM in any verdict path — compile, run, compare to the signed
oracle. This is the Archestra demo: PASS means it survived every angle; FAIL
means at least one execution-backed lens caught it, and it tells you which.
"""
from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path

ROOT = Path("/home/au/forge-gate")
PY = sys.executable
ENV = dict(os.environ, PYTHONPATH=f"{ROOT}/src:{ROOT}/tools", PYTHONDONTWRITEBYTECODE="1")
VERD = re.compile(r"\b(RELATION-PASS|RELATION-FAIL|UNSUPPORTED|UNSTABLE|PASS|FAIL|SOLID|HOLLOW)\b")


def _run(cmd, cwd=ROOT):
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=str(cwd), env=ENV, timeout=120)
    m = VERD.search(p.stdout + p.stderr)
    return m.group(1) if m else "ERROR"


def _fixture_status(f, pattern):
    """Run the PURE property-primary fixture (not the integrated CLI)."""
    import json
    fx = ROOT / "src" / "forge_gate" / "fixtures" / f"{pattern}.py"
    p = subprocess.run([PY, str(fx), f], capture_output=True, text=True, cwd=str(ROOT), env=ENV, timeout=120)
    for line in (p.stdout + p.stderr).splitlines():
        if line.startswith("FORGE_GATE_RESULT "):
            try:
                return json.loads(line[len("FORGE_GATE_RESULT "):]).get("status", "ERROR")
            except Exception:
                pass
    return "ERROR"


def lenses(f, pattern):
    r = {}
    r["property-primary"] = _fixture_status(f, pattern)
    r["twin-consensus"] = _run([PY, "tools/twin_consensus.py", "verify", f, "--pattern", pattern])
    r["metamorphic"] = _run([PY, "-m", "metamorphic.runner", f, pattern])
    r["invariant"] = _run([PY, "tools/invariant_gate.py", "verify", f, "--pattern", pattern])
    return r


def overall(r):
    bad = {"FAIL", "RELATION-FAIL", "UNSTABLE", "HOLLOW", "ERROR"}
    # a lens that is UNSUPPORTED for this pattern doesn't count against the verdict
    applicable = {k: v for k, v in r.items() if v != "UNSUPPORTED"}
    if any(v in bad for v in applicable.values()):
        return "FAIL"
    return "PASS"


CASES = [
    ("examples say correct", "tests/corpus/linear_regression_gd_canonical_good.py", "linear_regression_gd",
     "A correct implementation."),
    ("correct — DIFFERENT algorithm", "tests/corpus/linreg_normal_eq.py", "linear_regression_gd",
     "Normal equations instead of gradient descent. Right answer, different method — must still PASS."),
    ("broken (sign flip)", "tests/corpus/linreg_broken_sign.py", "linear_regression_gd",
     "Gradient sign flipped — diverges."),
    ("the agent that did NOTHING", "/tmp/demo_noop.py", "linear_regression_gd",
     "Defines the function but returns without computing. The classic false-'done'."),
    ("subtly wrong — the base check MISSES it", "/tmp/demo_ratio.py", "linear_regression_gd",
     "Weights [2.4, 3.0] — plausible-looking but wrong. Pure property-primary PASSES it (R²>0.8, weights within tolerance). The metamorphic and invariant lenses CATCH it. This is exactly why one check isn't enough."),
]


def main():
    # build the two synthetic demo files
    Path("/tmp/demo_noop.py").write_text(
        "def linear_regression_gd(X, y, learning_rate=0.01, iterations=200):\n    return [0.0, 0.0], 0.0\n")
    Path("/tmp/demo_ratio.py").write_text(
        "def linear_regression_gd(X, y, learning_rate=0.01, iterations=200):\n    return [2.4, 3.0], 0.0\n")

    print("=" * 78)
    print("  FORGE GATE — deterministic verification for AI-generated code")
    print("  Four execution-backed lenses. Zero LLM in the verdict path.")
    print("=" * 78)
    cols = ["property-primary", "twin-consensus", "metamorphic", "invariant"]
    for title, f, pattern, desc in CASES:
        r = lenses(f, pattern)
        ov = overall(r)
        badge = "✅ PASS" if ov == "PASS" else "❌ FAIL"
        print(f"\n▶ {title}   →   {badge}")
        print(f"  {desc}")
        line = "   ".join(f"{c}={r[c]}" for c in cols)
        print(f"  lenses: {line}")
    print("\n" + "=" * 78)
    print("  PASS = compiled, ran, and matched the signed oracle across every lens.")
    print("  FAIL = at least one deterministic check caught it — and named which.")
    print("=" * 78)


if __name__ == "__main__":
    main()
