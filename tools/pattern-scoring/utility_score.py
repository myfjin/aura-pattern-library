#!/usr/bin/env python3
"""
utility_score — frozen, versioned utility coefficient for data-science patterns.

Merged from:
  - sixelement's gate-suite/utility_score.py (CLI shape, auto-estimate heuristics,
    interactive mode, A/M/R/T/N dimensions)
  - fifth_state's two-instrument refinements:
      1. SENSE pre-filter before any scoring
      2. VALIDITY hard gate before U (any fail → U = 0)
      3. Missing evidence → U = null, never made-up 0.5
      4. M < threshold rejects only when measured
      5. Weights/thresholds/reference dataset frozen in versioned rubric
      6. Flags, never auto-deletes

U = (W1*A + W2*M + W3*R + W4*T + W5*N) / (W1+W2+W3+W4+W5)

Usage:
  utility_score.py <pattern.py>                                    # score one file
  utility_score.py <pattern.py> --validity report.json --evidence ev.json
  utility_score.py <pattern.py> --abuse --json                    # evidence card + fuzz
  utility_score.py --dir <directory> --rank                         # score all .py
  utility_score.py --dir <dir> --threshold 0.5 --rubric rubric.yaml
  utility_score.py --selftest

Non-destructive policy: this tool only FLAGS patterns. Illia decides what happens.
"""

import argparse
import ast
import glob
import importlib.util
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


def load_evidence_runner() -> Any:
    here = Path(__file__).resolve().parent
    er_path = here / "evidence_runner.py"
    if not er_path.exists():
        return None
    spec = importlib.util.spec_from_file_location("evidence_runner", er_path)
    er = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(er)
    return er


ER_MODULE: Optional[Any] = None


def get_evidence_runner() -> Optional[Any]:
    global ER_MODULE
    if ER_MODULE is None:
        ER_MODULE = load_evidence_runner()
    return ER_MODULE


# ─── DEFAULT RUBRIC (frozen, versioned) ───────────────────────────────────
DEFAULT_RUBRIC = {
    "version": "1.0.0",
    "description": "Merged generalization/correctness rubric for DS patterns.",
    "weights": {"A": 0.35, "M": 0.35, "R": 0.15, "T": 0.15, "N": 0.00},
    "thresholds": {
        "reject_measured_m": 0.30,
        "flag_missing_evidence": True,
        "library_min_u": 0.75,
        "review_min_u": 0.50,
    },
    "reference_dataset": {"name": "none", "version": "none"},
    "sense_filter": {
        "banned_prefixes": [
            "sklearn.",
            "scipy.",
            "statsmodels.",
            "numpy.mean",
            "np.mean",
            "pandas.DataFrame",
        ],
        "min_docstring_lines": 3,
        "min_function_lines": 5,
    },
}

DIM_NAMES = {
    "A": "Appropriateness — matches the problem setup",
    "M": "Model/Metric improvement + reliability",
    "R": "Reusability — reusable across datasets/projects",
    "T": "Tradeoff/cost — complexity, compute, maintenance",
    "N": "Novelty — fills a gap not covered by standard libraries",
}


# ─── DATA CLASSES ─────────────────────────────────────────────────────────
@dataclass(frozen=True)
class ScoreComponent:
    score: Optional[float]
    evidence: Optional[str]
    measured: bool


@dataclass
class PatternScore:
    file: str
    name: str
    rubric_version: str
    sense_pass: Optional[bool]
    sense_reason: Optional[str]
    description_pass: Optional[bool]
    description_reason: Optional[str]
    validity_gates: dict[str, bool]
    validity_pass: bool
    A: ScoreComponent
    M: ScoreComponent
    R: ScoreComponent
    T: ScoreComponent
    N: ScoreComponent
    U: Optional[float]
    status: str
    flags: list[str]
    evidence_card: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "file": self.file,
            "name": self.name,
            "rubric_version": self.rubric_version,
            "sense_pass": self.sense_pass,
            "sense_reason": self.sense_reason,
            "description_pass": self.description_pass,
            "description_reason": self.description_reason,
            "validity_gates": self.validity_gates,
            "validity_pass": self.validity_pass,
            "A": {"score": self.A.score, "evidence": self.A.evidence, "measured": self.A.measured},
            "M": {"score": self.M.score, "evidence": self.M.evidence, "measured": self.M.measured},
            "R": {"score": self.R.score, "evidence": self.R.evidence, "measured": self.R.measured},
            "T": {"score": self.T.score, "evidence": self.T.evidence, "measured": self.T.measured},
            "N": {"score": self.N.score, "evidence": self.N.evidence, "measured": self.N.measured},
            "U": self.U,
            "status": self.status,
            "flags": self.flags,
            "evidence_card": self.evidence_card,
        }


