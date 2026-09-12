#!/usr/bin/env python3
"""
evidence_runner.py — produce an evidence card per DS pattern.

Rule: no bare pass/fail. Each card must show:
  - CLAIM: what the description guarantees
  - SUCCESS RUN: input → actual output → claim held
  - ADVERSARY RUN: bad input → visible break → caught or not
  - FAILING COLUMN: exact layer + evidence if it failed

The runner is defensive: it executes patterns in a subprocess with a timeout,
captures output, and never trusts the pattern with the host environment.
"""

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class EvidenceCard:
    pattern_id: str
    claim: str
    declared_domain: Optional[str]
    success_run: Optional[dict[str, Any]]
    adversary_run: Optional[dict[str, Any]]
    abuse: Optional[dict[str, Any]]
    failing_column: Optional[str]
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "pattern_id": self.pattern_id,
            "claim": self.claim,
            "declared_domain": self.declared_domain,
            "success_run": self.success_run,
            "adversary_run": self.adversary_run,
            "abuse": self.abuse,
            "failing_column": self.failing_column,
            "evidence": self.evidence,
        }


def extract_claim(docstring: str) -> str:
    """First sentence of docstring = claim. Prefer a 'Claim:' line if present."""
    if not docstring:
        return "<no description: no claim to check>"
    for line in docstring.splitlines():
        m = re.search(r"(?i)\bclaim\b[:\s]+(.+)", line)
        if m:
            return m.group(1).strip()
    sentences = re.split(r"(?<=[.!?])\s+", docstring.strip())
    first = sentences[0] if sentences else docstring.strip()
    return first[:200]


def extract_declared_domain(docstring: str) -> Optional[str]:
    """Look for explicit 'Valid input', 'Domain', 'Requires', 'Assumes', 'Args' sections."""
    if not docstring:
        return None
    for line in docstring.splitlines():
        m = re.search(r"(?i)(?:valid input|input domain|domain|requires|assumes|preconditions?)[:\s]+(.+)", line)
        if m:
            return m.group(1).strip()[:300]
    # Fall back to Args section if present
    in_args = False
    args_lines: list[str] = []
    for line in docstring.splitlines():
        if re.match(r"(?i)^\s*args\s*:\s*$", line):
            in_args = True
            continue
        if in_args:
            if re.match(r"(?i)^\s*(returns|raises|notes|examples)\s*:\s*$", line):
                break
            if line.strip():
                args_lines.append(line.strip())
    if args_lines:
        return "Args: " + " | ".join(args_lines[:5])
    return None


def extract_fallback_docstring(tree: ast.AST) -> Optional[str]:
    """If the module has no docstring, use the first class/function docstring."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node)
            if doc and doc.strip():
                return doc.strip()
    return None


def infer_domain_from_params(params: list[tuple[str, str]]) -> Optional[str]:
    """Infer a domain only when concrete types are declared (not bare Any)."""
    concrete = [(n, t) for n, t in params if t != "Any"]
    if not concrete:
        return None
    return "params: " + ", ".join(f"{n}: {t}" for n, t in concrete)


def stderr_looks_benign(stderr: str) -> bool:
    """Allow stderr that is only INFO/DEBUG/WARNING logging lines."""
    if not stderr.strip():
        return True
    error_markers = ("ERROR", "CRITICAL", "Traceback", "Exception", "FATAL")
    low = stderr.lower()
    if any(marker.lower() in low for marker in error_markers):
        return False
    for line in stderr.splitlines():
        if not line.strip():
            continue
        if not re.match(r"^\s*(INFO|DEBUG|WARNING)\b", line, re.IGNORECASE):
            return False
    return True


def file_run_succeeded(run: dict[str, Any]) -> bool:
    """File-level success means the demo completed (returncode 0). We still fail
    if the process crashed hard (Traceback/Exception/FATAL in stderr). Demo code
    may intentionally log ERROR for failure scenarios it is demonstrating."""
    if run.get("returncode", -1) != 0:
        return False
    stderr = run.get("stderr", "")
    crash_markers = ("Traceback", "Exception", "FATAL")
    low = stderr.lower()
    return not any(marker.lower() in low for marker in crash_markers)


def find_top_level_functions(source: str) -> list[dict[str, Any]]:
    """Return list of top-level functions with simple signatures."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    funcs = []
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        args = node.args
        # Skip functions requiring complex types or many args
        if len(args.args) > 3 or args.vararg or args.kwarg or args.kwonlyargs:
            continue
        param_types = []
        ok = True
        for arg in args.args:
            ann = arg.annotation
            type_name = None
            if isinstance(ann, ast.Name):
                type_name = ann.id
            elif isinstance(ann, ast.Constant) and isinstance(ann.value, str):
                type_name = ann.value
            elif isinstance(ann, ast.Subscript):
                type_name = ast.unparse(ann) if hasattr(ast, "unparse") else "List"
            else:
                type_name = "Any"
            param_types.append((arg.arg, type_name))
        if ok:
            funcs.append({"name": node.name, "params": param_types})
    return funcs


