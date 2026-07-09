#!/usr/bin/env python3
"""
A simple job scheduler with cron-like expressions.
Supports minute, hour, day of month, month, and day of week fields.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
import time
from datetime import datetime, timedelta
from typing import List, Optional, Callable, Dict, Any
from dataclasses import dataclass
from enum import IntEnum


class DayOfWeek(IntEnum):
    """Day of week enumeration (0-6, Sunday=0)."""
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


@dataclass
class Job:
    """Represents a scheduled job."""
    name: str
    cron_expression: str
    func: Callable[[], None]
    args: tuple = ()
    kwargs: Dict[str, Any] = None
    last_run: Optional[datetime] = None
    next_run: Optional[datetime] = None
    is_running: bool = False
    
    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}


class CronParser:
    """Parses cron expressions and calculates next run times."""
    
    # Field positions: minute, hour, day of month, month, day of week
    FIELD_RANGES = [
        (0, 59),    # minute
        (0, 23),    # hour
        (1, 31),    # day of month
        (1, 12),    # month
        (0, 6)      # day of week (0-6, Sunday=0)
    ]
    
    MONTH_NAMES = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
        'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
        'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    DAY_NAMES = {
        'sun': 0, 'mon': 1, 'tue': 2, 'wed': 3,
        'thu': 4, 'fri': 5, 'sat': 6
    }
    
    def __init__(self, cron_expression: str):
        """Initialize with a cron expression."""
        self.expression = cron_expression.strip()
        self.parts = self.expression.split()
        
        if len(self.parts) != 5:
            raise ValueError(f"Invalid cron expression: {cron_expression}. Must have 5 fields.")
    
    def _parse_field(self, field: str, min_val: int, max_val: int) -> List[int]:
        """Parse a single cron field into a list of valid values."""
        if field == '*':
            return list(range(min_val, max_val + 1))
        
        values = set()
        parts = field.split(',')
        
        for part in parts:
            if '/' in part:
                base, step = part.split('/')
                step = int(step)
                
                if base == '*':
                    values.update(range(min_val, max_val + 1, step))
                else:
                    base_val = self._parse_single_value(base, min_val, max_val)
                    values.update(range(base_val, max_val + 1, step))
            elif '-' in part:
                start, end = part.split('-')
                start_val = self._parse_single_value(start, min_val, max_val)
                end_val = self._parse_single_value(end, min_val, max_val)
                values.update(range(start_val, end_val + 1))
            else:
                values.add(self._parse_single_value(part, min_val, max_val))
        
        # Filter to valid range and sort
        result = [v for v in values if min_val <= v <= max_val]
        return sorted(result)
    
    def _parse_single_value(self, value: str, min_val: int, max_val: int) -> int:
        """Parse a single value, handling names."""
        value = value.lower()
        
        # Handle month names
        if min_val == 1 and max_val == 12 and value in self.MONTH_NAMES:
            return self.MONTH_NAMES[value]
        
        # Handle day names
        if min_val == 0 and max_val == 6 and value in self.DAY_NAMES:
            return self.DAY_NAMES[value]
        
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid value in cron expression: {value}")
    
    def get_next_run(self, start_time: datetime = None) -> datetime:
        """Calculate the next run time after start_time."""
        if start_time is None:
            start_time = datetime.now()
        
        # Parse all fields
        minute_values = self._parse_field(self.parts[0], *self.FIELD_RANGES[0])
        hour_values = self._parse_field(self.parts[1], *self.FIELD_RANGES[1])
        day_values = self._parse_field(self.parts[2], *self.FIELD_RANGES[2])
        month_values = self._parse_field(self.parts[3], *self.FIELD_RANGES[3])
        dow_values = self._parse_field(self.parts[4], *self.FIELD_RANGES[4])
        
        # Start from the next minute
        check_time = start_time.replace(second=0, microsecond=0) + timedelta(minutes=1)
        
        # Try up to 2 years (to handle edge cases)
        for _ in range(2 * 365 * 24 * 60):
            # Check if this time matches the cron expression
            if (check_time.minute in minute_values and
                check_time.hour in hour_values and
                check_time.month in month_values and
                check_time.day in day_values):
                
                # If day of week is specified and doesn't match, skip
                if self.parts[4] != '*' and check_time.weekday() not in dow_values:
                    check_time += timedelta(days=1)
                    check_time = check_time.replace(hour=0, minute=0)
                    continue
                
                return check_time
            
            # Move to next minute
            check_time += timedelta(minutes=1)
            
            # Optimization: if we've moved to a new day, reset to start of day
            if check_time.hour == 0 and check_time.minute == 0:
                # Check if this day could possibly match
                if (check_time.month not in month_values or 
                    check_time.day not in day_values):
                    # Skip to next valid day
                    check_time += timedelta(days=1)
        
        raise RuntimeError("Could not find next run time within 2 years")


class Scheduler:
    """Main scheduler class that manages jobs."""
    
    def __init__(self):
        """Initialize the scheduler."""
        self.jobs: List[Job] = []
        self._running = False
    
    def add_job(self, name: str, cron_expression: str, func: Callable, 
                args: tuple = (), kwargs: Dict[str, Any] = None) -> Job:
        """Add a job to the scheduler."""
        if kwargs is None:
            kwargs = {}
            
        job = Job(name, cron_expression, func, args, kwargs)
        self.jobs.append(job)
        self._update_job_next_run(job)
        return job
    
    def remove_job(self, job: Job) -> None:
        """Remove a job from the scheduler."""
        if job in self.jobs:
            self.jobs.remove(job)
    
    def _update_job_next_run(self, job: Job) -> None:
        """Update the next run time for a job."""
        try:
            parser = CronParser(job.cron_expression)
            job.next_run = parser.get_next_run(job.last_run)
        except Exception as e:
            raise ValueError(f"Invalid cron expression for job '{job.name}': {e}")
    
    def get_due_jobs(self, now: datetime = None) -> List[Job]:
        """Get all jobs that are due to run."""
        if now is None:
            now = datetime.now()
        
        due_jobs = []
        for job in self.jobs:
            if job.next_run and not job.is_running and job.next_run <= now:
                due_jobs.append(job)
        
        return due_jobs
    
    def run_due_jobs(self) -> None:
        """Run all jobs that are due."""
        now = datetime.now()
        due_jobs = self.get_due_jobs(now)
        
        for job in due_jobs:
            self._run_job(job, now)
    
    def _run_job(self, job: Job, run_time: datetime) -> None:
        """Execute a single job."""
        job.is_running = True
        job.last_run = run_time
        
        try:
            job.func(*job.args, **job.kwargs)
        except Exception as e:
            # In a real implementation, you might want to log this
            pass
        finally:
            job.is_running = False
            self._update_job_next_run(job)
    
    def get_overdue_jobs(self, threshold_minutes: int = 5) -> List[Job]:
        """Get jobs that are overdue by more than threshold_minutes."""
        now = datetime.now()
        threshold = now - timedelta(minutes=threshold_minutes)
        
        overdue = []
        for job in self.jobs:
            if (job.next_run and 
                job.next_run < threshold and 
                not job.is_running):
                overdue.append(job)
        
        return overdue


def demo_function(name: str) -> None:
    """Demo function to be scheduled."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Executing job: {name}")


