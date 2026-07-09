"""
Bayes' theorem for diagnostic testing: sensitivity/specificity/prevalence → PPV/NPV.

Core idea: Positive Predictive Value (PPV) = P(disease | positive test) depends critically
on the base rate (prevalence). Even with high sensitivity/specificity, low prevalence causes
low PPV (most positives are false positives). Bayes' theorem links test performance to
clinical utility.

Use when: evaluating medical/diagnostic tests, understanding false positive rates, combining
multiple test results, assessing clinical decision thresholds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Tuple


def bayes_diagnostic(
    sensitivity: float,
    specificity: float,
    prevalence: float
) -> Tuple[float, float]:
    """
    Compute PPV and NPV from test characteristics.

    sensitivity = P(+ | disease) = true positive rate
    specificity = P(- | no disease) = true negative rate
    prevalence = P(disease) = base rate

    Returns: (PPV, NPV)
        PPV = P(disease | +) = positive predictive value
        NPV = P(no disease | -) = negative predictive value
    """
    # P(+ | disease) * P(disease)
    tp_prob = sensitivity * prevalence

    # P(+ | no disease) * P(no disease) = (1 - specificity) * (1 - prevalence)
    fp_prob = (1.0 - specificity) * (1.0 - prevalence)

    # P(+) = P(+ and disease) + P(+ and no disease)
    prob_positive = tp_prob + fp_prob

    # PPV = P(+ and disease) / P(+)
    ppv = tp_prob / prob_positive if prob_positive > 0 else 0.0

    # P(- | no disease) * P(no disease)
    tn_prob = specificity * (1.0 - prevalence)

    # P(- | disease) * P(disease) = (1 - sensitivity) * prevalence
    fn_prob = (1.0 - sensitivity) * prevalence

    # P(-) = P(- and no disease) + P(- and disease)
    prob_negative = tn_prob + fn_prob

    # NPV = P(- and no disease) / P(-)
    npv = tn_prob / prob_negative if prob_negative > 0 else 0.0

    return ppv, npv


if __name__ == "__main__":
    import random
    random.seed(42)

    # Test 1: Classic example — 1% prevalence, 90% sensitivity, 95% specificity
    # Hand calculation:
    # P(+) = 0.9 * 0.01 + 0.05 * 0.99 = 0.009 + 0.0495 = 0.0585
    # PPV = 0.009 / 0.0585 ≈ 0.1538 (~15.4%)
    sensitivity = 0.90
    specificity = 0.95
    prevalence = 0.01

    ppv, npv = bayes_diagnostic(sensitivity, specificity, prevalence)

    expected_ppv = 0.009 / (0.009 + 0.0495)  # Hand computation
    assert abs(ppv - expected_ppv) < 1e-9, f"PPV mismatch: {ppv} vs {expected_ppv}"
    assert 0.15 < ppv < 0.16, f"Classic example: PPV should be ~0.154, got {ppv}"

    # Test 2: High prevalence case (50%) should give high PPV even with moderate test quality
    prevalence_high = 0.50
    ppv_high, _ = bayes_diagnostic(sensitivity, specificity, prevalence_high)

    # With 50% base rate, PPV should be much higher
    assert ppv_high > 0.85, f"High prevalence should give high PPV, got {ppv_high}"
    assert ppv_high > ppv, f"Higher prevalence should increase PPV"

    # Test 3: Very low prevalence (0.1%) collapses PPV
    prevalence_very_low = 0.001
    ppv_very_low, _ = bayes_diagnostic(sensitivity, specificity, prevalence_very_low)

    assert ppv_very_low < ppv, f"Very low prevalence should decrease PPV"
    assert ppv_very_low < 0.02, f"Very low prevalence should give very low PPV, got {ppv_very_low}"

    # Test 4: NPV stays high even at low prevalence (most negatives are true negatives)
    _, npv_low_prev = bayes_diagnostic(sensitivity, specificity, 0.01)
    assert npv_low_prev > 0.99, f"NPV should be high at low prevalence, got {npv_low_prev}"

    # Test 5: Sensitivity vs specificity trade-off
    # Increase sensitivity (catch more disease), PPV increases
    ppv_high_sens, _ = bayes_diagnostic(0.99, specificity, 0.01)
    ppv_normal, _ = bayes_diagnostic(0.90, specificity, 0.01)
    assert ppv_high_sens > ppv_normal, "Higher sensitivity should increase PPV"

    # Test 6: Perfect test (100% sens, 100% spec) gives PPV = 1.0 at any prevalence
    ppv_perfect, npv_perfect = bayes_diagnostic(1.0, 1.0, 0.01)
    assert abs(ppv_perfect - 1.0) < 1e-9, f"Perfect test should give PPV=1.0, got {ppv_perfect}"
    assert abs(npv_perfect - 1.0) < 1e-9, f"Perfect test should give NPV=1.0, got {npv_perfect}"

    # Test 7: Useless test (50% sen, 50% spec) gives PPV ≈ prevalence
    ppv_useless, _ = bayes_diagnostic(0.5, 0.5, 0.01)
    # With 50% sen and 50% spec, the test is uninformative, so PPV should be close to prevalence
    assert abs(ppv_useless - 0.01) < 0.001, f"Useless test should give PPV ≈ prevalence"

    print("Bayes' theorem diagnostic test (PPV/NPV): all assertions PASS")
