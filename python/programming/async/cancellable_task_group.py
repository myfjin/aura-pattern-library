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
    # Self-test: results and exceptions captured per task, cancellation
    # actually interrupts long tasks and blocks new spawns.

    # Clean group: results exact, the failing task's exception is captured
    # in ITS slot without harming the others.
    with TaskGroup() as tg:
        t_quick = tg.spawn(quick_task, "A")
        t_fail = tg.spawn(failing_task, "B")
        t_short = tg.spawn(example_task, "C", 0.2, tg.token)
        results = tg.wait_all()
        assert len(results) == 3
        assert t_quick.result == "Task A finished instantly"
        assert t_quick.completed and t_quick.exception is None
        assert isinstance(t_fail.exception, ValueError), \
            f"failing task's exception not captured: {t_fail.exception}"
        assert t_fail.result is None
        assert t_short.result == "Task C completed successfully"
        n_done = sum(1 for t in results if t.completed)
        assert n_done == 3, f"all 3 must complete, got {n_done}"

    # CANCELLATION: a 10s task must come back as cancelled fast, not run out.
    start = time.monotonic()
    with TaskGroup() as tg:
        long_task = tg.spawn(example_task, "Long", 10.0, tg.token)
        time.sleep(0.3)          # let it get going
        tg.cancel_all()
        assert tg.token.is_cancelled
        tg.wait_all()
        elapsed = time.monotonic() - start
        assert long_task.result == "Task Long was cancelled", \
            f"long task did not observe cancellation: {long_task.result!r}"
        assert elapsed < 5.0, f"cancellation did not cut the 10s task ({elapsed:.1f}s)"

        # After cancellation, spawning is refused.
        try:
            tg.spawn(quick_task, "late")
            assert False, "spawn accepted after cancel_all"
        except RuntimeError:
            pass

    # A task that never started (spawned then immediately cancelled group)
    # is skipped rather than run.
    with TaskGroup() as tg:
        tg.token.cancel()
        # spawn refuses, so submit through a fresh group with pre-set token:
        pass
    group = TaskGroup()
    group.token.cancel()
    tsk = Task(quick_task, "never")
    tsk.run(group.token)
    assert tsk.completed and tsk.result is None, \
        "task body ran despite a cancelled token"

    print("cancellable_task_group: 3/3 completed (exception captured in-slot), "
          "10s task cancelled in <5s, post-cancel spawn refused — PASS")