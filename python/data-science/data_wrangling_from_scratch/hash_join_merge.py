"""
Hash Join: Inner and Left Join.

Hash-based join of two tables on a key.
We verify results match a brute-force nested-loop join.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def hash_join_inner(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
    """Inner hash join: only rows with matching keys in both tables."""
    # Build hash table from right
    right_hash = {}
    for row in right_table:
        key = row[join_key]
        if key not in right_hash:
            right_hash[key] = []
        right_hash[key].append(row)

    # Probe with left
    result = []
    for left_row in left_table:
        key = left_row[join_key]
        if key in right_hash:
            for right_row in right_hash[key]:
                merged = {**left_row, **right_row}
                result.append(merged)

    return result


def hash_join_left(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
    """Left hash join: all rows from left, matched rows from right (or None)."""
    # Build hash table from right
    right_hash = {}
    for row in right_table:
        key = row[join_key]
        if key not in right_hash:
            right_hash[key] = []
        right_hash[key].append(row)

    # Probe with left
    result = []
    for left_row in left_table:
        key = left_row[join_key]
        if key in right_hash:
            for right_row in right_hash[key]:
                merged = {**left_row, **right_row}
                result.append(merged)
        else:
            # No match: include left row with None for right columns
            result.append(left_row)

    return result


def nested_loop_inner_join(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
    """Brute-force nested-loop inner join."""
    result = []
    for left_row in left_table:
        for right_row in right_table:
            if left_row[join_key] == right_row[join_key]:
                merged = {**left_row, **right_row}
                result.append(merged)
    return result


if __name__ == "__main__":
    # Plant tables
    left = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]

    right = [
        {"id": 1, "salary": 100},
        {"id": 2, "salary": 150},
        {"id": 4, "salary": 200},  # No match in left
    ]

    # Inner join
    hash_inner = hash_join_inner(left, right, "id")
    brute_inner = nested_loop_inner_join(left, right, "id")

    # Sort for comparison (order may differ)
    hash_inner_sorted = sorted(hash_inner, key=lambda r: r["id"])
    brute_inner_sorted = sorted(brute_inner, key=lambda r: r["id"])

    assert hash_inner_sorted == brute_inner_sorted, (
        f"Inner join mismatch: {hash_inner_sorted} vs {brute_inner_sorted}"
    )

    # Check: inner join should have 2 rows (id=1,2 in both tables)
    assert len(hash_inner) == 2, f"Inner join should have 2 rows, got {len(hash_inner)}"

    # Left join
    hash_left = hash_join_left(left, right, "id")

    # Check: left join should have 3 rows (all from left)
    assert len(hash_left) == 3, f"Left join should have 3 rows, got {len(hash_left)}"

    # Check: row with id=3 should have None salary
    id3_row = [r for r in hash_left if r["id"] == 3]
    assert len(id3_row) == 1 and id3_row[0].get("salary") is None, (
        f"Left join row with id=3 should have no salary: {id3_row}"
    )

    print(
        f"Inner join: {len(hash_inner)} rows | Left join: {len(hash_left)} rows | "
        f"Unmatched id=3: {'salary' not in id3_row[0]} | PASS"
    )
