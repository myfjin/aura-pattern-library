"""Cron expression parser: calculate next fire time exactly.
Failure simulated: parse a cron expression and compute the EXACT next fire timestamp.
Assert: next_fire() produces the expected timestamp for known inputs.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import datetime

def next_fire(cron_expr, from_time=None):
    """Parse cron (minute hour day month dow) and return next fire timestamp.
    Raises ValueError if the expression is invalid.
    """
    if from_time is None:
        from_time = time.time()

    parts = cron_expr.split()
    if len(parts) != 5:
        raise ValueError(f"Invalid cron expression: {cron_expr}")

    minute_str, hour_str, day_str, month_str, dow_str = parts

    # Parse each field (simplified: only * and specific numbers, no ranges/steps)
    def parse_field(field_str, min_val, max_val):
        if field_str == '*':
            return list(range(min_val, max_val + 1))
        try:
            val = int(field_str)
            if min_val <= val <= max_val:
                return [val]
            else:
                raise ValueError(f"Value {val} out of range [{min_val}, {max_val}]")
        except ValueError:
            raise ValueError(f"Invalid field: {field_str}")

    minutes = parse_field(minute_str, 0, 59)
    hours = parse_field(hour_str, 0, 23)
    days = parse_field(day_str, 1, 31)
    months = parse_field(month_str, 1, 12)
    dows = parse_field(dow_str, 0, 6)  # 0=Sunday, 6=Saturday

    # Find next fire by brute-force search within next 4 years (reasonable limit)
    current_dt = datetime.datetime.fromtimestamp(from_time)
    search_end = current_dt + datetime.timedelta(days=1461)  # ~4 years

    # Start from next minute boundary
    check_dt = current_dt.replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)

    while check_dt <= search_end:
        if (check_dt.minute in minutes and
            check_dt.hour in hours and
            check_dt.day in days and
            check_dt.month in months and
            check_dt.weekday() in [(d - 1) % 7 for d in dows]):  # Convert cron dow to Python weekday
            return check_dt.timestamp()
        check_dt += datetime.timedelta(minutes=1)

    raise ValueError("No fire time found within search window")

def test_cron_next_fire():
    """Simulate a cron parse failure scenario: verify exact next-fire computation."""
    # Test 1: Every minute (0 0 * * *) — next fire should be the next hour boundary
    base_time = datetime.datetime(2024, 3, 15, 10, 30, 45).timestamp()
    next_ts = next_fire("0 0 * * *", base_time)
    expected_dt = datetime.datetime(2024, 3, 16, 0, 0, 0)
    assert next_ts == expected_dt.timestamp(), f"Expected {expected_dt.timestamp()}, got {next_ts}"

    # Test 2: Specific hour/minute (30 14 * * *) — 2:30 PM every day
    base_time = datetime.datetime(2024, 3, 15, 10, 0, 0).timestamp()
    next_ts = next_fire("30 14 * * *", base_time)
    expected_dt = datetime.datetime(2024, 3, 15, 14, 30, 0)
    assert next_ts == expected_dt.timestamp(), f"Expected {expected_dt.timestamp()}, got {next_ts}"

    # Test 3: Invalid cron expression (too few fields)
    try:
        next_fire("0 0 *", base_time)
        assert False, "Should have raised ValueError for invalid cron"
    except ValueError as e:
        assert "Invalid cron" in str(e), f"Unexpected error message: {e}"

    # Test 4: Next fire within the same hour
    base_time = datetime.datetime(2024, 3, 15, 14, 25, 0).timestamp()
    next_ts = next_fire("30 14 * * *", base_time)
    expected_dt = datetime.datetime(2024, 3, 15, 14, 30, 0)
    assert next_ts == expected_dt.timestamp(), f"Expected {expected_dt.timestamp()}, got {next_ts}"

    # Test 5: Parse error on out-of-range value
    try:
        next_fire("60 * * * *", base_time)
        assert False, "Should have raised ValueError for out-of-range minute"
    except ValueError as e:
        assert "Invalid field" in str(e) or "out of range" in str(e), f"Unexpected error message: {e}"

if __name__ == "__main__":
    test_cron_next_fire()
    print("✓ cron_expr_next_fire passed all assertions")
