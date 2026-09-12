"""
oracle.py — the 8-signal detection oracle (Layer 2) + 5S's honesty guardrails.
Judges a recipe's OUTPUT into a verdict signal. The recipe fires the attack;
this decides whether the result is a kill, a pass, or "I cannot tell".

The whole conscience (5S): the biggest risk is silently PASSing when it should FLAG.
"""
import math


def _is_finite_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)

def _has_nan(x):
    try:
        if isinstance(x, float): return math.isnan(x) or math.isinf(x)
        if isinstance(x, (list, tuple)): return any(_has_nan(v) for v in x)
    except TypeError:
        return False
    return False


def classify_signal(result):
    """The 8-signal table. result = {raised, error_text, output, clean_output,
    reached, names_bad_param, oracle_match}. Returns (signal, verdict_contribution)."""
    # row 1-2: an error was raised
    if result.get("raised"):
        txt = (result.get("error_text") or "")
        if result.get("names_bad_param"):
            return ("named_error", "PASS_signal")          # CONTRACT quality
        return ("cryptic_error", "PASS_signal_accidental")  # accidental catch, still caught

    out = result.get("output")

    # row 4: visible NaN/inf poison
    if _has_nan(out):
        return ("nan_output", "FLAG_signal")               # visible poison, not silent

    # guardrail: attack-reachability (5S proposal 2) — did the poison actually reach the code?
    if result.get("reached") is False:
        return ("attack_did_not_reach", "NO_JUDGMENT")     # exclude — prevents false-KILL

    # row 3: no error + output == clean-run output  -> fake-robust KILL (noise-identity)
    # round-2 B2 guard: only fire on MEANINGFUL output, never vacuous equality (None/empty).
    co = result.get("clean_output")
    if (co is not None and out is not None and out == co
            and (_is_finite_number(out) or (isinstance(out, (list, tuple, dict, str)) and len(out) > 0))):
        return ("output_identical_to_clean", "KILL_signal")

    # numeric-oracle mismatch -> wrong math
    if result.get("oracle_match") is False:
        return ("numeric_oracle_mismatch", "KILL_signal")

    # invariant broke on valid input
    if result.get("invariant_broken"):
        return ("invariant_broken", "KILL_or_FLAG_signal")

    # mutation coverage gap
    if result.get("mutation_unnoticed"):
        return ("mutation_coverage_gap", "FLAG_signal")

    # row 5: no error + confident plausible number  -> the hardest. silent-wrong SUSPECT.
    if _is_finite_number(out) or (isinstance(out, (list, tuple)) and out):
        # only a KILL if an oracle/invariant proved it wrong (handled above).
        # without that proof, this is NOT auto-pass -> it's suspicious-but-unproven.
        return ("confident_output_unproven", "NEEDS_ORACLE")

    return ("unclassified", "NEEDS_ORACLE")


def verdict_from_signals(signals, oracle_coverage, harness_ok, concurrency_ordering):
    """Combine per-recipe signals into a final verdict via the authority ladder + guardrails.

    oracle_coverage (5S #1): a PASS REQUIRES >=1 positive oracle (mechanical/semantic/numeric).
    harness_ok (5S #3): if the harness can't report success, cap at FLAG.
    concurrency_ordering (5S #8): if present, ordering is un-runnable -> cap at FLAG.
    """
    kills = [s for s in signals if s[1] in ("KILL_signal",)]
    kill_or_flag = [s for s in signals if s[1] == "KILL_or_FLAG_signal"]
    flags = [s for s in signals if s[1] in ("FLAG_signal",)]
    unproven = [s for s in signals if s[1] in ("NEEDS_ORACLE",)]

    card = {"signals": [s[0] for s in signals], "oracle_coverage": oracle_coverage}

    # hard KILL if any oracle/invariant proved wrong OR fake-robust identity
    if kills:
        card.update(verdict="INVALID", reason=kills[0][0], fix_available=None)
        return card

    # concurrency ordering cap (un-runnable boundary)
    if concurrency_ordering:
        card.update(verdict="FLAG", reason="ordering_unverified_by_execution",
                    note="third boundary: needs model-checker, not execution")
        return card

    # harness honesty gate
    if not harness_ok:
        card.update(verdict="FLAG", reason="harness_untrustworthy",
                    note="pattern ran but harness can't report success/failure")
        return card

    # oracle_coverage floor: no positive oracle => cannot claim PASS (4Q ticket 001 / 5S #1,#6)
    # 'mechanical' (recipes ran) is NOT positive verification -> only semantic/numeric/invariant.
    _has_pos = any(oracle_coverage.get(k) for k in ("semantic", "numeric", "invariant"))

    if kill_or_flag:
        card.update(verdict="FLAG", reason=kill_or_flag[0][0])
        return card

    # flags BEFORE unproven (2026-07-21 reporting fix): verdict is FLAG either way, but
    # "silent_domain_acceptance" is the actionable signal — it must not be shadowed by
    # the generic "confident_output_no_oracle".
    if flags:
        card.update(verdict="FLAG", reason="; ".join(sorted({s[0] for s in flags})))
        return card

    if unproven and not _has_pos:
        card.update(verdict="FLAG", reason="confident_output_no_oracle",
                    note="5S honest floor: cannot verify the number is right -> I cannot tell")
        return card

    # PASS only if a positive oracle backs it
    if _has_pos:
        card.update(verdict="PASS", reason="survived all applicable recipes with oracle backing")
    else:
        card.update(verdict="FLAG", reason="no_positive_oracle",
                    note="all recipes clean but nothing could positively verify correctness")
    return card


# --- FIX 2026-07-20 (4Q ticket 001 + 5S findings 1&6): coverage must be DERIVED not trusted ---
# "mechanical" (recipes ran) is NOT positive verification -> removed from the PASS-oracle set.
POSITIVE_ORACLES = ("semantic", "numeric", "invariant")

def has_positive_oracle(oracle_coverage):
    """A PASS requires a POSITIVE oracle. 'mechanical' = recipes-ran != verified (4Q/5S)."""
    return any(oracle_coverage.get(k) for k in POSITIVE_ORACLES)

def derive_coverage(signals, probe_result):
    """Derive coverage from ACTUAL signals + PROOF OF EXECUTION (5S/4Q round-2).
    A probe can no longer spoof coverage with a bare boolean — numeric needs a computed
    ground truth, invariant needs a real invariant signal. (Full elimination = v1.5 recipe
    wiring, where no human writes coverage at all.)"""
    sigs = {s[0] for s in signals}
    cov = {}
    # NUMERIC: requires proof the oracle actually ran AND a ground truth was computed
    # (round-2 A1: `oracle_match: True` presence is not enough).
    cov["numeric"] = (probe_result.get("oracle_run") is True
                      and probe_result.get("oracle_truth") is not None
                      and probe_result.get("oracle_match") is not None)
    # SEMANTIC: derived from ACTUAL signals only (already signal-derived — sound).
    cov["semantic"] = bool({"invariant_broken", "silent_wrong_on_invalid",
                            "output_identical_to_clean", "nan_output"} & sigs)
    # INVARIANT: requires a REAL invariant signal or a structured invariant_checks list,
    # NOT the `invariant_checked: True` boolean (round-2 A4 — same class as mechanical spoof).
    cov["invariant"] = ("invariant_broken" in sigs) or bool(probe_result.get("invariant_checks"))
    cov["mechanical"] = True  # evidence only; never a positive oracle (see POSITIVE_ORACLES)
    return cov
