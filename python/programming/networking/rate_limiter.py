# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading
from typing import Optional, Dict, Any
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class TokenBucket:
    """Token bucket implementation for rate limiting."""
    capacity: float  # Maximum tokens the bucket can hold
    refill_rate: float  # Tokens added per second
    tokens: float  # Current token count
    last_refill: float  # Timestamp of last refill

    def __init__(self, capacity: float, refill_rate: float):
        """
        Initialize token bucket.
        
        Args:
            capacity: Maximum number of tokens
            refill_rate: Tokens per second to add to bucket
        """
        if capacity <= 0 or refill_rate <= 0:
            raise ValueError("Capacity and refill_rate must be positive")
            
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.monotonic()

    def refill(self) -> None:
        """Refill tokens based on time elapsed since last refill."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        
        if elapsed > 0:
            new_tokens = elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_refill = now

    def consume(self, tokens: float = 1.0) -> bool:
        """
        Try to consume tokens from the bucket.
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            True if tokens were consumed, False if not enough tokens
        """
        if tokens <= 0:
            raise ValueError("Tokens to consume must be positive")
            
        self.refill()
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def remaining_time(self, tokens: float = 1.0) -> float:
        """
        Calculate time needed to accumulate enough tokens.
        
        Args:
            tokens: Number of tokens needed
            
        Returns:
            Time in seconds until enough tokens are available
        """
        if tokens <= 0:
            raise ValueError("Tokens must be positive")
            
        self.refill()
        
        if self.tokens >= tokens:
            return 0.0
            
        needed = tokens - self.tokens
        return needed / self.refill_rate


class RateLimiter:
    """Rate limiter using token bucket algorithm with per-key limits."""
    
    def __init__(self, capacity: float, refill_rate: float):
        """
        Initialize rate limiter.
        
        Args:
            capacity: Maximum tokens per bucket
            refill_rate: Tokens per second to refill
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets: Dict[str, TokenBucket] = defaultdict(
            lambda: TokenBucket(capacity, refill_rate)
        )
        self._lock = threading.RLock()

    def consume(self, key: str, tokens: float = 1.0) -> bool:
        """
        Try to consume tokens for a key.
        
        Args:
            key: Identifier for the rate limit bucket
            tokens: Number of tokens to consume
            
        Returns:
            True if allowed, False if rate limited
        """
        with self._lock:
            return self.buckets[key].consume(tokens)

    def remaining_time(self, key: str, tokens: float = 1.0) -> float:
        """
        Get time until key can consume tokens again.
        
        Args:
            key: Identifier for the rate limit bucket
            tokens: Number of tokens needed
            
        Returns:
            Time in seconds until allowed
        """
        with self._lock:
            return self.buckets[key].remaining_time(tokens)

    def reset(self, key: str) -> None:
        """
        Reset the bucket for a key.
        
        Args:
            key: Identifier for the rate limit bucket
        """
        with self._lock:
            if key in self.buckets:
                del self.buckets[key]

    def get_stats(self, key: str) -> Dict[str, Any]:
        """
        Get statistics for a key's bucket.
        
        Args:
            key: Identifier for the rate limit bucket
            
        Returns:
            Dictionary with current stats
        """
        with self._lock:
            bucket = self.buckets[key]
            bucket.refill()  # Update token count
            return {
                "tokens": bucket.tokens,
                "capacity": bucket.capacity,
                "refill_rate": bucket.refill_rate,
                "last_refill": bucket.last_refill
            }


def main():
    """Self-test on a fake monotonic clock: burst capacity exact, refill
    arithmetic exact, per-key isolation, remaining_time computes the wait."""
    _now = [5_000.0]
    _real_monotonic = time.monotonic
    time.monotonic = lambda: _now[0]
    try:
        limiter = RateLimiter(capacity=20.0, refill_rate=10.0)

        # Burst: exactly the 20-token capacity is grantable, the 21st denied.
        granted = sum(1 for _ in range(25) if limiter.consume("k"))
        assert granted == 20, f"capacity-20 bucket granted {granted} in a burst"
        assert limiter.consume("k") is False, "empty bucket granted a token"

        # Refill: +0.5s at 10/s = 5 tokens, exactly 5 more grants.
        _now[0] += 0.5
        regrants = sum(1 for _ in range(10) if limiter.consume("k"))
        assert regrants == 5, f"0.5s at 10/s must refill exactly 5, granted {regrants}"

        # remaining_time: needing 5 tokens on an empty bucket at 10/s = 0.5s.
        wait = limiter.remaining_time("k", 5.0)
        assert abs(wait - 0.5) < 1e-9, f"wait for 5 tokens at 10/s must be 0.5s, got {wait}"
        _now[0] += wait
        assert limiter.consume("k", 5.0) is True, "tokens not available after the computed wait"

        # Refill never exceeds capacity.
        _now[0] += 1000
        stats = limiter.get_stats("k")
        assert stats["tokens"] == 20.0, f"refill overfilled: {stats['tokens']}"
        assert stats["capacity"] == 20.0 and stats["refill_rate"] == 10.0

        # Per-key isolation: draining key A leaves key B full.
        assert all(limiter.consume("a") for _ in range(20))
        assert limiter.consume("a") is False
        assert limiter.consume("b") is True, "key isolation broken: b affected by a"

        # Multi-token consume: 3 tokens leave capacity-3 exactly empty.
        limiter.reset("m")
        small = RateLimiter(capacity=3.0, refill_rate=1.0)
        assert small.consume("m", 3.0) is True
        assert small.consume("m", 0.5) is False, "over-consumed past capacity"

        # reset() restores a fresh full bucket.
        limiter.reset("a")
        assert limiter.consume("a") is True, "reset did not refill the bucket"
    finally:
        time.monotonic = _real_monotonic

    print("rate_limiter: burst 20/25 exact, +0.5s→5 tokens, wait 0.5s computed, "
          "cap held at 20, keys isolated — PASS")


if __name__ == "__main__":
    main()