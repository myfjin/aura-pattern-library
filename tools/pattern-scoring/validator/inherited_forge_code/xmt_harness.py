#!/usr/bin/env python3
"""eXtreme Mutation Testing (XMT) harness for Forge Gate fixtures.

For each gate-ready pattern, we take the signed AURA oracle (the answer key),
neutralize each top-level function body one at a time, and run the pattern's
fixture against the mutant. A fixture that still returns PASS on a gutted oracle
is HOLLOW: the fixture didn't notice that the oracle produced garbage.

Usage:
    cd /home/au/forge-gate
    python3 tools/xmt_harness.py
"""
from __future__ import annotations

import ast
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
CATALOG_PATH = SRC_ROOT / "forge_gate" / "data" / "gate_catalog.json"
FIXTURES_DIR = SRC_ROOT / "forge_gate" / "fixtures"
LIBRARY_ROOT = Path("/home/au/aura-pattern-library")


@dataclass(frozen=True)
class MutantResult:
    pattern: str
    function: str
    mutant_index: int
    survived: bool  # True if fixture gave PASS on the mutant
    status: str
    reason: str


def load_catalog() -> Dict[str, Dict]:
    with open(CATALOG_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("patterns", {})


def parse_functions(source: str) -> List[ast.FunctionDef]:
    tree = ast.parse(source)
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def _extract_get_fn_calls(fixture_source: str) -> List[str]:
    """Parse a fixture and return the names of functions it loads from the user/oracle module."""
    tree = ast.parse(fixture_source)
    names: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id == "get_fn":
                if node.args and len(node.args) >= 2:
                    second = node.args[1]
                    if isinstance(second, ast.Constant) and isinstance(second.value, str):
                        names.append(second.value)
    return names


def _return_expr_for_returns(returns: Optional[ast.expr], default: ast.expr) -> ast.expr:
    """Build a return expression that is type-compatible with the annotation."""
    if returns is None:
        return default
    if isinstance(returns, ast.Constant):
        return ast.Constant(value=None)
    if isinstance(returns, ast.Name):
        if returns.id == "int":
            return ast.Constant(value=0)
        if returns.id == "float":
            return ast.Constant(value=0.0)
        if returns.id == "bool":
            return ast.Constant(value=False)
        if returns.id == "str":
            return ast.Constant(value="")
        if returns.id in ("List", "Tuple", "Dict"):
            return ast.Constant(value=None)
    if isinstance(returns, ast.Subscript):
        base = returns.value
        if isinstance(base, ast.Name):
            if base.id == "List":
                return ast.List(elts=[], ctx=ast.Load())
            if base.id == "Tuple":
                return ast.Tuple(elts=[], ctx=ast.Load())
            if base.id == "Dict":
                return ast.Dict(keys=[], values=[])
    return default


class FunctionBodyWiper(ast.NodeTransformer):
    """AST transformer that replaces a specific function body with a dumb return."""

    def __init__(self, target_name: str, return_value: ast.expr):
        self.target_name = target_name
        self.return_value = return_value

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        if node.name != self.target_name:
            return self.generic_visit(node)
        # Preserve decorators, signature, docstring; replace body with one return.
        new_node = ast.FunctionDef(
            name=node.name,
            args=node.args,
            body=[ast.Return(value=self.return_value)],
            decorator_list=node.decorator_list,
            returns=node.returns,
            type_comment=node.type_comment,
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return new_node


def generate_mutants(source: str, target_functions: Optional[List[str]] = None) -> List[Tuple[str, ast.AST]]:
    """Return (function_name, mutant_ast) pairs.

    Only mutates functions that the fixture actually exercises (via get_fn).
    Helper functions not loaded by the fixture are skipped so the harness
    doesn't report false hollows.
    """
    functions = parse_functions(source)
    targets = set(target_functions or [])
    mutants: List[Tuple[str, ast.AST]] = []
    for fn in functions:
        if fn.name.startswith("__"):
            continue
        if targets and fn.name not in targets:
            continue
        default_return = ast.Constant(value=None)
        return_expr = _return_expr_for_returns(fn.returns, default_return)
        transformer = FunctionBodyWiper(fn.name, return_expr)
        tree = ast.parse(source)
        mutant_tree = transformer.visit(tree)
        ast.fix_missing_locations(mutant_tree)
        mutants.append((fn.name, mutant_tree))
    return mutants


def run_fixture(fixture_script: Path, user_file: Path, pattern: str, timeout: float = 60.0) -> Tuple[str, str]:
    """Run a fixture script against a user/oracle file and parse the verdict."""
    runner = shutil.which("python3") or shutil.which("python")
    if not runner:
        raise RuntimeError("python3 not found on PATH")
    import os
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SRC_ROOT) + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    cmd = [runner, "-u", str(fixture_script), str(user_file)]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            cwd=str(REPO_ROOT),
        )
    except subprocess.TimeoutExpired:
        return "UNSTABLE", "fixture timed out"

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    # Fixtures emit a JSON line prefixed with FORGE_GATE_RESULT.
    for line in reversed(stdout.splitlines()):
        line = line.strip()
        if line.startswith("FORGE_GATE_RESULT "):
            payload = line[len("FORGE_GATE_RESULT "):]
            try:
                result = json.loads(payload)
                return result.get("status", "FAIL"), result.get("reason", "no reason")
            except json.JSONDecodeError:
                continue
    # Fall back to scanning for the status word.
    for word in ("PASS", "FAIL", "UNSTABLE", "UNSUPPORTED"):
        if word in stdout or word in stderr:
            return word, f"scanned status from output (exit {proc.returncode})"
    return "FAIL", f"no status found; exit={proc.returncode}; stderr={stderr[:200]}"


