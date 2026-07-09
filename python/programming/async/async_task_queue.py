"""
Async Task Queue with Priority and Retries

A production-ready async task queue implementation with priority levels,
automatic retries with exponential backoff, and dead-letter queue handling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import asyncio
import heapq
import logging
import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Optional, Tuple
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Enumeration of possible task statuses."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


class Priority(Enum):
    """Task priority levels."""
    LOW = 3
    NORMAL = 2
    HIGH = 1
    CRITICAL = 0


@dataclass
class Task:
    """
    Represents a task in the queue.
    
    Attributes:
        id: Unique identifier for the task
        func: The async function to execute
        args: Positional arguments for the function
        kwargs: Keyword arguments for the function
        priority: Priority level of the task
        max_retries: Maximum number of retry attempts
        retry_count: Current number of retry attempts
        backoff_factor: Factor for exponential backoff
        status: Current status of the task
        created_at: Timestamp when task was created
        scheduled_at: Timestamp when task is scheduled to run
        completed_at: Timestamp when task was completed
        error: Error message if task failed
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    func: Optional[Callable[..., Awaitable[Any]]] = None
    args: Tuple[Any, ...] = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    priority: Priority = Priority.NORMAL
    max_retries: int = 3
    retry_count: int = 0
    backoff_factor: float = 2.0
    status: TaskStatus = TaskStatus.PENDING
    created_at: float = field(default_factory=time.time)
    scheduled_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    error: Optional[str] = None

    def __lt__(self, other: 'Task') -> bool:
        """Enable task comparison for priority queue ordering."""
        # Primary sort by priority (lower value = higher priority)
        if self.priority.value != other.priority.value:
            return self.priority.value < other.priority.value
        # Secondary sort by scheduled time (earlier = higher priority)
        return self.scheduled_at < other.scheduled_at

    def calculate_backoff(self) -> float:
        """Calculate backoff time for retry."""
        return self.backoff_factor ** self.retry_count


