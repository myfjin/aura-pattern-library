"""
Request Collapser Module

This module implements a request collapser that batches identical requests
within a time window to reduce backend load. It deduplicates concurrent
requests and executes them as a single backend call.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import asyncio
import time
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from collections import defaultdict
from dataclasses import dataclass
import threading
import uuid


@dataclass
class BatchRequest:
    """
    Represents a batched request with its identifier and arguments.
    
    Attributes:
        request_id: Unique identifier for the request
        args: Positional arguments for the request
        kwargs: Keyword arguments for the request
        future: Future to set the result when completed
    """
    request_id: str
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    future: asyncio.Future


class Collapser:
    """
    Request collapser that batches identical requests within a time window.
    
    This class deduplicates concurrent requests and executes them as a single
    backend call to reduce load on the backend service.
    """
    
    def __init__(
        self,
        backend_func: Callable,
        window_ms: int = 10,
        max_batch_size: int = 100
    ):
        """
        Initialize the Collapser.
        
        Args:
            backend_func: The function to call for batched requests
            window_ms: Time window in milliseconds to collect requests
            max_batch_size: Maximum number of requests in a batch
        """
        self.backend_func = backend_func
        self.window_ms = window_ms
        self.max_batch_size = max_batch_size
        self.pending_requests: Dict[str, List[BatchRequest]] = defaultdict(list)
        self._lock = threading.Lock()
        self._timer_active = False
        self._timer_handle: Optional[asyncio.Handle] = None
        
    def _get_request_key(self, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> str:
        """
        Generate a unique key for a request based on its arguments.
        
        Args:
            args: Positional arguments
            kwargs: Keyword arguments
            
        Returns:
            String key representing the request
        """
        # Create a hashable representation of the arguments
        key_parts = []
        for arg in args:
            key_parts.append(str(arg))
        for k, v in sorted(kwargs.items()):
            key_parts.append(f"{k}:{v}")
        return "|".join(key_parts)
    
    async def submit(self, *args: Any, **kwargs: Any) -> Any:
        """
        Submit a request to be collapsed.
        
        Args:
            *args: Positional arguments for the request
            **kwargs: Keyword arguments for the request
            
        Returns:
            Result of the request
            
        Raises:
            Exception: Any exception raised by the backend function
        """
        # Create a unique request ID
        request_id = str(uuid.uuid4())
        
        # Create a future to hold the result
        future = asyncio.get_event_loop().create_future()
        
        # Generate the request key
        request_key = self._get_request_key(args, kwargs)
        
        # Create the batch request
        batch_request = BatchRequest(request_id, args, kwargs, future)
        
        # Add to pending requests
        with self._lock:
            self.pending_requests[request_key].append(batch_request)
            should_start_timer = not self._timer_active
            
            if should_start_timer:
                self._timer_active = True
                loop = asyncio.get_event_loop()
                self._timer_handle = loop.call_later(
                    self.window_ms / 1000.0, 
                    lambda: asyncio.create_task(self._process_batches())
                )
        
        # Wait for the result
        return await future
    
    async def _process_batches(self) -> None:
        """Process all pending batches."""
        with self._lock:
            self._timer_active = False
            if self._timer_handle:
                self._timer_handle.cancel()
                self._timer_handle = None
            
            # Copy and clear pending requests
            batches_to_process = dict(self.pending_requests)
            self.pending_requests.clear()
        
        # Process each batch
        for request_key, requests in batches_to_process.items():
            await self._process_batch(requests)
    
    async def _process_batch(self, requests: List[BatchRequest]) -> None:
        """
        Process a single batch of requests.
        
        Args:
            requests: List of requests to process as a batch
        """
        if not requests:
            return
            
        # Use the first request's arguments for the backend call
        # In a real implementation, you might need to merge arguments
        first_request = requests[0]
        
        try:
            # Call the backend function with the first request's arguments
            result = await self._call_backend(first_request.args, first_request.kwargs)
            
            # Set the result for all requests in the batch
            for request in requests:
                if not request.future.done():
                    request.future.set_result(result)
        except Exception as e:
            # Set the exception for all requests in the batch
            for request in requests:
                if not request.future.done():
                    request.future.set_exception(e)
    
    async def _call_backend(self, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Any:
        """
        Call the backend function, handling both sync and async functions.
        
        Args:
            args: Positional arguments
            kwargs: Keyword arguments
            
        Returns:
            Result from the backend function
        """
        if asyncio.iscoroutinefunction(self.backend_func):
            return await self.backend_func(*args, **kwargs)
        else:
            # Run synchronous function in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, self.backend_func, *args, **kwargs)


async def _selftest() -> None:
    """Self-test: identical requests collapse to ONE backend call; distinct
    requests do not; a backend failure reaches every collapsed waiter."""
    calls = {"n": 0, "args": []}

    async def counting_backend(user_id: int, include_profile: bool = False) -> Dict[str, Any]:
        calls["n"] += 1
        calls["args"].append(user_id)
        await asyncio.sleep(0)
        return {"user_id": user_id, "call_no": calls["n"]}

    # Request-key derivation is exact and order-normalizes kwargs.
    c = Collapser(counting_backend, window_ms=20, max_batch_size=10)
    assert c._get_request_key((1,), {"b": 2, "a": 3}) == "1|a:3|b:2", \
        "request key must sort kwargs for stable identity"

    # THE POINT of the pattern: 5 identical concurrent requests = 1 backend call.
    results = await asyncio.gather(*[c.submit(123, include_profile=True) for _ in range(5)])
    assert calls["n"] == 1, f"5 identical requests caused {calls['n']} backend calls, not 1"
    assert len(results) == 5
    assert all(r == results[0] for r in results), "collapsed waiters got different results"
    assert results[0]["user_id"] == 123 and results[0]["call_no"] == 1

    # Distinct requests must NOT be collapsed: 3 keys → exactly 3 more calls.
    r2 = await asyncio.gather(c.submit(123, include_profile=True),
                              c.submit(456, include_profile=True),
                              c.submit(789, include_profile=False))
    assert calls["n"] == 4, f"3 distinct requests after 1 must total 4 calls, got {calls['n']}"
    assert [r["user_id"] for r in r2] == [123, 456, 789]

    # THE FAILURE: a backend exception must reach EVERY collapsed waiter —
    # a silently-hung future is the disaster here.
    async def failing_backend(user_id: int) -> None:
        raise RuntimeError("backend down")

    f = Collapser(failing_backend, window_ms=20, max_batch_size=10)
    failures = await asyncio.gather(f.submit(7), f.submit(7), return_exceptions=True)
    assert len(failures) == 2
    assert all(isinstance(e, RuntimeError) and str(e) == "backend down" for e in failures), \
        f"collapsed waiters did not all receive the backend failure: {failures}"

    # Sync backends run via the executor path and still collapse.
    sync_calls = {"n": 0}
    def sync_backend(x: int) -> int:
        sync_calls["n"] += 1
        return x * 10
    s = Collapser(sync_backend, window_ms=20, max_batch_size=10)
    sr = await asyncio.gather(s.submit(4), s.submit(4), s.submit(4))
    assert sr == [40, 40, 40], f"sync backend results wrong: {sr}"
    assert sync_calls["n"] == 1, f"sync backend called {sync_calls['n']} times, not 1"

    print("budget_allocator (request collapser): 5→1 collapsed, 3 distinct kept, "
          "failure fanned out to all waiters, sync path collapsed — PASS")


if __name__ == "__main__":
    asyncio.run(_selftest())