def main():
    """Demo the scheduler functionality."""
    scheduler = Scheduler()
    
    # Add various jobs
    scheduler.add_job("every_minute", "* * * * *", demo_function, args=("Every minute",))
    scheduler.add_job("every_5_minutes", "*/5 * * * *", demo_function, args=("Every 5 minutes",))
    scheduler.add_job("daily_at_noon", "0 12 * * *", demo_function, args=("Daily at noon",))
    scheduler.add_job("weekdays_9am", "0 9 * * 1-5", demo_function, args=("Weekdays at 9am",))
    
    print("Scheduler demo started. Press Ctrl+C to stop.")
    print("Jobs:")
    for job in scheduler.jobs:
        if job.next_run:
            print(f"  {job.name}: next run at {job.next_run.strftime('%Y-%m-%d %H:%M')}")
    
    # Run for a short time to demonstrate functionality
    start_time = time.time()
    while time.time() - start_time < 10:  # Run for 10 seconds
        scheduler.run_due_jobs()
        
        # Check for overdue jobs
        overdue = scheduler.get_overdue_jobs(1)
        if overdue:
            print(f"Overdue jobs: {[job.name for job in overdue]}")
        
        time.sleep(0.5)  # Check every 500ms
    
    print("Demo completed.")


if __name__ == "__main__":
    main()