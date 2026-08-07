#!/usr/bin/env python3
"""Mutation ruler for python patterns.

Mutate numeric literals inside each registry entry function two ways:
  ZERO   -> 0
  DOUBLE -> value * 2
Run the pattern's own self-test and classify:
  KILLED        failed AND stderr contains AssertionError
  SURVIVED      exited 0
  CRASHED       failed but NO AssertionError in stderr
  INCONCLUSIVE  nothing to mutate, unmutated file does not pass, or the mutated
                  source is byte-identical to the original (all literals were zero)

A mutant whose SOURCE TEXT is identical to the original is a no-op mutant and is
reported INCONCLUSIVE, never SURVIVED.
"""

import argparse
import ast
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
from pathlib import Path


def numeric_literals_in_function(tree, func_name):
    """Return list of (lineno, col_offset, value) for int/float constants inside func."""
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == func_name:
            for n in ast.walk(node):
                if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                    # Avoid bool (which is a subclass of int in Python)
                    if isinstance(n.value, bool):
                        continue
                    targets.append((n.lineno, n.col_offset, n.value))
    return targets


def mutate_source(source, func_name, mode):
    """Return mutated source string. mode is 'zero' or 'double'."""
    tree = ast.parse(source)
    targets = numeric_literals_in_function(tree, func_name)
    if not targets:
        return None, []

    lines = source.splitlines(keepends=True)
    # Process in reverse order by position so offsets stay valid.
    targets_sorted = sorted(targets, key=lambda t: (t[0], t[1]), reverse=True)
    mutated_count = 0
    for lineno, col_offset, value in targets_sorted:
        line_idx = lineno - 1
        line = lines[line_idx]
        # Find the actual literal text at this position; ast col_offset is UTF-8 chars but
        # line split preserves them. We'll search forward for the literal.
        rest = line[col_offset:]
        # Match the literal as text (int or float, possibly negative? literals are not negated)
        m = re.match(r'(\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', rest)
        if not m:
            # Try matching with leading sign? ast parses -1.0 as UnaryOp, so skip.
            continue
        lit_text = m.group(0)
        end = col_offset + len(lit_text)
        if mode == 'zero':
            replacement = '0'
        else:  # double
            # Use repr to preserve float/int distinction
            new_val = value * 2
            replacement = repr(new_val)
        line = line[:col_offset] + replacement + line[end:]
        lines[line_idx] = line
        mutated_count += 1
    return ''.join(lines), mutated_count


