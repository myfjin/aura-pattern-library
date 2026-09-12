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
                
                # If day of week is specified and doesn't match, skip.
                # Python weekday() is Monday=0; cron (and DAY_NAMES above) is Sunday=0.
                cron_dow = (check_time.weekday() + 1) % 7
                if self.parts[4] != '*' and cron_dow not in dow_values:
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


def main():
    """Self-test: exact next-fire times from a fixed clock (2024-01-01 was a Monday)."""
    base = datetime(2024, 1, 1, 10, 30)  # Monday

    # Field parsing is exact.
    p = CronParser("*/15 * * * *")
    assert p._parse_field("*/15", 0, 59) == [0, 15, 30, 45]
    assert p._parse_field("1-5", 0, 6) == [1, 2, 3, 4, 5]
    assert p._parse_field("jan,jul", 1, 12) == [1, 7]
    assert p._parse_field("fri", 0, 6) == [5]

    # Next-fire arithmetic against planted truths.
    cases = [
        ("* * * * *",    datetime(2024, 1, 1, 10, 31)),   # next minute
        ("*/15 * * * *", datetime(2024, 1, 1, 10, 45)),   # next quarter-hour
        ("0 12 * * *",   datetime(2024, 1, 1, 12, 0)),    # noon today
        ("30 6 15 * *",  datetime(2024, 1, 15, 6, 30)),   # mid-month
        ("0 0 1 feb *",  datetime(2024, 2, 1, 0, 0)),     # month by name
        # THE BUG this test pins: cron dow is Sunday=0, python weekday Monday=0.
        # Weekdays-at-9 from Monday 10:30 must be TUESDAY 9:00 (not Wednesday).
        ("0 9 * * 1-5",  datetime(2024, 1, 2, 9, 0)),
        ("0 9 * * sat",  datetime(2024, 1, 6, 9, 0)),     # named day: Saturday
        ("0 9 * * mon",  datetime(2024, 1, 8, 9, 0)),     # next Monday, a week out
    ]
    for expr, expected in cases:
        got = CronParser(expr).get_next_run(base)
        assert got == expected, f"{expr!r} from {base} must fire {expected}, got {got}"

    # Malformed expressions are refused.
    for bad in ("* * * *", "* * * * * *", "xx * * * *"):
        try:
            CronParser(bad).get_next_run(base)
            assert False, f"cron {bad!r} accepted"
        except ValueError:
            pass

    # Scheduler: a due job runs exactly once, reschedules, and survives a
    # crashing job function (the scheduler must not die with the job).
    sched = Scheduler()
    ran = []
    job = sched.add_job("t", "* * * * *", lambda: ran.append(1))
    boom = sched.add_job("boom", "* * * * *", lambda: 1 / 0)
    for j in (job, boom):
        j.next_run = datetime.now() - timedelta(minutes=1)   # force due
    due = sched.get_due_jobs()
    assert {j.name for j in due} == {"t", "boom"}, f"due set wrong: {[j.name for j in due]}"
    sched.run_due_jobs()
    assert ran == [1], f"due job must run exactly once, ran {len(ran)} times"
    assert not job.is_running and not boom.is_running, "is_running flag stuck after run"
    assert job.next_run > datetime.now(), "job not rescheduled into the future"
    assert sched.get_due_jobs() == [], "jobs still due immediately after running"

    # Invalid cron at add time is refused with the job's name in the error.
    try:
        sched.add_job("bad", "not a cron", lambda: None)
        assert False, "invalid cron accepted by add_job"
    except ValueError as e:
        assert "bad" in str(e)

    print("job_scheduler: 8 exact next-fires (dow Sunday=0 pinned), due-run-once, "
          "crash-isolated, bad cron refused — PASS")


if __name__ == "__main__":
    main()