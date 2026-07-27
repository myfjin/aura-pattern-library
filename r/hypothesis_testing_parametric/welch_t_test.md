# welch t test

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

Welch's t-test (unequal variance)
Implements t statistic, df (Welch-Satterthwaite), p-value; verifies against t.test()
Use when: comparing means of two groups with unequal variance

## Guarantee

When it runs, welch t test guarantees all.equal(t_stat, as.numeric(t_oracle$statistic), tolerance = 1e-08); all.equal(p_val, t_oracle$p.value, tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(t_stat, as.numeric(t_oracle$statistic), tolerance = 1e-08)`
- `all.equal(p_val, t_oracle$p.value, tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x1` and `x2` representing independent samples.
**Core:** Computes the Welch-Satterthwaite t-statistic, approximate degrees of freedom, and two-tailed p-value, then verifies against `t.test()`.
**Assert:** Manual t-statistic and p-value match `t.test()` within `1e-8`.
**⚠️ Defect:** No input validation: empty vectors, one-element vectors, or constant/zero-variance groups make the denominator zero or produce `NaN`/`Inf`; non-numeric inputs error uncontrolled. Hardcoded two-tailed alternative. No function wrapper.

---

**R-sphere batch 2: 7/7 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/hypothesis_testing_parametric/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/hypothesis_testing_parametric/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.

---
*△ AURA Pattern Library — © Reality Optimizer*
