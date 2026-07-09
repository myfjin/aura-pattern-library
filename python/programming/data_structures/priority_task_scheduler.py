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
    """Demo the priority queue scheduler with 20 tasks."""
    print("Priority Queue Scheduler Demo")
    print("=" * 40)
    
    # Create scheduler and add tasks
    scheduler = PriorityQueueScheduler()
    tasks = _create_demo_tasks()
    
    print(f"Adding {len(tasks)} tasks to scheduler...")
    for task in tasks:
        scheduler.add_task(task)
    
    print(f"Tasks in queue: {scheduler.size()}")
    print("\nTop 5 tasks by priority:")
    top_tasks = scheduler.peek_tasks(5)
    for i, task in enumerate(top_tasks, 1):
        overdue = " (OVERDUE)" if task.is_overdue() else ""
        print(f"{i}. [{task.priority}] {task.id}: {task.description} "
              f"(Deadline: {task.deadline.strftime('%H:%M:%S')}){overdue}")
    
    print("\nProcessing tasks in priority order:")
    processed = 0
    while not scheduler.is_empty() and processed < 10:
        task = scheduler.pop_next_task()
        if task:
            overdue = " (OVERDUE)" if task.is_overdue() else ""
            print(f"Processing: [{task.priority}] {task.id}: {task.description}{overdue}")
            processed += 1
    
    print(f"\nRemaining tasks: {scheduler.size()}")
    
    # Demonstrate task removal
    print("\nRemoving task_08...")
    removed = scheduler.remove_task("task_08")
    print(f"Removal successful: {removed}")
    print(f"Tasks remaining: {scheduler.size()}")
    
    # Show new top task
    next_task = scheduler.get_next_task()
    if next_task:
        print(f"Next task: [{next_task.priority}] {next_task.id}: {next_task.description}")


if __name__ == "__main__":
    main()