"""
Async task group implementation with cancellation support.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import threading
import time
from typing import List, Optional, Callable, Any
from concurrent.futures import Future, ThreadPoolExecutor


class CancellationToken:
    """A token that can be used to signal cancellation to running tasks."""
    
    def __init__(self):
        self._cancelled = False
        self._lock = threading.Lock()
    
    def cancel(self) -> None:
        """Signal that operations should be cancelled."""
        with self._lock:
            self._cancelled = True
    
    @property
    def is_cancelled(self) -> bool:
        """Check if cancellation has been requested."""
        with self._lock:
            return self._cancelled


class Task:
    """Represents an asynchronous task."""
    
    def __init__(self, fn: Callable, *args: Any, **kwargs: Any):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.future: Optional[Future] = None
        self.thread: Optional[threading.Thread] = None
        self.result: Any = None
        self.exception: Optional[Exception] = None
        self.completed = False
    
    def run(self, token: CancellationToken) -> None:
        """Execute the task function."""
        try:
            if not token.is_cancelled:
                self.result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            self.exception = e
        finally:
            self.completed = True


class TaskGroup:
    """Manages a group of asynchronous tasks with cancellation support."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.token = CancellationToken()
        self._lock = threading.Lock()
        self._executor = ThreadPoolExecutor(max_workers=10)
    
    def spawn(self, fn: Callable, *args: Any, **kwargs: Any) -> Task:
        """Spawn a new task in the group."""
        with self._lock:
            if self.token.is_cancelled:
                raise RuntimeError("Cannot spawn tasks after cancellation")
            
            task = Task(fn, *args, **kwargs)
            task.future = self._executor.submit(task.run, self.token)
            self.tasks.append(task)
            return task
    
    def cancel_all(self) -> None:
        """Cancel all tasks in the group."""
        with self._lock:
            self.token.cancel()
            # Wait a bit for tasks to notice cancellation
            time.sleep(0.01)
    
    def wait_all(self) -> List[Task]:
        """Wait for all tasks to complete and return them."""
        # Wait for all futures to complete
        futures = [task.future for task in self.tasks if task.future]
        # Collect results (this will wait for completion)
        for future in futures:
            if future:
                future.result()  # This blocks until the future completes
        return self.tasks
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._executor.shutdown(wait=True)


def example_task(name: str, duration: float, token: CancellationToken) -> str:
    """Example task function that respects cancellation."""
    start = time.time()
    while time.time() - start < duration:
        if token.is_cancelled:
            return f"Task {name} was cancelled"
        time.sleep(0.1)
    return f"Task {name} completed successfully"


def failing_task(name: str) -> str:
    """Example task that raises an exception."""
    raise ValueError(f"Task {name} failed intentionally")


def quick_task(name: str) -> str:
    """Example quick task."""
    return f"Task {name} finished instantly"


if __name__ == "__main__":
    # Demo the TaskGroup functionality
    print("Starting TaskGroup demo...")
    
    with TaskGroup() as tg:
        # Spawn various tasks
        task1 = tg.spawn(example_task, "Quick", 0.5, tg.token)
        task2 = tg.spawn(example_task, "Slow", 2.0, tg.token)
        task3 = tg.spawn(quick_task, "Instant")
        task4 = tg.spawn(failing_task, "Failure")
        
        print(f"Spawned {len(tg.tasks)} tasks")
        
        # Wait a bit then cancel all tasks
        time.sleep(0.8)
        print("Cancelling all tasks...")
        tg.cancel_all()
        
        # Wait for all tasks to complete
        results = tg.wait_all()
        
        # Print results
        for i, task in enumerate(results):
            if task.exception:
                print(f"Task {i+1}: Exception - {task.exception}")
            else:
                print(f"Task {i+1}: {task.result}")
    
    print("Demo completed.")