# catalog coverage diversity

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders II — kept survivors

## What it does

Catalog coverage and diversity of recommendations.

Measures the fraction of the overall catalog that appears in a recommendation list.
A diverse list exposes more of the catalog, while a narrow list clusters in a
small subset. Coverage is defined as |unique recommended items| / catalog_size.

## Guarantee

When it runs, catalog coverage diversity guarantees coverage_diverse > coverage_narrow (weak-grade: directional, proven by run).

**Checkable constraints:**

- `coverage_diverse > coverage_narrow`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def catalog_coverage(recommendations: Iterable[int], catalog_size: int) -> float:`, `def main() -> None:`
**Valid input:** `recommendations` is any iterable of item identifiers; `catalog_size` is a positive integer.
**Core:** Catalog coverage is the fraction of the full catalog that appears at least once in a recommendation list. It is a simple diversity metric: a higher value means the recommender explores more of the catalog instead of repeatedly returning the same popular items.
**Assert:** A list touching every item in a 5-item catalog gives coverage `1.0`; a narrow list touching only 2 items gives `0.4`; an empty list gives `0.0`; repeated items do not inflate coverage.
**⚠️ Defect:** The function silently clamps coverage to `1.0` if recommendations contain IDs larger than `catalog_size`, hiding a catalog-declaration mismatch rather than raising. It also validates `catalog_size` but not that recommendation IDs are non-negative or within any expected range.

---
*△ AURA Pattern Library — © Reality Optimizer*
