# concept drift ensemble

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(y: List[int], window: int) → ?`

## What it does

Concept-drift ensemble vs a frozen single learner.
Core idea: on a stream whose concept flips, a drift-aware ensemble that spawns a fresh
learner per window and weights learners by their RECENT accuracy adapts to the new
concept, while a single learner frozen on pre-drift data keeps predicting the old one.
When: streaming classification under concept drift -- the demo MEASURES the ensemble
beating the frozen model on the post-drift segment (the defining claim, not "acc>0.4").

## Guarantee

When it runs, concept drift ensemble guarantees ens_acc > 0.75; single_acc < 0.3; ens_acc - single_acc > 0.4 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ens_acc > 0.75`
- `single_acc < 0.3`
- `ens_acc - single_acc > 0.4`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
