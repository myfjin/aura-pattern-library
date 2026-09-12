"""
Group-By Aggregation (Multi-Key).

Group records by one or more keys, then aggregate (sum, mean, count, min, max).
We verify against a brute-force nested-loop computation on the same data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def group_by_aggregate(
    records: List[Dict[str, Any]],
    group_keys: List[str],
    agg_col: str,
    agg_func: str,  # "sum", "mean", "count", "min", "max"
) -> Dict[tuple, float]:
    """
    Group records by group_keys, aggregate agg_col via agg_func.
    Returns: {group_tuple: result}.
    """
    groups = {}

    for record in records:
        # Compute group key
        key = tuple(record[k] for k in group_keys)

        # Add to group
        if key not in groups:
            groups[key] = []
        groups[key].append(record[agg_col])

    # Aggregate
    result = {}
    for key, values in groups.items():
        if agg_func == "sum":
            result[key] = sum(values)
        elif agg_func == "mean":
            result[key] = sum(values) / len(values)
        elif agg_func == "count":
            result[key] = len(values)
        elif agg_func == "min":
            result[key] = min(values)
        elif agg_func == "max":
            result[key] = max(values)

    return result


def brute_force_aggregate(
    records: List[Dict[str, Any]],
    group_keys: List[str],
    agg_col: str,
    agg_func: str,
) -> Dict[tuple, float]:
    """Brute-force nested-loop aggregation (for verification)."""
    result = {}

    for record in records:
        key = tuple(record[k] for k in group_keys)

        if key not in result:
            if agg_func == "count":
                result[key] = 0
            else:
                result[key] = None

        if agg_func == "sum":
            result[key] = (result[key] or 0) + record[agg_col]
        elif agg_func == "mean":
            # Accumulate sum and count
            if result[key] is None:
                result[key] = {"sum": 0, "count": 0}
            result[key]["sum"] += record[agg_col]
            result[key]["count"] += 1
        elif agg_func == "count":
            result[key] += 1
        elif agg_func == "min":
            if result[key] is None:
                result[key] = record[agg_col]
            else:
                result[key] = min(result[key], record[agg_col])
        elif agg_func == "max":
            if result[key] is None:
                result[key] = record[agg_col]
            else:
                result[key] = max(result[key], record[agg_col])

    # Post-process mean
    if agg_func == "mean":
        result = {k: v["sum"] / v["count"] for k, v in result.items()}

    return result


if __name__ == "__main__":
    # Plant records
    records = [
        {"category": "A", "region": "US", "value": 10},
        {"category": "A", "region": "US", "value": 20},
        {"category": "A", "region": "EU", "value": 15},
        {"category": "B", "region": "US", "value": 5},
        {"category": "B", "region": "EU", "value": 25},
        {"category": "B", "region": "EU", "value": 30},
    ]

    # Test sum
    result_sum = group_by_aggregate(records, ["category", "region"], "value", "sum")
    brute_sum = brute_force_aggregate(records, ["category", "region"], "value", "sum")
    assert result_sum == brute_sum, f"Sum mismatch: {result_sum} vs {brute_sum}"

    # Test mean
    result_mean = group_by_aggregate(records, ["category"], "value", "mean")
    brute_mean = brute_force_aggregate(records, ["category"], "value", "mean")
    assert result_mean == brute_mean, f"Mean mismatch: {result_mean} vs {brute_mean}"

    # Test count
    result_count = group_by_aggregate(records, ["region"], "value", "count")
    brute_count = brute_force_aggregate(records, ["region"], "value", "count")
    assert result_count == brute_count, f"Count mismatch: {result_count} vs {brute_count}"

    # Test min/max
    result_min = group_by_aggregate(records, ["category"], "value", "min")
    brute_min = brute_force_aggregate(records, ["category"], "value", "min")
    assert result_min == brute_min, f"Min mismatch: {result_min} vs {brute_min}"

    print(
        f"Sum (cat, region): {result_sum} | Mean (cat): {result_mean} | "
        f"Count (region): {result_count} | Min (cat): {result_min} | PASS"
    )