# ─── SENSE PRE-FILTER ─────────────────────────────────────────────────────
def _imports_from_banned(tree: ast.AST, banned_bases: list[str]) -> bool:
    """Detect `from <banned> import ...` or `import <banned>`."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                base = alias.name.split(".")[0]
                if base in banned_bases:
                    return True
        elif isinstance(node, ast.ImportFrom):
            base = (node.module or "").split(".")[0]
            if base in banned_bases:
                return True
    return False


def _is_trivial_wrapper(tree: ast.AST, banned_prefixes: list[str]) -> bool:
    """A trivial wrapper has a top-level function whose body is only a return
    call (e.g., def mean(x): return np.mean(x), or def train(X,y): return
    LogisticRegression().fit(X,y)). Imports from a banned module alone are
    not enough; the function must be structurally trivial."""
    banned_bases = [p.rstrip(".") for p in banned_prefixes]
    imports_banned = _imports_from_banned(tree, banned_bases)

    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        body = [s for s in node.body if not isinstance(s, ast.Expr) or not isinstance(s.value, ast.Constant)]  # ast.Str removed in py3.12+; Constant covers str literals since 3.8
        if len(body) != 1:
            continue
        stmt = body[0]
        if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            func = call.func
            name = ""
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = ast.unparse(func) if hasattr(ast, "unparse") else func.attr
            for prefix in banned_prefixes:
                base = prefix.rstrip(".")
                if name.startswith(prefix) or name.startswith(base):
                    return True
            # Also reject single-return-call wrappers that import from a banned module.
            if imports_banned:
                return True
    return False


def sense_check(pattern_text: str, rubric: dict) -> tuple[bool, Optional[str]]:
    cfg = rubric.get("sense_filter", {})
    text = pattern_text.strip()

    if len(text) < 100:
        return False, "File too short to be a meaningful pattern."

    try:
        tree = ast.parse(text)
    except SyntaxError:
        return False, "SyntaxError: cannot parse file."

    # Must contain at least one function or class to be a runnable pattern.
    has_runnable = any(
        isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef))
        for n in ast.iter_child_nodes(tree)
    )
    if not has_runnable:
        return False, "No top-level function or class found."

    banned = cfg.get("banned_prefixes", [])
    if _is_trivial_wrapper(tree, banned):
        return False, "Trivial wrapper: function body is only a return call to a banned prefix."

    # Hollow assertions: a "self-test" built only of tautologies (assert True,
    # assert 1==1) is fake and worthless. BUT `assert False, "..."` is a deliberate
    # negative-test / unreachability marker (cause-the-disaster-prove-rejection) —
    # the strongest kind of check — so it must NEVER be flagged. Flag ONLY when a
    # file HAS assertions and EVERY one of them is a tautology.
    _asserts = [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]

    def _is_tautology(a: ast.Assert) -> bool:
        t = a.test
        if isinstance(t, ast.Constant) and t.value is True:
            return True
        if (isinstance(t, ast.Compare) and len(t.ops) == 1
                and isinstance(t.ops[0], ast.Eq)
                and isinstance(t.left, ast.Constant)
                and len(t.comparators) == 1
                and isinstance(t.comparators[0], ast.Constant)):
            return t.left.value == t.comparators[0].value
        return False

    if _asserts and all(_is_tautology(a) for a in _asserts):
        return False, "hollow_assert: all assertions are tautologies (assert True / 1==1)"

    return True, None


# ─── DESCRIPTION CHECKS ────────────────────────────────────────────────────
def _first_meaningful_docstring(pattern_text: str) -> str:
    """Module docstring, or the first class/function docstring, or empty."""
    try:
        tree = ast.parse(pattern_text)
    except SyntaxError:
        return ""
    doc = ast.get_docstring(tree) or ""
    if doc.strip():
        return doc.strip()
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node) or ""
            if doc.strip():
                return doc.strip()
    return ""


def has_description(pattern_text: str) -> tuple[bool, Optional[str]]:
    """Return (has_description, reason). No description -> auto-quarantine before U."""
    docstring = _first_meaningful_docstring(pattern_text)
    if not docstring or not docstring.strip():
        return False, "no_docstring"
    return True, None


def extract_docstring(pattern_text: str) -> str:
    return _first_meaningful_docstring(pattern_text)


# ─── VALIDITY GATE CHECK ───────────────────────────────────────────────────
def check_validity(validity_report: Optional[dict]) -> tuple[dict[str, bool], bool]:
    if not validity_report:
        return {}, False
    gates = validity_report.get("gates", validity_report)
    results = {k: bool(v) for k, v in gates.items() if isinstance(v, bool)}
    if not results:
        return {}, False
    return results, all(results.values())


# ─── EVIDENCE PARSING ─────────────────────────────────────────────────────
def parse_component(label: str, data: Any) -> tuple[Optional[float], Optional[str], bool]:
    score: Optional[float] = None
    evidence: Optional[str] = None
    measured = False

    if isinstance(data, dict):
        score_raw = data.get("score")
        evidence = data.get("evidence") or data.get("source") or data.get("note")
        measured = bool(data.get("measured", evidence is not None and score_raw is not None))
        if score_raw is not None:
            try:
                score = float(score_raw)
            except (TypeError, ValueError):
                score = None
    elif isinstance(data, (int, float)):
        score = float(data)
        measured = True
    elif isinstance(data, str):
        evidence = data
        measured = False

    return score, evidence, measured


def compute_u(components: dict[str, ScoreComponent], weights: dict[str, float]) -> tuple[Optional[float], list[str]]:
    flags: list[str] = []
    numerator = 0.0
    denominator = 0.0
    has_missing_required = False

    for key in DIM_NAMES:
        comp = components[key]
        w = weights.get(key, 0.0)
        if w == 0.0:
            # Zero-weight dimensions are optional; missing them does not block U.
            if comp.score is not None:
                numerator += w * comp.score
                denominator += w
            continue
        if comp.score is None:
            has_missing_required = True
            flags.append(f"{key}: missing evidence -> UNDEFINED")
        else:
            numerator += w * comp.score
            denominator += w

    if has_missing_required:
        return None, flags
    if denominator == 0.0:
        return 0.0, ["sum_of_weights_is_zero"]
    return numerator / denominator, flags


# ─── AUTO-ESTIMATE HEURISTICS (sixelement's logic, evidence-aware) ─────────
def estimate_from_pattern(filepath: str) -> Optional[dict[str, Any]]:
    """Return placeholder structure only; scores stay UNDEFINED until measured.

    The old heuristic filled A/M/R/T/N with 0.5/0.6/0.8 "auto-estimates". That
    violated the rule "missing evidence = UNDEFINED, never 0.5". We keep the
    heuristic notes as qualitative evidence, but score is null and measured=False.
    """
    with open(filepath) as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    docstring = ast.get_docstring(tree) or ""
    doc_lower = docstring.lower()

    notes: list[str] = []

    a_indicators = {
        "time_series": ["time series", "temporal", "sequential", "walk forward", "rolling"],
        "imbalance": ["imbalance", "rare", "skewed", "unbalanced"],
        "leakage": ["leakage", "data leakage", "target leakage"],
        "causal": ["causal", "treatment", "confound"],
        "production": ["production", "deployment", "monitoring", "drift"],
    }
    a_hits = [ctx for ctx, kws in a_indicators.items() if any(kw in doc_lower for kw in kws)]
    if a_hits:
        notes.append(f"context hints: {', '.join(a_hits)}")

    m_indicators = [
        "improve", "lift", "gain", "better", "metric", "score", "auc", "accuracy",
        "f1", "mse", "rmse", "calibration", "stability", "robust", "variance", "bias",
    ]
    m_hits = [kw for kw in m_indicators if kw in doc_lower]
    if m_hits:
        notes.append(f"metric keywords: {', '.join(m_hits[:5])}")

    r_indicators = ["reusable", "generic", "any dataset", "pipeline", "step", "component", "plug", "drop-in"]
    r_hits = [kw for kw in r_indicators if kw in doc_lower]
    if r_hits:
        notes.append(f"reuse keywords: {', '.join(r_hits[:5])}")

    lines = source.split("\n")
    notes.append(f"{len(lines)} lines")

    expensive = ["for", "while", "nested", "O(n", "O(N"]
    if any(kw in source for kw in expensive):
        notes.append("contains loops/expensive ops")

    n_imports = sum(1 for lib in ["sklearn", "scipy", "numpy", "pandas"] if f"import {lib}" in source or f"from {lib}" in source)
    notes.append(f"{n_imports} ds-library imports")

    evidence_note = "auto placeholder (unmeasured)" + ("; " + " | ".join(notes) if notes else "")

    scores: dict[str, Any] = {
        "A": {"score": None, "evidence": evidence_note, "measured": False},
        "M": {"score": None, "evidence": evidence_note, "measured": False},
        "R": {"score": None, "evidence": evidence_note, "measured": False},
        "T": {"score": None, "evidence": evidence_note, "measured": False},
        "N": {"score": None, "evidence": evidence_note, "measured": False},
    }

    return scores


# ─── INTERACTIVE INPUT ─────────────────────────────────────────────────────
def prompt_score(dim_name: str) -> ScoreComponent:
    while True:
        val = input(f"  {dim_name} (0..1 or 'skip'): ").strip()
        if val.lower() in ("skip", "", "s"):
            return ScoreComponent(None, None, False)
        try:
            f = float(val)
            if 0.0 <= f <= 1.0:
                ev = input(f"    evidence for {dim_name}: ").strip() or None
                return ScoreComponent(f, ev, ev is not None)
            print("    Must be between 0 and 1.")
        except ValueError:
            print("    Enter a number or 'skip'.")


def prompt_description_review(docstring: str) -> tuple[bool, str]:
    """Interactive Illia manual gate. Returns (pass, reason)."""
    print("\n=== DESCRIPTION REVIEW ===")
    print(docstring[:800])
    print("=== END DESCRIPTION ===\n")

    def ask(q: str) -> bool:
        while True:
            a = input(f"{q} (y/n): ").strip().lower()
            if a in ("y", "yes"):
                return True
            if a in ("n", "no"):
                return False
            print("    Answer 'y' or 'n'.")

    d1 = ask("① What it does — do you understand the purpose?")
    if not d1:
        return False, "D1_manual_fail: purpose unclear"
    d2 = ask("② When to use it — do you know the right situation?")
    if not d2:
        return False, "D2_manual_fail: usage situation unclear"
    d3 = ask("③ What it guarantees — do you know the output/promise?")
    if not d3:
        return False, "D3_manual_fail: guarantees unclear"
    d4 = ask("④ Plain words — is the description jargon-free enough for you?")
    if not d4:
        return False, "D4_manual_fail: too jargon-opaque"

    return True, "manual_review_pass"


# ─── ABUSE / FUZZ GATE ───────────────────────────────────────────────────────
def abuse_invalid(card: Optional[dict[str, Any]]) -> bool:
    """Illia's anti-theater rule: type-breaking input that does NOT error and
    produces output is treated as silently wrong until a human overrides it.
    """
    if not card:
        return False
    return card.get("failing_column") in ("abuse_silent_output", "abuse_wrong")


def run_evidence_card(filepath: str) -> Optional[dict[str, Any]]:
    er = get_evidence_runner()
    if er is None:
        return None
    try:
        card = er.run_evidence(filepath)
        return card.to_dict()
    except Exception as e:
        return {"pattern_id": filepath, "failing_column": "evidence_runner_error", "evidence": [str(e)]}


# ─── CORE SCORING FUNCTION ─────────────────────────────────────────────────
def score_pattern(
    filepath: str,
    rubric: dict,
    validity_report: Optional[dict] = None,
    evidence: Optional[dict] = None,
    interactive: bool = False,
    fallback_auto: bool = True,
    description_review: bool = False,
    abuse: bool = False,
) -> PatternScore:
    name = os.path.splitext(os.path.basename(filepath))[0]
    weights = rubric.get("weights", DEFAULT_RUBRIC["weights"])
    thresholds = rubric.get("thresholds", DEFAULT_RUBRIC["thresholds"])

    # 1. Read file + optionally build the evidence card up front
    try:
        text = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=False, sense_reason=f"read error: {e}",
            description_pass=None, description_reason=None,
            validity_gates={}, validity_pass=False,
            A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
            R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
            N=ScoreComponent(None, None, False),
            U=None, status="flagged", flags=["read_error"], evidence_card=None,
        )

    evidence_card = run_evidence_card(filepath) if abuse else None

    # 2. SENSE pre-filter
    sense_ok, sense_reason = sense_check(text, rubric)
    if not sense_ok:
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=False, sense_reason=sense_reason,
            description_pass=None, description_reason=None,
            validity_gates={}, validity_pass=False,
            A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
            R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
            N=ScoreComponent(None, None, False),
            U=None, status="senseless", flags=[f"senseless: {sense_reason}"],
            evidence_card=evidence_card,
        )

    # 2b. DOMAIN gate: fuzzing requires a declared valid-input domain.
    if abuse and evidence_card and evidence_card.get("failing_column") == "domain_undefined":
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=True, sense_reason=None,
            description_pass=True, description_reason=None,
            validity_gates={}, validity_pass=True,
            A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
            R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
            N=ScoreComponent(None, None, False),
            U=None, status="quarantine_undefined_domain",
            flags=["undefined_domain: no declared valid-input domain"],
            evidence_card=evidence_card,
        )

    # 3. VALIDITY hard gate (no description injection)
    gates, validity_ok = check_validity(validity_report)
    validity_missing = not validity_report
    if not validity_ok and not validity_missing:
        flags = [f"validity_gate_failed: {k}" for k, v in gates.items() if not v]
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=True, sense_reason=None,
            description_pass=None, description_reason=None,
            validity_gates=gates, validity_pass=False,
            A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
            R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
            N=ScoreComponent(None, None, False),
            U=0.0, status="invalid", flags=flags, evidence_card=evidence_card,
        )

    # 4. AUTO-QUARANTINE: no description at all
    has_desc, desc_reason = has_description(text)
    if not has_desc:
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=True, sense_reason=None,
            description_pass=False, description_reason=f"auto_quarantine: {desc_reason}",
            validity_gates=gates, validity_pass=True,
            A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
            R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
            N=ScoreComponent(None, None, False),
            U=None, status="quarantine_no_description",
            flags=["no_description: auto-quarantine, gets one rewrite attempt"],
            evidence_card=evidence_card,
        )

    # 5. Build A/M/R/T/N components and compute U
    components: dict[str, ScoreComponent] = {}

    if interactive:
        print(f"\n── {name} ──")
        for key in DIM_NAMES:
            components[key] = prompt_score(f"{key}: {DIM_NAMES[key]}")
    elif evidence:
        for key in DIM_NAMES:
            s, ev, m = parse_component(key, evidence.get(key))
            if s is not None:
                s = max(0.0, min(1.0, s))
            components[key] = ScoreComponent(s, ev, m)
    elif fallback_auto:
        estimated = estimate_from_pattern(filepath)
        if estimated is None:
            return PatternScore(
                file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
                sense_pass=True, sense_reason=None,
                description_pass=True, description_reason=None,
                validity_gates=gates, validity_pass=True,
                A=ScoreComponent(None, None, False), M=ScoreComponent(None, None, False),
                R=ScoreComponent(None, None, False), T=ScoreComponent(None, None, False),
                N=ScoreComponent(None, None, False),
                U=None, status="flagged", flags=["parse_error"],
                evidence_card=evidence_card,
            )
        for key in DIM_NAMES:
            s, ev, m = parse_component(key, estimated.get(key))
            if s is not None:
                s = max(0.0, min(1.0, s))
            components[key] = ScoreComponent(s, ev, m)
    else:
        for key in DIM_NAMES:
            components[key] = ScoreComponent(None, None, False)

    # 6. ABUSE hard gate: silently-wrong type-breaking behavior = INVALID
    flags: list[str] = []
    if abuse_invalid(evidence_card):
        flags.append(f"abuse_silent_wrong:{evidence_card['failing_column']}")
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=True, sense_reason=None,
            description_pass=True, description_reason=None,
            validity_gates=gates, validity_pass=False,
            A=components["A"], M=components["M"], R=components["R"],
            T=components["T"], N=components["N"],
            U=0.0, status="invalid", flags=flags,
            evidence_card=evidence_card,
        )

    # 7. M < threshold reject only when measured
    m_comp = components["M"]
    if m_comp.score is not None and m_comp.score < thresholds.get("reject_measured_m", 0.30):
        return PatternScore(
            file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
            sense_pass=True, sense_reason=None,
            description_pass=True, description_reason=None,
            validity_gates=gates, validity_pass=True,
            A=components["A"], M=components["M"], R=components["R"],
            T=components["T"], N=components["N"],
            U=0.0, status="rejected_low_m",
            flags=[f"M={m_comp.score:.2f} < threshold {thresholds.get('reject_measured_m', 0.30)}"],
            evidence_card=evidence_card,
        )

    # 8. Compute U
    U, missing_flags = compute_u(components, weights)
    flags.extend(missing_flags)
    if validity_missing:
        flags.append("validity_report_missing")

    # Evidence-verified shortcut: a clean evidence card (sense ok, description ok,
    # no abuse failures, no undefined domain) is enough for VERIFIED when no external
    # validity report has been supplied. Prevents valid patterns stalling at
    # "needs_validity" when the runtime evidence itself proves the pattern.
    evidence_clean = (
        evidence_card is not None
        and evidence_card.get("failing_column") is None
        and evidence_card.get("success_run") is not None
        and evidence_card["success_run"].get("ok") is True
    )

    # Evidence-verified promotion comes before U=None handling so that a clean
    # runtime evidence card (claim + success + no abuse/domain failures) yields
    # VERIFIED even when no measured A/M/R/T/N evidence has been supplied yet.
    if validity_missing and evidence_clean:
        status = "VERIFIED"
    elif validity_missing:
        status = "needs_validity"
    elif U is None:
        status = "flagged"
    elif U >= thresholds.get("library_min_u", 0.75):
        status = "library_ready"
    elif U >= thresholds.get("review_min_u", 0.50):
        status = "review"
    else:
        status = "flagged"

    if evidence_card and evidence_card.get("failing_column"):
        flags.append(f"evidence:{evidence_card['failing_column']}")

    # 9. MANUAL DESCRIPTION REVIEW (after U, for --description-review mode)
    if description_review:
        docstring = extract_docstring(text)
        manual_ok, manual_reason = prompt_description_review(docstring)
        if not manual_ok:
            return PatternScore(
                file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
                sense_pass=True, sense_reason=None,
                description_pass=False, description_reason=manual_reason,
                validity_gates=gates, validity_pass=True,
                A=components["A"], M=components["M"], R=components["R"],
                T=components["T"], N=components["N"],
                U=U, status="gone",
                flags=[f"manual_description: {manual_reason}"],
                evidence_card=evidence_card,
            )

    return PatternScore(
        file=filepath, name=name, rubric_version=rubric.get("version", "unknown"),
        sense_pass=True, sense_reason=None,
        description_pass=True, description_reason=None,
        validity_gates=gates, validity_pass=True,
        A=components["A"], M=components["M"], R=components["R"],
        T=components["T"], N=components["N"],
        U=U, status=status, flags=flags,
        evidence_card=evidence_card,
    )


# ─── OUTPUT FORMATTING ─────────────────────────────────────────────────────
def print_result(result: PatternScore, verbose: bool = False):
    u = result.U
    u_str = f"{u:.3f}" if u is not None else "null "
    bar = "█" * int((u or 0.0) * 20) if u is not None else ""
    print(f"{u_str}  {bar}  {result.status:<16}  {result.name}")
    if verbose:
        for key in DIM_NAMES:
            comp = getattr(result, key)
            s = f"{comp.score:.2f}" if comp.score is not None else "null"
            ev = comp.evidence or "no evidence"
            print(f"       {key}={s}  ({ev})")
        if result.flags:
            print(f"       flags: {', '.join(result.flags)}")


# ─── RUBRIC LOADING ────────────────────────────────────────────────────────
def load_rubric(path: Optional[str]) -> dict:
    if path is None:
        return DEFAULT_RUBRIC
    p = Path(path)
    if not p.exists():
        print(f"[WARN] Rubric not found at {path}; using default v{DEFAULT_RUBRIC['version']}", file=sys.stderr)
        return DEFAULT_RUBRIC
    text = p.read_text(encoding="utf-8")
    if p.suffix in (".yaml", ".yml"):
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


# ─── CLI ───────────────────────────────────────────────────────────────────
def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Frozen, versioned utility coefficient for DS patterns.")
    parser.add_argument("pattern", nargs="?", help="Single .py pattern file to score.")
    parser.add_argument("--dir", help="Directory of .py patterns to score.")
    parser.add_argument("--rubric", help="Path to frozen rubric YAML/JSON.")
    parser.add_argument("--validity", help="Path to validity gate report JSON.")
    parser.add_argument("--evidence", help="Path to A/M/R/T/N evidence JSON.")
    parser.add_argument("--interactive", action="store_true", help="Prompt for A/M/R/T/N scores.")
    parser.add_argument("--description-review", action="store_true", help="Prompt for manual D1-D4 description gate (Illia's rule).")
    parser.add_argument("--auto", action="store_true", help="Force auto-estimate even if evidence given.")
    parser.add_argument("--no-auto", action="store_true", help="Do not fall back to auto-estimate; missing = null.")
    parser.add_argument("--rank", action="store_true", help="Sort results by U descending.")
    parser.add_argument("--threshold", type=float, default=0.0, help="Only show U >= threshold.")
    parser.add_argument("--weights", help="DEPRECATED: weights are frozen in rubric. Use --rubric to change set.")
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    parser.add_argument("--verbose", action="store_true", help="Show per-dimension scores.")
    parser.add_argument("--abuse", action="store_true", help="Run runtime evidence card (success + adversary + fuzz).")
    parser.add_argument("--selftest", action="store_true", help="Run numeric self-test.")
    args = parser.parse_args(argv[1:])

    if args.weights:
        print("[WARN] --weights is deprecated; weights are frozen in the rubric. Use --rubric.", file=sys.stderr)

    rubric = load_rubric(args.rubric)

    validity_report = None
    if args.validity:
        with open(args.validity, "r", encoding="utf-8") as f:
            validity_report = json.load(f)

    evidence = None
    if args.evidence:
        with open(args.evidence, "r", encoding="utf-8") as f:
            evidence = json.load(f)

    if args.selftest:
        return selftest(rubric)

    fallback_auto = not args.no_auto
    if args.auto:
        evidence = None

    if args.pattern:
        result = score_pattern(
            args.pattern, rubric, validity_report, evidence,
            interactive=args.interactive, fallback_auto=fallback_auto,
            description_review=args.description_review, abuse=args.abuse,
        )
        if args.json:
            print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        else:
            print_result(result, verbose=True)
        return 0

    if args.dir:
        pattern = os.path.join(args.dir, "**", "*.py")
        files = sorted(glob.glob(pattern, recursive=True))
        if not files:
            print(f"No .py files found in {args.dir}", file=sys.stderr)
            return 1

        results: list[PatternScore] = []
        for f in files:
            r = score_pattern(
                f, rubric, validity_report, evidence,
                fallback_auto=fallback_auto,
                description_review=args.description_review, abuse=args.abuse,
            )
            results.append(r)

        if args.rank:
            # null sorts to bottom
            results.sort(key=lambda x: (x.U is None, -(x.U or 0.0)))

        if args.json:
            print(json.dumps([r.to_dict() for r in results], indent=2, ensure_ascii=False))
        else:
            print(f"\nUtility scores for {len(results)} patterns in {args.dir}")
            print(f"Rubric: {rubric.get('version')} | weights: A={rubric['weights']['A']} M={rubric['weights']['M']} R={rubric['weights']['R']} T={rubric['weights']['T']} N={rubric['weights']['N']}")
            print("=" * 80)
            for r in results:
                if (r.U is not None and r.U >= args.threshold) or (r.U is None and args.threshold == 0.0):
                    print_result(r, verbose=args.verbose)

            if args.threshold > 0:
                below = [r for r in results if r.U is not None and r.U < args.threshold]
                print(f"\n--- {len(below)} patterns below threshold {args.threshold} ---")
                for r in below[:10]:
                    print(f"  {r.U:.3f}  {r.status:<16}  {r.name}")
                if len(below) > 10:
                    print(f"  ... and {len(below)-10} more")
        return 0

    parser.print_help(sys.stderr)
    return 2


def selftest(rubric: dict) -> int:
    weights = rubric["weights"]
    cases = [
        ({"A": 0.9, "M": 0.7, "R": 0.8, "T": 0.6, "N": 0.0}, 0.770),
        ({"A": 1.0, "M": 0.9, "R": 0.7, "T": 0.5, "N": 0.0}, 0.845),
        ({"A": 0.6, "M": 0.7, "R": 0.5, "T": 0.3, "N": 0.0}, 0.575),
    ]
    ok = 0
    for scores, expected in cases:
        components = {k: ScoreComponent(v, "selftest", True) for k, v in scores.items()}
        u, _ = compute_u(components, weights)
        got = round(u, 3) if u is not None else None
        flag = "ok" if got == expected else "FAIL"
        ok += (flag == "ok")
        print(f"  [{flag}] U({scores}) = {got} (expected {expected:.3f})")
    print(f"selftest {ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
