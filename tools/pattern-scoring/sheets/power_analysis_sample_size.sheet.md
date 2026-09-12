# PATTERN SHEET — power_analysis_sample_size
`python/data-science/statistical_modeling/power_analysis_sample_size.py`

## What it solves
Before running an A/B experiment: **how many samples per group do I need** to reliably detect a
difference between two proportions (e.g. conversion 30% vs 50%)? Too few samples → real effects go
unnoticed; too many → wasted time/money. This computes the minimum n hitting your target power.

## Valid inputs (the contract)
| Input | Domain | Violating it → |
|---|---|---|
| `p1`, `p2` (the two proportions) | each in [0, 1] | AURA-E003 |
| `alpha` (significance level) | in (0, 1), conventionally 0.05 | AURA-E001 |
| `target_power` | in (0, 1), conventionally 0.80 | (B5) |
| `p1 ≠ p2` | effect must be nonzero | AURA-E002 |

## How inputs shape the output
- **Effect size `|p1 − p2|` is the dominant knob**: halving the gap roughly *quadruples* required n
  (n scales with 1/effect²). p1=p2 → n is undefined (infinite) — that's E002, not a bug.
- **`alpha` down** (stricter significance, e.g. 0.01) → larger n: rarer false alarms cost samples.
- **`target_power` up** (e.g. 0.90) → larger n: catching real effects more reliably costs samples.
- **Proportions near 0.5** carry maximum variance → larger n than the same gap near 0 or 1.

## Worked example (real run)
```
$ python3 python/data-science/statistical_modeling/power_analysis_sample_size.py
power_analysis_sample_size.py: n_computed=185, achieved_power=0.963, target=0.8 PASS
```
**Reading the output:** to distinguish 30% vs 50% conversion at alpha=0.05 with 80% target power,
you need **185 samples per group** (370 total). The self-check then *proves* the number: at n=185
the achieved power is 0.963 ≥ 0.8, and (asserted in code) n−1 gives strictly less power — so 185
is sufficient and not padded.

## Failure modes (audited by hand, 2026-07-19)
| Trigger | What happens today | Meaning |
|---|---|---|
| `alpha = -0.05` | ValueError (math.log domain) — AURA-E001, accidental/cryptic | significance must be in (0,1) |
| `p1 = p2` | ZeroDivisionError — AURA-E002, accidental/cryptic | zero effect → n undefined |
| `p1 = 1.5` | ValueError (sqrt domain) — AURA-E003, accidental/cryptic | proportion outside [0,1] |
| combined bad inputs | only the FIRST crash reports, misattributed | fixed by accumulate-then-raise retrofit (see `playground/retrofit_demo/`) |

## Provenance
Machine-VERIFIED (frozen ruler v1.0.0) · description cross-model reviewed 2026-07-18 ·
**Illia's audit 2026-07-19: PASS-WITH-FLAG** (3 attacks, 0 silent-wrong; all catches accidental →
retrofit candidate E001–E003) · evidence: `output/manual_audit_2026-07-19.csv`
