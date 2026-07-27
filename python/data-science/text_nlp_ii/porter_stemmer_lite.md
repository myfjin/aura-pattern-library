# porter stemmer lite

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(word: str) → str`

## What it does

Porter stemmer: rule-based morphological analysis for English word stemming.

Reduces words to root form via suffix removal rules. Core claim: canonical
test pairs stem correctly; planted words recover their stems.

## Guarantee

When it runs, porter stemmer lite guarantees stem == expected (proven by run).

**Checkable constraints:**

- `stem == expected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def porter_stem_lite(word: str) -> str:`
**Valid input:** `word` is a string.
**Core:** Simplified rule-based Porter stemmer that strips common English suffixes (-s, -es, -ies, -ing, -ed, -ational, -tional, -ly, -ness) and performs minor orthographic fixes.
**Assert:** Planted pairs stem as expected: "running" → "runn", "runs" → "run", "ponies" → "poni", "caresses" → "caress", "organizational" → "organize", "happiness" → "happi", "slowly" → "slow".
**⚠️ Defect:** The implementation covers only a tiny subset of Porter's steps and conditions; many valid English words will be under-stemmed or over-stemmed. It does not handle the consonant/vowel measure (`m`) that the full Porter algorithm uses to decide when suffix removal is safe, so words like "ational" in other contexts may be over-truncated.

---
*△ AURA Pattern Library — © Reality Optimizer*
