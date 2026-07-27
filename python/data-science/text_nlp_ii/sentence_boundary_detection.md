# sentence boundary detection

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(text: str) → List[str]`

## What it does

Sentence boundary detection: split text at sentence ends despite abbreviations.

Detects end-of-sentence punctuation (. ! ?) while NOT splitting on the periods inside
common abbreviations (Dr., Mr., St., …). Core claim: abbreviation periods are protected;
real sentence ends are split.

## Guarantee

When it runs, sentence boundary detection guarantees any(('Hello' in s for s in basic)); abbrev[0] == 'Dr. Smith went home.' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(basic) == 3`
- `any(('Hello' in s for s in basic))`
- `len(abbrev) == 2`
- `abbrev[0] == 'Dr. Smith went home.'`
- `len(two) == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def split_sentences(text: str) -> List[str]:`
**Valid input:** `text` is a string containing sentence-ending punctuation and optional abbreviations.
**Core:** Splits text into sentences at `.`, `!`, or `?` when the punctuation is followed by a space or end of text, while protecting a small hardcoded set of abbreviations (`Dr`, `Mr`, `Mrs`, `Ms`, `Prof`, `St`, `Ave`, `Inc`, `Ltd`, `vs`, `etc`).
**Assert:** "Hello world. This is a test. How are you?" splits into 3 sentences; "Dr. Smith went home. He was tired." splits into 2 sentences with the abbreviation kept intact; two abbreviations in one sentence do not cause spurious splits.
**⚠️ Defect:** The abbreviation set is tiny and English-centric; any abbreviation not in the set triggers a false split. It only checks whether the word stripped of punctuation is in the set, so "Dr" at a real sentence end is also protected. Punctuation followed by a newline rather than a space is not treated as a boundary.

---
*△ AURA Pattern Library — © Reality Optimizer*