class TaskQueue:
    """
    Priority-based async task queue with retry and dead-letter functionality.
    
    Attributes:
        _queue: Priority queue for pending tasks
        _processing: Set of currently processing tasks
        _dead_letter_queue: Queue for failed tasks
        _lock: Async lock for thread safety
        _task_index: Index for quick task lookup
        _stats: Statistics about task processing
    """
    
    def __init__(self) -> None:
        self._queue: List[Task] = []
        self._processing: Dict[str, Task] = {}
        self._dead_letter_queue: List[Task] = []
        self._lock = asyncio.Lock()
        self._task_index: Dict[str, Task] = {}
        self._stats = defaultdict(int)
        
    async def enqueue(self, task: Task) -> str:
        """
        Add a task to the queue.
        
        Args:
            task: Task to add to the queue
            
        Returns:
            Task ID
            
        Raises:
            ValueError: If task is None or has no function
        """
        if not task or not task.func:
            raise ValueError("Task must have a function to execute")
            
        async with self._lock:
            heapq.heappush(self._queue, task)
            self._task_index[task.id] = task
            self._stats['enqueued'] += 1
            logger.info(f"Enqueued task {task.id} with priority {task.priority.name}")
            return task.id
            
    async def dequeue(self) -> Optional[Task]:
        """
        Remove and return the highest priority task from the queue.
        
        Returns:
            Task or None if queue is empty
        """
        async with self._lock:
            while self._queue:
                # Get the highest priority task
                task = heapq.heappop(self._queue)
                
                # Check if it's ready to be processed
                if task.scheduled_at <= time.time():
                    task.status = TaskStatus.PROCESSING
                    self._processing[task.id] = task
                    self._stats['processing'] += 1
                    logger.info(f"Dequeued task {task.id}")
                    return task
                else:
                    # Put it back and try the next one
                    heapq.heappush(self._queue, task)
                    break
                    
            return None
            
    async def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to complete
            
        Returns:
            True if task was found and completed, False otherwise
        """
        async with self._lock:
            if task_id in self._processing:
                task = self._processing.pop(task_id)
                task.status = TaskStatus.COMPLETED
                task.completed_at = time.time()
                self._stats['completed'] += 1
                logger.info(f"Completed task {task_id}")
                return True
            return False
            
    async def fail_task(self, task_id: str, error: str) -> bool:
        """
        Handle task failure with retry logic.
        
        Args:
            task_id: ID of the failed task
            error: Error message
            
        Returns:
            True if task was retried or moved to dead letter queue, False if not found
        """
        async with self._lock:
            if task_id in self._processing:
                task = self._processing.pop(task_id)
                task.error = error
                
                # Check if we should retry
                if task.retry_count < task.max_retries:
                    task.retry_count += 1
                    task.status = TaskStatus.RETRYING
                    backoff = task.calculate_backoff()
                    task.scheduled_at = time.time() + backoff
                    heapq.heappush(self._queue, task)
                    self._stats['retried'] += 1
                    logger.info(f"Retrying task {task_id} in {backoff:.2f} seconds (attempt {task.retry_count})")
                else:
                    # Move to dead letter queue
                    task.status = TaskStatus.FAILED
                    task.completed_at = time.time()
                    self._dead_letter_queue.append(task)
                    self._stats['failed'] += 1
                    logger.warning(f"Task {task_id} failed permanently and moved to dead letter queue")
                    
                return True
            return False
            
    async def get_stats(self) -> Dict[str, int]:
        """Get queue statistics."""
        async with self._lock:
            stats = self._stats.copy()
            stats['pending'] = len(self._queue)
            stats['processing'] = len(self._processing)
            stats['dead_letter'] = len(self._dead_letter_queue)
            return stats
            
    async def get_dead_letter_queue(self) -> List[Task]:
        """Get all tasks in the dead letter queue."""
        async with self._lock:
            return self._dead_letter_queue.copy()


class Worker(ABC):
    """
    Abstract base class for task workers.
    
    Attributes:
        queue: Task queue to process tasks from
        name: Worker name for identification
        _running: Flag indicating if worker is running
        _task: Current running task
    """
    
    def __init__(self, queue: TaskQueue, name: str = "Worker") -> None:
        self.queue = queue
        self.name = name
        self._running = False
        self._task: Optional[asyncio.Task] = None
        
    async def start(self) -> None:
        """Start the worker."""
        if self._running:
            return
            
        self._running = True
        self._task = asyncio.create_task(self._run())
        logger.info(f"{self.name} started")
        
    async def stop(self) -> None:
        """Stop the worker."""
        if not self._running:
            return
            
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        logger.info(f"{self.name} stopped")
        
    async def _run(self) -> None:
        """Main worker loop."""
        while self._running:
            try:
                task = await self.queue.dequeue()
                if task:
                    await self._process_task(task)
                else:
                    # No tasks available, sleep briefly
                    await asyncio.sleep(0.1)
            except Exception as e:
                logger.error(f"{self.name} encountered an error: {e}")
                await asyncio.sleep(1)  # Brief pause before continuing
                
    async def _process_task(self, task: Task) -> None:
        """Process a single task."""
        try:
            logger.info(f"{self.name} processing task {task.id}")
            result = await task.func(*task.args, **task.kwargs)
            await self.queue.complete_task(task.id)
            logger.info(f"{self.name} completed task {task.id} with result: {result}")
        except Exception as e:
            error_msg = str(e)
            logger.error(f"{self.name} failed task {task.id}: {error_msg}")
            await self.queue.fail_task(task.id, error_msg)


# Demo functions
async def demo_task_success(name: str, duration: float = 0.1) -> str:
    """Demo task that succeeds."""
    await asyncio.sleep(duration)
    return f"Success: {name}"

async def demo_task_failure(name: str) -> str:
    """Demo task that fails."""
    await asyncio.sleep(0.1)
    raise RuntimeError(f"Intentional failure for {name}")

async def demo_task_random(name: str) -> str:
    """Demo task that randomly succeeds or fails."""
    await asyncio.sleep(0.1)
    import random
    if random.random() < 0.7:  # 70% chance of success
        return f"Random success: {name}"
    else:
        raise RuntimeError(f"Random failure for {name}")


async def main() -> None:
    """Demo the task queue functionality."""
    print("=== Async Task Queue Demo ===\n")
    
    # Create queue and worker
    queue = TaskQueue()
    worker = Worker(queue, "DemoWorker")
    
    # Start worker
    await worker.start()
    
    # Create and enqueue various tasks
    tasks = []
    
    # High priority successful tasks
    for i in range(3):
        task = Task(
            func=demo_task_success,
            args=[f"High Priority Task {i}"],
            priority=Priority.HIGH,
            max_retries=2
        )
        tasks.append(task)
        await queue.enqueue(task)
    
    # Normal priority tasks with some failures
    for i in range(5):
        task = Task(
            func=demo_task_random if i % 2 == 0 else demo_task_failure,
            args=[f"Normal Task {i}"],
            priority=Priority.NORMAL,
            max_retries=3
        )
        tasks.append(task)
        await queue.enqueue(task)
    
    # Low priority tasks
    for i in range(2):
        task = Task(
            func=demo_task_success,
            args=[f"Low Priority Task {i}"],
            priority=Priority.LOW,
            max_retries=1
        )
        tasks.append(task)
        await queue.enqueue(task)
    
    print(f"Enqueued {len(tasks)} tasks\n")
    
    # Wait for tasks to process
    await asyncio.sleep(5)
    
    # Print statistics
    stats = await queue.get_stats()
    print("=== Processing Statistics ===")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")
    
    # Print dead letter queue
    dlq = await queue.get_dead_letter_queue()
    if dlq:
        print("\n=== Dead Letter Queue ===")
        for task in dlq:
            print(f"Task {task.id}: {task.error}")
    
    # Stop worker
    await worker.stop()
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    asyncio.run(main())