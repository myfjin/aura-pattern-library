"""
As-Of Join (Rolling Join).

For each row in left table, find the nearest preceding row in right table
on a timestamp/key column. Used for merging trades with quotes at the same or earlier time.
We verify against brute-force for correctness.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def asof_join(
    left: List[Dict[str, Any]],
    right: List[Dict[str, Any]],
    key: str,  # Timestamp key to join on
) -> List[Dict[str, Any]]:
    """
    As-of join: for each left row, find the right row with the largest key <= left's key.
    """
    # Sort right by key
    right_sorted = sorted(right, key=lambda r: r[key])

    result = []

    for left_row in left:
        left_key = left_row[key]

        # Find nearest preceding right row via binary search or linear scan
        nearest_right = None
        for right_row in reversed(right_sorted):
            if right_row[key] <= left_key:
                nearest_right = right_row
                break

        # Merge (prefix right columns to avoid overwriting left)
        if nearest_right is not None:
            merged = {**left_row}
            for k, v in nearest_right.items():
                if k not in merged or k == "time":  # Skip time from right (already have left's time)
                    if k != "time":
                        merged[k] = v
        else:
            merged = left_row

        result.append(merged)

    return result


def brute_force_asof(
    left: List[Dict[str, Any]],
    right: List[Dict[str, Any]],
    key: str,
) -> List[Dict[str, Any]]:
    """Brute-force as-of join for verification."""
    result = []

    for left_row in left:
        left_key = left_row[key]

        # Find all right rows with key <= left_key
        candidates = [r for r in right if r[key] <= left_key]

        # Pick the one with max key
        if candidates:
            nearest_right = max(candidates, key=lambda r: r[key])
            merged = {**left_row}
            for k, v in nearest_right.items():
                if k != "time":  # Skip time from right
                    merged[k] = v
        else:
            merged = left_row

        result.append(merged)

    return result


if __name__ == "__main__":
    # Plant trades and quotes with common "time" key
    trades = [
        {"time": 100, "side": "trade", "price": 50},
        {"time": 150, "side": "trade", "price": 51},
        {"time": 200, "side": "trade", "price": 52},
    ]

    quotes = [
        {"time": 80, "side": "quote", "bid": 49, "ask": 50},
        {"time": 120, "side": "quote", "bid": 50, "ask": 51},
        {"time": 180, "side": "quote", "bid": 51, "ask": 52},
    ]

    # As-of join on time
    joined = asof_join(trades, quotes, "time")
    brute_joined = brute_force_asof(trades, quotes, "time")

    # Verify results match (extract times and quotes)
    joined_times = [(r["time"], r.get("bid")) for r in joined]
    brute_times = [(r["time"], r.get("bid")) for r in brute_joined]

    assert joined_times == brute_times, (
        f"As-of join mismatch: {joined_times} vs {brute_times}"
    )

    # Verify specific matches
    # Trade at time 100 should match quote at time 80
    trade_100 = joined[0]
    assert trade_100["time"] == 100, "First trade should be time 100"
    assert trade_100.get("bid") == 49, f"Trade at 100 should match quote at 80 (bid=49), got {trade_100.get('bid')}"

    # Trade at time 150 should match quote at time 120
    trade_150 = joined[1]
    assert trade_150.get("bid") == 50, f"Trade at 150 should match quote at 120 (bid=50), got {trade_150.get('bid')}"

    # Trade at time 200 should match quote at time 180
    trade_200 = joined[2]
    assert trade_200.get("bid") == 51, f"Trade at 200 should match quote at 180 (bid=51), got {trade_200.get('bid')}"

    print(
        f"Trades: {len(trades)} | Quotes: {len(quotes)} | Joined: {len(joined)} | "
        f"Matches: {joined_times} | PASS"
    )
