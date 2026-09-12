#!/usr/bin/env python3
"""
Priority Queue Scheduler Module

This module implements a priority queue scheduler that handles tasks with
different priorities and deadlines. Tasks are ordered first by priority,
then by deadline, and finally by insertion order for stability.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import heapq
from dataclasses import dataclass
from typing import Any, List, Optional
from datetime import datetime, timedelta
import time


@dataclass
class Task:
    """
    A task to be scheduled with priority and deadline information.
    
    Attributes:
        id: Unique identifier for the task
        priority: Priority level (lower numbers indicate higher priority)
        deadline: Absolute deadline for task completion
        description: Description of the task
        data: Optional data associated with the task
    """
    id: str
    priority: int
    deadline: datetime
    description: str = ""
    data: Any = None
    _insertion_time: float = 0.0
    _sequence: int = 0

    def __lt__(self, other: 'Task') -> bool:
        """
        Define ordering for tasks in the priority queue.
        
        Ordering rules:
        1. Lower priority number comes first
        2. Earlier deadline comes first
        3. Earlier insertion time comes first (for stability)
        """
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.deadline != other.deadline:
            return self.deadline < other.deadline
        return (self._insertion_time, self._sequence) < (other._insertion_time, other._sequence)

    def __eq__(self, other: 'Task') -> bool:
        """Check equality based on all attributes."""
        return (self.id == other.id and 
                self.priority == other.priority and 
                self.deadline == other.deadline and
                self.description == other.description and
                self.data == other.data)

    def is_overdue(self) -> bool:
        """Check if the task is past its deadline."""
        return datetime.now() > self.deadline

    def time_until_deadline(self) -> timedelta:
        """Get the time remaining until the deadline."""
        return self.deadline - datetime.now()


class PriorityQueueScheduler:
    """
    A priority queue scheduler that manages tasks based on priority and deadlines.
    
    Tasks are ordered by priority first, then by deadline, and finally by
    insertion order for stability.
    """
    
    def __init__(self) -> None:
        """Initialize an empty priority queue scheduler."""
        self._queue: List[Task] = []
        self._task_count = 0
        self._sequence_number = 0

    def add_task(self, task: Task) -> None:
        """
        Add a task to the scheduler.
        
        Args:
            task: The task to add to the scheduler
            
        Raises:
            TypeError: If task is not a Task instance
        """
        if not isinstance(task, Task):
            raise TypeError("Task must be an instance of Task class")
            
        task._insertion_time = time.time()
        task._sequence = self._sequence_number
        self._sequence_number += 1
        
        heapq.heappush(self._queue, task)
        self._task_count += 1

    def get_next_task(self) -> Optional[Task]:
        """
        Get the highest priority task without removing it from the queue.
        
        Returns:
            The highest priority task or None if queue is empty
        """
        if not self._queue:
            return None
        return self._queue[0]

    def pop_next_task(self) -> Optional[Task]:
        """
        Remove and return the highest priority task from the queue.
        
        Returns:
            The highest priority task or None if queue is empty
        """
        if not self._queue:
            return None
        task = heapq.heappop(self._queue)
        self._task_count -= 1
        return task

    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task by its ID from the queue.
        
        Args:
            task_id: The ID of the task to remove
            
        Returns:
            True if task was found and removed, False otherwise
        """
        for i, task in enumerate(self._queue):
            if task.id == task_id:
                # Remove the task and re-heapify
                self._queue.pop(i)
                heapq.heapify(self._queue)
                self._task_count -= 1
                return True
        return False

    def peek_tasks(self, n: int = 5) -> List[Task]:
        """
        Peek at the top N tasks without removing them.
        
        Args:
            n: Number of tasks to peek at
            
        Returns:
            List of the top N tasks
        """
        # Return a sorted copy of the queue (without modifying it)
        return sorted(self._queue)[:n]

    def size(self) -> int:
        """Get the number of tasks in the queue."""
        return self._task_count

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._task_count == 0

    def clear(self) -> None:
        """Remove all tasks from the queue."""
        self._queue.clear()
        self._task_count = 0