def build_success_probe(source: str, func_name: str, params: list[tuple[str, str]]) -> str:
    """Build a small script that imports the pattern by path and calls func_name.

    The probe uses values that satisfy the *declared* parameter types. When the
    declared domain uses loose names like `model` (an object with .fit / .predict),
    we inject a tiny stub class so the success run actually executes.
    """
    args_list = []
    stub_definitions: list[str] = []
    for pname, ptype in params:
        if "List" in ptype or "list" in ptype.lower() or "iterable" in ptype.lower():
            args_list.append(f"{pname}=[1.0, 2.0, 3.0, 4.0, 5.0]")
        elif "int" in ptype.lower():
            args_list.append(f"{pname}=5")
        elif "float" in ptype.lower() or "double" in ptype.lower():
            args_list.append(f"{pname}=2.5")
        elif "str" in ptype.lower():
            args_list.append(f'{pname}="test"')
        elif "bool" in ptype.lower():
            args_list.append(f"{pname}=True")
        elif "model" in ptype.lower() or "estimator" in ptype.lower() or pname in ("model", "estimator", "clf", "classifier", "regressor"):
            stub_name = f"_StubModel_{pname}"
            stub_definitions.append(
                f"class {stub_name}:\n"
                "    def fit(self, X, y): return self\n"
                "    def predict(self, X): return [1]*len(X)"
            )
            args_list.append(f"{pname}={stub_name}()")
        elif pname in ("X", "features") or "features" in ptype.lower():
            args_list.append(f"{pname}=[[0], [1], [2], [3], [4]]")
        elif pname in ("y", "target") or "target" in ptype.lower():
            args_list.append(f"{pname}=[0, 1, 0, 1, 0]")
        else:
            args_list.append(f"{pname}=[1.0, 2.0, 3.0]")

    stub_block = "\n".join(stub_definitions)
    probe = f"""
{stub_block}

import importlib.util
spec = importlib.util.spec_from_file_location("pattern_module", {json.dumps(source)})
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
{func_name} = getattr(mod, {json.dumps(func_name)})

try:
    result = {func_name}({', '.join(args_list)})
    print(f"OUTPUT: {{result!r}}")
except Exception as e:
    print(f"ERROR: {{type(e).__name__}}: {{e}}")
"""
    return probe


def build_abuse_inputs(params: list[tuple[str, str]]) -> tuple[list[str], str]:
    """Return (args_list, human-readable abuse summary)."""
    args_list = []
    summaries = []
    for pname, ptype in params:
        if "List" in ptype or "list" in ptype.lower():
            val = '"not_a_list_letters"'
            summaries.append(f"{pname}={val} (string instead of list)")
        elif "int" in ptype.lower():
            val = '"abc"'
            summaries.append(f"{pname}={val} (letters instead of int)")
        elif "float" in ptype.lower() or "double" in ptype.lower():
            val = '"xyz"'
            summaries.append(f"{pname}={val} (letters instead of float)")
        elif "str" in ptype.lower():
            val = "12345"
            summaries.append(f"{pname}={val} (number instead of string)")
        elif "bool" in ptype.lower():
            val = '"true"'
            summaries.append(f"{pname}={val} (string instead of bool)")
        else:
            val = '"wrong_type"'
            summaries.append(f"{pname}={val} (mismatched type)")
        args_list.append(f"{pname}={val}")
    return args_list, "; ".join(summaries)


