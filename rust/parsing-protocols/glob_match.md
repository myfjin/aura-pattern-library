# glob match

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(pattern: &str, text: &str) → bool`

## What it does

glob_match — from-scratch * ? [..] matcher; planted matches/non-matches correct.

Core idea: implement glob pattern matching with *, ?, and character classes [abc] / [^abc].
THE ONE LAW: plant patterns and filenames with known matches and non-matches, then assert
every match/non-match is correct — a naive string contains would fail on * or ? anchoring.
When to use: file listing, wildcard filters, pathname matching in shell/tools.

## Guarantee

When it runs, glob match guarantees assert_eq!(result, *expected, "glob_match failed for pattern '{}' vs '{}'", pattern, text) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, *expected, "glob_match failed for pattern '{}' vs '{}'", pattern, text)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
