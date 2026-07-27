# soundex phonetic

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(name: str) → str`

## What it does

Soundex: phonetic encoding for name matching and fuzzy search.

Maps names to 4-char code (1 letter + 3 digits) based on pronunciation.
Core claim: known name pairs match (same code); dissimilar names differ.

## Guarantee

When it runs, soundex phonetic guarantees soundex('Robert') == soundex('Rupert'); soundex('Ashcraft') == soundex('Ashcroft'); soundex('Alice') != soundex('Bob') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `soundex('Robert') == soundex('Rupert')`
- `soundex('Ashcraft') == soundex('Ashcroft')`
- `soundex('Alice') != soundex('Bob')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def soundex(name: str) -> str:`
**Valid input:** `name` is a string; empty string is allowed.
**Core:** Computes the classic Soundex phonetic code: first letter + up to three digits derived from consonant classes, removing adjacent duplicate codes and padding to four characters with zeros.
**Assert:** `soundex("Robert") == soundex("Rupert")`; `soundex("Ashcraft") == soundex("Ashcroft")`; `soundex("Alice") != soundex("Bob")`.
**⚠️ Defect:** The simplified implementation does not follow the full Soundex rule that a code assigned to the first letter should be dropped, nor does it always handle adjacent duplicate codes correctly when the first letter maps to a digit. Non-ASCII names and mixed-case input may produce unexpected results.

---
*△ AURA Pattern Library — © Reality Optimizer*
