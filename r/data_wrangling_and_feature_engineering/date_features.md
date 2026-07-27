# date features

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

Date Feature Engineering
Implements Date → weekday/month/quarter/is-weekend; verified against known calendar
Use when: extracting temporal features

## Guarantee

When it runs, date features guarantees month[idx_jan1] == 1; quarter[idx_jan1] == 1; weekday[idx_jan1] == 3 (proven by run).

**Checkable constraints:**

- `month[idx_jan1] == 1`
- `quarter[idx_jan1] == 1`
- `weekday[idx_jan1] == 3`
- `is_weekend[idx_jan1] == 0`
- `month[idx_test] == 4`
- `quarter[idx_test] == 2`
- `all(quarter >= 1 & quarter <= 4)`
- `all(is_weekend %in% c(0, 1))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `Date` vector named `dates` must exist in the global environment. The script generates 100 consecutive days starting from `2025-01-01` as a demo if `dates` is not pre-loaded, so results depend on whether `dates` is caller-supplied.
**Core:** Extracts weekday (`%w`, 0 = Sunday), month, quarter, and weekend flag from a date vector using base R `format()` and arithmetic.
**Assert:** Spot-checks known calendar dates (2025-01-01 is Wednesday, Q1); verifies all quarters are in 1–4 and all weekend flags are 0/1.
**⚠️ Defect:** No input validation: a non-Date vector or `NA` dates produce silently wrong or `NA` results. The `%w` Sunday-zero convention is undocumented in the script. Because it is a top-level script, it cannot be reused as a function and it mutates/replaces the extracted vectors in the global environment.

---
*△ AURA Pattern Library — © Reality Optimizer*
