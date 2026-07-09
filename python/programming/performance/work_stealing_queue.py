"""
Work-Stealing Queue Implementation

A thread-safe work-stealing queue system where workers can steal tasks from
other workers when their local queues are empty.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import threading
import time
import random
from collections import deque
from typing import Any, Optional, List, Callable
from contextlib import contextmanager


class WorkStealingQueue:
    """
    A thread-safe work-stealing queue that allows workers to steal tasks
    from other workers when their local queue is empty.
    """
    
    def __init__(self, num_workers: int = 4):
        """
        Initialize the work-stealing queue system.
        
        Args:
            num_workers: Number of worker threads to create
        """
        self.num_workers = num_workers
        self.workers: List[Worker] = []
        self.global_queue: deque = deque()
        self.lock = threading.RLock()
        self.task_counter = 0
        self.completed_tasks = 0
        self.completed_lock = threading.Lock()
        
        # Create workers
        for i in range(num_workers):
            worker = Worker(f"Worker-{i}", self)
            self.workers.append(worker)
    
    def add_task(self, task: Any) -> None:
        """
        Add a task to the global queue.
        
        Args:
            task: Task to be added to the queue
        """
        with self.lock:
            self.global_queue.append(task)
            self.task_counter += 1
    
    def get_global_task(self) -> Optional[Any]:
        """
        Get a task from the global queue.
        
        Returns:
            A task from the global queue or None if empty
        """
        with self.lock:
            if self.global_queue:
                return self.global_queue.popleft()
            return None
    
    def steal_task(self, thief_worker_id: int) -> Optional[Any]:
        """
        Attempt to steal a task from another worker.
        
        Args:
            thief_worker_id: ID of the worker attempting to steal
            
        Returns:
            Stolen task or None if no tasks available to steal
        """
        # Try to steal from a random worker first
        victim_indices = list(range(self.num_workers))
        random.shuffle(victim_indices)
        
        for victim_index in victim_indices:
            if victim_index == thief_worker_id:
                continue
                
            task = self.workers[victim_index].steal()
            if task is not None:
                return task
        
        return None
    
    def task_completed(self) -> None:
        """Mark a task as completed."""
        with self.completed_lock:
            self.completed_tasks += 1
    
    def get_completed_count(self) -> int:
        """Get the number of completed tasks."""
        with self.completed_lock:
            return self.completed_tasks
    
    def get_total_tasks(self) -> int:
        """Get the total number of tasks added."""
        with self.lock:
            return self.task_counter
    
    def start_workers(self) -> None:
        """Start all worker threads."""
        for worker in self.workers:
            worker.start()
    
    def stop_workers(self) -> None:
        """Signal all workers to stop."""
        for worker in self.workers:
            worker.stop()
    
    def wait_for_completion(self) -> None:
        """Wait for all workers to finish processing."""
        for worker in self.workers:
            worker.join()


class Worker(threading.Thread):
    """
    Worker thread that processes tasks from its local queue and can steal
    tasks from other workers.
    """
    
    def __init__(self, name: str, queue_system: WorkStealingQueue):
        """
        Initialize a worker.
        
        Args:
            name: Name of the worker
            queue_system: Reference to the work-stealing queue system
        """
        super().__init__(name=name)
        self.name = name
        self.queue_system = queue_system
        self.local_queue: deque = deque()
        self.running = True
        self.processed_count = 0
        
    def run(self) -> None:
        """Main worker loop."""
        while self.running:
            # Try to get a task from local queue
            task = self.get_local_task()
            
            # If local queue is empty, try to get from global queue
            if task is None:
                task = self.queue_system.get_global_task()
            
            # If both queues are empty, try to steal
            if task is None:
                task = self.queue_system.steal_task(int(self.name.split('-')[1]))
            
            # If we have a task, process it
            if task is not None:
                self.process_task(task)
            else:
                # No tasks available, brief pause to avoid busy waiting
                time.sleep(0.001)
    
    def add_task(self, task: Any) -> None:
        """
        Add a task to the worker's local queue.
        
        Args:
            task: Task to add to local queue
        """
        self.local_queue.append(task)
    
    def get_local_task(self) -> Optional[Any]:
        """
        Get a task from the worker's local queue.
        
        Returns:
            A task from local queue or None if empty
        """
        if self.local_queue:
            return self.local_queue.popleft()
        return None
    
    def steal(self) -> Optional[Any]:
        """
        Allow another worker to steal a task from this worker's queue.
        
        Returns:
            Stolen task or None if local queue is empty
        """
        if self.local_queue:
            # Steal from the back of the queue (least recently added)
            return self.local_queue.pop()
        return None
    
    def process_task(self, task: Any) -> None:
        """
        Process a task.
        
        Args:
            task: Task to process
        """
        # Simulate work with a small random delay
        time.sleep(random.uniform(0.001, 0.01))
        self.processed_count += 1
        self.queue_system.task_completed()
    
    def stop(self) -> None:
        """Signal the worker to stop."""
        self.running = False


def example_task_processor(task_id: int) -> str:
    """
    Example task processor function.
    
    Args:
        task_id: ID of the task to process
        
    Returns:
        Result of processing the task
    """
    return f"Processed task {task_id}"


@contextmanager
def work_stealing_context(num_workers: int = 4):
    """
    Context manager for work-stealing queue.
    
    Args:
        num_workers: Number of workers to create
    """
    wsq = WorkStealingQueue(num_workers)
    try:
        yield wsq
    finally:
        wsq.stop_workers()


def main():
    """Demo of the work-stealing queue system."""
    print("Starting work-stealing queue demo...")
    
    # Create work-stealing queue with 3 workers
    wsq = WorkStealingQueue(num_workers=3)
    
    # Add 20 tasks to the system
    for i in range(20):
        wsq.add_task(f"Task-{i}")
    
    print(f"Added {wsq.get_total_tasks()} tasks to the system")
    
    # Start workers
    wsq.start_workers()
    
    # Wait for tasks to complete
    start_time = time.time()
    while wsq.get_completed_count() < wsq.get_total_tasks():
        if time.time() - start_time > 5:  # Timeout after 5 seconds
            print("Timeout waiting for tasks to complete")
            break
        time.sleep(0.1)
    
    # Stop workers
    wsq.stop_workers()
    wsq.wait_for_completion()
    
    # Print results
    completed = wsq.get_completed_count()
    print(f"Completed {completed} tasks")
    
    # Show worker stats
    for worker in wsq.workers:
        print(f"{worker.name} processed {worker.processed_count} tasks")
    
    print("Work-stealing queue demo completed")


if __name__ == "__main__":
    main()