def evaluate_pattern(pattern: str, meta: Dict, verbose: bool = False) -> Tuple[int, int, List[MutantResult]]:
    """Run XMT on one pattern. Returns (killed, total, details)."""
    aura_path = LIBRARY_ROOT / meta["aura_path"]
    source = aura_path.read_text(encoding="utf-8")

    fixture_script = FIXTURES_DIR / f"{meta['fixture']}.py"
    if not fixture_script.exists():
        return 0, 0, []

    fixture_source = fixture_script.read_text(encoding="utf-8")
    target_functions = _extract_get_fn_calls(fixture_source)
    mutants = generate_mutants(source, target_functions=target_functions)

    killed = 0
    details: List[MutantResult] = []
    for i, (fn_name, mutant_tree) in enumerate(mutants, start=1):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, dir=str(REPO_ROOT / "tools"), encoding="utf-8"
        ) as tmp:
            tmp.write(ast.unparse(mutant_tree))
            mutant_path = Path(tmp.name)

        try:
            status, reason = run_fixture(fixture_script, mutant_path, pattern)
        finally:
            mutant_path.unlink(missing_ok=True)

        survived = status == "PASS"
        if not survived:
            killed += 1
        details.append(MutantResult(pattern, fn_name, i, survived, status, reason))
        if verbose:
            mark = "SURVIVED" if survived else "KILLED"
            print(f"  {pattern} :: {fn_name} [{i}] -> {mark} ({status})")

    return killed, len(mutants), details


def run_negative_control(verbose: bool = False) -> bool:
    """Run the permanently checked-in weak fixture.

    Returns True if the harness correctly flags a SURVIVED mutant (HOLLOW).
    This is the test-of-the-test: if HOLLOW detection were cosmetic or if
    mutants were not actually executed, this fixture would look SOLID.
    """
    oracle_path = REPO_ROOT / "tests" / "xmt_negative_control" / "oracle.py"
    fixture_script = REPO_ROOT / "tests" / "xmt_negative_control" / "weak_fixture.py"
    if not oracle_path.exists() or not fixture_script.exists():
        print("Negative-control files missing.", file=sys.stderr)
        return False

    source = oracle_path.read_text(encoding="utf-8")
    mutants = generate_mutants(source, target_functions=["answer"])
    if not mutants:
        print("No mutants generated for negative control.", file=sys.stderr)
        return False

    killed = 0
    details: List[MutantResult] = []
    for i, (fn_name, mutant_tree) in enumerate(mutants, start=1):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, dir=str(REPO_ROOT / "tools"), encoding="utf-8"
        ) as tmp:
            tmp.write(ast.unparse(mutant_tree))
            mutant_path = Path(tmp.name)

        try:
            status, reason = run_fixture(fixture_script, mutant_path, "xmt-negative-control")
        finally:
            mutant_path.unlink(missing_ok=True)

        survived = status == "PASS"
        if not survived:
            killed += 1
        details.append(MutantResult("xmt-negative-control", fn_name, i, survived, status, reason))
        if verbose:
            mark = "SURVIVED" if survived else "KILLED"
            print(f"  xmt-negative-control :: {fn_name} [{i}] -> {mark} ({status})")

    count = len(mutants)
    rate = 100.0 * killed / count if count else 0.0
    hollow = killed < count
    status = "HOLLOW" if hollow else "SOLID"
    print(f"\n{'xmt-negative-control':30} {killed:3}/{count:3} killed ({rate:5.1f}%)  [{status}]")
    if hollow:
        for r in details:
            if r.survived:
                print(f"    SURVIVOR: {r.function} -> {r.status} ({r.reason})")
        print("Negative control correctly detected HOLLOW behavior.")
    else:
        print("ERROR: negative control was not flagged HOLLOW — XMT detection may be broken.")
    return hollow


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Forge Gate eXtreme Mutation Testing (XMT) harness"
    )
    ap.add_argument(
        "--negative-control",
        action="store_true",
        help="run the permanently weak fixture and expect HOLLOW (test-of-the-test)",
    )
    args = ap.parse_args()

    if args.negative_control:
        print("Forge Gate eXtreme Mutation Testing (XMT) harness")
        print("=" * 60)
        print("Running permanently checked-in negative control...")
        return 0 if run_negative_control(verbose=True) else 1

    catalog = load_catalog()
    if not catalog:
        print("No patterns found in catalog.", file=sys.stderr)
        return 1

    print("Forge Gate eXtreme Mutation Testing (XMT) harness")
    print("=" * 60)

    total_killed = 0
    total_mutants = 0
    hollow_patterns: List[str] = []

    for pattern, meta in sorted(catalog.items()):
        killed, count, details = evaluate_pattern(pattern, meta, verbose=True)
        total_killed += killed
        total_mutants += count
        rate = 100.0 * killed / count if count else 0.0
        status = "HOLLOW" if killed < count else "SOLID"
        print(f"\n{pattern:30} {killed:3}/{count:3} killed ({rate:5.1f}%)  [{status}]")
        if killed < count:
            hollow_patterns.append(pattern)
            for r in details:
                if r.survived:
                    print(f"    SURVIVOR: {r.function} -> {r.status} ({r.reason})")

    print("=" * 60)
    if total_mutants:
        overall = 100.0 * total_killed / total_mutants
        print(f"Total: {total_killed}/{total_mutants} mutants killed ({overall:.1f}%)")
    if hollow_patterns:
        print(f"HOLLOW fixtures detected: {', '.join(hollow_patterns)}")
        return 1
    print("All fixtures are SOLID — every oracle-body-deletion mutant was killed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
