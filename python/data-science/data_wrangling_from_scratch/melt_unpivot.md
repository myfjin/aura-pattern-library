# melt unpivot

**Language:** Python · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(wide_data: Dict[Any, Dict[Any, float]], row_key_name: str, col_key_name: str, val_key_name: str) → List[Dict[str, Any]]`

## What it does

Melt (Unpivot): Wide to Long Format.

Convert wide-format table back to long-format records.
We verify that pivot(melt(data)) == data (round-trip).

## Guarantee

When it runs, melt unpivot guarantees wide_again == wide; {'category': 'A', 'region': 'US', 'amount': 150} in long (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(long) == 4`
- `wide_again == wide`
- `{'category': 'A', 'region': 'US', 'amount': 150} in long`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def melt(wide_data: Dict[Any, Dict[Any, float]], row_key_name: str, col_key_name: str, val_key_name: str) -> List[Dict[str, Any]]:`, `def pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str) -> Dict[Any, Dict[Any, float]]:`
**Valid input:** `wide_data` is a nested dict `{row: {col: value}}`; key-name strings are non-empty.
**Core:** Melt (unpivot): converts a wide nested-dict table into long-format records. Includes a simple pivot function for the reverse direction to verify round-trip equality.
**Assert:** On a 2×2 wide table, `melt` produces 4 records and `pivot_table(melt(...))` recovers the original wide table exactly.
**⚠️ Defect:** `pivot_table` in this module silently overwrites duplicate `(row, col)` pairs instead of aggregating. If the long input contains repeated row/column combinations, information is lost. The round-trip assertion passes only because the demo has unique cells.

---
*△ AURA Pattern Library — © Reality Optimizer*
