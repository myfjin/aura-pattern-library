# bayes diagnostic test

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(sensitivity: float, specificity: float, prevalence: float) → Tuple[float, float]`

## What it does

Bayes' theorem for diagnostic testing: sensitivity/specificity/prevalence → PPV/NPV.

Core idea: Positive Predictive Value (PPV) = P(disease | positive test) depends critically
on the base rate (prevalence). Even with high sensitivity/specificity, low prevalence causes
low PPV (most positives are false positives). Bayes' theorem links test performance to
clinical utility.

Use when: evaluating medical/diagnostic tests, understanding false positive rates, combining
multiple test results, assessing clinical decision thresholds.

## Guarantee

When it runs, bayes diagnostic test guarantees abs(ppv - expected_ppv) < 1e-09; abs(ppv_perfect - 1.0) < 1e-09; abs(npv_perfect - 1.0) < 1e-09 (proven by run).

**Checkable constraints:**

- `abs(ppv - expected_ppv) < 1e-09`
- `0.15 < ppv < 0.16`
- `ppv_high > 0.85`
- `ppv_high > ppv`
- `ppv_very_low < ppv`
- `ppv_very_low < 0.02`
- `npv_low_prev > 0.99`
- `ppv_high_sens > ppv_normal`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def bayes_diagnostic(sensitivity: float, specificity: float, prevalence: float) -> Tuple[float, float]:`
**Valid input:** `sensitivity`, `specificity`, `prevalence` are probabilities in [0, 1].
**Core:** Computes Positive Predictive Value (PPV) and Negative Predictive Value (NPV) from test sensitivity/specificity and disease prevalence using Bayes' theorem. Demonstrates that even highly accurate tests yield low PPV when prevalence is low.
**Assert:** At 1% prevalence, 90% sensitivity, 95% specificity, PPV ≈ 0.154; NPV > 0.99. Higher prevalence increases PPV; a perfect test gives PPV = NPV = 1.0.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
