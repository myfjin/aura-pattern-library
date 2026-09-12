# Library Docs Architecture — product-grade documentation (Illia, 2026-07-20)
**Goal: the library reads as a product. Two-tier docs + uniform in-file descriptions.**

## Three layers of description (each a different audience)
1. **In-file doc-comment** (in the .py/.cpp/.rs/.go/.R itself) — follows `DESCRIPTION_STANDARD.md`
   (WHAT / WHEN / GUARANTEES + human when-to-use). The developer reading source. → separate class-fix.
2. **Per-pattern detail doc** — one Markdown file per pattern, the SHEET format we've been writing
   in `pattern-scoring/sheets/`: what-it-solves (human) · valid inputs/contract · how inputs shape
   output · worked example (real run) · failure modes · provenance. The student/evaluator.
3. **Main index** — one file, short one-line description per pattern + link to its detail doc,
   grouped by language → sphere. The browser/newcomer.

## Layout (in the library)
```
aura-pattern-library/
  docs/
    INDEX.md                     ← main index: short desc + link per pattern, grouped
    <lang>/<sphere>/<name>.md    ← per-pattern detail doc (sheet format)
```
The ~20 audited patterns already have detail docs in `pattern-scoring/sheets/` → seed docs/ from
those. The rest get written per the sheet template.

## Division of labor (Illia's directive)
- **6E writes** the per-pattern detail docs + short index entries (per DESCRIPTION_STANDARD + the
  sheet template). Account: llibresnave (with 4Q).
- **Ver approves** (@stewardhermesbot) — cross-model check: does each description match the CODE?
  (the docstring-lie hunt, applied to docs). Account: ihladkyi2 (with 5S) — lighter load = approval.
- Same two-model discipline as the 191-description fix + cross-model review: writer ≠ approver.

## Phasing (this runs in PARALLEL with the tool build; does NOT block it)
- **Phase 1:** the ~20 AUDITED patterns — polish existing sheets into docs/, write index entries.
  (Their prose exists; 6E refines + Ver approves. Small, fast, proves the pipeline.)
- **Phase 2:** by sphere, highest-value first (the public-facing DS + sysadmin spheres).
- **Phase 3:** remainder. No deadline — quality over speed; the tool build is the deadline item.

## Verification
A linter checks: every pattern has (a) a docs/ detail file with all required sections,
(b) an INDEX.md entry linking it, (c) an in-file doc-comment passing DESCRIPTION_STANDARD.
GREEN = the library is fully, uniformly documented.
