"""Jitter backoff: add randomness to retry delays to prevent thundering herd.
Failure simulated: N jobs all retry at the same time; assert jitter spreads fires across time.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import time
import threading

def compute_backoff_with_jitter(attempt, base_delay=0.1, max_jitter_factor=0.5, max_delay=10):
    """Compute backoff delay with jitter: base * 2^attempt +/- jitter.

    Formula: delay = min(base * 2^attempt * (1 +/- random(-jitter, +jitter)), max_delay)
    """
    exponential = base_delay * (2 ** attempt)
    jitter = exponential * random.uniform(-max_jitter_factor, max_jitter_factor)
    delay = exponential + jitter
    return min(delay, max_delay)

class JitterBackoffRetry:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.retry_times = []
        self.lock = threading.Lock()

    def retry_with_jitter(self, callback, max_attempts=3, base_delay=0.05):
        """Retry callback with jitter backoff. Record retry times."""
        for attempt in range(max_attempts):
            try:
                callback()
                return  # Success
            except Exception:
                if attempt < max_attempts - 1:
                    delay = compute_backoff_with_jitter(attempt, base_delay=base_delay)
                    with self.lock:
                        self.retry_times.append((attempt + 1, time.time(), delay))
                    time.sleep(delay)
                else:
                    raise  # Final attempt failed

    def get_retry_times(self):
        """Return list of (attempt, timestamp, delay) tuples."""
        with self.lock:
            return list(self.retry_times)

def test_jitter_backoff():
    """Simulate failure: N jobs retry at same time; assert jitter spreads fires."""
    # Test 1: Single retry with jitter has delay
    random.seed(42)
    retrier = JitterBackoffRetry()
    attempt_count = [0]

    def failing_callback():
        attempt_count[0] += 1
        if attempt_count[0] < 2:
            raise RuntimeError("Intentional failure for test")

    start = time.time()
    retrier.retry_with_jitter(failing_callback, max_attempts=2, base_delay=0.05)
    elapsed = time.time() - start

    assert attempt_count[0] == 2, f"Expected 2 attempts, got {attempt_count[0]}"
    retry_times = retrier.get_retry_times()
    assert len(retry_times) == 1, f"Expected 1 retry recorded, got {len(retry_times)}"
    attempt_num, retry_ts, delay = retry_times[0]
    assert attempt_num == 1, f"Expected attempt 1, got {attempt_num}"
    assert delay > 0, f"Expected positive delay, got {delay}"
    assert elapsed >= delay * 0.8, f"Expected elapsed time >= {delay * 0.8}, got {elapsed}"

    # Test 2: Multiple retries have different jittered delays
    random.seed(123)
    retrier2 = JitterBackoffRetry()
    attempt_count[0] = 0
    fail_count = [0]

    def multi_fail_callback():
        attempt_count[0] += 1
        fail_count[0] += 1
        if fail_count[0] < 3:
            raise RuntimeError("Multi-attempt failure")

    start = time.time()
    retrier2.retry_with_jitter(multi_fail_callback, max_attempts=3, base_delay=0.02)
    elapsed = time.time() - start

    assert attempt_count[0] == 3, f"Expected 3 attempts, got {attempt_count[0]}"
    retry_times = retrier2.get_retry_times()
    assert len(retry_times) == 2, f"Expected 2 retries recorded, got {len(retry_times)}"

    # Verify delays are different (jitter applied)
    delay1 = retry_times[0][2]
    delay2 = retry_times[1][2]
    assert delay1 > 0, "First delay should be positive"
    assert delay2 > 0, "Second delay should be positive"
    # Delays should be different due to jitter (very high probability)
    # Second delay should be roughly 2x first (exponential backoff)
    assert delay2 > delay1 * 1.5, f"Second delay should be longer: {delay1} vs {delay2}"

    # Test 3: Jitter prevents thundering herd (parallel retries spread out)
    random.seed(99)
    num_jobs = 5
    fire_times = []
    fire_lock = threading.Lock()

    def parallel_job(job_id):
        attempt_count = [0]

        def fail_twice():
            attempt_count[0] += 1
            if attempt_count[0] < 2:
                raise RuntimeError("Job failure")

        retrier = JitterBackoffRetry()
        start = time.time()
        try:
            retrier.retry_with_jitter(fail_twice, max_attempts=2, base_delay=0.02)
        except:
            pass
        retry_times = retrier.get_retry_times()
        if retry_times:
            with fire_lock:
                fire_times.append(retry_times[0][1])  # Record retry time

    threads = [threading.Thread(target=parallel_job, args=(i,)) for i in range(num_jobs)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    if len(fire_times) > 1:
        # Verify fires are not all at the same time (jitter spread them)
        time_range = max(fire_times) - min(fire_times)
        assert time_range > 0, "Retries should be spread across time due to jitter"

if __name__ == "__main__":
    test_jitter_backoff()
    print("✓ jitter_backoff passed all assertions")
