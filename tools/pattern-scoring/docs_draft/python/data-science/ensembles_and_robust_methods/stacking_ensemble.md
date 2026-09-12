# Stacking Ensemble with Meta-Learner

**File:** `python/data-science/ensembles_and_robust_methods/stacking_ensemble.py`
**Sphere:** Data Science — Ensembles and Robust Methods
**Status:** ❌ INVALID as shipped (Illia's audit 2026-07-19)

---

## What it solves

Two mediocre models can beat one good one — if you combine them well. Stacking trains base models, then trains a **meta-model on their predictions**: it learns *when to trust which base*. This pattern demonstrates the full loop: fit bases → generate meta-features → fit meta → compare accuracies (stack should match or beat the best base).

**When to use:** Combining diverse base models where you suspect different models excel on different regions of the data. The meta-learner learns the weighting automatically — you don't have to guess which model to trust when.

---

## Valid inputs (the contract — enforced only in the retrofit)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | list of `(x1, x2)` tuples of **finite** floats | AURA-E-B2 (shape) / AURA-E008 (NaN/inf) |
| `y` | list of labels in {0, 1}, `len(y) == len(X)` | AURA-E007 |

---

## How inputs shape the output

- **Class separation drives everything:** the demo's clusters sit at (2,2) vs (8,8) with σ=2.5 — well separated → accuracies near 1.0. Move the means closer and all three accuracies fall together; stacking's *edge* over the bases shows most at intermediate separation.
- **`n_per_class` is the stability knob:** more points → tighter accuracy estimates (Illia's n=150/100 runs moved accuracies by a few points — that's sampling noise, not behavior change).
- **Label quality is the silent killer:** one shifted label chain (E007) or one NaN point (E008) corrupts training with NO visible change in output — which is why the contract must check what the math never will.

---

## Worked example (real run)

```
$ python3 python/data-science/ensembles_and_robust_methods/stacking_ensemble.py
stacking_ensemble: base1_acc=0.9667, base2_acc=1.0000, stack_acc=1.0000 PASS
```

**Reading the output:** base1 (threshold on x1) gets 96.7%, base2 (distance-based) gets 100%, and the stack learns to lean on base2 → 100%. The claim proven is `stack ≥ max(bases)` on this data — stacking never has to be worse than its best ingredient.

---

## Failure modes (audited by hand — this audit's purest silent failure)

| Trigger | As shipped | Retrofit |
|---|---|---|
| `X[0] = (float("nan"), 0.0)` | **PASS, numbers identical to clean run** — poisoned model, zero trace | AURA-E008 raised |
| junk label + length mismatch (`y=[10]+…`) | trained on shifted labels; crashed LATER by IndexError luck | AURA-E007: both faults named together |
| `'nan'` string / `99` int as a point | cryptic TypeError deep in `sorted()` | named shape/type violation |
| `X=[]`, `y=[]` before generation loops | **no-op attack** — loops rebuild data; PASS is legitimate | (field note: attack after generation) |

---

## Provenance

Machine-VERIFIED (frozen ruler) · description cross-model reviewed 2026-07-18 · Illia's audit 2026-07-19: 10 runs → NaN silent-wrong → ❌ INVALID; retrofit proven same day · evidence: `output/manual_audit_2026-07-19.csv` · errors: AURA-E007, E008
