# Pattern Description Standard — uniform structure, library-wide
**Illia's product requirement, 2026-07-20: every pattern's in-file description follows ONE
structure so the library reads as a product, not a pile. The "when to use" must speak to a
regular human, not only a specialist. Applies across all 5 languages.**

## The canonical 4-part structure (in the file's top doc-comment)
```
<NAME> — <one-line what-it-is>

WHAT IT DOES: 2–4 plain sentences. The mechanism in human terms (see the pattern-sheets'
  "human version" as the voice: e.g. gradient boosting = "prediction by committee of dumb rules").
WHEN TO USE: the real-world situation a NON-specialist would recognise. Name the problem before
  the solution ("You ran an A/B test and B looks better — is it real, or luck?"). 1–3 sentences.
GUARANTEES: what it promises + the disaster it survives (the ORACLE LAW: "cause the disaster,
  prove survival"). State the invariant precisely — this is what the audit checks against.
```
Optional 4th line: `NOT: <common misread>` when the name misleads (e.g. stick-breaking is NOT
neural-net weights; budget_allocator is NOT a byte allocator).

## Why (product rationale)
- Universities/students: uniform structure = teachable, scannable, trustworthy.
- The audit itself: a precise GUARANTEES line is the invariant the tool's R11 recipe tests. Vague
  descriptions can't be validated — good structure and good validation are the same discipline.
- Already-good exemplars to match: atomic_spinlock ("Core idea / THE ONE LAW / When to use"),
  checkpoint_resume_crc ("cause the real disaster"). Copy their shape everywhere.

## Scope & method (a CLASS fix — gated batch, NOT hot-edit)
- Source of truth for each pattern's human WHAT/WHEN: its pattern-sheet in `sheets/` (already
  written in human voice for the audited ones) → back-port sheet prose into the file doc-comment.
- Mass edit across ~1,399 files → runs through WORKFLOW Stage 3 (fix session → cross-model review
  → re-sign → library_verify GREEN). NOT during the audit.
- Ordering: audited patterns first (their sheets exist), then the rest by sphere.
- Verification: a linter that checks each file's doc-comment has all 3 required headings +
  a non-empty human "when to use" (>1 sentence, not just a title).

## Status
QUEUED as a post-audit class-fix. Standard defined 07-20. Not yet applied. Owner: a fix session
under Opus or a fresh Fable session, after the 33-pattern exam set is complete.
