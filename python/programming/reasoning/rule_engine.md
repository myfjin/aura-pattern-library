# rule engine

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

**Signature:** `() → None`

## What it does

Rule-based inference engine with forward chaining and conflict resolution.

## Guarantee

When it runs, rule engine guarantees facts_added == 4; added2 == 2; len(kb.facts) == 3 and len(kb.rules) == 4 (proven by run).

**Checkable constraints:**

- `len(kb.facts) == 3 and len(kb.rules) == 4`
- `facts_added == 4`
- `iterations >= 2`
- `kb.query(Fact('diagnosis', disease='flu'))`
- `kb.query(Fact('diagnosis', disease='migraine'))`
- `kb.query(Fact('treatment', medication='antipyretic'))`
- `kb.query(Fact('treatment', medication='analgesic'))`
- `not kb.query(Fact('diagnosis', disease='cancer'))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
