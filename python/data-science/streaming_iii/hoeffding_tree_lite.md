# hoeffding tree lite

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(X: ?, y: ?, thresholds: ?, delta: float) → ?`

## What it does

Hoeffding tree (VFDT) lite -- a streaming decision stump with a Hoeffding-bound split test.
Core idea: accumulate class counts on each side of every candidate split as data streams
in. After n samples the true information gain of a split is within
eps = sqrt(R^2 ln(1/delta) / 2n) of its observed gain (Hoeffding bound). Split as soon as
the best candidate's observed gain beats the runner-up's by more than eps -- then that
choice is provably the true best with prob >= 1-delta. The leaf predicts its majority class.
When: grow a decision tree online with a statistical guarantee on each split decision.

## Guarantee

When it runs, hoeffding tree lite guarantees bf == 0; stream_acc > majority + 0.25; abs(stream_acc - batch_acc) < 0.03 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bf == 0`
- `stream_acc > majority + 0.25`
- `abs(stream_acc - batch_acc) < 0.03`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
