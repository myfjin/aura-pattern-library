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
        """Timeout function for thread-based implementation. (Runs inside a
        threading.Timer that already waited timeout_seconds — the former
        extra sleep here flagged the timeout at DOUBLE the deadline.)"""
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
        # Try signal-based timeout first (Unix systems). setitimer takes
        # FLOAT seconds — the former signal.alarm(int(0.3)) truncated to
        # alarm(0), which CANCELS the alarm: every sub-second timeout
        # silently disarmed itself. Setup errors are separated from body
        # errors: catching around the yield swallowed the operation's own
        # exceptions and fell through to a second yield (RuntimeError).
        use_signal = False
        if hasattr(signal, 'SIGALRM') and hasattr(signal, 'setitimer'):
            try:
                self._original_handler = signal.signal(signal.SIGALRM, self._signal_handler)
                signal.setitimer(signal.ITIMER_REAL, self.timeout_seconds)
                use_signal = True
            except (ValueError, AttributeError):
                use_signal = False  # e.g. not the main thread

        if use_signal:
            try:
                yield
                return
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)  # Cancel the timer
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
    # Self-test: THE DISASTER (a hung task) must actually happen and be cut
    # off; fast tasks pass through; fallbacks fire only on timeout.

    # Fast path: result passes through untouched, well under the deadline.
    assert TimedOperation(fast_task, timeout=1.0).execute("Quick") == "Quick"

    # THE HANG: a 2s task under a 0.3s deadline must be interrupted and the
    # fallback must answer. Wall time proves the cut-off actually happened.
    start = time.monotonic()
    result = TimedOperation(
        lambda: slow_task(2.0, "should never return"),
        timeout=0.3,
        fallback=lambda: fallback_task("too slow"),
    ).execute()
    elapsed = time.monotonic() - start
    assert result == "Fallback: too slow", f"fallback did not answer: {result}"
    assert elapsed < 1.5, f"timeout did not cut the 2s hang (took {elapsed:.2f}s)"
    assert abs(elapsed - 0.3) < 0.25, \
        f"cut must land near the 0.3s deadline, took {elapsed:.2f}s"

    # Without a fallback, the timeout surfaces as TimeoutError.
    start = time.monotonic()
    try:
        TimedOperation(lambda: slow_task(2.0), timeout=0.2).execute()
        assert False, "hung task returned"
    except TimeoutError:
        pass
    assert time.monotonic() - start < 1.5, "TimeoutError came too late to matter"

    # Direct guard usage: the with-block is interrupted.
    guard = TimeoutGuard(timeout_seconds=0.2, fallback_value="guard-fb")
    interrupted = False
    try:
        with guard():
            slow_task(2.0)
    except TimeoutError:
        interrupted = True
    assert interrupted, "TimeoutGuard let the slow block finish"
    assert guard.fallback_value == "guard-fb"

    # A task that fits inside its deadline completes normally.
    assert TimedOperation(lambda: slow_task(0.05, "in time"),
                          timeout=1.0).execute() == "in time"

    # The operation's own exception is not swallowed as a timeout.
    def own_error():
        raise ValueError("mine")
    try:
        TimedOperation(own_error, timeout=1.0).execute()
        assert False, "operation's exception vanished"
    except ValueError:
        pass

    # Fallback receives the original call's arguments.
    echo = TimedOperation(lambda tag: slow_task(2.0),
                          timeout=0.2, fallback=lambda tag: f"fb:{tag}")
    assert echo.execute("xyz") == "fb:xyz", "fallback lost the call arguments"

    print("timeout_guard: 2s hang cut at 0.3s (fallback answered), bare "
          "TimeoutError timely, in-deadline task fine, own errors surface — PASS")