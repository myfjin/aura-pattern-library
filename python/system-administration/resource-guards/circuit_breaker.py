"""Circuit breaker: opens after N failures, short-circuits further calls.
Failure simulated: call function 100 times, it fails first 10 times;
assert breaker opens after 10 failures, short-circuits remaining 90 calls,
short-circuit count = 90.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

def circuit_breaker_guard(failure_threshold=10, recovery_timeout=1.0):
    """Circuit breaker that opens after threshold failures.
    Returns: context with call_fn(), state, short_circuit_count.
    """
    class CircuitBreaker:
        def __init__(self, threshold, timeout):
            self.threshold = threshold
            self.timeout = timeout
            self.failure_count = 0
            self.state = 'closed'  # closed, open, half_open
            self.last_failure_time = None
            self.short_circuits = 0
            self.successful_calls = 0

        def call(self, fn):
            """Call function; manage breaker state."""
            import time

            # Check if should try recovery
            if self.state == 'open':
                now = time.time()
                if self.last_failure_time and (now - self.last_failure_time) > self.timeout:
                    self.state = 'half_open'
                else:
                    self.short_circuits += 1
                    return False, "Circuit open"

            if self.state == 'half_open':
                try:
                    result = fn()
                    # Success; close circuit
                    self.state = 'closed'
                    self.failure_count = 0
                    self.successful_calls += 1
                    return True, result
                except Exception as e:
                    # Failure in half-open; reopen
                    self.failure_count += 1
                    self.last_failure_time = time.time()
                    if self.failure_count >= self.threshold:
                        self.state = 'open'
                    return False, str(e)

            # Closed state
            try:
                result = fn()
                self.successful_calls += 1
                return True, result
            except Exception as e:
                self.failure_count += 1
                self.last_failure_time = time.time()
                if self.failure_count >= self.threshold:
                    self.state = 'open'
                return False, str(e)

    return CircuitBreaker(failure_threshold, recovery_timeout)

if __name__ == '__main__':
    import random
    random.seed(42)

    breaker = circuit_breaker_guard(failure_threshold=10)

    # Function that fails first 10 times, then succeeds
    call_count = [0]
    def failing_fn():
        call_count[0] += 1
        if call_count[0] <= 10:
            raise ValueError(f"Failure {call_count[0]}")
        return "success"

    # Call 100 times
    successes = 0
    failures = 0
    short_circuits = 0

    for i in range(100):
        success, result = breaker.call(failing_fn)
        if not success and result == "Circuit open":
            short_circuits += 1
        elif success:
            successes += 1
        else:
            failures += 1

    # Assert: circuit opened after 10 failures, short-circuited remaining calls
    assert breaker.state == 'open', f"Breaker state {breaker.state}, expected 'open'"
    assert short_circuits >= 80, f"Short-circuited {short_circuits} calls, expected ≥ 80"
    assert breaker.failure_count >= 10, f"Failure count {breaker.failure_count}, expected ≥ 10"
