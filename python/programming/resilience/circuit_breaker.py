# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading
from enum import Enum
from typing import Callable, Any, Optional
from functools import wraps


class CircuitState(Enum):
    """Enumeration of possible circuit breaker states."""
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"


class CircuitBreakerError(Exception):
    """Base exception for circuit breaker errors."""
    pass


class CircuitOpenError(CircuitBreakerError):
    """Exception raised when the circuit is open."""
    pass


class CircuitBreaker:
    """
    A circuit breaker implementation to prevent cascading failures.
    
    The circuit breaker has three states:
    - CLOSED: Normal operation, requests are allowed
    - OPEN: Failure threshold exceeded, requests are blocked
    - HALF_OPEN: Recovery state, limited requests are allowed to test availability
    """
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        expected_exception: type = Exception,
        name: str = "default"
    ):
        """
        Initialize the circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening the circuit
            recovery_timeout: Time in seconds before attempting recovery
            expected_exception: Exception type that triggers failure counting
            name: Name for identification in logs
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        self.name = name
        
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time: Optional[float] = None
        self._lock = threading.RLock()
    
    def __call__(self, func: Callable) -> Callable:
        """
        Decorator to wrap a function with the circuit breaker.
        
        Args:
            func: Function to wrap
            
        Returns:
            Wrapped function with circuit breaker protection
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return self.call(func, *args, **kwargs)
        return wrapper
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute a function with circuit breaker protection.
        
        Args:
            func: Function to execute
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            Result of the function call
            
        Raises:
            CircuitOpenError: If the circuit is open
            Exception: Any exception raised by the wrapped function
        """
        with self._lock:
            if self.state == CircuitState.OPEN:
                if self._should_attempt_reset():
                    self._transition_to_half_open()
                else:
                    raise CircuitOpenError(f"Circuit '{self.name}' is OPEN")
            
            if self.state == CircuitState.HALF_OPEN:
                return self._execute_half_open(func, *args, **kwargs)
            else:  # CLOSED state
                return self._execute_closed(func, *args, **kwargs)
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt recovery."""
        if self.last_failure_time is None:
            return False
        return time.time() - self.last_failure_time >= self.recovery_timeout
    
    def _transition_to_half_open(self) -> None:
        """Transition the circuit to HALF_OPEN state."""
        self.state = CircuitState.HALF_OPEN
        print(f"[CircuitBreaker {self.name}] Transitioned to HALF_OPEN")
    
    def _transition_to_open(self) -> None:
        """Transition the circuit to OPEN state."""
        self.state = CircuitState.OPEN
        self.last_failure_time = time.time()
        print(f"[CircuitBreaker {self.name}] Transitioned to OPEN")
    
    def _transition_to_closed(self) -> None:
        """Transition the circuit to CLOSED state."""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
        print(f"[CircuitBreaker {self.name}] Transitioned to CLOSED")
    
    def _execute_closed(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function when circuit is CLOSED.
        
        Args:
            func: Function to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            Function result
            
        Raises:
            Exception: Any exception from the function
        """
        try:
            result = func(*args, **kwargs)
            return result
        except self.expected_exception as e:
            self._handle_failure()
            raise e
    
    def _execute_half_open(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function when circuit is HALF_OPEN.
        
        Args:
            func: Function to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            Function result
            
        Raises:
            Exception: Any exception from the function
        """
        try:
            result = func(*args, **kwargs)
            self._transition_to_closed()
            return result
        except self.expected_exception as e:
            self._transition_to_open()
            raise e
    
    def _handle_failure(self) -> None:
        """Handle a failure by incrementing count and potentially opening circuit."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        print(f"[CircuitBreaker {self.name}] Failure {self.failure_count}/{self.failure_threshold}")
        
        if self.failure_count >= self.failure_threshold:
            self._transition_to_open()
    
    @property
    def is_closed(self) -> bool:
        """Check if circuit is in CLOSED state."""
        return self.state == CircuitState.CLOSED
    
    @property
    def is_open(self) -> bool:
        """Check if circuit is in OPEN state."""
        return self.state == CircuitState.OPEN
    
    @property
    def is_half_open(self) -> bool:
        """Check if circuit is in HALF_OPEN state."""
        return self.state == CircuitState.HALF_OPEN
    
    def __str__(self) -> str:
        """String representation of the circuit breaker."""
        return (f"CircuitBreaker(name={self.name}, state={self.state.value}, "
                f"failures={self.failure_count}/{self.failure_threshold})")


if __name__ == "__main__":
    # Self-test on a fake clock: full lifecycle CLOSED→OPEN→HALF_OPEN→
    # (CLOSED on success | OPEN on failure), fail-fast without calling.
    _now = [40_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=5.0,
                                 name="test")
        calls = {"n": 0}

        @breaker
        def service(fail: bool) -> str:
            calls["n"] += 1
            if fail:
                raise ConnectionError("down")
            return "ok"

        # CLOSED: successes flow through, failures count.
        assert service(False) == "ok" and breaker.is_closed
        for i in range(3):
            try:
                service(True)
            except ConnectionError:
                pass
        assert breaker.is_open, f"3 failures at threshold 3 must OPEN, state {breaker.state}"
        assert breaker.failure_count == 3

        # OPEN: fail-fast — the service is NOT called.
        before = calls["n"]
        try:
            service(False)
            assert False, "OPEN breaker executed the call"
        except CircuitOpenError:
            pass
        assert calls["n"] == before, "OPEN breaker still invoked the service"

        # HALF_OPEN after recovery timeout; a FAILURE re-opens immediately.
        _now[0] += 5.1
        try:
            service(True)
        except ConnectionError:
            pass
        assert breaker.is_open, "failed half-open probe must re-OPEN"

        # HALF_OPEN again; a SUCCESS closes and resets the failure count.
        _now[0] += 5.1
        assert service(False) == "ok"
        assert breaker.is_closed, "successful half-open probe must CLOSE"
        assert breaker.failure_count == 0, \
            f"failure count must reset on close, got {breaker.failure_count}"

        # After closing, the breaker needs a fresh threshold of failures.
        for i in range(2):
            try:
                service(True)
            except ConnectionError:
                pass
        assert breaker.is_closed, "breaker opened below the threshold after reset"
        assert calls["n"] == 8, f"service must have run exactly 8 times, ran {calls['n']}"

        # Unexpected exception types pass through without tripping the breaker.
        plain = CircuitBreaker(failure_threshold=1, expected_exception=ConnectionError)
        def type_error():
            raise TypeError("not counted")
        try:
            plain.call(type_error)
        except TypeError:
            pass
        assert plain.is_closed, "non-expected exception tripped the breaker"
    finally:
        time.time = _real_time

    print("circuit_breaker: 3 fails→OPEN, fail-fast verified (no call), "
          "half-open fail re-OPENs / success CLOSES+resets, 8 calls exact — PASS")