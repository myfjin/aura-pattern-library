# PATTERN SHEET — bayesian_ab_beta
`python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py`
**Status: ❌ INVALID as shipped (Illia's audit, 2026-07-19) — fake-robust on impossible data.
Fix proven in `playground/retrofit_demo/bayesian_ab_beta_RETROFIT.py`, queued for gated ingest.**

## What it solves
You ran an A/B experiment (e.g. two page designs): A converted 60/100, B converted 65/100.
Is B *really* better, or is that luck? This computes **P(B > A)** — the probability that B's true
rate beats A's — using Beta posteriors, plus the posterior mean rate of each variant.

## Valid inputs (the contract — enforced only in the retrofit)
| Input | Domain | Violating it → |
|---|---|---|
| `successes_*` | integer, 0 ≤ successes ≤ trials | AURA-E004 (impossible data) |
| `trials_*` | integer > 0 | AURA-E005 (no experiment ran) |
| `prior_alpha`, `prior_beta` | > 0 | (B5) |
| non-numeric (e.g. `"шістдесят п'ять"`) | rejected | AURA-E-B1 |

## How inputs shape the output
- **The gap `successes/trials` between A and B drives P(B>A)**: bigger gap → closer to 1.0 (or 0.0).
- **Trial counts are the confidence knob**: 65/100 vs 60/100 gives P(B>A)≈0.76 — suggestive, not
  conclusive; the same rates at 650/1000 vs 600/1000 would push far closer to 1. Small trials →
  wide posteriors → P(B>A) hugs 0.5.
- **Priors** (default Beta(1,1) = uniform) act like phantom prior observations; raising
  `prior_alpha/beta` shrinks estimates toward the prior mean — matters only when trials are few.
- **Asymmetric trials are fine** (10 vs 1000 is valid data) — but the small side dominates the
  uncertainty. What is NEVER fine: successes > trials, or zero/negative trials — see failure modes.

## Worked example (real run)
```
$ python3 python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py
bayesian_ab_beta.py: P(B>A)=0.759, means A=0.598 B=0.647 PASS
```
**Reading the output:** given 60/100 vs 65/100, there's a **75.9% probability B is truly better** —
promising but under the conventional 95% decision bar: keep the test running. The means (0.598,
0.647) are posterior estimates of each true rate, slightly shrunk toward 0.5 by the uniform prior.

## Failure modes (audited by hand — this pattern's audit found the library's first fake-robust)
| Trigger | As shipped | Retrofit |
|---|---|---|
| 65 successes / 10 trials | **silent `PASS, P(B>A)=1.000`** — negative Beta param, sampler saturates | AURA-E004 raised |
| 65 successes / 0 trials | **silent `PASS, mean B=1.000`** — confident fiction from no data | AURA-E005 raised |
| `"шістдесят п'ять"` as successes | TypeError only by luck deeper in math | AURA-E-B1, named |
| several bad inputs at once | first crash wins, misattributed | ALL faults listed in one error |
| valid data where A wins (6/10 vs 5/10) | demo asserts fail — **not a pattern bug**: the `__main__` is a proof harness with planted data | teach: call the function, don't repurpose the harness |

## Provenance
Machine-VERIFIED (frozen ruler) · description cross-model reviewed 2026-07-18 ·
**Illia's audit 2026-07-19: 12 hand-run attacks → 2 silent-wrong → ❌ INVALID; retrofit designed,
proven against all his attacks same day** · evidence: `output/manual_audit_2026-07-19.csv` ·
errors: AURA-E004, E005 in `ERROR_CATALOG.md`
