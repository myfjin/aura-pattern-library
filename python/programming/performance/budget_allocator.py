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


# Demo backend function
async def demo_backend_func(user_id: int, include_profile: bool = False) -> Dict[str, Any]:
    """
    Demo backend function that simulates fetching user data.
    
    Args:
        user_id: ID of the user to fetch
        include_profile: Whether to include profile information
        
    Returns:
        User data dictionary
    """
    # Simulate some processing time
    await asyncio.sleep(0.1)
    
    # Return mock user data
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
        "profile_included": include_profile,
        "timestamp": time.time()
    }


async def demo() -> None:
    """Demonstrate the request collapser with concurrent identical queries."""
    print("Request Collapser Demo")
    print("=" * 50)
    
    # Create a collapser instance
    collapser = Collapser(demo_backend_func, window_ms=50, max_batch_size=10)
    
    # Submit multiple identical requests concurrently
    print("Submitting 5 identical requests for user 123...")
    
    start_time = time.time()
    
    # Create tasks for concurrent requests
    tasks = [
        collapser.submit(123, include_profile=True),
        collapser.submit(123, include_profile=True),
        collapser.submit(123, include_profile=True),
        collapser.submit(123, include_profile=True),
        collapser.submit(123, include_profile=True),
    ]
    
    # Wait for all results
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    # Print results
    print(f"Received {len(results)} results in {end_time - start_time:.2f} seconds")
    
    for i, result in enumerate(results):
        print(f"Result {i+1}: User {result['user_id']}, Name: {result['name']}")
    
    # Verify all results are identical (deduplication worked)
    all_identical = all(result == results[0] for result in results)
    print(f"All results identical: {all_identical}")
    
    # Test with different requests (should not be collapsed)
    print("\nSubmitting different requests...")
    different_tasks = [
        collapser.submit(123, include_profile=True),
        collapser.submit(456, include_profile=True),
        collapser.submit(789, include_profile=False),
    ]
    
    different_results = await asyncio.gather(*different_tasks)
    print(f"Received {len(different_results)} different results:")
    
    for i, result in enumerate(different_results):
        print(f"Result {i+1}: User {result['user_id']}, Profile: {result['profile_included']}")


if __name__ == "__main__":
    # Run the demo
    asyncio.run(demo())