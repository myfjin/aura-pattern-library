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
    """Demo burst traffic simulation with rate limiting."""
    print("=== Rate Limiter Demo ===")
    
    # Create rate limiter: 10 requests/second, burst capacity of 20
    limiter = RateLimiter(capacity=20.0, refill_rate=10.0)
    
    def simulate_requests(name: str, requests: int, delay: float = 0.0) -> None:
        """Simulate a burst of requests."""
        print(f"\n{name}: Starting burst of {requests} requests")
        
        allowed = 0
        denied = 0
        
        for i in range(requests):
            if limiter.consume("demo_key"):
                allowed += 1
                status = "ALLOWED"
            else:
                denied += 1
                status = "DENIED"
                
            print(f"{name} - Request {i+1:2d}: {status}")
            
            if delay > 0:
                time.sleep(delay)
        
        print(f"{name}: Allowed: {allowed}, Denied: {denied}")
        
        # Show current stats
        stats = limiter.get_stats("demo_key")
        print(f"{name}: Remaining tokens: {stats['tokens']:.2f}")
    
    # Simulate initial burst (should mostly be allowed due to burst capacity)
    simulate_requests("Burst 1", 15, 0.01)
    
    # Wait for partial refill
    print("\n--- Waiting 1 second for partial refill ---")
    time.sleep(1.0)
    
    # Simulate another burst
    simulate_requests("Burst 2", 12, 0.01)
    
    # Show when requests will be allowed again
    remaining = limiter.remaining_time("demo_key", 5.0)
    print(f"\nTime until 5 tokens available: {remaining:.2f} seconds")
    
    # Wait and try again
    print(f"\n--- Waiting {remaining:.2f} seconds ---")
    time.sleep(remaining)
    
    if limiter.consume("demo_key", 5.0):
        print("Successfully consumed 5 tokens after waiting")
    else:
        print("Failed to consume 5 tokens")
    
    # Reset and show final stats
    stats = limiter.get_stats("demo_key")
    print(f"\nFinal stats: {stats}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()