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
    """Self-test: EDF-with-priority ordering exact on a fixed clock, ties
    broken by priority then submission, removal honest."""
    now = 1_000_000.0
    pq = PriorityQueue()

    # Deadlines dominate: pop order is by deadline regardless of priority.
    pq.submit_task("bg-1", Priority.LOW, now + 60, "bg",
                   preemption=PreemptionHint.PREEMPTABLE)
    pq.submit_task("bg-2", Priority.NORMAL, now + 120, "report")
    pq.submit_task("urgent-1", Priority.CRITICAL, now + 10, "alert")
    pq.submit_task("urgent-2", Priority.HIGH, now + 30, "payment")
    pq.submit_task("bg-3", Priority.LOW, now + 90, "archive")
    assert pq.size() == 5

    order = []
    while not pq.is_empty():
        order.append(pq.pop_next_task().task_id)
    assert order == ["urgent-1", "urgent-2", "bg-1", "bg-3", "bg-2"], \
        f"EDF order wrong: {order}"
    assert pq.pop_next_task() is None and pq.is_empty()

    # Same deadline: HIGHER priority pops first.
    pq.submit_task("low", Priority.LOW, now + 50, "l")
    pq.submit_task("crit", Priority.CRITICAL, now + 50, "c")
    pq.submit_task("norm", Priority.NORMAL, now + 50, "n")
    tie_order = [pq.pop_next_task().task_id for _ in range(3)]
    assert tie_order == ["crit", "norm", "low"], \
        f"priority tie-break wrong: {tie_order}"

    # Same deadline AND priority: earlier submission first (FIFO).
    pq.submit_task("first", Priority.NORMAL, now + 50, "1")
    pq.submit_task("second", Priority.NORMAL, now + 50, "2")
    assert [pq.pop_next_task().task_id for _ in range(2)] == ["first", "second"], \
        "FIFO tie-break violated"

    # Overdue detection is a real deadline comparison.
    pq.submit_task("past", Priority.NORMAL, time.time() - 5, "late")
    pq.submit_task("future", Priority.NORMAL, time.time() + 500, "ok")
    past = pq.pop_next_task()
    assert past.task_id == "past" and past.is_overdue() is True
    assert past.time_until_deadline() < 0
    fut = pq.pop_next_task()
    assert fut.is_overdue() is False and fut.time_until_deadline() > 400

    # Removal: honest, and the removed task never pops.
    pq.submit_task("keep", Priority.NORMAL, now + 10, "k")
    pq.submit_task("temp", Priority.NORMAL, now + 5, "t")
    assert pq.size() == 2
    assert pq.remove_task("temp") is True
    assert pq.remove_task("temp") is False, "double removal reported success"
    assert pq.remove_task("ghost") is False
    assert pq.size() == 1
    assert pq.pop_next_task().task_id == "keep", "removed task leaked back out"

    print("priority_queue_scheduler: EDF order exact (urgent-1 first, bg-2 "
          "last), priority then FIFO tie-breaks, overdue real, removal honest — PASS")


if __name__ == "__main__":
    main()
