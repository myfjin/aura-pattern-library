# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import signal
import threading
from typing import Any, Callable, Optional, Union
from contextlib import contextmanager


class TimeoutError(Exception):
    """Raised when an operation times out."""
    pass


class TimeoutGuard:
    """
    A context manager that enforces a timeout on operations.
    
    Supports both signal-based (Unix) and thread-based (cross-platform) timeouts.
    """
    
    def __init__(self, timeout_seconds: float, fallback_value: Any = None):
        """
        Initialize the timeout guard.
        
        Args:
            timeout_seconds: Maximum time to allow for operation in seconds
            fallback_value: Value to return if operation times out
        """
        if timeout_seconds <= 0:
            raise ValueError("Timeout must be positive")
        
        self.timeout_seconds = timeout_seconds
        self.fallback_value = fallback_value
        self._timed_out = False
        self._original_handler = None
        self._timer = None
        
    def _signal_handler(self, signum: int, frame) -> None:
        """Handle timeout signal."""
        self._timed_out = True
        raise TimeoutError(f"Operation timed out after {self.timeout_seconds} seconds")
    
    def _thread_timeout(self) -> None:
        """Timeout function for thread-based implementation."""
        time.sleep(self.timeout_seconds)
        self._timed_out = True
    
    @contextmanager
    def __call__(self):
        """
        Context manager entry point.
        
        Yields:
            None
            
        Raises:
            TimeoutError: If operation exceeds timeout
        """
        # Try signal-based timeout first (Unix systems)
        if hasattr(signal, 'SIGALRM'):
            try:
                self._original_handler = signal.signal(signal.SIGALRM, self._signal_handler)
                signal.alarm(int(self.timeout_seconds))
                yield
                signal.alarm(0)  # Cancel the alarm
                return
            except (ValueError, AttributeError):
                # Signal-based timeout not available, fall back to thread-based
                pass
            finally:
                if self._original_handler is not None:
                    signal.signal(signal.SIGALRM, self._original_handler)
        
        # Thread-based timeout (cross-platform)
        self._timer = threading.Timer(self.timeout_seconds, self._thread_timeout)
        self._timer.start()
        
        try:
            yield
        finally:
            self._timer.cancel()
            if self._timed_out:
                raise TimeoutError(f"Operation timed out after {self.timeout_seconds} seconds")


class TimedOperation:
    """
    A wrapper for executing operations with timeout and fallback capabilities.
    """
    
    def __init__(self, operation: Callable, timeout: float, fallback: Optional[Callable] = None):
        """
        Initialize the timed operation.
        
        Args:
            operation: The function to execute
            timeout: Maximum time to allow for operation in seconds
            fallback: Optional fallback function to call on timeout
        """
        self.operation = operation
        self.timeout = timeout
        self.fallback = fallback
    
    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operation with timeout protection.
        
        Args:
            *args: Positional arguments to pass to the operation
            **kwargs: Keyword arguments to pass to the operation
            
        Returns:
            Result of the operation or fallback function
            
        Raises:
            Exception: Any exception raised by the operation (except timeout)
        """
        guard = TimeoutGuard(self.timeout)
        
        try:
            with guard():
                return self.operation(*args, **kwargs)
        except TimeoutError:
            if self.fallback is not None:
                return self.fallback(*args, **kwargs)
            else:
                raise


def slow_task(duration: float, result: str = "Success") -> str:
    """
    Simulate a slow task.
    
    Args:
        duration: How long to sleep in seconds
        result: Result to return after sleeping
        
    Returns:
        The result string
    """
    time.sleep(duration)
    return result


def fast_task(result: str = "Fast Success") -> str:
    """
    Simulate a fast task.
    
    Args:
        result: Result to return immediately
        
    Returns:
        The result string
    """
    return result


def fallback_task(message: str = "Fallback Result") -> str:
    """
    Fallback task for when operations time out.
    
    Args:
        message: Message to return
        
    Returns:
        The fallback message
    """
    return f"Fallback: {message}"


if __name__ == "__main__":
    print("Testing TimeoutGuard and TimedOperation...")
    
    # Test 1: Fast operation within timeout
    print("\n1. Testing fast operation within timeout:")
    timed_op = TimedOperation(fast_task, timeout=1.0)
    try:
        result = timed_op.execute("Quick Result")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Slow operation that times out with fallback
    print("\n2. Testing slow operation with fallback:")
    timed_op = TimedOperation(
        lambda: slow_task(2.0, "Should timeout"), 
        timeout=0.5, 
        fallback=lambda: fallback_task("Operation took too long")
    )
    try:
        result = timed_op.execute()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Slow operation that times out without fallback
    print("\n3. Testing slow operation without fallback:")
    timed_op = TimedOperation(lambda: slow_task(2.0), timeout=0.1)
    try:
        result = timed_op.execute()
        print(f"   Result: {result}")
    except TimeoutError as e:
        print(f"   TimeoutError: {e}")
    except Exception as e:
        print(f"   Other Error: {e}")
    
    # Test 4: Direct use of TimeoutGuard
    print("\n4. Testing direct TimeoutGuard usage:")
    guard = TimeoutGuard(timeout_seconds=0.2, fallback_value="Guard Fallback")
    try:
        with guard():
            result = slow_task(1.0, "Direct Guard Test")
            print(f"   Result: {result}")
    except TimeoutError as e:
        print(f"   TimeoutError: {e}")
        print(f"   Fallback would be: {guard.fallback_value}")
    
    # Test 5: Operation that completes just within timeout
    print("\n5. Testing operation that completes just within timeout:")
    timed_op = TimedOperation(
        lambda: slow_task(0.1, "Just in time!"), 
        timeout=0.15
    )
    try:
        result = timed_op.execute()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\nAll tests completed.")