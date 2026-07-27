# zipf law fit

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(word_frequencies: List[int]) → float`

## What it does

Zipf's law: rank-frequency relationship in natural language.

log(frequency) ∝ log(rank) with slope ≈ −1. Core claim: natural text follows
Zipf; uniform text violates it. Fitted slope measured.

## Guarantee

When it runs, zipf law fit guarantees 0.5 < slope_natural < 2.0; slope_uniform < 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.5 < slope_natural < 2.0`
- `slope_uniform < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def fit_zipf(word_frequencies: List[int]) -> float:`
**Valid input:** `word_frequencies` is a list of non-negative integers; length ≥ 2.
**Core:** Fits Zipf's law by sorting frequencies in descending order and regressing log(frequency) against log(rank); returns the negative slope.
**Assert:** A Zipf-like distribution yields a slope between 0.5 and 2.0; a uniform distribution yields a slope near 0 (below 0.5).
**⚠️ Defect:** Zero frequencies are replaced with `log(0) = 0`, which distorts the regression for low-frequency or padded rank bins. The regression uses population covariance/variance rather than sample formulas, and it does not return any goodness-of-fit or intercept, only the slope.

---
*△ AURA Pattern Library — © Reality Optimizer*
