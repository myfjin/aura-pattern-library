#!/usr/bin/env python3
"""
Testbed driver for the pattern-scoring mechanism.

Runs each planted pattern through utility_score.py --abuse, compares the
mechanism's status to the oracle's known-answer verdict, and reports the
mechanism's own error rate: false-pass and false-reject.

Rule: the driver only feeds inputs. The planted oracle is the judge.
"""

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PATTERNS_DIR = ROOT / "patterns"
ORACLE_PATH = ROOT / "oracle.json"
SCORE_SCRIPT = ROOT.parent / "utility_score.py"
RESULTS_PATH = ROOT / "results" / "run.json"


def run_score(pattern_path: Path) -> dict:
    cmd = [sys.executable, str(SCORE_SCRIPT), str(pattern_path), "--abuse", "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if proc.returncode != 0:
        return {
            "file": pattern_path.name,
            "status": "driver_error",
            "error": proc.stderr,
            "raw_stdout": proc.stdout,
        }
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {
            "file": pattern_path.name,
            "status": "driver_error",
            "error": f"JSON decode: {e}",
            "raw_stdout": proc.stdout,
            "raw_stderr": proc.stderr,
        }


def main() -> int:
    oracle = json.loads(ORACLE_PATH.read_text(encoding="utf-8"))
    accept_statuses = set(oracle["accept_statuses"])
    reject_statuses = set(oracle["reject_statuses"])
    expected = {entry["file"]: entry for entry in oracle["patterns"]}

    results: list[dict] = []
    false_pass: list[dict] = []
    false_reject: list[dict] = []
    driver_errors: list[dict] = []
    correct = 0
    total = len(expected)

    print(f"Running mechanism on {total} planted patterns...")
    print(f"Score script: {SCORE_SCRIPT}")
    print("=" * 80)

    for entry in oracle["patterns"]:
        name = entry["file"]
        path = PATTERNS_DIR / name
        actual = run_score(path)
        actual_status = actual.get("status", "unknown")
        actual_accept = actual_status in accept_statuses
        actual_reject = actual_status in reject_statuses
        expected_verdict = entry["verdict"]

        record = {
            "file": name,
            "expected": expected_verdict,
            "actual_status": actual_status,
            "U": actual.get("U"),
            "flags": actual.get("flags", []),
            "failing_column": (actual.get("evidence_card") or {}).get("failing_column"),
            "match": False,
        }

        if expected_verdict == "ACCEPT":
            if actual_accept:
                record["match"] = True
                correct += 1
                print(f"[OK ] {name:<35} ACCEPT (status={actual_status}, U={actual.get('U')})")
            elif actual_reject:
                false_reject.append(record)
                print(f"[FR ] {name:<35} expected ACCEPT, got {actual_status} (U={actual.get('U')}, flags={actual.get('flags')})")
            else:
                driver_errors.append(record)
                print(f"[ERR] {name:<35} expected ACCEPT, unclassifiable status {actual_status}")
        else:  # REJECT
            if actual_reject:
                record["match"] = True
                correct += 1
                print(f"[OK ] {name:<35} REJECT (status={actual_status})")
            elif actual_accept:
                false_pass.append(record)
                print(f"[FP ] {name:<35} expected REJECT, got {actual_status} (U={actual.get('U')})")
            else:
                driver_errors.append(record)
                print(f"[ERR] {name:<35} expected REJECT, unclassifiable status {actual_status}")

        results.append(record)

    accuracy = correct / total if total else 0.0
    false_pass_rate = len(false_pass) / total if total else 0.0
    false_reject_rate = len(false_reject) / total if total else 0.0
    error_rate = (len(false_pass) + len(false_reject)) / total if total else 0.0

    summary = {
        "total": total,
        "correct": correct,
        "accuracy": round(accuracy, 4),
        "false_pass_count": len(false_pass),
        "false_reject_count": len(false_reject),
        "false_pass_rate": round(false_pass_rate, 4),
        "false_reject_rate": round(false_reject_rate, 4),
        "mechanism_error_rate": round(error_rate, 4),
        "driver_errors": len(driver_errors),
        "details": results,
        "false_passes": false_pass,
        "false_rejects": false_reject,
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=" * 80)
    print(f"Mechanism accuracy : {correct}/{total} = {accuracy:.2%}")
    print(f"False-pass rate    : {false_pass_rate:.2%} ({len(false_pass)} cases)")
    print(f"False-reject rate  : {false_reject_rate:.2%} ({len(false_reject)} cases)")
    print(f"Mechanism error rate: {error_rate:.2%}")
    if driver_errors:
        print(f"Driver/unclassifiable statuses: {len(driver_errors)}")
    print(f"Full results written to: {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
