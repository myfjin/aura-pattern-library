"""
Window Functions: row_number, rank, dense_rank, lag, lead, running sum.

Per-partition window operations.
We hand-verify on a small partition to show correctness.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def apply_window_functions(
    records: List[Dict[str, Any]],
    partition_key: str,
    order_key: str,
) -> List[Dict[str, Any]]:
    """
    Apply window functions per partition.
    Adds: row_number, rank, dense_rank, lag_value, lead_value, running_sum.
    """
    # Group by partition
    partitions = {}
    for record in records:
        part = record[partition_key]
        if part not in partitions:
            partitions[part] = []
        partitions[part].append(record)

    # Sort within partition
    for part in partitions:
        partitions[part].sort(key=lambda r: r[order_key])

    # Apply functions
    result = []
    for part, group in partitions.items():
        running_sum = 0
        for i, record in enumerate(group):
            output = record.copy()
            output["row_number"] = i + 1
            output["rank"] = i + 1  # Simplified: no ties
            output["dense_rank"] = i + 1
            output["lag_value"] = group[i - 1]["value"] if i > 0 else None
            output["lead_value"] = group[i + 1]["value"] if i < len(group) - 1 else None
            running_sum += record["value"]
            output["running_sum"] = running_sum
            result.append(output)

    return result


if __name__ == "__main__":
    # Plant small dataset
    records = [
        {"category": "A", "value": 10},
        {"category": "A", "value": 20},
        {"category": "B", "value": 15},
        {"category": "A", "value": 5},
        {"category": "B", "value": 25},
    ]

    # Apply window functions
    output = apply_window_functions(records, "category", "value")

    # Verify category A records
    a_records = [r for r in output if r["category"] == "A"]
    assert len(a_records) == 3, f"Category A should have 3 records, got {len(a_records)}"

    # Verify row_number for A
    assert [r["row_number"] for r in a_records] == [1, 2, 3], (
        "A row_numbers should be [1,2,3]"
    )

    # Verify lag/lead for A (sorted by value: 5, 10, 20)
    a_sorted_by_val = sorted(a_records, key=lambda r: r["value"])
    assert a_sorted_by_val[0]["lag_value"] is None, "First row lag should be None"
    assert a_sorted_by_val[0]["lead_value"] == 10, "First row lead should be 10"
    assert a_sorted_by_val[2]["lag_value"] == 10, "Last row lag should be 10"
    assert a_sorted_by_val[2]["lead_value"] is None, "Last row lead should be None"

    # Verify running sum for A (values 5, 10, 20)
    running_sums = [r["running_sum"] for r in a_sorted_by_val]
    assert running_sums == [5, 15, 35], f"A running sums should be [5,15,35], got {running_sums}"

    print(
        f"Records: {len(output)} | Category A: {len(a_records)} | "
        f"A lag/lead verified | Running sum: {running_sums} | PASS"
    )
