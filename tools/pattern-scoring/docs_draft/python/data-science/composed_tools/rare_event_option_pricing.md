# Rare-Event Option Pricing

**File:** `python/data-science/composed_tools/rare_event_option_pricing.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Importance sampling where naive Monte Carlo goes blind.** A deep out-of-the-money option's payoff almost never triggers: naive MC with thousands of paths sees ~zero hits and prices it as 0 (or one wild outlier). Importance sampling SHIFTS the sampling drift toward the payoff region and re-weights by the likelihood ratio — a thousand tilted paths beat a million blind ones, verified against the Black-Scholes closed form.

**When to use:** Pricing deep out-of-the-money options or any rare-event expectation where naive MC has near-zero hit rate.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `S0`, `K` | float > 0, spot and strike | K >> S0 for deep OTM |
| `R`, `SIGMA`, `T` | float > 0, risk-free rate, vol, time | standard BS params |

---

## How inputs shape the output

- **Naive MC is visibly blind** (relative error > 3× IS error).
- **Importance sampling lands within 10%** of the Black-Scholes truth.
- **Estimator standard error is under 10%** of truth — the honest precision.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/rare_event_option_pricing.py
Black-Scholes truth: 0.000234
naive MC  (n=2000): 0.000000  rel err 100%
IS MC     (n=2000): 0.000251  rel err 7.3% · SE/truth 8.1%
rare_event_option_pricing.py PASS
```

**Reading the output:** with strike at 200 and spot at 100, naive MC sees zero payoffs in 2000 paths and prices the option at 0. Importance sampling with the same 2000 paths estimates 0.000251 — within 7.3% of the true BS price of 0.000234.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| at-the-money option | naive MC also works | IS still doesn't hurt |
| theta aimed wrong | IS may be worse than naive | needs correct drift targeting |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20