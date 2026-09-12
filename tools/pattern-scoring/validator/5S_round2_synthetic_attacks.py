"""5S Round 2: synthetic probes to prove the two remaining spoofing vectors.

Run: cd validator && python3 5S_round2_synthetic_attacks.py
"""
import validate
import probes


def make_probe(overrides):
    base = {
        "raised": False,
        "output": 42.0,
        "reached": True,
        "error_text": None,
        "names_bad_param": False,
        "oracle_match": None,
        "invariant_broken": False,
        "mutation_unnoticed": False,
        "invariant_checked": False,
        "detail": "synthetic round-2 attack",
    }
    base.update(overrides)
    return lambda: base


def run_case(name, expected, overrides):
    fake_file = f"test/{name}.py"
    probes.PROBES[fake_file] = make_probe(overrides)
    exam = validate.load_exam()
    exam["expansion"].append({
        "file": fake_file,
        "verdict": expected,
        "ruling": "illia-pending",
        "lean": expected,
        "note": "synthetic round-2 probe",
    })
    results, correct, graded = validate.grade(exam)
    for f, exp, got, mark in results:
        if f == fake_file:
            status = "LIE" if got != expected else "honest"
            print(f"[{status:6}] {name:35} expected={expected:8} got={got:8}")
            return got


print("=" * 78)
print("5S ROUND 2 SYNTHETIC ATTACKS ON v1.1")
print("=" * 78)

# A1: numeric spoof
run_case("numeric_spoof_oracle_match_true", "FLAG",
         {"oracle_match": True})

# A4: invariant_checked spoof
run_case("invariant_checked_spoof", "FLAG",
         {"invariant_checked": True})

# B2: vacuous clean_output equality
run_case("vacuous_clean_output_none", "FLAG",
         {"clean_output": None, "output": None})

# C2: hand-tuned semantic pass vs recipe-driven would FLAG
run_case("hand_tuned_semantic_pass", "FLAG",
         {"invariant_checked": True, "detail": "hand-tuned semantic flag set"})

# Control: truly no oracle -> should FLAG honestly
run_case("honest_no_oracle", "FLAG", {})

print("=" * 78)
