"""
CSV Type Inference.

Read CSV and infer column types (int, float, date, str).
We verify every column against planted data with explicit types.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
from typing import List, Dict, Any


def infer_type(value: str) -> str:
    """Infer type of a string value."""
    if value == "" or value.lower() == "none":
        return "missing"

    # Try int
    try:
        int(value)
        return "int"
    except ValueError:
        pass

    # Try float
    try:
        float(value)
        return "float"
    except ValueError:
        pass

    # Try date (YYYY-MM-DD)
    if re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return "date"

    return "str"


def infer_column_types(
    rows: List[Dict[str, str]]
) -> Dict[str, str]:
    """Infer type for each column (most common non-missing type)."""
    if not rows:
        return {}

    columns = rows[0].keys()
    type_counts = {col: {} for col in columns}

    for row in rows:
        for col in columns:
            value = row[col]
            inferred = infer_type(value)
            if inferred != "missing":
                type_counts[col][inferred] = type_counts[col].get(inferred, 0) + 1

    # Most common type per column
    result = {}
    for col, counts in type_counts.items():
        if counts:
            result[col] = max(counts, key=counts.get)
        else:
            result[col] = "str"  # Default if all missing

    return result


if __name__ == "__main__":
    # Plant CSV data
    rows = [
        {"id": "1", "age": "25", "salary": "50000.50", "date": "2024-01-15", "name": "Alice"},
        {"id": "2", "age": "30", "salary": "60000.00", "date": "2024-02-20", "name": "Bob"},
        {"id": "3", "age": "", "salary": "75000", "date": "2024-03-10", "name": "Charlie"},
    ]

    # Infer types
    types = infer_column_types(rows)

    # Verify each column
    assert types["id"] == "int", f"id should be int, got {types['id']}"
    assert types["age"] == "int", f"age should be int, got {types['age']}"
    assert types["salary"] == "float", f"salary should be float, got {types['salary']}"
    assert types["date"] == "date", f"date should be date, got {types['date']}"
    assert types["name"] == "str", f"name should be str, got {types['name']}"

    # Verify missing value handling: age has one missing (""), but 2 ints, so type is int
    age_values = [r["age"] for r in rows]
    assert "" in age_values, "Should have a missing age"

    print(
        f"Inferred types: {types} | "
        f"id={types['id']} | age={types['age']} (with missing) | "
        f"salary={types['salary']} | date={types['date']} | name={types['name']} | PASS"
    )
