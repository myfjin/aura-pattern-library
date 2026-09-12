# PATTERN SHEET — gradient_boosting_stumps
`python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py`
**Status: PASS-WITH-FLAG (Illia's audit, 2026-07-19) — boosting held; empty/NaN degenerates
flagged; in-file description ruled jargon → this sheet is the rewrite source.**

## What it solves (the human version — no "AI decisions" mystique)
**Prediction by committee of very dumb rules.** A "stump" is the dumbest possible predictor:
one question, one split — "is x₁ > 5? then predict 22, else predict 3." Alone it's crude
(our demo: error 0.32). Boosting's trick: after the first stump, look at what it got WRONG
(the residuals), and train the next stump *only on those mistakes*. Then the next on what's
STILL wrong. Each stump is weighted small (the learning rate) so no single dumb rule dominates.
50 dumb rules, each fixing the last one's errors → error 0.04, **8× better than one stump**.
That's the whole idea behind XGBoost/LightGBM that wins Kaggle — this file is the minimal
honest version of it.

## Valid inputs (the contract — to be enforced per fix #8)
| Input | Domain | Today → |
|---|---|---|
| `y` (labels for gini_split) | non-empty list of finite numbers | `[]` → `(0.0, inf)` silently · NaN → `(nan, inf)` |
| training data | ≥ 1 point, finite | empty set trains silently, crashes later at MSE |
| single label | legit: one point is "pure", threshold `inf` = no split possible | works, undeclared |

## How inputs shape the output
- **Rounds × learning rate is one knob wearing two hats**: more rounds or higher rate = more
  aggressive fitting. Too much → memorizing noise (see walk_forward_early_stopping — its sibling
  pattern exists exactly to stop this).
- **Noise level (demo's `gauss(0, 1.5)`) sets the floor**: boosting can't beat irreducible noise;
  it approaches it. Crank the noise and watch boosted_mse rise toward it — honest behavior.
- **The quadrant landscape is why stumps need boosting**: one split can't carve four regions;
  each round's stump handles one boundary at a time.

## Worked example (real run)
```
$ python3 python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py
gradient_boosting_stumps: single_stump_mse=0.3244, boosted_mse=0.0396 PASS
```
**Reading the output:** one dumb rule scores 0.32 error; fifty of them, each correcting the
last, score 0.04. The assert proves the ensemble beats the best single stump — the claim that
justifies the pattern's existence.

## Failure modes (audited by hand)
| Trigger | What happens today | Meaning |
|---|---|---|
| `gini_split([])` | `(0.0, inf)` silently — "perfect purity" from no data | E009-class; needs guard |
| `gini_split([nan, 1.0])` | `(nan, inf)` — visible poison | E008-family (visible variant) |
| negative n → empty dataset | fit runs on nothing; ZeroDivision only at MSE downstream | E007-class late catch — worst kind |

## Provenance
Machine-VERIFIED (frozen ruler) · cross-model reviewed 07-18 · **Illia's audit 07-19:
PASS-WITH-FLAG; description ruled below comprehension gate → rewrite queued (fix #8)** ·
evidence: `output/manual_audit_2026-07-19.csv`