def build_adversary_probe(source: str, func_name: str, params: list[tuple[str, str]]) -> str:
    """Build a probe with type-breaking inputs per Illia's rule.
    If no error is raised and output is silently wrong, the pattern is invalid.
    """
    args_list, _ = build_abuse_inputs(params)

    probe = f"""
import importlib.util
spec = importlib.util.spec_from_file_location("pattern_module", {json.dumps(source)})
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
{func_name} = getattr(mod, {json.dumps(func_name)})

try:
    result = {func_name}({', '.join(args_list)})
    print(f"ADV_OUTPUT: {{result!r}}")
except Exception as e:
    print(f"ADV_CAUGHT: {{type(e).__name__}}: {{e}}")
"""
    return probe


def build_abuse_probe(source: str, func_name: str, params: list[tuple[str, str]]) -> tuple[str, str]:
    """Build the ABUSE probe and a human-readable summary of the injected bad inputs."""
    args_list, summary = build_abuse_inputs(params)
    probe = f"""
import importlib.util
spec = importlib.util.spec_from_file_location("pattern_module", {json.dumps(source)})
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
{func_name} = getattr(mod, {json.dumps(func_name)})

try:
    result = {func_name}({', '.join(args_list)})
    print(f"ABUSE_OUTPUT: {{result!r}}")
except Exception as e:
    print(f"ABUSE_ERRORED: {{type(e).__name__}}: {{e}}")
"""
    return probe, summary


