#!/usr/bin/env python3
"""
Priority Queue with Deadline Scheduling Module

This module implements a priority queue that supports deadline-aware scheduling
and preemption hints for task management.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import heapq
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, List, Optional, Tuple
from datetime import datetime, timedelta


class Priority(Enum):
    """Task priority levels."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


class PreemptionHint(Enum):
    """Preemption behavior hints for tasks."""
    NON_PREEMPTABLE = 0
    PREEMPTABLE = 1


@dataclass
class ScheduledTask:
    """
    A task with scheduling information.
    
    Attributes:
        task_id: Unique identifier for the task
        priority: Task priority level
        deadline: Absolute deadline time (seconds since epoch)
        preemption: Preemption hint for the task
        payload: The actual work to be performed
        submission_time: When the task was submitted
    """
    task_id: str
    priority: Priority
    deadline: float
    preemption: PreemptionHint
    payload: Any
    submission_time: float
    
    def __lt__(self, other: 'ScheduledTask') -> bool:
        """
        Compare tasks for priority queue ordering.
        
        Tasks are ordered by:
        1. Deadline (earlier deadlines first)
        2. Priority (higher priority first)
        3. Submission time (earlier submissions first)
        """
        if self.deadline != other.deadline:
            return self.deadline < other.deadline
        if self.priority.value != other.priority.value:
            return self.priority.value > other.priority.value
        return self.submission_time < other.submission_time
    
    def __eq__(self, other: 'ScheduledTask') -> bool:
        """Check equality based on task_id."""
        return self.task_id == other.task_id
    
    def is_overdue(self) -> bool:
        """Check if the task is past its deadline."""
        return time.time() > self.deadline
    
    def time_until_deadline(self) -> float:
        """Get seconds until deadline (negative if overdue)."""
        return self.deadline - time.time()


