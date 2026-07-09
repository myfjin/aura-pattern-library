"""Retry with backoff: exponential backoff for failed operations.
Failure simulated: callback fails N times; assert retry delays grow exponentially.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import random

def retry_with_exponential_backoff(callback, max_attempts=3, initial_delay=0.1, max_delay=10):
    """Retry callback with exponential backoff: delay = initial * 2^attempt (capped).

    Returns (success, attempts, total_delay).
    """
    total_delay = 0
    last_exception = None

    for attempt in range(max_attempts):
        try:
            callback()
            return (True, attempt + 1, total_delay)
        except Exception as e:
            last_exception = e
            if attempt < max_attempts - 1:
                # Calculate delay: initial_delay * 2^attempt, cap at max_delay
                delay = min(initial_delay * (2 ** attempt), max_delay)
                time.sleep(delay)
                total_delay += delay

    # All attempts failed
    return (False, max_attempts, total_delay)

def test_retry_with_backoff():
    """Simulate failure: callback fails N times; assert retry delays grow."""
    # Test 1: Callback fails then succeeds on retry
    attempt_count = [0]
    attempt_times = []

    def fail_once():
        attempt_times.append(time.time())
        attempt_count[0] += 1
        if attempt_count[0] < 2:
            raise ValueError("First attempt fails")

    start = time.time()
    success, attempts, total_delay = retry_with_exponential_backoff(
        fail_once,
        max_attempts=3,
        initial_delay=0.05
    )
    elapsed = time.time() - start

    assert success, "Should succeed on second attempt"
    assert attempts == 2, f"Expected 2 attempts, got {attempts}"
    assert total_delay > 0.04, f"Should have delay, got {total_delay}"
    assert elapsed >= total_delay * 0.8, f"Elapsed {elapsed} should be >= {total_delay * 0.8}"

    # Test 2: Exponential backoff grows correctly (no random)
    attempt_times = []

    def fail_three_times():
        attempt_times.append(time.time())
        raise ValueError("Always fails")

    success, attempts, total_delay = retry_with_exponential_backoff(
        fail_three_times,
        max_attempts=4,
        initial_delay=0.05,
        max_delay=10
    )

    assert not success, "Should fail after all attempts"
    assert attempts == 4, f"Expected 4 attempts, got {attempts}"
    # Total delay should be 0.05 + 0.1 + 0.2 = 0.35 (approximately)
    assert 0.3 <= total_delay <= 0.5, f"Delays should sum to ~0.35, got {total_delay}"

    # Verify timing increases between retries
    intervals = []
    for i in range(1, len(attempt_times)):
        interval = attempt_times[i] - attempt_times[i - 1]
        intervals.append(interval)

    # First interval ~0.05, second ~0.1, third ~0.2
    assert len(intervals) >= 2, "Should have multiple intervals"
    assert intervals[1] > intervals[0], f"Delays should grow: {intervals[0]} -> {intervals[1]}"
    if len(intervals) > 2:
        assert intervals[2] > intervals[1], f"Delays should grow: {intervals[1]} -> {intervals[2]}"

    # Test 3: Max delay cap is respected
    attempt_count[0] = 0

    def always_fail():
        attempt_count[0] += 1
        raise ValueError("Persistent failure")

    success, attempts, total_delay = retry_with_exponential_backoff(
        always_fail,
        max_attempts=5,
        initial_delay=0.05,
        max_delay=0.15  # Cap delays at 0.15
    )

    assert not success, "Should fail"
    # Delays: 0.05 + 0.1 + 0.15 + 0.15 = 0.45 (capped at max_delay)
    assert total_delay <= 0.5, f"Should respect max_delay cap, got {total_delay}"

    # Test 4: Single attempt (no retries)
    attempt_count[0] = 0

    def fail_immediately():
        attempt_count[0] += 1
        raise ValueError("Fails immediately")

    success, attempts, total_delay = retry_with_exponential_backoff(
        fail_immediately,
        max_attempts=1,
        initial_delay=0.1
    )

    assert not success, "Should fail"
    assert attempts == 1, f"Expected 1 attempt, got {attempts}"
    assert total_delay == 0, f"No retries means no delay, got {total_delay}"

    # Test 5: Success on first attempt (no backoff needed)
    attempt_count[0] = 0

    def succeeds_immediately():
        attempt_count[0] += 1
        return "success"

    start = time.time()
    success, attempts, total_delay = retry_with_exponential_backoff(
        succeeds_immediately,
        max_attempts=3,
        initial_delay=0.1
    )
    elapsed = time.time() - start

    assert success, "Should succeed"
    assert attempts == 1, f"Expected 1 attempt, got {attempts}"
    assert total_delay == 0, f"No retries means no delay, got {total_delay}"
    assert elapsed < 0.1, f"Should run without delay, took {elapsed}s"

if __name__ == "__main__":
    test_retry_with_backoff()
    print("✓ retry_with_backoff passed all assertions")
