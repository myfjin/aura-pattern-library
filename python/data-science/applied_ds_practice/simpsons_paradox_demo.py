"""
Simpson's Paradox: aggregate trend reverses within strata.

An association between two variables at the aggregate level reverses direction
when data is split by a confounding variable (stratum). Classic example:
treatment A beats B overall, but B beats A within every subgroup.

Use: causal inference, detecting confounding, interpreting correlations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from collections import defaultdict


def compute_rate(numerator: int, denominator: int) -> float:
    """Compute success rate."""
    return numerator / denominator if denominator > 0 else 0


if __name__ == "__main__":
    # Simpson's Paradox:
    # B beats A in EVERY stratum, but A beats B in AGGREGATE.
    # Key: A applied mostly to easy stratum, B mostly to hard stratum.
    # Within each stratum B is better, but hard stratum (B's majority)
    # has lower base rates, so B's overall rate is pulled down.

    # Stratum 1 (EASY cases, 80% base success):
    # A: 800/1000 applied here = 80%
    # B: 100/1000 applied here = 90%
    # B clearly better within stratum 1
    stratum1_a_successes = 800
    stratum1_a_total = 1000
    stratum1_b_successes = 90
    stratum1_b_total = 100

    # Stratum 2 (HARD cases, 10% base success):
    # A: 100/1100 applied here = 10%
    # B: 1000/1100 applied here = 12%
    # B slightly better within stratum 2, but both low
    stratum2_a_successes = 10
    stratum2_a_total = 100
    stratum2_b_successes = 120
    stratum2_b_total = 1000

    print("Simpson's Paradox Demonstration")
    print()

    # Compute stratified rates
    print("STRATIFIED (within each group):")
    print()

    rate_a_s1 = compute_rate(stratum1_a_successes, stratum1_a_total)
    rate_b_s1 = compute_rate(stratum1_b_successes, stratum1_b_total)

    print(f"Stratum 1 (easy cases, 80% baseline success):")
    print(f"  Treatment A: {stratum1_a_successes}/{stratum1_a_total} = {rate_a_s1:.1%}")
    print(f"  Treatment B: {stratum1_b_successes}/{stratum1_b_total} = {rate_b_s1:.1%}")
    print(f"  Winner within stratum 1: {'B' if rate_b_s1 > rate_a_s1 else 'A'}")
    print()

    rate_a_s2 = compute_rate(stratum2_a_successes, stratum2_a_total)
    rate_b_s2 = compute_rate(stratum2_b_successes, stratum2_b_total)

    print(f"Stratum 2 (hard cases, 10% baseline success):")
    print(f"  Treatment A: {stratum2_a_successes}/{stratum2_a_total} = {rate_a_s2:.1%}")
    print(f"  Treatment B: {stratum2_b_successes}/{stratum2_b_total} = {rate_b_s2:.1%}")
    print(f"  Winner within stratum 2: {'B' if rate_b_s2 > rate_a_s2 else 'A'}")
    print()

    # Compute aggregate rate
    print("AGGREGATE (ignoring strata):")
    print()

    agg_a_successes = stratum1_a_successes + stratum2_a_successes
    agg_a_total = stratum1_a_total + stratum2_a_total
    agg_b_successes = stratum1_b_successes + stratum2_b_successes
    agg_b_total = stratum1_b_total + stratum2_b_total

    rate_a_agg = compute_rate(agg_a_successes, agg_a_total)
    rate_b_agg = compute_rate(agg_b_successes, agg_b_total)

    print(f"  Treatment A: {agg_a_successes}/{agg_a_total} = {rate_a_agg:.1%}")
    print(f"  Treatment B: {agg_b_successes}/{agg_b_total} = {rate_b_agg:.1%}")
    print(f"  Winner in aggregate: {'B' if rate_b_agg > rate_a_agg else 'A'}")
    print()

    # Detect paradox
    print("PARADOX DETECTION:")
    print()

    # Check if B beats A within each stratum
    b_wins_s1 = rate_b_s1 > rate_a_s1
    b_wins_s2 = rate_b_s2 > rate_a_s2
    b_wins_aggregate = rate_b_agg > rate_a_agg

    print(f"  B wins stratum 1: {b_wins_s1}")
    print(f"  B wins stratum 2: {b_wins_s2}")
    print(f"  B wins aggregate: {b_wins_aggregate}")
    print()

    # The paradox: B wins in both strata but loses in aggregate (or vice versa)
    paradox_detected = (b_wins_s1 and b_wins_s2 and not b_wins_aggregate) or \
                       (not b_wins_s1 and not b_wins_s2 and b_wins_aggregate)

    if paradox_detected:
        print("✓ SIMPSON'S PARADOX DETECTED!")
        print()
        if b_wins_s1 and b_wins_s2 and not b_wins_aggregate:
            print("  B beats A in EVERY stratum, but A beats B in AGGREGATE.")
            print(f"  Cause: A concentrated on easy cases; B on hard cases.")
            print(f"        Easy base rate (80%) >> hard base rate (10%).")
    else:
        print("✗ No paradox detected.")

    print()

    # Quantitative assertions
    assert b_wins_s1, f"B should win stratum 1: {rate_b_s1:.1%} > {rate_a_s1:.1%}"
    assert b_wins_s2, f"B should win stratum 2: {rate_b_s2:.1%} > {rate_a_s2:.1%}"
    assert not b_wins_aggregate, \
        f"A should win aggregate: {rate_a_agg:.1%} > {rate_b_agg:.1%}"
    assert paradox_detected, "Simpson's Paradox should be detected"

    print("Assertions: all paradox conditions verified ✓")

    print("\nsimpsons_paradox_demo.py PASS")
