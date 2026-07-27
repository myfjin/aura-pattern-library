# rare event option pricing

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(x: float) → float`

## What it does

Rare-Event Option Pricing — importance sampling where naive Monte Carlo goes blind.

CROSS-SPHERE COMPOSED PATTERN: black_scholes_monte_carlo (Econometrics & Finance)
x metropolis_hastings_mcmc / importance_sampling (Statistical Modeling) — embedding
bridge 0.532, found 2026-07-08. A deep out-of-the-money option's payoff almost
never triggers: naive MC with thousands of paths sees ~zero hits and prices it as
0 (or one wild outlier). Importance sampling SHIFTS the sampling drift toward the
payoff region and re-weights by the likelihood ratio — a thousand tilted paths
beat a million blind ones, verified against the Black-Scholes closed form (the
oracle this composition is judged by).

Human logic of the name: the payoff is a RARE EVENT; you price it by going to
where it lives instead of waiting for it to visit you.

## Guarantee

When it runs, rare event option pricing guarantees err_is < 0.1; err_naive > 3 * err_is; se / truth < 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `err_is < 0.1`
- `err_naive > 3 * err_is`
- `se / truth < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
