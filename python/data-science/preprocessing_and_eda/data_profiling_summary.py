"""
Data Profiling Summary Pattern.

Per-column profile of a mixed dataset (numeric/categorical): type inference,
missing count, cardinality, min/max/mean for numeric, top values for categorical.
Core idea: one-pass summary to understand data structure, missingness, range,
and uniqueness without external libraries.

When to use: exploratory data analysis, data quality checks, understanding
dataset structure before modeling, missing-data patterns, feature planning.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any, Union
import statistics


def infer_type(value: Any) -> str:
    """Infer type: numeric or categorical."""
    if value is None:
        return "unknown"
    try:
        float(value)
        return "numeric"
    except (ValueError, TypeError):
        return "categorical"


def profile_column(data: List[Any]) -> Dict[str, Any]:
    """
    Profile a single column.
    Returns dict with: type, missing_count, cardinality, {min,max,mean} or {top_values}
    """
    n = len(data)
    non_null = [x for x in data if x is not None]
    missing_count = n - len(non_null)

    if not non_null:
        return {
            "type": "unknown",
            "missing_count": missing_count,
            "cardinality": 0,
        }

    # Infer type from first non-null value
    col_type = infer_type(non_null[0])

    # Count unique values
    cardinality = len(set(non_null))

    profile = {
        "type": col_type,
        "missing_count": missing_count,
        "cardinality": cardinality,
    }

    if col_type == "numeric":
        numeric_vals = []
        for x in non_null:
            try:
                numeric_vals.append(float(x))
            except (ValueError, TypeError):
                pass

        if numeric_vals:
            profile["min"] = min(numeric_vals)
            profile["max"] = max(numeric_vals)
            profile["mean"] = statistics.mean(numeric_vals)

    elif col_type == "categorical":
        # Count occurrences, get top values
        counts = {}
        for x in non_null:
            counts[x] = counts.get(x, 0) + 1

        top_3 = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:3]
        profile["top_values"] = [val for val, count in top_3]
        profile["top_counts"] = [count for val, count in top_3]

    return profile


def profile_dataset(data: List[List[Any]], column_names: List[str] = None) -> Dict[str, Dict]:
    """
    Profile entire dataset (list of rows).
    Args:
        data: List of rows (each row is a list of values)
        column_names: Optional list of column names
    Returns:
        Dict mapping column name -> profile dict
    """
    if not data:
        return {}

    n_cols = len(data[0])
    if column_names is None:
        column_names = [f"col_{i}" for i in range(n_cols)]

    # Transpose to get columns
    columns = [[row[i] for row in data] for i in range(n_cols)]

    profiles = {}
    for name, col in zip(column_names, columns):
        profiles[name] = profile_column(col)

    return profiles


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic mixed dataset
    dataset = [
        # age (numeric), city (categorical), salary (numeric), employed (binary)
        [25, "NYC", 50000, "yes"],
        [30, "LA", 60000, "yes"],
        [None, "NYC", 55000, "no"],  # Missing age
        [35, "Chicago", None, "yes"],  # Missing salary
        [28, "NYC", 52000, "yes"],
        [42, "LA", 75000, "yes"],
        [None, "Chicago", 58000, "no"],  # Missing age
        [31, "NYC", 61000, "yes"],
        [36, "LA", 70000, "no"],
        [27, "Chicago", 49000, "yes"],
    ]

    profiles = profile_dataset(
        dataset, column_names=["age", "city", "salary", "employed"]
    )

    # Verify age profile
    age_prof = profiles["age"]
    assert age_prof["type"] == "numeric", f"Age type: {age_prof['type']}"
    assert age_prof["missing_count"] == 2, f"Age missing: {age_prof['missing_count']}"
    assert age_prof["cardinality"] == 8, f"Age cardinality: {age_prof['cardinality']}"
    assert "min" in age_prof and "max" in age_prof and "mean" in age_prof
    assert age_prof["min"] == 25, f"Age min: {age_prof['min']}"
    assert age_prof["max"] == 42, f"Age max: {age_prof['max']}"

    # Verify city profile
    city_prof = profiles["city"]
    assert city_prof["type"] == "categorical", f"City type: {city_prof['type']}"
    assert city_prof["missing_count"] == 0, f"City missing: {city_prof['missing_count']}"
    assert city_prof["cardinality"] == 3, f"City cardinality: {city_prof['cardinality']}"
    assert set(city_prof["top_values"]) == {"NYC", "LA", "Chicago"}

    # Verify salary profile
    salary_prof = profiles["salary"]
    assert salary_prof["type"] == "numeric", f"Salary type: {salary_prof['type']}"
    assert salary_prof["missing_count"] == 1, f"Salary missing: {salary_prof['missing_count']}"

    # Verify employed profile
    employed_prof = profiles["employed"]
    assert employed_prof["type"] == "categorical", f"Employed type: {employed_prof['type']}"
    assert employed_prof["cardinality"] == 2, f"Employed cardinality: {employed_prof['cardinality']}"

    print("data_profiling_summary.py: PASS")