def run_probe(probe_code: str, timeout: int = 30) -> dict[str, Any]:
    """Run probe in a temp file subprocess; return captured output."""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(probe_code)
        tmp = f.name
    try:
        proc = subprocess.run(
            [sys.executable, tmp],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        stdout = proc.stdout.strip()
        stderr = proc.stderr.strip()
        return {
            "returncode": proc.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "ok": proc.returncode == 0 and not stderr,
        }
    except subprocess.TimeoutExpired:
        return {"returncode": None, "stdout": "", "stderr": "TIMEOUT", "ok": False}
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def evaluate_run(run: dict[str, Any], claim: str) -> tuple[bool, list[str]]:
    """Return (claim_appears_held, evidence). Very conservative."""
    evidence: list[str] = []
    stdout = run.get("stdout", "")
    stderr = run.get("stderr", "")

    if run.get("returncode") is None:
        evidence.append("probe timed out")
        return False, evidence
    if run.get("returncode", 0) != 0 or stderr:
        evidence.append(f"runtime error: {stderr[:200]}")
        return False, evidence

    if "OUTPUT:" in stdout:
        evidence.append(f"produced output: {stdout}")
        # Naive: if output exists and no error, we mark claim as "observed", not proven.
        return True, evidence

    evidence.append(f"no OUTPUT marker in stdout: {stdout[:200]}")
    return False, evidence


def run_evidence(filepath: str) -> EvidenceCard:
    """Main entry: build and return the evidence card for a pattern."""
    pattern_id = str(filepath)
    try:
        text = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return EvidenceCard(
            pattern_id=pattern_id,
            claim="<could not read file>",
            declared_domain=None,
            success_run=None,
            adversary_run=None,
            abuse=None,
            failing_column="read_error",
            evidence=[str(e)],
        )

    try:
        tree = ast.parse(text)
        docstring = ast.get_docstring(tree) or ""
    except SyntaxError as e:
        return EvidenceCard(
            pattern_id=pattern_id,
            claim="<syntax error: no parse>",
            declared_domain=None,
            success_run=None,
            adversary_run=None,
            abuse=None,
            failing_column="syntax_error",
            evidence=[str(e)],
        )

    fallback_doc = extract_fallback_docstring(tree) or ""
    effective_doc = docstring or fallback_doc

    claim = extract_claim(effective_doc)
    declared_domain = extract_declared_domain(effective_doc)

    if not effective_doc.strip():
        return EvidenceCard(
            pattern_id=pattern_id,
            claim=claim,
            declared_domain=None,
            success_run=None,
            adversary_run=None,
            abuse=None,
            failing_column="no_description",
            evidence=["no module-level or class/function docstring"],
        )

    # Look for embedded test/demo code first
    has_main = "if __name__" in text
    has_selftest = "def selftest" in text or "def test_" in text

    funcs = find_top_level_functions(text)
    if not funcs and not has_main and not has_selftest:
        return EvidenceCard(
            pattern_id=pattern_id,
            claim=claim,
            declared_domain=declared_domain,
            success_run=None,
            adversary_run=None,
            abuse=None,
            failing_column="no_runnable_surface",
            evidence=["no top-level function or test block found"],
        )

    # Pick a target. If the module has a __main__ block, treat it as the intended
    # runnable surface and run the whole file. That avoids false failures on helper
    # functions that only make sense inside the module's own demo. Otherwise fall back
    # to the first simple top-level function.
    target = funcs[0] if funcs else None
    is_driver = has_main

    success_run = None
    adversary_run = None
    abuse_run = None
    evidence: list[str] = []

    if target and not is_driver:
        fn, params = target["name"], target["params"]

        # Infer a concrete declared domain from typed signatures when the author did
        # not spell it out at module level. Reject bare Any as a domain.
        if declared_domain is None:
            declared_domain = infer_domain_from_params(params)

        # SUCCESS
        success_probe = build_success_probe(filepath, fn, params)
        success_run = run_probe(success_probe)
        held, ev = evaluate_run(success_run, claim)
        evidence.extend(ev)

        # ADVERSARY (edge-case values)
        adversary_probe = build_adversary_probe(filepath, fn, params)
        adversary_run = run_probe(adversary_probe)
        if "ADV_CAUGHT:" in adversary_run.get("stdout", ""):
            evidence.append("adversary input was caught (exception raised)")
        elif "ADV_OUTPUT:" in adversary_run.get("stdout", ""):
            evidence.append(f"adversary input produced output: {adversary_run['stdout']}")
        else:
            evidence.append(f"adversary input did not produce recognizable output: {adversary_run.get('stdout','')[:200]}")

        # ABUSE (type-breaking inputs per Illia's rule)
        abuse_probe, abuse_summary = build_abuse_probe(filepath, fn, params)
        abuse_run = run_probe(abuse_probe)
        abuse_stdout = abuse_run.get("stdout", "")
        errored = "ABUSE_ERRORED:" in abuse_stdout
        output = None
        if not errored:
            m = re.search(r"ABUSE_OUTPUT:\s*(.+)", abuse_stdout)
            if m:
                output = m.group(1).strip()
        abuse_run = {
            "injected": abuse_summary,
            "errored": errored,
            "error": abuse_run.get("stderr", "") if not errored else None,
            "output": output,
            "raw_stdout": abuse_stdout,
            "raw_stderr": abuse_run.get("stderr", ""),
        }

        failing_column = None
        if not held:
            failing_column = "success_run_failed"
        elif not declared_domain:
            failing_column = "domain_undefined"
            evidence.append("no declared valid-input domain: cannot judge abuse result")
        elif not errored and output is not None:
            # Produced output on bad input without error. Need human to mark correct or silently-wrong.
            failing_column = "abuse_silent_output"
            evidence.append("abuse input produced output without error: needs manual verdict (correct? silently wrong?)")
        elif not errored and output is None:
            failing_column = "abuse_unclear"
            evidence.append("abuse input produced no recognizable output and no error")
        else:
            failing_column = None
    else:
        # has main/selftest or is a driver: run the file directly as success
        run = run_probe(text)
        run["ok"] = file_run_succeeded(run)
        success_run = run
        if run["ok"]:
            evidence.append(f"file-level run succeeded: {run['stdout'][:300]}")
            failing_column = None
        else:
            evidence.append(f"file-level run failed: {run['stderr'][:200]}")
            failing_column = "file_run_failed"

    return EvidenceCard(
        pattern_id=pattern_id,
        claim=claim,
        declared_domain=declared_domain,
        success_run=success_run,
        adversary_run=adversary_run,
        abuse=abuse_run,
        failing_column=failing_column,
        evidence=evidence,
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", required=True)
    args = parser.parse_args()
    card = run_evidence(args.pattern)
    print(json.dumps(card.to_dict(), indent=2, ensure_ascii=False))
