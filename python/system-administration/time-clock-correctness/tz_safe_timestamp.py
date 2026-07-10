"""Safe timezone-aware timestamp handling without DST confusion."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from datetime import datetime, timedelta, timezone


class TZSafeConverter:
    """Convert timestamps safely between timezones using UTC as intermediary."""

    @staticmethod
    def to_utc_seconds(dt):
        """Convert datetime to UTC epoch seconds (ISO 8601 compliant)."""
        if dt.tzinfo is None:
            raise ValueError("Timestamp must be timezone-aware")
        return dt.timestamp()

    @staticmethod
    def from_utc_seconds(epoch_seconds, target_tz=None):
        """Convert UTC epoch seconds to datetime in target timezone."""
        if target_tz is None:
            target_tz = timezone.utc
        return datetime.fromtimestamp(epoch_seconds, tz=target_tz)

    @staticmethod
    def round_trip(dt, target_tz):
        """Convert UTC -> target TZ -> back to UTC. Assert no precision loss."""
        utc_seconds = TZSafeConverter.to_utc_seconds(dt)
        converted = TZSafeConverter.from_utc_seconds(utc_seconds, target_tz)
        back_to_utc = TZSafeConverter.to_utc_seconds(converted)

        # ASSERT: round-trip preserves exact second (no DST corruption)
        if utc_seconds != back_to_utc:
            raise AssertionError(
                f"Round-trip precision loss: {utc_seconds} -> {back_to_utc}"
            )

        return True


def test_round_trip_preserves_epoch():
    """Test: round-trip through timezone does not corrupt epoch time."""
    # Start with a UTC time (Jan 2, 2026, 12:34:56 UTC)
    original_dt = datetime(2026, 1, 2, 12, 34, 56, tzinfo=timezone.utc)

    # Convert to fixed offset timezone (+5 hours)
    tz_plus5 = timezone(timedelta(hours=5))

    # ASSERT: round-trip preserves exact epoch second
    assert TZSafeConverter.round_trip(original_dt, tz_plus5) is True


def test_reject_naive_datetime():
    """Test: reject naive (tz-unaware) datetime."""
    naive_dt = datetime(2026, 1, 2, 12, 34, 56)

    try:
        TZSafeConverter.to_utc_seconds(naive_dt)
        assert False, "Should reject naive datetime"
    except ValueError as e:
        assert "timezone-aware" in str(e)


def test_multiple_tz_conversions():
    """Test: multiple TZ conversions maintain precision."""
    dt = datetime(2026, 6, 15, 3, 0, 0, tzinfo=timezone.utc)
    original_epoch = dt.timestamp()

    tz_minus8 = timezone(timedelta(hours=-8))
    tz_plus12 = timezone(timedelta(hours=12))

    # Convert through multiple timezones
    epoch1 = TZSafeConverter.to_utc_seconds(
        TZSafeConverter.from_utc_seconds(original_epoch, tz_minus8)
    )
    epoch2 = TZSafeConverter.to_utc_seconds(
        TZSafeConverter.from_utc_seconds(original_epoch, tz_plus12)
    )

    # ASSERT: both preserve the original epoch
    assert epoch1 == original_epoch
    assert epoch2 == original_epoch


if __name__ == "__main__":
    test_round_trip_preserves_epoch()
    test_reject_naive_datetime()
    test_multiple_tz_conversions()
    print("✓ tz_safe_timestamp passed")
