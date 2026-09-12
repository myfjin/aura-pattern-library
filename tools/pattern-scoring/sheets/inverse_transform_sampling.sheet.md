# PATTERN SHEET — inverse_transform_sampling
`python/data-science/information_theory_and_probability/inverse_transform_sampling.py`
**Status: ❌-lean / ILLIA-TO-RULE (audit 2026-07-20) — the `u` contract is the best-quality guard
in the library, but the neighboring `rate` parameter is unguarded and returns silent negative
(impossible) waiting times. One-line fix, queue #13.**

## What it solves
"How do I generate random numbers from ANY distribution, given only a uniform random generator?"
The universal trick: take a uniform u in (0,1), run it through the distribution's inverse CDF, and
out comes a sample from that distribution. This is how `random.expovariate` and friends work under
the hood — turn plain uniform randomness into exponential, or any custom shape.

## How to drive it
```python
u = random.random()                      # uniform in (0,1)
x = exponential_inverse_cdf(u, rate=2.0) # → a sample from Exponential(rate=2)
# many samples → their mean ≈ 1/rate, variance ≈ 1/rate²  (the demo checks exactly this)
```

## Valid inputs — a study in one good guard and one missing one
| Input | Domain | Today → |
|---|---|---|
| `u` | strictly (0, 1) | **EXEMPLARY:** `ValueError: u must be in (0, 1), got 1.5` — named, stated, shown |
| `rate` | > 0 | **UNGUARDED:** -2 → returns -0.3466 (impossible) silently · 0 → cryptic ZeroDivision |

The whole audit lesson in one file: the author knew how to write a contract (the u-guard is the
library's gold standard) — and left the parameter one line below it naked. Good practice and the
gap live side by side.

## How inputs shape the output
- **`u → 0`** gives samples near 0; **`u → 1`** gives large samples (the tail) — that's why the
  domain is OPEN: u=1 would be `-log(0)/rate = +∞`, so the guard correctly forbids it.
- **`rate` scales inversely**: doubling rate halves the mean sample. Negative rate flips the sign —
  which is meaningless for a waiting time, hence the needed guard.

## Failure modes (audited by hand)
| Trigger | What happens today | Meaning |
|---|---|---|
| `u = 1.5` or `u = 1.0` | contract ValueError, named | the standard every pattern should meet ✅✅ |
| `rate = -2.0` | **-0.3466 silently** — negative waiting time | silent-wrong-sign on a plausible call (kill-class) |
| `rate = 0` | ZeroDivisionError | honest but cryptic; the guard would name it |
| demo `true_var` corrupted | assert fires instantly | LIVE oracle — coverage real (contrast log_rank) |

## Worked example (real run)
```
$ python3 python/data-science/information_theory_and_probability/inverse_transform_sampling.py
Inverse-transform sampling (exponential + piecewise): all assertions PASS
```
The demo derives its expected mean/variance FROM `rate`, so changing rate keeps the test honest —
a well-built oracle that tracks its own inputs.

## Provenance
Machine-VERIFIED (frozen ruler) · cross-model reviewed 07-18 · **Illia's audit 07-20: u-guard
exemplary, rate-guard missing (silent negative output) → ❌-lean, severity ruling pending; fix #13** ·
evidence: `output/manual_audit_2026-07-19.csv`
