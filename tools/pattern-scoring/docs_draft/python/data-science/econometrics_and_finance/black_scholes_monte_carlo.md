# Black-Scholes Monte Carlo Option Pricing

**File:** `python/data-science/econometrics_and_finance/black_scholes_monte_carlo.py`
**Sphere:** Data Science — Econometrics and Finance

---

## What it solves

**What's a fair price for this option?** The Black-Scholes formula gives the closed-form price for a European call option. Monte Carlo simulation estimates the same price by simulating thousands of possible price paths. This pattern compares both: the MC price should fall within ~3 standard errors of the closed-form price, proving that simulation can price options when the closed form doesn't exist (e.g. exotic options).

**When to use:** You need to price a European option and want to understand the relationship between the closed-form solution and simulation. Or you need a Monte Carlo baseline for pricing options where no closed form exists.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `S` (spot price) | > 0 | negative → nonsensical |
| `K` (strike) | > 0 | — |
| `T` (time to expiry) | > 0 | — |
| `r` (risk-free rate) | float, typically 0.01–0.10 | — |
| `sigma` (volatility) | > 0 | 0 → option worth exactly intrinsic |
| `num_sim` | > 0, larger = tighter CI | small → wide confidence interval |

---

## How inputs shape the output

- **More simulations tighten the confidence interval:** the standard error shrinks as 1/√n. 10,000 simulations give ~2% relative error on a ~10 option.
- **At-the-money options (S≈K)** have the most uncertainty — the payoff is binary near the strike. Deep ITM/OTM options converge faster.
- **Volatility is the price driver:** higher σ → higher option price (more chance of large moves). The MC and BS prices should agree at any σ.

---

## Worked example (real run)

```
$ python3 python/data-science/econometrics_and_finance/black_scholes_monte_carlo.py
PASS
```

**Reading the output:** a bare PASS means the MC price was within 3×SE of the BS price. For S=100, K=100, T=1, r=0.05, σ=0.2, the BS price is ~10.45; MC with 10k sims should be within ~0.60 of that.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `num_sim = 0` | ZeroDivision | needs guard |
| `sigma = 0` | option = max(S-K, 0) | correct but edge case |
| very few simulations | wide CI, assert may fail | expected behavior |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
