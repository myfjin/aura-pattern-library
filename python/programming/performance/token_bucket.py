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
    """Demo the rate limiter functionality."""
    print("Token Bucket Rate Limiter Demo")
    print("=" * 40)
    
    # Create a rate limiter allowing 5 requests per second with burst capacity of 10
    limiter = RateLimiter(capacity=10, refill_rate=5.0)
    
    print(f"Rate limiter created: {limiter.bucket.capacity} capacity, "
          f"{limiter.bucket.refill_rate}/sec refill rate")
    
    # Test immediate consumption
    print("\n1. Testing immediate consumption:")
    for i in range(5):
        success, wait = limiter.try_acquire()
        print(f"   Request {i+1}: {'Allowed' if success else 'Denied'}, "
              f"Wait: {wait:.3f}s, Available: {limiter.available_permits():.1f}")
    
    # Test burst behavior
    print("\n2. Testing burst behavior:")
    time.sleep(1.0)  # Let bucket refill
    print(f"   After 1s wait, available permits: {limiter.available_permits():.1f}")
    
    # Try to consume more than capacity
    print("\n3. Testing burst limit:")
    for i in range(12):
        success, wait = limiter.try_acquire()
        status = 'Allowed' if success else 'Denied'
        print(f"   Burst request {i+1}: {status}, "
              f"Wait: {wait:.3f}s, Available: {limiter.available_permits():.1f}")
    
    # Test waiting behavior
    print("\n4. Testing automatic wait:")
    time.sleep(2.0)  # Accumulate tokens
    print(f"   After 2s wait, available permits: {limiter.available_permits():.1f}")
    
    # Acquire multiple tokens
    success = limiter.acquire(3)
    print(f"   Acquired 3 tokens: {'Success' if success else 'Failed'}, "
          f"Remaining: {limiter.available_permits():.1f}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()