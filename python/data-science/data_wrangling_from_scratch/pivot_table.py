"""
Pivot Table (Long to Wide).

Convert long-format records to wide-format table with row/column headers and aggregation.
We verify that pivot + row/column totals (margins) equal independently computed totals.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def pivot_table(
    records: List[Dict[str, Any]],
    row_key: str,
    col_key: str,
    val_key: str,
    agg_func: str = "sum",
) -> Dict[Any, Dict[Any, float]]:
    """Pivot long → wide. Returns {row_val: {col_val: aggregated_value}}."""
    pivot = {}

    for record in records:
        row = record[row_key]
        col = record[col_key]
        val = record[val_key]

        if row not in pivot:
            pivot[row] = {}

        if col not in pivot[row]:
            if agg_func == "sum":
                pivot[row][col] = 0
            elif agg_func == "count":
                pivot[row][col] = 0
            else:
                pivot[row][col] = []

        if agg_func == "sum":
            pivot[row][col] += val
        elif agg_func == "count":
            pivot[row][col] += 1

    return pivot


def compute_margins(pivot: Dict[Any, Dict[Any, float]]) -> Dict[str, Dict[Any, float]]:
    """Compute row totals and column totals."""
    row_totals = {}
    col_totals = {}

    for row, cols in pivot.items():
        row_totals[row] = sum(cols.values())
        for col, val in cols.items():
            if col not in col_totals:
                col_totals[col] = 0
            col_totals[col] += val

    return {"row_totals": row_totals, "col_totals": col_totals}


if __name__ == "__main__":
    # Plant long-format data
    records = [
        {"category": "A", "region": "US", "amount": 100},
        {"category": "A", "region": "US", "amount": 50},
        {"category": "A", "region": "EU", "amount": 75},
        {"category": "B", "region": "US", "amount": 30},
        {"category": "B", "region": "EU", "amount": 80},
        {"category": "B", "region": "EU", "amount": 45},
    ]

    # Pivot
    pivot = pivot_table(records, "category", "region", "amount", "sum")

    # Compute margins
    margins = compute_margins(pivot)
    row_totals = margins["row_totals"]
    col_totals = margins["col_totals"]

    # Verify: sum of row totals = sum of all values
    total_from_rows = sum(row_totals.values())
    total_from_cols = sum(col_totals.values())
    total_from_records = sum(r["amount"] for r in records)

    assert total_from_rows == total_from_records, (
        f"Row totals {total_from_rows} != record sum {total_from_records}"
    )
    assert total_from_cols == total_from_records, (
        f"Col totals {total_from_cols} != record sum {total_from_records}"
    )

    # Verify specific pivot cells
    assert pivot["A"]["US"] == 150, f"A/US should be 150, got {pivot['A']['US']}"
    assert pivot["B"]["EU"] == 125, f"B/EU should be 125, got {pivot['B']['EU']}"

    # Verify row totals
    assert row_totals["A"] == 225, f"A total should be 225, got {row_totals['A']}"
    assert row_totals["B"] == 155, f"B total should be 155, got {row_totals['B']}"

    print(
        f"Pivot: A/US={pivot['A']['US']} | B/EU={pivot['B']['EU']} | "
        f"Row totals: {row_totals} | Col totals: {col_totals} | "
        f"Grand total: {total_from_rows} | PASS"
    )
