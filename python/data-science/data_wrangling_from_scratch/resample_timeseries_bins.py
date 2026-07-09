"""
Resample Time Series: Bucketing and Aggregation.

Bucket timestamps into time bins (hourly, daily) and aggregate values.
We verify that bin sums equal brute-force per-bin computation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def parse_timestamp(ts: str) -> tuple:
    """Parse YYYY-MM-DD HH:MM format to (year, month, day, hour)."""
    date_part, time_part = ts.split(" ")
    year, month, day = map(int, date_part.split("-"))
    hour, minute = map(int, time_part.split(":"))
    return (year, month, day, hour)


def bucket_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
    """Bucket records by hour and sum values."""
    buckets = {}

    for record in records:
        ts = record["timestamp"]
        year, month, day, hour = parse_timestamp(ts)
        bin_key = (year, month, day, hour)

        if bin_key not in buckets:
            buckets[bin_key] = 0

        buckets[bin_key] += record["value"]

    return buckets


def bucket_daily(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
    """Bucket records by day and sum values."""
    buckets = {}

    for record in records:
        ts = record["timestamp"]
        year, month, day, _ = parse_timestamp(ts)
        bin_key = (year, month, day)

        if bin_key not in buckets:
            buckets[bin_key] = 0

        buckets[bin_key] += record["value"]

    return buckets


def brute_force_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
    """Brute-force hourly bucketing for verification."""
    result = {}

    for record in records:
        ts = record["timestamp"]
        year, month, day, hour = parse_timestamp(ts)
        bin_key = (year, month, day, hour)

        count = sum(1 for r in records if parse_timestamp(r["timestamp"]) == (year, month, day, hour))
        total = sum(r["value"] for r in records if parse_timestamp(r["timestamp"]) == (year, month, day, hour))

        result[bin_key] = total

    return result


if __name__ == "__main__":
    # Plant time series data
    records = [
        {"timestamp": "2024-01-15 08:00", "value": 10},
        {"timestamp": "2024-01-15 08:15", "value": 5},
        {"timestamp": "2024-01-15 09:00", "value": 20},
        {"timestamp": "2024-01-16 08:00", "value": 15},
        {"timestamp": "2024-01-16 08:30", "value": 8},
    ]

    # Hourly bucketing
    hourly = bucket_hourly(records)
    brute_hourly = brute_force_hourly(records)

    # Verify hourly
    assert hourly == brute_hourly, (
        f"Hourly bucketing mismatch: {hourly} vs {brute_hourly}"
    )

    # Verify specific hourly buckets
    assert hourly[(2024, 1, 15, 8)] == 15, "Hour 8 on Jan 15 should sum to 15"
    assert hourly[(2024, 1, 15, 9)] == 20, "Hour 9 on Jan 15 should be 20"
    assert hourly[(2024, 1, 16, 8)] == 23, "Hour 8 on Jan 16 should sum to 23"

    # Daily bucketing
    daily = bucket_daily(records)

    # Verify daily
    assert daily[(2024, 1, 15)] == 35, "Jan 15 should sum to 35"
    assert daily[(2024, 1, 16)] == 23, "Jan 16 should sum to 23"

    # Verify total
    assert sum(daily.values()) == sum(r["value"] for r in records), (
        "Daily sum should equal record sum"
    )

    print(
        f"Records: {len(records)} | Hourly bins: {len(hourly)} | Daily bins: {len(daily)} | "
        f"Daily totals: {daily} | PASS"
    )