def run_python_file(path, timeout=60):
    """Run python3 path and return (rc, stdout, stderr, timed_out).

    ⛔ NEVER `subprocess.run(..., timeout=)` HERE. That kills only the DIRECT child, so a
    pattern that spawns its own worker (multiprocessing, a concurrency pattern, anything
    that shells out) leaves the grandchild spinning at 100% CPU after the ruler moves on.
    Measured against a fixture built to orphan on purpose: the old semantics left the
    grandchild RUNNING, these semantics reaped it. Same discipline as guard_lens.py.

    ⭐ A TIMEOUT IS A VERDICT, NOT AN EXCEPTION. The old code let TimeoutExpired propagate
    out of the sweep, so one hanging pattern aborted the whole run and — because the TSV is
    flushed per row — left a truncated file with NO row for the pattern that hung. A reader
    counts the missing rows as nothing at all. Absence must never default to pass, so the
    caller turns `timed_out` into INCONCLUSIVE.
    """
    p = subprocess.Popen(
        [sys.executable, str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,          # its own process group, so killpg can reach the tree
    )
    try:
        out, err = p.communicate(timeout=timeout)
        return p.returncode, out, err, False
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
        out, err = p.communicate()
        return None, out, err, True


def mutate_and_test(src_path, func_name, work_dir):
    original_path = work_dir / src_path.name
    shutil.copy(src_path, original_path)
    original_source = src_path.read_text()
    rc0, out0, err0, to0 = run_python_file(original_path)
    if to0:
        reason = 'unmutated timed out — cannot measure this pattern'
        return [(func_name, m, 'INCONCLUSIVE', reason) for m in ('ZERO', 'DOUBLE')]
    if rc0 != 0:
        return [
            (func_name, 'ZERO', 'INCONCLUSIVE', f'unmutated failed rc={rc0}'),
            (func_name, 'DOUBLE', 'INCONCLUSIVE', f'unmutated failed rc={rc0}'),
        ]

    results = []
    for mode in ('ZERO', 'DOUBLE'):
        mutant_src, mutated_count = mutate_source(original_source, func_name, mode.lower())
        if mutant_src is None:
            results.append((func_name, mode, 'INCONCLUSIVE', 'no numeric literals in entry function'))
            continue
        if mutant_src == original_source:
            results.append((func_name, mode, 'INCONCLUSIVE', 'mutant source identical to original (all literals were zero)'))
            continue
        mutant_path = work_dir / f'{src_path.stem}_{mode.lower()}{src_path.suffix}'
        mutant_path.write_text(mutant_src)
        rc, out, err, timed_out = run_python_file(mutant_path)
        detail = f'mutated {mutated_count} literal(s)'
        if timed_out:
            # A mutant that hangs was NOT detected by the assert and did NOT survive —
            # it could not be measured. Never let that read as either.
            results.append((func_name, mode, 'INCONCLUSIVE',
                            detail + '; mutant timed out — could not measure'))
            continue
        if rc == 0:
            outcome = 'SURVIVED'
            detail += '; exited 0'
        elif 'AssertionError' in err:
            outcome = 'KILLED'
            detail += '; AssertionError in stderr'
        else:
            outcome = 'CRASHED'
            # Escape newlines in stderr so the TSV stays single-line.
            safe_err = err.replace('\n', '\\n').replace('\t', ' ')[:200]
            detail += f'; failed without AssertionError (stderr: {safe_err})'
        results.append((func_name, mode, outcome, detail))
    return results


def main():
    parser = argparse.ArgumentParser(description='Mutation ruler for python patterns')
    parser.add_argument('--patterns', required=True, help='directory containing pattern .py files')
    parser.add_argument('--registry', required=True, help='registry.jsonl path')
    parser.add_argument('--out', required=True, help='results TSV; scratch is created beside it')
    args = parser.parse_args()

    patterns_dir = Path(args.patterns)
    scratch_root = Path(args.out).resolve().parent   # portable: no machine hardcoded
    scratch_root.mkdir(parents=True, exist_ok=True)
    with open(args.registry) as f:
        registries = [json.loads(line) for line in f if line.strip()]

    with open(args.out, 'w') as outfh:
        outfh.write('pattern\tfunction\tmutant\toutcome\tdetail\n')
        outfh.flush()
        for reg in registries:
            pattern_id = reg['id']
            src_path = patterns_dir / f'{pattern_id}.py'
            if not src_path.exists():
                for fn in reg.get('entry_fns', []):
                    outfh.write(f'{pattern_id}\t{fn["name"]}\tZERO\tINCONCLUSIVE\tmissing file\n')
                    outfh.write(f'{pattern_id}\t{fn["name"]}\tDOUBLE\tINCONCLUSIVE\tmissing file\n')
                    outfh.flush()
                continue
            # Drivable entry functions only
            for fn_info in reg.get('entry_fns', []):
                if not fn_info.get('drivable'):
                    continue
                func_name = fn_info['name']
                # Scratch lives beside the OUTPUT, not on any one machine. The original hardcoded
                # dir='/home/au/ai-lab/mutation-kit', so the tool ran only on .8 — while the
                # canonical library is on the Mac, the one place it actually needs to work. The
                # "never /tmp" rule that produced that hardcode is about AGENT ARTIFACTS
                # PERSISTING, not ephemeral scratch: this dir is created and destroyed inside a
                # single call and holds no result.
                with tempfile.TemporaryDirectory(prefix=f'mut_{pattern_id}_', dir=scratch_root) as tmp:
                    tmp_path = Path(tmp)
                    results = mutate_and_test(src_path, func_name, tmp_path)
                    for fn, mode, outcome, detail in results:
                        outfh.write(f'{pattern_id}\t{fn}\t{mode}\t{outcome}\t{detail}\n')
                        outfh.flush()
    print(f'Wrote {args.out}')


if __name__ == '__main__':
    main()
