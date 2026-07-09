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
    """Demonstrate the bulkhead pattern isolator."""
    print("Bulkhead Pattern Isolator Demo")
    print("=" * 40)
    
    # Create isolated executor
    executor = IsolatedExecutor()
    
    # Create bulkheads with different capacities
    api_bulkhead = executor.create_bulkhead("api", 3)
    database_bulkhead = executor.create_bulkhead("database", 2)
    
    print(f"Created bulkhead 'api' with max concurrent: {api_bulkhead.max_concurrent}")
    print(f"Created bulkhead 'database' with max concurrent: {database_bulkhead.max_concurrent}")
    print()
    
    # Submit tasks to API bulkhead
    print("Submitting 5 tasks to API bulkhead (capacity 3)...")
    api_futures = []
    for i in range(5):
        future = executor.submit(
            "api",
            _demo_worker_task,
            i,
            duration=0.2,
            fallback=_demo_fallback
        )
        api_futures.append(future)
    
    # Submit tasks to database bulkhead
    print("Submitting 4 tasks to database bulkhead (capacity 2)...")
    db_futures = []
    for i in range(4):
        future = executor.submit(
            "database",
            _demo_worker_task,
            i + 100,
            duration=0.3,
            fallback=_demo_fallback
        )
        db_futures.append(future)
    
    # Collect results
    print("\nCollecting results...")
    all_futures = api_futures + db_futures
    
    for i, future in enumerate(as_completed(all_futures)):
        try:
            result = future.result(timeout=1.0)
            print(f"  Result {i+1}: {result}")
        except Exception as e:
            print(f"  Error {i+1}: {e}")
    
    # Print final statistics
    print("\nFinal Statistics:")
    print("-" * 20)
    stats = executor.bulkhead_stats()
    for name, bulkhead_stats in stats.items():
        print(f"Bulkhead '{name}':")
        for stat_name, value in bulkhead_stats.items():
            print(f"  {stat_name}: {value}")
        print()
    
    # Demonstrate timeout behavior
    print("Testing timeout behavior...")
    try:
        # This should timeout since all permits are in use
        result = api_bulkhead.execute(
            _demo_worker_task,
            999,
            timeout=0.1,  # Short timeout
            fallback=_demo_fallback
        )
        print(f"Timeout test result: {result}")
    except TimeoutError as e:
        print(f"Timeout error as expected: {e}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()