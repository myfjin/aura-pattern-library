# bayesian ab beta

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(successes_a: int, trials_a: int, successes_b: int, trials_b: int, prior_alpha: float, prior_beta: float, num_samples: int) → Tuple[float, float, float]`

## What it does

Bayesian A/B testing with Beta-Binomial posteriors.

Core idea: model each variant's success rate as Beta distribution, update
posterior with observed data (successes + failures), then estimate P(B > A)
via posterior sampling.

When to use: when you want a probabilistic answer to "is B better than A?" with
uncertainty quantification, especially for small sample sizes.

## Guarantee

When it runs, bayesian ab beta guarantees prob_b_better > 0.5; mean_b > mean_a; prob_b_better > 0.7 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `prob_b_better > 0.5`
- `mean_b > mean_a`
- `prob_b_better > 0.7`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def bayesian_ab_test(successes_a: int, trials_a: int, successes_b: int, trials_b: int, prior_alpha: float = 1.0, prior_beta: float = 1.0, num_samples: int = 10000,) -> Tuple[float, float, float]:`
**Valid input:** `0 <= successes_a <= trials_a`, `0 <= successes_b <= trials_b`; `trials_a`, `trials_b`, `num_samples` > 0; `prior_alpha`, `prior_beta` > 0.
**Core:** Bayesian A/B testing with Beta-Binomial posteriors. Updates Beta priors with observed successes/failures, then estimates `P(B > A)`, and posterior mean rates via sampling.
**Assert:** When B has higher observed rate (65/100 vs 60/100), `P(B > A) > 0.5`, posterior mean B > posterior mean A, and with the planted gap `P(B > A) > 0.7`.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
