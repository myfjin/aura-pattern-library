# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading
from typing import Optional, Tuple
from collections import deque


class TokenBucket:
    """A token bucket implementation for rate limiting."""
    
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the token bucket.
        
        Args:
            capacity: Maximum number of tokens the bucket can hold
            refill_rate: Number of tokens added per second
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be positive")
            
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()
        self._lock = threading.RLock()
    
    def _refill(self) -> None:
        """Refill tokens based on time elapsed since last refill."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        if elapsed > 0:
            new_tokens = elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_refill = now
    
    def consume(self, tokens: int = 1) -> Tuple[bool, float]:
        """
        Attempt to consume tokens from the bucket.
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            Tuple of (success, wait_time_seconds)
            success: True if tokens were consumed, False otherwise
            wait_time_seconds: Time to wait before enough tokens are available
        """
        if tokens <= 0:
            raise ValueError("Tokens to consume must be positive")
        if tokens > self.capacity:
            # Impossible to satisfy this request
            return False, float('inf')
            
        with self._lock:
            self._refill()
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True, 0.0
            else:
                # Calculate time needed to accumulate enough tokens
                needed = tokens - self.tokens
                wait_time = needed / self.refill_rate
                return False, wait_time
    
    def peek(self) -> float:
        """
        Check current token count without consuming tokens.
        
        Returns:
            Current number of tokens in the bucket
        """
        with self._lock:
            self._refill()
            return self.tokens


class RateLimiter:
    """A rate limiter using the token bucket algorithm."""
    
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the rate limiter.
        
        Args:
            capacity: Maximum number of requests allowed in burst
            refill_rate: Number of requests allowed per second
        """
        self.bucket = TokenBucket(capacity, refill_rate)
    
    def acquire(self, tokens: int = 1) -> bool:
        """
        Attempt to acquire tokens, waiting if necessary.
        
        Args:
            tokens: Number of tokens to acquire
            
        Returns:
            True if tokens were acquired, False if impossible
        """
        success, wait_time = self.bucket.consume(tokens)
        
        if success:
            return True
        elif wait_time == float('inf'):
            return False
        else:
            time.sleep(wait_time)
            # Try again after waiting
            success, _ = self.bucket.consume(tokens)
            return success
    
    def try_acquire(self, tokens: int = 1) -> Tuple[bool, float]:
        """
        Try to acquire tokens without blocking.
        
        Args:
            tokens: Number of tokens to acquire
            
        Returns:
            Tuple of (success, wait_time_seconds)
        """
        return self.bucket.consume(tokens)
    
    def available_permits(self) -> float:
        """
        Get the number of available permits.
        
        Returns:
            Number of available permits
        """
        return self.bucket.peek()


def main():
    """Self-test: refill math on a fake clock, denial on empty, cap enforcement."""
    # Deterministic fake clock — the bucket's arithmetic is under test, not the OS timer.
    _now = [1000.0]
    _real_monotonic = time.monotonic
    time.monotonic = lambda: _now[0]
    try:
        tb = TokenBucket(capacity=10, refill_rate=5.0)

        # Burst: a full bucket grants exactly its capacity.
        for i in range(10):
            ok, wait = tb.consume(1)
            assert ok and wait == 0.0, f"burst token {i + 1} should be granted instantly"

        # THE FAILURE: the 11th request hits an empty bucket and must be DENIED,
        # with the exact wait for 1 token at 5 tokens/s = 0.2s.
        ok, wait = tb.consume(1)
        assert not ok, "11th token granted from an empty bucket"
        assert abs(wait - 0.2) < 1e-9, f"wait for 1 token at 5/s must be 0.2s, got {wait}"

        # Refill math: +0.5s at 5 tokens/s = exactly 2.5 tokens.
        _now[0] += 0.5
        assert abs(tb.peek() - 2.5) < 1e-9, f"0.5s at 5/s must refill 2.5 tokens, got {tb.peek()}"
        ok, _ = tb.consume(2)
        assert ok, "2 tokens must be grantable from 2.5"
        assert abs(tb.peek() - 0.5) < 1e-9, f"2.5 - 2 must leave 0.5, got {tb.peek()}"

        # Cap: a long idle period never overfills past capacity.
        _now[0] += 100.0
        assert abs(tb.peek() - 10.0) < 1e-9, f"refill must cap at 10, got {tb.peek()}"

        # Impossible request (> capacity) is refused outright, not queued.
        ok, wait = tb.consume(11)
        assert not ok and wait == float("inf"), "request above capacity must be impossible"

        # Invalid construction/usage must be refused.
        for bad in ((0, 1.0), (10, 0.0), (-1, 5.0)):
            try:
                TokenBucket(*bad)
                assert False, f"TokenBucket{bad} accepted invalid arguments"
            except ValueError:
                pass
        try:
            tb.consume(0)
            assert False, "consume(0) accepted"
        except ValueError:
            pass

        # RateLimiter facade delegates to the same bucket.
        rl = RateLimiter(capacity=4, refill_rate=2.0)
        assert abs(rl.available_permits() - 4.0) < 1e-9
        assert rl.acquire(4) is True
        assert abs(rl.available_permits() - 0.0) < 1e-9
    finally:
        time.monotonic = _real_monotonic

    print("token_bucket: burst 10/10, deny-on-empty (wait 0.2s), refill 2.5@0.5s, cap held — PASS")


if __name__ == "__main__":
    main()