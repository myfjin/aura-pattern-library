# Walk-Forward Early Stopping

**File:** `python/data-science/composed_tools/walk_forward_early_stopping.py`
**Sphere:** Data Science — Composed Tools
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-19)

---

## What it solves

**The gambler's problem: when do you stop training before your model starts lying to you?** A model that trains too long stops learning the signal and starts memorizing the noise — it looks BETTER on data it has seen (train error falls forever) while getting WORSE on the future.

This composed pattern welds two tools into the honest answer:
- **Walk-forward validation:** never grade the model on its own homework. Train on the past, test only on the *next* slice of time it has never seen — like a trader backtesting: you can't trade yesterday. (The demo shows the split: train error sinks to 0.45 "memorizing noise" while forward error bottoms at 0.944 and then RISES — that rise is the lie beginning.)
- **Early stopping with patience:** watch the forward error; when it hasn't improved for `patience` consecutive rounds, stop. Not at the first bad round (noise wiggles) — after a full patience window. The demo stops at round 26: minimum at 11 + patience 15. Exact.

**When to use:** Tuning training duration/rounds for any iterative model on time-ordered data. Where you meet this: every neural network's `EarlyStopping` callback, every trading-strategy backtest, every Kaggle submission that didn't overfit.

---

## Valid inputs (the contract — to be enforced per fix #9)

| Input | Domain | Today → |
|---|---|---|
| `X`, `r` (points, residuals) | same length, non-empty, finite | **mismatch → silent `(0, 0.0, 0.0, 0.0)`** · empty X → IndexError |
| `n` vs `split` | n > split (forward window must be non-empty) | n=11 → ZeroDivision deep in `mae` |
| `patience` | int ≥ 1 | (untested corruption caught by harness asserts) |

---

## How inputs shape the output

- **`patience` trades safety for opportunity:** small → stops early, may quit before the true minimum; large → waits longer, burns rounds training on noise. Demo: 15 rounds past minimum.
- **The train/forward split is the honesty knob:** tiny train set (split=8) → instant memorization (train MAE 0.000) and the overfit *shape* changes — the harness then refuses to certify (its asserts demand the phenomenon it documents). Planted-regime sensitivity, honest.
- **`since_best` is the whole mechanism:** Illia corrupted it both ways (+100 → stops absurdly early; +0.1 → never reaches integer patience, never stops) and BOTH asserts fired. A harness that verifies its own machinery — the standard other patterns should meet.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/walk_forward_early_stopping.py
train MAE at round 120: 0.453 (memorizing noise)
forward MAE: best 0.944 @ round 11 · final 1.097 @ round 120 · early-stopped @ 26
walk_forward_early_stopping.py PASS
```

**Reading the output:** by round 120 the train error (0.453) is far below the forward error (1.097) — the model memorized. The forward minimum was round 11; training past it made the future WORSE (0.944 → 1.097). Early stopping would have quit at 26, keeping nearly the best model. The three numbers ARE the overfitting story.

---

## Failure modes (audited by hand)

| Trigger | What happens today | Meaning |
|---|---|---|
| X/r length mismatch (either way) | **silent `(0, 0.0, 0.0, 0.0)`** — plausible zero-stump | E007-silent; a boosting loop swallows it wordlessly |
| empty X | IndexError at `X[0]` — accidental | needs contract |
| n ≤ split | forward window empty → ZeroDivision in `mae` | late accidental; needs n>split guard |
| corrupted stopping counter | **harness asserts CATCH it** (both directions) | mechanism-verifying asserts — exemplary |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · Illia's audit 2026-07-19: PASS-WITH-FLAG; description enrichment queued (fix #9); harness praised · evidence: `output/manual_audit_2026-07-19.csv`