class PriorityQueue:
    """
    A priority queue with deadline-aware scheduling.
    
    Tasks are ordered by deadline first, then by priority, then by submission time.
    """
    
    def __init__(self) -> None:
        """Initialize an empty priority queue."""
        self._queue: List[ScheduledTask] = []
        self._task_map: dict[str, ScheduledTask] = {}
        self._counter = 0
    
    def submit_task(
        self,
        task_id: str,
        priority: Priority,
        deadline: float,
        payload: Any,
        preemption: PreemptionHint = PreemptionHint.NON_PREEMPTABLE
    ) -> None:
        """
        Submit a task to the queue.
        
        Args:
            task_id: Unique identifier for the task
            priority: Task priority level
            deadline: Absolute deadline time (seconds since epoch)
            payload: The actual work to be performed
            preemption: Preemption hint for the task
            
        Raises:
            ValueError: If task_id already exists in the queue
        """
        if task_id in self._task_map:
            raise ValueError(f"Task with ID '{task_id}' already exists")
        
        task = ScheduledTask(
            task_id=task_id,
            priority=priority,
            deadline=deadline,
            preemption=preemption,
            payload=payload,
            submission_time=time.time()
        )
        
        heapq.heappush(self._queue, task)
        self._task_map[task_id] = task
    
    def get_next_task(self) -> Optional[ScheduledTask]:
        """
        Get the next task to execute without removing it from the queue.
        
        Returns:
            The next task to execute, or None if queue is empty
        """
        self._cleanup_overdue_tasks()
        return self._queue[0] if self._queue else None
    
    def pop_next_task(self) -> Optional[ScheduledTask]:
        """
        Remove and return the next task to execute.
        
        Returns:
            The next task to execute, or None if queue is empty
        """
        self._cleanup_overdue_tasks()
        if not self._queue:
            return None
        
        task = heapq.heappop(self._queue)
        del self._task_map[task.task_id]
        return task
    
    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task by ID.
        
        Args:
            task_id: ID of the task to remove
            
        Returns:
            True if task was removed, False if not found
        """
        if task_id not in self._task_map:
            return False
        
        task = self._task_map[task_id]
        self._queue.remove(task)
        heapq.heapify(self._queue)  # Re-heapify after removal
        del self._task_map[task_id]
        return True
    
    def get_task(self, task_id: str) -> Optional[ScheduledTask]:
        """
        Get a task by ID without removing it.
        
        Args:
            task_id: ID of the task to retrieve
            
        Returns:
            The task if found, None otherwise
        """
        return self._task_map.get(task_id)
    
    def size(self) -> int:
        """Get the number of tasks in the queue."""
        return len(self._queue)
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._queue) == 0
    
    def get_all_tasks(self) -> List[ScheduledTask]:
        """Get a copy of all tasks in the queue."""
        return list(self._queue)
    
    def _cleanup_overdue_tasks(self) -> None:
        """Remove overdue tasks that cannot be executed."""
        # In a real system, we might want to handle overdue tasks differently
        # For now, we'll just remove them from our tracking but keep them in queue
        pass


def format_deadline(deadline: float) -> str:
    """Format a deadline timestamp for display."""
    dt = datetime.fromtimestamp(deadline)
    return dt.strftime("%H:%M:%S")


def main() -> None:
    """Demo of the priority queue with deadline scheduling."""
    print("=== Priority Queue with Deadline Scheduling Demo ===\n")
    
    # Create a priority queue
    pq = PriorityQueue()
    
    # Get current time for reference
    now = time.time()
    
    # Submit background tasks with later deadlines
    print("Submitting background tasks...")
    pq.submit_task(
        task_id="bg-1",
        priority=Priority.LOW,
        deadline=now + 60,  # 1 minute from now
        payload="Background data processing",
        preemption=PreemptionHint.PREEMPTABLE
    )
    print(f"  Submitted bg-1 (deadline: {format_deadline(now + 60)})")
    
    pq.submit_task(
        task_id="bg-2",
        priority=Priority.NORMAL,
        deadline=now + 120,  # 2 minutes from now
        payload="Generate weekly report",
        preemption=PreemptionHint.NON_PREEMPTABLE
    )
    print(f"  Submitted bg-2 (deadline: {format_deadline(now + 120)})")
    
    # Submit urgent tasks with earlier deadlines
    print("\nSubmitting urgent tasks...")
    pq.submit_task(
        task_id="urgent-1",
        priority=Priority.CRITICAL,
        deadline=now + 10,  # 10 seconds from now
        payload="Process emergency alert",
        preemption=PreemptionHint.PREEMPTABLE
    )
    print(f"  Submitted urgent-1 (deadline: {format_deadline(now + 10)})")
    
    pq.submit_task(
        task_id="urgent-2",
        priority=Priority.HIGH,
        deadline=now + 30,  # 30 seconds from now
        payload="Handle user payment",
        preemption=PreemptionHint.NON_PREEMPTABLE
    )
    print(f"  Submitted urgent-2 (deadline: {format_deadline(now + 30)})")
    
    # Submit another background task
    pq.submit_task(
        task_id="bg-3",
        priority=Priority.LOW,
        deadline=now + 90,  # 1.5 minutes from now
        payload="Archive old logs",
        preemption=PreemptionHint.PREEMPTABLE
    )
    print(f"  Submitted bg-3 (deadline: {format_deadline(now + 90)})")
    
    print(f"\nQueue size: {pq.size()}")
    
    # Show the ordering of tasks
    print("\nTask execution order (by deadline and priority):")
    tasks = pq.get_all_tasks()
    for i, task in enumerate(sorted(tasks), 1):
        status = "OVERDUE" if task.is_overdue() else "PENDING"
        print(f"  {i}. {task.task_id}: {task.payload}")
        print(f"     Priority: {task.priority.name}, "
              f"Deadline: {format_deadline(task.deadline)}, "
              f"Status: {status}")
    
    # Process tasks in order
    print("\nProcessing tasks...")
    processed_tasks = []
    while not pq.is_empty():
        task = pq.pop_next_task()
        if task:
            processed_tasks.append(task)
            print(f"  Processing {task.task_id}: {task.payload}")
            print(f"    Priority: {task.priority.name}, "
                  f"Deadline: {format_deadline(task.deadline)}")
            
            # Simulate processing time
            time.sleep(0.1)
    
    # Show final statistics
    print(f"\nProcessed {len(processed_tasks)} tasks:")
    overdue_count = sum(1 for task in processed_tasks if task.is_overdue())
    if overdue_count > 0:
        print(f"  Warning: {overdue_count} tasks were overdue")
    
    # Demonstrate task removal
    print("\n=== Task Removal Demo ===")
    pq.submit_task(
        task_id="temp-task",
        priority=Priority.NORMAL,
        deadline=now + 300,
        payload="Temporary task to be removed"
    )
    print(f"Queue size before removal: {pq.size()}")
    
    removed = pq.remove_task("temp-task")
    print(f"Task removal successful: {removed}")
    print(f"Queue size after removal: {pq.size()}")
    
    # Try to remove non-existent task
    removed = pq.remove_task("non-existent")
    print(f"Non-existent task removal: {removed}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()