def _create_demo_tasks() -> List[Task]:
    """Create a list of demo tasks for testing."""
    now = datetime.now()
    tasks = []
    
    # Create 20 tasks with varying priorities and deadlines
    task_data = [
        ("task_01", 1, now + timedelta(minutes=30), "Critical security update"),
        ("task_02", 3, now + timedelta(hours=2), "Generate monthly report"),
        ("task_03", 2, now + timedelta(minutes=45), "Database backup"),
        ("task_04", 1, now + timedelta(minutes=15), "System reboot"),
        ("task_05", 4, now + timedelta(hours=1), "Send notification emails"),
        ("task_06", 2, now + timedelta(minutes=20), "Process user uploads"),
        ("task_07", 3, now + timedelta(minutes=90), "Update documentation"),
        ("task_08", 1, now + timedelta(minutes=5), "Emergency fix"),
        ("task_09", 5, now + timedelta(hours=3), "Clean up temporary files"),
        ("task_10", 2, now + timedelta(minutes=60), "Sync with external API"),
        ("task_11", 4, now + timedelta(minutes=30), "Run data validation"),
        ("task_12", 3, now + timedelta(minutes=75), "Compile performance metrics"),
        ("task_13", 1, now + timedelta(minutes=10), "Fix critical bug"),
        ("task_14", 5, now + timedelta(hours=2), "Archive old logs"),
        ("task_15", 2, now + timedelta(minutes=40), "Update user permissions"),
        ("task_16", 4, now + timedelta(minutes=20), "Send daily digest"),
        ("task_17", 3, now + timedelta(minutes=60), "Optimize database queries"),
        ("task_18", 1, now + timedelta(minutes=2), "System failure recovery"),
        ("task_19", 5, now + timedelta(minutes=45), "Update configuration files"),
        ("task_20", 2, now + timedelta(minutes=35), "Process batch jobs"),
    ]
    
    for task_id, priority, deadline, description in task_data:
        tasks.append(Task(
            id=task_id,
            priority=priority,
            deadline=deadline,
            description=description
        ))
    
    return tasks


def main() -> None:
    """Self-test: exact pop order (priority → deadline → FIFO), peek purity,
    mid-heap removal integrity, and a 300-task sorted-oracle drain."""
    import random
    random.seed(42)
    base = datetime(2030, 1, 1, 12, 0)

    # Exact ordering: priority wins, then earlier deadline, then insertion.
    s = PriorityQueueScheduler()
    s.add_task(Task("low", 3, base + timedelta(minutes=9), "low prio"))
    s.add_task(Task("p1_late", 1, base + timedelta(minutes=5), "p1 later deadline"))
    s.add_task(Task("mid", 2, base + timedelta(minutes=1), "mid prio"))
    s.add_task(Task("p1_soon", 1, base + timedelta(minutes=1), "p1 sooner deadline"))
    assert s.size() == 4
    order = [s.pop_next_task().id for _ in range(4)]
    assert order == ["p1_soon", "p1_late", "mid", "low"], f"pop order wrong: {order}"
    assert s.pop_next_task() is None and s.is_empty()

    # FIFO tie-break: identical priority AND deadline → insertion order.
    for name in ("first", "second", "third"):
        s.add_task(Task(name, 2, base, "tie"))
    assert [s.pop_next_task().id for _ in range(3)] == ["first", "second", "third"], \
        "FIFO tie-break violated"

    # peek/get_next are pure: they must not consume.
    s.add_task(Task("a", 2, base, ""))
    s.add_task(Task("b", 1, base, ""))
    top2 = s.peek_tasks(2)
    assert [t.id for t in top2] == ["b", "a"] and s.size() == 2, "peek consumed tasks"
    assert s.get_next_task().id == "b" and s.size() == 2

    # Mid-heap removal keeps the heap ordered.
    s.add_task(Task("c", 3, base, ""))
    assert s.remove_task("b") is True
    assert s.remove_task("b") is False, "double removal reported success"
    assert s.remove_task("ghost") is False
    assert [s.pop_next_task().id for _ in range(2)] == ["a", "c"], \
        "heap order broken after mid-heap removal"

    # is_overdue is a real deadline check.
    past = Task("late", 1, datetime(2000, 1, 1), "")
    future = Task("ok", 1, datetime(2100, 1, 1), "")
    assert past.is_overdue() is True and future.is_overdue() is False

    # Refusal: only Task instances enter the queue.
    try:
        s.add_task("not a task")  # type: ignore[arg-type]
        assert False, "non-Task accepted"
    except TypeError:
        pass

    # Oracle drain: 300 random tasks pop out exactly in sorted(Task) order.
    tasks = [Task(f"t{i}", random.randint(1, 5),
                  base + timedelta(minutes=random.randint(0, 500)), "")
             for i in range(300)]
    big = PriorityQueueScheduler()
    for t in tasks:
        big.add_task(t)
    drained = []
    while not big.is_empty():
        drained.append(big.pop_next_task())
    assert len(drained) == 300
    assert drained == sorted(tasks), "drain order diverged from the comparator oracle"
    priorities = [t.priority for t in drained]
    assert priorities == sorted(priorities), "priorities not non-decreasing in drain"

    print("priority_task_scheduler: pop order exact, FIFO ties, peek pure, "
          "mid-heap removal safe, 300-task drain == sorted oracle — PASS")


if __name__ == "__main__":
    main()