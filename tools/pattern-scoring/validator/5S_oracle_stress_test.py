"""5S stress test of oracle.py guardrails — synthetic signals, no real patterns.

Goal: exercise the 8-signal oracle and 5S honesty guardrails directly,
without needing executable probes. Finds where the oracle itself lies.
"""
from oracle import classify_signal, verdict_from_signals


def test(name, result, coverage, harness_ok=True, concurrency=False):
    sig = classify_signal(result)
    signals = [sig]
    # mirror validate.py's extra-signal injection
    if result.get("confident_impossible") or result.get("nan_absorbed_silently"):
        signals.append(("silent_wrong_on_invalid", "KILL_signal"))
    if result.get("oracle_match") is False:
        signals.append(("numeric_oracle_mismatch", "KILL_signal"))
    card = verdict_from_signals(signals, coverage, harness_ok=harness_ok,
                                concurrency_ordering=concurrency)
    print(f"{name:45} -> {card['verdict']:8} ({card.get('reason','')})")
    return card


print("=" * 78)
print("5S ORACLE STRESS TEST — synthetic signals")
print("=" * 78)

# Front 1: false-PASS hunt
print("\n-- Front 1: false-PASS hunt --")
# Clean output, no oracle -> should FLAG (honest)
test("clean_output_no_oracle",
     {"raised": False, "output": 3.14, "reached": True}, {})

# Clean output, fake mechanical coverage -> PASS (this is the risk vector)
test("clean_output_fake_mechanical",
     {"raised": False, "output": 3.14, "reached": True}, {"mechanical": True})

# Clean output, fake semantic coverage -> PASS (risk vector)
test("clean_output_fake_semantic",
     {"raised": False, "output": 3.14, "reached": True}, {"semantic": True})

# Numeric oracle mismatch -> INVALID (correct)
test("numeric_oracle_mismatch",
     {"raised": False, "output": 1.24, "reached": True, "oracle_match": False},
     {"numeric": True})

# Invariant broken -> INVALID/FLAG (correct)
test("invariant_broken",
     {"raised": False, "output": 0.6, "reached": True, "invariant_broken": True},
     {"semantic": True})

# Mutation coverage gap -> FLAG
test("mutation_gap",
     {"raised": False, "output": 0.0, "reached": True, "mutation_unnoticed": True},
     {"mechanical": True})

# Front 2: false-KILL / attack reachability
print("\n-- Front 2: attack-reachability --")
# Attack did not reach -> NO_JUDGMENT, then no oracle -> FLAG (not KILL)
test("attack_never_reached",
     {"raised": False, "output": 3.14, "reached": False}, {})

# Attack reached + output == clean -> KILL (fake-robust)
test("attack_reached_identical",
     {"raised": False, "output": 3.14, "reached": True, "clean_output": 3.14},
     {"semantic": True})

# Attack did not reach BUT clean_output equal -> classify_signal hits reachability first
# so returns NO_JUDGMENT; validate.py doesn't inject KILL from clean_output in this case.
test("attack_not_reached_but_equal_clean",
     {"raised": False, "output": 3.14, "reached": False, "clean_output": 3.14},
     {})

# Front 3: boundary honesty
print("\n-- Front 3: boundary honesty --")
# Concurrency pattern with clean output and mechanical coverage -> should FLAG (ordering cap)
test("concurrency_clean_with_mechanical",
     {"raised": False, "output": 42, "reached": True},
     {"mechanical": True}, concurrency=True)

# Concurrency pattern with real KILL -> INVALID (real bug overrides ordering cap?)
test("concurrency_with_kill_signal",
     {"raised": False, "output": 1.24, "reached": True, "oracle_match": False},
     {"numeric": True}, concurrency=True)

# Untrustworthy harness -> FLAG even with positive oracle
test("harness_untrustworthy",
     {"raised": False, "output": 42, "reached": True},
     {"mechanical": True}, harness_ok=False)

# NaN output visible -> FLAG
test("nan_output_visible",
     {"raised": False, "output": float("nan"), "reached": True}, {})

# Named error -> PASS
test("named_contract_error",
     {"raised": True, "error_text": "ValueError: alpha must be in (0,1)",
      "names_bad_param": True}, {"mechanical": True})

print("=" * 78)
