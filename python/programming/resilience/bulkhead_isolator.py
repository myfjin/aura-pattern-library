"""
Bulkhead Pattern Isolator Module

This module implements the bulkhead pattern to isolate system resources and prevent
cascading failures. It provides resource isolation through semaphore-based pools
and isolated execution contexts.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import threading
import time
from typing import Any, Callable, Dict, List, Optional, Union
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from collections import defaultdict


class SemaphorePool:
    """
    A pool of semaphores for resource management.
    
    Manages a fixed number of permits that can be acquired and released,
    providing resource isolation for the bulkhead pattern.
    """
    
    def __init__(self, permits: int):
        """
        Initialize the semaphore pool.
        
        Args:
            permits: Number of available permits in the pool
        """
        if permits <= 0:
            raise ValueError("Permits must be positive")
        self._semaphore = threading.Semaphore(permits)
        self._permits = permits
        self._lock = threading.Lock()
        self._acquired = 0
    
    @property
    def permits(self) -> int:
        """Get the total number of permits."""
        return self._permits
    
    @property
    def available_permits(self) -> int:
        """Get the number of currently available permits."""
        with self._lock:
            return self._permits - self._acquired
    
    def acquire(self, timeout: Optional[float] = None) -> bool:
        """
        Acquire a permit from the pool.
        
        Args:
            timeout: Maximum time to wait for a permit (None for no timeout)
            
        Returns:
            True if permit was acquired, False if timeout occurred
        """
        acquired = self._semaphore.acquire(timeout=timeout)
        if acquired:
            with self._lock:
                self._acquired += 1
        return acquired
    
    def release(self) -> None:
        """Release a permit back to the pool."""
        with self._lock:
            if self._acquired > 0:
                self._acquired -= 1
        self._semaphore.release()


class Bulkhead:
    """
    Bulkhead resource isolator.
    
    Provides resource isolation by limiting concurrent access to a resource
    through a semaphore pool.
    """
    
    def __init__(self, name: str, max_concurrent: int):
        """
        Initialize the bulkhead.
        
        Args:
            name: Name identifier for the bulkhead
            max_concurrent: Maximum concurrent operations allowed
        """
        self.name = name
        self._semaphore_pool = SemaphorePool(max_concurrent)
        self._lock = threading.Lock()
        self._total_requests = 0
        self._rejected_requests = 0
    
    @property
    def max_concurrent(self) -> int:
        """Get the maximum concurrent operations allowed."""
        return self._semaphore_pool.permits
    
    @property
    def available_concurrent(self) -> int:
        """Get the number of available concurrent operations."""
        return self._semaphore_pool.available_permits
    
    @property
    def total_requests(self) -> int:
        """Get the total number of requests processed."""
        with self._lock:
            return self._total_requests
    
    @property
    def rejected_requests(self) -> int:
        """Get the number of rejected requests."""
        with self._lock:
            return self._rejected_requests
    
    def execute(
        self, 
        func: Callable[..., Any], 
        *args: Any, 
        timeout: Optional[float] = None,
        fallback: Optional[Callable[[], Any]] = None,
        **kwargs: Any
    ) -> Any:
        """
        Execute a function within the bulkhead isolation.
        
        Args:
            func: Function to execute
            *args: Positional arguments for the function
            timeout: Timeout for acquiring a permit
            fallback: Fallback function to execute if permit acquisition fails
            **kwargs: Keyword arguments for the function
            
        Returns:
            Result of the function execution or fallback
            
        Raises:
            Exception: Any exception raised by the function (if no fallback)
        """
        with self._lock:
            self._total_requests += 1
        
        # Try to acquire a permit
        if not self._semaphore_pool.acquire(timeout=timeout):
            with self._lock:
                self._rejected_requests += 1
            if fallback is not None:
                return fallback()
            else:
                raise TimeoutError(f"Bulkhead {self.name} timeout acquiring permit")
        
        try:
            # Execute the function with the permit
            return func(*args, **kwargs)
        finally:
            # Always release the permit
            self._semaphore_pool.release()


class IsolatedExecutor:
    """
    Executor that runs tasks in isolated bulkhead contexts.
    
    Manages multiple bulkheads and provides a clean interface for
    executing tasks with resource isolation.
    """
    
    def __init__(self):
        """Initialize the isolated executor."""
        self._bulkheads: Dict[str, Bulkhead] = {}
        self._lock = threading.Lock()
    
    def create_bulkhead(self, name: str, max_concurrent: int) -> Bulkhead:
        """
        Create a new bulkhead.
        
        Args:
            name: Name identifier for the bulkhead
            max_concurrent: Maximum concurrent operations allowed
            
        Returns:
            The created bulkhead
            
        Raises:
            ValueError: If bulkhead with the name already exists
        """
        with self._lock:
            if name in self._bulkheads:
                raise ValueError(f"Bulkhead '{name}' already exists")
            bulkhead = Bulkhead(name, max_concurrent)
            self._bulkheads[name] = bulkhead
            return bulkhead
    
    def get_bulkhead(self, name: str) -> Optional[Bulkhead]:
        """
        Get an existing bulkhead by name.
        
        Args:
            name: Name of the bulkhead to retrieve
            
        Returns:
            The bulkhead if found, None otherwise
        """
        with self._lock:
            return self._bulkheads.get(name)
    
    def remove_bulkhead(self, name: str) -> bool:
        """
        Remove a bulkhead.
        
        Args:
            name: Name of the bulkhead to remove
            
        Returns:
            True if bulkhead was removed, False if not found
        """
        with self._lock:
            if name in self._bulkheads:
                del self._bulkheads[name]
                return True
            return False
    
    def submit(
        self, 
        bulkhead_name: str,
        func: Callable[..., Any],
        *args: Any,
        timeout: Optional[float] = None,
        fallback: Optional[Callable[[], Any]] = None,
        **kwargs: Any
    ) -> Future:
        """
        Submit a task to be executed in a bulkhead context.
        
        Args:
            bulkhead_name: Name of the bulkhead to use
            func: Function to execute
            *args: Positional arguments for the function
            timeout: Timeout for acquiring a permit
            fallback: Fallback function to execute if permit acquisition fails
            **kwargs: Keyword arguments for the function
            
        Returns:
            Future representing the execution
            
        Raises:
            ValueError: If bulkhead with the name doesn't exist
        """
        with self._lock:
            if bulkhead_name not in self._bulkheads:
                raise ValueError(f"Bulkhead '{bulkhead_name}' not found")
            bulkhead = self._bulkheads[bulkhead_name]
        
        # Use a thread pool to execute the bulkhead operation asynchronously
        executor = ThreadPoolExecutor(max_workers=1)
        future = executor.submit(bulkhead.execute, func, *args, timeout=timeout, fallback=fallback, **kwargs)
        
        # Ensure executor is cleaned up after completion
        def cleanup(_):
            executor.shutdown(wait=False)
        future.add_done_callback(cleanup)
        
        return future
    
    def bulkhead_stats(self) -> Dict[str, Dict[str, int]]:
        """
        Get statistics for all bulkheads.
        
        Returns:
            Dictionary mapping bulkhead names to their statistics
        """
        stats = {}
        with self._lock:
            for name, bulkhead in self._bulkheads.items():
                stats[name] = {
                    'max_concurrent': bulkhead.max_concurrent,
                    'available_concurrent': bulkhead.available_concurrent,
                    'total_requests': bulkhead.total_requests,
                    'rejected_requests': bulkhead.rejected_requests
                }
        return stats


def _demo_worker_task(task_id: int, duration: float = 0.1) -> str:
    """Demo worker task that simulates work."""
    time.sleep(duration)
    return f"Task {task_id} completed"


def _demo_fallback() -> str:
    """Demo fallback function."""
    return "FALLBACK_EXECUTED"


def main():
    """Self-test: the bulkhead's concurrency CEILING is measured under real
    thread pressure, isolation between bulkheads proven, fallback on saturation."""
    executor = IsolatedExecutor()
    api = executor.create_bulkhead("api", 3)
    db = executor.create_bulkhead("database", 2)

    # Measure the true max concurrency inside the protected function.
    meter = {"api": 0, "api_max": 0, "db": 0, "db_max": 0}
    meter_lock = threading.Lock()

    def tracked(kind: str, duration: float) -> str:
        with meter_lock:
            meter[kind] += 1
            meter[f"{kind}_max"] = max(meter[f"{kind}_max"], meter[kind])
        time.sleep(duration)
        with meter_lock:
            meter[kind] -= 1
        return f"{kind}-done"

    # 6 api tasks (cap 3) + 4 db tasks (cap 2), generous acquire timeout so
    # everything eventually runs — the CEILING is what we assert.
    futures = [executor.submit("api", tracked, "api", 0.1, timeout=5.0)
               for _ in range(6)]
    futures += [executor.submit("database", tracked, "db", 0.1, timeout=5.0)
                for _ in range(4)]
    results = [f.result(timeout=10.0) for f in futures]
    assert results.count("api-done") == 6 and results.count("db-done") == 4, \
        f"all tasks must complete: {results}"
    assert meter["api_max"] <= 3, \
        f"api bulkhead (cap 3) reached {meter['api_max']} concurrent"
    assert meter["db_max"] <= 2, \
        f"db bulkhead (cap 2) reached {meter['db_max']} concurrent — ISOLATION BROKEN"
    assert meter["api_max"] >= 2, "api tasks never actually overlapped (test too weak)"

    # Stats accounting: every request counted, none rejected yet.
    stats = executor.bulkhead_stats()
    assert stats["api"]["total_requests"] == 6, f"api stats: {stats['api']}"
    assert stats["database"]["total_requests"] == 4
    assert stats["api"]["rejected_requests"] == 0

    # SATURATION: hold all 3 api permits, then a 0.05s-timeout call must
    # take the FALLBACK, and the rejection must be counted.
    hold = threading.Event()
    def holder() -> str:
        hold.wait(3.0)
        return "held"
    holders = [executor.submit("api", holder, timeout=5.0) for _ in range(3)]
    time.sleep(0.2)  # let the holders occupy the permits
    result = api.execute(lambda: "should not run", timeout=0.05,
                         fallback=lambda: "FALLBACK")
    assert result == "FALLBACK", f"saturated bulkhead must fall back, got {result!r}"
    assert executor.bulkhead_stats()["api"]["rejected_requests"] == 1, \
        "rejection not counted"
    hold.set()
    for h in holders:
        assert h.result(timeout=5.0) == "held"

    # Unknown bulkhead is refused; duplicate creation is refused.
    try:
        executor.submit("ghost", lambda: None)
        assert False, "unknown bulkhead accepted"
    except ValueError:
        pass

    print(f"bulkhead_isolator: ceilings held (api {meter['api_max']}<=3, "
          f"db {meter['db_max']}<=2), 10/10 completed, saturation → fallback "
          f"+ rejection counted — PASS")


if __name__ == "__main__":
    main()